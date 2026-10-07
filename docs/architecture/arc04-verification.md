# ARC-04 verification

Local Python 3.12.14 verification on 2026-10-07:

| Command | Result |
| --- | --- |
| `python3 scripts/dev.py install` | Standard-library-only workspace ready |
| `python3 scripts/dev.py lint` | Syntax, whitespace and architecture passed |
| `python3 scripts/dev.py build` | Public imports, boundaries and ZIP build passed |
| `python3 scripts/dev.py test` | 103 tests passed; 31 added relative to ARC-03 |
| `python3 scripts/dev.py test:architecture` | Full fitness and 32 architecture tests passed |
| `python3 scripts/dev.py fitness:json --output build/architecture-fitness.json` | 34 rules passed; 7 modules, 26 production files, one AST scan; no violations, warnings, exceptions or cycles |
| `python3 scripts/dev.py dependencies:json` | Dependency report succeeded |
| `python3 scripts/dev.py doctor` | Configuration, seven public modules and activation wiring passed |
| `python3 scripts/dev.py run --once --format json` | Five boundary markers healthy; reverse cleanup succeeded |
| `python3 scripts/dev.py run --once --config config/test.json --format json` | Empty activation host healthy; clean shutdown |
| `git diff --check` | Passed |

The complete test command includes BOOT-TEST-001..010, failed/partial startup and cleanup retry, config validation/precedence, test overrides, architecture negative fixtures and a real SIGTERM shutdown through the development wrapper. Tests exercise boundary lifecycle only; no semantic/compiler/runtime behavior is claimed.

CI repeats verification on Python 3.11, 3.12 and 3.13, including the populated and empty smoke hosts. Its outcome must be read from the GitHub run; local verification alone is not a claim that CI passed.
