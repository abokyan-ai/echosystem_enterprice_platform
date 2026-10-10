from enum import Enum
from pathlib import Path
from typing import get_type_hints
import unittest
from architecture_fitness.discovery import discover
from architecture_fitness.engine import execute
from semantic_kernel.public import SemanticElement, SemanticElementKind

ROOT = Path(__file__).resolve().parents[2]


class SemanticElementKindBoundaryTests(unittest.TestCase):
    def test_public_kind_is_kernel_value_not_enum_and_root_is_typed(self):
        self.assertEqual(SemanticElementKind.__module__, 'semantic_kernel.public')
        self.assertFalse(issubclass(SemanticElementKind, Enum))
        self.assertIs(get_type_hints(SemanticElement.kind.fget)['return'], SemanticElementKind)
        self.assertIsNone(SemanticElement.kind.fset)

    def test_existing_independence_and_public_import_rules_pass(self):
        model = discover(ROOT)
        self.assertEqual(execute(model, rule_ids=('ARCH-SK-002', 'ARCH-SK-003'))['summary']['status'], 'HEALTHY')
        self.assertEqual(model.graph('observed')['semantic-kernel'], set())
