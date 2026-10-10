from dataclasses import replace
import unittest
from fixtures.type_validation import host, field, definition, ReadOnlyLookup
from semantic_kernel.public import PrimitiveTypes, ElementRef, SemanticElementKinds, SemanticVersion
from model_core.public import (
    TypeValidator, TypeValidationContext, SemanticTypeRef, PrimitiveTypeRef,
    MaxLengthConstraint,
)


class TypeValidationIntegrationTests(unittest.TestCase):
    def test_customer_address_readonly_lookup_integration(self):
        customer, address = host(1), host(2, name='sales.Address')
        model = definition(field(SemanticTypeRef(ElementRef(address.id)), name='address'), owner=customer)
        result = TypeValidator().validate(model, TypeValidationContext(ReadOnlyLookup((customer, address))))
        self.assertTrue(result.is_valid)
        self.assertEqual(result.diagnostics, ())

    def test_missing_address_is_a_full_validation_error(self):
        customer, address = host(1), host(2, name='sales.Address')
        model = definition(field(SemanticTypeRef(ElementRef(address.id)), name='address'), owner=customer)
        result = TypeValidator().validate(model, TypeValidationContext(ReadOnlyLookup((customer,))))
        self.assertEqual([d.code for d in result.diagnostics], ['TYPE-VAL-REF-001'])
        self.assertEqual(str(result.diagnostics[0].path), 'sales.Customer.data.fields.address')

    def test_existing_non_type_target_is_distinct_from_missing(self):
        action = host(2, name='sales.Submit', kind=SemanticElementKinds.ACTION_DEFINITION)
        model = definition(field(SemanticTypeRef(ElementRef(action.id)), name='customer'))
        result = TypeValidator().validate(model, TypeValidationContext(ReadOnlyLookup((action,))))
        self.assertEqual([d.code for d in result.diagnostics], ['TYPE-VAL-REF-002'])

    def test_self_and_mutual_graphs_validate_without_recursive_execution(self):
        a, b = host(1, name='test.A'), host(2, name='test.B')
        models = (definition(field(SemanticTypeRef(ElementRef(a.id)), name='self'), owner=a), definition(field(SemanticTypeRef(ElementRef(b.id)), name='peerB'), owner=a), definition(field(SemanticTypeRef(ElementRef(a.id)), name='peerA'), owner=b))
        context = TypeValidationContext(ReadOnlyLookup((a, b)))
        for model in models:
            self.assertTrue(TypeValidator().validate(model, context).is_valid)

    def test_current_validation_does_not_revalidate_target_constraints(self):
        customer, address = host(1), host(2, name='sales.Address')
        invalid_address = definition(field(PrimitiveTypeRef(PrimitiveTypes.BOOLEAN), [MaxLengthConstraint(10)]), owner=address)
        model = definition(field(SemanticTypeRef(ElementRef(address.id))), owner=customer)
        context = TypeValidationContext(ReadOnlyLookup((customer, address)))
        self.assertFalse(TypeValidator().validate(invalid_address, context).is_valid)
        self.assertTrue(TypeValidator().validate(model, context).is_valid)

    def test_lookup_view_supplies_version_without_validator_selection(self):
        target = host(2)
        model = definition(field(SemanticTypeRef(ElementRef(target.id))))
        validator = TypeValidator()
        first = validator.validate(model, TypeValidationContext(ReadOnlyLookup((target,))))
        second = validator.validate(model, TypeValidationContext(ReadOnlyLookup((replace(target, version=SemanticVersion(2, 0, 0)),))))
        self.assertEqual(first, second)
        self.assertTrue(first.is_valid)
        self.assertFalse(hasattr(model.data.fields[0].type, 'version'))
