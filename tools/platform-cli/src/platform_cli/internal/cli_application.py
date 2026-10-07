"""CLI adapter entry: parse, compose explicit services, dispatch, render diagnostics."""
import argparse
from pathlib import Path
import sys
import threading
from platform_cli.public import CLI_VERSION, CliDiagnostic, CliError, CommandResult, PlatformRequest
from platform_cli.internal.cli_context import CliExecutionContext
from platform_cli.internal.cli_diagnostics import classify
from platform_cli.internal.cli_output import Output
from platform_cli.internal.cli_registry import default_registry
from platform_cli.internal.cli_services import LocalCliServices


class Parser(argparse.ArgumentParser):
    def __init__(self, *args, stdout=None, stderr=None, **kwargs):
        self.stdout, self.stderr = stdout or sys.stdout, stderr or sys.stderr
        super().__init__(*args, **kwargs)

    def print_help(self, file=None):
        super().print_help(file or self.stdout)

    def add_subparsers(self, **kwargs):
        kwargs.setdefault("parser_class", lambda **kw: Parser(stdout=self.stdout, stderr=self.stderr, **kw))
        return super().add_subparsers(**kwargs)

    def error(self, message):
        raise CliError(2, CliDiagnostic("CLI-INPUT-001", message, suggestion="Run platform --help or platform <command> --help."))


def global_options(parser):
    suppress = argparse.SUPPRESS
    parser.add_argument("--root", type=Path, default=suppress, help="Repository root; defaults to current working directory")
    parser.add_argument("--config", type=Path, default=suppress, help="Configuration JSON path, relative to --root")
    parser.add_argument("--profile", choices=("development", "test", "production"), default=suppress, help="Configuration profile override")
    parser.add_argument("--modules", default=suppress, help="Enabled module IDs, comma separated; empty means none")
    parser.add_argument("--output", choices=("human", "json"), default=suppress, help="Result format (default: human)")
    parser.add_argument("--format", choices=("text", "json"), default=suppress, help="ARC-04 compatibility alias for --output")
    verbosity = parser.add_mutually_exclusive_group()
    verbosity.add_argument("--verbose", action="store_true", default=suppress, help="Include lifecycle events and unexpected exception type")
    verbosity.add_argument("--quiet", action="store_true", default=suppress, help="Suppress successful human output and operational logs; JSON and errors remain")
    parser.add_argument("--version", action="store_true", default=suppress, help="Show CLI version without loading configuration")


def requested_output(argv):
    # Early parse diagnostics must be machine readable even if argument parsing fails.
    for index, value in enumerate(argv):
        if value == "--output=json" or value == "--format=json" or value in {"--output", "--format"} and index + 1 < len(argv) and argv[index + 1] == "json":
            return "json"
    return "human"


def main(argv=None, *, services=None, stdout=None, stderr=None, cancellation=None, registry=None):
    argv = list(sys.argv[1:] if argv is None else argv)
    stdout, stderr = stdout or sys.stdout, stderr or sys.stderr
    output = Output(stdout, stderr, requested_output(argv))
    try:
        # Child parsers inherit invocation streams through a parser factory.
        parser = Parser(prog="platform", description="Model-Driven Enterprise Ecosystem Platform: local developer CLI", epilog="Examples: platform doctor; platform modules --output json; platform run --once; platform --config config/test.json health", stdout=stdout, stderr=stderr)
        global_options(parser)
        (registry or default_registry()).attach(parser, global_options)
        args = parser.parse_args(argv)
        if getattr(args, "verbose", False) and getattr(args, "quiet", False):
            parser.error("--verbose and --quiet cannot be combined")
        mode = getattr(args, "output", None)
        legacy = getattr(args, "format", None)
        if mode and legacy and mode != ("human" if legacy == "text" else "json"):
            parser.error("--output and --format specify conflicting formats")
        output = Output(stdout, stderr, mode or ("human" if legacy in {None, "text"} else "json"), getattr(args, "quiet", False), getattr(args, "verbose", False))
        if getattr(args, "version", False):
            output.result(CommandResult("version", {"version": CLI_VERSION}))
            return 0
        if not hasattr(args, "definition"):
            parser.error("A command is required")
        enabled = tuple(m.strip() for m in args.modules.split(",") if m.strip()) if hasattr(args, "modules") else None
        root = getattr(args, "root", Path.cwd()).resolve()
        request = PlatformRequest(root, getattr(args, "config", None), getattr(args, "profile", None), enabled)
        context = CliExecutionContext(request, services if services is not None else LocalCliServices(), output, cancellation if cancellation is not None else threading.Event(), Path.cwd())
        result = args.definition.handler(context, args)
        if isinstance(result, CommandResult):
            output.result(result)
            return result.exit_code
        return int(result or 0)
    except SystemExit as error:
        return int(error.code or 0)
    except KeyboardInterrupt:
        output.diagnostics((CliDiagnostic("CLI-CANCEL-001", "Command interrupted", suggestion="Retry when ready."),), exit_code=1)
        return 1
    except Exception as error:
        failure = classify(error)
        output.diagnostics(failure.diagnostics, exit_code=failure.exit_code)
        if output.verbose:
            # Exception type only: raw tracebacks/exception text can reveal settings or secrets.
            print(f"Debug exception type: {type(error).__name__}", file=stderr)
        return failure.exit_code
