# Contributing

1. Use Python 3.11+ and the root commands in README. Run the install command for the pinned MOD-02 YAML parser dependency.
2. Create a focused branch. Keep changes inside the owning module and import other modules through `package.public` only.
3. Before creating a module, state its responsibility, public contract and allowed dependency edges. Register zone/owner/language/public surface/edge categories in `architecture.json` and validate against `architecture-policy.json` and update documentation. Avoid generic shared/common/utils packages.
4. Follow [AGENTS.md](AGENTS.md): comprehensive/runtime tests are currently DEFERRED. Document complete cases in the task archive; do not run `test`, `test:architecture` or archived cases. Essential static lint/build/dependency checks are separate and do not establish semantic correctness.
5. Under the current deferral policy, document meaningful positive/negative/edge/integration scenarios in the repository task archive. Preserve existing executable tests and update affected expectations, but do not run them or introduce infrastructure solely for deferred testing.
6. External dependencies need explicit review, narrow ownership, an approved adapter profile and a module declaration. Neutral zones use restricted foundational stdlib allowlists. Current Django/DRF approvals are for future HTTP adapters only; MOD-02 adds the narrowly owned PyYAML parser in input tooling.
7. Use UTF-8, LF, four-space Python indentation and no trailing whitespace. `lint` checks syntax/whitespace/import policy; there is no unused formatter dependency.
8. Keep source, configuration, secrets and generated artifacts separate. No production deployment is included.

Public APIs are contracts; `internal/` is private by repository policy. Breaking contract changes require a compatibility decision. Python cannot physically prevent every reflection-based access; the architecture checker is static enforcement, not a security sandbox.

Run `python3 scripts/dev.py dependencies:json` to inspect observed and declared edges. Do not add internal aliases to public APIs, production imports from tests or inline ignores. Temporary waivers require exact scopes, owner/reason/review reference and expiry, as documented in fitness-tests.md. Use specifically owned mock-data adapters for production mock data, not test fixtures. Update doctor's explicit public registration imports and declarations when its inspected module set changes. New production languages need an analyzer before source is accepted.

For a new fitness function: define a pure evaluator over ArchitectureModel, register one rule with stable ID/category/severity/scope, add synthetic positive/negative tests, and document remediation. Do not rescan files in evaluators. Full CI runs all rules; filtered `fitness --rule` runs are diagnostic only.
