from dataclasses import FrozenInstanceError, replace, fields
import unittest
from semantic_kernel.public import (
    PrimitiveType, PrimitiveTypes, ElementRef, SemanticElementId,
    ElementVersionRef, SemanticVersion, QualifiedName, SemanticContextRef,
)
from model_core.public import (
    TypeRef, TypeRefKind, PrimitiveTypeRef, SemanticTypeRef, TypeRefError,
    FieldDefinition, FieldId, FieldName, FieldConstraintSet, FieldPresence,
    FieldNullability, PrecisionConstraint, DataFacet,
)

ID = SemanticElementId('sem_550e8400-e29b-41d4-a716-446655440000')
OTHER = SemanticElementId('sem_550e8400-e29b-41d4-a716-446655440001')
PLAIN = FieldConstraintSet(FieldPresence.REQUIRED, FieldNullability.NON_NULL, ())
FID = FieldId('fld_550e8400-e29b-41d4-a716-446655440000')


class PrimitiveTypeRefTests(unittest.TestCase):
    def test_all_seven_typed_references(self):
        for primitive in PrimitiveTypes.ALL:
            ref = PrimitiveTypeRef(primitive)
            self.assertIs(ref.primitive, primitive)
            self.assertIs(ref.kind, TypeRefKind.PRIMITIVE)
            self.assertIsInstance(ref, TypeRef)

    def test_value_equality_and_hash(self):
        a, b = PrimitiveTypeRef(PrimitiveTypes.STRING), PrimitiveTypeRef(PrimitiveType.parse('string'))
        self.assertEqual(a, b)
        self.assertEqual(hash(a), hash(b))
        self.assertNotEqual(a, PrimitiveTypeRef(PrimitiveTypes.INTEGER))
        self.assertNotEqual(a, PrimitiveTypes.STRING)
        self.assertNotEqual(a, 'string')

    def test_reject_raw_strings_runtime_types_and_subclasses(self):
        class Subclass(PrimitiveType):
            pass
        for value in (None, 'string', str, int, 'varchar', {}, ElementRef(ID), Subclass('string')):
            with self.assertRaises(TypeRefError) as caught:
                PrimitiveTypeRef(value)
            self.assertEqual(caught.exception.code, 'TYPE-REF-002')

    def test_only_primitive_payload_and_readonly_kind(self):
        self.assertEqual({f.name: f.type for f in fields(PrimitiveTypeRef)}, {'primitive': PrimitiveType})
        self.assertIsNone(PrimitiveTypeRef.kind.fset)
        with self.assertRaises(TypeError):
            PrimitiveTypeRef(PrimitiveTypes.STRING, kind=TypeRefKind.SEMANTIC)
        with self.assertRaises(FrozenInstanceError):
            PrimitiveTypeRef(PrimitiveTypes.STRING).primitive = PrimitiveTypes.INTEGER


class SemanticTypeRefTests(unittest.TestCase):
    def test_identity_target_retained_without_lookup(self):
        target = ElementRef(ID)
        ref = SemanticTypeRef(target)
        self.assertIs(ref.target, target)
        self.assertIs(ref.kind, TypeRefKind.SEMANTIC)
        self.assertIsInstance(ref, TypeRef)
        self.assertEqual({f.name: f.type for f in fields(SemanticTypeRef)}, {'target': ElementRef})

    def test_identity_equality_hash_and_distinct_variants(self):
        ref = SemanticTypeRef(ElementRef(ID))
        same = SemanticTypeRef(ElementRef.parse(str(ID)))
        self.assertEqual(ref, same)
        self.assertEqual(hash(ref), hash(same))
        self.assertNotEqual(ref, SemanticTypeRef(ElementRef(OTHER)))
        self.assertNotEqual(ref, PrimitiveTypeRef(PrimitiveTypes.STRING))
        self.assertNotEqual(ref, ElementRef(ID))

    def test_missing_target_diagnostic(self):
        with self.assertRaises(TypeRefError) as caught:
            SemanticTypeRef(None)
        self.assertEqual(caught.exception.code, 'TYPE-REF-005')

    def test_reject_names_loaded_objects_exact_refs_and_raw_ids(self):
        class Subclass(ElementRef):
            pass
        exact = ElementVersionRef(ID, SemanticVersion(1, 0, 0))
        for value in (str(ID), ID, QualifiedName.parse('sales.Customer'), SemanticContextRef(ID), exact, object(), {}, Subclass(ID)):
            with self.assertRaises(TypeRefError) as caught:
                SemanticTypeRef(value)
            self.assertEqual(caught.exception.code, 'TYPE-REF-003')

    def test_identity_only_no_optional_version_or_names(self):
        ref = SemanticTypeRef(ElementRef(ID))
        for member in ('qualified_name', 'version', 'registry', 'resolver', 'definition', 'relationship', 'nullable', 'presence', 'cardinality', 'resolve', 'compile', 'runtime_type', 'sql_type'):
            self.assertFalse(hasattr(ref, member))
        with self.assertRaises(TypeError):
            SemanticTypeRef(ElementRef(ID), version=SemanticVersion(1, 0, 0))

    def test_frozen_nested_target(self):
        ref = SemanticTypeRef(ElementRef(ID))
        with self.assertRaises(FrozenInstanceError):
            ref.target = ElementRef(OTHER)
        with self.assertRaises(FrozenInstanceError):
            ref.target.element_id = OTHER
        self.assertFalse(hasattr(ref, '__dict__'))


