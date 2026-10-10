from dataclasses import replace
import json
import unittest
from semantic_kernel.public import PrimitiveTypes, PrimitiveTypeError, SemanticContextRef, ElementRef, ElementRefError, SemanticElementId, QualifiedName, SemanticVersion
from model_core.public import (
    PrimitiveTypeRef, SemanticTypeRef, TypeRefKind, TypeRefError,
    FieldDefinition, FieldId, FieldName, FieldConstraintSet, FieldPresence,
    FieldNullability, MaxLengthConstraint, MinimumConstraint, PrecisionConstraint,
    ScaleConstraint, DataFacet, TypeDataComposition,
)
from model_core.constraint_wire import type_ref_to_wire, type_ref_from_wire, field_to_wire, field_from_wire
from test_data_facet import customer


PLAIN = FieldConstraintSet(FieldPresence.REQUIRED, FieldNullability.NON_NULL, ())


def field(name, type, constraints=PLAIN, number=0):
    # Fixture-only explicit convenience, not a canonical constructor default.
    return FieldDefinition(FieldId(f'fld_550e8400-e29b-41d4-a716-{number:012d}'), FieldName(name), type, constraints)


def typed_customer():
    return TypeDataComposition(customer(), DataFacet([
        field('name', PrimitiveTypeRef(PrimitiveTypes.STRING), FieldConstraintSet(FieldPresence.REQUIRED, FieldNullability.NON_NULL, [MaxLengthConstraint(200)])),
        field('active', PrimitiveTypeRef(PrimitiveTypes.BOOLEAN), number=1),
        field('creditLimit', PrimitiveTypeRef(PrimitiveTypes.DECIMAL), FieldConstraintSet(FieldPresence.OPTIONAL, FieldNullability.NON_NULL, [MinimumConstraint('0'), PrecisionConstraint(18), ScaleConstraint(2)]), number=2),
    ]))


