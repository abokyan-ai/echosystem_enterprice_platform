import ast
from pathlib import Path
from typing import get_type_hints
import unittest
from architecture_fitness.discovery import discover
from architecture_fitness.engine import execute
import model_core.public as model
import semantic_kernel.public as kernel

ROOT = Path(__file__).resolve().parents[2]


class TypeRegistryBoundaryTests(unittest.TestCase):
    def test_registry_is_model_owned_and_kernel_remains_independent(self):
        for cls in (model.TypeRegistry, model.TypeRegistryLookup, model.TypeRegistrationResult, model.TypeRegistrationDiagnostic, model.TypeRegistrationFailure):
            self.assertEqual(cls.__module__, 'model_core.public')
            self.assertNotIn(cls.__name__, kernel.__all__)
        discovered = discover(ROOT)
        self.assertEqual(discovered.graph('observed')['model-core'], {'semantic-kernel'})
        self.assertEqual(discovered.graph('observed')['semantic-kernel'], set())
        self.assertEqual(execute(discovered)['summary']['status'], 'HEALTHY')

    def test_existing_lookup_and_validator_signatures_are_unchanged(self):
        self.assertEqual({name for name in model.TypeLookup.__dict__ if not name.startswith('_')}, {'find'})
        self.assertEqual(get_type_hints(model.TypeLookup.find)['reference'], kernel.ElementRef)
        self.assertEqual(get_type_hints(model.TypeRegistry.find)['return'], kernel.SemanticElement | None)
        self.assertEqual(get_type_hints(model.TypeRegistry.find_by_version)['reference'], kernel.ElementVersionRef)
        self.assertEqual(get_type_hints(model.TypeValidator.validate)['type_definition'], model.TypeDataComposition)
        for cls in (model.TypeRegistry, model.TypeRegistryLookup):
            for name in ('latest', 'validate', 'compile', 'resolve_aliases', 'persist', 'execute', 'validate_entire_world'):
                self.assertFalse(hasattr(cls, name))

    def test_registry_has_no_validation_runtime_or_dynamic_dependency(self):
        tree = ast.parse((ROOT / 'platform/model/model-core/src/model_core/public.py').read_text())
        types_imports = [node for node in tree.body if isinstance(node, ast.ImportFrom) and node.module == 'types']
        self.assertEqual([[alias.name for alias in n.names] for n in types_imports], [['MappingProxyType']])
        names = {'TypeRegistry', 'TypeRegistryLookup', '_registry_capture_owner', '_registry_snapshot', '_registry_data_is_canonical', '_registration_rejected'}
        for node in tree.body:
            if isinstance(node, (ast.ClassDef, ast.FunctionDef)) and node.name in names:
                for call in (n for n in ast.walk(node) if isinstance(n, ast.Call)):
                    if isinstance(call.func, ast.Name):
                        self.assertNotIn(call.func.id, {'TypeValidator', 'open', 'eval', 'exec', '__import__'})
                    if isinstance(call.func, ast.Attribute):
                        self.assertNotIn(call.func.attr, {'validate', 'compile', 'persist', 'execute', 'resolve_aliases'})
