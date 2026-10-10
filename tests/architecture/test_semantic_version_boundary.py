from dataclasses import fields
from pathlib import Path
from typing import get_type_hints
import unittest
from architecture_fitness.discovery import discover
from architecture_fitness.engine import execute
from semantic_kernel.public import SemanticVersion, ElementVersionRef, SemanticElementId, SemanticElement

ROOT = Path(__file__).resolve().parents[2]


class SemanticVersionBoundaryTests(unittest.TestCase):
    def test_primitives_are_kernel_owned_and_existing_dependency_rules_pass(self):
        for primitive in (SemanticVersion, ElementVersionRef):
            self.assertEqual(primitive.__module__, 'semantic_kernel.public')
        model = discover(ROOT)
        self.assertEqual(model.graph('observed')['semantic-kernel'], set())
        self.assertEqual(execute(model, rule_ids=('ARCH-SK-002', 'ARCH-SK-003'))['summary']['status'], 'HEALTHY')

    def test_reference_contains_only_identity_and_exact_version(self):
        self.assertEqual({field.name: field.type for field in fields(ElementVersionRef)}, {'element_id': SemanticElementId, 'version': SemanticVersion})
        self.assertEqual({field.name: field.type for field in fields(SemanticVersion)}, {'major': int, 'minor': int, 'patch': int})
        self.assertIs(get_type_hints(SemanticElement.version.fget)['return'], SemanticVersion)
        self.assertIsNone(SemanticElement.version.fset)

    def test_primitives_expose_no_resolution_or_compatibility_behavior(self):
        for primitive in (SemanticVersion, ElementVersionRef):
            for name in ('resolve', 'load', 'latest', 'get_definition', 'is_compatible_with', 'next_major', 'next_minor', 'next_patch'):
                self.assertFalse(hasattr(primitive, name))