class TypeReferenceContractTests(unittest.TestCase):
    def test_all_primitive_wire_round_trips(self):
        for primitive in PrimitiveTypes.ALL:
            ref = PrimitiveTypeRef(primitive)
            wire = type_ref_to_wire(ref)
            self.assertEqual(wire, {'kind': 'primitive', 'primitive': str(primitive)})
            self.assertEqual(type_ref_from_wire(json.loads(json.dumps(wire))), ref)

    def test_semantic_wire_uses_existing_element_ref_canonical_text(self):
        ref = SemanticTypeRef(ElementRef(customer().id))
        wire = type_ref_to_wire(ref)
        self.assertEqual(wire, {'kind': 'semantic', 'elementRef': str(customer().id)})
        self.assertEqual(type_ref_from_wire(json.loads(json.dumps(wire))), ref)
        self.assertEqual(set(wire), {'kind', 'elementRef'})

    def test_required_explicit_discriminator_no_compact_or_class_names(self):
        for wire in ('string', str(customer().id), [], {}, {'kind': 'PrimitiveTypeRef', 'primitive': 'string'}, {'$type': 'PrimitiveTypeRef', 'primitive': 'string'}, {'kind': 0, 'primitive': 'string'}, {'kind': TypeRefKind.PRIMITIVE, 'primitive': 'string'}, {'kind': 'array', 'primitive': 'string'}):
            with self.assertRaises(TypeRefError) as caught:
                type_ref_from_wire(wire)
            self.assertEqual(caught.exception.code, 'TYPE-REF-004')
        with self.assertRaises(TypeRefError) as caught:
            type_ref_from_wire(None)
        self.assertEqual(caught.exception.code, 'TYPE-REF-001')

    def test_reject_ambiguous_optional_version_and_named_wire_variants(self):
        for wire in ({'kind': 'semantic'}, {'kind': 'primitive'}, {'kind': 'semantic', 'elementRef': str(customer().id), 'version': '1.0.0'}, {'kind': 'semantic', 'elementRef': str(customer().id), 'qualifiedName': 'sales.Customer'}, {'kind': 'primitive', 'primitive': 'string', 'elementRef': str(customer().id)}, {'kind': 'primitive', 'primitive': 'string', 'nullable': True}):
            with self.assertRaises(TypeRefError):
                type_ref_from_wire(wire)

    def test_invalid_payloads_delegate_foundational_validation(self):
        for value in ('String', 'any', 'varchar', 'string[]', int, None, 0, True):
            with self.assertRaises(PrimitiveTypeError):
                type_ref_from_wire({'kind': 'primitive', 'primitive': value})
        for value in ('sales.Customer', 'bad', str(customer().id) + '@1.0.0', None, 0, {}):
            with self.assertRaises(ElementRefError):
                type_ref_from_wire({'kind': 'semantic', 'elementRef': value})
        with self.assertRaises(TypeRefError):
            type_ref_to_wire(ElementRef(customer().id))

    def test_both_field_variants_round_trip(self):
        for ref in (PrimitiveTypeRef(PrimitiveTypes.DECIMAL), SemanticTypeRef(ElementRef(customer().id))):
            original = field('value', ref)
            wire = field_to_wire(original)
            self.assertEqual(set(wire), {'id', 'name', 'type', 'constraints'})
            self.assertEqual(field_from_wire(json.loads(json.dumps(wire))), original)
            self.assertEqual(wire['type']['kind'], ref.kind.value)
            with self.assertRaises(TypeError):
                json.dumps(original)

    def test_missing_field_type_wire_has_no_legacy_default(self):
        wire = field_to_wire(field('name', PrimitiveTypeRef(PrimitiveTypes.STRING)))
        wire.pop('type')
        with self.assertRaises(ValueError):
            field_from_wire(wire)
        wire['type'] = None
        with self.assertRaises(TypeRefError):
            field_from_wire(wire)

    def test_target_rename_context_or_version_change_preserves_ref(self):
        old = customer()
        ref = SemanticTypeRef(ElementRef(old.id))
        new = replace(old, qualified_name=QualifiedName.parse('crm.Client'), context=SemanticContextRef(SemanticElementId('sem_550e8400-e29b-41d4-a716-446655440004')), version=SemanticVersion(2, 0, 0))
        self.assertEqual(ref, SemanticTypeRef(ElementRef(new.id)))
        wire = type_ref_to_wire(ref)
        self.assertNotIn('sales.Customer', json.dumps(wire))
        self.assertNotIn('crm.Client', json.dumps(wire))
        self.assertNotIn('version', wire)

    def test_primitive_string_and_sales_string_are_distinct(self):
        host = replace(customer(), qualified_name=QualifiedName.parse('sales.String'))
        semantic = SemanticTypeRef(ElementRef(host.id))
        primitive = PrimitiveTypeRef(PrimitiveTypes.STRING)
        self.assertNotEqual(semantic, primitive)
        self.assertNotEqual(type_ref_to_wire(semantic), type_ref_to_wire(primitive))

    def test_sales_customer_and_order_demo(self):
        composition = typed_customer()
        self.assertEqual([str(f.type.primitive) for f in composition.data.fields], ['string', 'boolean', 'decimal'])
        self.assertEqual([str(f.name) for f in composition.data.fields], ['name', 'active', 'creditLimit'])
        self.assertEqual(str(composition.type_definition.qualified_name), 'sales.Customer')
        self.assertEqual(str(composition.type_definition.version), '1.0.0')
        order_host = replace(customer(), id=SemanticElementId('sem_550e8400-e29b-41d4-a716-446655440002'), qualified_name=QualifiedName.parse('sales.SalesOrder'))
        order = TypeDataComposition(order_host, DataFacet([field('customer', SemanticTypeRef(ElementRef(composition.type_definition.id)))]))
        self.assertEqual(order.data.fields[0].type.target.element_id, composition.type_definition.id)
        for member in ('relationship', 'foreign_key', 'version', 'qualified_name'):
            self.assertFalse(hasattr(order.data.fields[0].type, member))
        self.assertEqual(field_from_wire(json.loads(json.dumps(field_to_wire(order.data.fields[0])))), order.data.fields[0])

    def test_self_and_mutual_refs_serialize_without_nested_host_graph(self):
        a, b = customer().id, SemanticElementId('sem_550e8400-e29b-41d4-a716-446655440003')
        cases = (field('self', SemanticTypeRef(ElementRef(a))), field('peerB', SemanticTypeRef(ElementRef(b))), field('peerA', SemanticTypeRef(ElementRef(a))))
        for original in cases:
            wire = field_to_wire(original)
            self.assertIs(type(wire['type']['elementRef']), str)
            self.assertEqual(field_from_wire(json.loads(json.dumps(wire))), original)

    def test_mutable_wire_cannot_change_reference(self):
        original = SemanticTypeRef(ElementRef(customer().id))
        wire = type_ref_to_wire(original)
        restored = type_ref_from_wire(wire)
        wire['elementRef'] = 'bad'
        self.assertEqual(restored, original)
        self.assertEqual(type_ref_to_wire(restored)['elementRef'], str(customer().id))
