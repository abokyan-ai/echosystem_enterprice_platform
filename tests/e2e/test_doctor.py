import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


class DoctorTests(unittest.TestCase):
    def test_root_command(self):
        result = subprocess.run([sys.executable, "scripts/dev.py", "doctor"], cwd=ROOT, capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("Doctor OK", result.stdout)

    def test_missing_configuration_has_actionable_error(self):
        with tempfile.TemporaryDirectory() as directory:
            result = subprocess.run([sys.executable, "-m", "platform_cli", "doctor", "--root", directory], cwd=ROOT, capture_output=True, text=True, env=os.environ.copy())
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("Doctor failed", result.stderr)
        self.assertNotIn("Traceback", result.stderr)
