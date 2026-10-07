from unittest import TestCase
from semantic_kernel.public import MODULE_NAME


class PublicBoundaryTest(TestCase):
    def test_module_registration(self):
        self.assertEqual(MODULE_NAME, "semantic-kernel")
