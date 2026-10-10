# Model-Driven Enterprise Ecosystem Platform

ARC-01, ARC-02 and ARC-03 establish a contract-driven modular monolith repository. It does **not** implement the semantic platform, compiler, runtime behavior, persistence or UI.

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

The repository contains seven physical source modules: five platform foundations, one independent hosting contract boundary and one CLI. Other families have documented future ownership, not empty packages. Python is an implementation choice; semantic boundaries do not expose Python framework or infrastructure types. Cross-language/wire contracts require explicit design when a real target needs them.

There is no runnable web/mobile UI in ARC-01. Reference Mini Sales is reserved for the first executable vertical slice.

## Dependency governance and selected stack

ARC-02 adds registered zones/owners, exact public API checks, production/test isolation, external approval profiles, deterministic observed/declared graphs and stable diagnostics. See [dependency rules](docs/architecture/dependency-rules.md) and [ARC-02 verification](docs/architecture/arc02-verification.md).

Selected future implementation stack: **Angular + PrimeNG**, **Django + Django REST Framework**, and **contract-based in-memory Mock Data without a database**. The current runnable code is Python governance/doctor tooling; UI/API/data behavior and framework installation are outside ARC-02. Unsupported TS production code fails until a TypeScript analyzer is introduced.

For ARC-02 before its predecessor is merged, check out `arc-02-dependency-rules`. Its pull request is stacked on `arc-01-repository-architecture`; retarget it to main after ARC-01 is merged and revalidate CI.

## Architecture fitness harness

See [fitness functions](docs/architecture/fitness-tests.md) for the ARC-03 30-rule baseline (34 after ARC-04), shared model, severity handling, temporary exceptions, negative fixtures and rule registration. Run `python3 scripts/dev.py fitness` or `fitness:json --output build/architecture-fitness.json`. Full build/architecture checks enforce fitness; filtered runs are for diagnosis. ARC-03 is in `arc-03-fitness-harness`, stacked on ARC-02 until the predecessor is merged.


## Platform bootstrap

ARC-04 adds explicit composition, deterministic activation, validated configuration, lifecycle cleanup and local health. See [platform bootstrap](docs/architecture/platform-bootstrap.md).

```bash
python3 scripts/dev.py doctor
python3 scripts/dev.py run --once
python3 scripts/dev.py run --once --config config/test.json --format json
python3 scripts/dev.py run # stays active until Ctrl-C or SIGTERM
```

The five running modules are boundary markers; no compiler/runtime business behavior is implied. Angular + PrimeNG, Django + DRF and database-free mock contracts remain the selected future adapter stack.


## Unified developer CLI

ARC-05 provides `./bin/platform --help`, `version`, `doctor`, `run`, `modules` and `health`. Commands use explicit registration, public capability injection, human/JSON output and documented exit codes. See [CLI guide](docs/developer/cli.md).

```bash
./bin/platform --help
./bin/platform doctor --output json
./bin/platform modules --output json
./bin/platform health --output json
./bin/platform run --once --output json
```

Health/modules inspect a newly built local host, not another process. Full architecture fitness now enforces 37 rules.


## Semantic Kernel identity

SK-01 introduces the immutable `semantic_kernel.public.SemanticElementId`: an opaque `sem_<UUIDv4>` value with strict validation, canonical lowercase output, safe parsing and value equality/hash semantics. JSON boundaries map it explicitly to a scalar string. See [semantic identity](docs/kernel/semantic-element-id.md) and [ADR-0008](docs/architecture/decisions/ADR-0008-semantic-element-identity.md). Full fitness now enforces 40 rules; no namespace, semantic element, generator, persistence or runtime feature is introduced.

SK-02 adds immutable `semantic_kernel.public.Namespace` with dot-separated ASCII segments, lowercase canonicalization, precise validation, scalar round trips and small naming-only parent/child helpers. See [namespace contract](docs/kernel/namespace.md), [ADR-0009](docs/architecture/decisions/ADR-0009-semantic-namespace-naming.md) and [verification](docs/architecture/sk02-verification.md). Full fitness now enforces 41 rules, including static Namespace ownership; QualifiedName follows in SK-03.

SK-03 adds structured immutable `semantic_kernel.public.QualifiedName`: a validated Namespace plus a case-sensitive ASCII local name, final-dot parsing, structural equality/hash and explicit scalar JSON mapping. See [qualified name contract](docs/kernel/qualified-name.md), [ADR-0010](docs/architecture/decisions/ADR-0010-qualified-semantic-naming.md) and [verification](docs/architecture/sk03-verification.md). Full fitness now enforces 42 rules. Context/reference/element/resolution features follow in later stages.

SK-04 adds immutable `semantic_kernel.public.SemanticContextRef`, a typed wrapper around stable SemanticElementId identity with delegated parsing, value equality/hash and explicit scalar JSON mapping. It does not infer context from Namespace or resolve target existence/kind. See [context reference contract](docs/kernel/semantic-context-ref.md), [ADR-0011](docs/architecture/decisions/ADR-0011-semantic-context-reference-identity.md) and [verification](docs/architecture/sk04-verification.md). Full fitness now enforces 43 rules. Next: SK-05 SemanticElement Base Contract.

SK-05 introduces the minimal `semantic_kernel.public.SemanticElement` Protocol with read-only typed identity, qualified_name and context properties. Test-only Type/Action fixtures demonstrate structural consumption without a production hierarchy. See [root contract](docs/kernel/semantic-element.md), [ADR-0012](docs/architecture/decisions/ADR-0012-minimal-semantic-element-root.md) and [verification](docs/architecture/sk05-verification.md). Full fitness now enforces 44 rules. Context-definition bootstrap ownership remains an explicit deferred decision; next is SK-06 Semantic Element Kinds.

SK-06 adds immutable open `semantic_kernel.public.SemanticElementKind`, a frozen twelve-value Core catalog and required typed `SemanticElement.kind`. Unknown valid values round-trip without compiler/registry checks; canonical case is strict lowercase. See [kind contract](docs/kernel/semantic-element-kind.md), [ADR-0013](docs/architecture/decisions/ADR-0013-open-semantic-element-kind.md) and [verification](docs/architecture/sk06-verification.md). Existing 44 Fitness rules remain sufficient; open-vocabulary/root-type tests add targeted protection. Next: SK-07 Semantic Version Reference.
