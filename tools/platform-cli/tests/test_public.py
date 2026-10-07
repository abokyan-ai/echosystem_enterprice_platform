from unittest import TestCase
from platform_cli.public import MODULE_NAME


class PublicBoundaryTest(TestCase):
    def test_module_registration(self):
        self.assertEqual(MODULE_NAME, "platform-cli")
