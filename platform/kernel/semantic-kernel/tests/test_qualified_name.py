import copy
from dataclasses import FrozenInstanceError, replace
import unittest
from unittest.mock import patch
from semantic_kernel.public import Namespace, NamespaceError, QualifiedName, QualifiedNameError, SemanticElementId


class QualifiedNameTests(unittest.TestCase):
    def test_structural_construction_and_factory(self):
        namespace = Namespace('sales.orders')
        for name in (QualifiedName(namespace, 'SalesOrder'), QualifiedName.create(namespace, 'SalesOrder')):
            self.assertIs(name.namespace, namespace)
            self.assertEqual(name.local_name, 'SalesOrder')
            self.assertEqual(str(name), 'sales.orders.SalesOrder')

    def test_fixtures_and_final_separator(self):
        for text in ('sales.Customer', 'sales.Product', 'sales.SalesOrder', 'sales.CreateOrder', 'sales.SubmitOrder', 'sales.OrderCreated', 'sales.OrderSubmitted', 'identity.Party', 'billing.Invoice', 'platform.SemanticElement', 'sales.orders.SalesOrder', 'finance.accounts.payable.Invoice'):
            with self.subTest(text=text):
                name = QualifiedName.parse(text)
                namespace, local = text.rsplit('.', 1)
                self.assertEqual(name.namespace, Namespace(namespace))
                self.assertEqual(name.local_name, local)
                self.assertEqual(str(name), text)

    def test_namespace_case_canonical_local_case_preserved(self):
        self.assertEqual(str(QualifiedName.parse('Sales.Orders.SalesOrder')), 'sales.orders.SalesOrder')
        self.assertNotEqual(QualifiedName.parse('sales.Customer'), QualifiedName.parse('sales.customer'))
        self.assertEqual(QualifiedName.parse('Sales.Customer'), QualifiedName.parse('sales.Customer'))

    def test_local_lexical_validity_has_no_style_rules(self):
        for local in ('Customer', 'SalesOrder', 'Order2', 'ApproveOrder', 'OrderSubmitted', 'customer', 'sales_order', 'class', 'namespace', 'C_9'):
            self.assertEqual(QualifiedName(Namespace('sales'), local).local_name, local)

    def test_namespace_hyphens_allowed_local_hyphens_rejected(self):
        self.assertEqual(str(QualifiedName.parse('sales-orders.accounts_payable.Invoice')), 'sales-orders.accounts_payable.Invoice')
        self.assert_rejected('sales.Sales-Order', 'SEM-QN-004', 1)

    def test_required_scalar(self):
        for value in (None, '', ' ', '\t\n', '\u2003'):
            self.assert_rejected(value, 'SEM-QN-001')

    def test_non_string_scalar_is_not_coerced(self):
        for value in (1, True, {}, [], ('sales', 'Customer'), b'sales.Customer', QualifiedName.parse('sales.Customer')):
            self.assert_rejected(value, 'SEM-QN-006')

    def test_unqualified_names_have_no_implicit_root(self):
        for text in ('Customer', 'SalesOrder', 'sales/Customer'):
            self.assert_rejected(text, 'SEM-QN-002')

    def test_empty_segments(self):
        for text, index in (('.Customer', 0), ('.sales.Customer', 0), ('sales..Customer', 1), ('sales.', 1), ('sales.Customer.', 2), ('sales.orders.', 2), ('sales..orders.Customer', 1)):
            self.assert_rejected(text, 'SEM-QN-005', index)

    def test_invalid_namespace_uses_sk02_rules(self):
        for namespace in ('9sales', 'sales/orders', 'sales\\orders', 'sales orders', ' sales', 'sales ', 'équipe', 'sales#orders', 'sales:orders', 'sal\x00es'):
            with self.subTest(namespace=namespace):
                with self.assertRaises(NamespaceError) as original:
                    Namespace.parse(namespace)
                with self.assertRaises(QualifiedNameError) as translated:
                    QualifiedName.parse(namespace + '.Customer')
                self.assertEqual(translated.exception.code, 'SEM-QN-003')
                self.assertEqual(translated.exception.namespace_code, original.exception.code)
                self.assertEqual(translated.exception.segment_index, original.exception.segment_index)
                self.assertIsNone(QualifiedName.try_parse(namespace + '.Customer'))

    def test_invalid_local_names(self):
        for local in ('Customer Name', '.Customer', 'Customer.', 'orders.Customer', 'Customer/Address', 'Customer\\Address', 'Customer#1', 'Customer:Type', '9Customer', '_Customer', '*', 'Customer@v1', 'Customer ', ' Customer', 'Customer\n', 'C\x00ustomer', 'عميل', 'Ｃustomer', '"Customer"'):
            with self.subTest(local=local), self.assertRaises(QualifiedNameError) as caught:
                QualifiedName.create(Namespace('sales'), local)
            self.assertEqual(caught.exception.code, 'SEM-QN-004')

    def test_invalid_local_representations(self):
        for local in (1, True, [], {}, Namespace('sales')):
            with self.subTest(local=local), self.assertRaises(QualifiedNameError) as caught:
                QualifiedName(Namespace('sales'), local)
            self.assertEqual(caught.exception.code, 'SEM-QN-004')
        for local in (None, ''):
            with self.assertRaises(QualifiedNameError) as caught:
                QualifiedName(Namespace('sales'), local)
            self.assertEqual(caught.exception.code, 'SEM-QN-005')

    def test_structural_namespace_must_be_typed(self):
        for namespace, code in ((None, 'SEM-QN-002'), ('sales', 'SEM-QN-003'), (1, 'SEM-QN-003'), ({}, 'SEM-QN-003')):
            with self.assertRaises(QualifiedNameError) as caught:
                QualifiedName(namespace, 'Customer')
            self.assertEqual(caught.exception.code, code)

    def test_parse_delegates_namespace_validation(self):
        with patch.object(Namespace, 'parse', wraps=Namespace.parse) as parse:
            name = QualifiedName.parse('Sales.Orders.SalesOrder')
        parse.assert_called_once_with('Sales.Orders')
        self.assertEqual(name.namespace, Namespace('sales.orders'))

    def test_structural_construction_does_not_reparse_namespace(self):
        namespace = Namespace('sales')
        with patch.object(Namespace, 'parse', side_effect=AssertionError('already validated')):
            self.assertEqual(QualifiedName(namespace, 'Customer').namespace, namespace)

    def test_structural_equality_hash_and_dictionary_keys(self):
        a = QualifiedName(Namespace('Sales'), 'Customer')
        b = QualifiedName.parse('sales.Customer')
        self.assertEqual(a, b)
        self.assertEqual(hash(a), hash(b))
        self.assertEqual({a: 'found'}[b], 'found')
        self.assertEqual(len({a, b}), 1)
        for other in (QualifiedName.parse('billing.Customer'), QualifiedName.parse('sales.Client'), QualifiedName.parse('sales.customer'), 'sales.Customer', Namespace('sales.customer')):
            self.assertNotEqual(a, other)

    def test_frozen_components(self):
        name = QualifiedName.parse('sales.Customer')
        for field, value in (('namespace', Namespace('billing')), ('local_name', 'Client')):
            with self.assertRaises(FrozenInstanceError):
                setattr(name, field, value)
        self.assertFalse(hasattr(name, '__dict__'))

    def test_copies_and_replacement_validate(self):
        name = QualifiedName.parse('sales.Customer')
        self.assertEqual(copy.copy(name), name)
        self.assertEqual(copy.deepcopy(name), name)
        self.assertEqual(replace(name, local_name='Client'), QualifiedName.parse('sales.Client'))
        with self.assertRaises(QualifiedNameError):
            replace(name, local_name='bad.name')

    def test_no_implicit_ordering(self):
        with self.assertRaises(TypeError):
            QualifiedName.parse('sales.Customer') < QualifiedName.parse('sales.Client')

    def test_string_round_trips_for_combinations(self):
        for namespace in ('sales', 'sales.orders', 'finance.accounts.payable', 'sales-orders.accounts_payable', 'Sales.Orders'):
            for local in ('Customer', 'customer', 'SalesOrder', 'Order2', 'sales_order'):
                name = QualifiedName(Namespace(namespace), local)
                self.assertEqual(QualifiedName.parse(str(name)), name)

    def test_rename_and_move_are_new_names_without_id_changes(self):
        identity = SemanticElementId('sem_550e8400-e29b-41d4-a716-446655440000')
        original = QualifiedName.parse('sales.Customer')
        item = {'id': identity, 'name': original}
        for renamed in ('sales.Client', 'crm.Customer'):
            item['name'] = QualifiedName.parse(renamed)
            self.assertEqual(item['id'], identity)
            self.assertNotEqual(item['name'], original)
        self.assertEqual(str(original), 'sales.Customer')
        self.assertNotEqual(original, identity)
        self.assertIsNone(QualifiedName.try_parse(identity))
        self.assertIsNone(SemanticElementId.try_parse(original))

    def test_safe_parse_only_catches_expected_diagnostics(self):
        self.assertEqual(QualifiedName.try_parse('sales.Customer'), QualifiedName.parse('sales.Customer'))
        with patch.object(Namespace, 'parse', side_effect=RuntimeError('unexpected')):
            with self.assertRaises(RuntimeError):
                QualifiedName.try_parse('sales.Customer')

    def test_string_subclasses_cannot_override_split_or_value_equality(self):
        class Tricky(str):
            def rpartition(self, *args):
                return ('bad..scope', '.', 'Customer')
            def __str__(self):
                return 'BadName'
            def __eq__(self, other):
                return False
            __hash__ = None
        parsed = QualifiedName.parse(Tricky('Sales.Customer'))
        structural = QualifiedName(Namespace('sales'), Tricky('Customer'))
        self.assertEqual(parsed, structural)
        self.assertEqual(hash(parsed), hash(structural))
        self.assertIs(type(structural.local_name), str)
        self.assertEqual(str(structural), 'sales.Customer')

    def test_diagnostics_explain_failure_without_echoing_input(self):
        for text, code in (('sales.Secret Token', 'SEM-QN-004'), ('secret/token.Customer', 'SEM-QN-003')):
            with self.assertRaises(QualifiedNameError) as caught:
                QualifiedName.parse(text)
            error = caught.exception
            self.assertEqual(error.code, code)
            self.assertIn('ASCII', error.message)
            self.assertNotIn('Secret', str(error))
            self.assertNotIn('secret/token', str(error))

    def test_segments_have_no_kind_version_tenant_or_security_semantics(self):
        for text in ('sales.v2.Customer', 'TenantA.sales.Customer', 'security.AdminPolicy', 'package.sales.Customer'):
            self.assertEqual(QualifiedName.parse(text).local_name, text.rsplit('.', 1)[1])
        for text in ('type:sales.Customer', 'sales.Customer@v1', 'sales.Customer:2'):
            self.assertIsNone(QualifiedName.try_parse(text))

    def assert_rejected(self, value, code, index=None):
        with self.assertRaises(QualifiedNameError) as caught:
            QualifiedName.parse(value)
        self.assertEqual(caught.exception.code, code)
        self.assertEqual(caught.exception.segment_index, index)
        self.assertIsNone(QualifiedName.try_parse(value))
