# TYPE-03 verification

Local verification on Python 3.12.14, 2026-10-10:

| Executed command | Result |
| --- | --- |
| `python3 scripts/dev.py install` | Standard-library workspace ready |
| `python3 scripts/dev.py lint` | Syntax, whitespace and architecture passed |
| `python3 scripts/dev.py build` | Syntax, boundaries/public imports passed; source ZIP generated |
| `python3 scripts/dev.py test` | All 12 suites completed: 444 tests passed, 24 new relative to TYPE-02 |
| `python3 scripts/dev.py test:architecture` | Full fitness and 59 architecture tests passed |
| `python3 scripts/dev.py fitness:json --output build/architecture-fitness.json` | All 44 existing rules passed; 7 modules, 38 production files, single scan; no violations, warnings, cycles or exceptions |
| `python3 scripts/dev.py dependencies:json` | Passed; observed model-core -> Kernel only, Kernel -> none |
| `./bin/platform --help` | Existing CLI entry point passed |
| `./bin/platform doctor --output json` | Four read-only checks passed |
| `./bin/platform run --once --output json` | Five foundation boundary markers healthy; once-run completes cleanly |
| Mini Sales demo in full contracts | Test-only sales.Customer@1.0.0 with name/active/creditLimit; order and stable IDs preserved, 2.0.0 rename representable; types/constraints deferred |
| `git diff --check` | Passed |

New coverage: 13 DataFacet unit cases, 8 composition/wire/demo contracts and 3 actual architecture tests. All prior 420 tests remain covered; completed integration (17) and e2e (2) suites are included. Initial architecture regression assumed model-core had no actual Kernel imports; after DataFacet began consuming approved SK-10 contracts, expectations were updated to observed Kernel use. The distinction test still proves declared-versus-observed graphs differ through compiled-contracts. Full tests and architecture were rerun successfully after that correction.

Tests verify empty/single/multiple fields, fixed kind/noncaller control, explicit ordered list/tuple input and defensive tuple copying, no null/raw/unordered entries, duplicate IDs/names and ASCII case-only collision rejection, deterministic first-error indices/precedence, typed exact lookups and missing results, local rather than global uniqueness, order-sensitive equality/hash with identity-preserving reorder/rename, structural FacetDefinition consumption, retained five-property type host, no duplicate fields, missing-versus-empty, one data slot/rejected multiple facets, explicit applicability/non-Type rejection and ordered evolving JSON round trips.

Architecture guards verify model placement, structural facet kind, no SemanticElement inheritance or physical/runtime state, unchanged FieldDefinition id/name, single source of structural truth and approved model->Kernel direction. Existing 44 Fitness rules remain unchanged; no new module, general facet engine or external static type checker was added/run.

Prerequisite/limits: TYPE-01 production TypeDefinition, SK-09 and SK-11 are absent. Host integration uses TypeDataComposition through the existing SemanticElement contract and immutable test-only TypeDefinition. This is a provisional seam, not a claim that production TYPE-01 is implemented. Concrete hosts must enforce immutable snapshots; the wrapper retains host reference and cannot deep-freeze arbitrary implementations. Local DataFacetError follows current conventions while unified diagnostics are missing. No generic FacetHost/Registry/merge, Field Types/constraints, physical projections or compatibility/migration engine is implemented.

See [contract](../model/data-facet.md) and [ADR-0018](decisions/ADR-0018-data-facet-structural-composition.md). Complete missing prerequisites before production type integration, then TYPE-04/05/06. The specific test converter demonstrates internal/evolving JSON only, not a final published authoring schema. GitHub CI must succeed on the exact submitted head before merge to main.
