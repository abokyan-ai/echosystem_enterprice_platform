from semantic_kernel.public import PrimitiveTypes
from model_core.public import PrimitiveTypeRef
from dataclasses import FrozenInstanceError, replace
import unittest
from unittest.mock import patch
from model_core.public import FieldConstraintSet, FieldPresence, FieldNullability, FieldId, FieldIdError, FieldName, FieldNameError, FieldDefinition, FieldDefinitionError
from semantic_kernel.public import SemanticElementId, QualifiedName

ID = 'fld_550e8400-e29b-41d4-a716-446655440000'
OTHER = 'fld_550e8400-e29b-41d4-a716-446655440001'


class FieldIdTests(unittest.TestCase):
    def test_parse_constructor_and_canonical_round_trip(self):
        identity = FieldId.parse('fld_' + ID[4:].upper())
        self.assertEqual(str(identity), ID)
        self.assertEqual(FieldId(ID), identity)
        self.assertEqual(FieldId.parse(str(identity)), identity)
        self.assertEqual(FieldId.try_parse(ID), identity)

    def test_equality_hash_and_distinct_identity_intent(self):
        a = FieldId(ID)
        b = FieldId.parse(ID)
        self.assertEqual(a, b)
        self.assertEqual(hash(a), hash(b))
        self.assertEqual({a: 'member'}[b], 'member')
        self.assertNotEqual(a, FieldId(OTHER))
        self.assertNotEqual(a, ID)
        self.assertNotEqual(a, SemanticElementId('sem_' + ID[4:]))
        with self.assertRaises(TypeError):
            a < b

    def test_required_diagnostic(self):
        for value in (None, '', ' ', '\t\n'):
            with self.subTest(value=value), self.assertRaises(FieldIdError) as caught:
                FieldId(value)
            self.assertEqual(caught.exception.code, 'TYPE-FIELD-001')

    def test_invalid_prefix_uuid_shape_version_variant_and_types(self):
        for value in ('sem_' + ID[4:], 'FLD_' + ID[4:], ID[4:], ' ' + ID, ID + '\n', ID.replace('-41d4-', '-11d4-'), ID.replace('-a716-', '-7716-'), ID.replace('-', ''), 'fld_bad', 'creditLimit', 1, True, [], {}, SemanticElementId('sem_' + ID[4:])):
            with self.subTest(value=value), self.assertRaises(FieldIdError) as caught:
                FieldId.parse(value)
            self.assertEqual(caught.exception.code, 'TYPE-FIELD-002')
            self.assertIsNone(FieldId.try_parse(value))

    def test_immutable_identity(self):
        with self.assertRaises(FrozenInstanceError):
            FieldId(ID).value = OTHER
        self.assertFalse(hasattr(FieldId(ID), '__dict__'))

    def test_string_subclass_uses_builtin_canonicalization(self):
        class Tricky(str):
            def lower(self):
                return 'bad'
        self.assertEqual(FieldId(Tricky('fld_' + ID[4:].upper())), FieldId(ID))

    def test_safe_parse_propagates_unexpected_errors(self):
        class Broken(FieldId):
            def __post_init__(self):
                raise RuntimeError('unexpected')
        with self.assertRaises(RuntimeError):
            Broken.try_parse(ID)


class FieldNameTests(unittest.TestCase):
    def test_local_names_and_round_trip(self):
        for text in ('name', 'active', 'creditLimit', 'createdAt', 'external_id', 'addressLine2'):
            value = FieldName.parse(text)
            self.assertEqual(str(value), text)
            self.assertEqual(FieldName.parse(str(value)), value)
            self.assertEqual(FieldName.try_parse(text), value)

    def test_case_sensitive_equality_hash_without_style_conversion(self):
        self.assertEqual(FieldName('creditLimit'), FieldName.parse('creditLimit'))
        self.assertEqual(hash(FieldName('creditLimit')), hash(FieldName.parse('creditLimit')))
        self.assertNotEqual(FieldName('creditLimit'), FieldName('CreditLimit'))
        self.assertNotEqual(FieldName('credit_limit'), FieldName('creditLimit'))
        self.assertNotEqual(FieldName('name'), 'name')

    def test_required_name_diagnostic(self):
        for value in (None, '', ' ', '\t\n'):
            with self.subTest(value=value), self.assertRaises(FieldNameError) as caught:
                FieldName(value)
            self.assertEqual(caught.exception.code, 'TYPE-FIELD-003')

    def test_malformed_local_names_and_types(self):
        for value in ('credit limit', 'customer.name', '.name', 'name.', 'name/value', 'name\\value', 'name#1', ' name', 'name ', 'name\n', '1name', '_name', 'credit-limit', 'náme', 1, True, [], {}, QualifiedName.parse('sales.Customer')):
            with self.subTest(value=value), self.assertRaises(FieldNameError) as caught:
                FieldName.parse(value)
            self.assertEqual(caught.exception.code, 'TYPE-FIELD-004')
            self.assertIsNone(FieldName.try_parse(value))

    def test_keywords_and_special_looking_names_have_no_magic(self):
        for value in ('class', 'namespace', 'type', 'record', 'order', 'group', 'user', 'id', 'createdAt', 'tenantId'):
            self.assertEqual(str(FieldName(value)), value)

    def test_immutable_plain_string_even_with_str_subclass(self):
        class Tricky(str):
            def __str__(self):
                return 'other'
            def __eq__(self, other):
                return False
            __hash__ = None
        name = FieldName(Tricky('creditLimit'))
        self.assertIs(type(name.value), str)
        self.assertEqual(name, FieldName('creditLimit'))
        with self.assertRaises(FrozenInstanceError):
            name.value = 'creditCeiling'

    def test_safe_parse_propagates_unexpected_errors(self):
        class Broken(FieldName):
            def __post_init__(self):
                raise RuntimeError('unexpected')
        with self.assertRaises(RuntimeError):
            Broken.try_parse('name')

    def test_diagnostics_explain_format_without_echoing_input(self):
        for constructor, value in ((FieldName, 'private/token'), (FieldId, 'fld_private-token')):
            with self.assertRaises(ValueError) as caught:
                constructor(value)
            self.assertNotIn('private', str(caught.exception))
            self.assertTrue(caught.exception.message)


