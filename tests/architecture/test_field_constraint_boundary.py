from dataclasses import fields
from pathlib import Path
from typing import get_type_hints
import unittest
from architecture_fitness.discovery import discover
from architecture_fitness.engine import execute
from model_core.public import (
    FieldConstraintSet, FieldPresence, FieldNullability, ConstraintKind, ValueConstraint,
    FieldDefinition, NumericConstraintValue, MinLengthConstraint, MaxLengthConstraint,
    MinimumConstraint, MaximumConstraint, PrecisionConstraint, ScaleConstraint, PatternConstraint,
)
from semantic_kernel.public import SemanticElement

ROOT = Path(__file__).resolve().parents[2]


class FieldConstraintBoundaryTests(unittest.TestCase):
    def test_constraints_owned_by_model_and_no_infrastructure_dependency(self):
        for cls in (FieldConstraintSet, FieldPresence, FieldNullability, ConstraintKind, ValueConstraint, NumericConstraintValue, MinLengthConstraint, MaxLengthConstraint, MinimumConstraint, MaximumConstraint, PrecisionConstraint, ScaleConstraint, PatternConstraint):
            self.assertEqual(cls.__module__, 'model_core.public')
            self.assertNotIn(SemanticElement, cls.__mro__)
        model = discover(ROOT)
        self.assertEqual(model.graph('observed')['semantic-kernel'], set())
        self.assertEqual(model.graph('observed')['model-core'], {'semantic-kernel'})
        imports = {name.split('.')[0] for source in model.sources if source.owner == 'model-core' for name, line in source.targets}
        self.assertEqual(imports, {'dataclasses', 're', 'enum', 'decimal', 'typing', 'types', 'model_core', 'semantic_kernel'})
        self.assertEqual(execute(model)['summary']['status'], 'HEALTHY')

    def test_typed_canonical_shape_with_distinct_axes_no_metadata_bag(self):
        self.assertEqual({f.name: f.type for f in fields(FieldConstraintSet)}, {'presence': FieldPresence, 'nullability': FieldNullability, 'value_constraints': tuple[ValueConstraint, ...]})
        self.assertIsNot(FieldPresence, FieldNullability)
        self.assertIs(get_type_hints(FieldDefinition)['constraints'], FieldConstraintSet)
        self.assertEqual({f.name for f in fields(FieldDefinition)}, {'id', 'name', 'type', 'constraints'})
        self.assertIs(get_type_hints(ValueConstraint.kind.fget)['return'], ConstraintKind)
        self.assertIsNone(ValueConstraint.kind.fset)

    def test_definitions_have_no_execution_projection_or_identity_members(self):
        for cls in (FieldConstraintSet, MinLengthConstraint, MaxLengthConstraint, MinimumConstraint, MaximumConstraint, PrecisionConstraint, ScaleConstraint, PatternConstraint):
            for member in ('id', 'version', 'severity', 'error_message', 'label', 'sql', 'engine', 'validate', 'compile', 'render', 'supports', 'to_json_schema', 'generate_migration', 'type'):
                self.assertFalse(hasattr(cls, member), (cls, member))
