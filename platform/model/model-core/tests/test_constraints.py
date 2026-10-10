from dataclasses import FrozenInstanceError, replace
from decimal import localcontext
import re
import unittest
from model_core.public import (
    FieldPresence, FieldNullability, ConstraintKind, ConstraintKinds,
    FieldConstraintError, FieldConstraintSet, NumericConstraintValue,
    MinLengthConstraint, MaxLengthConstraint, MinimumConstraint, MaximumConstraint,
    PrecisionConstraint, ScaleConstraint, PatternConstraint,
    FieldDefinition, FieldDefinitionError, FieldId, FieldName, DataFacet, DataFacetError,
)


def constraints(*values, presence=FieldPresence.REQUIRED, nullability=FieldNullability.NON_NULL):
    return FieldConstraintSet.create(presence, nullability, list(values))


def field(cs, name='creditLimit', number=0):
    return FieldDefinition.create(FieldId(f'fld_550e8400-e29b-41d4-a716-{number:012d}'), FieldName(name), cs)


class ConstraintKindTests(unittest.TestCase):
    def test_open_identifier_round_trip(self):
        for text in ('min-length', 'acme.routing-code', 'future.v2'):
            kind = ConstraintKind.parse(text)
            self.assertEqual(str(kind), text)
            self.assertEqual(kind, ConstraintKind.try_parse(text))
            self.assertEqual(hash(kind), hash(ConstraintKind(text)))
        self.assertFalse(ConstraintKinds.is_core(ConstraintKind('acme.routing-code')))

    def test_invalid_identifier_is_distinct_from_unsupported(self):
        for text in (None, '', True, {}, ' min-length', 'MinLength', 'acme..foo', '-min', 'foo-', 'foo--bar', 'á', 'foo\n', '.foo'):
            with self.subTest(text=text), self.assertRaises(FieldConstraintError) as caught:
                ConstraintKind(text)
            self.assertEqual(caught.exception.code, 'TYPE-CONSTRAINT-012')
            self.assertIsNone(ConstraintKind.try_parse(text))

    def test_catalog_is_fixed_and_typed(self):
        self.assertEqual({str(k) for k in ConstraintKinds.ALL}, {'min-length', 'max-length', 'minimum', 'maximum', 'pattern', 'precision', 'scale'})
        self.assertTrue(all(ConstraintKinds.is_core(k) for k in ConstraintKinds.ALL))
        self.assertFalse(ConstraintKinds.is_core('minimum'))
        with self.assertRaises(FrozenInstanceError):
            ConstraintKinds.MINIMUM = ConstraintKind('other')

    def test_kind_plain_string_and_immutability(self):
        class Tricky(str):
            def __str__(self):
                return 'other'
        kind = ConstraintKind(Tricky('acme.routing-code'))
        self.assertIs(type(kind.value), str)
        self.assertEqual(str(kind), 'acme.routing-code')
        with self.assertRaises(FrozenInstanceError):
            kind.value = 'other'


class NumericConstraintTests(unittest.TestCase):
    def test_exact_literal_and_round_trip(self):
        for text in ('-100', '0', '1', '10.25', '999999999999.9999', '0.1'):
            value = NumericConstraintValue.parse(text)
            self.assertEqual(str(value), text)
            self.assertEqual(value, NumericConstraintValue.parse(str(value)))

    def test_canonical_equivalent_values_and_signed_zero(self):
        for text, expected in (('001.000', '1'), ('-000.000', '0'), ('000.1000', '0.1'), ('-003.500', '-3.5')):
            self.assertEqual(str(NumericConstraintValue(text)), expected)
            self.assertEqual(hash(NumericConstraintValue(text)), hash(NumericConstraintValue(expected)))

    def test_reject_non_exact_types_and_spellings(self):
        for value in (0.1, 1, True, None, '', '1e2', '+1', ' 1', '1 ', '.1', '1.', 'NaN', 'Infinity', '1,2', '١', [], {}):
            with self.subTest(value=value), self.assertRaises(FieldConstraintError) as caught:
                NumericConstraintValue(value)
            self.assertEqual(caught.exception.code, 'TYPE-CONSTRAINT-013')
            self.assertIsNone(NumericConstraintValue.try_parse(value))

    def test_representation_limit_without_int_conversion(self):
        text = '9' * 4096
        self.assertEqual(str(NumericConstraintValue(text)), text)
        with self.assertRaises(FieldConstraintError):
            NumericConstraintValue('9' * 4097)
        self.assertEqual(str(NumericConstraintValue('-0.' + '1' * 4095)), '-0.' + '1' * 4095)

    def test_bound_convenience_retains_exact_typed_payload(self):
        value = NumericConstraintValue('0.1')
        self.assertIs(MinimumConstraint(value).value, value)
        self.assertEqual(MaximumConstraint('0.1000').value, value)
        for cls in (MinimumConstraint, MaximumConstraint):
            for bad in (0.1, 1, None, True):
                with self.assertRaises(FieldConstraintError):
                    cls(bad)

    def test_comparison_independent_of_decimal_context(self):
        a = '123456789012345678901234567890.00000000000000000001'
        b = '123456789012345678901234567890.00000000000000000002'
        with localcontext() as context:
            context.prec = 1
            context.traps.update({signal: True for signal in context.traps})
            constraints(MinimumConstraint(a), MaximumConstraint(b))
            with self.assertRaises(FieldConstraintError) as caught:
                constraints(MinimumConstraint(b), MaximumConstraint(a))
            self.assertEqual(caught.exception.code, 'TYPE-CONSTRAINT-004')

    def test_negative_numeric_order_not_lexical_order(self):
        constraints(MinimumConstraint('-100'), MaximumConstraint('-2'))
        with self.assertRaises(FieldConstraintError):
            constraints(MinimumConstraint('10'), MaximumConstraint('2'))

    def test_numeric_snapshot_is_immutable(self):
        bound = MinimumConstraint('1.0')
        with self.assertRaises(FrozenInstanceError):
            bound.value.value = '2'
        with self.assertRaises(FrozenInstanceError):
            bound.value = NumericConstraintValue('2')


