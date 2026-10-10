"""Reference intent, immutable snapshot evolution and explicit wire mappings."""
from dataclasses import fields, replace
import json
import unittest
from semantic_kernel.public import ElementRef, ElementRefError, ElementVersionRef, ElementVersionRefError, SemanticElementId, SemanticContextRef, SemanticContextRefError, SemanticVersion, QualifiedName, SemanticElementKinds
from test_semantic_element import TestTypeDefinition, ID, CONTEXT, OTHER_CONTEXT, VERSION
from test_semantic_version_serialization import ref_from_wire


class SemanticReferenceContractTests(unittest.TestCase):
    def test_identity_reference_has_one_field_and_exact_reference_requires_two(self):
        self.assertEqual({field.name: field.type for field in fields(ElementRef)}, {'element_id': SemanticElementId})
        self.assertEqual({field.name: field.type for field in fields(ElementVersionRef)}, {'element_id': SemanticElementId, 'version': SemanticVersion})
        with self.assertRaises(TypeError):
            ElementRef(ID, VERSION)
        with self.assertRaises(TypeError):
            ElementVersionRef(ID)
        with self.assertRaises(ElementVersionRefError):
            ElementVersionRef(ID, None)

    def test_identity_and_version_pin_have_distinct_equality_semantics(self):
        identity_ref = ElementRef(ID)
        exact_a = ElementVersionRef(ID, VERSION)
        exact_b = ElementVersionRef(ID, SemanticVersion(3, 0, 0))
        self.assertNotEqual(exact_a, exact_b)
        self.assertEqual(exact_a, ElementVersionRef(ID, SemanticVersion.parse('2.1.0')))
        # Discarding a version is an explicit caller decision using the ID field.
        self.assertEqual(ElementRef.from_id(exact_a.element_id), identity_ref)
        self.assertEqual(ElementRef.from_id(exact_b.element_id), identity_ref)
        self.assertNotEqual(identity_ref, exact_a)
        for other in (exact_a, exact_b):
            with self.assertRaises(ElementRefError):
                ElementRef.from_id(other)

    def test_identity_context_exact_name_and_raw_string_are_not_interchangeable(self):
        identity_ref = ElementRef(ID)
        context_ref = SemanticContextRef(ID)
        exact_ref = ElementVersionRef(ID, VERSION)
        for other in (ID, context_ref, exact_ref, str(ID), QualifiedName.parse('sales.Customer')):
            self.assertNotEqual(identity_ref, other)
        with self.assertRaises(SemanticContextRefError):
            SemanticContextRef.from_id(identity_ref)
        with self.assertRaises(ElementVersionRefError):
            ElementVersionRef(identity_ref, VERSION)
        self.assertIsNone(ElementRef.try_parse(identity_ref))
        self.assertIsNone(SemanticElementId.try_parse(identity_ref))
        self.assertIsNone(ElementRef.try_parse(QualifiedName.parse('sales.Customer')))

    def test_rename_context_move_and_version_evolution_preserve_identity_reference(self):
        original = TestTypeDefinition(ID, QualifiedName.parse('sales.Customer'), CONTEXT, SemanticElementKinds.TYPE_DEFINITION, VERSION)
        reference = ElementRef.from_id(original.id)
        renamed = replace(original, qualified_name=QualifiedName.parse('crm.Customer'))
        moved = replace(renamed, context=OTHER_CONTEXT)
        evolved = replace(moved, version=SemanticVersion(3, 0, 0))
        for snapshot in (renamed, moved, evolved):
            self.assertEqual(ElementRef.from_id(snapshot.id), reference)
        self.assertNotEqual(ElementVersionRef(original.id, original.version), ElementVersionRef(evolved.id, evolved.version))
        self.assertEqual(str(reference), str(ID))

    def test_identity_reference_scalar_and_target_field_json_round_trip(self):
        ref = ElementRef(ID)
        scalar = json.dumps(str(ref))
        self.assertEqual(ElementRef.parse(json.loads(scalar)), ref)
        wire = json.dumps({'target': str(ref)})
        self.assertEqual(json.loads(wire), {'target': str(ID)})
        self.assertEqual(ElementRef.parse(json.loads(wire)['target']), ref)
        with self.assertRaises(TypeError):
            json.dumps({'target': ref})

    def test_invalid_serialized_identity_is_rejected_without_guessing_reference_type(self):
        for wire, code in (('null', 'SEM-REF-001'), ('""', 'SEM-REF-001'), ('" "', 'SEM-REF-001'), ('123', 'SEM-REF-002'), ('true', 'SEM-REF-002'), ('[]', 'SEM-REF-002'), ('{}', 'SEM-REF-002'), ('"sales.Customer"', 'SEM-REF-003'), ('"' + str(ID) + '@2.1.0"', 'SEM-REF-003'), ('{"elementId":"' + str(ID) + '","version":"2.1.0"}', 'SEM-REF-002')):
            with self.subTest(wire=wire), self.assertRaises(ElementRefError) as caught:
                ElementRef.parse(json.loads(wire))
            self.assertEqual(caught.exception.code, code)

    def test_exact_target_retains_sk07_structured_wire_contract(self):
        ref = ElementVersionRef(ID, VERSION)
        encoded = json.dumps({'target': {'elementId': str(ref.element_id), 'version': str(ref.version)}})
        self.assertEqual(ref_from_wire(json.loads(encoded)['target']), ref)
        self.assertEqual(json.loads(encoded)['target']['version'], '2.1.0')
        self.assertEqual(ElementVersionRef.parse(str(ref)), ref)
        self.assertIsNone(ElementRef.try_parse(str(ref)))
        self.assertIsNone(ElementVersionRef.try_parse(str(ElementRef(ID))))

    def test_demo_identity_pinned_version_pinned_and_name_without_resolution(self):
        identity = ElementRef.from_id(ID)
        exact = ElementVersionRef(ID, SemanticVersion.parse('2.1.0'))
        name = QualifiedName.parse('sales.Customer')
        self.assertEqual(str(identity), str(ID))
        self.assertFalse(hasattr(identity, 'version'))
        self.assertEqual(str(exact.version), '2.1.0')
        self.assertEqual(str(name), 'sales.Customer')
        self.assertNotEqual(identity, exact)
        self.assertIsNone(ElementRef.try_parse(str(name)))  # No symbolic name resolution.