class TypedFieldTests(unittest.TestCase):
    def test_required_type_constructor_and_factory(self):
        ref = PrimitiveTypeRef(PrimitiveTypes.DECIMAL)
        for field in (FieldDefinition(FID, FieldName('creditLimit'), ref, PLAIN), FieldDefinition.create(FID, FieldName('creditLimit'), ref, PLAIN)):
            self.assertIs(field.type, ref)
            self.assertIs(field.constraints, PLAIN)
        with self.assertRaises(TypeError):
            FieldDefinition(FID, FieldName('name'), constraints=PLAIN)
        with self.assertRaises(TypeRefError) as caught:
            FieldDefinition(FID, FieldName('name'), None, PLAIN)
        self.assertEqual(caught.exception.code, 'TYPE-REF-001')

    def test_no_unknown_raw_or_custom_variant_escape_hatches(self):
        class Custom:
            kind = TypeRefKind.PRIMITIVE
            primitive = PrimitiveTypes.STRING
        class Subclass(PrimitiveTypeRef):
            pass
        for ref in ('string', 'any', 'object', 'unknown', str, ElementRef(ID), {}, Custom(), Subclass(PrimitiveTypes.STRING)):
            with self.assertRaises(TypeRefError) as caught:
                FieldDefinition(FID, FieldName('name'), ref, PLAIN)
            self.assertEqual(caught.exception.code, 'TYPE-REF-004')

    def test_type_change_retains_identity_and_constraints(self):
        old = FieldDefinition(FID, FieldName('amount'), PrimitiveTypeRef(PrimitiveTypes.INTEGER), PLAIN)
        new = replace(old, type=PrimitiveTypeRef(PrimitiveTypes.DECIMAL))
        self.assertEqual(old.id, new.id)
        self.assertIs(old.constraints, new.constraints)
        self.assertNotEqual(old, new)
        self.assertEqual(old.type.primitive, PrimitiveTypes.INTEGER)

    def test_presence_and_nullability_stay_in_constraint_set(self):
        for presence in FieldPresence:
            for nullability in FieldNullability:
                cs = FieldConstraintSet(presence, nullability, ())
                field = FieldDefinition(FID, FieldName('name'), PrimitiveTypeRef(PrimitiveTypes.STRING), cs)
                self.assertIs(field.constraints, cs)
                self.assertFalse(hasattr(field.type, 'nullability'))
                self.assertFalse(hasattr(field.type, 'presence'))

    def test_no_constraint_applicability_yet(self):
        cs = FieldConstraintSet(FieldPresence.REQUIRED, FieldNullability.NON_NULL, [PrecisionConstraint(18)])
        field = FieldDefinition(FID, FieldName('name'), PrimitiveTypeRef(PrimitiveTypes.STRING), cs)
        self.assertEqual(field.constraints.value_constraints, (PrecisionConstraint(18),))

    def test_self_reference_is_finite_and_needs_no_host(self):
        field = FieldDefinition(FID, FieldName('parent'), SemanticTypeRef(ElementRef(ID)), PLAIN)
        self.assertEqual(DataFacet((field,)).fields[0].type.target.element_id, ID)

    def test_mutual_references_need_no_loaded_object_graph(self):
        a = DataFacet((FieldDefinition(FID, FieldName('peerB'), SemanticTypeRef(ElementRef(OTHER)), PLAIN),))
        b = DataFacet((FieldDefinition(FID, FieldName('peerA'), SemanticTypeRef(ElementRef(ID)), PLAIN),))
        self.assertEqual(a.fields[0].type.target.element_id, OTHER)
        self.assertEqual(b.fields[0].type.target.element_id, ID)
