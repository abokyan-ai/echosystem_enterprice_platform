# Model-Driven Enterprise Ecosystem Platform

ARC-01 establishes a contract-driven modular monolith repository. It does **not** implement the semantic platform, compiler, runtime behavior, persistence or UI.

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
```

`install` validates the standard-library workspace; it does not install packages. Windows can use `python` instead of `python3`. Optional Make targets: `install`, `build`, `test`, `test-architecture`, `doctor`, `lint`.

Build checks syntax, architectural boundaries and importable public entry points, and creates `build/arc01-workspace.zip` plus isolated bytecode. Generated output is not source. This is a source workspace, not a released PyPI distribution.

`doctor` is the root equivalent of `platform doctor`: it validates Python availability, manifest configuration, module registration, import wiring and architecture. Root commands provide all module source paths to isolated subprocesses; individual modules never modify `sys.path`.

## Architecture

See [architecture](docs/architecture/README.md), [repository structure](docs/architecture/repository-structure.md), [dependency rules](docs/architecture/dependency-rules.md), [module guidelines](docs/architecture/module-guidelines.md) and [contributing](CONTRIBUTING.md).

The repository contains six physical source modules, five in the platform and one CLI. Other families have documented future ownership, not empty packages. Python is an implementation choice; semantic boundaries do not expose Python framework or infrastructure types. Cross-language/wire contracts require explicit design when a real target needs them.

There is no runnable web/mobile UI in ARC-01. Reference Mini Sales is reserved for the first executable vertical slice.
