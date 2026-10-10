from dataclasses import FrozenInstanceError
import unittest
from semantic_kernel.public import FacetKind, FacetKindError, FacetKinds, FacetApplicability, FacetApplicabilityError, SemanticElementKind, SemanticElementKinds


class FacetKindTests(unittest.TestCase):
    def test_all_fourteen_core_values_are_typed_and_canonical(self):
        names = ('data', 'behavior', 'lifecycle', 'workflow', 'rule', 'policy', 'security', 'api', 'event', 'persistence', 'experience', 'search', 'audit', 'integration')
        self.assertEqual(tuple(map(str, FacetKinds.ALL)), names)
        for name in names:
            value = getattr(FacetKinds, name.upper())
            self.assertIsInstance(value, FacetKind)
            self.assertEqual(FacetKind.parse(name), value)
            self.assertTrue(FacetKinds.is_core(value))
        self.assertFalse(FacetKinds.is_core('data'))
        self.assertFalse(FacetKinds.is_core(SemanticElementKind('data')))

    def test_unknown_scoped_and_future_unqualified_values_round_trip(self):
        for text in ('acme.routing', 'industry.healthcare.regulatory', 'partner.analytics', 'future-concern'):
            kind = FacetKind.parse(text)
            self.assertEqual(str(kind), text)
            self.assertEqual(FacetKind.parse(str(kind)), kind)
            self.assertEqual(FacetKind.try_parse(text), kind)
            self.assertFalse(FacetKinds.is_core(kind))

    def test_required_kind_diagnostic(self):
        for value in (None, '', ' ', '\t\n'):
            with self.subTest(value=value), self.assertRaises(FacetKindError) as caught:
                FacetKind(value)
            self.assertEqual(caught.exception.code, 'SEM-FACET-KIND-001')

    def test_malformed_kind_diagnostic_without_normalization(self):
        for value in ('Data', 'Policy Facet', '.data', 'data.', 'acme..routing', 'acme/routing', 'data ', ' data', 'acme._routing', 'acme.route--kind', 'acme.route-', 'acme.1routing', 'dáta', 'data\n', '*', 1, True, [], {}):
            with self.subTest(value=value), self.assertRaises(FacetKindError) as caught:
                FacetKind.parse(value)
            self.assertEqual(caught.exception.code, 'SEM-FACET-KIND-002')
            self.assertIsNone(FacetKind.try_parse(value))
        with self.assertRaises(FacetKindError) as caught:
            FacetKind.parse('acme..routing')
        self.assertEqual(caught.exception.segment_index, 1)

    def test_equality_hash_and_distinct_semantic_kind_intent(self):
        a = FacetKind('data')
        b = FacetKind.parse('data')
        self.assertEqual(a, b)
        self.assertEqual(hash(a), hash(b))
        self.assertEqual({a: 'concern'}[b], 'concern')
        self.assertNotEqual(a, FacetKinds.POLICY)
        self.assertNotEqual(a, 'data')
        self.assertNotEqual(a, SemanticElementKind('data'))
        with self.assertRaises(TypeError):
            a < b

    def test_value_and_catalog_are_immutable(self):
        with self.assertRaises(FrozenInstanceError):
            FacetKinds.DATA.value = 'policy'
        with self.assertRaises(FrozenInstanceError):
            FacetKinds.DATA = FacetKinds.POLICY
        self.assertIsInstance(FacetKinds.ALL, tuple)
        self.assertFalse(hasattr(FacetKinds.DATA, '__dict__'))

    def test_safe_parse_propagates_unexpected_failure(self):
        class Broken(FacetKind):
            def __post_init__(self):
                raise RuntimeError('unexpected')
        with self.assertRaises(RuntimeError):
            Broken.try_parse('data')

    def test_string_subclass_cannot_change_stored_value(self):
        class Tricky(str):
            def split(self, *args):
                return ['data']
            def __str__(self):
                return 'data'
            def __eq__(self, other):
                return False
            __hash__ = None
        kind = FacetKind(Tricky('acme.routing'))
        self.assertIs(type(kind.value), str)
        self.assertEqual(kind, FacetKind('acme.routing'))
        self.assertIsNone(FacetKind.try_parse(Tricky('Policy Facet')))

    def test_diagnostic_explains_grammar_without_echoing_input(self):
        with self.assertRaises(FacetKindError) as caught:
            FacetKind.parse('private/token')
        self.assertIn('kebab-case', caught.exception.message)
        self.assertNotIn('private', str(caught.exception))


