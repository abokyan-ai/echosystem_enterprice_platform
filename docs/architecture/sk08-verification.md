# SK-08 verification

Local verification on Python 3.12.14, 2026-10-10:

| Executed command | Result |
| --- | --- |
| `python3 scripts/dev.py install` | Standard-library workspace ready |
| `python3 scripts/dev.py lint` | Syntax, whitespace and architecture passed |
| `python3 scripts/dev.py build` | Syntax, boundaries/public imports passed; source ZIP generated |
| `python3 scripts/dev.py test` | All 12 suites completed: 365 tests passed, 22 new relative to SK-07 |
| `python3 scripts/dev.py test:architecture` | Full fitness and 50 architecture tests passed |
| `python3 scripts/dev.py fitness:json --output build/architecture-fitness.json` | All 44 existing rules passed; 7 modules, 38 production files, single scan; no violations, warnings, cycles or exceptions |
| `python3 scripts/dev.py dependencies:json` | Passed; zero observed Kernel module dependencies |
| `./bin/platform --help` | Existing CLI entry point passed |
| `./bin/platform doctor --output json` | Four read-only checks passed |
| `./bin/platform run --once --output json` | Five foundation boundary markers start healthy; once-run completes cleanly |
| Reference demo within full contract suite | ID-only identity reference, exact 2.1.0 reference, separate sales.Customer name; no name resolution |
| `git diff --check` | Passed |

New coverage: 11 ElementRef unit cases, 8 reference intent/wire/evolution contracts and 3 actual architecture tests. Existing public export expectations were extended. All prior 343 tests remain covered, including SK-07 exact equality/version differences, numeric ordering and structured serialization. Final full log includes completed integration (17) and e2e (2) suites, not only preceding unit/contract results.

Cases cover typed constructor/from_id preservation without reparsing, delegated SK-01 parsing/canonical hex case, expected diagnostic codes/identity_code/cause, no raw coercion, immutable wrapper/nested ID, equality/hash dictionary/set use, wrong reference intent rejection, unknown valid ID acceptance without a model, unexpected errors propagating from safe parse, strict identity syntax and rejected names/versioned text, stable refs across definition rename/context move/version evolution, exact-versus-identity semantics and explicit caller pin dropping, no optional version/default fields, scalar/nested JSON round trips, unchanged SK-07 exact wire mapping and no Kernel serializer.

Existing ARCH-SK-002/003 plus general stdlib/public/import/dependency rules protect independence. Targeted real tests protect one typed ID field in ElementRef, two required fields in ElementVersionRef, no infrastructure/resolution/name state, Kernel public ownership, no base reference hierarchy and the small identity-only source API. No redundant Fitness rules were added and no external static type checker was run. The unchanged five-property root remains covered by existing contract/architecture tests.

Production inspection found no temporary target-reference API in other modules needing migration; foundation module identifiers/CLI release strings have different semantics. No SemanticContextRef/ElementVersionRef refactor, root-field addition, bootstrap registration or UI/CLI command was needed. Deferred symbolic/unresolved/resolved reference contracts, namespace/alias/import resolution, version selection/ranges, specialized refs, instance refs, registries and content/publication governance are documented in ADR-0015. Next: SK-09, SK-10, SK-11.

See [reference contract](../kernel/semantic-references.md) and [ADR-0015](decisions/ADR-0015-semantic-reference-model.md). GitHub CI must succeed on the exact submitted head before merge to main.
