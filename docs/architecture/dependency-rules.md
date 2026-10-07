# ARC-02 — Dependency governance

## Principles

Dependencies point toward stable abstractions. Semantic meaning does not depend on runtime/infrastructure implementation. Adapters depend on platform contracts, not the reverse. Compile-able code can be architecturally invalid: imports and allowlists both undergo validation before build.

## Actual state and zones

ARC-01 has five platform modules plus CLI, with public registration markers only. Initially platform modules had no cross-module source imports; CLI dynamically inspected public APIs without observable static edges. ARC-02 replaces that dynamic inspection with five explicit tooling imports and documents them as development edges. There were no actual compiler/runtime cycles, private cross-module imports or adapters in platform source. The earlier checker did not protect production/test imports or public aliases to local implementation and lacked stable IDs and zone metadata; these governance gaps are now covered.

| Zone | Actual modules | Responsibility |
| --- | --- | --- |
| kernel | semantic-kernel | Stable semantics |
| model | model-core | Authoring/canonical model ownership |
| compiled-contracts | compiled-contracts | Independent IR/runtime artifact contracts |
| compiler | compiler-core | Compiler implementation ownership |
| runtime | runtime-core | Compiled artifact consumption |
| tooling | platform-cli | Public registration inspection |
| experience | No source module yet | Existing documented future boundary |
| adapter | No source module yet | Existing documented implementation boundary |
| application | README only | Reference Mini Sales composition boundary |
| tests | Module test trees and root tests | Development checks; not production modules |

Compilation IR and runtime contracts share one stable zone because ARC-01 intentionally has one independent contract module. Packages/evolution/control-plane/agents are not registered zones until meaningful modules exist. Owner labels are responsibility roles, not assignments to named people.

## Actual module allowlist matrix

All allowed cross-module edges use the exact `package.public` surface. ✓ is a declared API edge; D is a declared development inspection edge; ✗ is forbidden/undeclared; — is self access (not a cross-module dependency).

| From / To | Kernel | Model | Contracts | Compiler | Runtime | CLI |
| --- | --- | --- | --- | --- | --- | --- |
| Kernel | — | ✗ | ✗ | ✗ | ✗ | ✗ |
| Model | ✓ | — | ✗ | ✗ | ✗ | ✗ |
| Contracts | ✓ | ✗ | — | ✗ | ✗ | ✗ |
| Compiler | ✓ | ✓ | ✓ | — | ✗ | ✗ |
| Runtime | ✓ | ✗ | ✓ | ✗ | — | ✗ |
| CLI | D | D | D | D | D | — |

This matrix is an allowlist, not a claim that placeholder platform modules import one another. `dependencies:json` reports **declared** and **observed** graphs separately. Currently only the CLI has five observed module edges. Zone policy is an additional ceiling: adding a forbidden edge to a module manifest cannot authorize it.

## Zone policy for existing architectural boundaries

| Consumer zone | Eligible target zones, subject to explicit module allowlist |
| --- | --- |
| kernel | None |
| model | kernel, model |
| compiled-contracts | kernel, compiled-contracts |
| compiler | kernel, model, compiled-contracts, compiler |
| runtime | kernel, compiled-contracts, runtime |
| experience | kernel, model, compiled-contracts, experience |
| adapter | kernel, compiled-contracts, runtime, experience |
| application | kernel, model, compiled-contracts, runtime, experience, adapter |
| tooling | kernel, model, compiled-contracts, compiler, runtime, experience, adapter, application |

Same-zone dependencies still require declaration; all cycles, including self-edges, fail. Frontend adapters have a narrower profile permitting only compiled-contracts/runtime/experience. Django REST Framework and mock-data adapter profiles permit only compiled-contracts/runtime public contracts. Applications wire adapters explicitly in process. No transport between modules is introduced.

## Rule catalogue and executable coverage

| Rule | Meaning | Negative fixture coverage |
| --- | --- | --- |
| ARCH-DEP-001 / DR-001 | Kernel independence | AT-DEP-001, AT-DEP-002, infrastructure/dynamic fixtures |
| ARCH-DEP-002 / DR-002 | Model independence | AT-DEP-003, AT-DEP-004 |
| ARCH-DEP-003 / DR-003 | Compiler direction | Compiler → runtime/database fixtures |
| ARCH-DEP-004 / DR-004 | Runtime independent of source/authoring parsers | AT-DEP-005 (model, YAML, JSON) |
| ARCH-DEP-005 / DR-005 | IR/contracts independent of runtime | Compiled IR → runtime fixture |
| ARCH-DEP-006 / DR-006 | Platform never imports adapters; adapter inversion | AT-DEP-006 and valid memory adapter → runtime fixture |
| ARCH-DEP-007 / DR-007 | Applications do not leak into platform | AT-DEP-007 |
| ARCH-DEP-008 / DR-008 | Experience is framework neutral | AT-DEP-008 |
| ARCH-DEP-009 / DR-009 | Frontend profile consumes designated contracts | Synthetic adapter profile fixture |
| ARCH-DEP-010 / DR-010 | Tooling isolation | Core → CLI fixture |
| ARCH-DEP-011 / DR-011 | Production cannot depend on tests/fixtures | AT-DEP-011 and test-category fixture |
| ARCH-DEP-012 / DR-012 | No generic shared dumping-ground module | AT-DEP-012 |
| ARCH-CYCLE-001 | Cycles in declared or observed graph | AT-DEP-009 and parser unit tests |
| ARCH-API-001 | Cross-module public API only | AT-DEP-010; namespace/private/wildcard fixtures |
| ARCH-API-002 | Public contracts cannot re-export local internals | Public internal alias fixture |
| ARCH-ALLOW-001 | Every observed edge must be declared | Same-zone undeclared fixture |
| ARCH-EXT-001 | External dependency ownership/profile approval | Framework approval/leakage fixtures |
| ARCH-REG-001 | Production source must have registered ownership/analyzer | Unregistered TypeScript fixture |
| ARCH-DYNAMIC-001 | No direct dynamic execution/import in neutral modules | Dynamic import fixture |
| ARCH-SOURCE-001 | Valid syntax/relative imports | Relative-import parser unit tests |
| ARCH-CONFIG-001 | Valid schemas, paths, owners, categories, registrations | Invalid manifest/exception fixtures |

