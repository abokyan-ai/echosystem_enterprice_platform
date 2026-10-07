import json
import tempfile
import unittest
from pathlib import Path
from bootstrap_contracts.public import BootstrapError, HealthStatus, HostState, ModuleRegistration, PlatformConfiguration
from platform_cli.internal.bootstrap_configuration import load_configuration
from platform_cli.internal.bootstrap_host import BootstrapBuilder
from bootstrap_support import FakeModule, TestHost


class BootstrapTests(unittest.TestCase):
    def assert_code(self, code, operation):
        with self.assertRaises(BootstrapError) as caught:
            operation()
        self.assertEqual(caught.exception.diagnostics[0].code, code)
        self.assertNotIn("sensitive", str(caught.exception))
        return caught.exception

    def test_BOOT_TEST_001_empty(self):
        host = TestHost().build()
        host.start()
        self.assertEqual(host.health().status, HealthStatus.HEALTHY)
        host.dispose()
        self.assertEqual(host.state, HostState.DISPOSED)

    def test_BOOT_TEST_002_single(self):
        fixture = TestHost().register("one")
        host = fixture.build()
        host.start()
        host.stop()
        self.assertEqual(fixture.events, [("start", "one"), ("stop", "one")])

    def test_BOOT_TEST_003_order_and_reverse_shutdown(self):
        fixture = TestHost().register("c", ("b",)).register("b", ("a",)).register("a")
        host = fixture.build()
        self.assertEqual(host.order, ("a", "b", "c"))
        host.start()
        host.stop()
        self.assertEqual(fixture.events, [("start", n) for n in ("a", "b", "c")] + [("stop", n) for n in ("c", "b", "a")])

    def test_BOOT_TEST_004_missing_dependency(self):
        fixture = TestHost().register("one", ("missing",))
        error = self.assert_code("BOOT-MOD-002", fixture.build)
        self.assertEqual(error.diagnostics[0].dependency, "missing")
        self.assertEqual(fixture.events, [])

    def test_BOOT_TEST_005_duplicate(self):
        fixture = TestHost().register("one")
        self.assert_code("BOOT-MOD-001", lambda: fixture.register("one"))

    def test_BOOT_TEST_006_cycle_path(self):
        fixture = TestHost().register("a", ("b",)).register("b", ("a",))
        error = self.assert_code("BOOT-CYCLE-001", fixture.build)
        self.assertEqual(error.diagnostics[0].path, ("a", "b", "a"))

    def test_BOOT_TEST_007_start_failure_cleanup(self):
        fixture = TestHost().register("a").register("b", ("a",), fail_start=True).register("c", ("b",))
        host = fixture.build()
        self.assert_code("BOOT-START-001", host.start)
        self.assertEqual(host.state, HostState.FAILED)
        self.assertEqual(fixture.events, [("start", "a"), ("start", "b"), ("stop", "b"), ("stop", "a")])
        self.assertFalse(any(m.active for m in fixture.instances.values()))
        self.assertEqual(host.health().status, HealthStatus.UNHEALTHY)

    def test_BOOT_TEST_008_config_precedence(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "config.json"
            path.write_text(json.dumps({"profile": "production", "enabled_modules": ["a"], "module_settings": {"a": {"x": 1, "retained": 4}}}))
            config = load_configuration(path, {"PLATFORM_PROFILE": "development", "PLATFORM_MODULES": "b", "PLATFORM_MODULE_SETTINGS": '{"a":{"x":2}}'}, {"profile": "test", "enabled_modules": ["a"], "module_settings": {"a": {"x": 3}}})
            self.assertEqual(config.profile, "test")
            self.assertEqual(config.enabled_modules, ("a",))
            self.assertEqual(config.module_settings, {"a": {"x": 3, "retained": 4}})
        self.assertEqual(load_configuration(environment={}).profile, "development")

    def test_BOOT_TEST_009_explicit_override(self):
        fixture = TestHost().register("a")
        replacement = FakeModule("override", fixture.events)
        fixture.override(ModuleRegistration("a", lambda dependencies, settings: replacement))
        host = fixture.build()
        host.start()
        host.dispose()
        self.assertEqual(fixture.events, [("start", "override"), ("stop", "override")])

    def test_BOOT_TEST_010_deterministic_and_isolated(self):
        orders = []
        for names in (("c", "a", "b"), ("b", "c", "a")):
            fixture = TestHost()
            for name in names:
                fixture.register(name)
            host = fixture.build()
            orders.append(host.order)
            host.start()
            host.dispose()
        self.assertEqual(orders, [("a", "b", "c")] * 2)

    def test_shutdown_failure_continues_and_retries_pending_resources(self):
        fixture = TestHost().register("a").register("b", ("a",), fail_stop=True)
        host = fixture.build()
        host.start()
        self.assert_code("BOOT-STOP-001", host.stop)
        self.assertFalse(fixture.instances["a"].active)
        self.assertEqual(host.health().status, HealthStatus.UNHEALTHY)
        fixture.instances["b"].fail_stop = False
        host.dispose()
        self.assertFalse(fixture.instances["b"].active)
        self.assertEqual(host.state, HostState.DISPOSED)

    def test_partial_start_cleanup_failure_retained_for_retry(self):
        fixture = TestHost().register("a").register("b", ("a",), fail_start=True, fail_stop=True)
        host = fixture.build()
        error = self.assert_code("BOOT-START-001", host.start)
        self.assertEqual([d.code for d in error.diagnostics], ["BOOT-START-001", "BOOT-STOP-001"])
        fixture.instances["b"].fail_stop = False
        host.dispose()
        self.assertFalse(fixture.instances["b"].active)

    def test_idempotent_start_stop_dispose_and_illegal_restart(self):
        fixture = TestHost().register("a")
        host = fixture.build()
        host.start()
        host.start()
        host.stop()
        host.stop()
        self.assert_code("BOOT-STATE-001", host.start)
        host.dispose()
        host.dispose()
        self.assertEqual(len(fixture.events), 2)

    def test_stop_before_start_prevents_restart(self):
        host = TestHost().build()
        host.stop()
        self.assert_code("BOOT-STATE-001", host.start)

    def test_unknown_and_disabled_dependency(self):
        self.assert_code("BOOT-MOD-002", TestHost(PlatformConfiguration(enabled_modules=("missing",))).build)
        fixture = TestHost(PlatformConfiguration(enabled_modules=("b",))).register("a").register("b", ("a",))
        self.assert_code("BOOT-MOD-002", fixture.build)

    def test_all_settings_validated_before_factories(self):
        called = []
        builder = BootstrapBuilder(PlatformConfiguration(module_settings={"b": {"invalid": True}}))
        builder.add_module(ModuleRegistration("a", lambda d, s: called.append("a")))
        builder.add_module(ModuleRegistration("b", lambda d, s: called.append("b")))
        self.assert_code("BOOT-CONFIG-001", builder.build)
        self.assertEqual(called, [])

    def test_invalid_configuration_has_diagnostic(self):
        for overrides in ({"profile": []}, {"profile": "unknown"}, {"enabled_modules": ["a", "a"]}, {"unknown": "sensitive"}, {"module_settings": []}):
            self.assert_code("BOOT-CONFIG-001", lambda: load_configuration(environment={}, overrides=overrides))
        self.assert_code("BOOT-CONFIG-001", lambda: load_configuration(environment={"PLATFORM_MODULE_SETTINGS": "invalid"}))
        self.assert_code("BOOT-CONFIG-001", lambda: load_configuration(Path("missing-config.json"), environment={}))

    def test_unknown_module_settings(self):
        fixture = TestHost(PlatformConfiguration(module_settings={"missing": {}})).register("a")
        self.assert_code("BOOT-CONFIG-001", fixture.build)

    def test_explicit_injection_only_declared_dependencies_and_owned_settings(self):
        received = {}
        builder = BootstrapBuilder(PlatformConfiguration(module_settings={"b": {"value": 7}}))
        a = FakeModule("a", [])
        builder.add_module(ModuleRegistration("a", lambda d, s: a))
        builder.add_module(ModuleRegistration("unused", lambda d, s: FakeModule("unused", [])))
        def factory(dependencies, settings):
            received.update(dependencies=dependencies, settings=settings)
            return FakeModule("b", [])
        builder.add_module(ModuleRegistration("b", factory, ("a",), lambda s: None))
        builder.build()
        self.assertEqual(dict(received["dependencies"]), {"a": a})
        self.assertEqual(received["settings"], {"value": 7})
        with self.assertRaises(TypeError):
            received["dependencies"]["unused"] = a

    def test_health_degraded_and_exception(self):
        fixture = TestHost().register("a", status=HealthStatus.DEGRADED)
        host = fixture.build()
        self.assertEqual(host.health().status, HealthStatus.DEGRADED)
        host.start()
        self.assertEqual(host.health().status, HealthStatus.DEGRADED)
        fixture.instances["a"].health = lambda: 1 / 0
        self.assertEqual(host.health().status, HealthStatus.UNHEALTHY)
        host.dispose()

    def test_adapter_registration_and_override_validation(self):
        builder = BootstrapBuilder(PlatformConfiguration())
        adapter = ModuleRegistration("adapter", lambda d, s: FakeModule("adapter", []), kind="adapter")
        self.assert_code("BOOT-MOD-001", lambda: builder.add_module(adapter))
        builder.add_adapter(adapter)
        builder.build().dispose()
        self.assert_code("BOOT-MOD-002", lambda: builder.replace_registration(ModuleRegistration("unknown", lambda d, s: None)))

    def test_event_sink_failure_degrades_without_leaking_resources(self):
        builder = BootstrapBuilder(PlatformConfiguration(), lambda e, m: 1 / 0)
        host = builder.build()
        host.start()
        self.assertEqual(host.health().status, HealthStatus.DEGRADED)
        self.assertEqual(host.health().diagnostics[0].code, "BOOT-LOG-001")
        host.dispose()
