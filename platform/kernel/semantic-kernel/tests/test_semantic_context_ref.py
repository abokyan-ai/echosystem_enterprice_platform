import copy
from dataclasses import FrozenInstanceError, fields, replace
import unittest
from unittest.mock import patch
from semantic_kernel.public import Namespace, QualifiedName, SemanticContextRef, SemanticContextRefError, SemanticElementId, SemanticElementIdError

VALUE = 'sem_550e8400-e29b-41d4-a716-446655440000'
OTHER = 'sem_550e8400-e29b-41d4-a716-446655440001'


class SemanticContextRefTests(unittest.TestCase):
    def test_constructor_and_factory_retain_typed_identity(self):
        identity = SemanticElementId(VALUE)
        for ref in (SemanticContextRef(identity), SemanticContextRef.from_id(identity)):
            self.assertIs(ref.context_id, identity)
            self.assertEqual(str(ref), VALUE)

    def test_structural_construction_does_not_reparse_identity(self):
        identity = SemanticElementId(VALUE)
        with patch.object(SemanticElementId, 'parse', side_effect=AssertionError('already validated')):
            self.assertIs(SemanticContextRef.from_id(identity).context_id, identity)

    def test_parse_reuses_identity_validation(self):
        with patch.object(SemanticElementId, 'parse', wraps=SemanticElementId.parse) as parse:
            ref = SemanticContextRef.parse(VALUE)
        parse.assert_called_once_with(VALUE)
        self.assertEqual(ref.context_id, SemanticElementId(VALUE))

    def test_canonical_hex_case_and_round_trip(self):
        ref = SemanticContextRef.parse('sem_' + VALUE[4:].upper())
        self.assertEqual(str(ref), VALUE)
        self.assertEqual(SemanticContextRef.parse(str(ref)), ref)
        self.assertEqual(SemanticContextRef.try_parse(VALUE), ref)

    def test_equal_references_hash_and_dictionary_keys(self):
        a = SemanticContextRef(SemanticElementId(VALUE))
        b = SemanticContextRef.parse('sem_' + VALUE[4:].upper())
        self.assertEqual(a, b)
        self.assertEqual(hash(a), hash(b))
        self.assertEqual({a: 'found'}[b], 'found')
        self.assertEqual(len({a, b}), 1)
        self.assertNotEqual(a, SemanticContextRef.parse(OTHER))

    def test_reference_is_distinct_from_identity_string_and_names(self):
        identity = SemanticElementId(VALUE)
        ref = SemanticContextRef.from_id(identity)
        for other in (identity, VALUE, Namespace('sales'), QualifiedName.parse('sales.Customer')):
            self.assertNotEqual(ref, other)
        with self.assertRaises(SemanticContextRefError):
            SemanticContextRef.from_id(ref)
        self.assertIsNone(SemanticContextRef.try_parse(identity))
        self.assertIsNone(SemanticElementId.try_parse(ref))

    def test_null_identity_is_required(self):
        for construct in (SemanticContextRef, SemanticContextRef.from_id):
            with self.assertRaises(SemanticContextRefError) as caught:
                construct(None)
            self.assertEqual(caught.exception.code, 'SEM-CTXREF-001')

    def test_structural_identity_requires_explicit_typed_construction(self):
        for value in (VALUE, '', 1, True, {}, [], Namespace('sales'), QualifiedName.parse('sales.Customer')):
            with self.subTest(value=value):
                for construct in (SemanticContextRef, SemanticContextRef.from_id):
                    with self.assertRaises(SemanticContextRefError) as caught:
                        construct(value)
                    self.assertEqual(caught.exception.code, 'SEM-CTXREF-002')

    def test_required_textual_input(self):
        for value in (None, '', ' ', '\t\n', '\u2003'):
            self.assert_rejected(value, 'SEM-CTXREF-001', 'SEM-ID-001')

    def test_textual_input_is_not_coerced(self):
        for value in (1, True, {}, [], ('id',), b'identity', SemanticContextRef.parse(VALUE)):
            self.assert_rejected(value, 'SEM-CTXREF-002', 'SEM-ID-003')

    def test_invalid_identity_has_delegated_diagnostic(self):
        for value in ('not-a-semantic-id', 'ctx_' + VALUE[4:], VALUE[4:], 'SEM_' + VALUE[4:], ' ' + VALUE, VALUE + ' ', VALUE.replace('-41d4-', '-11d4-'), VALUE.replace('-a716-', '-7716-'), VALUE + '\n', VALUE.replace('550e', '５50e')):
            self.assert_rejected(value, 'SEM-CTXREF-003', 'SEM-ID-002')

    def assert_rejected(self, value, code, identity_code):
        with self.assertRaises(SemanticElementIdError) as original:
            SemanticElementId.parse(value)
        with self.assertRaises(SemanticContextRefError) as caught:
            SemanticContextRef.parse(value)
        self.assertEqual(caught.exception.code, code)
        self.assertEqual(caught.exception.identity_code, identity_code)
        self.assertEqual(caught.exception.identity_code, original.exception.code)
        self.assertIsInstance(caught.exception.__cause__, SemanticElementIdError)
        self.assertIsNone(SemanticContextRef.try_parse(value))

    def test_frozen_reference_and_wrapped_id(self):
        ref = SemanticContextRef.parse(VALUE)
        with self.assertRaises(FrozenInstanceError):
            ref.context_id = SemanticElementId(OTHER)
        with self.assertRaises(FrozenInstanceError):
            ref.context_id.value = OTHER
        self.assertFalse(hasattr(ref, '__dict__'))

    def test_copy_and_replacement_keep_contract(self):
        ref = SemanticContextRef.parse(VALUE)
        self.assertEqual(copy.copy(ref), ref)
        self.assertEqual(copy.deepcopy(ref), ref)
        self.assertEqual(replace(ref, context_id=SemanticElementId(OTHER)), SemanticContextRef.parse(OTHER))
        with self.assertRaises(SemanticContextRefError):
            replace(ref, context_id=OTHER)

    def test_no_implicit_ordering(self):
        with self.assertRaises(TypeError):
            SemanticContextRef.parse(VALUE) < SemanticContextRef.parse(OTHER)

    def test_only_identity_state_and_no_resolution_or_naming_api(self):
        ref = SemanticContextRef.parse(VALUE)
        self.assertEqual([field.name for field in fields(ref)], ['context_id'])
        for name in ('resolve', 'load', 'fetch', 'get_definition', 'exists', 'owns', 'namespace', 'qualified_name', 'name_hint', 'definition', 'registry', 'tenant', 'package', 'parent', 'children', 'permissions'):
            self.assertFalse(hasattr(ref, name), name)

    def test_valid_unknown_identity_is_accepted_without_resolving_target_kind(self):
        # There is no loaded model. A valid identity conveys intent, not proof of a Context target.
        for value in (VALUE, OTHER):
            identity = SemanticElementId(value)
            self.assertEqual(SemanticContextRef.from_id(identity).context_id, identity)

    def test_rename_and_namespace_move_do_not_change_reference(self):
        ref = SemanticContextRef.parse(VALUE)
        illustration = {'id': ref.context_id, 'name': QualifiedName.parse('commerce.Sales')}
        illustration['name'] = QualifiedName.parse('commerce.Ordering')
        self.assertEqual(SemanticContextRef.from_id(illustration['id']), ref)
        illustration['name'] = QualifiedName.parse('operations.Ordering')
        self.assertEqual(SemanticContextRef.from_id(illustration['id']), ref)

    def test_safe_parse_propagates_unexpected_failure(self):
        with patch.object(SemanticElementId, 'parse', side_effect=RuntimeError('unexpected')):
            with self.assertRaises(RuntimeError):
                SemanticContextRef.try_parse(VALUE)

    def test_diagnostic_does_not_echo_rejected_input(self):
        with self.assertRaises(SemanticContextRefError) as caught:
            SemanticContextRef.parse('private/token')
        self.assertEqual(caught.exception.code, 'SEM-CTXREF-003')
        self.assertIn('UUIDv4', caught.exception.message)
        self.assertNotIn('private', str(caught.exception))

    def test_string_subclass_uses_existing_identity_canonicalization(self):
        class Tricky(str):
            def lower(self):
                return 'bad-id'
        ref = SemanticContextRef.parse(Tricky('sem_' + VALUE[4:].upper()))
        self.assertEqual(str(ref), VALUE)
        self.assertEqual(ref, SemanticContextRef.parse(VALUE))
