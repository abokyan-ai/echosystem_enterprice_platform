# ARC-03 verification

Local execution: 2026-10-07, Python 3.12.14. ARC-03 builds on ARC-02 commit eab923e79498c02c1c9c8df475cd57602800ce87. ARC-01 is merged in main; ARC-02 is still an open predecessor.

| Check | Actual local result |
| --- | --- |
| install | Passed: workspace metadata validation |
| lint | Passed: syntax, whitespace and full fitness enforcement |
| build | Passed: required fitness, bytecode, public imports and source bundle |
| test | Passed: 72 tests |
| test:architecture | Passed: full 30-rule fitness report and 32 negative/repository fixture tests |
| fitness:json | Passed: 6 modules, 30 rules, 30 passed, 0 failed/warnings/exceptions/cycles |
| discovery | 20 source files parsed, one scan pass |
| doctor | Passed: registration/configuration and full fitness checks |
| git diff --check | Passed |

The 72 tests comprise 6 module tests, 26 unit tests (6 existing parser tests and 20 harness tests), 32 architecture tests, 1 public-surface test, 5 integration command tests and 2 CLI E2E tests. The original ARC-02 tests remain passing. Synthetic models test severity/exception/report/registry behavior without modifying real source. A temporary repository proves exact waivers are applied and expired waivers fail through the real CLI. A model/runtime source fixture remains valid Python but fails both checker and build. Code-owned graph rules detect a transitive path and survive a relaxed configuration allowlist.

One run discovers source once and executes all rules on that model. The existing governance evaluator is cached once per run, independently tested. Rule result determinism excludes timestamp/duration; exception evaluation is deterministic for an injected as-of date. CI uses actual UTC dates.

The CI configuration runs the full JSON fitness baseline and uploads its report even on failure, preserving Python 3.11/3.12/3.13. Local tests ran on 3.12.14; remote CI results are verified separately. No frontend/API/database/semantic feature is implemented. No real exception is applied. TypeScript/Angular analyzers, installed dependency closure, reflection and future action/tenant/agent semantics remain out of scope.

The harness reduces false confidence through negative fixtures, protects policy intent with code-owned invariants, exposes suppressed evidence and rejects expired/unknown/broad waivers. Repository protection/code-review approval and unsupported language semantics remain separate concerns.
