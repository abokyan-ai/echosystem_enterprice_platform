# SK-01 verification

Local verification on Python 3.12.14, 2026-10-07:

| Executed command | Result |
| --- | --- |
| `python3 scripts/dev.py install` | Standard-library workspace ready |
| `python3 scripts/dev.py build` | Syntax, boundaries, launcher and public imports passed; source ZIP generated |
| `python3 scripts/dev.py test` | 171 tests passed, 35 added relative to ARC-05; complete suite passed twice consecutively after the final import-path fix |
| `python3 scripts/dev.py test:architecture` | Full fitness plus 34 architecture tests passed |
| `python3 scripts/dev.py fitness:json --output build/architecture-fitness.json` | 40 rules passed; 7 modules, 38 production files, one scan; no violations/warnings/cycles/exceptions |
| `python3 scripts/dev.py dependencies:json` | Passed |
| `python3 scripts/dev.py lint` | Syntax, whitespace and architecture passed |
| `./bin/platform --help` | Existing CLI entry point passed |
| `./bin/platform doctor --output json` | All four read-only checks passed |
| `./bin/platform run --once --output json` | Five foundation boundary markers start healthy and dispose cleanly |
| `git diff --check` | Passed |

New coverage: 22 identity tests, 5 JSON scalar contract tests, 5 pure architecture-rule fixtures, 2 real kernel boundary tests and 1 launcher/standard-library integration regression. Cases include constructor/parse validation, diagnostic codes, exact 40-character layout, hex/prefix case, RFC version/variant bits, Unicode/control/whitespace rejection, frozen state, equality/hash/dictionary use, copies, safe parse, UUIDv4 compatibility, JSON input shape rejection, rename independence, ownership and forbidden imports.

Kernel production imports are only dataclasses and re. Generation is not implemented; compatibility tests consume standard-library UUIDv4 values and do not assert mathematical/global uniqueness. The demo contract test creates an identity, converts it to scalar JSON, parses it back, checks equality and rejects invalid input.

A discovered standard-library import conflict required renaming scripts/platform.py to scripts/platform_cli_launcher.py and placing the standard-library path before tooling helper paths in source launchers. The real platform/uuid regression and existing CLI signal/exit-code integration tests pass. The platform executable name and dev aliases are unchanged.

GitHub CI repeats the full suite on Python 3.11/3.12/3.13. Its result must be checked independently before merging; local success alone is not a CI claim.
