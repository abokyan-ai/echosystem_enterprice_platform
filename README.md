# Model-Driven Enterprise Ecosystem Platform

A contract-driven modular monolith with semantic identity/type contracts, immutable type registration and authoring schema foundations. Compiler behavior, application runtime, persistence and UI remain future stages.

## Quick start

Prerequisite: Python 3.11+; Git for cloning. No pip dependencies, frontend framework, database, containers or services are required.

```sh
git clone https://github.com/abokyan-ai/echosystem_enterprice_platform.git
cd echosystem_enterprice_platform
python3 scripts/dev.py install
python3 scripts/dev.py build
python3 scripts/dev.py check:architecture
python3 scripts/dev.py dependencies:json
```

`install` validates the standard-library workspace; it does not install packages. Windows can use `python` instead of `python3`. Current static Make targets include `install`, `build` and `lint`. Comprehensive/runtime test commands exist but are deferred under [AGENTS.md](AGENTS.md); do not run them during implementation.

Build checks syntax, architectural boundaries and importable public entry points, and creates `build/platform-workspace.zip` plus isolated bytecode. Generated output is not source. This is a source workspace, not a released PyPI distribution.

`doctor` is the root equivalent of `platform doctor`: it validates Python availability, manifest configuration, module registration, import wiring and architecture. Root commands provide all module source paths to isolated subprocesses; individual modules never modify `sys.path`.

## Architecture

See [architecture](docs/architecture/README.md), [repository structure](docs/architecture/repository-structure.md), [dependency rules](docs/architecture/dependency-rules.md), [module guidelines](docs/architecture/module-guidelines.md) and [contributing](CONTRIBUTING.md).

The repository contains eight physical source modules: five platform foundations, one authoring representation boundary, one independent hosting contract boundary and one CLI. Other families have documented future ownership, not empty packages. Python is an implementation choice; semantic boundaries do not expose Python framework or infrastructure types. Cross-language/wire contracts require explicit design when a real target needs them.

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

## Exact semantic versions

SK-07 adds immutable `SemanticVersion` (canonical major.minor.patch, numeric ordering), exact `ElementVersionRef` (stable element ID + version) and required typed `SemanticElement.version`. Versions are independent of package/artifact/deployment numbering and imply no compatibility. See [version contract](docs/kernel/semantic-version.md), [ADR-0014](docs/architecture/decisions/ADR-0014-exact-semantic-version-reference.md) and [verification](docs/architecture/sk07-verification.md). Next: SK-08 Semantic References, then SK-09 Primitive Type System.

## Semantic references

SK-08 adds immutable `ElementRef` containing only a stable `SemanticElementId`. Exact coordinates remain `ElementVersionRef`; symbolic name resolution is deferred outside Kernel. See [reference contract](docs/kernel/semantic-references.md), [ADR-0015](docs/architecture/decisions/ADR-0015-semantic-reference-model.md) and [verification](docs/architecture/sk08-verification.md). Next: SK-09 Primitive Type System, then SK-10 Facet Base Contract and SK-11 Diagnostics Model.

## Composable semantic facets

SK-10 adds open typed `FacetKind`, fourteen immutable Core `FacetKinds`, a one-property `FacetDefinition` Protocol and declarative `FacetApplicability` using semantic kinds. No facets collection or behavior enters `SemanticElement`. See [facet contract](docs/kernel/facets.md), [ADR-0016](docs/architecture/decisions/ADR-0016-composable-semantic-facet-model.md) and [verification](docs/architecture/sk10-verification.md). SK-09 PrimitiveType is still missing; this independent stage does not claim Minimum Kernel completion. Complete SK-09 and SK-11 before concrete Type/Field/DataFacet work.

## Structural field definitions

TYPE-02 adds model-owned immutable `FieldId`, case-sensitive local `FieldName` and minimal `FieldDefinition(id, name)`. Stable identity survives rename; type/constraints and physical projections remain deferred. See [field contract](docs/model/field-definition.md), [ADR-0017](docs/architecture/decisions/ADR-0017-field-identity-and-local-naming.md) and [verification](docs/architecture/type02-verification.md). SK-09, SK-11 and TYPE-01 are absent; this independent stage does not claim them complete. Integrate DataFacet only after those prerequisites.

## Structural data facet

TYPE-03 adds immutable ordered `DataFacet`, fixed `data` kind, local ID/name/case-collision validation and exact typed lookup. `TypeDataComposition` provides a minimal explicit single-facet association through the existing root contract; production TYPE-01 is still missing, so integration is tested with an immutable fixture. See [DataFacet contract](docs/model/data-facet.md), [ADR-0018](docs/architecture/decisions/ADR-0018-data-facet-structural-composition.md) and [verification](docs/architecture/type03-verification.md). Complete missing prerequisites before production type integration; then TYPE-04/05/06.

### TYPE-04 — Field Constraints

FieldDefinition now requires an explicit FieldConstraintSet with separate FieldPresence and FieldNullability axes, plus seven immutable typed constraints. Kind-normalized collections reject duplicates and local length/range/precision contradictions. Numeric bounds use exact fixed-point text; patterns remain unevaluated text with dialect deferred. Internal snapshot mappings round-trip canonical state without JSON/framework coupling. Field types and applicability remain TYPE-05/06 work; production TYPE-01, SK-09 and SK-11 are still missing.

