from dataclasses import replace, FrozenInstanceError
import json
import unittest
from semantic_kernel.public import FacetDefinition, FacetKinds, SemanticElementKinds
from model_core.public import DataFacet, DataFacetError, TypeDataComposition, DATA_FACET_APPLICABILITY, FieldId, FieldName, FieldDefinition
from test_semantic_element import TestTypeDefinition, ID, CONTEXT
from semantic_kernel.public import QualifiedName, SemanticVersion


def customer():
    return TestTypeDefinition(ID, QualifiedName.parse('sales.Customer'), CONTEXT, SemanticElementKinds.TYPE_DEFINITION, SemanticVersion(1, 0, 0))


def data():
    return DataFacet([FieldDefinition(FieldId(f'fld_550e8400-e29b-41d4-a716-{i:012d}'), FieldName(name)) for i, name in enumerate(('name', 'active', 'creditLimit'))])


def read_facet(facet: FacetDefinition):
    return facet.kind


def from_wire(wire):
    if wire['kind'] != str(FacetKinds.DATA):
        raise ValueError('Expected data discriminator')
    return DataFacet([FieldDefinition(FieldId.parse(f['id']), FieldName.parse(f['name'])) for f in wire['fields']])


class DataFacetContractTests(unittest.TestCase):
    def test_structural_facet_integration(self):
        self.assertIs(read_facet(data()), FacetKinds.DATA)

    def test_minimal_composition_retains_core_host_and_single_source(self):
        host, facet = customer(), data()
        composition = TypeDataComposition(host, facet)
        self.assertIs(composition.type_definition, host)
        self.assertIs(composition.data, facet)
        self.assertFalse(hasattr(host, 'fields'))
        self.assertFalse(hasattr(composition, 'fields'))
        with self.assertRaises(FrozenInstanceError):
            composition.data = DataFacet(())

    def test_missing_is_distinct_from_explicit_empty(self):
        host = customer()
        absent = TypeDataComposition(host)
        empty = TypeDataComposition(host, DataFacet(()))
        self.assertIsNone(absent.data)
        self.assertIsNotNone(empty.data)
        self.assertEqual(empty.data.fields, ())
        self.assertNotEqual(absent, empty)

    def test_duplicate_facets_are_rejected_never_merged(self):
        with self.assertRaises(DataFacetError) as caught:
            TypeDataComposition(customer(), [data(), DataFacet(())])
        self.assertEqual(caught.exception.code, 'TYPE-DATA-005')

    def test_applicability_rejects_non_type_host(self):
        self.assertEqual(DATA_FACET_APPLICABILITY.allowed_element_kinds, frozenset({SemanticElementKinds.TYPE_DEFINITION}))
        for kind in (SemanticElementKinds.POLICY_DEFINITION, SemanticElementKinds.ACTION_DEFINITION):
            with self.assertRaises(DataFacetError) as caught:
                TypeDataComposition(replace(customer(), kind=kind), data())
            self.assertEqual(caught.exception.code, 'TYPE-DATA-006')
        with self.assertRaises(DataFacetError):
            TypeDataComposition(object(), data())

    def test_internal_wire_round_trip_preserves_order_and_ids(self):
        facet = data()
        wire = {'kind': str(facet.kind), 'fields': [{'id': str(f.id), 'name': str(f.name)} for f in facet.fields]}
        self.assertEqual(from_wire(json.loads(json.dumps(wire))), facet)
        self.assertEqual([f['name'] for f in wire['fields']], ['name', 'active', 'creditLimit'])
        self.assertEqual(from_wire({'kind': 'data', 'fields': []}), DataFacet(()))
        with self.assertRaises(TypeError):
            json.dumps(facet)

    def test_invalid_internal_wire_is_validated(self):
        with self.assertRaises(ValueError):
            from_wire({'kind': 'policy', 'fields': []})
        field = {'id': 'fld_550e8400-e29b-41d4-a716-000000000000', 'name': 'name'}
        with self.assertRaises(DataFacetError):
            from_wire({'kind': 'data', 'fields': [field, field]})

    def test_demo_customer_v1_and_rename_snapshot(self):
        composed = TypeDataComposition(customer(), data())
        self.assertEqual(str(composed.type_definition.qualified_name), 'sales.Customer')
        self.assertEqual(str(composed.type_definition.version), '1.0.0')
        self.assertEqual([str(f.name) for f in composed.data.fields], ['name', 'active', 'creditLimit'])
        renamed = replace(composed.data.fields[2], name=FieldName('creditCeiling'))
        evolved = TypeDataComposition(replace(customer(), version=SemanticVersion(2, 0, 0)), DataFacet([*composed.data.fields[:2], renamed]))
        self.assertEqual(composed.data.fields[2].id, evolved.data.fields[2].id)
