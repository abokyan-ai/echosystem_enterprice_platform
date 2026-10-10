# SK-05 verification

Local verification on Python 3.12.14, 2026-10-10:

| Executed command | Result |
| --- | --- |
| `python3 scripts/dev.py install` | Standard-library workspace ready |
| `python3 scripts/dev.py test` | 283 tests passed; 18 new relative to SK-04; full suite passed again after isolating negative dependency fixtures |
| `python3 scripts/dev.py lint` | Syntax, whitespace and architecture passed |
| `python3 scripts/dev.py build` | Syntax, boundaries and public imports passed; source ZIP generated |
| `python3 scripts/dev.py test:architecture` | Full fitness and 42 architecture tests passed |
| `python3 scripts/dev.py fitness:json --output build/architecture-fitness.json` | 44 rules passed; 7 modules, 38 production files, one scan; no violations, warnings, cycles or exceptions |
| `python3 scripts/dev.py dependencies:json` | Passed |
| `./bin/platform --help` | Existing CLI entry point passed |
| `./bin/platform doctor --output json` | All four read-only checks passed |
| `./bin/platform run --once --output json` | Five foundation boundary markers start healthy and dispose cleanly |
| `SemanticElementContractTests.test_demo` (within full test run) | Test Type/Action definitions consumed through the same typed root contract; ID, name and context preserved |
| `git diff --check` | Passed |

New coverage: 12 functional/contract tests, 4 pure architecture fixtures and 2 real architecture boundary tests. Contract tests consume two distinct frozen structural test implementations, preserve typed values, reject raw/missing values at test fixture construction, check property types/read-only shape, distinguish identity from fixture snapshot equality, preserve ID across rename/context move, demonstrate context independent of namespace, confirm no generic production root instance/runtime-checkable validation claim, and execute the demo. Architecture cases reject root duplication outside Kernel and hypothetical runtime/compiler/ORM/UI imports, reuse one AST discovery pass, verify current root contains only three typed property contracts and confirm no observed Kernel module dependency.

The root is typing.Protocol, not a concrete model, runtime validator or heavy inheritance base. Getter annotations form the static contract; Python does not automatically enforce runtime value types/immutability on arbitrary implementations. Test fixtures protect their own construction and are not production Type/Action definitions. No external static type checker, polymorphic serializer, discriminator or registry was added or executed.

Kernel production imports are dataclasses/re/typing. The root directly references the three existing primitives only. ARCH-SK-ELEM-001 adds static ownership protection while existing ARCH-SK-002/003 protect dependency neutrality. Static ownership does not infer generated classes or aliases, and the source-shape test is complemented by actual contract consumers rather than serving as the sole evidence.

Required explicit context remains non-optional. Ownership/bootstrap of a future ContextDefinition remains a documented decision gate in ADR-0012; no root context, null exception or hidden namespace mapping is invented. Kind, Version, references, facets, metadata, concrete definitions, registries and resolution remain deferred.

GitHub CI independently repeats verification on Python 3.11, 3.12 and 3.13; its result is checked before merging. Local success alone is not remote CI evidence.
