from dataclasses import dataclass, replace, FrozenInstanceError, fields
import unittest
from fixtures.type_validation import host, field, definition, ReadOnlyLookup
from semantic_kernel.public import PrimitiveTypes, ElementRef, SemanticElementKinds, QualifiedName
from model_core.public import (
    TypeValidator, TypeValidationContext, TypeValidationResult, TypeValidationDiagnostic,
    TypeValidationSeverity, TypeValidationPath, TypeLookup, TypeValidationRule,
    PrimitiveTypeRef, SemanticTypeRef, ConstraintKind, ConstraintKinds, FieldName,
    FieldConstraintSet, FieldPresence, FieldNullability,
    MinLengthConstraint, MaxLengthConstraint, PatternConstraint, MinimumConstraint,
    MaximumConstraint, PrecisionConstraint, ScaleConstraint, primitive_constraint_kinds,
    FieldConstraintValidationRule, SemanticReferenceValidationRule,
)

CONSTRAINTS = (MinLengthConstraint(0), MaxLengthConstraint(200), PatternConstraint('['), MinimumConstraint('-10'), MaximumConstraint('100'), PrecisionConstraint(18), ScaleConstraint(2))
CONTEXT = TypeValidationContext(ReadOnlyLookup(()))


class PrimitiveMatrixTests(unittest.TestCase):
    def check_matrix(self, primitive, allowed):
        for constraint in CONSTRAINTS:
            with self.subTest(primitive=str(primitive), constraint=str(constraint.kind)):
                result = TypeValidator().validate(definition(field(PrimitiveTypeRef(primitive), (constraint,))), CONTEXT)
                self.assertEqual(result.is_valid, str(constraint.kind) in allowed)
                if result.is_valid:
                    self.assertEqual(result.diagnostics, ())
                else:
                    self.assertEqual(len(result.diagnostics), 1)
                    d = result.diagnostics[0]
                    self.assertEqual(d.code, 'TYPE-VAL-CONSTRAINT-001')
                    self.assertEqual(str(d.path), 'sales.Customer.data.fields.value.constraints.' + str(constraint.kind))
                    self.assertEqual(d.field_id, definition(field()).data.fields[0].id)

    def test_string_matrix(self):
        self.check_matrix(PrimitiveTypes.STRING, {'min-length', 'max-length', 'pattern'})

    def test_boolean_matrix(self):
        self.check_matrix(PrimitiveTypes.BOOLEAN, set())

    def test_integer_matrix(self):
        self.check_matrix(PrimitiveTypes.INTEGER, {'minimum', 'maximum'})

    def test_decimal_matrix(self):
        self.check_matrix(PrimitiveTypes.DECIMAL, {'minimum', 'maximum', 'precision', 'scale'})

    def test_date_matrix(self):
        self.check_matrix(PrimitiveTypes.DATE, set())

    def test_datetime_matrix(self):
        self.check_matrix(PrimitiveTypes.DATETIME, set())

    def test_uuid_matrix(self):
        self.check_matrix(PrimitiveTypes.UUID, set())

    def test_policy_is_typed_and_immutable(self):
        allowed = primitive_constraint_kinds(PrimitiveTypes.STRING)
        self.assertIs(type(allowed), frozenset)
        self.assertEqual(allowed, frozenset({ConstraintKinds.MIN_LENGTH, ConstraintKinds.MAX_LENGTH, ConstraintKinds.PATTERN}))
        with self.assertRaises(TypeError):
            primitive_constraint_kinds('string')

    def test_all_presence_nullability_combinations_for_all_variants(self):
        target = host(1)
        context = TypeValidationContext(ReadOnlyLookup((target,)))
        for reference in (*[PrimitiveTypeRef(p) for p in PrimitiveTypes.ALL], SemanticTypeRef(ElementRef(target.id))):
            for presence in FieldPresence:
                for nullability in FieldNullability:
                    with self.subTest(reference=reference, presence=presence, nullability=nullability):
                        self.assertTrue(TypeValidator().validate(definition(field(reference, presence=presence, nullability=nullability)), context).is_valid)

    def test_integer_fractional_minimum_and_maximum_rejected(self):
        for constraint in (MinimumConstraint('0.5'), MaximumConstraint('-0.50')):
            result = TypeValidator().validate(definition(field(PrimitiveTypeRef(PrimitiveTypes.INTEGER), (constraint,))), CONTEXT)
            self.assertEqual([d.code for d in result.diagnostics], ['TYPE-VAL-CONSTRAINT-002'])
            self.assertEqual(result.diagnostics[0].path.constraint_kind, constraint.kind)

    def test_integer_exact_integral_spellings_and_large_bounds(self):
        for value in ('-10', '100', '1.000', '-0.000', '9' * 4096):
            result = TypeValidator().validate(definition(field(PrimitiveTypeRef(PrimitiveTypes.INTEGER), (MinimumConstraint(value),))), CONTEXT)
            self.assertTrue(result.is_valid)

    def test_decimal_fractional_bounds_and_independent_precision_scale(self):
        for constraint in (MinimumConstraint('-3.75'), MaximumConstraint('10.25'), PrecisionConstraint(18), ScaleConstraint(0)):
            self.assertTrue(TypeValidator().validate(definition(field(PrimitiveTypeRef(PrimitiveTypes.DECIMAL), (constraint,))), CONTEXT).is_valid)

    def test_pattern_is_not_compiled_or_evaluated(self):
        self.assertTrue(TypeValidator().validate(definition(field(values=(PatternConstraint('['),))), CONTEXT).is_valid)

    def test_primitive_fields_do_not_use_lookup(self):
        class ExplodingLookup:
            def find(self, reference):
                raise AssertionError('primitive validation performed lookup')
        self.assertTrue(TypeValidator().validate(definition(field()), TypeValidationContext(ExplodingLookup())).is_valid)


