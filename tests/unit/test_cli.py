import json
from pathlib import Path
import signal
import threading
import unittest
from unittest.mock import patch
from bootstrap_contracts.public import BootstrapDiagnostic, BootstrapError, HealthStatus
from platform_cli.public import CLI_VERSION, CliDiagnostic, CliError, CommandResult
from platform_cli.internal.cli_registry import CommandDefinition, CommandRegistry
from cli_support import FakeHost, FakeServices, invoke


class CliTests(unittest.TestCase):
    def test_help_discoverable_without_services(self):
        services = FakeServices()
        code, out, err = invoke("--help", services=services)
        self.assertEqual(code, 0)
        for value in ("doctor", "run", "modules", "health", "--output", "Examples:"):
            self.assertIn(value, out)
        self.assertEqual(services.calls, [])
        self.assertEqual(err, "")

    def test_version_flag_and_command_without_configuration(self):
        for arguments in (("--version",), ("version",)):
            services = FakeServices()
            code, out, err = invoke(*arguments, "--output", "json", services=services)
            report = json.loads(out)
            self.assertEqual((code, report["version"], report["schema_version"]), (0, CLI_VERSION, 1))
            self.assertEqual(services.calls, [])
            self.assertEqual(err, "")

    def test_command_help_is_captured(self):
        code, out, err = invoke("run", "--help")
        self.assertEqual(code, 0)
        self.assertIn("--once", out)
        self.assertEqual(err, "")

    def test_global_options_before_and_after_command(self):
        services = FakeServices()
        code, out, err = invoke("--profile", "test", "--root", "..", "modules", "--modules", "a,b", "--output", "json", services=services)
        self.assertEqual(code, 0)
        self.assertEqual(services.request.profile, "test")
        self.assertEqual(services.request.enabled_modules, ("a", "b"))
        self.assertEqual(services.request.root, Path("..").resolve())
        self.assertEqual(json.loads(out)["profile"], "test")

    def test_invalid_inputs_are_code_two_and_structured(self):
        for options in (("unknown",), ("modules", "--bad"), ("health", "--profile", "unknown"), ("modules", "--output", "xml"), ("--verbose", "health", "--quiet"), ("health", "--output", "json", "--format", "text"), ()):
            with self.subTest(options=options):
                code, out, err = invoke("--output", "json", *options)
                self.assertEqual(code, 2)
                self.assertEqual(out, "")
                report = json.loads(err)
                self.assertEqual(report["exit_code"], 2)
                self.assertEqual(report["diagnostics"][0]["code"], "CLI-INPUT-001")
                self.assertNotIn("Traceback", err)

    def test_doctor_independent_checks_all_pass(self):
        services = FakeServices()
        code, out, err = invoke("doctor", "--output", "json", services=services)
        report = json.loads(out)
        self.assertEqual(code, 0)
        self.assertEqual([c["status"] for c in report["checks"]], ["PASS"] * 4)
        self.assertEqual(services.local_host.events, ["dispose"])
        self.assertEqual(err, "")

    def test_doctor_config_failure_skips_graph_but_checks_architecture(self):
        services = FakeServices(failures={"configuration": BootstrapError(BootstrapDiagnostic("BOOT-CONFIG-001", "Invalid configuration"))})
        code, out, err = invoke("doctor", "--output", "json", services=services)
        self.assertEqual(code, 3)
        self.assertEqual([c["status"] for c in json.loads(out)["checks"]], ["PASS", "FAIL", "PASS", "SKIP"])
        self.assertIn("architecture", services.calls)
        self.assertNotIn("host", services.calls)
        self.assertEqual(json.loads(err)["diagnostics"][0]["code"], "BOOT-CONFIG-001")

    def test_doctor_multiple_failures_aggregate_with_stable_priority(self):
        services = FakeServices(failures={"repository": RuntimeError("secret-value"), "architecture": CliError(5, CliDiagnostic("ARCH-CYCLE-001", "Cycle")), "host": BootstrapError(BootstrapDiagnostic("BOOT-MOD-002", "Missing dependency"))})
        code, out, err = invoke("doctor", "--output", "json", services=services)
        self.assertEqual(code, 5)
        self.assertEqual([c["status"] for c in json.loads(out)["checks"]], ["FAIL", "PASS", "FAIL", "FAIL"])
        self.assertEqual(len(json.loads(err)["diagnostics"]), 3)
        self.assertNotIn("secret-value", out + err)

    def test_each_error_category_maps_to_documented_exit(self):
        errors = ((RuntimeError("secret-value"), 1), (BootstrapError(BootstrapDiagnostic("BOOT-CONFIG-001", "Config")), 3), (BootstrapError(BootstrapDiagnostic("BOOT-START-001", "Start")), 4), (CliError(5, CliDiagnostic("ARCH-TEST", "Architecture")), 5))
        for error, expected in errors:
            code, out, err = invoke("modules", "--output", "json", services=FakeServices(failures={"configuration": error}))
            self.assertEqual(code, expected)
            self.assertEqual(out, "")
            self.assertEqual(json.loads(err)["exit_code"], expected)
            self.assertNotIn("secret-value", err)

    def test_run_once_starts_and_disposes_actual_injected_contract(self):
        host = FakeHost()
        code, out, err = invoke("run", "--once", "--output", "json", services=FakeServices(host))
        self.assertEqual(code, 0)
        self.assertEqual(host.events, ["start", "dispose"])
        self.assertEqual(json.loads(out)["health"]["state"], "running")
        self.assertEqual(err, "")

    def test_run_startup_failure_still_disposes(self):
        host = FakeHost(start_error=BootstrapError(BootstrapDiagnostic("BOOT-START-001", "Start failed", "one")))
        code, out, err = invoke("run", "--once", "--output", "json", services=FakeServices(host))
        self.assertEqual(code, 4)
        self.assertEqual(host.events, ["start", "dispose"])
        self.assertEqual(out, "")
        self.assertEqual(json.loads(err)["diagnostics"][0]["context"]["module"], "one")

    def test_run_aggregates_start_and_shutdown_failures(self):
        host = FakeHost(start_error=BootstrapError(BootstrapDiagnostic("BOOT-START-001", "Start failed")), stop_error=BootstrapError(BootstrapDiagnostic("BOOT-STOP-001", "Stop failed")))
        code, out, err = invoke("run", "--once", "--output", "json", services=FakeServices(host))
        self.assertEqual(code, 4)
        self.assertEqual([d["code"] for d in json.loads(err)["diagnostics"]], ["BOOT-START-001", "BOOT-STOP-001"])

    def test_run_once_shutdown_failure_does_not_emit_success(self):
        host = FakeHost(stop_error=BootstrapError(BootstrapDiagnostic("BOOT-STOP-001", "Stop failed")))
        code, out, err = invoke("run", "--once", "--output", "json", services=FakeServices(host))
        self.assertEqual(code, 4)
        self.assertEqual(out, "")
        self.assertIn("BOOT-STOP-001", err)

    def test_persistent_run_explicit_cancellation_restores_handlers(self):
        event = threading.Event()
        event.set()
        previous = signal.getsignal(signal.SIGINT)
        host = FakeHost()
        code, out, err = invoke("run", "--output", "json", services=FakeServices(host), cancellation=event)
        self.assertEqual(code, 0)
        self.assertEqual(host.events, ["start", "dispose"])
        self.assertEqual(signal.getsignal(signal.SIGINT), previous)
        self.assertEqual(json.loads(out)["health"]["status"], "healthy")

    def test_run_interrupt_during_startup_is_failure_with_cleanup(self):
        host = FakeHost(start_error=KeyboardInterrupt())
        code, out, err = invoke("run", "--once", "--output", "json", services=FakeServices(host))
        self.assertEqual(code, 4)
        self.assertEqual(host.events, ["start", "dispose"])
        self.assertEqual(json.loads(err)["diagnostics"][0]["code"], "CLI-CANCEL-001")

    def test_modules_empty_single_and_dependencies_without_start(self):
        for names in ((), ("one",), ("one", "two")):
            host = FakeHost(names)
            code, out, err = invoke("modules", "--output", "json", services=FakeServices(host))
            self.assertEqual(code, 0)
            report = json.loads(out)
            self.assertEqual(len(report["modules"]), len(names))
            self.assertEqual(report["startup_order"], list(names))
            self.assertEqual(host.events, ["dispose"])
            if len(names) == 2:
                self.assertEqual(report["modules"][1]["dependencies"], ["one"])

    def test_health_healthy_degraded_unhealthy(self):
        for status in HealthStatus:
            code, out, err = invoke("health", "--output", "json", services=FakeServices(FakeHost(status=status)))
            self.assertEqual(code, 1 if status == HealthStatus.UNHEALTHY else 0)
            self.assertEqual(json.loads(out)["health"]["status"], status)
            self.assertEqual(json.loads(out)["scope"], "local-inspection")

    def test_quiet_suppresses_human_but_retains_json_and_errors(self):
        self.assertEqual(invoke("modules", "--quiet")[1:], ("", ""))
        code, out, err = invoke("version", "--quiet", "--output", "json")
        self.assertEqual(json.loads(out)["version"], CLI_VERSION)
        code, out, err = invoke("health", "--quiet", services=FakeServices(failures={"configuration": RuntimeError("secret")}))
        self.assertEqual(code, 1)
        self.assertIn("CLI-INTERNAL-001", err)

    def test_verbose_reports_type_without_sensitive_exception_text(self):
        code, out, err = invoke("modules", "--verbose", services=FakeServices(failures={"configuration": RuntimeError("secret-value")}))
        self.assertIn("RuntimeError", err)
        self.assertNotIn("secret-value", err)
        self.assertNotIn("Traceback", err)

    def test_explicit_nested_command_extends_without_root_dispatch_change(self):
        registry = CommandRegistry().register(CommandDefinition(("architecture", "test"), "Test a real future capability", lambda c, a: CommandResult("architecture test", {"answer": 42})))
        code, out, err = invoke("architecture", "test", "--output", "json", registry=registry)
        self.assertEqual(code, 0)
        self.assertEqual(json.loads(out)["answer"], 42)
        code, out, err = invoke("architecture", "test", "--help", registry=registry)
        self.assertEqual(code, 0)
        self.assertIn("real future capability", out)
        self.assertEqual(err, "")

    def test_registry_rejects_duplicates_and_leaf_namespace_conflicts(self):
        definition = CommandDefinition(("one",), "One", lambda c, a: 0)
        registry = CommandRegistry((definition,))
        for candidate in (definition, CommandDefinition(("one", "two"), "Two", lambda c, a: 0), CommandDefinition((), "Empty", lambda c, a: 0)):
            with self.assertRaises(ValueError):
                registry.register(candidate)


    def test_hyphenated_commands_and_shared_namespaces(self):
        registry = CommandRegistry((CommandDefinition(("inspect-ir",), "Inspect IR", lambda c, a: CommandResult("inspect-ir", {"value": 1})), CommandDefinition(("model", "inspect"), "Inspect", lambda c, a: CommandResult("model inspect", {"value": 2})), CommandDefinition(("model", "validate"), "Validate", lambda c, a: CommandResult("model validate", {"value": 3}))))
        for arguments, expected in ((("inspect-ir",), 1), (("model", "inspect"), 2), (("model", "validate"), 3)):
            code, out, err = invoke(*arguments, "--output", "json", registry=registry)
            self.assertEqual(code, 0)
            self.assertEqual(json.loads(out)["value"], expected)

    def test_json_metadata_cannot_be_overwritten_by_command_payload(self):
        registry = CommandRegistry((CommandDefinition(("example",), "Example", lambda c, a: CommandResult("example", {"schema_version": 999, "exit_code": 8})),))
        code, out, err = invoke("example", "--output", "json", registry=registry)
        self.assertEqual(code, 0)
        self.assertEqual(json.loads(out)["schema_version"], 1)
        self.assertEqual(json.loads(out)["exit_code"], 0)
