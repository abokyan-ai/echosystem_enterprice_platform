# Repository implementation workflow

## Mandatory deferred-test policy (2026-10-10)

The user's current instruction applies to every implementation task in this repository until the user explicitly changes it.

1. Inspect existing contracts and implement the current task completely.
2. Document all required positive, negative, collision, failure, boundary and integration scenarios in `test-archive/{TASK-ID}/README.md` and `test-archive/{TASK-ID}/{TASK-ID}-deferred-test-spec.md` at the repository root.
3. Reuse existing archive directories. Preserve previously documented scenarios and stable IDs; update or append without deleting history.
4. Each specification must include a stable test ID/name, component, objective, prerequisites, inputs/setup, expected behavior, expected invalid-case diagnostics, edge cases, dependencies, acceptance criteria and execution status. Initially use `NOT_RUN — DEFERRED`.
5. Do not execute the deferred test suite locally or indirectly through CI. Do not run `scripts/dev.py test`, `scripts/dev.py test:architecture`, unittest/pytest discovery or individual archived test methods during implementation. Preserve existing executable tests and required production validation logic.
6. Do not create test infrastructure solely for deferred testing. Code inspection/static reasoning is allowed. Essential syntax/build/dependency checks must be reported separately from deferred test execution; they do not establish semantic correctness.
7. Report implemented contracts, changed sources, archive/spec paths, documented case count, deferred tests executed (0), `DEFERRED / NOT VERIFIED`, limitations/risks and readiness for the next stage. Report skipped CI tests as skipped, never as passed.
8. Complete only the requested task and stop. Do not automatically start the next architectural task.

Future deferred-suite execution requires an explicit later user instruction permitting it, a fixed source revision, available prerequisite contracts/fixtures and recorded evidence. Do not enable test execution merely because a CI job is green. The existing CI workflow's `DEFER_COMPREHENSIVE_TESTS` flag defaults to true; change it only when future execution is explicitly authorized.

Historical executed verification records remain factual and must not be erased or relabeled. A new archive's NOT_RUN status records execution under that archive revision; it does not negate earlier test runs.
