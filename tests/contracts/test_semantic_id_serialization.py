"""Serializer mapping is outside Kernel production code: scalar str in, parse out."""
import json
import unittest
from semantic_kernel.public import SemanticElementId, SemanticElementIdError

VALUE = "sem_550e8400-e29b-41d4-a716-446655440000"


class SemanticIdSerializationTests(unittest.TestCase):
    def test_json_scalar_and_definition_field_round_trip(self):
        identity = SemanticElementId(VALUE)
        scalar = json.dumps(str(identity))
        self.assertIsInstance(json.loads(scalar), str)
        self.assertEqual(SemanticElementId.parse(json.loads(scalar)), identity)
        encoded = json.dumps({"id": str(identity)}, sort_keys=True)
        self.assertEqual(encoded, '{"id": "' + VALUE + '"}')
        self.assertEqual(SemanticElementId.parse(json.loads(encoded)["id"]), identity)

    def test_json_mixed_case_deserializes_and_reserializes_canonically(self):
        incoming = json.dumps({"id": "sem_" + VALUE[4:].upper()})
        identity = SemanticElementId.parse(json.loads(incoming)["id"])
        self.assertEqual(json.dumps({"id": str(identity)}), json.dumps({"id": VALUE}))

    def test_invalid_serialized_shapes_are_rejected_without_coercion(self):
        for text, code in (("null", "SEM-ID-001"), ('""', "SEM-ID-001"), ('"not-an-id"', "SEM-ID-002"), ('"' + VALUE + ' "', "SEM-ID-002"), ("123", "SEM-ID-003"), ("true", "SEM-ID-003"), ('{"value":"' + VALUE + '"}', "SEM-ID-003"), ("[]", "SEM-ID-003")):
            with self.subTest(text=text):
                with self.assertRaises(SemanticElementIdError) as caught:
                    SemanticElementId.parse(json.loads(text))
                self.assertEqual(caught.exception.code, code)

    def test_default_serializer_does_not_silently_encode_value_object_as_object(self):
        with self.assertRaises(TypeError):
            json.dumps({"id": SemanticElementId(VALUE)})

    def test_demo_valid_round_trip_and_invalid_input(self):
        identity = SemanticElementId(VALUE)
        restored = SemanticElementId.parse(json.loads(json.dumps(str(identity))))
        self.assertEqual(identity, restored)
        self.assertEqual(SemanticElementId.try_parse("not-an-id"), None)
