from dataclasses import replace
import json
import unittest
from semantic_kernel.public import PrimitiveTypes, QualifiedName
from model_core.public import (
    TypeValidator, TypeValidationContext, TypeValidationResult, TypeValidationRule,
    FieldConstraintValidationRule, SemanticReferenceValidationRule,
    PrimitiveTypeRef, TypeDataComposition, DataFacet, FieldConstraintSet,
    FieldPresence, FieldNullability, PrecisionConstraint, MaxLengthConstraint,
)
from model_core.constraint_wire import field_to_wire
from fixtures.type_validation import ReadOnlyLookup
from test_type_references import typed_customer


class TypeValidationContractTests(unittest.TestCase):
    def test_valid_sales_customer_demo_with_current_public_contract(self):
        composition = typed_customer()
        result = TypeValidator().validate(composition, TypeValidationContext(ReadOnlyLookup((composition.type_definition,))))
        self.assertIs(type(result), TypeValidationResult)
        self.assertTrue(result.is_valid)
        self.assertEqual(result.diagnostics, ())
        self.assertEqual([str(f.type.primitive) for f in composition.data.fields], ['string', 'boolean', 'decimal'])

    def test_invalid_sales_demo_aggregates_two_diagnostics_without_wire_mutation(self):
        model = typed_customer()
        a = replace(model.data.fields[0], constraints=FieldConstraintSet(FieldPresence.REQUIRED, FieldNullability.NON_NULL, [PrecisionConstraint(18)]))
        b = replace(model.data.fields[1], constraints=FieldConstraintSet(FieldPresence.REQUIRED, FieldNullability.NON_NULL, [MaxLengthConstraint(10)]))
        invalid = TypeDataComposition(model.type_definition, DataFacet([a, b, model.data.fields[2]]))
        before = json.dumps([field_to_wire(f) for f in invalid.data.fields])
        result = TypeValidator().validate(invalid, TypeValidationContext(ReadOnlyLookup(())))
        self.assertFalse(result.is_valid)
        self.assertEqual([d.code for d in result.diagnostics], ['TYPE-VAL-CONSTRAINT-001'] * 2)
        self.assertEqual([str(d.path) for d in result.diagnostics], ['sales.Customer.data.fields.name.constraints.precision', 'sales.Customer.data.fields.active.constraints.max-length'])
        self.assertEqual([d.field_id for d in result.diagnostics], [a.id, b.id])
        self.assertEqual(json.dumps([field_to_wire(f) for f in invalid.data.fields]), before)

    def test_representation_stays_separate_from_semantic_judgment(self):
        model = typed_customer()
        credit = replace(model.data.fields[2], type=PrimitiveTypeRef(PrimitiveTypes.STRING))
        composed = TypeDataComposition(model.type_definition, DataFacet([credit]))
        self.assertEqual(credit.constraints, model.data.fields[2].constraints)
        result = TypeValidator().validate(composed, TypeValidationContext(ReadOnlyLookup(())))
        self.assertFalse(result.is_valid)
        self.assertEqual([str(d.path.constraint_kind) for d in result.diagnostics], ['minimum', 'precision', 'scale'])
        self.assertFalse(hasattr(credit, 'validate'))

    def test_diagnostic_path_changes_with_display_name_but_identity_is_retained(self):
        model = typed_customer()
        invalid = replace(model.data.fields[0], constraints=FieldConstraintSet(FieldPresence.REQUIRED, FieldNullability.NON_NULL, [PrecisionConstraint(18)]))
        original = TypeDataComposition(model.type_definition, DataFacet([invalid]))
        renamed = TypeDataComposition(replace(model.type_definition, qualified_name=QualifiedName.parse('crm.Client')), DataFacet([invalid]))
        context = TypeValidationContext(ReadOnlyLookup(()))
        old = TypeValidator().validate(original, context).diagnostics[0]
        new = TypeValidator().validate(renamed, context).diagnostics[0]
        self.assertEqual(old.field_id, new.field_id)
        self.assertNotEqual(old.path, new.path)
        self.assertEqual(str(new.path), 'crm.Client.data.fields.name.constraints.precision')

    def test_builtin_rules_satisfy_the_small_structural_rule_contract(self):
        def consume(rule: TypeValidationRule, definition, context):
            return rule.id, rule.validate(definition, context)
        model = typed_customer()
        context = TypeValidationContext(ReadOnlyLookup(()))
        self.assertEqual(consume(FieldConstraintValidationRule(), model, context), ('TYPE-RULE-FIELD-CONSTRAINT', ()))
        self.assertEqual(consume(SemanticReferenceValidationRule(), model, context), ('TYPE-RULE-SEMANTIC-REFERENCE', ()))
