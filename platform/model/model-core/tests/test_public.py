from unittest import TestCase
from model_core.public import MODULE_NAME


class PublicBoundaryTest(TestCase):
    def test_module_registration(self):
        self.assertEqual(MODULE_NAME, "model-core")
