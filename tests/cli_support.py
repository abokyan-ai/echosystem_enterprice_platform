"""In-process CLI harness with explicit fake service injection and captured streams."""
import io
from bootstrap_contracts.public import HealthStatus, HostState, PlatformConfiguration, PlatformHealth, ModuleHealth
from platform_cli.internal.cli_application import main


class FakeHost:
    def __init__(self, names=("one",), status=HealthStatus.HEALTHY, start_error=None, stop_error=None):
        self.names, self.status = names, status
        self.start_error, self.stop_error = start_error, stop_error
        self.state = HostState.BUILT
        self.events = []

    def start(self):
        self.events.append("start")
        if self.start_error:
            raise self.start_error
        self.state = HostState.RUNNING

    def dispose(self):
        self.events.append("dispose")
        if self.stop_error:
            raise self.stop_error
        self.state = HostState.DISPOSED

    def stop(self):
        self.state = HostState.STOPPED

    def health(self):
        return PlatformHealth(self.state, self.status, self.names, self.names if self.state == HostState.RUNNING else (), (), tuple(ModuleHealth(name, self.status, self.state == HostState.RUNNING) for name in self.names), ())


class FakeServices:
    def __init__(self, host=None, failures=None):
        self.local_host = host or FakeHost()
        self.failures = failures or {}
        self.calls = []
        self.request = None

    def call(self, name, request):
        self.calls.append(name)
        self.request = request
        if name in self.failures:
            raise self.failures[name]

    def repository(self, request):
        self.call("repository", request)
        return {"public_modules": 7}

    def configuration(self, request):
        self.call("configuration", request)
        return PlatformConfiguration(profile=request.profile or "development")

    def architecture(self, request):
        self.call("architecture", request)
        return {"status": "HEALTHY"}

    def host(self, request, configuration, events):
        self.call("host", request)
        return self.local_host

    def describe(self, host):
        return {"startup_order": host.names, "startup_ms": 0.0, "module_startup_ms": {}, "modules": [{"id": name, "dependencies": () if index == 0 else (host.names[index - 1],), "status": host.status, "started": host.state == HostState.RUNNING, "kind": "core"} for index, name in enumerate(host.names)]}


def invoke(*arguments, services=None, registry=None, cancellation=None):
    stdout, stderr = io.StringIO(), io.StringIO()
    code = main(arguments, services=services if services is not None else FakeServices(), stdout=stdout, stderr=stderr, registry=registry, cancellation=cancellation)
    return code, stdout.getvalue(), stderr.getvalue()
