from unittest import TestCase
from compiled_contracts.public import MODULE_NAME


class PublicBoundaryTest(TestCase):
    def test_module_registration(self):
        self.assertEqual(MODULE_NAME, "compiled-contracts")