See [contract, truth table and Sales demo](docs/model/field-constraints.md), [ADR-0019](docs/architecture/decisions/ADR-0019-field-presence-nullability-and-constraints.md) and [verification](docs/architecture/type04-verification.md). Two-argument FieldDefinition construction and legacy wire mappings now require explicit constraints; no hidden defaults are supplied.

### TYPE-05 — Type References

FieldDefinition now requires `id, name, type, constraints`. TypeRef is the closed PrimitiveTypeRef/SemanticTypeRef union: typed Kernel primitive vocabulary or stable Kernel ElementRef identity. No raw/runtime/database type, name hint, optional version, Any default, registry or relationship inference exists. Internal mappings use explicit primitive/semantic discriminators; self/mutual references remain finite ID snapshots. TYPE-03/04 invariants remain covered.

SK-09 was missing: a minimal seven-token Kernel PrimitiveType prerequisite is supplied here, without claiming the full unseen SK-09 specification complete. Production TYPE-01 and SK-11 remain missing. Next: TYPE-06 applicability/validation, then TYPE-07 registry. See [actual contracts and Sales demo](docs/model/type-references.md), [primitive prerequisite](docs/kernel/primitive-vocabulary.md), [ADR-0020](docs/architecture/decisions/ADR-0020-semantic-type-reference-strategy.md) and [verification](docs/architecture/type05-verification.md).

### TYPE-06 — Type Validation Rules

TypeValidator now judges declarations separately from their constructors: centralized primitive/constraint applicability, exact integral Integer bounds, conservative semantic-type constraint restrictions and read-only target existence/identity/kind checks. It returns immutable ordered diagnostics with derived validity, keeps core checks mandatory, and performs no mutation, instance validation, recursive graph validation or version selection.

The input remains the TypeDataComposition seam pending production TYPE-01. TypeValidationDiagnostic/Path are explicitly provisional while SK-11 is missing; full SK-09 remains incomplete. Tests cover all 49 primitive/constraint combinations, four presence/nullability states, missing/non-Type/self/mutual targets and Sales valid/invalid examples. Next: TYPE-07 Registry implementing TypeLookup. See [contract and generated matrix](docs/model/type-validation.md), [ADR-0021](docs/architecture/decisions/ADR-0021-semantic-type-validation-architecture.md) and [verification](docs/architecture/type06-verification.md).

### TYPE-07 — Type Registry

TypeRegistry provides context-scoped immutable snapshots with exact ElementVersionRef lookup and deterministic ID/name version collections. Registration is atomic, recognizes structurally equal duplicates, rejects conflicts/name ownership collisions, and preserves per-version historical names without aliases or automatic version selection. Captured root metadata protects snapshots from externally mutable Protocol hosts.

TYPE-06 TypeLookup remains unchanged. Direct registry lookup supports zero/one-version identities; multiversion lookups require an explicitly bound TypeRegistryLookup view. Registration does not invoke validation or traverse references. Production TYPE-01/SK-11 remain missing and the supported input remains TypeDataComposition; full SK-09 is still incomplete. Implementation follows existing Python contracts, not a parallel TypeScript stack. Next: TYPE-08 Semantic Instance Contract. See [contract and Sales example](docs/model/type-registry.md), [ADR-0022](docs/architecture/decisions/ADR-0022-context-scoped-immutable-type-registry.md) and [verification](docs/architecture/type07-verification.md).

### Mandatory deferred test documentation

Current and subsequent implementation tasks must preserve complete test specifications in `test-archive/{TASK-ID}/README.md` and `{TASK-ID}-deferred-test-spec.md` without executing the deferred suites. Each case starts as `NOT_RUN — DEFERRED`; completion reports state `DEFERRED / NOT VERIFIED` and zero deferred tests executed. Historical execution records remain intact. Existing CI performs static architecture/syntax/build checks while comprehensive and runtime checks are explicitly skipped under the deferral flag; green static CI is not proof of semantic correctness. See [repository workflow](AGENTS.md) and [TYPE-07 test archive](test-archive/TYPE-07/README.md). TYPE-08 has not been started.

### MOD-01 — Authoring Model Schema v0

The model-authoring module defines frozen authoring documents, type/data/field/constraint declarations and four explicit type-expression variants. Its pure structural validator accepts decoded abstract documents, rejects unknown shapes/properties/kinds and local duplicates, and preserves unresolved names, exact authored references and original declaration/literal order. It does not resolve names, generate canonical definitions, register types or invoke semantic applicability validation.

Implementation follows current Python contracts; TYPE-01/SK-11/TYPE-08 and full SK-09 integration remain open. The eight-module inventory includes authoring, without changing the five foundation activation markers. [Mini Sales source](examples/authoring/mini-sales.json) is included but not executed. Testing status: **DEFERRED / NOT VERIFIED**, deferred-suite executions **0**. See [schema/assessment](docs/model/authoring-schema.md), [ADR-0023](docs/architecture/decisions/ADR-0023-authoring-schema-representation-boundary.md), [task archive](test-archive/MOD-01/README.md) and [static-check record](docs/architecture/mod01-verification.md). No next stage is started automatically.
