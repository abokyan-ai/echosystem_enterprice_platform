import ast
import unittest
from pathlib import Path
from check_architecture import ArchitectureError, Violation, cycles, import_targets


class DependencyParserTests(unittest.TestCase):
    def test_absolute_alias_imports(self):
        self.assertEqual(list(import_targets(ast.parse("import first.public as one, second.public as two"), "local", Path("internal/code.py"))), [("first.public", 1), ("second.public", 1)])

    def test_relative_import_resolution(self):
        targets = list(import_targets(ast.parse("from ..public import Value"), "owned", Path("internal/code.py")))
        self.assertEqual(targets, [("owned.public", 1)])

    def test_invalid_relative_import_is_diagnostic(self):
        with self.assertRaises(ArchitectureError):
            list(import_targets(ast.parse("from ...public import Value"), "owned", Path("public.py")))

    def test_private_exports_are_marked(self):
        targets = list(import_targets(ast.parse("from other.public import _Private"), "owned", Path("public.py")))
        self.assertIn(("other.public.__private_export__", 1), targets)

    def test_cycle_detection_handles_self_and_disjoint_graphs(self):
        self.assertEqual(cycles({"a": set(), "b": {"a"}}), [])
        self.assertEqual(len(cycles({"a": {"a"}, "b": {"c"}, "c": {"b"}})), 2)

    def test_diagnostic_format(self):
        v = Violation("ARCH-DEP-001", "kernel", "runtime", "public.py:2", "Forbidden", "Invert dependency")
        self.assertIn("Resolution: Invert dependency", v.render())
