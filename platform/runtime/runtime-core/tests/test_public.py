from unittest import TestCase
from runtime_core.public import MODULE_NAME


class PublicBoundaryTest(TestCase):
    def test_module_registration(self):
        self.assertEqual(MODULE_NAME, "runtime-core")
