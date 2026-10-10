import copy
from dataclasses import FrozenInstanceError
import unittest
from semantic_kernel.public import Namespace, NamespaceError, SemanticElementId


class NamespaceTests(unittest.TestCase):
    def test_valid_scopes(self):
        for value in ('sales', 'sales.orders', 'sales.pricing', 'identity', 'identity.parties', 'finance.accounts', 'finance.accounts.payable', 'platform', 'sales-orders', 'accounts_payable', 'sales2.a_9-b'):
            with self.subTest(value=value):
                self.assertEqual(str(Namespace(value)), value)

    def test_canonical_case_and_segments(self):
        scope = Namespace.parse('Sales.Orders')
        self.assertEqual(scope.value, 'sales.orders')
        self.assertEqual(scope.segments, ('sales', 'orders'))
        self.assertIs(scope.segments, scope.segments)

    def test_required_input(self):
        for value in (None, '', ' ', '\t\n', '\u2003'):
            self.assert_rejected(value, 'SEM-NS-001', None)

    def test_non_string_is_not_coerced(self):
        for value in (1, True, [], {}, ('sales',), b'sales', Namespace('sales')):
            self.assert_rejected(value, 'SEM-NS-002', None)

    def test_empty_segments(self):
        for value, index in (('.', 0), ('.sales', 0), ('sales.', 1), ('sales..orders', 1), ('sales.orders..', 2)):
            self.assert_rejected(value, 'SEM-NS-004', index)

    def test_invalid_segments(self):
        for segment in ('9sales', '_sales', '-sales', 'sales orders', 'sales/orders', 'sales\\orders', 'sales:orders', '*', 'sales#orders', 'sales?x', 'https://sales', '"sales"', "'sales'", 'équipe', 'Ｓales', 'sal\x00es', 'sales\n', 'sales\u200b', ' sales', 'sales '):
            with self.subTest(segment=segment):
                self.assert_rejected('valid.' + segment, 'SEM-NS-003', 1)

    def assert_rejected(self, value, code, index):
        for parse in (Namespace, Namespace.parse):
            with self.assertRaises(NamespaceError) as caught:
                parse(value)
            self.assertEqual(caught.exception.code, code)
            self.assertEqual(caught.exception.segment_index, index)
            self.assertTrue(caught.exception.message)
        self.assertIsNone(Namespace.try_parse(value))

    def test_no_reserved_words(self):
        for value in ('platform', 'system', 'internal', 'class', 'namespace', 'module', 'package'):
            self.assertEqual(Namespace(value).value, value)

    def test_value_equality_hash_and_dictionary_keys(self):
        a, b = Namespace('Sales.Orders'), Namespace('sales.orders')
        self.assertEqual(a, b)
        self.assertEqual(hash(a), hash(b))
        self.assertEqual({a: 'found'}[b], 'found')
        self.assertEqual(len({a, b}), 1)
        self.assertNotEqual(a, Namespace('sales.pricing'))
        self.assertNotEqual(a, 'sales.orders')
        self.assertNotEqual(a, ('sales', 'orders'))

    def test_identity_is_independent_of_namespace_rename(self):
        identity = SemanticElementId('sem_550e8400-e29b-41d4-a716-446655440000')
        item = {'id': identity, 'namespace': Namespace('sales.orders')}
        before = item['namespace']
        item['namespace'] = Namespace('commerce.orders')
        self.assertEqual(item['id'], identity)
        self.assertNotEqual(before, item['namespace'])
        self.assertNotEqual(identity, before)
        self.assertIsNone(Namespace.try_parse(identity))
        self.assertIsNone(SemanticElementId.try_parse(before))

    def test_string_round_trip(self):
        for value in ('Sales.Orders', 'sales-orders.Accounts_Payable', 'a.b.c'):
            scope = Namespace(value)
            self.assertEqual(Namespace.parse(str(scope)), scope)

    def test_frozen_value_and_segments(self):
        scope = Namespace('sales.orders')
        for attribute, value in (('value', 'bad..value'), ('_segments', ('bad',)), ('segments', ('bad',))):
            with self.assertRaises((FrozenInstanceError, AttributeError, TypeError)):
                setattr(scope, attribute, value)
        with self.assertRaises(TypeError):
            scope.segments[0] = 'commerce'
        self.assertFalse(hasattr(scope, '__dict__'))

    def test_copy_preserves_value(self):
        scope = Namespace('sales.orders')
        self.assertEqual(copy.copy(scope), scope)
        self.assertEqual(copy.deepcopy(scope), scope)

    def test_no_implicit_ordering(self):
        with self.assertRaises(TypeError):
            Namespace('sales') < Namespace('finance')

    def test_parent_is_naming_only(self):
        scope = Namespace('sales.orders.pricing')
        self.assertEqual(scope.parent(), Namespace('sales.orders'))
        self.assertEqual(scope.parent().parent(), Namespace('sales'))
        self.assertIsNone(Namespace('sales').parent())
        self.assertEqual(scope.value, 'sales.orders.pricing')

    def test_child_is_one_segment_and_does_not_mutate_parent(self):
        scope = Namespace('sales')
        self.assertEqual(scope.child('Orders'), Namespace('sales.orders'))
        self.assertEqual(scope.child('Orders').parent(), scope)
        self.assertEqual(scope.value, 'sales')
        for invalid in ('orders.pricing', '', None, '.orders', 'order management', 'orders/'):
            with self.subTest(invalid=invalid), self.assertRaises(NamespaceError):
                scope.child(invalid)

    def test_safe_parse_only_catches_expected_diagnostics(self):
        class BrokenNamespace(Namespace):
            def __post_init__(self):
                raise RuntimeError('unexpected')
        with self.assertRaises(RuntimeError):
            BrokenNamespace.try_parse('sales')
        self.assertEqual(Namespace.try_parse('Sales'), Namespace('sales'))

    def test_string_subclass_cannot_override_normalization_or_split(self):
        class Tricky(str):
            def lower(self):
                return 'bad..scope'
            def split(self, *args):
                return ['bad..scope']
            def isspace(self):
                return False
        self.assertEqual(Namespace(Tricky('Sales.Orders')), Namespace('sales.orders'))
        self.assertIsNone(Namespace.try_parse(Tricky(' ')))
        self.assertIsNone(Namespace.try_parse(Tricky('sales..orders')))

    def test_no_arbitrary_length_or_depth_limit(self):
        scope = Namespace('a' * 1024 + '.' + '.'.join(['b'] * 128))
        self.assertEqual(len(scope.segments), 129)
        self.assertEqual(Namespace(str(scope)), scope)

    def test_diagnostics_have_context_without_echoing_input(self):
        with self.assertRaises(NamespaceError) as caught:
            Namespace('sales.secret/token')
        error = caught.exception
        self.assertEqual(error.segment_index, 1)
        self.assertIn('ASCII', error.message)
        self.assertNotIn('secret', str(error))
