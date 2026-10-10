import unittest
from pathlib import Path
from architecture_fitness.discovery import discover
from architecture_fitness.engine import execute
from semantic_kernel.public import Namespace, QualifiedName, QualifiedNameError

ROOT = Path(__file__).resolve().parents[2]


class QualifiedNameBoundaryTests(unittest.TestCase):
    def test_qualified_name_contract_is_owned_by_existing_kernel(self):
        self.assertEqual(QualifiedName.__module__, 'semantic_kernel.public')
        self.assertEqual(QualifiedNameError.__module__, 'semantic_kernel.public')
        self.assertIs(QualifiedName.__annotations__['namespace'], Namespace)

    def test_ownership_and_existing_dependency_neutrality_rules(self):
        model = discover(ROOT)
        report = execute(model, rule_ids=('ARCH-SK-QN-001', 'ARCH-SK-002', 'ARCH-SK-003'))
        self.assertEqual(report['summary']['status'], 'HEALTHY')
        self.assertEqual(model.graph('observed')['semantic-kernel'], set())
