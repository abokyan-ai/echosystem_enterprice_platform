"""No feature contract tests: validate the actual public registration boundary."""
import importlib
import unittest
from pathlib import Path
from check_architecture import load_manifest

ROOT = Path(__file__).resolve().parents[2]


class PublicSurfaceTests(unittest.TestCase):
    def test_registered_public_apis_import_and_identify_their_owner(self):
        for module in load_manifest(ROOT)["modules"]:
            with self.subTest(module=module["name"]):
                public = importlib.import_module(module["public_api"][0])
                self.assertEqual(public.MODULE_NAME, module["name"])
                self.assertFalse(hasattr(public, "ConcreteRepository"))
