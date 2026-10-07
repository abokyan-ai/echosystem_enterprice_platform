# Model-Driven Enterprise Ecosystem Platform

ARC-01 and ARC-02 establish a contract-driven modular monolith repository. It does **not** implement the semantic platform, compiler, runtime behavior, persistence or UI.

## Quick start

Prerequisite: Python 3.11+; Git for cloning. No pip dependencies, frontend framework, database, containers or services are required.

```sh
git clone https://github.com/abokyan-ai/echosystem_enterprice_platform.git
cd echosystem_enterprice_platform
python3 scripts/dev.py install
python3 scripts/dev.py build
python3 scripts/dev.py test
python3 scripts/dev.py test:architecture
python3 scripts/dev.py doctor
python3 scripts/dev.py check:architecture
python3 scripts/dev.py dependencies:json
```

`install` validates the standard-library workspace; it does not install packages. Windows can use `python` instead of `python3`. Optional Make targets: `install`, `build`, `test`, `test-architecture`, `doctor`, `lint`.

Build checks syntax, architectural boundaries and importable public entry points, and creates `build/platform-workspace.zip` plus isolated bytecode. Generated output is not source. This is a source workspace, not a released PyPI distribution.

`doctor` is the root equivalent of `platform doctor`: it validates Python availability, manifest configuration, module registration, import wiring and architecture. Root commands provide all module source paths to isolated subprocesses; individual modules never modify `sys.path`.

## Architecture

See [architecture](docs/architecture/README.md), [repository structure](docs/architecture/repository-structure.md), [dependency rules](docs/architecture/dependency-rules.md), [module guidelines](docs/architecture/module-guidelines.md) and [contributing](CONTRIBUTING.md).

The repository contains six physical source modules, five in the platform and one CLI. Other families have documented future ownership, not empty packages. Python is an implementation choice; semantic boundaries do not expose Python framework or infrastructure types. Cross-language/wire contracts require explicit design when a real target needs them.

There is no runnable web/mobile UI in ARC-01. Reference Mini Sales is reserved for the first executable vertical slice.

## Dependency governance and selected stack

ARC-02 adds registered zones/owners, exact public API checks, production/test isolation, external approval profiles, deterministic observed/declared graphs and stable diagnostics. See [dependency rules](docs/architecture/dependency-rules.md) and [ARC-02 verification](docs/architecture/arc02-verification.md).

Selected future implementation stack: **Angular + PrimeNG**, **Django + Django REST Framework**, and **contract-based in-memory Mock Data without a database**. The current runnable code is Python governance/doctor tooling; UI/API/data behavior and framework installation are outside ARC-02. Unsupported TS production code fails until a TypeScript analyzer is introduced.

For ARC-02 before its predecessor is merged, check out `arc-02-dependency-rules`. Its pull request is stacked on `arc-01-repository-architecture`; retarget it to main after ARC-01 is merged and revalidate CI.
