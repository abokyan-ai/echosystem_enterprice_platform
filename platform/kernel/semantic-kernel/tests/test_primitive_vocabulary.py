from dataclasses import FrozenInstanceError
import unittest
from semantic_kernel.public import PrimitiveType, PrimitiveTypes, PrimitiveTypeError


class PrimitiveVocabularyTests(unittest.TestCase):
    def test_seven_canonical_types_parse_round_trip(self):
        self.assertEqual({str(p) for p in PrimitiveTypes.ALL}, {'string', 'boolean', 'integer', 'decimal', 'date', 'datetime', 'uuid'})
        for p in PrimitiveTypes.ALL:
            self.assertEqual(PrimitiveType.parse(str(p)), p)
            self.assertEqual(PrimitiveType.try_parse(str(p)), p)
            self.assertEqual(hash(p), hash(PrimitiveType(str(p))))

    def test_reject_aliases_unknowns_runtime_and_database_types(self):
        for value in ('String', 'bool', 'int', 'float', 'varchar', 'object', 'any', 'string[]', ' string', 'string\n', 'sales.String', int, True, {}, []):
            with self.assertRaises(PrimitiveTypeError) as caught:
                PrimitiveType(value)
            self.assertEqual(caught.exception.code, 'SEM-PRIMITIVE-002')
            self.assertIsNone(PrimitiveType.try_parse(value))

    def test_missing_type(self):
        for value in (None, ''):
            with self.assertRaises(PrimitiveTypeError) as caught:
                PrimitiveType(value)
            self.assertEqual(caught.exception.code, 'SEM-PRIMITIVE-001')

    def test_immutable_catalog_and_values(self):
        with self.assertRaises(FrozenInstanceError):
            PrimitiveTypes.STRING = PrimitiveTypes.INTEGER
        with self.assertRaises(FrozenInstanceError):
            PrimitiveTypes.STRING.value = 'integer'
        self.assertNotEqual(PrimitiveTypes.STRING, 'string')
        self.assertFalse(hasattr(PrimitiveTypes.STRING, '__dict__'))

    def test_builtin_string_canonicalization(self):
        class Tricky(str):
            def __str__(self):
                return 'other'
        value = PrimitiveType(Tricky('string'))
        self.assertIs(type(value.value), str)
        self.assertEqual(value, PrimitiveTypes.STRING)
