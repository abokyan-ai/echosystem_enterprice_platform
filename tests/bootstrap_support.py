"""Test-only host overrides and resource fakes; never imported by production modules."""
from bootstrap_contracts.public import HealthStatus, ModuleRegistration, PlatformConfiguration
from platform_cli.internal.bootstrap_host import BootstrapBuilder


class FakeModule:
    def __init__(self, name, events, fail_start=False, fail_stop=False, status=HealthStatus.HEALTHY):
        self.name, self.events = name, events
        self.fail_start, self.fail_stop, self.status = fail_start, fail_stop, status
        self.active = False

    def start(self):
        self.events.append(("start", self.name))
        self.active = True
        if self.fail_start:
            raise RuntimeError("sensitive module exception")

    def stop(self):
        self.events.append(("stop", self.name))
        if self.fail_stop:
            raise RuntimeError("sensitive cleanup exception")
        self.active = False

    def health(self):
        return self.status


class TestHost:
    """Each test constructs an isolated host; overrides are explicit registrations."""
    def __init__(self, configuration=None):
        self.events = []
        self.instances = {}
        self.builder = BootstrapBuilder(configuration or PlatformConfiguration(profile="test"))

    def register(self, name, requires=(), **options):
        def factory(dependencies, settings):
            instance = FakeModule(name, self.events, **options)
            self.instances[name] = instance
            return instance
        self.builder.add_module(ModuleRegistration(name, factory, requires))
        return self

    def override(self, registration):
        self.builder.replace_registration(registration)
        return self

    def build(self):
        return self.builder.build()
