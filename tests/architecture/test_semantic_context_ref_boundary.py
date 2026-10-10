import unittest
from pathlib import Path
from architecture_fitness.discovery import discover
from architecture_fitness.engine import execute
from semantic_kernel.public import SemanticContextRef, SemanticContextRefError, SemanticElementId

ROOT = Path(__file__).resolve().parents[2]


class SemanticContextRefBoundaryTests(unittest.TestCase):
    def test_context_reference_is_owned_by_kernel_and_wraps_identity_only(self):
        self.assertEqual(SemanticContextRef.__module__, 'semantic_kernel.public')
        self.assertEqual(SemanticContextRefError.__module__, 'semantic_kernel.public')
        self.assertEqual(SemanticContextRef.__annotations__, {'context_id': SemanticElementId})

    def test_ownership_and_existing_kernel_dependency_rules(self):
        model = discover(ROOT)
        report = execute(model, rule_ids=('ARCH-SK-CTX-001', 'ARCH-SK-002', 'ARCH-SK-003'))
        self.assertEqual(report['summary']['status'], 'HEALTHY')
        self.assertEqual(model.graph('observed')['semantic-kernel'], set())
