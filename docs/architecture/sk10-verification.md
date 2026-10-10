# SK-10 verification

Local verification on Python 3.12.14, 2026-10-10:

| Executed command | Result |
| --- | --- |
| `python3 scripts/dev.py install` | Standard-library workspace ready |
| `python3 scripts/dev.py lint` | Syntax, whitespace and architecture passed |
| `python3 scripts/dev.py build` | Syntax, boundaries/public imports passed; source ZIP generated |
| `python3 scripts/dev.py test` | All 12 suites completed: 390 tests passed, 25 new relative to SK-08 |
| `python3 scripts/dev.py test:architecture` | Full fitness and 53 architecture tests passed |
| `python3 scripts/dev.py fitness:json --output build/architecture-fitness.json` | All 44 existing rules passed; 7 modules, 38 production files, single scan; no violations, warnings, cycles or exceptions |
| `python3 scripts/dev.py dependencies:json` | Passed; zero observed Kernel module dependencies |
| `./bin/platform --help` | Existing CLI entry point passed |
| `./bin/platform doctor --output json` | Four read-only checks passed |
| `./bin/platform run --once --output json` | Five foundation boundary markers healthy; once-run completes cleanly |
| Facet demo within full contract suite | Core data, valid/non-Core preserved acme.routing, illustrative data/type-definition applicability, Data Facet -> SEM-FACET-KIND-002 |
| `git diff --check` | Passed after removing an extra EOF blank line; lint/build repeated after that formatting-only fix |

New coverage: 9 FacetKind cases, 6 Applicability cases, 7 structural/wire/demo contracts and 3 actual architecture tests. Existing public export expectations were extended. All prior 365 tests remain covered, including SemanticElementKind regression after extraction of the shared private lexical validator. Final full log includes completed integration (17) and e2e (2) suites.

Coverage includes all fourteen typed canonical Core constants, frozen catalog/value, unknown scoped/future unqualified preservation, strict case/grammar/segments, no normalization/raw coercion, string subclass handling, expected diagnostics/index and safe-parse unexpected-error propagation, equality/hash consistency, immutable typed frozenset host categories, custom hosts, empty-as-nowhere, set-order-independent equality, rejection of raw/runtime classes/mutable collections, test-only immutable structural facet consumer, scalar/nested JSON round trips and invalid serialized kinds, no generic production payload/serializer and applicability distinct from presence/requirement.

Existing ARCH-SK-002/003 plus stdlib/public/import/dependency Fitness rules protect neutrality; no duplicate rules were added. Focused tests guard actual Kernel ownership, one read-only FacetKind root getter without behavior/bags, FacetApplicability's two typed fields, no infrastructure/runtime/metadata state and the unchanged five-property SemanticElement. No external static type checker was run; Protocol itself does not enforce runtime immutability/types.

Prerequisite status: SK-09 PrimitiveType is absent in inspected main. SK-10 is independent of it and completes only this requested facet base stage. It does not claim SK-09 or whole Minimum Kernel completion. Complete SK-09 and SK-11 before concrete TYPE-01/02/03. No existing semantic facets/bags needed migration, no bootstrap/CLI registration or UI was added. No final Core applicability matrix, FacetHost, engine/registry, polymorphic loading or concrete DataFacet is implemented. Future one-facet-per-kind remains a documented invariant, not enforcement code.

See [facet contract](../kernel/facets.md) and [ADR-0016](decisions/ADR-0016-composable-semantic-facet-model.md). GitHub CI must succeed on the exact submitted head before merge to main.
