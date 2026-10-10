import ast
from dataclasses import fields, MISSING
from pathlib import Path
import unittest
from architecture_fitness.discovery import discover
from architecture_fitness.engine import execute
from semantic_kernel.public import ElementRef, ElementRefError, ElementVersionRef, SemanticElementId, SemanticVersion

ROOT = Path(__file__).resolve().parents[2]


class SemanticReferenceBoundaryTests(unittest.TestCase):
    def test_references_are_kernel_owned_and_existing_independence_rules_pass(self):
        for value_type in (ElementRef, ElementRefError, ElementVersionRef):
            self.assertEqual(value_type.__module__, 'semantic_kernel.public')
        model = discover(ROOT)
        self.assertEqual(model.graph('observed')['semantic-kernel'], set())
        self.assertEqual(execute(model, rule_ids=('ARCH-SK-002', 'ARCH-SK-003'))['summary']['status'], 'HEALTHY')

    def test_reference_shape_excludes_version_ambiguity_and_resolution_state(self):
        self.assertEqual({field.name: field.type for field in fields(ElementRef)}, {'element_id': SemanticElementId})
        self.assertEqual({field.name: field.type for field in fields(ElementVersionRef)}, {'element_id': SemanticElementId, 'version': SemanticVersion})
        for value_type in (ElementRef, ElementVersionRef):
            for field in fields(value_type):
                self.assertIs(field.default, MISSING)
                self.assertIs(field.default_factory, MISSING)
            for name in ('resolve', 'load', 'fetch', 'latest', 'exists', 'registry', 'resolver', 'qualified_name', 'name_hint', 'context', 'namespace', 'kind', 'expected_kind', 'definition', 'runtime_object', 'tenant_id', 'package', 'constraints', 'source_location', 'permissions'):
                self.assertFalse(hasattr(value_type, name), name)

    def test_identity_wrapper_uses_only_identity_primitive_and_small_value_api(self):
        tree = ast.parse((ROOT / 'platform/kernel/semantic-kernel/src/semantic_kernel/public.py').read_text())
        ref = next(node for node in tree.body if isinstance(node, ast.ClassDef) and node.name == 'ElementRef')
        self.assertEqual(ref.bases, [])
        self.assertEqual({node.name for node in ref.body if isinstance(node, ast.FunctionDef)}, {'__post_init__', 'from_id', 'parse', 'try_parse', '__str__'})
        used_names = {node.id for node in ast.walk(ref) if isinstance(node, ast.Name)}
        self.assertTrue({'SemanticElementId', 'SemanticElementIdError', 'ElementRefError'} <= used_names)
        self.assertTrue(used_names.isdisjoint({'QualifiedName', 'Namespace', 'SemanticContextRef', 'SemanticElementKind', 'SemanticVersion', 'ElementVersionRef'}))
