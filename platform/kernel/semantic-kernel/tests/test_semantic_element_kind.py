import copy
from dataclasses import FrozenInstanceError
from enum import Enum
import unittest
from semantic_kernel.public import SemanticElementKind, SemanticElementKindError, SemanticElementKinds

CORE = ('type', 'relationship', 'behavior', 'capability', 'action', 'event', 'process', 'rule', 'policy', 'contract', 'composition', 'extension')


class SemanticElementKindTests(unittest.TestCase):
    def test_core_constants_are_typed_and_canonical(self):
        for category in CORE:
            constant = getattr(SemanticElementKinds, category.upper() + '_DEFINITION')
            self.assertIsInstance(constant, SemanticElementKind)
            self.assertEqual(str(constant), category + '-definition')
            self.assertEqual(SemanticElementKind.parse(str(constant)), constant)
            self.assertTrue(SemanticElementKinds.is_core(constant))
        self.assertEqual(len(SemanticElementKinds.ALL), 12)
        self.assertEqual(len(set(SemanticElementKinds.ALL)), 12)

    def test_public_value_is_not_a_closed_enum(self):
        self.assertFalse(issubclass(SemanticElementKind, Enum))
        self.assertEqual(SemanticElementKind.parse('acme.route-definition').value, 'acme.route-definition')

    def test_should_preserve_valid_unknown_semantic_element_kind(self):
        for value in ('acme.route-definition', 'industry.healthcare.protocol-definition', 'partner.workflow-template', 'platform.agent-definition', 'partner.acme.route-definition', 'future-definition'):
            kind = SemanticElementKind.parse(value)
            self.assertEqual(kind.value, value)
            self.assertEqual(str(kind), value)
            self.assertEqual(SemanticElementKind.parse(str(kind)), kind)
            self.assertFalse(SemanticElementKinds.is_core(kind))

    def test_unqualified_future_vocabulary_is_lexically_valid(self):
        # Known Core membership is not a parser allowlist; publisher registration rules come later.
        self.assertEqual(str(SemanticElementKind('new-platform-definition')), 'new-platform-definition')
        self.assertFalse(SemanticElementKinds.is_core(SemanticElementKind('new-platform-definition')))

    def test_lowercase_kebab_segments(self):
        for value in ('a', 'a1', 'a-2', 'acme2.route-definition', 'partner-a.route2-definition', 'a.b.c-d'):
            self.assertEqual(SemanticElementKind(value).value, value)

    def test_required_values(self):
        for value in (None, '', ' ', '\t\n', '\u2003'):
            self.assert_rejected(value, 'SEM-KIND-001', None)

    def test_non_string_values_are_not_coerced(self):
        for value in (1, True, {}, [], b'action-definition', SemanticElementKinds.ACTION_DEFINITION):
            self.assert_rejected(value, 'SEM-KIND-002', None)

    def test_noncanonical_case_and_style_are_rejected(self):
        for value in ('ActionDefinition', 'Action-Definition', 'ACTION-DEFINITION', 'action_definition', 'acme.route_definition', 'Acme.route-definition'):
            self.assert_rejected(value, 'SEM-KIND-002', 0 if '.' not in value or value.startswith('Acme') else 1)

    def test_invalid_segments_and_separators(self):
        for value, index in (('.action-definition', 0), ('action-definition.', 1), ('acme..route-definition', 1), ('-action', 0), ('action-', 0), ('acme.route--definition', 1), ('9acme.route-definition', 0), ('acme/route-definition', 0), ('acme\\route-definition', 0), ('acme:route-definition', 0), ('acme.*', 1), ('action definition', 0), ('acme. route-definition', 1), ('action-definition ', 0), ('action-definition\n', 0), ('acme.équipe', 1), ('acme.route\x00definition', 1), ('acme."route"', 1), ('acme.route@v1', 1)):
            self.assert_rejected(value, 'SEM-KIND-002', index)

    def assert_rejected(self, value, code, index):
        for parse in (SemanticElementKind, SemanticElementKind.parse):
            with self.assertRaises(SemanticElementKindError) as caught:
                parse(value)
            self.assertEqual(caught.exception.code, code)
            self.assertEqual(caught.exception.segment_index, index)
        self.assertIsNone(SemanticElementKind.try_parse(value))

    def test_equal_values_hash_and_dictionary_keys(self):
        a = SemanticElementKind('acme.route-definition')
        b = SemanticElementKind.parse('acme.route-definition')
        self.assertEqual(a, b)
        self.assertEqual(hash(a), hash(b))
        self.assertEqual({a: 'found'}[b], 'found')
        self.assertNotEqual(a, SemanticElementKinds.ACTION_DEFINITION)
        self.assertNotEqual(a, 'acme.route-definition')

    def test_kind_and_catalog_are_frozen(self):
        with self.assertRaises(FrozenInstanceError):
            SemanticElementKinds.ACTION_DEFINITION.value = 'other'
        with self.assertRaises(FrozenInstanceError):
            SemanticElementKinds.ACTION_DEFINITION = SemanticElementKind('other')
        self.assertIsInstance(SemanticElementKinds.ALL, tuple)

    def test_copies_preserve_values(self):
        kind = SemanticElementKind('acme.route-definition')
        self.assertEqual(copy.copy(kind), kind)
        self.assertEqual(copy.deepcopy(kind), kind)

    def test_no_implicit_ordering(self):
        with self.assertRaises(TypeError):
            SemanticElementKinds.TYPE_DEFINITION < SemanticElementKinds.ACTION_DEFINITION

    def test_core_membership_is_not_support_or_ownership_check(self):
        self.assertTrue(SemanticElementKinds.is_core(SemanticElementKind('action-definition')))
        self.assertFalse(SemanticElementKinds.is_core('action-definition'))
        self.assertFalse(SemanticElementKinds.is_core(SemanticElementKind('acme.action-definition')))
        self.assertEqual(str(SemanticElementKind('acme.action-definition')), 'acme.action-definition')

    def test_safe_parse_does_not_hide_unexpected_failure(self):
        class BrokenKind(SemanticElementKind):
            def __post_init__(self):
                raise RuntimeError('unexpected')
        with self.assertRaises(RuntimeError):
            BrokenKind.try_parse('action-definition')
        self.assertEqual(SemanticElementKind.try_parse('action-definition'), SemanticElementKinds.ACTION_DEFINITION)

    def test_string_subclass_cannot_change_stored_value_or_equality(self):
        class Tricky(str):
            def split(self, *args):
                return ['type-definition']
            def __str__(self):
                return 'other'
            def __eq__(self, other):
                return False
            __hash__ = None
        kind = SemanticElementKind(Tricky('acme.route-definition'))
        self.assertIs(type(kind.value), str)
        self.assertEqual(kind, SemanticElementKind('acme.route-definition'))
        self.assertIsNone(SemanticElementKind.try_parse(Tricky('Action Definition')))

    def test_diagnostic_explains_grammar_without_echoing_input(self):
        with self.assertRaises(SemanticElementKindError) as caught:
            SemanticElementKind('acme.private/token')
        self.assertIn('kebab-case', caught.exception.message)
        self.assertNotIn('private', str(caught.exception))
        self.assertEqual(caught.exception.segment_index, 1)
