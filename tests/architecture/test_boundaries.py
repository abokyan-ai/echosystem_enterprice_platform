"""AT-DEP-001..012 plus policy regression fixtures; no synthetic production features."""
import json
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from check_architecture import ArchitectureError, analyze, check

ROOT = Path(__file__).resolve().parents[2]


class DependencyTests(unittest.TestCase):
    def setUp(self):
        (ROOT / "build").mkdir(exist_ok=True)
        self.temporary = tempfile.TemporaryDirectory(dir=ROOT / "build")
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name) / "repo"
        self.root.mkdir()
        for filename in ("architecture.json", "architecture-policy.json"):
            shutil.copy2(ROOT / filename, self.root / filename)
        (self.root / "docs/architecture").mkdir(parents=True)
        shutil.copy2(ROOT / "docs/architecture/dependency-exceptions.json", self.root / "docs/architecture")
        for family in ("platform", "tools", "adapters", "apps", "scripts"):
            shutil.copytree(ROOT / family, self.root / family, ignore=shutil.ignore_patterns("__pycache__"))

    def manifest(self):
        return json.loads((self.root / "architecture.json").read_text())

    def save(self, data):
        (self.root / "architecture.json").write_text(json.dumps(data))

    def module(self, name):
        return next(m for m in self.manifest()["modules"] if m["name"] == name)

    def source(self, name, content, filename="public.py"):
        m = self.module(name)
        p = self.root / m["path"] / "src" / m["package"] / filename
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(content)

    def permit(self, source, target, category="api"):
        data = self.manifest()
        m = next(m for m in data["modules"] if m["name"] == source)
        if target not in m["allowed_dependencies"]:
            m["allowed_dependencies"].append(target)
        m["dependency_categories"][target] = category
        self.save(data)

    def add_module(self, name, zone, path, profile=None):
        data = self.manifest()
        package = name.replace("-", "_")
        m = {"name": name, "package": package, "path": path, "zone": zone, "owner": "fixture owner", "language": "python", "public_api": [package + ".public"], "allowed_dependencies": [], "dependency_categories": {}, "external_dependencies": []}
        if profile:
            m["technology_profile"] = profile
        data["modules"].append(m)
        directory = self.root / path / "src" / package
        directory.mkdir(parents=True)
        (directory / "public.py").write_text(f'MODULE_NAME = "{name}"\n')
        self.save(data)
        return package

    def assert_rule(self, rule, source=None):
        violations = analyze(self.root)["violations"]
        self.assertTrue(any(v["rule_id"] == rule and (source is None or v["source"] == source) for v in violations), violations)

    def test_real_repository_has_no_violations(self):
        self.assertEqual(check(ROOT), [])
        self.assertEqual(analyze(ROOT)["cycle_count"], 0)

    def test_AT_DEP_001_kernel_runtime(self):
        self.permit("semantic-kernel", "runtime-core")
        self.source("semantic-kernel", "from runtime_core.public import MODULE_NAME\n")
        self.assert_rule("ARCH-DEP-001", "semantic-kernel")

    def test_AT_DEP_002_kernel_compiler(self):
        self.source("semantic-kernel", "import compiler_core.public\n")
        self.assert_rule("ARCH-DEP-001", "semantic-kernel")

    def test_AT_DEP_003_model_runtime(self):
        self.permit("model-core", "runtime-core")
        self.source("model-core", "from runtime_core.public import MODULE_NAME\n")
        self.assert_rule("ARCH-DEP-002", "model-core")

    def test_AT_DEP_004_model_frontend_framework(self):
        for name in ("react", "angular", "flutter", "django", "rest_framework", "primeng"):
            with self.subTest(name=name):
                self.source("model-core", f"import {name}\n")
                self.assert_rule("ARCH-DEP-002", "model-core")

    def test_AT_DEP_005_runtime_authoring_parsers(self):
        for name in ("yaml", "json", "model_core.public"):
            with self.subTest(name=name):
                self.source("runtime-core", f"import {name}\n")
                self.assert_rule("ARCH-DEP-004", "runtime-core")

    def test_AT_DEP_006_platform_adapter(self):
        package = self.add_module("memory-data", "adapter", "adapters/data/memory", "mock-data")
        self.permit("runtime-core", "memory-data")
        self.source("runtime-core", f"import {package}.public\n")
        self.assert_rule("ARCH-DEP-006", "runtime-core")

    def test_AT_DEP_007_platform_reference_app(self):
        package = self.add_module("reference-mini-sales", "application", "apps/reference-mini-sales")
        self.permit("model-core", "reference-mini-sales")
        self.source("model-core", f"import {package}.public\n")
        self.assert_rule("ARCH-DEP-007", "model-core")

    def test_AT_DEP_008_experience_frontend(self):
        self.add_module("experience-model", "experience", "platform/experience/experience-model")
        for name in ("angular", "primeng", "react", "flutter"):
            self.source("experience-model", f"import {name}\n")
            self.assert_rule("ARCH-DEP-008", "experience-model")

    def test_AT_DEP_009_declared_and_observed_cycles(self):
        self.permit("semantic-kernel", "model-core")
        self.source("semantic-kernel", "import model_core.public\n")
        self.source("model-core", "import semantic_kernel.public\n")
        report = analyze(self.root)
        self.assertEqual(report["cycle_count"], 2)
        self.assert_rule("ARCH-CYCLE-001")

    def test_AT_DEP_010_internal_and_namespace_imports(self):
        for statement in ("import semantic_kernel.internal", "from semantic_kernel import internal", "import semantic_kernel", "from semantic_kernel.public import _secret", "from semantic_kernel.public import *"):
            self.source("model-core", statement + "\n")
            self.assert_rule("ARCH-API-001", "model-core")

    def test_AT_DEP_011_production_test_imports(self):
        for statement in ("import unittest", "from .tests import fixture", "import fixtures", "import semantic_kernel.test_utils"):
            self.source("model-core", statement + "\n")
            self.assert_rule("ARCH-DEP-011", "model-core")

    def test_AT_DEP_012_generic_module(self):
        self.add_module("shared", "model", "platform/model/shared")
        self.assert_rule("ARCH-DEP-012", "shared")

    def test_compiler_runtime_and_persistence_leakage(self):
        for name in ("runtime_core.public", "psycopg", "sqlite3"):
            self.source("compiler-core", f"import {name}\n")
            self.assert_rule("ARCH-DEP-003", "compiler-core")

    def test_compiled_ir_cannot_import_runtime(self):
        self.permit("compiled-contracts", "runtime-core")
        self.source("compiled-contracts", "import runtime_core.public\n")
        self.assert_rule("ARCH-DEP-005", "compiled-contracts")

    def test_core_cannot_depend_on_tools(self):
        self.permit("model-core", "platform-cli")
        self.source("model-core", "import platform_cli.public\n")
        self.assert_rule("ARCH-DEP-010", "model-core")

    def test_frontend_profile_contract_direction(self):
        self.add_module("angular-target", "adapter", "adapters/frontend/angular", "angular-primeng")
        self.permit("angular-target", "semantic-kernel")
        self.source("angular-target", "import semantic_kernel.public\n")
        self.assert_rule("ARCH-DEP-009", "angular-target")

    def test_valid_public_imports_and_port_direction(self):
        self.source("model-core", "from semantic_kernel.public import MODULE_NAME\n")
        self.add_module("memory-data", "adapter", "adapters/data/memory", "mock-data")
        self.permit("memory-data", "runtime-core")
        self.source("memory-data", "from runtime_core.public import MODULE_NAME\n")
        self.assertEqual(check(self.root), [])

    def test_relative_internal_import_allowed_in_internal_implementation(self):
        self.source("model-core", "from . import companion\n", "internal/consumer.py")
        self.source("model-core", "VALUE = 1\n", "internal/companion.py")
        self.assertEqual(check(self.root), [])

    def test_public_contract_cannot_reexport_internal(self):
        self.source("model-core", "from .internal import ConcreteRepository\n")
        self.assert_rule("ARCH-API-002", "model-core")

    def test_nested_and_type_checking_imports_are_detected(self):
        self.source("model-core", "from typing import TYPE_CHECKING\nif TYPE_CHECKING:\n    import runtime_core.public\ndef f():\n    import compiler_core.public\n")
        self.assert_rule("ARCH-DEP-002", "model-core")

    def test_dynamic_imports_and_infrastructure_stdlib_are_rejected(self):
        for statement in ("__import__('django')", "exec('import django')", "import importlib", "import sqlite3", "import http.client"):
            self.source("semantic-kernel", statement + "\n")
            self.assertTrue(check(self.root))

    def test_undeclared_same_zone_dependency_is_rejected(self):
        self.add_module("canonical-model", "model", "platform/model/canonical-model")
        self.source("model-core", "import canonical_model.public\n")
        self.assert_rule("ARCH-ALLOW-001", "model-core")

    def test_unknown_source_and_language_fail_closed(self):
        directory = self.root / "adapters/frontend/angular"
        directory.mkdir(parents=True)
        (directory / "widget.ts").write_text("import { Component } from '@angular/core';\n")
        self.assert_rule("ARCH-REG-001")

    def test_external_framework_approval_is_narrow(self):
        self.add_module("http-api", "adapter", "adapters/http/drf", "django-rest-framework")
        data = self.manifest()
        m = data["modules"][-1]
        m["external_dependencies"] = ["django", "rest_framework"]
        self.save(data)
        self.source("http-api", "import django\nimport rest_framework\n")
        self.assertEqual(check(self.root), [])
        data["modules"][0]["external_dependencies"] = ["django"]
        self.save(data)
        self.assert_rule("ARCH-EXT-001", "semantic-kernel")

    def test_manifest_rejects_zone_relabeling_unknown_edges_and_overlaps(self):
        original = self.manifest()
        for field, value in (("zone", "tooling"), ("allowed_dependencies", ["nonexistent"]), ("path", "../escape")):
            data = json.loads(json.dumps(original))
            data["modules"][0][field] = value
            self.save(data)
            with self.assertRaises(ArchitectureError):
                analyze(self.root)
        self.save(original)
        data = self.manifest()
        data["modules"][1]["path"] = data["modules"][0]["path"]
        self.save(data)
        with self.assertRaises(ArchitectureError):
            analyze(self.root)

    def test_exception_registry_cannot_silently_disable_rules(self):
        (self.root / "docs/architecture/dependency-exceptions.json").write_text('{"schema_version":1,"exceptions":[{"rule_id":"ARCH-DEP-001"}]}')
        with self.assertRaises(ArchitectureError):
            analyze(self.root)

    def test_diagnostics_contain_rule_location_and_resolution(self):
        self.source("model-core", "import runtime_core.public\n")
        diagnostics = check(self.root)
        self.assertTrue(any(all(text in d for text in ("ARCH-DEP-002", "From: model-core", "To: runtime-core", "public.py:1", "Resolution:")) for d in diagnostics))

    def test_actual_and_declared_graphs_are_distinct_and_deterministic(self):
        report = analyze(ROOT)
        self.assertEqual(report, analyze(ROOT))
        model = next(m for m in report["modules"] if m["module"] == "model-core")
        self.assertEqual(model["observed_dependencies"], [])
        self.assertEqual(model["declared_dependencies"], ["semantic-kernel"])
        cli = next(m for m in report["modules"] if m["module"] == "platform-cli")
        self.assertEqual(len(cli["observed_dependencies"]), 5)

    def test_violation_fails_checker_and_build_even_when_python_compiles(self):
        self.source("model-core", "import runtime_core.public\n")
        compile((self.root / "platform/model/model-core/src/model_core/public.py").read_text(), "fixture", "exec")
        for command in (["scripts/check_architecture.py"], ["scripts/dev.py", "build"]):
            result = subprocess.run([sys.executable, *command], cwd=self.root, text=True, capture_output=True)
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("ARCH-DEP-002", result.stderr)
            self.assertNotIn("Traceback", result.stderr)

    def test_test_category_is_not_a_production_edge(self):
        self.permit("model-core", "semantic-kernel", "test")
        self.assert_rule("ARCH-DEP-011", "model-core")

    def test_fitness_exception_round_trip_and_expiry_fail_cli(self):
        self.permit("model-core", "runtime-core")
        self.source("model-core", "from runtime_core.public import MODULE_NAME as RUNTIME\nMODULE_NAME = 'model-core'\n")
        registry = {"schema_version": 1, "exceptions": []}
        for index, rule_id in enumerate(("ARCH-DEP-002", "ARCH-FIT-DEP-003")):
            registry["exceptions"].append({"id": f"fixture-waiver-{index}", "rule_id": rule_id, "source": "model-core", "target": "runtime-core", "reason": "Temporary negative fixture only", "owner": "fixture owner", "created_at": "2026-10-01", "expires_at": "2026-11-01", "review_issue": "ADR-TEST-001"})
        path = self.root / "docs/architecture/dependency-exceptions.json"
        path.write_text(json.dumps(registry))
        command = [sys.executable, "scripts/dev.py", "fitness:json", "--as-of", "2026-10-07"]
        result = subprocess.run(command, cwd=self.root, capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stderr)
        report = json.loads(result.stdout)
        self.assertEqual(report["summary"]["suppressed"], 3)
        self.assertTrue(all(e["status"] == "applied" for e in report["exceptions"]))
        registry["exceptions"][0]["expires_at"] = "2026-10-06"
        path.write_text(json.dumps(registry))
        result = subprocess.run(command, cwd=self.root, capture_output=True, text=True)
        self.assertNotEqual(result.returncode, 0)
        self.assertTrue(any(v["rule_id"] == "ARCH-EXC-001" for v in json.loads(result.stdout)["violations"]))