class FacetApplicabilityTests(unittest.TestCase):
    def test_representation_retains_typed_facet_and_explicit_host_kinds(self):
        kinds = frozenset({SemanticElementKinds.TYPE_DEFINITION})
        applicability = FacetApplicability(FacetKinds.DATA, kinds)
        self.assertIs(applicability.facet_kind, FacetKinds.DATA)
        self.assertIs(applicability.allowed_element_kinds, kinds)
        self.assertIn(SemanticElementKinds.TYPE_DEFINITION, applicability.allowed_element_kinds)
        self.assertNotIn(SemanticElementKinds.ACTION_DEFINITION, applicability.allowed_element_kinds)

    def test_custom_facet_and_custom_host_need_no_registry(self):
        kind = SemanticElementKind('acme.route-definition')
        rule = FacetApplicability(FacetKind('acme.routing'), frozenset({kind}))
        self.assertIn(kind, rule.allowed_element_kinds)

    def test_empty_set_explicitly_allows_nowhere(self):
        rule = FacetApplicability(FacetKinds.DATA, frozenset())
        self.assertEqual(rule.allowed_element_kinds, frozenset())
        self.assertNotIn(SemanticElementKinds.TYPE_DEFINITION, rule.allowed_element_kinds)

    def test_equality_and_hash_are_set_order_independent(self):
        a = FacetApplicability(FacetKinds.POLICY, frozenset({SemanticElementKinds.TYPE_DEFINITION, SemanticElementKinds.ACTION_DEFINITION}))
        b = FacetApplicability(FacetKind('policy'), frozenset({SemanticElementKinds.ACTION_DEFINITION, SemanticElementKinds.TYPE_DEFINITION}))
        self.assertEqual(a, b)
        self.assertEqual(hash(a), hash(b))
        self.assertNotEqual(a, FacetApplicability(FacetKinds.DATA, b.allowed_element_kinds))
        self.assertNotEqual(a, FacetApplicability(FacetKinds.POLICY, frozenset()))

    def test_construction_rejects_raw_kinds_runtime_classes_and_mutable_sets(self):
        for facet, kinds, code in ((None, frozenset(), '001'), ('data', frozenset(), '002'), (SemanticElementKind('data'), frozenset(), '002'), (FacetKinds.DATA, None, '003'), (FacetKinds.DATA, set(), '003'), (FacetKinds.DATA, [], '003'), (FacetKinds.DATA, frozenset({'type-definition'}), '004'), (FacetKinds.DATA, frozenset({dict}), '004'), (FacetKinds.DATA, frozenset({FacetKinds.DATA}), '004')):
            with self.subTest(code=code), self.assertRaises(FacetApplicabilityError) as caught:
                FacetApplicability(facet, kinds)
            self.assertEqual(caught.exception.code, 'SEM-FACET-APP-' + code)
        with self.assertRaises(TypeError):
            FacetApplicability(FacetKinds.DATA)

    def test_immutable_applicability_has_no_mutable_members(self):
        rule = FacetApplicability(FacetKinds.DATA, frozenset({SemanticElementKinds.TYPE_DEFINITION}))
        with self.assertRaises(FrozenInstanceError):
            rule.facet_kind = FacetKinds.POLICY
        with self.assertRaises(FrozenInstanceError):
            rule.allowed_element_kinds = frozenset()
        self.assertFalse(hasattr(rule.allowed_element_kinds, 'add'))