class SemanticReferenceRuleTests(unittest.TestCase):
    def test_resolved_type_target_valid(self):
        target = host(1)
        model = definition(field(SemanticTypeRef(ElementRef(target.id))))
        self.assertTrue(TypeValidator().validate(model, TypeValidationContext(ReadOnlyLookup((target,)))).is_valid)

    def test_missing_target_is_error_not_exception(self):
        reference = SemanticTypeRef(ElementRef(host(1).id))
        result = TypeValidator().validate(definition(field(reference)), CONTEXT)
        self.assertFalse(result.is_valid)
        d = result.diagnostics[0]
        self.assertEqual(d.code, 'TYPE-VAL-REF-001')
        self.assertEqual(d.target, reference.target)
        self.assertEqual(str(d.path), 'sales.Customer.data.fields.value')

    def test_existing_action_and_policy_target_are_not_types(self):
        for kind in (SemanticElementKinds.ACTION_DEFINITION, SemanticElementKinds.POLICY_DEFINITION):
            target = host(1, kind=kind)
            result = TypeValidator().validate(definition(field(SemanticTypeRef(ElementRef(target.id)))), TypeValidationContext(ReadOnlyLookup((target,))))
            self.assertEqual([d.code for d in result.diagnostics], ['TYPE-VAL-REF-002'])

    def test_lookup_identity_mismatch_is_diagnostic(self):
        class WrongLookup:
            def find(self, reference):
                return host(2)
        result = TypeValidator().validate(definition(field(SemanticTypeRef(ElementRef(host(1).id)))), TypeValidationContext(WrongLookup()))
        self.assertEqual([d.code for d in result.diagnostics], ['TYPE-VAL-REF-003'])

    def test_no_automatic_self_registration(self):
        owner = host()
        model = definition(field(SemanticTypeRef(ElementRef(owner.id))), owner=owner)
        self.assertTrue(TypeValidator().validate(model, TypeValidationContext(ReadOnlyLookup((owner,)))).is_valid)
        self.assertFalse(TypeValidator().validate(model, CONTEXT).is_valid)

    def test_mutual_reference_definitions_are_not_recursively_validated(self):
        a, b = host(1, name='test.A'), host(2, name='test.B')
        ma = definition(field(SemanticTypeRef(ElementRef(b.id))), owner=a)
        mb = definition(field(SemanticTypeRef(ElementRef(a.id))), owner=b)
        context = TypeValidationContext(ReadOnlyLookup((a, b)))
        self.assertTrue(TypeValidator().validate(ma, context).is_valid)
        self.assertTrue(TypeValidator().validate(mb, context).is_valid)

    def test_primitive_value_constraints_on_semantic_ref_all_rejected(self):
        target = host(1)
        context = TypeValidationContext(ReadOnlyLookup((target,)))
        for constraint in CONSTRAINTS:
            result = TypeValidator().validate(definition(field(SemanticTypeRef(ElementRef(target.id)), (constraint,))), context)
            self.assertEqual([d.code for d in result.diagnostics], ['TYPE-VAL-CONSTRAINT-001'])

    def test_lookup_errors_and_bad_contract_returns_propagate(self):
        class BrokenLookup:
            def find(self, reference):
                raise RuntimeError('provider failure')
        class BadLookup:
            def find(self, reference):
                return object()
        model = definition(field(SemanticTypeRef(ElementRef(host(1).id))))
        with self.assertRaises(RuntimeError):
            TypeValidator().validate(model, TypeValidationContext(BrokenLookup()))
        with self.assertRaises(TypeError):
            TypeValidator().validate(model, TypeValidationContext(BadLookup()))


