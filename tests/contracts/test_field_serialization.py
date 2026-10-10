"""TYPE-02 test-only evolving model mapping; not a final public wire schema."""
import json
import unittest
from model_core.public import FieldId, FieldIdError, FieldName, FieldNameError, FieldDefinition

ID = 'fld_550e8400-e29b-41d4-a716-446655440000'


def from_internal_wire(wire):
    return FieldDefinition.create(FieldId.parse(wire.get('id')), FieldName.parse(wire.get('name')))


class FieldSerializationTests(unittest.TestCase):
    def test_scalar_id_and_name_round_trips(self):
        for value in (FieldId(ID), FieldName('creditLimit')):
            self.assertEqual(type(value).parse(json.loads(json.dumps(str(value)))), value)

    def test_evolving_two_field_internal_model_round_trip(self):
        field = FieldDefinition.create(FieldId(ID), FieldName('creditLimit'))
        wire = {'id': str(field.id), 'name': str(field.name)}
        self.assertEqual(from_internal_wire(json.loads(json.dumps(wire))), field)
        self.assertEqual(set(wire), {'id', 'name'})

    def test_invalid_and_missing_serialized_values(self):
        for wire in ({}, {'name': 'name'}, {'id': 'bad', 'name': 'name'}):
            with self.assertRaises(FieldIdError):
                from_internal_wire(wire)
        for wire in ({'id': ID}, {'id': ID, 'name': 'credit limit'}):
            with self.assertRaises(FieldNameError):
                from_internal_wire(wire)
        for scalar in (None, True, 1, [], {}):
            for constructor in (FieldId, FieldName):
                with self.assertRaises(ValueError):
                    constructor.parse(json.loads(json.dumps(scalar)))

    def test_id_case_normalizes_name_case_remains_exact(self):
        field = from_internal_wire({'id': 'fld_' + ID[4:].upper(), 'name': 'CreditLimit'})
        self.assertEqual(str(field.id), ID)
        self.assertEqual(str(field.name), 'CreditLimit')

    def test_serializer_requires_explicit_mapping(self):
        for value in (FieldId(ID), FieldName('name'), FieldDefinition(FieldId(ID), FieldName('name'))):
            with self.assertRaises(TypeError):
                json.dumps(value)

    def test_demo_rename_identity_without_compatibility_classification(self):
        a = FieldDefinition(FieldId(ID), FieldName('creditLimit'))
        b = FieldDefinition(a.id, FieldName('creditCeiling'))
        self.assertEqual(a.id, b.id)
        self.assertNotEqual(a.name, b.name)
        self.assertNotEqual(a, b)
