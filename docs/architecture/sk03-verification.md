# SK-03 verification

Local verification on Python 3.12.14, 2026-10-10:

| Executed command | Result |
| --- | --- |
| `python3 scripts/dev.py install` | Standard-library workspace ready |
| `python3 scripts/dev.py test` | 235 tests passed; 35 new relative to SK-02 |
| `python3 scripts/dev.py lint` | Syntax, whitespace and architecture passed |
| `python3 scripts/dev.py build` | Syntax, boundaries and public imports passed; source ZIP generated |
| `python3 scripts/dev.py test:architecture` | Full fitness and 38 architecture tests passed |
| `python3 scripts/dev.py fitness:json --output build/architecture-fitness.json` | 42 rules passed; 7 modules, 38 production files, one scan; no violations, warnings, cycles or exceptions |
| `python3 scripts/dev.py dependencies:json` | Passed |
| `./bin/platform --help` | Existing CLI entry point passed |
| `./bin/platform doctor --output json` | All four read-only checks passed |
| `./bin/platform run --once --output json` | Five foundation boundary markers start healthy and dispose cleanly |
| Inline source demo | Parsed sales.orders.SalesOrder, extracted components, canonical output/round trip PASS; SalesOrder -> SEM-QN-002; sales.Order Management -> SEM-QN-004 |
| `git diff --check` | Passed |

New coverage: 25 QualifiedName unit tests, 5 scalar JSON contract tests, 3 ownership/discovery fixtures and 2 real architecture boundary tests. Cases include structural constructor/factory, final-dot parsing, mandatory namespace, canonical namespace/exact local case, lexical validity without kind style enforcement, malformed segments, all required invalid input cases, no coercion/repair, Namespace validation delegation and diagnostic mapping, no reparsing already validated Namespace, frozen components/copies/replacement, structural equality/hash/dictionary use, cross-type rejection, string round trips across 25 combinations, identity separation on rename/move, string-subclass equality safety, safe-parse unexpected failure propagation and ordinary segments without version/tenant/kind/security semantics.

Kernel production imports remain dataclasses/re and no observed module dependency. ARCH-SK-QN-001 adds static QualifiedName class ownership protection with existing single-pass AST discovery. Existing ARCH-SK-002/003 cover dependency independence and public import neutrality; redundant naming infrastructure rules are not added. Dynamically generated classes and aliases are not inferred by static ownership checks.

No QualifiedName resolution, registry, SemanticElement, context, reference, version or migration behavior is implemented. Scalar JSON mapping occurs only at the contract-test/documented boundary outside Kernel.

GitHub CI independently repeats verification on Python 3.11, 3.12 and 3.13; its result is checked before merging. Local results do not imply remote CI success.
