import ast
from pathlib import Path
import unittest
from architecture_fitness.discovery import discover
from architecture_fitness.engine import execute
from semantic_kernel.public import SemanticElement

ROOT = Path(__file__).resolve().parents[2]


class SemanticElementBoundaryTests(unittest.TestCase):
    def test_root_is_kernel_owned_and_existing_rules_pass(self):
        self.assertEqual(SemanticElement.__module__, 'semantic_kernel.public')
        model = discover(ROOT)
        report = execute(model, rule_ids=('ARCH-SK-ELEM-001', 'ARCH-SK-002', 'ARCH-SK-003'))
        self.assertEqual(report['summary']['status'], 'HEALTHY')
        self.assertEqual(model.graph('observed')['semantic-kernel'], set())

    def test_root_source_contains_only_three_typed_property_contracts(self):
        tree = ast.parse((ROOT / 'platform/kernel/semantic-kernel/src/semantic_kernel/public.py').read_text())
        root = next(node for node in tree.body if isinstance(node, ast.ClassDef) and node.name == 'SemanticElement')
        properties = [node for node in root.body if isinstance(node, ast.FunctionDef)]
        self.assertEqual({node.name: ast.unparse(node.returns) for node in properties}, {'id': 'SemanticElementId', 'qualified_name': 'QualifiedName', 'context': 'SemanticContextRef'})
        for node in properties:
            self.assertEqual([ast.unparse(decorator) for decorator in node.decorator_list], ['property'])
            self.assertTrue(all(isinstance(part, ast.Expr) and isinstance(part.value, ast.Constant) for part in node.body))
        self.assertTrue(all(isinstance(node, ast.FunctionDef) or isinstance(node, ast.Expr) and isinstance(node.value, ast.Constant) and isinstance(node.value.value, str) for node in root.body))
