from semantic_kernel.public import PrimitiveTypes
from model_core.public import PrimitiveTypeRef
"""TYPE-02 test-only evolving model mapping; not a final public wire schema."""
import json
import unittest
from model_core.constraint_wire import field_from_wire, field_to_wire
from model_core.public import FieldConstraintSet, FieldPresence, FieldNullability, FieldId, FieldIdError, FieldName, FieldNameError, FieldDefinition

PLAIN = FieldConstraintSet(FieldPresence.REQUIRED, FieldNullability.NON_NULL, ())
ID = 'fld_550e8400-e29b-41d4-a716-446655440000'


def from_internal_wire(wire):
    return field_from_wire(wire)


class FieldSerializationTests(unittest.TestCase):
    def test_scalar_id_and_name_round_trips(self):
        for value in (FieldId(ID), FieldName('creditLimit')):
            self.assertEqual(type(value).parse(json.loads(json.dumps(str(value)))), value)

    def test_evolving_four_field_internal_model_round_trip(self):
        field = FieldDefinition.create(FieldId(ID), FieldName('creditLimit'), PrimitiveTypeRef(PrimitiveTypes.STRING), PLAIN)
        wire = field_to_wire(field)
        self.assertEqual(from_internal_wire(json.loads(json.dumps(wire))), field)
        self.assertEqual(set(wire), {'id', 'name', 'type', 'constraints'})

    def test_invalid_and_missing_serialized_values(self):
        for wire in ({}, {'name': 'name'}, {'id': ID, 'name': 'name'}):
            with self.assertRaises(ValueError):
                from_internal_wire(wire)
        for wire in ({'id': 'bad', 'name': 'name'}, {'id': ID, 'name': 'credit limit'}):
            with self.assertRaises(ValueError):
                from_internal_wire({**wire, 'type': {'kind': 'primitive', 'primitive': 'string'}, 'constraints': field_to_wire(FieldDefinition(FieldId(ID), FieldName('name'), PrimitiveTypeRef(PrimitiveTypes.STRING), PLAIN))['constraints']})
        for scalar in (None, True, 1, [], {}):
            for constructor in (FieldId, FieldName):
                with self.assertRaises(ValueError):
                    constructor.parse(json.loads(json.dumps(scalar)))

    def test_id_case_normalizes_name_case_remains_exact(self):
        field = from_internal_wire({'id': 'fld_' + ID[4:].upper(), 'name': 'CreditLimit', 'type': {'kind': 'primitive', 'primitive': 'string'}, 'constraints': {'presence': 'required', 'nullability': 'non-null', 'values': []}})
        self.assertEqual(str(field.id), ID)
        self.assertEqual(str(field.name), 'CreditLimit')

    def test_serializer_requires_explicit_mapping(self):
        for value in (FieldId(ID), FieldName('name'), FieldDefinition(FieldId(ID), FieldName('name'), PrimitiveTypeRef(PrimitiveTypes.STRING), PLAIN)):
            with self.assertRaises(TypeError):
                json.dumps(value)

    def test_demo_rename_identity_without_compatibility_classification(self):
        a = FieldDefinition(FieldId(ID), FieldName('creditLimit'), PrimitiveTypeRef(PrimitiveTypes.STRING), PLAIN)
        b = FieldDefinition(a.id, FieldName('creditCeiling'), PrimitiveTypeRef(PrimitiveTypes.STRING), PLAIN)
        self.assertEqual(a.id, b.id)
        self.assertNotEqual(a.name, b.name)
        self.assertNotEqual(a, b)
