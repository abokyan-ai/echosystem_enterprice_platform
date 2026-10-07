import unittest
from architecture_fitness.discovery import discover
from architecture_fitness.engine import execute
from pathlib import Path
import semantic_kernel.public as public
from semantic_kernel.public import SemanticElementId

ROOT = Path(__file__).resolve().parents[2]


class SemanticIdentityBoundaryTests(unittest.TestCase):
    def test_public_identity_is_owned_by_existing_kernel(self):
        self.assertEqual(SemanticElementId.__module__, "semantic_kernel.public")
        self.assertEqual(set(public.__all__), {"MODULE_NAME", "SemanticElementId", "SemanticElementIdError"})

    def test_kernel_has_only_foundational_imports_and_no_module_dependencies(self):
        model = discover(ROOT)
        kernel = next(module for module in model.modules if module.id == "semantic-kernel")
        self.assertEqual(kernel.metadata["allowed_dependencies"], [])
        self.assertEqual(model.graph("observed")[kernel.id], set())
        imports = {name.split(".")[0] for source in model.sources if source.owner == kernel.id for name, line in source.targets}
        self.assertEqual(imports, {"dataclasses", "re"})
        self.assertEqual(execute(model, rule_ids=("ARCH-SK-001", "ARCH-SK-002", "ARCH-SK-003"))["summary"]["status"], "HEALTHY")
