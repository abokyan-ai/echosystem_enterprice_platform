# Contributing

1. Use Python 3.11+ and the root commands in README. No dependency installation is needed.
2. Create a focused branch. Keep changes inside the owning module and import other modules through `package.public` only.
3. Before creating a module, state its responsibility, public contract and allowed dependency edges. Register it in `architecture.json` and update documentation. Avoid generic shared/common/utils packages.
4. Run `python3 scripts/dev.py lint`, `build`, `test`, `test:architecture` and `doctor` before submitting a pull request.
5. Add negative architecture fixtures for new rules and meaningful behavior tests for implemented features. Do not add fake tests for future features.
6. External dependencies need explicit review, narrow ownership and a corresponding checker policy update. Platform source currently allows the standard library only, excluding dynamic-loading and infrastructure imports.
7. Use UTF-8, LF, four-space Python indentation and no trailing whitespace. `lint` checks syntax/whitespace/import policy; there is no unused formatter dependency.
8. Keep source, configuration, secrets and generated artifacts separate. No production deployment is included.

Public APIs are contracts; `internal/` is private by repository policy. Breaking contract changes require a compatibility decision. Python cannot physically prevent every reflection-based access; the architecture checker is static enforcement, not a security sandbox.
