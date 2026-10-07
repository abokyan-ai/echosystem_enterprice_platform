from unittest import TestCase
from bootstrap_contracts.public import MODULE_NAME, ModuleRegistration, BootstrapError


class HostingContractsTest(TestCase):
    def test_module_registration(self):
        self.assertEqual(MODULE_NAME, "bootstrap-contracts")

    def test_invalid_module_identity_and_factory(self):
        for identity in ("", "../module", "bad name"):
            with self.assertRaises(BootstrapError):
                ModuleRegistration(identity, lambda dependencies, settings: None)
