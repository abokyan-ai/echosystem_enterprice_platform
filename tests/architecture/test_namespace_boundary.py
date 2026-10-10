import unittest
from pathlib import Path
from architecture_fitness.discovery import discover
from architecture_fitness.engine import execute
from semantic_kernel.public import Namespace, NamespaceError

ROOT = Path(__file__).resolve().parents[2]


class NamespaceBoundaryTests(unittest.TestCase):
    def test_namespace_public_contract_is_kernel_owned(self):
        self.assertEqual(Namespace.__module__, 'semantic_kernel.public')
        self.assertEqual(NamespaceError.__module__, 'semantic_kernel.public')

    def test_namespace_ownership_and_existing_neutrality_rules(self):
        model = discover(ROOT)
        report = execute(model, rule_ids=('ARCH-SK-NS-001', 'ARCH-SK-002', 'ARCH-SK-003'))
        self.assertEqual(report['summary']['status'], 'HEALTHY')
        self.assertEqual(model.graph('observed')['semantic-kernel'], set())
