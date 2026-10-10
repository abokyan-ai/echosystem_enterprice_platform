from dataclasses import fields
from pathlib import Path
import unittest
from architecture_fitness.discovery import discover
from architecture_fitness.engine import execute
from model_core.public import FieldDefinition, FieldId, FieldName, FieldConstraintSet
from semantic_kernel.public import SemanticElement

ROOT = Path(__file__).resolve().parents[2]


class FieldBoundaryTests(unittest.TestCase):
    def test_fields_are_owned_by_model_and_kernel_remains_independent(self):
        for value in (FieldId, FieldName, FieldDefinition):
            self.assertEqual(value.__module__, 'model_core.public')
        model = discover(ROOT)
        self.assertEqual(model.graph('observed')['semantic-kernel'], set())
        self.assertEqual(model.graph('observed')['model-core'], {'semantic-kernel'})
        self.assertEqual(execute(model)['summary']['status'], 'HEALTHY')

    def test_snapshot_contains_only_three_model_owned_typed_members(self):
        self.assertEqual({field.name: field.type for field in fields(FieldDefinition)}, {'id': FieldId, 'name': FieldName, 'constraints': FieldConstraintSet})
        self.assertNotIn(SemanticElement, FieldDefinition.__mro__)
        for name in ('qualified_name', 'context', 'kind', 'version', 'type', 'required', 'nullable', 'default', 'order', 'ordinal', 'column_name', 'label', 'owner', 'registry', 'resolve', 'compile', 'persist'):
            self.assertFalse(hasattr(FieldDefinition, name), name)

    def test_model_public_boundary_has_only_foundational_imports(self):
        model = discover(ROOT)
        imports = {name.split('.')[0] for source in model.sources if source.owner == 'model-core' for name, line in source.targets}
        self.assertEqual(imports, {'dataclasses', 're', 'semantic_kernel', 'enum', 'decimal', 'typing', 'model_core'})
