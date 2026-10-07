import json
import os
from pathlib import Path
import signal
import shutil
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[2]


class CliIntegrationTests(unittest.TestCase):
    def invoke(self, *arguments, cwd=None, env=None):
        environment = {k: v for k, v in os.environ.items() if not k.startswith("PLATFORM_")}
        environment.update(env or {})
        return subprocess.run([sys.executable, str(ROOT / "scripts/platform_cli_launcher.py"), *arguments], cwd=cwd or ROOT, env=environment, text=True, capture_output=True, timeout=20)

    def test_help_and_version_executable(self):
        result = subprocess.run([str(ROOT / "bin/platform"), "--help"], cwd=ROOT, text=True, capture_output=True, timeout=20)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("Model-Driven", result.stdout)
        result = self.invoke("--version", "--output", "json")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(json.loads(result.stdout)["command"], "version")

    def test_doctor_is_structured_and_read_only(self):
        before = {path: path.read_bytes() for path in (ROOT / "architecture.json", ROOT / "architecture-policy.json", ROOT / "config/development.json")}
        result = self.invoke("doctor", "--output", "json")
        self.assertEqual(result.returncode, 0, result.stderr)
        report = json.loads(result.stdout)
        self.assertTrue(all(check["status"] == "PASS" for check in report["checks"]))
        self.assertEqual(result.stderr, "")
        for path, contents in before.items():
            self.assertEqual(path.read_bytes(), contents)

    def test_modules_metadata_and_unstarted_health(self):
        result = self.invoke("modules", "--output", "json")
        self.assertEqual(result.returncode, 0, result.stderr)
        report = json.loads(result.stdout)
        runtime = next(module for module in report["modules"] if module["id"] == "runtime-core")
        self.assertEqual(set(runtime["dependencies"]), {"semantic-kernel", "compiled-contracts"})
        self.assertFalse(runtime["started"])
        self.assertEqual(report["scope"], "local-inspection")
        result = self.invoke("health", "--output", "json")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(json.loads(result.stdout)["health"]["status"], "degraded")

    def test_working_directory_and_configuration_precedence(self):
        with tempfile.TemporaryDirectory() as directory:
            result = self.invoke("--root", str(ROOT), "--profile", "test", "modules", "--modules", "", "--output", "json", cwd=directory, env={"PLATFORM_PROFILE": "production", "PLATFORM_MODULES": "runtime-core"})
            self.assertEqual(result.returncode, 0, result.stderr)
            report = json.loads(result.stdout)
            self.assertEqual(report["profile"], "test")
            self.assertEqual(report["modules"], [])
            result = self.invoke("doctor", "--output", "json", cwd=directory)
            self.assertEqual(result.returncode, 3)
            self.assertEqual(json.loads(result.stdout)["status"], "unhealthy")
            self.assertEqual(json.loads(result.stderr)["exit_code"], 3)

    def test_invalid_input_config_and_activation_have_distinct_exits(self):
        for arguments, expected in ((("unknown",), 2), (("modules", "--config", "missing.json"), 3), (("run", "--once", "--modules", "runtime-core"), 4)):
            result = self.invoke("--output", "json", *arguments)
            self.assertEqual(result.returncode, expected, result.stderr)
            self.assertEqual(result.stdout, "")
            self.assertEqual(json.loads(result.stderr)["exit_code"], expected)
            self.assertNotIn("Traceback", result.stderr)
            wrapped = subprocess.run([sys.executable, "scripts/dev.py", "cli", "--output", "json", *arguments], cwd=ROOT, text=True, capture_output=True, timeout=20)
            self.assertEqual(wrapped.returncode, expected)

    def test_doctor_architecture_failure_exit_five(self):
        with tempfile.TemporaryDirectory(dir=ROOT / "build") as directory:
            root = Path(directory)
            for family in ("platform", "tools", "scripts", "docs", "config"):
                shutil.copytree(ROOT / family, root / family, ignore=shutil.ignore_patterns("__pycache__"))
            shutil.copy2(ROOT / "architecture.json", root / "architecture.json")
            policy = json.loads((ROOT / "architecture-policy.json").read_text())
            policy["zones"]["bootstrap-contracts"]["stdlib"].remove("re")
            (root / "architecture-policy.json").write_text(json.dumps(policy))
            result = self.invoke("doctor", "--root", str(root), "--output", "json")
            self.assertEqual(result.returncode, 5, result.stderr)
            checks = json.loads(result.stdout)["checks"]
            self.assertEqual([c["status"] for c in checks], ["PASS", "PASS", "FAIL", "PASS"])
            self.assertTrue(any(d["code"] == "ARCH-BOOT-CONTRACT-001" for d in json.loads(result.stderr)["diagnostics"]))

    @unittest.skipUnless(os.name == "posix", "POSIX signal integration")
    def test_sigint_direct_launcher_clean_shutdown(self):
        process = subprocess.Popen([sys.executable, str(ROOT / "scripts/platform_cli_launcher.py"), "run", "--modules", "", "--output", "json"], cwd=ROOT, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        try:
            report = json.loads(process.stdout.readline())
            self.assertEqual(report["health"]["status"], "healthy")
            process.send_signal(signal.SIGINT)
            out, err = process.communicate(timeout=10)
            self.assertEqual(process.returncode, 0, err)
            self.assertEqual(err, "")
        finally:
            if process.poll() is None:
                process.kill()
                process.communicate()


    def test_source_launcher_protects_standard_library_imports(self):
        from unittest.mock import patch
        import runpy
        with patch("os.execve") as execute, patch("sys.argv", ["platform", "--version"]):
            with self.assertRaises(SystemExit):
                runpy.run_path(str(ROOT / "scripts/platform_cli_launcher.py"), run_name="__main__")
        environment = execute.call_args.args[2]
        result = subprocess.run([sys.executable, "-c", "import platform, uuid; assert callable(platform.system); print(uuid.uuid4().version)"], cwd=ROOT, env=environment, text=True, capture_output=True, timeout=20)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(result.stdout.strip(), "4")
