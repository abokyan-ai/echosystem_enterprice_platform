"""Local synchronous lifecycle host. No globals, business behavior or container lookup."""
import copy
import heapq
from time import perf_counter
from types import MappingProxyType
from bootstrap_contracts.public import BootstrapDiagnostic, BootstrapError, HealthStatus, HostState, ModuleHealth, PlatformHealth
from platform_cli.internal.bootstrap_configuration import validate_configuration


def startup_order(registrations):
    graph = {name: registration.requires for name, registration in registrations.items()}
    for name, dependencies in sorted(graph.items()):
        for dependency in dependencies:
            if dependency not in graph:
                raise BootstrapError(BootstrapDiagnostic("BOOT-MOD-002", "Required module is not enabled/registered", name, dependency))
    visited, active = set(), []
    def visit(name):
        if name in active:
            path = tuple(active[active.index(name):] + [name])
            raise BootstrapError(BootstrapDiagnostic("BOOT-CYCLE-001", "Activation dependency cycle", name, path=path))
        if name in visited:
            return
        active.append(name)
        for dependency in sorted(graph[name]):
            visit(dependency)
        active.pop()
        visited.add(name)
    for name in sorted(graph):
        visit(name)
    indegree = {name: len(dependencies) for name, dependencies in graph.items()}
    ready = [name for name, count in indegree.items() if count == 0]
    heapq.heapify(ready)
    order = []
    while ready:
        name = heapq.heappop(ready)
        order.append(name)
        for candidate in sorted(graph):
            if name in graph[candidate]:
                indegree[candidate] -= 1
                if indegree[candidate] == 0:
                    heapq.heappush(ready, candidate)
    return tuple(order)


class BootstrapBuilder:
    def __init__(self, configuration, event_sink=None):
        self.configuration = configuration
        self.registrations = {}
        self.event_sink = event_sink or (lambda event, module: None)

    def add_module(self, registration):
        return self._add(registration, "core")

    def add_adapter(self, registration):
        return self._add(registration, "adapter")

    def _add(self, registration, kind):
        if registration.kind != kind:
            raise BootstrapError(BootstrapDiagnostic("BOOT-MOD-001", "Use the registration method for this module kind", registration.id))
        if registration.id in self.registrations:
            raise BootstrapError(BootstrapDiagnostic("BOOT-MOD-001", "Duplicate module registration", registration.id))
        self.registrations[registration.id] = registration
        return self

    def replace_registration(self, registration):
        if registration.id not in self.registrations:
            raise BootstrapError(BootstrapDiagnostic("BOOT-MOD-002", "Cannot replace an unregistered module", registration.id))
        self.registrations[registration.id] = registration
        return self

    def build(self):
        configuration = validate_configuration(self.configuration)
        enabled = set(self.registrations) if configuration.enabled_modules is None else set(configuration.enabled_modules)
        unknown = enabled - self.registrations.keys()
        if unknown:
            raise BootstrapError(BootstrapDiagnostic("BOOT-MOD-002", "Unknown enabled module", sorted(unknown)[0]))
        if set(configuration.module_settings) - enabled:
            raise BootstrapError(BootstrapDiagnostic("BOOT-CONFIG-001", "Settings reference an unknown/disabled module", setting="module_settings"))
        selected = {name: registration for name, registration in self.registrations.items() if name in enabled}
        order = startup_order(selected)
        # Validate every module before constructing any instance or starting any resource.
        for name in order:
            try:
                selected[name].validate_settings(copy.deepcopy(configuration.module_settings.get(name, {})))
            except Exception as exc:
                raise BootstrapError(BootstrapDiagnostic("BOOT-CONFIG-001", "Module-owned settings validation failed", name, setting="module_settings")) from exc
        instances = {}
        for name in order:
            registration = selected[name]
            dependencies = MappingProxyType({dependency: instances[dependency] for dependency in registration.requires})
            try:
                instance = registration.factory(dependencies, copy.deepcopy(configuration.module_settings.get(name, {})))
                if not all(callable(getattr(instance, method, None)) for method in ("start", "stop", "health")):
                    raise TypeError("Invalid module contract")
                instances[name] = instance
            except Exception as exc:
                # Factories must be side-effect free; resources belong to start/stop.
                raise BootstrapError(BootstrapDiagnostic("BOOT-START-001", "Module construction failed; factories must not allocate resources", name)) from exc
        return LocalPlatformHost(configuration.profile, selected, instances, order, self.event_sink)


