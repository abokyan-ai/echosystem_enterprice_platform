from semantic_kernel.public import PrimitiveTypes
from model_core.public import PrimitiveTypeRef
from dataclasses import FrozenInstanceError, replace
import unittest
from model_core.public import FieldConstraintSet, FieldPresence, FieldNullability, DataFacet, DataFacetError, FieldDefinition, FieldId, FieldName
from semantic_kernel.public import FacetKinds


def field(number, name):
    return FieldDefinition(FieldId(f'fld_550e8400-e29b-41d4-a716-{number:012d}'), FieldName(name), PrimitiveTypeRef(PrimitiveTypes.STRING), FieldConstraintSet(FieldPresence.REQUIRED, FieldNullability.NON_NULL, ()))


class DataFacetTests(unittest.TestCase):
    def test_empty_and_single_field(self):
        self.assertEqual(DataFacet.create([]).fields, ())
        a = field(0, 'name')
        self.assertEqual(DataFacet.create([a]).fields, (a,))

    def test_fixed_kind_cannot_be_supplied_or_mutated(self):
        facet = DataFacet(())
        self.assertIs(facet.kind, FacetKinds.DATA)
        with self.assertRaises(TypeError):
            DataFacet((), kind=FacetKinds.POLICY)
        with self.assertRaises((FrozenInstanceError, TypeError, AttributeError)):
            facet.kind = FacetKinds.POLICY

    def test_order_is_preserved_without_sorting(self):
        fields = [field(2, 'creditLimit'), field(0, 'name'), field(1, 'active')]
        facet = DataFacet(fields)
        self.assertEqual(facet.fields, tuple(fields))
        self.assertEqual(tuple(map(lambda f: str(f.name), facet.fields)), ('creditLimit', 'name', 'active'))

    def test_defensive_copy_and_frozen_snapshot(self):
        source = [field(0, 'name')]
        facet = DataFacet(source)
        source.append(field(1, 'active'))
        source[0] = field(2, 'other')
        self.assertEqual(len(facet.fields), 1)
        self.assertEqual(str(facet.fields[0].name), 'name')
        with self.assertRaises(FrozenInstanceError):
            facet.fields = ()
        self.assertFalse(hasattr(facet.fields, 'append'))

    def test_invalid_null_members_and_unordered_inputs(self):
        for source in (None, {}, set(), frozenset(), iter([]), 'fields', [None], [object()]):
            with self.subTest(source=source), self.assertRaises(DataFacetError) as caught:
                DataFacet(source)
            self.assertEqual(caught.exception.code, 'TYPE-DATA-004')

    def test_duplicate_ids(self):
        a = field(0, 'name')
        with self.assertRaises(DataFacetError) as caught:
            DataFacet([a, replace(a, name=FieldName('email'))])
        self.assertEqual(caught.exception.code, 'TYPE-DATA-001')
        self.assertEqual((caught.exception.field_index, caught.exception.previous_index), (1, 0))

    def test_duplicate_names(self):
        with self.assertRaises(DataFacetError) as caught:
            DataFacet([field(0, 'name'), field(1, 'name')])
        self.assertEqual(caught.exception.code, 'TYPE-DATA-002')
        self.assertEqual((caught.exception.field_index, caught.exception.previous_index), (1, 0))

    def test_case_only_collisions_rejected_without_changing_fieldname(self):
        for a, b in (('creditLimit', 'CreditLimit'), ('creditLimit', 'Creditlimit'), ('NAME', 'name')):
            self.assertNotEqual(FieldName(a), FieldName(b))
            with self.assertRaises(DataFacetError) as caught:
                DataFacet([field(0, a), field(1, b)])
            self.assertEqual(caught.exception.code, 'TYPE-DATA-003')

    def test_first_error_and_id_before_name_are_deterministic(self):
        a = field(0, 'name')
        with self.assertRaises(DataFacetError) as caught:
            DataFacet([a, a, None])
        self.assertEqual(caught.exception.code, 'TYPE-DATA-001')
        self.assertEqual(caught.exception.field_index, 1)

    def test_uniqueness_is_local_not_global(self):
        a = field(0, 'name')
        self.assertEqual(DataFacet([a]), DataFacet([a]))
        self.assertEqual(DataFacet([field(1, 'name')]).fields[0].name, a.name)

    def test_exact_typed_lookup_and_missing(self):
        a, b = field(0, 'name'), field(1, 'active')
        facet = DataFacet([a, b])
        self.assertIs(facet.find_by_id(a.id), a)
        self.assertIs(facet.find_by_name(b.name), b)
        self.assertIsNone(facet.find_by_id(field(2, 'missing').id))
        self.assertIsNone(facet.find_by_name(FieldName('Active')))
        for lookup, value in ((facet.find_by_id, str(a.id)), (facet.find_by_name, 'name')):
            with self.assertRaises(DataFacetError):
                lookup(value)

    def test_order_sensitive_equality_hash_and_reorder_identity(self):
        a, b = field(0, 'name'), field(1, 'active')
        facet = DataFacet([a, b])
        self.assertEqual(facet, DataFacet((a, b)))
        self.assertEqual(hash(facet), hash(DataFacet((a, b))))
        reordered = DataFacet([b, a])
        self.assertNotEqual(facet, reordered)
        self.assertEqual({f.id for f in facet.fields}, {f.id for f in reordered.fields})

    def test_rename_as_new_facet_preserves_field_identity(self):
        a = field(0, 'creditLimit')
        old = DataFacet([a])
        new = DataFacet([replace(a, name=FieldName('creditCeiling'))])
        self.assertEqual(old.fields[0].id, new.fields[0].id)
        self.assertNotEqual(old, new)
