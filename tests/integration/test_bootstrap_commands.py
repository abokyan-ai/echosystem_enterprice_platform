import json
import os
import signal
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


class BootstrapCommandTests(unittest.TestCase):
    def command(self, *options):
        environment = {k: v for k, v in os.environ.items() if not k.startswith("PLATFORM_")}
        return subprocess.run([sys.executable, "scripts/dev.py", *options], cwd=ROOT, env=environment, capture_output=True, text=True, timeout=20)

    def test_default_run_and_reverse_shutdown(self):
        result = self.command("run", "--once", "--format", "json")
        self.assertEqual(result.returncode, 0, result.stderr)
        report = json.loads(result.stdout)
        self.assertEqual(report["health"]["status"], "healthy")
        self.assertEqual(len(report["startup_order"]), 5)
        stops = [line.split(": ")[1] for line in result.stderr.splitlines() if line.startswith("module stopping:")]
        self.assertEqual(stops, list(reversed(report["startup_order"])))

    def test_empty_test_host_and_doctor(self):
        result = self.command("run", "--once", "--config", "config/test.json", "--format", "json")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(json.loads(result.stdout)["startup_order"], [])
        result = self.command("doctor", "--config", "config/test.json")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("Doctor OK", result.stdout)

    def test_missing_dependency_and_invalid_config_early_failure(self):
        for options, code in ((("--modules", "runtime-core"), "BOOT-MOD-002"), (("--config", "missing.json"), "BOOT-CONFIG-001")):
            result = self.command("run", "--once", *options)
            self.assertNotEqual(result.returncode, 0)
            self.assertIn(code, result.stderr)
            self.assertNotIn("module starting", result.stderr)
            self.assertNotIn("Traceback", result.stderr)

    @unittest.skipUnless(os.name == "posix", "POSIX signal integration")
    def test_sigterm_graceful_cleanup(self):
        # Verify the development wrapper forwards termination to the actual host.
        process = subprocess.Popen([sys.executable, "scripts/dev.py", "run", "--modules", "", "--format", "json"], cwd=ROOT, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        try:
            report = json.loads(process.stdout.readline())
            self.assertEqual(report["health"]["status"], "healthy")
            process.send_signal(signal.SIGTERM)
            stdout, stderr = process.communicate(timeout=10)
            self.assertEqual(process.returncode, 0, stderr)
            self.assertIn("platform stopped", stderr)
        finally:
            if process.poll() is None:
                process.kill()
                process.communicate()
