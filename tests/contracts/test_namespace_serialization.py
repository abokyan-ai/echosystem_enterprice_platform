"""Explicit scalar wire mapping outside Kernel, following SK-01."""
import json
import unittest
from semantic_kernel.public import Namespace, NamespaceError


class NamespaceSerializationTests(unittest.TestCase):
    def test_scalar_and_field_json_round_trip(self):
        scope = Namespace('sales.orders')
        scalar = json.dumps(str(scope))
        self.assertEqual(json.loads(scalar), 'sales.orders')
        self.assertEqual(Namespace.parse(json.loads(scalar)), scope)
        encoded = json.dumps({'namespace': str(scope)})
        self.assertEqual(encoded, '{"namespace": "sales.orders"}')
        self.assertEqual(Namespace.parse(json.loads(encoded)['namespace']), scope)

    def test_mixed_case_reserializes_canonically(self):
        scope = Namespace.parse(json.loads('{"namespace":"Sales.Orders"}')['namespace'])
        self.assertEqual(json.dumps({'namespace': str(scope)}), '{"namespace": "sales.orders"}')

    def test_invalid_json_values_are_rejected(self):
        for text in ('null', '""', '"sales..orders"', '"sales/orders"', '123', 'true', '[]', '{"segments":["sales"]}'):
            with self.subTest(text=text), self.assertRaises(NamespaceError):
                Namespace.parse(json.loads(text))

    def test_serializer_requires_explicit_scalar_mapping(self):
        with self.assertRaises(TypeError):
            json.dumps({'namespace': Namespace('sales')})

    def test_demo(self):
        scope = Namespace.parse('sales.orders')
        self.assertEqual(scope.segments, ('sales', 'orders'))
        self.assertEqual(Namespace.parse(json.loads(json.dumps(str(scope)))), scope)
        with self.assertRaises(NamespaceError) as caught:
            Namespace.parse('sales..orders')
        self.assertEqual(caught.exception.code, 'SEM-NS-004')
