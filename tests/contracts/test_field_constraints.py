from semantic_kernel.public import PrimitiveTypes
from model_core.public import PrimitiveTypeRef
from dataclasses import replace
import json
import unittest
from model_core.public import (
    FieldConstraintSet, FieldPresence, FieldNullability, FieldConstraintError,
    MaxLengthConstraint, MinimumConstraint, MaximumConstraint, MinLengthConstraint,
    PrecisionConstraint, ScaleConstraint, PatternConstraint, ValueConstraint,
    FieldDefinition, FieldId, FieldName, DataFacet, TypeDataComposition,
)
from model_core.constraint_wire import constraints_to_wire, constraints_from_wire, field_to_wire, field_from_wire
from test_data_facet import customer
from semantic_kernel.public import SemanticVersion


def sales_fields():
    specs = (
        ('name', FieldPresence.REQUIRED, FieldNullability.NON_NULL, [MaxLengthConstraint(200)]),
        ('middleName', FieldPresence.OPTIONAL, FieldNullability.NULLABLE, []),
        ('creditLimit', FieldPresence.OPTIONAL, FieldNullability.NON_NULL, [MinimumConstraint('0'), PrecisionConstraint(18), ScaleConstraint(2)]),
    )
    return tuple(FieldDefinition(FieldId(f'fld_550e8400-e29b-41d4-a716-{i:012d}'), FieldName(name), PrimitiveTypeRef({'name': PrimitiveTypes.STRING, 'middleName': PrimitiveTypes.STRING, 'creditLimit': PrimitiveTypes.DECIMAL}[name]), FieldConstraintSet(p, n, values)) for i, (name, p, n, values) in enumerate(specs))


def read_definition(value: ValueConstraint):
    return value.kind