class ConcreteConstraintTests(unittest.TestCase):
    def test_integer_domains(self):
        for cls in (MinLengthConstraint, MaxLengthConstraint, ScaleConstraint):
            for value in (0, 1, 100, 10**30):
                self.assertEqual(cls(value).value, value)
        for value in (1, 18, 38, 10**30):
            self.assertEqual(PrecisionConstraint(value).value, value)

    def test_integer_diagnostics_reject_bool_float_and_subclasses(self):
        class Integer(int):
            pass
        for cls, code in ((MinLengthConstraint, '001'), (MaxLengthConstraint, '002'), (PrecisionConstraint, '005'), (ScaleConstraint, '006')):
            for value in (-1, True, 1.0, None, '1', Integer(1)):
                with self.subTest(cls=cls, value=value), self.assertRaises(FieldConstraintError) as caught:
                    cls(value)
                self.assertEqual(caught.exception.code, 'TYPE-CONSTRAINT-' + code)
        with self.assertRaises(FieldConstraintError):
            PrecisionConstraint(0)

    def test_kind_is_readonly_and_not_caller_controlled(self):
        for constraint in (MinLengthConstraint(0), MaxLengthConstraint(0), MinimumConstraint('0'), MaximumConstraint('0'), PatternConstraint('['), PrecisionConstraint(1), ScaleConstraint(0)):
            self.assertIsNone(type(constraint).kind.fset)
            self.assertIn(constraint.kind, ConstraintKinds.ALL)
            with self.assertRaises(FrozenInstanceError):
                constraint.value = None
            with self.assertRaises(TypeError):
                type(constraint)(value=constraint.value, kind=ConstraintKind('acme.other'))

    def test_pattern_preserved_without_regex_execution_or_syntax_claim(self):
        for text in ('^[A-Z]+$', '[', ' ', 'a\nb', 'a' * 10000):
            self.assertEqual(PatternConstraint(text).value, text)
        for value in ('', None, re.compile('a'), 1):
            with self.assertRaises(FieldConstraintError) as caught:
                PatternConstraint(value)
            self.assertEqual(caught.exception.code, 'TYPE-CONSTRAINT-009')


