"""Structural consumers and immutable test-only definitions exercise the root contract."""
from dataclasses import dataclass, FrozenInstanceError, replace
from typing import get_type_hints
import unittest
from semantic_kernel.public import SemanticElement, SemanticElementId, QualifiedName, SemanticContextRef

ID = SemanticElementId('sem_550e8400-e29b-41d4-a716-446655440000')
CONTEXT = SemanticContextRef.parse('sem_550e8400-e29b-41d4-a716-446655440001')
OTHER_CONTEXT = SemanticContextRef.parse('sem_550e8400-e29b-41d4-a716-446655440002')


def validate_fixture(id, qualified_name, context):
    # This protects test fixture construction; Protocol is a static contract, not a validator.
    for value, expected in ((id, SemanticElementId), (qualified_name, QualifiedName), (context, SemanticContextRef)):
        if not isinstance(value, expected):
            raise TypeError('Test definition requires ' + expected.__name__)


@dataclass(frozen=True, slots=True)
class TestTypeDefinition:
    id: SemanticElementId
    qualified_name: QualifiedName
    context: SemanticContextRef

    def __post_init__(self):
        validate_fixture(self.id, self.qualified_name, self.context)


@dataclass(frozen=True, slots=True)
class TestActionDefinition:
    id: SemanticElementId
    qualified_name: QualifiedName
    context: SemanticContextRef

    def __post_init__(self):
        validate_fixture(self.id, self.qualified_name, self.context)


def read_definition(element: SemanticElement) -> tuple[SemanticElementId, QualifiedName, SemanticContextRef]:
    return element.id, element.qualified_name, element.context


def read_collection(elements: list[SemanticElement]) -> list[tuple[SemanticElementId, QualifiedName, SemanticContextRef]]:
    return [read_definition(element) for element in elements]


class SemanticElementContractTests(unittest.TestCase):
    def test_two_structural_implementations_share_the_root_consumer(self):
        type_definition = TestTypeDefinition(ID, QualifiedName.parse('sales.Customer'), CONTEXT)
        action_definition = TestActionDefinition(ID, QualifiedName.parse('sales.SubmitOrder'), CONTEXT)
        # No inheritance from a behavior-heavy root is required.
        self.assertNotIn(SemanticElement, TestTypeDefinition.__mro__)
        self.assertNotIn(SemanticElement, TestActionDefinition.__mro__)
        elements: list[SemanticElement] = [type_definition, action_definition]
        actual = read_collection(elements)
        self.assertEqual(actual, [(ID, QualifiedName.parse('sales.Customer'), CONTEXT), (ID, QualifiedName.parse('sales.SubmitOrder'), CONTEXT)])

    def test_identity_name_and_context_are_preserved(self):
        name = QualifiedName.parse('sales.Customer')
        element: SemanticElement = TestTypeDefinition(ID, name, CONTEXT)
        identity, preserved_name, context = read_definition(element)
        self.assertIs(identity, ID)
        self.assertIs(preserved_name, name)
        self.assertIs(context, CONTEXT)
        self.assertEqual(preserved_name.namespace.value, 'sales')

    def test_read_only_property_types_are_existing_primitives(self):
        expected = {'id': SemanticElementId, 'qualified_name': QualifiedName, 'context': SemanticContextRef}
        for name, value_type in expected.items():
            property_contract = getattr(SemanticElement, name)
            self.assertIsInstance(property_contract, property)
            self.assertIsNone(property_contract.fset)
            self.assertIs(get_type_hints(property_contract.fget)['return'], value_type)
        self.assertIs(get_type_hints(read_definition)['element'], SemanticElement)

    def test_fixture_construction_rejects_raw_types_and_absent_context(self):
        for cls in (TestTypeDefinition, TestActionDefinition):
            for values in ((str(ID), QualifiedName.parse('sales.Customer'), CONTEXT), (ID, 'sales.Customer', CONTEXT), (ID, QualifiedName.parse('sales.Customer'), str(CONTEXT)), (ID, QualifiedName.parse('sales.Customer'), None)):
                with self.subTest(cls=cls, values=values), self.assertRaises(TypeError):
                    cls(*values)

    def test_immutable_test_snapshot(self):
        element = TestTypeDefinition(ID, QualifiedName.parse('sales.Customer'), CONTEXT)
        for field, value in (('id', CONTEXT.context_id), ('qualified_name', QualifiedName.parse('sales.Client')), ('context', OTHER_CONTEXT)):
            with self.assertRaises(FrozenInstanceError):
                setattr(element, field, value)

    def test_rename_preserves_identity_without_equating_snapshot_fields(self):
        original = TestTypeDefinition(ID, QualifiedName.parse('sales.Customer'), CONTEXT)
        renamed = replace(original, qualified_name=QualifiedName.parse('sales.Client'))
        self.assertEqual(original.id, renamed.id)
        self.assertNotEqual(original.qualified_name, renamed.qualified_name)
        self.assertNotEqual(original, renamed)  # Fixture snapshot equality, not a root requirement.
        self.assertEqual(str(original.qualified_name), 'sales.Customer')

    def test_context_move_is_independent_of_identity_and_name(self):
        original = TestTypeDefinition(ID, QualifiedName.parse('sales.Customer'), CONTEXT)
        moved = replace(original, context=OTHER_CONTEXT)
        self.assertEqual(original.id, moved.id)
        self.assertEqual(original.qualified_name, moved.qualified_name)
        self.assertNotEqual(original.context, moved.context)

    def test_context_is_explicit_not_derived_from_namespace(self):
        name = QualifiedName.parse('sales.Customer')
        a = TestTypeDefinition(ID, name, CONTEXT)
        b = TestTypeDefinition(ID, name, OTHER_CONTEXT)
        self.assertEqual(a.qualified_name.namespace, b.qualified_name.namespace)
        self.assertNotEqual(a.context, b.context)
        c = TestActionDefinition(ID, QualifiedName.parse('operations.SubmitOrder'), CONTEXT)
        self.assertEqual(a.context, c.context)
        self.assertNotEqual(a.qualified_name.namespace, c.qualified_name.namespace)

    def test_root_has_no_generic_production_instance(self):
        with self.assertRaises(TypeError):
            SemanticElement()

    def test_protocol_does_not_claim_runtime_type_validation(self):
        element = TestTypeDefinition(ID, QualifiedName.parse('sales.Customer'), CONTEXT)
        with self.assertRaises(TypeError):
            isinstance(element, SemanticElement)

    def test_fixture_snapshot_equality_does_not_force_cross_type_identity_equality(self):
        type_definition = TestTypeDefinition(ID, QualifiedName.parse('sales.Customer'), CONTEXT)
        action_definition = TestActionDefinition(ID, QualifiedName.parse('sales.SubmitOrder'), CONTEXT)
        self.assertEqual(type_definition.id, action_definition.id)
        self.assertNotEqual(type_definition, action_definition)

    def test_demo(self):
        for fixture, name in ((TestTypeDefinition, 'sales.Customer'), (TestActionDefinition, 'sales.SubmitOrder')):
            element: SemanticElement = fixture(ID, QualifiedName.parse(name), CONTEXT)
            actual = read_definition(element)
            self.assertEqual(actual[0], ID)
            self.assertEqual(str(actual[1]), name)
            self.assertEqual(actual[2], CONTEXT)
