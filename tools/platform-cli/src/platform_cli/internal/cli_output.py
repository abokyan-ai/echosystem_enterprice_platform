"""Command data and diagnostics render separately from operational lifecycle logs."""
from dataclasses import asdict
import json
from platform_cli.public import CLI_VERSION, OUTPUT_SCHEMA_VERSION


class Output:
    def __init__(self, stdout, stderr, mode="human", quiet=False, verbose=False):
        self.stdout, self.stderr = stdout, stderr
        self.mode, self.quiet, self.verbose = mode, quiet, verbose

    def result(self, result):
        if self.mode == "json":
            payload = {**result.data, "schema_version": OUTPUT_SCHEMA_VERSION, "cli_version": CLI_VERSION, "command": result.command, "exit_code": result.exit_code, "diagnostics": [asdict(d) for d in result.diagnostics]}
            print(json.dumps(payload, sort_keys=True), file=self.stdout, flush=True)
        elif not self.quiet:
            self.human(result)
        if self.mode == "human":
            if result.command == "doctor" and result.exit_code:
                print("Doctor failed", file=self.stderr)
        self.diagnostics(result.diagnostics, result.command, result.exit_code)

    def human(self, result):
        data = result.data
        if result.command == "version":
            print(f"platform CLI {data['version']}", file=self.stdout)
        elif result.command == "doctor":
            print("Platform Doctor", file=self.stdout)
            for check in data["checks"]:
                print(f"{check['status']}  {check['name']}", file=self.stdout)
            print("Doctor OK" if result.exit_code == 0 else "Doctor failed", file=self.stdout)
            print(f"Status: {data['status'].upper()}", file=self.stdout)
        elif "health" in data:
            health = data["health"]
            print(f"Platform {health['status']}: state={health['state']}; profile={data['profile']}; scope={data['scope']}", file=self.stdout)
            for module in health["modules"]:
                print(f"  {module['id']}  {module['status']}", file=self.stdout)
            if result.command == "run" and not data.get("once"):
                print("Press Ctrl+C to stop.", file=self.stdout)
        elif "modules" in data:
            print("Modules (local inspection; not started)", file=self.stdout)
            for module in data["modules"]:
                print(f"  {module['id']}  {module['status']}  requires: {', '.join(module['dependencies']) or '-'}", file=self.stdout)
            if not data["modules"]:
                print("  No modules enabled", file=self.stdout)
        self.stdout.flush()

    def diagnostics(self, diagnostics, command=None, exit_code=1):
        if not diagnostics:
            return
        if self.mode == "json":
            print(json.dumps({"schema_version": OUTPUT_SCHEMA_VERSION, "cli_version": CLI_VERSION, "command": command, "exit_code": exit_code, "diagnostics": [asdict(d) for d in diagnostics]}, sort_keys=True), file=self.stderr)
        else:
            for diagnostic in diagnostics:
                print(f"{diagnostic.code} [{diagnostic.severity}] {diagnostic.message}", file=self.stderr)
                for key, value in diagnostic.context.items():
                    print(f"  {key}: {value}", file=self.stderr)
                print(f"  Suggestion: {diagnostic.suggestion}", file=self.stderr)

    def event(self, event, module=None):
        if self.quiet or self.mode == "json" and not self.verbose:
            return
        if self.verbose or event.startswith("platform "):
            print(event + (f": {module}" if module else ""), file=self.stderr, flush=True)