class ValidationPipelineTests(unittest.TestCase):
    def test_absent_and_empty_data_valid(self):
        for model in (definition(), definition(absent=True)):
            result = TypeValidator().validate(model, CONTEXT)
            self.assertTrue(result.is_valid)
            self.assertEqual(result.diagnostics, ())

    def test_explicit_context_required_and_only_canonical_input(self):
        for value in (None, {}, object()):
            with self.assertRaises(TypeError):
                TypeValidationContext(value)
        with self.assertRaises(TypeError):
            TypeValidator().validate(definition(), None)
        with self.assertRaises(TypeError):
            TypeValidator().validate(host(), CONTEXT)

    def test_multiple_errors_order_and_no_mutation(self):
        a = field(values=(PrecisionConstraint(18),), name='name')
        b = field(PrimitiveTypeRef(PrimitiveTypes.BOOLEAN), (MaxLengthConstraint(10),), name='active', number=1)
        model = definition(a, b)
        before = hash(model.data)
        validator = TypeValidator()
        first = validator.validate(model, CONTEXT)
        second = validator.validate(model, CONTEXT)
        self.assertEqual(first, second)
        self.assertEqual([d.code for d in first.diagnostics], ['TYPE-VAL-CONSTRAINT-001'] * 2)
        self.assertEqual([d.path.field_name for d in first.diagnostics], [a.name, b.name])
        self.assertEqual(hash(model.data), before)
        self.assertEqual(model.data.fields, (a, b))

    def test_constraint_diagnostics_use_canonical_kind_order(self):
        values = (PrecisionConstraint(18), MinimumConstraint('0'), MaxLengthConstraint(10))
        first = definition(field(PrimitiveTypeRef(PrimitiveTypes.BOOLEAN), values))
        second = definition(field(PrimitiveTypeRef(PrimitiveTypes.BOOLEAN), tuple(reversed(values))))
        a, b = TypeValidator().validate(first, CONTEXT), TypeValidator().validate(second, CONTEXT)
        self.assertEqual(a, b)
        self.assertEqual([str(d.path.constraint_kind) for d in a.diagnostics], ['max-length', 'minimum', 'precision'])

    def test_field_reorder_preserves_diagnostic_coordinates_and_ids(self):
        a = field(values=(PrecisionConstraint(18),), name='name')
        b = field(PrimitiveTypeRef(PrimitiveTypes.BOOLEAN), (MaxLengthConstraint(10),), name='active', number=1)
        left = TypeValidator().validate(definition(a, b), CONTEXT)
        right = TypeValidator().validate(definition(b, a), CONTEXT)
        self.assertEqual(set(left.diagnostics), set(right.diagnostics))
        self.assertNotEqual(left.diagnostics, right.diagnostics)

    def test_constraint_error_and_reference_error_are_aggregated(self):
        model = definition(field(SemanticTypeRef(ElementRef(host(1).id)), (MaxLengthConstraint(10),)))
        result = TypeValidator().validate(model, CONTEXT)
        self.assertEqual([d.code for d in result.diagnostics], ['TYPE-VAL-CONSTRAINT-001', 'TYPE-VAL-REF-001'])

    def test_unknown_constraint_fails_closed_at_defensive_boundary(self):
        @dataclass(frozen=True)
        class Unknown:
            kind: ConstraintKind
        # Canonical TYPE-04 construction rejects custom payloads already. Forge
        # a test-only bypass to verify defensive handling, without adding an API.
        cs = FieldConstraintSet(FieldPresence.REQUIRED, FieldNullability.NON_NULL, ())
        object.__setattr__(cs, 'value_constraints', (Unknown(ConstraintKind('acme.routing-code')),))
        f = replace(field(), constraints=cs)
        model = definition(f)
        result = TypeValidator().validate(model, CONTEXT)
        self.assertFalse(result.is_valid)
        self.assertEqual([d.code for d in result.diagnostics], ['TYPE-VAL-CONSTRAINT-003'])
        self.assertEqual(str(result.diagnostics[0].path.constraint_kind), 'acme.routing-code')
        self.assertEqual(model.data.fields[0].constraints.value_constraints, cs.value_constraints)

    def test_derived_validity_and_immutable_result(self):
        path = TypeValidationPath(QualifiedName.parse('sales.Customer'))
        warning = TypeValidationDiagnostic('TYPE-VAL-TEST-001', 'Warning', TypeValidationSeverity.WARNING, path)
        error = replace(warning, severity=TypeValidationSeverity.ERROR)
        source = [warning]
        result = TypeValidationResult(source)
        source.clear()
        self.assertTrue(result.is_valid)
        self.assertFalse(TypeValidationResult([warning, error]).is_valid)
        self.assertEqual({f.name for f in fields(TypeValidationResult)}, {'diagnostics'})
        with self.assertRaises(FrozenInstanceError):
            result.diagnostics = ()
        with self.assertRaises(FrozenInstanceError):
            warning.path.type_name = QualifiedName.parse('crm.Customer')
        with self.assertRaises(TypeError):
            TypeValidationResult([None])

    def test_additional_rule_order_copy_and_core_cannot_be_disabled(self):
        @dataclass(frozen=True)
        class Extra:
            id: str
            def validate(self, model, context):
                return (TypeValidationDiagnostic('TYPE-VAL-TEST-001', self.id, TypeValidationSeverity.WARNING, TypeValidationPath(model.type_definition.qualified_name)),)
        source = [Extra('TYPE-RULE-FIRST'), Extra('TYPE-RULE-SECOND')]
        validator = TypeValidator(source)
        source.clear()
        result = validator.validate(definition(), CONTEXT)
        self.assertEqual([d.message for d in result.diagnostics], ['TYPE-RULE-FIRST', 'TYPE-RULE-SECOND'])
        self.assertTrue(result.is_valid)
        self.assertEqual([r.id for r in validator.rules], ['TYPE-RULE-STRUCTURAL', 'TYPE-RULE-FIELD-CONSTRAINT', 'TYPE-RULE-SEMANTIC-REFERENCE', 'TYPE-RULE-FIRST', 'TYPE-RULE-SECOND'])
        self.assertFalse(TypeValidator([]).validate(definition(field(values=(PrecisionConstraint(18),))), CONTEXT).is_valid)
        for rules in ((Extra('TYPE-RULE-FIRST'), Extra('TYPE-RULE-FIRST')), (FieldConstraintValidationRule(),)):
            with self.assertRaises(ValueError):
                TypeValidator(rules)
        with self.assertRaises(FrozenInstanceError):
            validator.additional_rules = ()

    def test_programmer_rule_errors_propagate(self):
        class Broken:
            id = 'TYPE-RULE-BROKEN'
            def validate(self, model, context):
                raise RuntimeError('unexpected')
        with self.assertRaises(RuntimeError):
            TypeValidator([Broken()]).validate(definition(), CONTEXT)
        for rules in (None, {}, [object()]):
            with self.assertRaises(TypeError):
                TypeValidator(rules)

    def test_path_is_typed_not_identity_or_ordinal(self):
        path = TypeValidationPath(QualifiedName.parse('sales.Customer'), FieldName('name'), ConstraintKinds.MAX_LENGTH)
        self.assertEqual(str(path), 'sales.Customer.data.fields.name.constraints.max-length')
        with self.assertRaises(TypeError):
            TypeValidationPath('sales.Customer')
        with self.assertRaises(TypeError):
            TypeValidationPath(QualifiedName.parse('sales.Customer'), constraint_kind=ConstraintKinds.MAX_LENGTH)

    def test_small_protocol_contracts_are_not_instances_or_registries(self):
        for protocol in (TypeLookup, TypeValidationRule):
            with self.assertRaises(TypeError):
                protocol()
        self.assertEqual({f.name for f in fields(TypeValidationContext)}, {'type_lookup'})
        self.assertNotIn('register', TypeLookup.__dict__)


    def test_current_host_kind_is_checked_at_protocol_boundary(self):
        from types import SimpleNamespace
        original = host()
        mutable = SimpleNamespace(**{f.name: getattr(original, f.name) for f in fields(original)})
        model = definition(owner=mutable)
        # The retained Protocol boundary cannot enforce external deep immutability.
        mutable.kind = SemanticElementKinds.ACTION_DEFINITION
        result = TypeValidator().validate(model, CONTEXT)
        self.assertEqual([d.code for d in result.diagnostics], ['TYPE-VAL-STRUCTURAL-001'])
        self.assertIsNone(result.diagnostics[0].field_id)
        self.assertEqual(str(result.diagnostics[0].path), 'sales.Customer')
        self.assertEqual(mutable.kind, SemanticElementKinds.ACTION_DEFINITION)