class FieldDefinitionTests(unittest.TestCase):
    def test_typed_constructor_and_factory_preserve_values_without_reparse(self):
        identity = FieldId(ID)
        name = FieldName('creditLimit')
        with patch.object(FieldId, 'parse', side_effect=AssertionError('reparse')), patch.object(FieldName, 'parse', side_effect=AssertionError('reparse')):
            for field in (FieldDefinition(identity, name, PrimitiveTypeRef(PrimitiveTypes.STRING), FieldConstraintSet(FieldPresence.REQUIRED, FieldNullability.NON_NULL, ())), FieldDefinition.create(identity, name, PrimitiveTypeRef(PrimitiveTypes.STRING), FieldConstraintSet(FieldPresence.REQUIRED, FieldNullability.NON_NULL, ()))):
                self.assertIs(field.id, identity)
                self.assertIs(field.name, name)

    def test_typed_construction_diagnostics(self):
        for identity, name, code in ((None, FieldName('name'), '001'), (ID, FieldName('name'), '002'), (SemanticElementId('sem_' + ID[4:]), FieldName('name'), '002'), (FieldId(ID), None, '003'), (FieldId(ID), 'name', '004'), (FieldId(ID), QualifiedName.parse('sales.Customer'), '004')):
            with self.subTest(code=code), self.assertRaises(FieldDefinitionError) as caught:
                FieldDefinition.create(identity, name, PrimitiveTypeRef(PrimitiveTypes.STRING), FieldConstraintSet(FieldPresence.REQUIRED, FieldNullability.NON_NULL, ()))
            self.assertEqual(caught.exception.code, 'TYPE-FIELD-' + code)
        with self.assertRaises(TypeError):
            FieldDefinition(FieldId(ID))

    def test_immutable_snapshot_and_nested_values(self):
        field = FieldDefinition(FieldId(ID), FieldName('creditLimit'), PrimitiveTypeRef(PrimitiveTypes.STRING), FieldConstraintSet(FieldPresence.REQUIRED, FieldNullability.NON_NULL, ()))
        for member, value in (('id', FieldId(OTHER)), ('name', FieldName('creditCeiling'))):
            with self.assertRaises(FrozenInstanceError):
                setattr(field, member, value)
        with self.assertRaises(FrozenInstanceError):
            field.name.value = 'other'
        self.assertFalse(hasattr(field, '__dict__'))

    def test_rename_preserves_identity_but_changes_snapshot_equality(self):
        original = FieldDefinition(FieldId(ID), FieldName('creditLimit'), PrimitiveTypeRef(PrimitiveTypes.STRING), FieldConstraintSet(FieldPresence.REQUIRED, FieldNullability.NON_NULL, ()))
        renamed = replace(original, name=FieldName('creditCeiling'))
        self.assertEqual(original.id, renamed.id)
        self.assertNotEqual(original.name, renamed.name)
        self.assertNotEqual(original, renamed)
        self.assertEqual(original, FieldDefinition(FieldId.parse(ID), FieldName('creditLimit'), PrimitiveTypeRef(PrimitiveTypes.STRING), FieldConstraintSet(FieldPresence.REQUIRED, FieldNullability.NON_NULL, ())))
        self.assertEqual(hash(original), hash(FieldDefinition(FieldId(ID), FieldName('creditLimit'), PrimitiveTypeRef(PrimitiveTypes.STRING), FieldConstraintSet(FieldPresence.REQUIRED, FieldNullability.NON_NULL, ()))))

    def test_same_name_can_have_different_identity_before_collection_validation(self):
        a = FieldDefinition(FieldId(ID), FieldName('code'), PrimitiveTypeRef(PrimitiveTypes.STRING), FieldConstraintSet(FieldPresence.REQUIRED, FieldNullability.NON_NULL, ()))
        b = FieldDefinition(FieldId(OTHER), FieldName('code'), PrimitiveTypeRef(PrimitiveTypes.STRING), FieldConstraintSet(FieldPresence.REQUIRED, FieldNullability.NON_NULL, ()))
        self.assertEqual(a.name, b.name)
        self.assertNotEqual(a.id, b.id)
        self.assertNotEqual(a, b)

    def test_mini_sales_field_fixtures_without_full_types(self):
        names = {'Customer': ('name', 'active'), 'Product': ('name', 'price'), 'SalesOrder': ('orderNumber', 'orderDate')}
        fields = []
        for group in names.values():
            for name in group:
                number = len(fields)
                identity = FieldId(f'fld_550e8400-e29b-41d4-a716-{number:012d}')
                fields.append(FieldDefinition.create(identity, FieldName(name), PrimitiveTypeRef(PrimitiveTypes.STRING), FieldConstraintSet(FieldPresence.REQUIRED, FieldNullability.NON_NULL, ())))
        self.assertEqual([str(field.name) for field in fields], ['name', 'active', 'name', 'price', 'orderNumber', 'orderDate'])
        self.assertEqual(len({field.id for field in fields}), 6)
