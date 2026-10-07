# ARC-02 verification

Local execution date: 2026-10-07. Runtime: Python 3.12.14.

## Baseline inspected

All 53 local ARC-01 tracked blobs were compared with the GitHub branch and matched. Main still contains only initialization; ARC-01 remains an open predecessor. Initial platform cross-module source imports: zero. CLI used dynamic public registration inspection. Existing manifest permitted seven platform edges; no actual business behavior or framework dependencies existed.

## Final results

| Command | Actual local result |
| --- | --- |
| install | Passed: standard-library workspace validation |
| lint | Passed: syntax, whitespace, dependency policy |
| build | Passed: architecture enforcement, bytecode, public imports, source ZIP |
| test | Passed: 48 tests |
| test:architecture | Passed independently: 31 fixture tests plus real repository validation |
| dependencies:json | Passed: six modules, five observed edges, 12 declared edges, zero violations/cycles |
| doctor | Passed: runtime, manifest, explicit registration and dependency validation |
| git diff --check | Passed |

The 48 tests comprise six module registration tests, six parser/diagnostic unit tests, 31 architecture tests, one public-surface contract test, two command integration tests and two CLI E2E tests. AT-DEP-001..012 are present. A negative fixture compiles successfully as Python but both architecture check and build fail with ARCH-DEP-002. This verifies real build rejection, not an optional report.

## Scope and limits

No business feature, frontend renderer, API, persistence or database was added. Selected stack profiles document Angular/PrimeNG, Django/DRF and contract-based mock data. Synthetic Python frontend fixtures verify zone rules; TypeScript/Angular compilation and framework runtime behavior are not claimed. Future TS source fails closed pending a language analyzer. There are no dependency exceptions. Local checks used Python 3.12 only; the committed CI matrix targets 3.11/3.12/3.13 and remote results must be verified separately.

## Risk reduction

Cycles are checked in declared and observed graphs. Zone allowlists and owned contracts protect inward adapter direction. Exact public surfaces and re-export/test-import checks reduce accidental coupling. Narrow external profiles and neutral stdlib allowlists reduce framework/infrastructure leakage. Metadata and negative fixtures make team integration rules explicit. Dynamic/reflection paths, cross-language package exports and transitive dependency governance remain known limitations; the tool is not a security sandbox.

## Next step

Proceed to SK-01 — SemanticElementId after reviewing dependency policy. Extend TEST-03 when adding real language analyzers, external package manifests or more complex public export semantics. Introduce no phantom modules or frameworks merely to expand governance coverage.
