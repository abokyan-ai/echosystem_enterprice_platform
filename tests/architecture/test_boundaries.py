"""Negative fixtures prove rules reject actual violations, not just a clean graph."""
import json
import shutil
import tempfile
import unittest
from pathlib import Path
from check_architecture import check, cycles

ROOT = Path(__file__).resolve().parents[2]


class ArchitectureTests(unittest.TestCase):
    def setUp(self):
        (ROOT / "build").mkdir(exist_ok=True)
        self.temporary = tempfile.TemporaryDirectory(dir=ROOT / "build")
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name) / "repo"
        self.root.mkdir()
        shutil.copy2(ROOT / "architecture.json", self.root / "architecture.json")
        for family in ("platform", "tools", "adapters", "apps"):
            shutil.copytree(ROOT / family, self.root / family, ignore=shutil.ignore_patterns("__pycache__"))

    def inject(self, module_path, content):
        (self.root / module_path / "public.py").write_text(content)
        return check(self.root)

    def test_clean_repository(self):
        self.assertEqual(check(ROOT), [])

    def test_AT001_kernel_cannot_import_runtime(self):
        errors = self.inject("platform/kernel/semantic-kernel/src/semantic_kernel", "from runtime_core.public import MODULE_NAME\n")
        self.assertTrue(any("semantic-kernel -> runtime-core" in e for e in errors))

    def test_AT002_kernel_cannot_import_compiler(self):
        errors = self.inject("platform/kernel/semantic-kernel/src/semantic_kernel", "import compiler_core.public\n")
        self.assertTrue(any("semantic-kernel -> compiler-core" in e for e in errors))

    def test_AT003_platform_cannot_import_adapter(self):
        errors = self.inject("platform/runtime/runtime-core/src/runtime_core", "import postgres_adapter\n")
        self.assertTrue(any("Unapproved external import" in e for e in errors))

    def test_AT004_platform_cannot_import_application(self):
        errors = self.inject("platform/model/model-core/src/model_core", "import reference_mini_sales\n")
        self.assertTrue(any("Unapproved external import" in e for e in errors))

    def test_AT005_model_cannot_import_frontend(self):
        for framework in ("react", "angular", "flutter", "psycopg", "yaml"):
            with self.subTest(framework=framework):
                errors = self.inject("platform/model/model-core/src/model_core", f"import {framework}\n")
                self.assertTrue(any("Unapproved external import" in e for e in errors))

    def test_AT006_cycles_are_rejected(self):
        self.assertTrue(cycles({"a": {"b"}, "b": {"c"}, "c": {"a"}}))
        self.assertTrue(cycles({"a": {"a"}}))
        manifest = json.loads((self.root / "architecture.json").read_text())
        manifest["modules"][0]["allowed_dependencies"] = ["model-core"]
        (self.root / "architecture.json").write_text(json.dumps(manifest))
        self.assertTrue(any("Circular dependency" in e for e in check(self.root)))

    def test_internal_and_namespace_imports_are_rejected(self):
        for statement in ("import semantic_kernel.internal", "from semantic_kernel import internal", "import semantic_kernel"):
            errors = self.inject("platform/model/model-core/src/model_core", statement + "\n")
            self.assertTrue(any("Public API violation" in e for e in errors))

    def test_allowed_public_import_and_local_relative_import(self):
        errors = self.inject("platform/model/model-core/src/model_core", "from semantic_kernel.public import MODULE_NAME\nfrom . import internal\n")
        self.assertEqual(errors, [])

    def test_runtime_source_and_dynamic_imports_are_rejected(self):
        for statement in ("import model_core.public", "import yaml", "import importlib", "__import__('react')", "exec('import react')"):
            errors = self.inject("platform/runtime/runtime-core/src/runtime_core", statement + "\n")
            self.assertTrue(errors)

    def test_unregistered_source_is_rejected(self):
        directory = self.root / "adapters/persistence/memory"
        directory.mkdir(parents=True)
        (directory / "adapter.py").write_text("import os\n")
        self.assertTrue(any("Unregistered source" in e for e in check(self.root)))

    def test_manifest_cannot_relax_kernel_invariant(self):
        manifest = json.loads((self.root / "architecture.json").read_text())
        manifest["modules"][0]["allowed_dependencies"] = ["runtime-core"]
        (self.root / "architecture.json").write_text(json.dumps(manifest))
        self.assertTrue(any("Boundary dependency forbidden" in e for e in check(self.root)))

    def test_registered_adapter_and_app_edges_are_rejected(self):
        for name, family in (("memory-adapter", "adapters"), ("sales-app", "apps"), ("react-target", "adapters")):
            with self.subTest(name=name):
                manifest = json.loads((self.root / "architecture.json").read_text())
                package = name.replace("-", "_")
                path = f"{family}/{name}"
                directory = self.root / path / "src" / package
                directory.mkdir(parents=True)
                (directory / "public.py").write_text(f'MODULE_NAME = "{name}"\n')
                manifest["modules"].append({"name": name, "path": path, "package": package, "allowed_dependencies": []})
                manifest["modules"][1]["allowed_dependencies"].append(name)
                (self.root / "architecture.json").write_text(json.dumps(manifest))
                self.assertTrue(any("Platform dependency forbidden" in e for e in check(self.root)))

    def test_stdlib_infrastructure_imports_are_rejected(self):
        for name in ("sqlite3", "http.client", "socket"):
            errors = self.inject("platform/kernel/semantic-kernel/src/semantic_kernel", f"import {name}\n")
            self.assertTrue(any("Infrastructure import forbidden" in e for e in errors))