## Public/internal rules

Cross-module imports must use `from semantic_kernel.public import Name` or `import semantic_kernel.public`. Imports of namespace packages, `internal`, underscore-prefixed exports or wildcard exports are rejected. Implementations may import their own internal files. Public contract files may not import local internals and expose their concrete classes through aliases. Type-checking and nested imports are inspected, not skipped. Module initializer files are scanned like any other source.

Correct: `model_core` imports `semantic_kernel.public`. Forbidden: `model_core` imports `runtime_core.public`, even if the allowlist is edited to include runtime. Forbidden: `runtime_core` imports `model_core`, `yaml` or `json`. JSON serialization is not implemented in runtime; its current restricted stdlib policy can only change through an explicit reviewed decision.

## Cross-subsystem contracts

| Boundary | Contract ownership / future seam |
| --- | --- |
| Compiler → runtime | Independent compiled-contracts; no implementation edge |
| Runtime → data | Runtime-owned data/persistence port; in-memory mock-data adapter first |
| Runtime → messaging | Runtime-owned publisher/subscriber contracts |
| Runtime → policy | Authorization port and decision contract |
| Domain → experience | Semantic/action/query references |
| Experience → frontend | Presentation IR and renderer contract |
| Extensions / future agents | Extension or action/authorization public contract |

These are ownership rules, not implemented interfaces or behavior. Stable semantic contracts use API edges; infrastructure uses ports; optional subsystems use an explicit plugin/registration contract rather than a mandatory implementation import.

## Dependency categories and external governance

Module metadata classifies API, implementation, development, test, adapter and optional edges. All cross-module source imports still cross a public surface. Neutral module edges must be API/optional; test edges cannot appear in production manifests. Existing platform edges are API and CLI edges are development. Test dependencies live in test trees rather than production manifests.

External approval categories are foundational, infrastructure, framework, tooling and test-only. The current policy approves **no neutral third-party package**. Restricted stdlib profiles prevent network/database/dynamic-loading/test/parser leakage; compiler alone currently permits JSON parsing. Infrastructure/framework types stop at adapters. `django`/`rest_framework` are recognized framework approvals only for an explicitly opted-in `django-rest-framework` HTTP adapter, which must also declare them in its own manifest. No module currently declares or installs them. Transitive installed-package analysis and version/license governance remain future work when actual dependency manifests exist.

## Selected implementation stack

Angular + PrimeNG is the selected frontend target. Django + Django REST Framework is the selected HTTP adapter. Data is contract-based in-memory Mock Data with no database dependency. A production mock-data adapter is distinct from test fixtures and belongs in `adapters/data/`, not `tests/` or a generic `mocks` package. These choices do not put framework types in kernel/model/experience contracts. No Angular renderer, Django API, data port or mock persistence behavior is implemented in ARC-02.

## Cycle resolution

Depth-first traversal detects cycles in both the complete declared graph and the observed import graph with deterministic traversal order. Errors include the cycle path. Resolve by extracting an owned contract, introducing a port, inverting direction or moving ownership. A service locator, shared-everything module or disabled test is not a resolution. Cycle counts count detected paths separately in each graph, not all possible mathematical cycles.

## Exception policy

`dependency-exceptions.json` is an empty central registry. There are no waivers. This baseline deliberately rejects nonempty registries rather than silently ignoring rules. A proposed exception requires rule ID, affected modules, reason, owner, date, temporary/permanent status, review/expiry condition and ADR/issue reference, plus a reviewed implementation of narrowly matched enforcement. No inline ignores or global switches. Changes to policies and exceptions require architectural code review; CI itself cannot guarantee reviewer behavior without repository protection configuration.

## Commands and CI

```sh
python3 scripts/dev.py check:architecture
python3 scripts/dev.py test:architecture
python3 scripts/dev.py dependencies
python3 scripts/dev.py dependencies:json
python3 scripts/dev.py build
python3 scripts/dev.py test
python3 scripts/dev.py doctor
```

`check:architecture` validates the current repository. `test:architecture` validates it and runs the negative fixtures. Graph commands also return failure on violations; JSON stdout is machine-readable. Build/lint run enforcement before compilation. CI runs explicit enforcement, graph output, build, all tests, architecture fixtures and doctor across Python 3.11/3.12/3.13. No deployment is added.

## Limits and future extension

The active analyzer is Python AST plus manifest policy. There is **no TypeScript/Angular analyzer yet**: adding TS/JS/Dart production source currently fails closed with ARCH-REG-001 until a registered language analyzer/export policy exists. Synthetic frontend/experience fixtures prove Python-level zone/profile enforcement, not Angular compilation. Test trees and root tooling scripts are outside production module import enforcement. Reflection, computed attribute access, indirect re-exports through dynamic assignments, dynamic tooling loaders, file reads and subprocess contents cannot all be proven safe. The checker is architectural governance, not a security sandbox. Add language/dependency analyzers when real modules need them; do not introduce phantom packages now.
