import json
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


class FitnessCommandTests(unittest.TestCase):
    def command(self, *options):
        return subprocess.run([sys.executable, "scripts/dev.py", "fitness:json", *options], cwd=ROOT, capture_output=True, text=True)

    def test_full_report_and_specific_rule(self):
        for options, count in (((), 37), (("--rule", "ARCH-FIT-DEP-001"), 1)):
            result = self.command(*options)
            self.assertEqual(result.returncode, 0, result.stderr)
            report = json.loads(result.stdout)
            self.assertEqual(report["summary"]["rules_executed"], count)
            self.assertEqual(report["summary"]["status"], "HEALTHY")
            self.assertEqual(report["discovery"]["scan_passes"], 1)

    def test_category_filter(self):
        result = self.command("--category", "public-api")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertTrue(all(r["category"] == "public-api" for r in json.loads(result.stdout)["rules"]))

    def test_unknown_rule_fails_with_json_report(self):
        result = self.command("--rule", "ARCH-UNKNOWN-001")
        self.assertNotEqual(result.returncode, 0)
        report = json.loads(result.stdout)
        self.assertEqual(report["summary"]["status"], "FAILED")
        self.assertEqual(report["violations"][0]["rule_id"], "ARCH-CONFIG-001")
        self.assertNotIn("Traceback", result.stderr)