class LocalPlatformHost:
    def __init__(self, profile, registrations, instances, order, event_sink):
        self.profile = profile
        self.registrations = dict(registrations)
        self.instances = dict(instances)
        self.order = order
        self.state = HostState.BUILT
        self.started = []
        self._pending_cleanup = []
        self.failed = set()
        self.diagnostics = []
        self.module_startup_ms = {}
        self.startup_ms = 0.0
        self._event_sink = event_sink

    def _emit(self, event, module=None):
        try:
            self._event_sink(event, module)
        except Exception:
            self.diagnostics.append(BootstrapDiagnostic("BOOT-LOG-001", "Lifecycle event sink failed", module))

    def _cleanup(self, names):
        failures = []
        for name in names:
            self._emit("module stopping", name)
            try:
                self.instances[name].stop()
                if name in self._pending_cleanup:
                    self._pending_cleanup.remove(name)
                if name in self.started:
                    self.started.remove(name)
            except Exception:
                self.failed.add(name)
                failures.append(BootstrapDiagnostic("BOOT-STOP-001", "Module cleanup failed", name))
        self.diagnostics.extend(failures)
        return failures

    def start(self):
        if self.state == HostState.RUNNING:
            return
        if self.state != HostState.BUILT:
            raise BootstrapError(BootstrapDiagnostic("BOOT-STATE-001", "Start requires a freshly built host"))
        self.state = HostState.STARTING
        self._emit("platform bootstrap started")
        total = perf_counter()
        try:
            for name in self.order:
                begin = perf_counter()
                self._emit("module starting", name)
                try:
                    self._pending_cleanup.append(name)
                    self.instances[name].start()
                except BaseException as exc:
                    self.failed.add(name)
                    original = BootstrapDiagnostic("BOOT-START-001", "Module startup failed", name)
                    self.diagnostics.append(original)
                    # Include the failing module because start may have allocated partial resources.
                    cleanup = self._cleanup([name, *reversed(self.started)])
                    self.state = HostState.FAILED
                    if isinstance(exc, (KeyboardInterrupt, SystemExit)):
                        raise
                    raise BootstrapError(original, *cleanup) from exc
                self.module_startup_ms[name] = round((perf_counter() - begin) * 1000, 3)
                self.started.append(name)
                self._emit("module started", name)
            self.state = HostState.RUNNING
            self._emit("platform started")
        finally:
            self.startup_ms = round((perf_counter() - total) * 1000, 3)

    def stop(self):
        if self.state in {HostState.STOPPED, HostState.DISPOSED}:
            return
        if self.state in {HostState.STARTING, HostState.STOPPING}:
            raise BootstrapError(BootstrapDiagnostic("BOOT-STATE-001", "Cannot stop during a lifecycle transition"))
        was_failed = self.state == HostState.FAILED
        self.state = HostState.STOPPING
        self._emit("platform stopping")
        failures = self._cleanup(list(reversed(self._pending_cleanup)))
        self.state = HostState.FAILED if failures or was_failed else HostState.STOPPED
        self._emit("platform stopped")
        if failures:
            raise BootstrapError(*failures)

    def dispose(self):
        if self.state == HostState.DISPOSED:
            return
        self.stop()
        self.state = HostState.DISPOSED

    def health(self):
        modules = []
        for name in sorted(self.registrations):
            status = HealthStatus.UNHEALTHY if name in self.failed else HealthStatus.DEGRADED
            if name in self.started and name not in self.failed:
                try:
                    status = HealthStatus(self.instances[name].health())
                except Exception:
                    status = HealthStatus.UNHEALTHY
            modules.append(ModuleHealth(name, status, name in self.started))
        status = HealthStatus.HEALTHY if self.state == HostState.RUNNING else HealthStatus.DEGRADED
        if self.state == HostState.FAILED or any(m.status == HealthStatus.UNHEALTHY for m in modules):
            status = HealthStatus.UNHEALTHY
        elif any(m.status == HealthStatus.DEGRADED for m in modules) or self.diagnostics:
            status = HealthStatus.DEGRADED
        return PlatformHealth(self.state, status, tuple(sorted(self.registrations)), tuple(self.started), tuple(sorted(self.failed)), tuple(modules), tuple(self.diagnostics))
