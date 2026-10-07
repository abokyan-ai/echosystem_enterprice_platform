# ARC-03 — Architecture Fitness Test Harness

A fitness function is an executable assertion of an architectural property. The harness continuously checks architectural intent without implementing semantic or business behavior.

## Existing state and design

ARC-02 provided manifest metadata, an AST import parser, deterministic graphs and a monolithic evaluator. It had 48 passing tests but no rule registry, severity/result contract or active waiver mechanism. ARC-03 preserves that policy and its IDs, moving evaluation onto a discovered model rather than rewriting the policy.

`architecture_source.py` retains manifest validation, import parsing and graph traversal. `architecture_fitness/discovery.py` scans the registered Python source once. `model.py` defines module/source/architecture/rule/violation/result/exception contracts. `governance.py` evaluates the existing ARC-02 policy over those facts without file I/O. `rules.py` owns the registry, reused baseline rules and composed code-owned graph invariants. `engine.py` evaluates many rules against one model, caches the baseline evaluation, applies narrow exceptions and calculates severity outcomes. `reporting.py` renders human/JSON output. `__main__.py` is independent of unittest.

Root `scripts/` is existing repository tooling, outside shipped platform source. The harness does not create a new feature package or add compiler/runtime dependencies to platform modules. Tests consume tooling; tooling does not import tests. This avoids a new module just to host a standard-library command.

## Architecture model and discovery

Each Module records ID/path/zone/kind/public/internal surfaces and existing manifest metadata. Source facts record owner, relative file, resolved imports with line numbers, direct dynamic calls and scanner issues. ArchitectureModel contains all modules, facts, policy, exceptions, discovery metrics and declared/observed graphs. Its external inventory records actual non-stdlib imports as approved categories or unknown. No installed/transitive package inventory is claimed.

Discovery validates current mappings and parses each source once; rules never run their own repository scan. The adapter uses actual Python imports (including relative, nested and TYPE_CHECKING imports), not string searching. Unknown or unsupported production sources fail through registration fitness. Tests and source are discovered separately. No network or services are needed.

A future build-system adapter can return the same model. A future non-import fitness function can inspect additional explicit model metadata; it does not need a new runner/scanner in each rule.

## Rule contract, results and severity

ArchitectureRule has ID/name/description/category/severity/scope/evaluate. Its evaluator receives ArchitectureModel and a per-run shared cache and returns all ArchitectureViolation values. Registry rejects duplicate IDs, incomplete rules and unknown selection. ArchitectureRuleResult contains rule ID, PASS/WARNING/FAIL, active violations, duration and metadata. Evaluator exceptions or malformed results always fail, even for warning rules, and cannot be waived.

Violation fields: rule_id, severity, message, source, target, evidence, suggested_resolution, optional file/line and dependency_path. Rules cannot downgrade individual violation severity below their registered severity. INFO does not fail; WARNING does not fail unless `--warnings-as-errors`; ERROR and CRITICAL fail. Important existing boundaries are ERROR/CRITICAL, not warnings. One baseline is implemented; no maturity-level configuration is added.

## Stable rule IDs and mandatory invariants

ARC-03's suggested DEP numbers collide with established ARC-02 meanings. Existing IDs are preserved. New precise/transitive invariants use ARCH-FIT-DEP-001..006, with the original policy still executing. This avoids changing an existing rule's meaning in reports or exceptions.

