from unittest import TestCase
from compiler_core.public import MODULE_NAME


class PublicBoundaryTest(TestCase):
    def test_module_registration(self):
        self.assertEqual(MODULE_NAME, "compiler-core")
