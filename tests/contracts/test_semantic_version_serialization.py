"""Explicit wire mapping outside Kernel; no automatic framework serializer."""
import json
import unittest
from semantic_kernel.public import SemanticVersion, SemanticVersionError, SemanticElementId, SemanticElementIdError, ElementVersionRef, ElementVersionRefError

ID = SemanticElementId('sem_550e8400-e29b-41d4-a716-446655440000')


def ref_from_wire(wire):
    # Test-only converter illustrating validation of a named-field boundary.
    if not isinstance(wire, dict):
        raise ElementVersionRefError('SEM-VREF-003', 'Expected a structured reference object.')
    if wire.get('elementId') is None:
        raise ElementVersionRefError('SEM-VREF-001', 'Element ID is required.')
    if wire.get('version') is None:
        raise ElementVersionRefError('SEM-VREF-002', 'Semantic version is required.')
    if set(wire) != {'elementId', 'version'}:
        raise ElementVersionRefError('SEM-VREF-003', 'Expected exactly elementId and version fields.')
    return ElementVersionRef(SemanticElementId.parse(wire['elementId']), SemanticVersion.parse(wire['version']))


class SemanticVersionSerializationTests(unittest.TestCase):
    def test_scalar_round_trip(self):
        version = SemanticVersion(2, 1, 0)
        encoded = json.dumps(str(version))
        self.assertEqual(encoded, '"2.1.0"')
        self.assertEqual(SemanticVersion.parse(json.loads(encoded)), version)

    def test_structured_reference_round_trip(self):
        ref = ElementVersionRef(ID, SemanticVersion(2, 1, 0))
        wire = {'elementId': str(ref.element_id), 'version': str(ref.version)}
        self.assertEqual(ref_from_wire(json.loads(json.dumps(wire))), ref)
        self.assertEqual(set(wire), {'elementId', 'version'})

    def test_invalid_json_version_scalars(self):
        for wire in ('null', 'true', '123', '[]', '{}', '"1.0"', '"latest"', '"1.0.0-alpha"'):
            with self.subTest(wire=wire), self.assertRaises(SemanticVersionError):
                SemanticVersion.parse(json.loads(wire))

    def test_missing_required_reference_fields(self):
        for wire, code in (({}, 'SEM-VREF-001'), ({'version': '2.1.0'}, 'SEM-VREF-001'), ({'elementId': str(ID)}, 'SEM-VREF-002'), ({'elementId': str(ID), 'version': None}, 'SEM-VREF-002')):
            with self.subTest(wire=wire), self.assertRaises(ElementVersionRefError) as caught:
                ref_from_wire(json.loads(json.dumps(wire)))
            self.assertEqual(caught.exception.code, code)

    def test_invalid_reference_wire_shapes_and_values(self):
        for wire in ([], str(ID) + '@2.1.0', {'elementId': str(ID), 'version': '2.1.0', 'qualifiedName': 'sales.Customer'}):
            with self.subTest(wire=wire), self.assertRaises(ElementVersionRefError):
                ref_from_wire(wire)
        with self.assertRaises(SemanticVersionError):
            ref_from_wire({'elementId': str(ID), 'version': 'latest'})
        with self.assertRaises(SemanticElementIdError):
            ref_from_wire({'elementId': 'sales.Customer', 'version': '2.1.0'})

    def test_serialization_requires_explicit_mapping(self):
        for value in (SemanticVersion(2, 1, 0), ElementVersionRef(ID, SemanticVersion(2, 1, 0))):
            with self.assertRaises(TypeError):
                json.dumps(value)
