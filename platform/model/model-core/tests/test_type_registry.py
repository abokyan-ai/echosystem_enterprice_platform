from dataclasses import replace, FrozenInstanceError, fields
from itertools import permutations
from types import SimpleNamespace
import unittest
from fixtures.type_validation import host, field
from fixtures.type_registry import entry, exact
from semantic_kernel.public import Namespace, ElementRef, SemanticElementId, SemanticContextRef, SemanticElementKinds, SemanticVersion, QualifiedName, ElementVersionRef, PrimitiveTypes
from model_core.public import (
    TypeRegistry, TypeRegistryLookup, TypeRegistryAmbiguityError, TypeRegistrationResult,
    TypeRegistrationOutcome as Outcome, TypeRegistrationFailure as Failure,
    TypeRegistrationDiagnostic, TypeValidationSeverity, DataFacet, TypeDataComposition,
    PrimitiveTypeRef, MaxLengthConstraint, PrecisionConstraint, FieldPresence,
)


class TypeRegistryTests(unittest.TestCase):
    def setUp(self):
        self.model = entry(fields=(field(),))
        self.empty = TypeRegistry(self.model.type_definition.context)

    def populated(self, *models):
        registry = self.empty
        for model in models:
            result = registry.register(model)
            self.assertTrue(result.is_success, result.diagnostics)
            registry = result.registry
        return registry

    def failure(self, result, code, registry):
        self.assertFalse(result.is_success)
        self.assertIs(result.registry, registry)
        self.assertEqual(result.outcome, Outcome.REJECTED)
        self.assertEqual([d.code for d in result.diagnostics], [code])

    def test_register_exact_version_and_all_indexes(self):
        registry = self.populated(self.model)
        found = registry.find_by_version(exact(self.model))
        self.assertEqual(found.data, self.model.data)
        self.assertEqual(found.type_definition.id, self.model.type_definition.id)
        self.assertEqual(registry.find_by_id(found.type_definition.id), (found,))
        self.assertEqual(registry.find_by_qualified_name(found.type_definition.qualified_name), (found,))
        self.assertTrue(registry.contains(exact(self.model)))

    def test_versions_coexist_and_bare_id_returns_all(self):
        second = entry(version='1.1.0')
        registry = self.populated(self.model, second)
        self.assertEqual(registry.list_versions(host().id), (SemanticVersion(1, 0, 0), SemanticVersion(1, 1, 0)))
        for model in (self.model, second):
            self.assertEqual(registry.find_by_version(exact(model)).type_definition.version, model.type_definition.version)
        self.assertEqual(len(registry.find_by_id(host().id)), 2)
        self.assertEqual(len(registry.find_by_qualified_name(host().qualified_name)), 2)

    def test_unknown_exact_never_falls_back(self):
        registry = self.populated(self.model)
        unknown = exact(entry(version='2.0.0'))
        self.assertIsNone(registry.find_by_version(unknown))
        self.assertFalse(registry.contains(unknown))
        other = ElementVersionRef(host(9).id, self.model.type_definition.version)
        self.assertIsNone(registry.find_by_version(other))

    def test_numeric_version_order_not_lexical_or_insertion(self):
        models = [entry(version=v) for v in ('10.0.0', '1.10.0', '2.0.0', '1.2.0', '1.2.9', '1.2.10')]
        registry = self.populated(*models)
        self.assertEqual([str(v) for v in registry.list_versions(host().id)], ['1.2.0', '1.2.9', '1.2.10', '1.10.0', '2.0.0', '10.0.0'])

    def test_missing_broad_queries_are_empty(self):
        registry = self.populated(self.model)
        self.assertEqual(registry.find_by_id(host(9).id), ())
        self.assertEqual(registry.list_versions(host(9).id), ())
        self.assertEqual(registry.find_by_qualified_name(QualifiedName.parse('missing.Type')), ())
        self.assertIsNone(registry.find(ElementRef(host(9).id)))

    def test_equal_separate_definitions_are_idempotent(self):
        registry = self.populated(self.model)
        for model in (self.model, entry(fields=(field(),))):
            result = registry.register(model)
            self.assertEqual(result.outcome, Outcome.ALREADY_REGISTERED)
            self.assertIs(result.registry, registry)
            self.assertEqual(result.diagnostics, ())
        self.assertEqual(len(registry.entries), 1)

    def test_conflicting_facet_content_is_rejected(self):
        registry = self.populated(self.model)
        mutations = (entry(fields=(field(values=(MaxLengthConstraint(10),)),)), entry(fields=(field(name='other'),)), entry(fields=(field(PrimitiveTypeRef(PrimitiveTypes.BOOLEAN)),)), entry(absent=True), entry())
        for model in mutations:
            with self.subTest(model=model):
                self.failure(registry.register(model), Failure.DUPLICATE_CONFLICT, registry)
        self.assertEqual(registry.find_by_version(exact(self.model)).data, self.model.data)

    def test_field_identity_presence_and_order_are_registration_content(self):
        first = entry(fields=(field(name='a'), field(number=1, name='b')))
        registry = self.populated(first)
        for model in (entry(fields=(field(number=2, name='a'), field(number=1, name='b'))), entry(fields=(field(name='a', presence=FieldPresence.OPTIONAL), field(number=1, name='b'))), entry(fields=tuple(reversed(first.data.fields)))):
            self.failure(registry.register(model), Failure.DUPLICATE_CONFLICT, registry)

    def test_same_version_rename_is_conflict(self):
        registry = self.populated(self.model)
        model = entry(name='crm.Client', fields=(field(),))
        self.failure(registry.register(model), Failure.DUPLICATE_CONFLICT, registry)
        self.assertEqual(registry.find_by_qualified_name(model.type_definition.qualified_name), ())

    def test_different_id_same_name_is_collision(self):
        registry = self.populated(self.model)
        for version in ('1.0.0', '9.0.0'):
            self.failure(registry.register(entry(1, version)), Failure.QUALIFIED_NAME_COLLISION, registry)
        self.assertEqual(registry.find_by_id(host(1).id), ())
        self.assertEqual(len(registry.find_by_qualified_name(host().qualified_name)), 1)

    def test_rename_keeps_exact_versions_and_historical_name(self):
        old, new = entry(), entry(version='2.0.0', name='crm.Client')
        registry = self.populated(old, new)
        self.assertEqual(registry.find_by_qualified_name(old.type_definition.qualified_name), (registry.find_by_version(exact(old)),))
        self.assertEqual(registry.find_by_qualified_name(new.type_definition.qualified_name), (registry.find_by_version(exact(new)),))
        self.assertEqual(registry.find_by_version(exact(old)).type_definition.id, registry.find_by_version(exact(new)).type_definition.id)

    def test_historical_name_remains_owned(self):
        registry = self.populated(entry(), entry(version='2.0.0', name='crm.Client'))
        self.failure(registry.register(entry(8)), Failure.QUALIFIED_NAME_COLLISION, registry)

    def test_rename_backfill_does_not_depend_on_registration_order(self):
        old, new = entry(), entry(version='2.0.0', name='crm.Client')
        forward = self.populated(old, new)
        backward = self.populated(new, old)
        self.assertEqual(forward, backward)
        self.assertEqual(forward.entries, backward.entries)

    def test_rename_to_other_identity_owned_name_rejected(self):
        registry = self.populated(entry(), entry(1, name='crm.Client'))
        self.failure(registry.register(entry(version='2.0.0', name='crm.Client')), Failure.QUALIFIED_NAME_COLLISION, registry)
        self.assertEqual(registry.list_versions(host().id), (SemanticVersion(1, 0, 0),))

    def test_context_scope_rejects_cross_context_even_same_identity(self):
        other = SemanticContextRef(host(90).id)
        registry = self.populated(self.model)
        result = registry.register(entry(context=other))
        self.failure(result, Failure.SCOPE_MISMATCH, registry)
        self.assertEqual(result.diagnostics[0].context, other)

    def test_separate_contexts_allow_same_name_and_do_not_leak(self):
        other = SemanticContextRef(host(90).id)
        a = self.populated(entry())
        b_model = entry(1, context=other)
        b = TypeRegistry(other).register(b_model).registry
        self.assertEqual(len(b.find_by_qualified_name(host().qualified_name)), 1)
        self.assertIsNone(a.find_by_version(exact(b_model)))
        self.assertIsNone(b.find_by_version(exact(entry())))

    def test_snapshot_a_is_unchanged_by_snapshot_b(self):
        result = self.empty.register(self.model)
        self.assertEqual(self.empty.entries, ())
        self.assertIsNone(self.empty.find_by_version(exact(self.model)))
        self.assertNotEqual(self.empty, result.registry)
        self.assertEqual(len(result.registry.entries), 1)

    def test_indexes_and_exposed_collections_are_immutable(self):
        registry = self.populated(self.model)
        with self.assertRaises(FrozenInstanceError):
            registry.context = SemanticContextRef(host(80).id)
        for index in (registry._exact_index, registry._identity_index, registry._name_index):
            with self.assertRaises(TypeError):
                index['bad'] = self.model
        for collection in (registry.entries, registry.find_by_id(host().id), registry.find_by_qualified_name(host().qualified_name)):
            self.assertIs(type(collection), tuple)
            with self.assertRaises(TypeError):
                collection[0] = self.model

    def test_external_mutable_host_is_captured_not_retained(self):
        source = SimpleNamespace(**{f.name: getattr(host(), f.name) for f in fields(host())})
        model = TypeDataComposition(source, self.model.data)
        registry = self.populated(model)
        source.id = host(8).id
        source.qualified_name = QualifiedName.parse('crm.Changed')
        source.context = SemanticContextRef(host(80).id)
        source.kind = SemanticElementKinds.ACTION_DEFINITION
        source.version = SemanticVersion(9, 0, 0)
        stored = registry.entries[0].type_definition
        self.assertEqual(stored.id, host().id)
        self.assertEqual(stored.qualified_name, host().qualified_name)
        self.assertEqual(stored.version, host().version)
        with self.assertRaises(FrozenInstanceError):
            stored.qualified_name = source.qualified_name
        with self.assertRaises(FrozenInstanceError):
            registry.entries[0].data.fields[0].name = self.model.data.fields[0].name

    def test_source_field_list_cannot_mutate_registry(self):
        source = [field()]
        model = TypeDataComposition(host(), DataFacet(source))
        registry = self.populated(model)
        source.clear()
        self.assertEqual(len(registry.entries[0].data.fields), 1)

    def test_invalid_input_returns_diagnostic(self):
        for value in (None, {}, host(), 42, 'sales.Customer'):
            with self.subTest(value=value):
                self.failure(self.empty.register(value), Failure.INVALID_REGISTRY_ENTRY, self.empty)

    def test_non_type_element_is_distinct_failure(self):
        for kind in (SemanticElementKinds.ACTION_DEFINITION, SemanticElementKinds.POLICY_DEFINITION):
            result = self.empty.register(host(kind=kind))
            self.failure(result, Failure.UNSUPPORTED_ELEMENT_KIND, self.empty)
            self.assertEqual(result.diagnostics[0].reference, exact(entry()))
            self.assertEqual(result.diagnostics[0].qualified_name, host().qualified_name)
        source = SimpleNamespace(**{f.name: getattr(host(), f.name) for f in fields(host())})
        model = TypeDataComposition(source)
        source.kind = SemanticElementKinds.ACTION_DEFINITION
        self.failure(self.empty.register(model), Failure.UNSUPPORTED_ELEMENT_KIND, self.empty)

    def test_mutated_host_invalid_identity_is_rejected(self):
        source = SimpleNamespace(**{f.name: getattr(host(), f.name) for f in fields(host())})
        model = TypeDataComposition(source)
        source.version = '1.0.0'
        self.failure(self.empty.register(model), Failure.INVALID_REGISTRY_ENTRY, self.empty)

    def test_mutable_facet_subclass_is_rejected(self):
        class ExtendedData(DataFacet):
            pass
        model = TypeDataComposition(host(), ExtendedData((field(),)))
        self.failure(self.empty.register(model), Failure.INVALID_REGISTRY_ENTRY, self.empty)

    def test_registration_is_not_semantic_validation(self):
        invalid = entry(fields=(field(values=(PrecisionConstraint(18),)),))
        result = self.empty.register(invalid)
        self.assertTrue(result.is_success)
        self.assertEqual(result.registry.entries[0].data, invalid.data)

    def test_absent_and_empty_facet_are_distinct(self):
        absent = self.populated(entry(absent=True))
        self.failure(absent.register(entry()), Failure.DUPLICATE_CONFLICT, absent)
        self.assertIsNone(absent.entries[0].data)

    def test_lookup_rejects_untyped_inputs(self):
        for operation in (self.empty.find_by_id, self.empty.find_by_qualified_name, self.empty.find_by_version, self.empty.contains, self.empty.find, self.empty.list_versions):
            for value in (None, 'sales.Customer', 1):
                with self.assertRaises(TypeError):
                    operation(value)
        with self.assertRaises(TypeError):
            TypeRegistry(None)

    def test_direct_type_lookup_zero_or_one(self):
        reference = ElementRef(host().id)
        self.assertIsNone(self.empty.find(reference))
        registry = self.populated(self.model)
        self.assertEqual(registry.find(reference), registry.entries[0].type_definition)

    def test_direct_type_lookup_ambiguity_is_explicit(self):
        registry = self.populated(entry(), entry(version='2.0.0'))
        with self.assertRaises(TypeRegistryAmbiguityError) as caught:
            registry.find(ElementRef(host().id))
        self.assertEqual(caught.exception.code, 'TYPE-REG-006')
        self.assertEqual(caught.exception.references, (exact(entry()), exact(entry(version='2.0.0'))))

    def test_bound_view_chooses_only_explicit_versions(self):
        old, new, other = entry(), entry(version='2.0.0'), entry(1, name='sales.Address')
        registry = self.populated(old, new, other)
        for chosen in (old, new):
            view = registry.bind_versions([exact(chosen)])
            self.assertEqual(view.find(ElementRef(host().id)).version, chosen.type_definition.version)
            self.assertIsNone(view.find(ElementRef(other.type_definition.id)))
        self.assertIsNone(registry.bind_versions([]).find(ElementRef(host().id)))

    def test_invalid_bound_selections_are_programming_errors(self):
        registry = self.populated(entry(), entry(version='2.0.0'))
        for refs in ([exact(entry()), exact(entry(version='2.0.0'))], [exact(entry())] * 2, [exact(entry(version='9.0.0'))]):
            with self.assertRaises(ValueError):
                registry.bind_versions(refs)
        for refs in (None, {}, [ElementRef(host().id)]):
            with self.assertRaises(TypeError):
                registry.bind_versions(refs)
        with self.assertRaises(TypeError):
            registry.bind_versions([]).find(None)

    def test_bound_view_copies_inputs_and_is_snapshot_specific(self):
        registry = self.populated(entry())
        source = [exact(entry())]
        view = registry.bind_versions(source)
        source.clear()
        expanded = registry.register(entry(1, name='sales.Address')).registry
        self.assertEqual(len(view.references), 1)
        self.assertIsNone(view.find(ElementRef(host(1).id)))
        self.assertIsNotNone(expanded.find(ElementRef(host(1).id)))
        with self.assertRaises(FrozenInstanceError):
            view.references = ()

    def test_registration_permutations_have_equivalent_indexes(self):
        models = (entry(), entry(version='2.0.0', name='crm.Client'), entry(1, name='sales.Address'))
        baseline = self.populated(*models)
        for order in permutations(models):
            registry = self.populated(*order)
            self.assertEqual(registry, baseline)
            self.assertEqual(registry.entries, baseline.entries)
            self.assertEqual(registry.find_by_id(host().id), baseline.find_by_id(host().id))
            self.assertEqual(registry.find_by_qualified_name(host().qualified_name), baseline.find_by_qualified_name(host().qualified_name))
            self.assertEqual(registry.register(entry(8)).diagnostics, baseline.register(entry(8)).diagnostics)

    def test_diagnostic_coordinates_and_result_invariants(self):
        registry = self.populated(self.model)
        result = registry.register(entry(name='crm.Client'))
        diagnostic = result.diagnostics[0]
        self.assertEqual(diagnostic.reference, exact(entry()))
        self.assertEqual(diagnostic.qualified_name, QualifiedName.parse('crm.Client'))
        self.assertEqual(diagnostic.context, registry.context)
        self.assertEqual(str(diagnostic.path), 'crm.Client')
        self.assertEqual(diagnostic.severity, TypeValidationSeverity.ERROR)
        source = list(result.diagnostics)
        copied = TypeRegistrationResult(registry, Outcome.REJECTED, source)
        source.clear()
        self.assertEqual(copied.diagnostics, result.diagnostics)
        with self.assertRaises(FrozenInstanceError):
            diagnostic.message = 'changed'
        for outcome, diagnostics in ((Outcome.REJECTED, ()), (Outcome.REGISTERED, result.diagnostics)):
            with self.assertRaises(ValueError):
                TypeRegistrationResult(registry, outcome, diagnostics)
        with self.assertRaises(TypeError):
            TypeRegistrationDiagnostic('TYPE-REG-001', 'bad')
        with self.assertRaises(TypeError):
            TypeRegistrationResult(registry, Outcome.REJECTED, [None])

    def test_nested_mutable_namespace_extension_is_rejected(self):
        class MutableNamespace(Namespace):
            pass
        name = QualifiedName(MutableNamespace('sales'), 'Customer')
        model = entry()
        model = TypeDataComposition(replace(model.type_definition, qualified_name=name))
        self.failure(self.empty.register(model), Failure.INVALID_REGISTRY_ENTRY, self.empty)
        with self.assertRaises(TypeError):
            self.empty.find_by_qualified_name(name)

    def test_nested_context_identity_extension_is_rejected(self):
        class ExtendedId(SemanticElementId):
            pass
        context = SemanticContextRef(ExtendedId(str(host(90).id)))
        with self.assertRaises(TypeError):
            TypeRegistry(context)
        self.failure(self.empty.register(entry(context=context)), Failure.INVALID_REGISTRY_ENTRY, self.empty)