| ARC-03 property | Executable rule | Scope | Severity | Bad example → remediation |
| --- | --- | --- | --- | --- |
| Kernel independent of runtime | ARCH-FIT-DEP-001 + ARCH-DEP-001 | kernel | CRITICAL | kernel → runtime; extract owned abstraction |
| Kernel independent of compiler | ARCH-FIT-DEP-002 + ARCH-DEP-001 | kernel | CRITICAL | kernel → compiler; move required semantics inward |
| Model independent of runtime | ARCH-FIT-DEP-003 + ARCH-DEP-002 | model | CRITICAL | model → runtime; depend on stable semantic contracts |
| Platform independent of concrete adapters | ARCH-FIT-DEP-004 + ARCH-DEP-006 | all platform zones | CRITICAL | runtime → concrete adapter; introduce owned port |
| Platform independent of apps | ARCH-FIT-DEP-005 + ARCH-DEP-007 | all platform zones | CRITICAL | platform → mini-sales; move composition to application |
| Runtime independent of authoring | ARCH-FIT-DEP-006 + ARCH-DEP-004 | runtime | CRITICAL | runtime → model/YAML/JSON parser; consume compiled artifacts |
| Experience framework neutrality | ARCH-EXP-001 + ARCH-DEP-008 | experience | CRITICAL | experience → Django/framework import; keep target code in adapters |
| No cycles | ARCH-CYCLE-001 | declared and observed graph | CRITICAL | a → b → a; invert dependency via independent contract |
| Public contract imports only | ARCH-API-001 | cross-module imports | CRITICAL | a → b.internal; use b.public |
| Production independent of tests | ARCH-TEST-001 + ARCH-DEP-011 | production sources | ERROR | runtime → unittest/fixture; move test code out |
| Restricted kernel externals | ARCH-EXTDEP-001 + ARCH-EXT-001 | kernel | CRITICAL | kernel → Django/database library; adapter ownership |
| Classified module/source | ARCH-MOD-001 + ARCH-REG-001 | all production source | ERROR | unregistered source; register owner/zone/analyzer |

Good examples: model → kernel.public; runtime → compiled_contracts.public; concrete adapter → runtime-owned public port; application wires implementations. These patterns keep contracts stable and implementation volatility outside the core.

All 20 ARC-02 rule IDs are registered, including compiler/IR direction, external ownership, exact allowlists, public local re-exports, naming, dynamic imports and source validity. Ten additional fitness rules above bring the baseline to 30. ARCH-CONFIG-001 is a system discovery/selection/configuration failure; ARCH-EXC-001 is a system expiry failure. Their diagnostic results may appear in addition to registered rule results. The generated rule catalogue in JSON lists current names/severity/scope; do not keep another configurable registry.

Code-owned path rules search both declared and observed graphs, showing a shortest reachable dependency path. They remain executable even if a zone allowlist is relaxed. Counts do not enumerate every possible graph cycle/path. The legacy cycles algorithm remains deterministic and reports detected cycle paths.

## Adding a fitness function

1. Define a pure evaluator over ArchitectureModel. Return violations with the same ID/severity as the registered rule. Do not mutate the model, read source again or call services.
2. Register one ArchitectureRule in `default_registry()` (or use `forbidden_path_rule()` for a graph invariant). Category is an ordinary label; new contract/generated-artifact/security/evolution/tenant/agent categories require no engine change.
3. Add synthetic positive/negative tests and diagnostic assertions. If the rule needs new facts, extend the discovery adapter/model once; never add scanning to the rule.
4. Run the complete baseline and document purpose, scope, severity, good/bad example and remediation.

Example registration inside the existing registry (no additional implemented feature):

```python
registry.register(ArchitectureRule(
    id="ARCH-CONTRACT-EXAMPLE",
    name="Documented ownership",
    description="Verify an explicitly supplied contract ownership fact",
    category="contract",
    severity=Severity.WARNING,
    scope="Selected contracts",
    evaluate=evaluate_contract_ownership,
))
```

The example illustrates registration only; no artificial contract ownership rule or platform feature is shipped. Warning rules can later be promoted after useful evidence.

## Temporary exception mechanism

The central registry stays `docs/architecture/dependency-exceptions.json`, schema version 1. It is empty in this repository. ARC-03 replaces ARC-02's no-waiver baseline with validated temporary exact-match exceptions (ADR-0005).

```json
{
  "schema_version": 1,
  "exceptions": [{
    "id": "temporary-reviewed-seam",
    "rule_id": "ARCH-API-002",
    "source": "model-core",
    "target": "model_core.internal.ConcreteType",
    "reason": "Temporary transition with a scheduled contract extraction",
    "owner": "Architecture owner",
    "created_at": "2026-10-01",
    "expires_at": "2026-11-01",
    "review_issue": "ADR-or-issue-reference"
  }]
}
```

