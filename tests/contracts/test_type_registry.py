from dataclasses import replace, fields
import unittest
from semantic_kernel.public import SemanticVersion, QualifiedName, ElementRef, ElementVersionRef
from model_core.public import TypeRegistry, TypeRegistrationOutcome, TypeDataComposition, TypeLookup, TypeValidationContext, TypeValidator
from test_type_references import typed_customer


class TypeRegistryContractTests(unittest.TestCase):
    def test_sales_two_versions_exact_round_trip(self):
        old = typed_customer()
        new = TypeDataComposition(replace(old.type_definition, version=SemanticVersion(1, 1, 0)), old.data)
        empty = TypeRegistry(old.type_definition.context)
        first = empty.register(old)
        second = first.registry.register(new)
        self.assertEqual(first.outcome, TypeRegistrationOutcome.REGISTERED)
        self.assertEqual(second.outcome, TypeRegistrationOutcome.REGISTERED)
        for model in (old, new):
            reference = ElementVersionRef(model.type_definition.id, model.type_definition.version)
            found = second.registry.find_by_version(reference)
            self.assertEqual(found.data, model.data)
            self.assertEqual(found.type_definition.version, model.type_definition.version)
        self.assertEqual(second.registry.list_versions(old.type_definition.id), (SemanticVersion(1, 0, 0), SemanticVersion(1, 1, 0)))
        self.assertEqual(empty.entries, ())

    def test_both_registry_and_explicit_view_satisfy_type_lookup(self):
        def consume(lookup: TypeLookup, reference):
            return lookup.find(reference)
        model = typed_customer()
        registry = TypeRegistry(model.type_definition.context).register(model).registry
        ref = ElementRef(model.type_definition.id)
        selected = ElementVersionRef(model.type_definition.id, model.type_definition.version)
        for lookup in (registry, registry.bind_versions([selected])):
            self.assertEqual(consume(lookup, ref).id, model.type_definition.id)
            self.assertTrue(TypeValidator().validate(model, TypeValidationContext(lookup)).is_valid)
        self.assertEqual({name for name in TypeLookup.__dict__ if not name.startswith('_')}, {'find'})

    def test_historical_name_returns_only_recorded_versions(self):
        old = typed_customer()
        new = TypeDataComposition(replace(old.type_definition, qualified_name=QualifiedName.parse('crm.Client'), version=SemanticVersion(2, 0, 0)), old.data)
        registry = TypeRegistry(old.type_definition.context).register(new).registry.register(old).registry
        self.assertEqual([x.type_definition.version for x in registry.find_by_qualified_name(old.type_definition.qualified_name)], [SemanticVersion(1, 0, 0)])
        self.assertEqual([x.type_definition.version for x in registry.find_by_qualified_name(new.type_definition.qualified_name)], [SemanticVersion(2, 0, 0)])

    def test_registry_capture_has_only_known_semantic_root_and_preserves_data(self):
        model = typed_customer()
        registered = TypeRegistry(model.type_definition.context).register(model).registry.entries[0]
        self.assertIs(type(registered), TypeDataComposition)
        self.assertEqual({f.name for f in fields(registered.type_definition)}, {'id', 'qualified_name', 'context', 'kind', 'version'})
        self.assertIs(registered.data, model.data)
        for name in ('compile', 'persist', 'validate', 'execute', 'resolve_aliases'):
            self.assertFalse(hasattr(registered.type_definition, name))
