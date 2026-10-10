import ast
from dataclasses import fields
from pathlib import Path
from typing import get_type_hints
import unittest
from architecture_fitness.discovery import discover
from architecture_fitness.engine import execute
from semantic_kernel.public import FacetKind, FacetDefinition, FacetApplicability, SemanticElementKind, SemanticElement

ROOT = Path(__file__).resolve().parents[2]


class FacetBoundaryTests(unittest.TestCase):
    def test_facets_are_kernel_owned_without_infrastructure_dependencies(self):
        for value in (FacetKind, FacetDefinition, FacetApplicability):
            self.assertEqual(value.__module__, 'semantic_kernel.public')
        model = discover(ROOT)
        self.assertEqual(model.graph('observed')['semantic-kernel'], set())
        self.assertEqual(execute(model, rule_ids=('ARCH-SK-002', 'ARCH-SK-003'))['summary']['status'], 'HEALTHY')

    def test_base_contract_contains_only_typed_read_only_kind_without_behavior(self):
        tree = ast.parse((ROOT / 'platform/kernel/semantic-kernel/src/semantic_kernel/public.py').read_text())
        facet = next(node for node in tree.body if isinstance(node, ast.ClassDef) and node.name == 'FacetDefinition')
        self.assertEqual({node.name for node in facet.body if isinstance(node, ast.FunctionDef)}, {'kind'})
        self.assertTrue(all(isinstance(node, ast.FunctionDef) or isinstance(node, ast.Expr) and isinstance(node.value, ast.Constant) and isinstance(node.value.value, str) for node in facet.body))
        prop = next(node for node in facet.body if isinstance(node, ast.FunctionDef))
        self.assertEqual([ast.unparse(d) for d in prop.decorator_list], ['property'])
        self.assertEqual(ast.unparse(prop.returns), 'FacetKind')
        self.assertTrue(all(isinstance(node, ast.Expr) and isinstance(node.value, ast.Constant) for node in prop.body))
        self.assertNotIn(SemanticElement, FacetDefinition.__mro__)

    def test_applicability_is_typed_data_without_runtime_class_or_metadata_bag(self):
        self.assertEqual({field.name: field.type for field in fields(FacetApplicability)}, {'facet_kind': FacetKind, 'allowed_element_kinds': frozenset[SemanticElementKind]})
        self.assertEqual(get_type_hints(FacetDefinition.kind.fget), {'return': FacetKind})
        for contract in (FacetDefinition, FacetApplicability):
            for name in ('properties', 'metadata', 'payload', 'compile', 'execute', 'persist', 'render', 'authorize', 'validate', 'services', 'owner_element', 'host_element_id', 'version', 'enabled', 'priority', 'registry'):
                self.assertFalse(hasattr(contract, name), name)
        self.assertFalse(hasattr(SemanticElement, 'facets'))
