from dataclasses import fields
from pathlib import Path
from typing import get_args, get_type_hints
import unittest
from architecture_fitness.discovery import discover
from architecture_fitness.engine import execute
from model_core.public import TypeRef, TypeRefKind, PrimitiveTypeRef, SemanticTypeRef, FieldDefinition
from semantic_kernel.public import PrimitiveType, PrimitiveTypes, ElementRef

ROOT = Path(__file__).resolve().parents[2]


class TypeReferenceBoundaryTests(unittest.TestCase):
    def test_closed_algebra_exact_payload_shape_and_required_typed_field(self):
        self.assertEqual(set(get_args(TypeRef)), {PrimitiveTypeRef, SemanticTypeRef})
        self.assertIs(get_type_hints(FieldDefinition)['type'], TypeRef)
        self.assertEqual({f.name: f.type for f in fields(PrimitiveTypeRef)}, {'primitive': PrimitiveType})
        self.assertEqual({f.name: f.type for f in fields(SemanticTypeRef)}, {'target': ElementRef})
        self.assertEqual({k.value for k in TypeRefKind}, {'primitive', 'semantic'})
        self.assertFalse(any(str(p) in ('any', 'object', 'dynamic', 'unknown') for p in PrimitiveTypes.ALL))

    def test_kernel_primitives_model_specific_refs_and_direction(self):
        self.assertEqual(PrimitiveType.__module__, 'semantic_kernel.public')
        for cls in (TypeRefKind, PrimitiveTypeRef, SemanticTypeRef):
            self.assertEqual(cls.__module__, 'model_core.public')
        model = discover(ROOT)
        self.assertEqual(model.graph('observed')['semantic-kernel'], set())
        self.assertEqual(model.graph('observed')['model-core'], {'semantic-kernel'})
        self.assertEqual(execute(model)['summary']['status'], 'HEALTHY')

    def test_refs_expose_no_names_versions_objects_or_physical_execution(self):
        for cls in (PrimitiveTypeRef, SemanticTypeRef):
            self.assertIs(get_type_hints(cls.kind.fget)['return'], TypeRefKind)
            self.assertIsNone(cls.kind.fset)
            for name in ('qualified_name', 'definition', 'version', 'registry', 'resolver', 'context', 'runtime_type', 'sql_type', 'nullable', 'presence', 'cardinality', 'resolve', 'load', 'lookup', 'supports', 'allowed_constraints', 'compile', 'validate', 'is_assignable_from', 'coerce'):
                self.assertFalse(hasattr(cls, name), (cls, name))
