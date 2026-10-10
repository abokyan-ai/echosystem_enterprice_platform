import unittest
from fixtures.type_registry import entry, exact
from fixtures.type_validation import field
from semantic_kernel.public import ElementRef
from model_core.public import TypeRegistry, TypeLookup, TypeValidator, TypeValidationContext, SemanticTypeRef, PrecisionConstraint, TypeRegistryAmbiguityError


class TypeRegistryIntegrationTests(unittest.TestCase):
    def registry(self, *models):
        registry = TypeRegistry(models[0].type_definition.context)
        for model in models:
            result = registry.register(model)
            self.assertTrue(result.is_success)
            registry = result.registry
        return registry

    def validate(self, model, lookup: TypeLookup):
        return TypeValidator().validate(model, TypeValidationContext(lookup))

    def test_customer_address_target_resolved_through_actual_registry(self):
        address = entry(1, name='sales.Address')
        customer = entry(fields=(field(SemanticTypeRef(ElementRef(address.type_definition.id)), name='address'),))
        registry = self.registry(customer, address)
        self.assertTrue(self.validate(customer, registry).is_valid)
        self.assertTrue(self.validate(customer, registry.bind_versions([exact(customer), exact(address)])).is_valid)

    def test_missing_target_produces_existing_type06_diagnostic(self):
        address = entry(1, name='sales.Address')
        customer = entry(fields=(field(SemanticTypeRef(ElementRef(address.type_definition.id)), name='address'),))
        result = self.validate(customer, self.registry(customer))
        self.assertEqual([d.code for d in result.diagnostics], ['TYPE-VAL-REF-001'])

    def test_self_reference_does_not_recurse(self):
        plain = entry(name='sales.Employee')
        model = entry(name='sales.Employee', fields=(field(SemanticTypeRef(ElementRef(plain.type_definition.id)), name='manager'),))
        registry = self.registry(model)
        self.assertTrue(self.validate(model, registry).is_valid)
        self.assertTrue(self.validate(model, registry.bind_versions([exact(model)])).is_valid)

    def test_mutual_reference_does_not_recurse(self):
        a, b = entry(name='sales.A'), entry(1, name='sales.B')
        a = entry(name='sales.A', fields=(field(SemanticTypeRef(ElementRef(b.type_definition.id)), name='b'),))
        b = entry(1, name='sales.B', fields=(field(SemanticTypeRef(ElementRef(a.type_definition.id)), name='a'),))
        registry = self.registry(b, a)
        for model in (a, b):
            self.assertTrue(self.validate(model, registry).is_valid)

    def test_registration_and_target_lookup_do_not_execute_validator(self):
        target = entry(1, name='sales.Address', fields=(field(values=(PrecisionConstraint(18),)),))
        customer = entry(fields=(field(SemanticTypeRef(ElementRef(target.type_definition.id))),))
        registry = self.registry(target, customer)
        self.assertFalse(self.validate(target, registry).is_valid)
        self.assertTrue(self.validate(customer, registry).is_valid)

    def test_multiversion_validation_requires_explicit_selection(self):
        old, new = entry(1, name='sales.Address'), entry(1, version='2.0.0', name='crm.Address')
        customer = entry(fields=(field(SemanticTypeRef(ElementRef(old.type_definition.id))),))
        registry = self.registry(old, new, customer)
        with self.assertRaises(TypeRegistryAmbiguityError):
            self.validate(customer, registry)
        for selected in (old, new):
            view = registry.bind_versions([exact(selected)])
            self.assertTrue(self.validate(customer, view).is_valid)
            self.assertEqual(view.find(ElementRef(selected.type_definition.id)).version, selected.type_definition.version)
        self.assertEqual([d.code for d in self.validate(customer, registry.bind_versions([])).diagnostics], ['TYPE-VAL-REF-001'])
