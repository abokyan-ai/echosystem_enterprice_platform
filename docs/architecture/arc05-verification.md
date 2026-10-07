# ARC-05 verification

Local verification on Python 3.12.14, 2026-10-07:

| Executed command | Result |
| --- | --- |
| `python3 scripts/dev.py install` | Standard-library-only workspace ready |
| `python3 scripts/dev.py build` | Source syntax, boundaries, executable launcher and public imports passed; workspace ZIP generated |
| `python3 scripts/dev.py test` | 136 tests passed, 33 added relative to ARC-04 |
| `python3 scripts/dev.py test:architecture` | Full fitness and 32 architecture integration tests passed |
| `python3 scripts/dev.py fitness:json --output build/architecture-fitness.json` | 37 rules passed, 7 modules, 38 production files, one scan, no violations/warnings/cycles/exceptions |
| `python3 scripts/dev.py dependencies:json` | Passed |
| `python3 scripts/dev.py lint` | Syntax, whitespace and architecture passed |
| `./bin/platform --help` | Root help, commands/options/examples displayed |
| `./bin/platform --version` | CLI 0.1.0 displayed |
| `./bin/platform doctor` and `doctor --output json` | Four independent checks passed, human and structured results |
| `./bin/platform modules` and `modules --output json` | Five unstarted foundation markers and activation dependencies displayed |
| `./bin/platform health` and `health --output json` | Fresh local host snapshot, built/degraded, inspection success |
| `./bin/platform run --once` and `run --once --output json` | Host starts healthy and cleans up successfully |
| `./bin/platform run --once --config config/test.json --output json` | Empty activation starts healthy and cleans up |
| `git diff --check` | Passed |

The full test command exercises in-process service/host injection, argument/option validation, all exit categories 0–5, doctor aggregation, cancellation and startup/cleanup failure handling, human/JSON/quiet/verbose behavior, nested and hyphenated future registration, metadata envelope protection and architecture-negative fixtures. Integration launches real source/executable entry points, checks configuration precedence and working-directory semantics, proves source configuration is not modified by doctor, verifies exit propagation and performs persistent host shutdown with SIGINT and SIGTERM.

New direction/public-import rules: ARCH-CLI-001, ARCH-CLI-002, ARCH-CLI-003. ARCH-CLI-004 is explicitly deferred because general business semantics cannot be reliably inferred by the AST analyzer.

CI uses Python 3.11/3.12/3.13 and adds real CLI help/version/modules/health/doctor invocations alongside populated and empty host smoke runs. GitHub CI results must be checked separately; local success does not imply CI success.
