# Platform CLI (ARC-05)

The CLI is a local developer adapter. It composes existing public contracts and calls ARC-04 bootstrap; it implements no semantic model, compiler, runtime business feature, persistence or remote management.

## Invocation and installation

Python 3.11+ is required. No third-party dependency installation is needed. From a source checkout:

```bash
python3 scripts/dev.py install
./bin/platform --help
python3 scripts/platform.py --version
python3 scripts/dev.py cli modules --output json
```

To use the executable name directly on POSIX:

```bash
export PATH="$PWD/bin:$PATH"
platform --help
```

The source launcher replaces its process with `python -m platform_cli`, supplying registered source paths from the checkout. It preserves signals and exit codes. On systems without POSIX executable handling use `python scripts/platform.py`. Root `dev.py doctor/run/modules/health/version` are compatibility aliases; `dev.py cli` forwards arbitrary CLI arguments. Individual source modules do not change sys.path.

CLI version **0.1.0** is introduced explicitly for this CLI skeleton. No platform product version or commit identifier is fabricated.

## Global options

Options work before or after a command. A repeated scalar option uses its last value.

| Option | Behavior |
| --- | --- |
| `--help` | Root or command help; no configuration access |
| `--version` | CLI version; no configuration access |
| `--root PATH` | Inspected repository root, default current working directory |
| `--config PATH` | Bootstrap JSON, relative to root; default config/development.json |
| `--profile development\|test\|production` | Overrides the profile label, not module selection |
| `--modules IDS` | Comma-separated enabled IDs; an empty string enables none |
| `--output human\|json` | Command result format, default human |
| `--verbose` | Module lifecycle logs and unexpected exception type; no raw exception text/traceback |
| `--quiet` | Suppresses successful human output and logs; JSON results and errors remain |
| `--format text\|json` | Compatibility alias from ARC-04 |

Verbose/quiet and conflicting output/format values are rejected, including across the root and command option positions. Configuration uses the existing ARC-04 pipeline: defaults < JSON file < PLATFORM_* environment < CLI. No second loader is introduced. Relative config paths resolve against root, while the invocation working directory is retained in execution context.

## Commands

| Command | Purpose / behavior | Command options | Exit behavior |
| --- | --- | --- | --- |
| `version` | Shows CLI version only | Global options | 0 |
| `doctor` | Independent read-only repository, configuration, architecture fitness and activation graph checks | Global options | 0 when all pass; failures use the policy below |
| `run` | Builds/starts ARC-04 host; waits for SIGINT/SIGTERM and disposes | `--once` performs start/report/dispose | 0 after clean healthy/degraded run; 1 for unhealthy health, 3/4 for config/bootstrap failures |
| `modules` | Builds graph without starting modules; shows enabled IDs, dependencies, kinds and built-state status | Global options | 0 for valid inspection, 3/4 for config/graph failures |
| `health` | Snapshot of a freshly built local host, without starting it | Global options | 0 for healthy/degraded inspection; 1 for unhealthy, 3/4 for config/graph failures |

`modules` and `health` inspect a **new local host**, not a separately running process. Existing boundary markers therefore report built/degraded/unstarted. A successful inspection returns 0; degraded is not a failed command. The default graph contains five enabled foundation markers, not seven runnable services. Hosting contracts and CLI are source modules, not activated business modules. `config/test.json` selects an empty host.

```bash
platform doctor
platform doctor --output json
platform modules --output json
platform --config config/test.json health --output json
platform run --once --output json
platform run --verbose
platform run --once --modules runtime-core # fails: prerequisites not enabled
```

Doctor continues independent checks after failure; the graph check is skipped when configuration cannot bind. If multiple categories fail, priority is configuration (3), architecture (5), bootstrap (4), then general (1). It does not repair files. Its architecture adapter consumes the ARC-03 public CLI JSON interface and never imports fitness internals.

## Output and diagnostics

Human output is informational, without colors or terminal control sequences. Its whitespace is not an API. Experimental JSON results have `schema_version: 1`, `cli_version`, `command`, `exit_code`, `diagnostics` and command data. Reserved envelope fields are owned by the renderer. Modules include `dependencies`, `kind`, `status` and `started`; health includes the actual ARC-04 snapshot plus `scope` and `profile`. Stable ordering follows the bootstrap graph and sorted module identities; measured durations are naturally variable.

