# SK-02 verification

Local verification on Python 3.12.14, 2026-10-10:

| Executed command | Result |
| --- | --- |
| `python3 scripts/dev.py install` | Standard-library workspace ready |
| `python3 scripts/dev.py test` | 200 tests passed; 29 new relative to SK-01 |
| `python3 scripts/dev.py lint` | Syntax, whitespace and architecture passed |
| `python3 scripts/dev.py build` | Syntax, boundaries and public imports passed; source ZIP generated |
| `python3 scripts/dev.py test:architecture` | Full fitness and 36 architecture tests passed |
| `python3 scripts/dev.py fitness:json --output build/architecture-fitness.json` | 41 rules passed across 7 modules; no violations, warnings, cycles or exceptions |
| `python3 scripts/dev.py dependencies:json` | Passed |
| `./bin/platform doctor --output json` | All four read-only checks passed |
| `./bin/platform run --once --output json` | Five foundation boundary markers start healthy and dispose cleanly |
| `./bin/platform --help` | Existing CLI entry point passed |
| `git diff --check` | Passed |

New coverage comprises 19 Namespace unit tests, 5 scalar JSON contract tests, 3 ownership/discovery fixtures and 2 real architecture boundary tests. It verifies canonical case/segments, all required negative inputs, non-string rejection, equality/hash/dictionary use, frozen values/copies, string round trips, parent/child validation, no implicit ordering, reserved-word neutrality, no arbitrary length/depth limits, diagnostic context, string-subclass normalization, safe-parse failure propagation, identity independence on rename, and explicit JSON mapping. The JSON demo confirms sales.orders round trips and sales..orders returns SEM-NS-004.

One initial ownership fixture used an unregistered source with no module owner, which the governance fixture model does not support. The fixture was corrected to registered tooling/runtime sources; the production governance engine was not altered. The full suite then passed.

Kernel production imports remain dataclasses/re with no observed module dependencies. ARCH-SK-NS-001 adds static Namespace class ownership protection using the existing single AST discovery pass. Existing ARCH-SK-002/003 cover dependency independence/public import neutrality; redundant rules are not added. Static checks do not infer generated classes or aliases.

GitHub CI independently repeats validation on Python 3.11, 3.12 and 3.13. Local success is not a claim that remote CI passed; its result is verified before merging.
