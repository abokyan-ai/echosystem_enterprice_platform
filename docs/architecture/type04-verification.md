# TYPE-04 verification

Local verification on Python 3.12.14, 2026-10-10:

| Executed command | Result |
| --- | --- |
| `python3 scripts/dev.py install` | Standard-library workspace ready |
| `python3 scripts/dev.py lint` | Syntax, whitespace and architecture passed |
| `python3 scripts/dev.py build` | Syntax, boundaries and public imports passed; source ZIP generated |
| `python3 scripts/dev.py test` | All 12 suites completed: 488 tests passed, 44 new relative to TYPE-03 |
| `python3 scripts/dev.py test:architecture` | Full fitness and 62 architecture tests passed |
| `python3 scripts/dev.py fitness:json --output build/type04-fitness.json` | All 44 existing rules passed; 7 modules, 39 production files, single scan; no violations, warnings, cycles or exceptions |
| `python3 scripts/dev.py dependencies:json` | Passed; observed model-core -> Kernel only, Kernel -> none |
| `./bin/platform --help` | Existing CLI entry point passed |
| `./bin/platform doctor --output json` | Four read-only checks passed |
| `./bin/platform run --once --output json` | Five foundation boundary markers healthy; once-run completes cleanly |
| Mini Sales demo in full contracts | name required/non-null/max-length 200; middleName optional/nullable; creditLimit optional/non-null/minimum 0/precision 18/scale 2; actual wire round trips and new owner-version snapshot |
| `git diff --check` | Passed |

Coverage added: 30 model unit cases, 11 contract/serialization/demo cases and 3 actual architecture tests. All prior 444 tests remain covered with fixtures updated to explicit constraints. The full run includes completed integration (17) and e2e (2) suites. Final full-suite counts are 152,65,1,1,1,2,1,95,62,89,17,2. The final source ZIP is checked against changed production/test/documentation files after the last documentation update.

Tests verify all four independent presence/nullability states; explicit typed axes/no hidden defaults; open kind identifiers and closed built-in payload support; strict integer domains (including bool/subclass rejection); exact 0.1 and long close numeric bounds; canonical numeric equality/signed zero; 4096-digit input limit; context-independent numeric comparison with precision=1 and every Decimal trap enabled; nonlexical negative comparisons; preserved unevaluated pattern text; fixed kind; duplicate rejection with input indices; all three local contradictions and inclusive endpoints; single-sided constraints; normalized order-independent equality/hash/wire enumeration; defensive collection copying and nested immutability; typed lookup; structurally representable pattern+precision without inferred type; required constraints in FieldDefinition; identity retention/new constrained snapshot; all built-in wire kinds, malformed/unsupported payload rejection and wire copy isolation.

DataFacet regressions verify ID/name uniqueness, case portability, input ordering, lookup and identity semantics after field extension. Integration uses the existing immutable test-only TypeDefinition fixture through TypeDataComposition, not a production TYPE-01 host. No type compatibility, instance validator or physical projection is claimed.

Existing ARCH-DEP-002, ARCH-API-001/002, ARCH-EXT-001, ARCH-DYNAMIC-001 and Kernel direction guards remain active. Additional architecture tests verify actual ownership/dependencies, exact FieldConstraintSet/FieldDefinition typed shape, independent axes and no execution/physical/identity state. All 44 engine rules remain unchanged, without redundant new rules or external static type checker.

Open issues: TYPE-01 production TypeDefinition, SK-09 PrimitiveType and SK-11 Diagnostics Model are missing. Pattern dialect, portable subset, matching mode, instance length units and execution safety are provisional/deferred. The internal model_core.constraint_wire mapping is evolving, not a final public authoring schema; legacy two-member fields intentionally require explicit constraints. Numeric bounds represent exact literals, not runtime arithmetic. Complete missing prerequisites before claiming production type integration; next requested stages are TYPE-05 references and TYPE-06 applicability. GitHub CI must succeed on the exact submitted head before merge.

See [contract](../model/field-constraints.md) and [ADR-0019](decisions/ADR-0019-field-presence-nullability-and-constraints.md).