class ConstraintContractTests(unittest.TestCase):
    def test_pure_structural_contract(self):
        value = MaxLengthConstraint(200)
        self.assertEqual(str(read_definition(value)), 'max-length')
        with self.assertRaises(TypeError):
            ValueConstraint()
        for method in ('validate', 'compile', 'to_sql_check', 'to_json_schema', 'supports', 'is_breaking', 'generate_migration'):
            self.assertFalse(hasattr(value, method))

    def test_sales_demo_actual_mapping(self):
        fields = sales_fields()
        self.assertEqual([str(f.name) for f in fields], ['name', 'middleName', 'creditLimit'])
        wire = field_to_wire(fields[2])
        self.assertEqual(wire['constraints'], {'presence': 'optional', 'nullability': 'non-null', 'values': [{'kind': 'minimum', 'value': '0'}, {'kind': 'precision', 'value': 18}, {'kind': 'scale', 'value': 2}]})
        self.assertEqual(wire['type'], {'kind': 'primitive', 'primitive': 'decimal'})
        for field in fields:
            self.assertEqual(field_from_wire(json.loads(json.dumps(field_to_wire(field)))), field)

    def test_all_four_states_wire_round_trip(self):
        for presence in FieldPresence:
            for nullability in FieldNullability:
                cs = FieldConstraintSet(presence, nullability, [])
                self.assertEqual(constraints_from_wire(json.loads(json.dumps(constraints_to_wire(cs)))), cs)

    def test_future_missing_null_truth_table_documented_not_executed(self):
        # Expectations encode independent axes, not an instance validation engine.
        table = {
            ('required', 'non-null'): (False, False),
            ('required', 'nullable'): (False, True),
            ('optional', 'non-null'): (True, False),
            ('optional', 'nullable'): (True, True),
        }
        for presence in FieldPresence:
            for nullability in FieldNullability:
                cs = FieldConstraintSet(presence, nullability, [])
                self.assertEqual((cs.presence is FieldPresence.OPTIONAL, cs.nullability is FieldNullability.NULLABLE), table[(presence.value, nullability.value)])

    def test_all_builtin_payloads_round_trip_and_canonical_order(self):
        cs = FieldConstraintSet(FieldPresence.REQUIRED, FieldNullability.NULLABLE, [ScaleConstraint(2), PrecisionConstraint(18), PatternConstraint('[a-z]+'), MaximumConstraint('0001.1000'), MinimumConstraint('-01'), MinLengthConstraint(0), MaxLengthConstraint(200)])
        wire = constraints_to_wire(cs)
        self.assertEqual([c['kind'] for c in wire['values']], sorted(c['kind'] for c in wire['values']))
        self.assertEqual(constraints_from_wire(json.loads(json.dumps(wire))), cs)
        self.assertIs(type(next(c['value'] for c in wire['values'] if c['kind'] == 'maximum')), str)
        equivalent = replace(cs, value_constraints=tuple(reversed(cs.value_constraints)))
        self.assertEqual(json.dumps(wire), json.dumps(constraints_to_wire(equivalent)))

    def test_missing_explicit_states_and_unknown_members_rejected(self):
        wire = {'presence': 'optional', 'nullability': 'non-null', 'values': []}
        for key in wire:
            missing = dict(wire)
            missing.pop(key)
            with self.assertRaises(FieldConstraintError):
                constraints_from_wire(missing)
        with self.assertRaises(FieldConstraintError):
            constraints_from_wire({**wire, 'default': None})
        for values in (None, {}, (), True):
            with self.assertRaises(FieldConstraintError):
                constraints_from_wire({**wire, 'values': values})

    def test_reject_noncanonical_wire_enums(self):
        wire = {'presence': 'required', 'nullability': 'non-null', 'values': []}
        for key, invalid in (('presence', 'Required'), ('presence', True), ('presence', FieldPresence.REQUIRED), ('nullability', 'not-null'), ('nullability', 0), ('nullability', FieldNullability.NON_NULL)):
            with self.assertRaises(FieldConstraintError):
                constraints_from_wire({**wire, key: invalid})

    def test_invalid_vs_unsupported_wire_kind(self):
        wire = {'presence': 'required', 'nullability': 'non-null', 'values': [{'kind': 'acme.routing-code', 'value': 'x'}]}
        with self.assertRaises(FieldConstraintError) as caught:
            constraints_from_wire(wire)
        self.assertEqual(caught.exception.code, 'TYPE-CONSTRAINT-014')
        wire['values'][0]['kind'] = 'Acme.Bad'
        with self.assertRaises(FieldConstraintError) as caught:
            constraints_from_wire(wire)
        self.assertEqual(caught.exception.code, 'TYPE-CONSTRAINT-012')

    def test_malformed_payloads_use_model_invariants(self):
        wire = {'presence': 'required', 'nullability': 'non-null', 'values': []}
        for entries, code in (([{'kind': 'minimum', 'value': 0.1}], '013'), ([{'kind': 'scale', 'value': -1}], '006'), ([{'kind': 'max-length', 'value': 10}, {'kind': 'max-length', 'value': 20}], '008'), ([{'kind': 'minimum', 'value': '10'}, {'kind': 'maximum', 'value': '2'}], '004'), ([{'kind': 'scale', 'value': 6}, {'kind': 'precision', 'value': 5}], '007')):
            with self.assertRaises(FieldConstraintError) as caught:
                constraints_from_wire({**wire, 'values': entries})
            self.assertEqual(caught.exception.code, 'TYPE-CONSTRAINT-' + code)
        for entries in ([None], [{'kind': 'pattern', 'value': 'x', 'engine': 'python'}], [{'kind': 'pattern'}]):
            with self.assertRaises(FieldConstraintError):
                constraints_from_wire({**wire, 'values': entries})

    def test_round_trip_does_not_alias_mutable_wire(self):
        original = sales_fields()[2]
        wire = field_to_wire(original)
        restored = field_from_wire(wire)
        wire['constraints']['values'].clear()
        self.assertEqual(restored, original)
        fresh = field_to_wire(restored)
        self.assertEqual(len(fresh['constraints']['values']), 3)

    def test_demo_type_composition_and_new_owner_version(self):
        fields = sales_fields()
        original = TypeDataComposition(customer(), DataFacet(fields))
        name = replace(fields[0], constraints=FieldConstraintSet(FieldPresence.REQUIRED, FieldNullability.NON_NULL, [MaxLengthConstraint(100)]))
        evolved = TypeDataComposition(replace(customer(), version=SemanticVersion(2, 0, 0)), DataFacet((name, *fields[1:])))
        self.assertEqual(original.data.fields[0].id, evolved.data.fields[0].id)
        self.assertNotEqual(original.data, evolved.data)
        self.assertEqual(str(original.type_definition.version), '1.0.0')
        self.assertEqual(str(evolved.type_definition.version), '2.0.0')
