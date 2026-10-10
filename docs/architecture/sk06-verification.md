# SK-06 verification

Local verification on Python 3.12.14, 2026-10-10:

| Executed command | Result |
| --- | --- |
| `python3 scripts/dev.py install` | Standard-library workspace ready |
| `python3 scripts/dev.py test` | 310 tests passed; 27 new relative to SK-05 |
| `python3 scripts/dev.py lint` | Syntax, whitespace and architecture passed |
| `python3 scripts/dev.py build` | Syntax, boundaries and public imports passed; source ZIP generated |
| `python3 scripts/dev.py test:architecture` | Full fitness and 44 architecture tests passed |
| `python3 scripts/dev.py fitness:json --output build/architecture-fitness.json` | Existing 44 rules passed; 7 modules, 38 production files, one scan; no violations, warnings, cycles or exceptions |
| `python3 scripts/dev.py dependencies:json` | Passed |
| `./bin/platform --help` | Existing CLI entry point passed |
| `./bin/platform doctor --output json` | All four read-only checks passed |
| `./bin/platform run --once --output json` | Five foundation boundary markers start healthy and dispose cleanly |
| Inline Kind demo | action-definition is Core; acme.route-definition is valid/non-Core/preserved; both round trip; Action Definition -> SEM-KIND-002; compiler support explicitly not evaluated |
| Updated root contract demo (within full tests) | Explicit Type/Action kinds preserved through shared root consumer; custom kind accepted through same root |
| `git diff --check` | Passed |

New coverage: 17 Kind unit tests, 5 scalar JSON contracts, 3 additional root-contract cases and 2 real architecture boundary tests. Cases verify all twelve typed Core constants/canonical values, immutable catalog/value, non-Enum public value, unknown scoped/future unqualified preservation, strict lowercase kebab grammar, no normalization/coercion, malformed segments and separators, equality/hash/dictionary use, copies/no ordering, known-Core membership without support/ownership claims, safe-parse failure propagation, string-subclass storage safety, diagnostic context, Core/custom JSON round trips, numeric/object wire rejection and executable demo. Root tests require explicit typed kind with no default, preserve custom kind and keep classification independent of implementation class/identity/name/context.

All existing root fixtures/consumers are migrated to the fourth required property. A targeted source-shape guard now allows exactly id, qualified_name, context and kind. Public getter annotations use SemanticElementKind, and actual structural consumers exercise the contract. No external static type checker or polymorphic model serializer is claimed.

Kind uses dataclasses/re only, independently of peer primitives. Kernel imports remain dataclasses/re/typing with no observed cross-module dependency. Existing ARCH-SK-002/003 and ARC-03 rules suffice; no redundant rule or broad enum regex is added. Targeted non-Enum/unknown-preservation/root-type tests protect the open contract.

Lexical parsing remains independent of Core catalog membership. Namespaced extensions are the publication governance convention; unknown unqualified lexical identifiers are preserved for future platform vocabulary. Registry ownership, reservation enforcement, compiler support, handlers, schemas and package registration remain deferred, as recorded in ADR-0013. Root Context Definition ownership remains the ADR-0012 decision gate.

GitHub CI independently repeats verification on Python 3.11, 3.12 and 3.13; its result is checked before merging. Local success alone is not remote CI evidence.
