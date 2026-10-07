# ARC-04: Platform bootstrap

## Ownership and composition

Before ARC-04 the executable CLI exposed only doctor and static public identity imports. No host, lifecycle, configuration binding or activation registry existed.

`tools/platform-cli/src/platform_cli/internal/composition.py` is the local executable composition root. It registers five explicit public core identities as **boundary markers**, with no semantic, compiler or runtime behavior. `BootstrapBuilder` owns a local registration dictionary and constructs `LocalPlatformHost`; no process-global registry, package discovery or service locator exists. `add_module` and `add_adapter` distinguish registration intent. Actual infrastructure adapters remain future work.

`platform/bootstrap/contracts` is a small independently owned contract boundary, not a common utility library. It contains `PlatformModule`, `PlatformHost`, `ModuleRegistration`, configuration, health and diagnostics. Core source modules do not import the concrete host; implementation/configuration I/O stays in CLI. Factories receive only declared module instances and their own settings. Factories must not allocate resources; resource ownership begins in `start` and ends in `stop`. Modules must make `stop` safe after partial startup and retry cleanup after a failure.

## Activation and configuration

`architecture.json` remains the single module metadata source. `allowed_dependencies` governs source architecture; **separate** `activation_dependencies` govern the local activation plan. The lists currently mirror foundation dependencies, but one is never inferred from the other. Pure registrations/fakes can define activation graphs without repository discovery.

Unknown, duplicate, missing/disabled dependencies and cycles fail before construction or startup. Sorted traversal supplies cycle paths; a min-heap topological sort supplies a stable order, independent of registration ordering. Shutdown reverses the actual activation order.

Configuration precedence is defaults < JSON file < environment < CLI overrides. `profile` is development/test/production; profiles are labels, not deployment/security guarantees. CLI defaults to `config/development.json`; `--config config/test.json` selects an empty test activation plan. `--profile test` alone changes the label, not enabled modules. `enabled_modules: null` enables all explicitly registered modules; `[]` enables none. Selecting a dependent module does not silently enable prerequisites.

Environment variables: `PLATFORM_PROFILE`, `PLATFORM_MODULES` (comma-separated, empty means none), `PLATFORM_MODULE_SETTINGS` (JSON object). CLI supports `--profile`, `--modules` and `--config`. Module settings merge by module/key with higher precedence replacing values. All selected module settings are validated before **any** factory runs. Unknown fields, duplicate module IDs, unknown/disabled module settings and unsupported settings fail early. Configuration values and exception text from modules are never included in bootstrap diagnostics or lifecycle logs.

## Lifecycle and failures

The lifecycle is BUILT -> STARTING -> RUNNING -> STOPPING -> STOPPED -> DISPOSED. Failed starts/stops enter FAILED. Repeated start while RUNNING, stop while STOPPED and dispose while DISPOSED are no-ops. Restarting a stopped/failed/disposed host is rejected; build a new host. Transition reentry is rejected. The host is synchronous and is not a concurrent lifecycle manager.

Startup failure first cleans the partially started failing module, then successfully started modules in reverse order; later modules never start. Cleanup continues after individual failures and returns the original startup diagnostic plus cleanup diagnostics. Failed cleanup resources remain tracked for explicit retry through stop/dispose. Health remains unhealthy after a recorded lifecycle failure; disposal does not erase diagnostic history.

`platform run` installs SIGINT/SIGTERM handlers, reports startup health, waits for a termination request and disposes in a finally block. Previous handlers are restored. `--once` performs startup/report/shutdown for smoke checks; JSON mode puts the health report on stdout and lifecycle events on stderr. The report describes health **before** shutdown; a later shutdown failure still yields a nonzero exit. SIGTERM during startup requests shutdown after the synchronous start call completes. Hanging module callbacks cannot be forcibly cancelled by this baseline.

## Health, diagnostics and test host

Health is healthy/degraded/unhealthy with host state, registered/started/failed module IDs and per-module status. Startup duration and per-module timings are collected; they do not affect ordering. Event sink failure degrades health, while module health failure yields unhealthy. Structured diagnostics use BOOT-CONFIG-001, BOOT-MOD-001, BOOT-MOD-002, BOOT-CYCLE-001, BOOT-START-001, BOOT-STOP-001, BOOT-STATE-001 and BOOT-LOG-001. Messages name module/dependency/setting/path without logging settings or module exception text.

`tests/bootstrap_support.py` supplies TestHost and resource-owning fakes. It uses the same builder as production, with explicit replacement registrations and independent instances for each test. The test support path is added only for the root test command; production sources cannot import test helpers. Test override factories have the same lifecycle and side-effect requirements as real factories.

## Architecture fitness and tests

The complete registry now has 34 rules. ARCH-BOOT-CONTRACT-001 protects the independent hosting contract zone. ARCH-BOOT-002 prohibits core/hosting contract adapter coupling, preserving adapter selection in outer composition boundaries. ARCH-BOOT-003 prohibits platform dependence on concrete bootstrap/tooling. ARCH-BOOT-004 prohibits platform dependence on applications. The three direction invariants inspect transitive declared and observed graphs and survive a relaxed allowlist. They do not claim to identify every factory call outside a composition root.

ARCH-BOOT-001 (general service-locator detection) is deferred: reliable semantic detection is not available in the current AST analyzer. Explicit injection, local instance ownership and fake override tests verify this implementation without pretending to enforce all possible locator patterns.

BOOT-TEST-001..010 cover empty, single, ordering, missing dependency, duplicate registration, cycle path, failed startup cleanup, configuration precedence, explicit overrides and determinism. Additional cases cover partial cleanup retry, shutdown aggregation, idempotency, illegal restart, invalid config before factories, owned dependency injection, health, adapter registration and event sink failure. Integration covers five markers, empty activation, doctor validation, fail-fast CLI and graceful SIGTERM. Architecture fixtures prove forbidden bootstrap edges fail.

## Commands and scope

Use `python3 scripts/dev.py build`, `test`, `test:architecture`, `doctor`, and `run --once`. `python3 scripts/dev.py run` starts the persistent local host; `run --once --config config/test.json --format json` runs an empty test host. `python -m platform_cli doctor/run` is the direct executable form when registered source paths are on PYTHONPATH.

No database, Django endpoint, Angular UI, semantic primitive, compiler feature or runtime business service is introduced. The selected Angular/PrimeNG, Django/DRF and mock-data architecture remains unchanged. Dynamic plugins, async/distributed startup, production secrets, cancellation/timeouts, orchestration and real resource adapters are deferred. Next: ARC-05 Platform CLI Skeleton, then SK-01 SemanticElementId.
