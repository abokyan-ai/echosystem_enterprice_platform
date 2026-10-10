# TYPE-06 verification

Local verification on Python 3.12.14, 2026-10-10:

| Executed command | Result |
| --- | --- |
| `python3 scripts/dev.py install` | Standard-library workspace ready |
| `python3 scripts/dev.py lint` | Syntax, whitespace and architecture passed |
| `python3 scripts/dev.py build` | Syntax, boundaries/public imports passed; final source ZIP generated |
| `python3 scripts/dev.py test` | All 12 suites completed: 574 tests passed, 49 new relative to TYPE-05 |
| `python3 scripts/dev.py test:architecture` | Full fitness and 68 architecture tests passed |
| `python3 scripts/dev.py fitness:json --output build/type06-fitness.json` | All 44 rules passed; 7 modules, 39 production files, one scan; zero violations, warnings, cycles, exceptions or suppression |
| `python3 scripts/dev.py dependencies:json` | Passed; model-core -> Kernel, Kernel -> none |
| `./bin/platform --help` | Existing entry point passed |
| `./bin/platform doctor --output json` | Four read-only checks passed |
| `./bin/platform run --once --output json` | Five foundation boundary markers healthy; clean once-run |
| Generated documentation matrix | Derived directly from actual primitive_constraint_kinds policy |
| `git diff --check` | Passed |
| Final source ZIP comparison | All changed code/tests/docs match the final build artifact |

New coverage: 35 model unit cases, 5 contracts, 6 reference-aware integration cases and 3 architecture tests. All previous 525 cases remain covered; full suite counts are 157,117,1,1,1,2,1,95,68,106,23,2, including completed integration (23) and e2e (2). The 7 matrix test methods exhaust all 49 primitive/constraint combinations as subtests; another test covers all four presence/nullability states across seven primitives plus semantic refs. These subcases are not counted as additional standalone tests.

Tests verify the entire centralized applicability policy, exact fractional/integral Integer bounds including signed zero/1.000/4096-digit values, Decimal fractional bounds and independent precision/scale, unevaluated pattern syntax, no primitive lookup, current host-kind validation at the retained Protocol boundary, missing/Action/Policy/mismatched targets, required context, self/mutual references without recursion, conservative semantic constraints, lookup/rule programming error propagation, empty/absent data, multi-error aggregation and ordering, canonical kind-order independence, stable path/FieldId association across field reorder/host rename, unsupported-kind fail-closed behavior, copied immutable results/rule collections, derived validity with warnings, mandatory core rules and duplicate-ID rejection.

The Sales contract demo validates Customer@1.0.0 name:string/max-length 200, active:boolean and creditLimit:decimal/minimum 0/precision 18/scale 2. Invalid string+precision and boolean+max-length yield two diagnostics while actual field wire snapshots remain unchanged. Customer/Address integration passes with Address present and fails when absent/non-Type. A separately invalid Address does not cause recursive Customer validation; each definition is judged independently. Different supplied target-version views do not trigger latest/exact selection.

Canonical TYPE-04 rejects custom constraint payloads already. A test-only object.__setattr__ bypass exercises the defensive unsupported-kind path; no production generic/unsafe payload API is added. One initial test incorrectly treated Protocol's inherited ABC.register method as a platform Registry method; it was corrected to check that the declared TypeLookup contract contains only find, and full tests were rerun successfully.

Architecture tests verify actual model ownership, read-only lookup/context/result/path shapes, pure mandatory pipeline boundaries, policy outside PrimitiveType/TypeRef/constraints and core rule ASTs without model attribute writes, I/O or recursive validation. Existing ARCH-DEP-002, ARCH-API-001/002, ARCH-EXT-001, ARCH-DYNAMIC-001 and Kernel direction guards remain active. All 44 engine rules are unchanged; no module, concrete Registry, compiler/runtime dependency, CLI command or external static type checker was added.

Limits: production TYPE-01 and SK-11 are absent; full SK-09 remains incomplete beyond TYPE-05's minimal primitive vocabulary. The actual validator input is TypeDataComposition and lookup returns broad SemanticElement. Tests use frozen test-only hosts/views, not production TypeDefinition/Registry. TypeValidationDiagnostic/Path are a provisional type-specific seam; unified Diagnostic/SemanticPath/SourceLocation integration is not claimed. Core rules are stateless/non-mutating, but arbitrary injected rule/provider implementations must honor that contract. Pattern dialect and future ValueType constraint propagation remain open.

Deferred: concrete Registry, full foundation integration, instance/runtime validation, namespace/alias resolution, version selection, assignability/coercion, inheritance, ValueType propagation, cross-field/relationship rules, physical projections, compatibility/migration and global model validation orchestration. Next requested stage TYPE-07 implements read-only TypeLookup without reverse dependency. GitHub CI must succeed on the exact submitted head before merge.

See [contract/matrix/demos](../model/type-validation.md) and [ADR-0021](decisions/ADR-0021-semantic-type-validation-architecture.md).
