from dataclasses import dataclass, FrozenInstanceError
from typing import get_type_hints
import json
import unittest
from semantic_kernel.public import FacetDefinition, FacetKind, FacetKindError, FacetKinds, FacetApplicability, SemanticElement, SemanticElementKinds


@dataclass(frozen=True, slots=True)
class TestFacet:
    kind: FacetKind

    def __post_init__(self):
        if not isinstance(self.kind, FacetKind):
            raise TypeError('Test facet requires a FacetKind')


def read_facet(facet: FacetDefinition) -> FacetKind:
    return facet.kind


class FacetContractTests(unittest.TestCase):
    def test_structural_facet_consumer_preserves_core_and_custom_kind(self):
        for kind in (FacetKinds.DATA, FacetKind('acme.routing')):
            facet: FacetDefinition = TestFacet(kind)
            self.assertIs(read_facet(facet), kind)
        self.assertNotIn(FacetDefinition, TestFacet.__mro__)
        self.assertNotIn(SemanticElement, FacetDefinition.__mro__)
        self.assertIsNone(FacetDefinition.kind.fset)
        self.assertIs(get_type_hints(FacetDefinition.kind.fget)['return'], FacetKind)

    def test_test_only_snapshot_is_typed_and_frozen(self):
        for value in (None, 'data'):
            with self.assertRaises(TypeError):
                TestFacet(value)
        with self.assertRaises(FrozenInstanceError):
            TestFacet(FacetKinds.DATA).kind = FacetKinds.POLICY
        with self.assertRaises(TypeError):
            FacetDefinition()
        with self.assertRaises(TypeError):
            isinstance(TestFacet(FacetKinds.DATA), FacetDefinition)

    def test_core_and_custom_kind_scalar_json_round_trip(self):
        for kind in (*FacetKinds.ALL, FacetKind('acme.routing')):
            encoded = json.dumps(str(kind))
            self.assertEqual(FacetKind.parse(json.loads(encoded)), kind)
            wire = json.dumps({'kind': str(kind)})
            self.assertEqual(FacetKind.parse(json.loads(wire)['kind']), kind)
        self.assertEqual(json.dumps(str(FacetKind('acme.routing'))), '"acme.routing"')

    def test_invalid_serialized_kind_values_are_rejected(self):
        for wire in ('null', '""', '" "', '"Data"', '"Policy Facet"', '"acme..routing"', 'true', '123', '[]', '{}'):
            with self.subTest(wire=wire), self.assertRaises(FacetKindError):
                FacetKind.parse(json.loads(wire))

    def test_no_automatic_or_polymorphic_facet_serializer(self):
        for value in (FacetKinds.DATA, TestFacet(FacetKinds.DATA)):
            with self.assertRaises(TypeError):
                json.dumps(value)

    def test_applicability_does_not_mean_presence_or_requirement(self):
        rule = FacetApplicability(FacetKinds.DATA, frozenset({SemanticElementKinds.TYPE_DEFINITION}))
        self.assertIn(SemanticElementKinds.TYPE_DEFINITION, rule.allowed_element_kinds)
        # This is illustrative declaration only, not a platform-wide Data matrix.
        self.assertFalse(hasattr(rule, 'required'))
        self.assertFalse(hasattr(rule, 'present'))
        self.assertFalse(hasattr(SemanticElement, 'facets'))

    def test_demo_core_custom_applicability_and_invalid_kind(self):
        self.assertEqual(FacetKind.parse('data'), FacetKinds.DATA)
        self.assertTrue(FacetKinds.is_core(FacetKinds.DATA))
        custom = FacetKind.parse('acme.routing')
        self.assertFalse(FacetKinds.is_core(custom))
        self.assertEqual(FacetKind.parse(str(custom)), custom)
        self.assertEqual(read_facet(TestFacet(custom)), custom)
        rule = FacetApplicability(FacetKinds.DATA, frozenset({SemanticElementKinds.TYPE_DEFINITION}))
        self.assertIn(SemanticElementKinds.TYPE_DEFINITION, rule.allowed_element_kinds)
        with self.assertRaises(FacetKindError) as caught:
            FacetKind.parse('Data Facet')
        self.assertEqual(caught.exception.code, 'SEM-FACET-KIND-002')