class FieldConstraintSetTests(unittest.TestCase):
    def test_four_distinct_presence_nullability_combinations(self):
        matrix = [constraints(presence=p, nullability=n) for p in FieldPresence for n in FieldNullability]
        self.assertEqual(len(set(matrix)), 4)
        self.assertEqual({(c.presence.value, c.nullability.value) for c in matrix}, {('required', 'non-null'), ('required', 'nullable'), ('optional', 'non-null'), ('optional', 'nullable')})

    def test_explicit_states_no_constructor_defaults(self):
        with self.assertRaises(TypeError):
            FieldConstraintSet()
        with self.assertRaises(TypeError):
            FieldConstraintSet(FieldPresence.REQUIRED, FieldNullability.NON_NULL)
        for state in (None, True, 'required', FieldNullability.NON_NULL):
            with self.assertRaises(FieldConstraintError) as caught:
                FieldConstraintSet(state, FieldNullability.NON_NULL, [])
            self.assertEqual(caught.exception.code, 'TYPE-CONSTRAINT-010')
        for state in (None, True, 'non-null', FieldPresence.REQUIRED):
            with self.assertRaises(FieldConstraintError) as caught:
                FieldConstraintSet(FieldPresence.REQUIRED, state, [])
            self.assertEqual(caught.exception.code, 'TYPE-CONSTRAINT-011')

    def test_duplicate_kinds_with_same_or_different_value(self):
        for value in (100, 200):
            with self.assertRaises(FieldConstraintError) as caught:
                constraints(MaxLengthConstraint(100), MaxLengthConstraint(value))
            self.assertEqual(caught.exception.code, 'TYPE-CONSTRAINT-008')
            self.assertEqual((caught.exception.constraint_index, caught.exception.previous_index), (1, 0))

    def test_local_conflicts_and_equal_boundaries(self):
        for lower, upper, code in ((MinLengthConstraint(10), MaxLengthConstraint(5), '003'), (MinimumConstraint('101'), MaximumConstraint('100'), '004'), (ScaleConstraint(6), PrecisionConstraint(5), '007')):
            for values in ((lower, upper), (upper, lower)):
                with self.assertRaises(FieldConstraintError) as caught:
                    constraints(*values)
                self.assertEqual(caught.exception.code, 'TYPE-CONSTRAINT-' + code)
        constraints(MinLengthConstraint(0), MaxLengthConstraint(0), MinimumConstraint('1.0'), MaximumConstraint('1'), PrecisionConstraint(5), ScaleConstraint(5))

    def test_single_sided_constraints_valid(self):
        for value in (MinLengthConstraint(100), MaxLengthConstraint(0), MinimumConstraint('100'), MaximumConstraint('-100'), ScaleConstraint(10), PrecisionConstraint(1)):
            self.assertEqual(len(constraints(value).value_constraints), 1)

    def test_order_independent_equality_hash_and_enumeration(self):
        values = [MinLengthConstraint(1), MaxLengthConstraint(100), PatternConstraint('x')]
        a, b = constraints(*values), constraints(*reversed(values))
        self.assertEqual(a, b)
        self.assertEqual(hash(a), hash(b))
        self.assertEqual([str(c.kind) for c in a.value_constraints], ['max-length', 'min-length', 'pattern'])
        self.assertNotEqual(a, constraints(MaxLengthConstraint(99)))

    def test_defensive_copy_and_nested_immutability(self):
        source = [MaxLengthConstraint(100)]
        cs = FieldConstraintSet(FieldPresence.REQUIRED, FieldNullability.NON_NULL, source)
        source.clear()
        self.assertEqual(len(cs.value_constraints), 1)
        for name, value in (('presence', FieldPresence.OPTIONAL), ('nullability', FieldNullability.NULLABLE), ('value_constraints', ())):
            with self.assertRaises(FrozenInstanceError):
                setattr(cs, name, value)
        self.assertFalse(hasattr(cs, '__dict__'))

    def test_only_closed_frozen_builtin_payloads_accepted(self):
        class Custom:
            kind = ConstraintKind('acme.routing-code')
            value = {}
        class Subclass(MaxLengthConstraint):
            pass
        for values in (None, {}, set(), iter(()), [None], [Custom()], [Subclass(10)], ['max-length']):
            with self.assertRaises(FieldConstraintError) as caught:
                FieldConstraintSet(FieldPresence.REQUIRED, FieldNullability.NON_NULL, values)
            self.assertEqual(caught.exception.code, 'TYPE-CONSTRAINT-014')

    def test_typed_lookup_and_missing(self):
        cs = constraints(MaxLengthConstraint(100))
        self.assertEqual(cs.find_by_kind(ConstraintKinds.MAX_LENGTH), MaxLengthConstraint(100))
        self.assertIsNone(cs.find_by_kind(ConstraintKind('acme.routing-code')))
        with self.assertRaises(FieldConstraintError):
            cs.find_by_kind('max-length')

    def test_no_type_inference_pattern_and_precision_coexist(self):
        cs = constraints(PatternConstraint('x'), PrecisionConstraint(18))
        self.assertEqual(len(cs.value_constraints), 2)
        self.assertFalse(hasattr(cs, 'type'))


class FieldConstraintIntegrationTests(unittest.TestCase):
    def test_field_retains_explicit_constraint_object(self):
        cs = constraints(MinimumConstraint('0'), PrecisionConstraint(18), ScaleConstraint(2), presence=FieldPresence.OPTIONAL)
        f = field(cs)
        self.assertIs(f.constraints, cs)
        self.assertFalse(hasattr(f, 'type'))

    def test_field_rejects_missing_null_and_metadata_bags(self):
        for value in (None, {}, [], 'required'):
            with self.assertRaises(FieldDefinitionError) as caught:
                field(value)
            self.assertEqual(caught.exception.code, 'TYPE-FIELD-005')
        with self.assertRaises(TypeError):
            FieldDefinition(FieldId('fld_550e8400-e29b-41d4-a716-000000000000'), FieldName('name'))

    def test_constraint_change_new_snapshot_retains_identity(self):
        original = field(constraints(MaxLengthConstraint(200)))
        changed = replace(original, constraints=constraints(MaxLengthConstraint(100)))
        self.assertEqual(original.id, changed.id)
        self.assertNotEqual(original, changed)
        self.assertEqual(original.constraints.find_by_kind(ConstraintKinds.MAX_LENGTH).value, 200)

    def test_data_facet_preserves_order_and_duplicate_invariants(self):
        a, b = field(constraints(), 'name'), field(constraints(PatternConstraint('x')), 'creditLimit', 1)
        facet = DataFacet([b, a])
        self.assertEqual(facet.fields, (b, a))
        for candidate, code in ((replace(a, constraints=constraints(MaxLengthConstraint(10))), '001'), (field(constraints(), 'name', 2), '002'), (field(constraints(), 'Name', 2), '003')):
            with self.assertRaises(DataFacetError) as caught:
                DataFacet([a, candidate])
            self.assertEqual(caught.exception.code, 'TYPE-DATA-' + code)
