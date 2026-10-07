"""Pure model fixtures test the harness without scanning or modifying the repository."""
import copy
import json
import unittest
from dataclasses import replace
from datetime import date
from pathlib import Path
from unittest.mock import patch
from architecture_fitness.discovery import discover
from architecture_fitness.engine import HarnessError, execute
from architecture_fitness.model import ArchitectureModel, ArchitectureRule, ArchitectureViolation, Module, Severity, Source
from architecture_fitness.reporting import render
from architecture_fitness.rules import RuleRegistry, default_registry

ROOT = Path(__file__).resolve().parents[2]
POLICY = json.loads((ROOT / "architecture-policy.json").read_text())
TODAY = date(2026, 10, 7)


def module(name, zone, dependencies=()):
    package = name.replace("-", "_")
    metadata = {"name": name, "package": package, "zone": zone, "path": POLICY["zones"][zone]["path_prefix"] + name, "owner": "fixture", "public_api": [package + ".public"], "allowed_dependencies": list(dependencies), "dependency_categories": {n: "api" for n in dependencies}, "external_dependencies": []}
    return Module(name, metadata["path"], zone, "contract", tuple(metadata["public_api"]), (package + ".internal",), metadata)


def fixture(modules=(), sources=(), exceptions=(), policy=None):
    return ArchitectureModel(tuple(modules), tuple(sources), copy.deepcopy(policy or POLICY), tuple(exceptions), {"adapter": "synthetic", "scan_passes": 0})


def finding(rule_id="ARCH-CUSTOM-001", severity=Severity.ERROR, source="one", target="two"):
    return ArchitectureViolation(rule_id, severity, "Fixture violation", source, target, "fixture.py:7", "Use an owned contract", file="fixture.py", line=7)


def rule(findings=(), severity=Severity.ERROR, evaluator=None):
    return ArchitectureRule("ARCH-CUSTOM-001", "Custom fitness", "Test custom architecture property", "contract", severity, "fixture", evaluator or (lambda model, context: list(findings)))


def exception(rule_id="ARCH-CUSTOM-001", source="one", target="two", expires="2026-11-01"):
    return {"id": "waiver-1", "rule_id": rule_id, "source": source, "target": target, "reason": "Temporary compatibility seam", "owner": "architecture owner", "created_at": "2026-10-01", "expires_at": expires, "review_issue": "ADR-TEST-001"}


