import ast
from dataclasses import fields
from pathlib import Path
from typing import get_type_hints
import unittest
from architecture_fitness.discovery import discover
from architecture_fitness.engine import execute
import semantic_kernel.public as kernel
from model_core.public import (
    TypeLookup, TypeValidationContext, TypeValidationRule, TypeValidationResult,
    TypeValidationDiagnostic, TypeValidationPath, TypeValidationSeverity, TypeValidator,
    TypeDataComposition, FieldConstraintValidationRule, SemanticReferenceValidationRule,
    PrimitiveTypeRef, SemanticTypeRef, MinLengthConstraint, PrimitiveType,
)

ROOT = Path(__file__).resolve().parents[2]


class TypeValidationBoundaryTests(unittest.TestCase):
    def test_model_owned_validation_uses_only_approved_dependencies(self):
        for cls in (TypeLookup, TypeValidationContext, TypeValidationRule, TypeValidationResult, TypeValidationDiagnostic, TypeValidationPath, TypeValidationSeverity, TypeValidator):
            self.assertEqual(cls.__module__, 'model_core.public')
            self.assertNotIn(cls.__name__, kernel.__all__)
        model = discover(ROOT)
        self.assertEqual(model.graph('observed')['semantic-kernel'], set())
        self.assertEqual(model.graph('observed')['model-core'], {'semantic-kernel'})
        self.assertEqual(execute(model)['summary']['status'], 'HEALTHY')
        self.assertEqual({f.name for f in fields(TypeValidationContext)}, {'type_lookup'})
        self.assertEqual({f.name for f in fields(TypeValidationResult)}, {'diagnostics'})
        self.assertEqual({f.name for f in fields(TypeValidationPath)}, {'type_name', 'field_name', 'constraint_kind'})
        self.assertEqual({name for name in TypeLookup.__dict__ if not name.startswith('_')}, {'find'})

    def test_policy_stays_outside_representation_and_no_instance_validator(self):
        for cls in (PrimitiveType, PrimitiveTypeRef, SemanticTypeRef, MinLengthConstraint):
            for member in ('validate', 'supports', 'allowed_constraints', 'primitive_constraint_kinds'):
                self.assertFalse(hasattr(cls, member))
        for member in ('validate_value', 'validate_instance', 'compile', 'persist', 'register', 'resolve', 'latest'):
            self.assertFalse(hasattr(TypeValidator, member))
        hints = get_type_hints(TypeValidator.validate)
        self.assertIs(hints['type_definition'], TypeDataComposition)
        self.assertIs(hints['context'], TypeValidationContext)
        self.assertIs(hints['return'], TypeValidationResult)

    def test_builtin_rule_methods_have_no_model_writes_or_recursive_validation(self):
        source = ROOT / 'platform/model/model-core/src/model_core/public.py'
        tree = ast.parse(source.read_text())
        names = {'StructuralTypeValidationRule', 'FieldConstraintValidationRule', 'SemanticReferenceValidationRule'}
        for cls in (n for n in tree.body if isinstance(n, ast.ClassDef) and n.name in names):
            method = next(n for n in cls.body if isinstance(n, ast.FunctionDef) and n.name == 'validate')
            for node in ast.walk(method):
                if isinstance(node, ast.Attribute) and isinstance(node.ctx, ast.Store):
                    self.fail(f'Model attribute mutation in {cls.name}')
                if isinstance(node, ast.Call):
                    if isinstance(node.func, ast.Name):
                        self.assertNotIn(node.func.id, {'setattr', 'exec', 'eval', 'open', '__import__'})
                    if isinstance(node.func, ast.Attribute):
                        self.assertNotIn(node.func.attr, {'__setattr__', 'validate', 'validate_instance', 'compile', 'register', 'resolve'})