This is documentation only, not an applied waiver. ID/rule/source/target/reason/owner/dates/review reference are mandatory. Unknown IDs, wildcard scopes, empty fields, duplicate IDs/scopes, malformed dates, future creation or expiry before creation fail. Exception dates use ISO UTC evaluation dates. Expiry on or before the evaluation date fails even if the underlying violation disappeared. Matching active violations are retained in `suppressed_violations`; exceptions report applied/unmatched/expired and match counts. Suppression never silently removes evidence. An exact rule/source/target waiver applies to all occurrences of that edge, not an entire module or category.

Overlapping protection is intentional: a legacy zone waiver does not suppress a distinct code-owned path invariant. Both require explicitly reviewed exceptions if truly necessary. No permanent/inline/broad ignore mechanism exists. Evaluator crashes cannot be waived. Review references are local metadata, not network-validated approvals. Code review must approve the registry change.

`--as-of YYYY-MM-DD` makes expiry evaluation reproducible. CI uses the actual UTC date, so waivers cannot persist indefinitely. Same model/policy/as-of gives the same semantic result. Wall-clock timestamp and duration fields are deliberately observational, not deterministic assertions.

## Reports and commands

```sh
python3 scripts/dev.py fitness
python3 scripts/dev.py fitness:json --output build/architecture-fitness.json
python3 scripts/dev.py fitness --rule ARCH-FIT-DEP-001
python3 scripts/dev.py fitness --category dependency
python3 scripts/dev.py fitness --warnings-as-errors
python3 scripts/dev.py test:architecture
python3 scripts/dev.py build
python3 scripts/dev.py test
python3 scripts/dev.py doctor
```

Fitness commands accept repeated `--rule`, `--category`, `--format`, `--as-of`, `--warnings-as-errors` and `--output`. Filters are diagnostic tools, not the full CI baseline. Exit 0 means required selected rules passed; nonzero means a violation, invalid configuration or evaluator failure. JSON stdout is a schema independent of human text: timestamp/as_of/rules/results/violations/exceptions/suppressed_violations/summary/architecture/external_dependencies/discovery. Human output shows rule statuses, counts, remediation, paths and all waivers. Relative source evidence avoids host-specific paths.

Existing dependency graph commands and ARC-02 result schema remain available. `build`, `lint`, `doctor` and architecture validation now run required fitness checks. `test:architecture` runs the full fitness baseline followed by negative architecture tests. Root `test` includes the harness's unit tests and command integration tests as well.

## CI

Existing CI runs full JSON fitness enforcement before build/tests, writes `build/architecture-fitness.json` and uploads it as `architecture-fitness-python-<version>` even when fitness fails. The existing Python 3.11/3.12/3.13 matrix is preserved. No deployment infrastructure is added. CI failure is enforced by job exit status; repository branch-protection settings remain outside this change.

## Self-tests, fixtures and limits

Synthetic model fixtures cover pass/fail/multiple findings, severities, exact suppression, expiry, invalid exceptions, unknown IDs, evaluator errors, report serialization, semantic determinism, one cached baseline evaluation, no rescanning, transitive paths, relaxed-policy resistance, cycles, framework/internal/test/authoring/external/unclassified findings. A temporary repository verifies applied/expired exception JSON behavior through the actual CLI. Existing ARC-02 fixtures and compile-able-but-architecturally-invalid build rejection remain passing.

Only Python AST source is analyzed. Real Angular/TypeScript analysis, package export resolution, framework annotations, dynamic indirect aliases/reflection, installed transitive dependency analysis and artifact/security/tenancy semantics are not claimed. Unsupported production TS/JS/Dart source still fails closed. Future fitness categories can be registered now, but rules for nonexistent semantics are deliberately deferred. The tool governs architecture; it is not a security sandbox.