class HarnessTests(unittest.TestCase):
    def run_rule(self, r, exceptions=(), **options):
        return execute(fixture(exceptions=exceptions), RuleRegistry([r]), as_of=TODAY, **options)

    def test_no_violations_pass(self):
        report = self.run_rule(rule())
        self.assertEqual(report["summary"]["status"], "HEALTHY")
        self.assertEqual(report["results"][0]["status"], "PASS")

    def test_one_and_multiple_violations_all_returned(self):
        report = self.run_rule(rule([finding(), finding(target="three")]))
        self.assertEqual(report["summary"]["status"], "FAILED")
        self.assertEqual(len(report["violations"]), 2)

    def test_info_warning_error_critical_severity(self):
        for severity in Severity:
            with self.subTest(severity=severity):
                report = self.run_rule(rule([finding(severity=severity)], severity))
                self.assertEqual(report["summary"]["status"] == "FAILED", severity in {Severity.ERROR, Severity.CRITICAL})
        report = self.run_rule(rule([finding(severity=Severity.WARNING)], Severity.WARNING), warnings_as_errors=True)
        self.assertEqual(report["summary"]["status"], "FAILED")

    def test_suppression_requires_exact_scope_and_is_reported(self):
        report = self.run_rule(rule([finding()]), [exception()])
        self.assertEqual(report["summary"]["status"], "HEALTHY")
        self.assertEqual(report["summary"]["suppressed"], 1)
        self.assertEqual(report["exceptions"][0]["status"], "applied")
        self.assertEqual(report["suppressed_violations"][0]["violation"]["source"], "one")
        self.assertIn("SUPPRESSED", render(report))
        unmatched = self.run_rule(rule([finding(target="different")]), [exception()])
        self.assertEqual(unmatched["summary"]["status"], "FAILED")
        self.assertEqual(unmatched["exceptions"][0]["status"], "unmatched")

    def test_expired_exception_fails_even_without_underlying_violation(self):
        report = self.run_rule(rule(), [exception(expires="2026-10-07")])
        self.assertEqual(report["summary"]["status"], "FAILED")
        self.assertEqual(report["violations"][0]["rule_id"], "ARCH-EXC-001")

    def test_expired_exception_does_not_suppress(self):
        report = self.run_rule(rule([finding()]), [exception(expires="2026-10-06")])
        self.assertEqual(report["summary"]["suppressed"], 0)
        self.assertEqual(len(report["violations"]), 2)

    def test_invalid_unknown_wildcard_duplicate_and_bad_date_exceptions(self):
        cases = [exception(rule_id="UNKNOWN"), exception(source="*"), exception(expires="not-a-date"), {**exception(), "owner": ""}, {**exception(), "created_at": "2026-12-01"}, exception(expires="2026-09-01")]
        for item in cases:
            with self.subTest(item=item), self.assertRaises(ValueError):
                self.run_rule(rule(), [item])
        with self.assertRaises(HarnessError):
            self.run_rule(rule(), [exception(), {**exception(), "id": "waiver-2"}])

    def test_unknown_rule_or_category_selection_fails(self):
        for options in ({"rule_ids": ["UNKNOWN"]}, {"category": "not-a-category"}):
            with self.assertRaises(ValueError):
                self.run_rule(rule(), **options)

    def test_registry_rejects_duplicates_and_bad_contract(self):
        registry = RuleRegistry([rule()])
        with self.assertRaises(ValueError):
            registry.register(rule())
        with self.assertRaises(ValueError):
            RuleRegistry([replace(rule(), name="")])

    def test_evaluator_error_never_passes_or_gets_waived(self):
        def broken(model, context):
            raise RuntimeError("fixture failure")
        report = self.run_rule(rule(severity=Severity.WARNING, evaluator=broken))
        self.assertEqual(report["summary"]["status"], "FAILED")
        self.assertTrue(report["results"][0]["metadata"]["evaluator_failed"])

    def test_invalid_result_contract_fails(self):
        report = self.run_rule(rule(evaluator=lambda m, c: [finding(rule_id="WRONG")]))
        self.assertEqual(report["summary"]["status"], "FAILED")

    def test_transitive_kernel_runtime_path(self):
        model = fixture([module("kernel", "kernel", ["bridge"]), module("bridge", "model", ["runtime"]), module("runtime", "runtime")])
        report = execute(model, rule_ids=["ARCH-FIT-DEP-001"], as_of=TODAY)
        self.assertEqual(report["violations"][0]["dependency_path"], ("kernel", "bridge", "runtime"))
        self.assertIn("kernel -> bridge -> runtime", render(report))

    def test_code_owned_invariant_survives_relaxed_policy(self):
        policy = copy.deepcopy(POLICY)
        policy["zones"]["model"]["allowed_zones"].append("runtime")
        model = fixture([module("model", "model", ["runtime"]), module("runtime", "runtime")], policy=policy)
        report = execute(model, as_of=TODAY)
        self.assertTrue(any(v["rule_id"] == "ARCH-FIT-DEP-003" for v in report["violations"]))

    def test_cycle_fixture(self):
        model = fixture([module("a", "model", ["b"]), module("b", "model", ["a"])])
        report = execute(model, rule_ids=["ARCH-CYCLE-001"], as_of=TODAY)
        self.assertEqual(report["summary"]["status"], "FAILED")
        self.assertEqual(report["summary"]["cycles"], 1)

    def test_framework_internal_authoring_and_test_fixtures(self):
        models = [
            (fixture([module("experience", "experience")], [Source("experience/public.py", "experience", (("django", 2),))]), "ARCH-EXP-001"),
            (fixture([module("runtime", "runtime")], [Source("runtime/public.py", "runtime", (("yaml", 2),))]), "ARCH-DEP-004"),
            (fixture([module("model", "model", ["kernel"]), module("kernel", "kernel")], [Source("model/public.py", "model", (("kernel.internal", 2),))]), "ARCH-API-001"),
            (fixture([module("runtime", "runtime")], [Source("runtime/public.py", "runtime", (("unittest", 2),))]), "ARCH-TEST-001"),
            (fixture([module("kernel", "kernel")], [Source("kernel/public.py", "kernel", (("django", 2),))]), "ARCH-EXTDEP-001"),
        ]
        for model, rule_id in models:
            with self.subTest(rule_id=rule_id):
                report = execute(model, rule_ids=[rule_id], as_of=TODAY)
                self.assertEqual(report["summary"]["status"], "FAILED")

    def test_unclassified_source_and_external_inventory(self):
        model = fixture([module("kernel", "kernel")], [Source("unknown.py", None, issue="No owner", issue_kind="registration"), Source("kernel/public.py", "kernel", (("django", 1), ("not_a_known_library", 2)))])
        report = execute(model, as_of=TODAY)
        self.assertTrue(any(v["rule_id"] == "ARCH-MOD-001" for v in report["violations"]))
        self.assertIn({"module": "kernel", "dependency": "django", "category": "framework"}, report["external_dependencies"])
        self.assertIn({"module": "kernel", "dependency": "not_a_known_library", "category": "unknown"}, report["external_dependencies"])

    def test_rules_evaluate_shared_model_without_discovery(self):
        model = fixture([module("kernel", "kernel")])
        seen = []
        first = rule(evaluator=lambda m, c: seen.append(id(m)) or [])
        second = replace(first, id="ARCH-CUSTOM-002")
        with patch("architecture_fitness.discovery.discover", side_effect=AssertionError("No rescanning allowed")):
            report = execute(model, RuleRegistry([first, second]), as_of=TODAY)
        self.assertEqual(seen, [id(model), id(model)])
        self.assertEqual(report["summary"]["status"], "HEALTHY")

    def test_machine_schema_and_semantic_determinism(self):
        first = self.run_rule(rule([finding()]))
        second = self.run_rule(rule([finding()]))
        for report in (first, second):
            self.assertTrue({"timestamp", "rules", "results", "violations", "exceptions", "summary"}.issubset(report))
            report.pop("timestamp")
            for result in report["results"]:
                result.pop("duration_ms")
        self.assertEqual(json.loads(render(first, "json")), json.loads(render(second, "json")))

    def test_actual_repository_discovery_contract(self):
        model = discover(ROOT)
        self.assertEqual(len(model.modules), 6)
        self.assertEqual(model.discovery_metadata["scan_passes"], 1)
        self.assertEqual(len(model.graph("observed")["platform-cli"]), 5)
        self.assertTrue(all(m.public_api and m.internal_api and m.zone for m in model.modules))
        report = execute(model, as_of=TODAY)
        self.assertEqual(report["summary"]["status"], "HEALTHY")
        self.assertEqual(report["summary"]["rules_executed"], 30)

    def test_existing_governance_evaluated_once_for_all_rules(self):
        from architecture_fitness.governance import evaluate_governance
        model = fixture([module("kernel", "kernel")])
        with patch("architecture_fitness.rules.evaluate_governance", wraps=evaluate_governance) as evaluator:
            report = execute(model, as_of=TODAY)
        self.assertEqual(evaluator.call_count, 1)
        self.assertEqual(report["summary"]["rules_executed"], 30)
