from dataclasses import FrozenInstanceError, replace
import unittest
from unittest.mock import patch
from semantic_kernel.public import ElementRef, ElementRefError, SemanticElementId, SemanticElementIdError, SemanticContextRef, ElementVersionRef, SemanticVersion, QualifiedName

VALUE = 'sem_550e8400-e29b-41d4-a716-446655440000'
OTHER = 'sem_550e8400-e29b-41d4-a716-446655440001'


class ElementRefTests(unittest.TestCase):
    def test_constructor_and_factory_preserve_validated_identity_without_reparse(self):
        identity = SemanticElementId(VALUE)
        with patch.object(SemanticElementId, 'parse', side_effect=AssertionError('reparse')):
            for ref in (ElementRef(identity), ElementRef.from_id(identity)):
                self.assertIs(ref.element_id, identity)
                self.assertEqual(str(ref), VALUE)

    def test_parse_delegates_identity_validation(self):
        with patch.object(SemanticElementId, 'parse', wraps=SemanticElementId.parse) as parse:
            ref = ElementRef.parse(VALUE)
        parse.assert_called_once_with(VALUE)
        self.assertEqual(ref.element_id, SemanticElementId(VALUE))

    def test_canonical_hex_case_and_round_trip(self):
        ref = ElementRef.parse('sem_' + VALUE[4:].upper())
        self.assertEqual(str(ref), VALUE)
        self.assertEqual(ElementRef.parse(str(ref)), ref)
        self.assertEqual(ElementRef.try_parse(VALUE), ref)

    def test_equality_hashing_and_dictionary_keys(self):
        a = ElementRef.from_id(SemanticElementId(VALUE))
        b = ElementRef.parse(VALUE)
        self.assertEqual(a, b)
        self.assertEqual(hash(a), hash(b))
        self.assertEqual({a: 'target'}[b], 'target')
        self.assertEqual(len({a, b}), 1)
        self.assertNotEqual(a, ElementRef.parse(OTHER))
        with self.assertRaises(TypeError):
            a < b

    def test_typed_construction_rejects_other_reference_intents_and_raw_values(self):
        identity = SemanticElementId(VALUE)
        for value in (VALUE, 1, True, [], {}, QualifiedName.parse('sales.Customer'), SemanticContextRef(identity), ElementVersionRef(identity, SemanticVersion(2, 1, 0)), ElementRef(identity)):
            for constructor in (ElementRef, ElementRef.from_id):
                with self.subTest(value=value, constructor=constructor), self.assertRaises(ElementRefError) as caught:
                    constructor(value)
                self.assertEqual(caught.exception.code, 'SEM-REF-002')
        for constructor in (ElementRef, ElementRef.from_id):
            with self.assertRaises(ElementRefError) as caught:
                constructor(None)
            self.assertEqual(caught.exception.code, 'SEM-REF-001')
        with self.assertRaises(TypeError):
            ElementRef()

    def test_parse_diagnostics_match_delegated_identity_failures(self):
        cases = [(value, 'SEM-REF-001', 'SEM-ID-001') for value in (None, '', ' ', '\t\n')]
        cases += [(value, 'SEM-REF-002', 'SEM-ID-003') for value in (1, True, [], {}, b'identity', SemanticElementId(VALUE))]
        cases += [(value, 'SEM-REF-003', 'SEM-ID-002') for value in ('bad-id', 'sales.Customer', 'Customer', '../Customer', 'https://platform/elements/' + VALUE, 'latest:' + VALUE, VALUE + '@2.1.0', ' ' + VALUE, VALUE + '\n', 'SEM_' + VALUE[4:], VALUE.replace('-41d4-', '-11d4-'), VALUE.replace('-a716-', '-7716-'))]
        for value, code, identity_code in cases:
            with self.subTest(value=value), self.assertRaises(ElementRefError) as caught:
                ElementRef.parse(value)
            error = caught.exception
            self.assertEqual(error.code, code)
            self.assertEqual(error.identity_code, identity_code)
            self.assertIsInstance(error.__cause__, SemanticElementIdError)
            self.assertEqual(error.__cause__.code, identity_code)
            self.assertIsNone(ElementRef.try_parse(value))

    def test_immutable_reference_and_nested_identity(self):
        ref = ElementRef.parse(VALUE)
        with self.assertRaises(FrozenInstanceError):
            ref.element_id = SemanticElementId(OTHER)
        with self.assertRaises(FrozenInstanceError):
            ref.element_id.value = OTHER
        self.assertFalse(hasattr(ref, '__dict__'))
        self.assertEqual(replace(ref, element_id=SemanticElementId(OTHER)), ElementRef.parse(OTHER))
        with self.assertRaises(ElementRefError):
            replace(ref, element_id=OTHER)

    def test_unknown_identity_requires_no_loaded_model(self):
        # Syntax alone is sufficient; neither valid value claims existence or access.
        for value in (VALUE, OTHER):
            self.assertEqual(ElementRef.parse(value).element_id, SemanticElementId(value))

    def test_safe_parse_propagates_unexpected_failures(self):
        with patch.object(SemanticElementId, 'parse', side_effect=RuntimeError('unexpected')):
            with self.assertRaises(RuntimeError):
                ElementRef.try_parse(VALUE)
        class Broken(ElementRef):
            def __post_init__(self):
                raise RuntimeError('unexpected construction')
        with self.assertRaises(RuntimeError):
            Broken.try_parse(VALUE)

    def test_diagnostic_explains_identity_format_without_echoing_input(self):
        with self.assertRaises(ElementRefError) as caught:
            ElementRef.parse('private/token')
        self.assertIn('UUIDv4', caught.exception.message)
        self.assertNotIn('private', str(caught.exception))

    def test_string_subclass_uses_existing_canonicalization(self):
        class Tricky(str):
            def lower(self):
                return 'bad-id'
        self.assertEqual(ElementRef.parse(Tricky('sem_' + VALUE[4:].upper())), ElementRef.parse(VALUE))
