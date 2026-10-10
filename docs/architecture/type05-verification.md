# TYPE-05 verification

Local verification on Python 3.12.14, 2026-10-10:

| Executed command | Result |
| --- | --- |
| `python3 scripts/dev.py install` | Standard-library workspace ready |
| `python3 scripts/dev.py lint` | Syntax, whitespace and architecture passed |
| `python3 scripts/dev.py build` | Syntax, boundaries/public imports passed; final source ZIP generated |
| `python3 scripts/dev.py test` | All 12 suites completed: 525 tests passed, 37 new relative to TYPE-04 |
| `python3 scripts/dev.py test:architecture` | Full fitness and 65 architecture tests passed |
| `python3 scripts/dev.py fitness:json --output build/type05-fitness.json` | All 44 existing rules passed; 7 modules, 39 production files, one scan; zero violations, warnings, cycles, exceptions or suppression |
| `python3 scripts/dev.py dependencies:json` | Passed; model-core -> Kernel, Kernel -> none |
| `./bin/platform --help` | Existing entry point passed |
| `./bin/platform doctor --output json` | All four read-only checks passed |
| `./bin/platform run --once --output json` | Five foundation boundary markers healthy; clean once-run |
| Executable Sales demo in contract suite | Customer@1.0.0 string name/max-length 200, boolean active, decimal creditLimit/minimum 0/precision 18/scale 2; Order.customer stable semantic ref |
| `git diff --check` | Passed |
| Final source ZIP comparison | All changed code/tests/docs match the final build artifact |

New coverage: 5 Kernel primitive prerequisite tests, 17 model reference/field tests, 12 contract/wire/demo tests and 3 actual architecture tests. All prior 488 cases remain covered with explicit type fixtures; no Any/unknown production or legacy wire default was introduced. Full suite counts: 157,82,1,1,1,2,1,95,65,101,17,2, including completed integration (17) and e2e (2).

Tests verify seven canonical primitive references, strict nominal payloads, read-only fixed variant kinds, frozen nested state, equality/hash and cross-variant separation, missing/invalid field types, exact-class closed union admission, retained primitive/ElementRef objects, rejected raw names/IDs/classes/DB types/loaded objects/versioned refs, no custom/Any/Object/Unknown/subclass escape, FieldId retention on INTEGER -> DECIMAL snapshot, separate four-state constraint axes, structurally allowed string+precision pending applicability, self/mutual finite refs, explicit discriminator/variant wire shapes, foundational parse error propagation, rejection of optional-version/name-hint/mixed/compact wire forms, both field variants round trip, missing-type rejection without default, wire copy isolation, sales.String distinction and rename/context/version stability.

DataFacet regressions retain local ID/name uniqueness, ASCII case portability, ordering, lookup, immutability and identity semantics. TYPE-04 exact numeric, duplicate/local contradiction, collection normalization, presence/nullability and serialization tests remain covered. Sales fixtures carry explicit representative types; target validity/constraint applicability are not claimed.

Architecture verifies exact union/payload/FieldDefinition type shapes, Kernel ownership of PrimitiveType with no model imports, model-owned TypeRef using only Kernel public primitives, and absence of loaded target/name/version/registry/runtime/SQL/nullable/executable members. Existing 44 Fitness rules remain unchanged, no new module/bootstrap registration or external static type checker.

Prerequisite reconciliation: SK-09 PrimitiveType did not exist. This stage provides only the minimal seven-token foundational vocabulary required by the TYPE-05 specification, with documentation and tests; it does not claim completion of the full unseen SK-09 stage. TYPE-01 production host and SK-11 unified diagnostics are still absent. Integration uses the existing frozen test-only TypeDefinition through TypeDataComposition. Local errors retain existing conventions; full primitive temporal/runtime semantics and diagnostic path integration remain open. Pattern dialect remains provisional. Internal wire shapes are evolving rather than final authoring schema.

Deferred: authoring/symbolic resolution, target existence/kind, exact-version selection, registry, applicability/assignability/coercion, collections/generics, relationships, runtime validation, physical projections, compatibility/migration. Next requested stage TYPE-06, then TYPE-07; complete missing prerequisites before claiming full production type integration. GitHub CI must succeed on the exact submitted head before merge.

See [contract](../model/type-references.md), [minimal prerequisite](../kernel/primitive-vocabulary.md) and [ADR-0020](decisions/ADR-0020-semantic-type-reference-strategy.md).
