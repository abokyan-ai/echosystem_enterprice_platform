import json
import unittest
from semantic_kernel.public import SemanticElementKind, SemanticElementKindError, SemanticElementKinds


class SemanticElementKindSerializationTests(unittest.TestCase):
    def test_all_core_kind_scalar_round_trips(self):
        for kind in SemanticElementKinds.ALL:
            encoded = json.dumps({'kind': str(kind)})
            self.assertEqual(SemanticElementKind.parse(json.loads(encoded)['kind']), kind)

    def test_should_preserve_valid_unknown_semantic_element_kind_on_wire(self):
        for value in ('acme.route-definition', 'partner.future-category', 'future-definition'):
            incoming = json.dumps({'kind': value})
            kind = SemanticElementKind.parse(json.loads(incoming)['kind'])
            self.assertFalse(SemanticElementKinds.is_core(kind))
            self.assertEqual(json.dumps({'kind': str(kind)}), incoming)

    def test_invalid_wire_values_and_numeric_ordinals_are_rejected(self):
        for text in ('null', '""', '"Action Definition"', '"acme..route-definition"', '4', 'true', '[]', '{"value":"action-definition"}'):
            with self.subTest(text=text), self.assertRaises(SemanticElementKindError):
                SemanticElementKind.parse(json.loads(text))

    def test_default_serializer_requires_explicit_mapping(self):
        with self.assertRaises(TypeError):
            json.dumps({'kind': SemanticElementKinds.ACTION_DEFINITION})

    def test_demo_core_custom_and_invalid_kind(self):
        self.assertTrue(SemanticElementKinds.is_core(SemanticElementKind.parse('action-definition')))
        custom = SemanticElementKind.parse('acme.route-definition')
        self.assertFalse(SemanticElementKinds.is_core(custom))
        self.assertEqual(str(custom), 'acme.route-definition')
        self.assertEqual(SemanticElementKind.parse(str(custom)), custom)
        with self.assertRaises(SemanticElementKindError) as caught:
            SemanticElementKind.parse('Action Definition')
        self.assertEqual(caught.exception.code, 'SEM-KIND-002')
