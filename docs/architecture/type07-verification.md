# TYPE-07 verification

Executed locally on Python 3.12.14, 2026-10-10. Implementation follows the repository's Python public-contract conventions rather than introducing an unrelated TypeScript workspace.

| Executed command | Result |
| --- | --- |
| `python3 scripts/dev.py install` | Standard-library workspace ready |
| `python3 scripts/dev.py lint` | Syntax, whitespace and architecture passed |
| `python3 scripts/dev.py build` | Syntax, module boundaries and public imports passed; final source ZIP generated |
| `python3 scripts/dev.py test` | 12 suites, 623 tests passed: 49 new relative to TYPE-06 |
| `python3 scripts/dev.py test:architecture` | All 71 architecture tests and all fitness rules passed |
| `python3 scripts/dev.py fitness:json --output build/type07-fitness.json` | HEALTHY; 44 rules passed, 7 modules, zero cycles/warnings/exceptions/suppression |
| `python3 scripts/dev.py dependencies:json` | model-core -> semantic-kernel only; Kernel -> none |
| `./bin/platform --help` | Existing entry point passed |
| `./bin/platform doctor --output json` | All four checks passed |
| `./bin/platform run --once --output json` | Five foundation modules healthy, clean once-run |
| `git diff --check` | Passed |
| Final source ZIP comparison | All changed code/tests/docs match the final build artifact |

Suite counts: 157,153,1,1,1,2,1,95,71,110,29,2. New coverage consists of 36 model unit cases, 4 contract cases, 6 integration cases and 3 architecture cases. All prior 574 tests remain covered.

Unit coverage: exact/all-version ID/name lookup, numeric ordering across major/minor/patch boundaries, unknown exact references without fallback, distinct absent/empty data, structurally equal separate-input idempotence, conflicting name/data/field identity/order/type/presence/constraints, ownership collisions across differing versions, historical rename/backfill and retained-name ownership, context rejection/isolation, old snapshot preservation, readonly indexes/collections, captured mutable Protocol hosts, input-list aliasing, invalid/non-Type/mutable-subclass input, nested Namespace/context identity extension rejection, diagnostics and result invariants, no embedded semantic validation, explicit ambiguity and selected-only bound views, invalid selections, immutable/copied version binding and snapshot-specific views. All six valid permutations of the representative multiversion/rename/multi-ID set produce equivalent indexes and failure diagnostics.

Contract/integration coverage uses production TypeRegistry/TypeRegistryLookup and actual TypeDataComposition. Existing Mini Sales Customer@1.0.0 and Customer@1.1.0 retain exact versions and original string/boolean/decimal facets. Registry and bound lookup satisfy the unchanged TypeLookup Protocol. Historical-name queries do not redirect. Customer.address resolves when registered and reports existing TYPE-06 missing-target diagnostics otherwise. Employee.manager and A.b/B.a references finish without recursion. An invalid target's constraints are not recursively validated. Multiversion validation raises an explicit orchestration ambiguity unless an exact selected-only view is supplied.

Architecture coverage checks model ownership and unchanged Kernel dependency direction, exact reference/lookup/validator signatures, absence of registry compiler/runtime/authoring methods, no validator calls or dynamic/I/O dependencies in registry methods/helpers, and the sole new stdlib `types` import being MappingProxyType. Two previous exact-import-set assertions were updated to permit this immutable stdlib primitive; the first full run exposed those two outdated assertions. They were corrected and the complete suite rerun successfully. All 44 Fitness rules remain unchanged; no suppression, dependency exception, new module, bootstrap registration or CLI command was introduced.

Immutability is tested at both root and facet/index boundaries. The registry captures supported semantic metadata once, rejects mutable extensions and shares only canonical frozen facet graphs. Duplicate comparison uses supported structural contracts, not object identity, serialization or hashes. Registration failures keep the original snapshot and both indexes intact. Readonly tuple outputs and explicit ordering make insertion order immaterial.

Limits: full production TYPE-01 and SK-11 are still unavailable, and the minimal TYPE-05 vocabulary does not complete full SK-09. The private root capture is not a replacement TypeDefinition; unknown future host facets are outside the supported composition contract. Registration diagnostics reuse current severity/path conventions but cannot claim nonexistent SK-11 integration. A bare ElementRef cannot carry an exact-version request or ambiguity result; direct multiversion find raises TYPE-REG-006, while explicit TypeRegistryLookup supplies the existing unambiguous boundary without changing TYPE-06. Bound views are selected-only, with no implicit fallback. Deliberate Python immutability bypasses are outside supported use.

Deferred: TYPE-08, full missing foundation integration, semantic instances/validation/storage, persistence, endpoints/UI, authoring/imports/aliases, latest/default/version-preference policies, compatibility/migrations, compiler/runtime, graph traversal, inheritance/ValueType propagation, tenant authorization and global/remote registries. GitHub checks must succeed on the exact submitted head before merging.

See [actual contracts/policies/example](../model/type-registry.md) and [ADR-0022](decisions/ADR-0022-context-scoped-immutable-type-registry.md).