Successful results and structured inspection reports go to stdout. Diagnostics/errors go to stderr; JSON doctor/health failures include diagnostics in both the result envelope and the stderr diagnostic envelope. Failures before a command result exists produce only stderr. Quiet preserves machine-readable data and errors.

Operational lifecycle events go to stderr, separately from results. Default JSON mode suppresses operational logs; verbose JSON mode includes lifecycle text on stderr. Never parse verbose stderr as one JSON document. Stdout remains a single valid JSON result.

Persistent `run` emits one startup snapshot before waiting; its exit code and stderr determine the final shutdown outcome. `--once` emits its snapshot only after successful cleanup, so a failed shutdown cannot emit a success result. Both modes report the startup health state; they do not claim that the host remains running after command exit. SIGINT/SIGTERM request graceful shutdown; signal handlers are restored and cleanup errors aggregate. Synchronous callbacks cannot be forcibly cancelled if they hang, as documented in ARC-04.

Diagnostics reuse bootstrap codes and add severity, module/dependency/setting/path context and a suggestion. CLI-owned errors use CLI-INPUT-001, CLI-REPO-001, CLI-ARCH-001, CLI-INTERNAL-001, CLI-HEALTH-001, CLI-CANCEL-001 and CLI-LAUNCH-001. Raw module/config exception text and tracebacks are never rendered. Verbose reveals exception type only.

## Exit codes

| Code | Meaning |
| --- | --- |
| 0 | Successful command or clean requested shutdown |
| 1 | General/internal failure or unhealthy health |
| 2 | Invalid command/arguments/options |
| 3 | Configuration/launcher failure |
| 4 | Bootstrap graph, startup, shutdown or interrupted-start failure |
| 5 | Architecture validation/interface failure |

A Ctrl+C request during a persistent run exits 0 when cleanup succeeds. An interruption thrown by a module during startup is diagnosed as failure (4). All launcher/compatibility aliases preserve these exit codes.

## Command architecture and extension

The executable entry point delegates to `cli_application`. It sets up options, explicit services, context, output and diagnostics, then dispatches through the registered definition's handler. It has no per-command switch. `CommandRegistry` builds argparse subparsers from tuple paths, supports shared nested namespaces and rejects duplicate/leaf-prefix conflicts. No plugin discovery or placeholder namespace is created.

Handlers use `platform_cli.public.CliServices` and `bootstrap_contracts.public` contracts. Concrete `LocalCliServices` adapts existing bootstrap/configuration implementations in CLI internals; it is supplied at composition, never looked up globally. `CliExecutionContext` contains request, services, output, invocation directory and cancellation event. Platform core never depends on CLI.

To add a real command:

1. Define a small handler depending on explicit public capability contracts.
2. Return a `CommandResult`; keep domain behavior in its owning module.
3. Add a `CommandDefinition(("name",), help, handler, configure)` to explicit registration. Tuple paths such as `("architecture", "test")` add a nested command without changing root dispatch.
4. Add in-process tests injecting services and captured streams, plus relevant integration/JSON/error cases.
5. Document usage/help and run full architecture fitness.

`tests/cli_support.py` provides invocation/capture and fake service/host injection. It is a test-only module. The extension example is exercised in tests; no architecture/model/compiler placeholder command ships.

## Architecture rules and scope

ARCH-CLI-001 prohibits core-to-CLI/tooling transitive dependencies. ARCH-CLI-002 enforces CLI cross-module public imports. ARCH-CLI-003 rejects adapter internal imports from CLI. Existing ARCH-API/BOOT/TEST rules remain enforced. The complete registry has 37 rules.

ARCH-CLI-004 (general semantic/business implementation detection) is deferred: the analyzer cannot reliably infer business semantics from arbitrary Python. Small contract-based handlers and review/tests establish the current boundary without a false detection claim.

Remote/cloud/authentication, plugin commands, interactive shell, completion, compiler/model/artifact/app/package/tenant/agent commands and multi-workspace management remain deferred until real capabilities exist. Next implementation: SK-01 — SemanticElementId.
