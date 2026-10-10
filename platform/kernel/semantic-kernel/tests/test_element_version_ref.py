from dataclasses import FrozenInstanceError, fields
import unittest
from unittest.mock import patch
from semantic_kernel.public import ElementVersionRef, ElementVersionRefError, SemanticElementId, SemanticVersion

ID = SemanticElementId('sem_550e8400-e29b-41d4-a716-446655440000')
VERSION = SemanticVersion(2, 1, 0)


class ElementVersionRefTests(unittest.TestCase):
    def test_typed_construction_preserves_validated_values_without_reparse(self):
        with patch.object(SemanticElementId, 'parse', side_effect=AssertionError('reparse')), patch.object(SemanticVersion, 'parse', side_effect=AssertionError('reparse')):
            ref = ElementVersionRef(ID, VERSION)
        self.assertIs(ref.element_id, ID)
        self.assertIs(ref.version, VERSION)
        self.assertEqual([(field.name, field.type) for field in fields(ref)], [('element_id', SemanticElementId), ('version', SemanticVersion)])

    def test_equality_hashing_include_identity_and_exact_version(self):
        ref = ElementVersionRef(ID, VERSION)
        equal = ElementVersionRef(SemanticElementId.parse(str(ID)), SemanticVersion.parse('2.1.0'))
        self.assertEqual(ref, equal)
        self.assertEqual(hash(ref), hash(equal))
        self.assertEqual({ref: 'definition'}[equal], 'definition')
        self.assertNotEqual(ref, ElementVersionRef(ID, SemanticVersion(2, 1, 1)))
        self.assertNotEqual(ref, ElementVersionRef(SemanticElementId('sem_550e8400-e29b-41d4-a716-446655440001'), VERSION))
        self.assertNotEqual(ref, (ID, VERSION))
        with self.assertRaises(TypeError):
            ref < equal

    def test_reference_is_immutable(self):
        ref = ElementVersionRef(ID, VERSION)
        for field, value in (('element_id', ID), ('version', SemanticVersion(3, 0, 0))):
            with self.assertRaises(FrozenInstanceError):
                setattr(ref, field, value)
        self.assertFalse(hasattr(ref, '__dict__'))

    def test_typed_construction_diagnostics(self):
        for identity, version, code in ((None, VERSION, 'SEM-VREF-001'), (ID, None, 'SEM-VREF-002'), (str(ID), VERSION, 'SEM-VREF-003'), (ID, '2.1.0', 'SEM-VREF-003'), (123, VERSION, 'SEM-VREF-003')):
            with self.subTest(code=code), self.assertRaises(ElementVersionRefError) as caught:
                ElementVersionRef(identity, version)
            self.assertEqual(caught.exception.code, code)
        with self.assertRaises(TypeError):
            ElementVersionRef(ID)

    def test_text_round_trip_and_identity_canonicalization(self):
        ref = ElementVersionRef(ID, VERSION)
        self.assertEqual(str(ref), str(ID) + '@2.1.0')
        self.assertEqual(ElementVersionRef.parse(str(ref)), ref)
        self.assertEqual(ElementVersionRef.try_parse(str(ref)), ref)
        self.assertEqual(ElementVersionRef.parse('sem_' + str(ID)[4:].upper() + '@2.1.0'), ref)

    def test_invalid_text_shapes(self):
        for value in (None, '', 1, [], str(ID), str(ID) + '@2.1.0@3.0.0', ' ' + str(ID) + '@2.1.0', str(ID) + '@2.1.0 '):
            with self.subTest(value=value), self.assertRaises(ElementVersionRefError):
                ElementVersionRef.parse(value)
            self.assertIsNone(ElementVersionRef.try_parse(value))

    def test_delegated_diagnostics_preserve_primitive_code_and_cause(self):
        for text, code, primitive in (('@2.1.0', 'SEM-VREF-001', 'SEM-ID-001'), (str(ID) + '@', 'SEM-VREF-002', 'SEM-VER-001'), ('sales.Customer@2.1.0', 'SEM-VREF-003', 'SEM-ID-002'), (str(ID) + '@latest', 'SEM-VREF-003', 'SEM-VER-002'), (str(ID) + '@9223372036854775808.0.0', 'SEM-VREF-003', 'SEM-VER-003')):
            with self.subTest(text=text), self.assertRaises(ElementVersionRefError) as caught:
                ElementVersionRef.parse(text)
            self.assertEqual(caught.exception.code, code)
            self.assertEqual(caught.exception.primitive_code, primitive)
            self.assertEqual(caught.exception.__cause__.code, primitive)

    def test_try_parse_propagates_unexpected_errors(self):
        class Broken(ElementVersionRef):
            def __post_init__(self):
                raise RuntimeError('unexpected')
        with self.assertRaises(RuntimeError):
            Broken.try_parse(str(ID) + '@2.1.0')

    def test_demo_exact_coordinate_numeric_order_and_diagnostic(self):
        self.assertEqual(ElementVersionRef.parse(str(ElementVersionRef(ID, VERSION))), ElementVersionRef(ID, VERSION))
        self.assertLess(SemanticVersion.parse('1.9.0'), SemanticVersion.parse('1.10.0'))
        with self.assertRaises(ValueError) as caught:
            SemanticVersion.parse('v1.0')
        self.assertEqual(caught.exception.code, 'SEM-VER-002')
