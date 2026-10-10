"""Explicit scalar reference mapping outside Kernel follows SK-01 through SK-03."""
import json
import unittest
from semantic_kernel.public import SemanticContextRef, SemanticContextRefError, SemanticElementId

VALUE = 'sem_550e8400-e29b-41d4-a716-446655440000'


class SemanticContextRefSerializationTests(unittest.TestCase):
    def test_scalar_and_context_field_round_trip(self):
        ref = SemanticContextRef.from_id(SemanticElementId(VALUE))
        scalar = json.dumps(str(ref))
        self.assertIsInstance(json.loads(scalar), str)
        self.assertEqual(SemanticContextRef.parse(json.loads(scalar)), ref)
        encoded = json.dumps({'context': str(ref)})
        self.assertEqual(encoded, '{"context": "' + VALUE + '"}')
        self.assertEqual(SemanticContextRef.parse(json.loads(encoded)['context']), ref)

    def test_hex_case_normalizes_on_ingress(self):
        incoming = json.dumps({'context': 'sem_' + VALUE[4:].upper()})
        ref = SemanticContextRef.parse(json.loads(incoming)['context'])
        self.assertEqual(json.dumps({'context': str(ref)}), json.dumps({'context': VALUE}))

    def test_invalid_serialized_identity_and_shapes(self):
        for text, code in (('null', 'SEM-CTXREF-001'), ('""', 'SEM-CTXREF-001'), ('"not-a-semantic-id"', 'SEM-CTXREF-003'), ('"sales.Customer"', 'SEM-CTXREF-003'), ('123', 'SEM-CTXREF-002'), ('true', 'SEM-CTXREF-002'), ('[]', 'SEM-CTXREF-002'), ('{"contextId":"' + VALUE + '"}', 'SEM-CTXREF-002')):
            with self.subTest(text=text), self.assertRaises(SemanticContextRefError) as caught:
                SemanticContextRef.parse(json.loads(text))
            self.assertEqual(caught.exception.code, code)

    def test_serializer_requires_explicit_scalar_mapping(self):
        with self.assertRaises(TypeError):
            json.dumps({'context': SemanticContextRef.parse(VALUE)})

    def test_demo_creation_round_trip_equality_and_invalid_reference(self):
        identity = SemanticElementId(VALUE)
        ref = SemanticContextRef.from_id(identity)
        self.assertEqual(str(ref), VALUE)
        self.assertEqual(SemanticContextRef.parse(str(ref)), ref)
        self.assertEqual(SemanticContextRef.parse(json.loads(json.dumps(str(ref)))), ref)
        with self.assertRaises(SemanticContextRefError) as caught:
            SemanticContextRef.parse('not-a-semantic-id')
        self.assertEqual(caught.exception.code, 'SEM-CTXREF-003')
