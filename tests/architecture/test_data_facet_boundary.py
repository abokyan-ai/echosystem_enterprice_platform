from dataclasses import fields
from pathlib import Path
from typing import get_type_hints
import unittest
from architecture_fitness.discovery import discover
from architecture_fitness.engine import execute
from model_core.public import DataFacet, TypeDataComposition, FieldDefinition
from semantic_kernel.public import FacetKind, SemanticElement

ROOT = Path(__file__).resolve().parents[2]


class DataFacetBoundaryTests(unittest.TestCase):
    def test_model_placement_dependency_direction_and_fitness(self):
        self.assertEqual(DataFacet.__module__, 'model_core.public')
        self.assertNotIn(SemanticElement, DataFacet.__mro__)
        model = discover(ROOT)
        self.assertEqual(model.graph('observed')['semantic-kernel'], set())
        self.assertEqual(model.graph('observed')['model-core'], {'semantic-kernel'})
        self.assertEqual(execute(model)['summary']['status'], 'HEALTHY')

    def test_only_ordered_fields_and_readonly_typed_fixed_kind(self):
        self.assertEqual({f.name: f.type for f in fields(DataFacet)}, {'fields': tuple[FieldDefinition, ...]})
        self.assertIs(get_type_hints(DataFacet.kind.fget)['return'], FacetKind)
        self.assertIsNone(DataFacet.kind.fset)
        for name in ('id', 'owner', 'version', 'table_name', 'indexes', 'values', 'compile', 'persist', 'render'):
            self.assertFalse(hasattr(DataFacet, name))

    def test_wrapper_has_no_duplicate_fields_or_general_metadata_bag(self):
        self.assertEqual({f.name for f in fields(TypeDataComposition)}, {'type_definition', 'data'})
        self.assertFalse(hasattr(TypeDataComposition, 'fields'))
        self.assertEqual({f.name for f in fields(FieldDefinition)}, {'id', 'name'})
