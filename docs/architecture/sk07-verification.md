# SK-07 verification

Local verification on Python 3.12.14, 2026-10-10:

| Executed command | Result |
| --- | --- |
| `python3 scripts/dev.py install` | Standard-library workspace ready |
| `python3 scripts/dev.py lint` | Syntax, whitespace and architecture passed |
| `python3 scripts/dev.py build` | Syntax, boundaries and public imports passed; source ZIP generated |
| `python3 scripts/dev.py test` | 343 tests passed; 33 new relative to SK-06 |
| `python3 scripts/dev.py test:architecture` | Full fitness and 47 architecture tests passed |
| `python3 scripts/dev.py fitness:json --output build/architecture-fitness.json` | All 44 existing rules passed; 7 modules, 38 production files, one scan; zero violations, warnings, cycles or exceptions |
| `python3 scripts/dev.py dependencies:json` | Passed; zero observed Kernel module dependencies |
| `./bin/platform --help` | Existing CLI entry point passed |
| `./bin/platform doctor --output json` | Four read-only checks passed |
| `./bin/platform run --once --output json` | Five foundation boundary markers start healthy and dispose cleanly |
| Version/reference demo within full tests | 2.1.0 exact reference round trip; 1.9.0 < 1.10.0; v1.0 -> SEM-VER-002 |
| Updated root demo within full tests | Test Type/Action definitions expose all five typed properties including version |
| `git diff --check` | Passed |

New coverage: 13 SemanticVersion unit cases, 9 ElementVersionRef unit cases, 6 explicit JSON boundary contracts, 2 additional root-contract cases and 3 real architecture tests. Existing root consumers/property guards/public export expectations were migrated to five properties. All prior 310 tests continue to pass.

Tests cover canonical positive/zero versions, numeric ordering including lexical traps, equality/hash consistency, frozen fields, typed components, bool/int-subclass/float rejection, all three overflow positions including 5000-digit input, no prefixes/leading zeros/Unicode/whitespace/ranges/selectors/suffixes, safe parsing/unexpected error propagation, exact reference equality across ID/version changes, delegated diagnostics/cause, human-text and structured JSON round trips, missing/invalid wire fields, no Kernel serializer, version-required/no-default root implementations and independent stable identity/name.

The existing ARCH-SK-002/003, Kernel stdlib/public API and general dependency rules protect independence; no duplicate Fitness rules were added. Actual boundary tests verify Kernel ownership, exactly two typed reference fields, three plain integer version fields, SemanticElement.version's actual SemanticVersion annotation/read-only getter and absence of lookup/compatibility/increment helpers. Static tests are scoped assertions, not a compatibility analysis engine or general-purpose type checker. No external static checker was run.

The required property addition is an intentional early structural contract evolution: external four-field implementations must provide a typed version. No production concrete definitions currently exist. Published ID/version immutability still requires future governance; coordinates prove neither content integrity, existence nor compatibility. Prerelease/build metadata, ranges/selectors, compatibility/diff/migrations, package/artifact/model/deployment engines and latest/registry resolution remain deferred. Context-definition ownership remains the ADR-0012 gate. Next: SK-08 Semantic References, then SK-09 Primitive Type System.

See [contract](../kernel/semantic-version.md) and [ADR-0014](decisions/ADR-0014-exact-semantic-version-reference.md). GitHub CI must pass on the exact submitted head before merging to main.
