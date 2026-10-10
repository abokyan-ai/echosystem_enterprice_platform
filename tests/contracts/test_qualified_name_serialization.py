"""Scalar mapping at the external JSON boundary; no serializer import in Kernel."""
import json
import unittest
from semantic_kernel.public import Namespace, QualifiedName, QualifiedNameError


class QualifiedNameSerializationTests(unittest.TestCase):
    def test_scalar_and_field_json_round_trip(self):
        name = QualifiedName.create(Namespace('sales.orders'), 'SalesOrder')
        scalar = json.dumps(str(name))
        self.assertIsInstance(json.loads(scalar), str)
        self.assertEqual(QualifiedName.parse(json.loads(scalar)), name)
        encoded = json.dumps({'qualifiedName': str(name)})
        self.assertEqual(encoded, '{"qualifiedName": "sales.orders.SalesOrder"}')
        self.assertEqual(QualifiedName.parse(json.loads(encoded)['qualifiedName']), name)

    def test_namespace_normalizes_local_case_survives(self):
        for local in ('Customer', 'customer', 'sales_order'):
            name = QualifiedName.parse(json.loads(json.dumps('Sales.Orders.' + local)))
            self.assertEqual(json.dumps(str(name)), json.dumps('sales.orders.' + local))

    def test_invalid_json_shapes_and_values(self):
        for text in ('null', '""', '"Customer"', '"sales..Customer"', '"sales.Customer Name"', '123', 'true', '[]', '{"namespace":"sales","localName":"Customer"}'):
            with self.subTest(text=text), self.assertRaises(QualifiedNameError):
                QualifiedName.parse(json.loads(text))

    def test_default_serializer_requires_explicit_scalar(self):
        with self.assertRaises(TypeError):
            json.dumps({'qualifiedName': QualifiedName.parse('sales.Customer')})

    def test_demo(self):
        name = QualifiedName.parse('sales.orders.SalesOrder')
        self.assertEqual(name.namespace, Namespace('sales.orders'))
        self.assertEqual(name.local_name, 'SalesOrder')
        self.assertEqual(str(name), 'sales.orders.SalesOrder')
        self.assertEqual(QualifiedName.parse(json.loads(json.dumps(str(name)))), name)
        for text, code in (('SalesOrder', 'SEM-QN-002'), ('sales.Order Management', 'SEM-QN-004')):
            with self.assertRaises(QualifiedNameError) as caught:
                QualifiedName.parse(text)
            self.assertEqual(caught.exception.code, code)
