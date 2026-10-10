import json
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


class DependencyCommandTests(unittest.TestCase):
    def test_root_json_graph_is_machine_readable(self):
        result = subprocess.run([sys.executable, "scripts/dev.py", "dependencies:json"], cwd=ROOT, text=True, capture_output=True)
        self.assertEqual(result.returncode, 0, result.stderr)
        report = json.loads(result.stdout)
        self.assertEqual(len(report["modules"]), 9)
        self.assertEqual(report["violations"], [])
        self.assertEqual(report["cycle_count"], 0)

    def test_root_validation_runs_real_repository(self):
        result = subprocess.run([sys.executable, "scripts/dev.py", "check:architecture"], cwd=ROOT, text=True, capture_output=True)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("0 dependency violations", result.stdout)
