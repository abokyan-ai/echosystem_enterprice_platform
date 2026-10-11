# Model-Driven Enterprise Ecosystem Platform

A contract-driven modular monolith with semantic identity/type contracts, immutable type registration and authoring schema foundations. Compiler foundations, bounded runtime-loading orchestration, a scoped exact-version registry and conditional immutable instance orchestration are implemented. Actual TYPE-08 canonical instances, approved loaded instance schemas/decoders and authenticated runtime integrations remain unavailable; activation, persistence and UI remain future capabilities.

## Quick start

Prerequisite: Python 3.11+; Git for cloning. MOD-02 YAML loading uses pinned PyYAML; no frontend framework, database, containers or services are required.

```sh
git clone https://github.com/abokyan-ai/echosystem_enterprice_platform.git
cd echosystem_enterprice_platform
python3 scripts/dev.py install
python3 scripts/dev.py build
python3 scripts/dev.py check:architecture
python3 scripts/dev.py dependencies:json
```

`install` installs the explicit YAML parser dependency from requirements-model-loader.txt. Windows can use `python` instead of `python3`. Current static Make targets include `install`, `build` and `lint`. Comprehensive/runtime test commands exist but are deferred under [AGENTS.md](AGENTS.md); do not run them during implementation.

Build checks syntax, architectural boundaries and importable public entry points, and creates `build/platform-workspace.zip` plus isolated bytecode. Generated output is not source. This is a source workspace, not a released PyPI distribution.

`doctor` is the root equivalent of `platform doctor`: it validates Python availability, manifest configuration, module registration, import wiring and architecture. Root commands provide all module source paths to isolated subprocesses; individual modules never modify `sys.path`.

## Architecture

See [architecture](docs/architecture/README.md), [repository structure](docs/architecture/repository-structure.md), [dependency rules](docs/architecture/dependency-rules.md), [module guidelines](docs/architecture/module-guidelines.md) and [contributing](CONTRIBUTING.md).

The repository contains twelve physical source modules: five platform foundations, one authoring representation boundary, one independent hosting contract boundary, one input loader, one CLI, one artifact filesystem boundary, one runtime-loading composition boundary and one pure Python semantic-instance application composition boundary. Other families have documented future ownership, not empty packages. Python is an implementation choice; semantic boundaries do not expose Python framework or infrastructure types. Cross-language/wire contracts require explicit design when a real target needs them.

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

## MOD-02: Model Loader

Explicit memory/file sources feed strict JSON or bounded PyYAML SafeLoader 1.1 decoding, then the existing MOD-01 structural validator. Source-associated immutable results preserve unresolved declarations; ordered batches distinguish all/partial/failed/empty outcomes and reject every duplicate source-ID submission. No semantic lookup, registration, canonicalization, compilation or runtime execution is performed.

See [loading contract and Mini Sales usage](docs/model/model-loader.md), [ADR-0024](docs/architecture/decisions/ADR-0024-model-source-loading-boundary.md), [archive](test-archive/MOD-02/README.md) and [static record](docs/architecture/mod02-verification.md). YAML 1.1 coercions, filesystem trust/resource limits and provisional SK-11 diagnostics are documented limitations. Deferred executions: **0**; status **DEFERRED / NOT VERIFIED**. No loading examples were run; stop at MOD-02.

## MOD-03: Source Location Tracking

The existing input loader now retains immutable source spans and typed node-location indexes for JSON/YAML, including distinct property key/value locations. SourcePosition gains an optional Unicode character offset; pointer paths, deterministic read-only lookup, source snapshot digests and precise primary/related diagnostic locations remain auxiliary to authoring semantics. Legacy source/decoder/result constructors remain compatible.

No Django/DRF endpoint or ORM model is introduced: no existing HTTP API requires extension. General SK-11 remains an explicit missing dependency; the actual loading diagnostic seam is extended without claiming its completion. No test code or examples are executed. See [contract and Mini Sales paths](docs/model/source-location-tracking.md), [ADR-0025](docs/architecture/decisions/ADR-0025-source-location-tracking.md), [single detailed archive](test-archive/MOD-03/MOD-03-deferred-tests.md) and [static record](docs/architecture/mod03-verification.md). Status: **NOT_RUN — DEFERRED / NOT VERIFIED**. Stop at MOD-03.

## MOD-04: Canonical Model Contract

Existing model-core now defines one-context immutable canonical snapshots with caller-selected exact versions, deterministic membership/order/lookup and atomic intrinsic construction results. The current closed payload reuses TypeDataComposition and TYPE-07 frozen host capture; full TypeDefinition and general SK-11 remain explicit missing prerequisites. No registry registration, authoring conversion, reference closure/latest selection, semantic validation orchestration, serialization/hash, framework or runtime behavior is added.

See [contract and unexecuted Mini Sales usage](docs/model/canonical-model.md), [ADR-0026](docs/architecture/decisions/ADR-0026-canonical-model-contract.md), [single detailed archive](test-archive/MOD-04/MOD-04-deferred-tests.md) and [static record](docs/architecture/mod04-verification.md). New automated tests: **0**; executions: **0**; status **NOT_RUN — DEFERRED / NOT VERIFIED**. Stop at MOD-04.

## MOD-05 — Explicit canonicalization

`model_authoring.public.Canonicalizer` transforms one immutable authoring document plus explicit typed resolution bindings into the existing MOD-04 canonical model. It preserves stable IDs/versions/FieldIds, constructs existing fields/data/references/constraints and returns atomic failures with source paths and delegated diagnostics. The model-loader tooling can attach optional existing MOD-03 physical source locations as an external sidecar. No parsing, resolution, registry mutation, validation orchestration, compilation, persistence or endpoint is added.

Current support is the existing five-value host/data seam, not a missing full TYPE-01 contract. General SK-11 is also absent; exact field-version pins fail rather than weaken identity-only TYPE-05. See [contract/usage](docs/model/canonicalizer.md), [ADR-0027](docs/architecture/decisions/ADR-0027-explicit-canonicalization-boundary.md) and [implementation/static evidence](docs/architecture/mod05-verification.md).

[MOD-05 archive](test-archive/MOD-05/README.md): **143** documented scenarios, **0** tests implemented/executed, **NOT_RUN — DEFERRED / NOT VERIFIED**. The Mini Sales snippet was not executed. Static checks do not verify semantic behavior. Stop after MOD-05.

## MOD-06 — Explicit namespace resolution

`model_authoring.public.NamespaceResolver` resolves existing name/identity/exact expressions against a frozen single-context symbol environment. Local-name search uses current plus explicitly supplied namespaces; qualified names are exact; resolver-only explicit aliases never override ordinary dotted names. Ambiguity fails before kind/version requirements can choose an identity. Identity outcomes remain unversioned; exact pins remain exact.

A type-only adapter snapshots explicitly selected actual TYPE-07 TypeLookup identities, and a minimal bridge returns the existing MOD-05 ResolvedFieldBinding without canonicalization. Optional existing tooling attaches actual MOD-03 locations. No new module/dependency/endpoint/ORM, registry mutation, complete reference-binding pipeline or MOD-07. General SK-11/full TYPE-01 and exact-field TYPE-05 compatibility remain documented gaps.

[Resolver/usage](docs/model/namespace-resolver.md), [ADR-0028](docs/architecture/decisions/ADR-0028-explicit-namespace-visibility.md), [implementation/static record](docs/architecture/mod06-verification.md), [archive](test-archive/MOD-06/README.md): **146** documented scenarios; **0** tests implemented/executed; **NOT_RUN — DEFERRED / NOT VERIFIED**. Examples and resolver scenarios were not executed. Static checks are separate evidence.

## MOD-07 — Semantic reference resolution

`model_authoring.public.SemanticReferenceResolver` reuses MOD-06 lookup to verify visible target evidence, context, kind and explicit version requirements. Immutable single/batch results retain diagnostics and partial bindings; complete document preparation exposes the existing MOD-05 ResolvedAuthoringModel only after every required declaration/field binding is satisfied. Primitive fields bypass lookup; forward/self references need no graph traversal. Exact field pins fail explicitly while TYPE-05 remains identity-only. Optional model-loader helpers attach actual MOD-03 locations externally.

[Contract and unexecuted usage](docs/model/semantic-reference-resolver.md), [ADR-0029](docs/architecture/decisions/ADR-0029-verified-reference-binding.md), [implementation/static record](docs/architecture/mod07-verification.md), [archive](test-archive/MOD-07/README.md): **150** documented scenarios, **0** tests implemented/executed, **DEFERRED / NOT VERIFIED**. Full TYPE-01/general SK-11 and cross-context limitations remain explicit. Stop after MOD-07.

## MOD-08 — Explicit validation orchestration

`model_authoring.public.ModelValidationPipeline` checks explicit canonical scope then invokes the existing full TYPE-06 validator on every supported MOD-04 definition, including its approved reference rules. A finite immutable capture of caller-selected TYPE-07 lookup metadata rejects inconsistent environments without selecting versions or mutating the registry. Ordered stage outcomes retain original diagnostics; mandatory incomplete/skipped stages prevent validity, and readiness is derived from VALID/INVALID/INCOMPLETE plus explicit warning policy. Optional model-loader presentation attaches actual MOD-03 locations through existing MOD-05 associations.

[Contract and unexecuted Mini Sales usage](docs/model/validation-pipeline.md), [ADR-0030](docs/architecture/decisions/ADR-0030-validation-orchestration.md), [implementation/static record](docs/architecture/mod08-verification.md), [archive](test-archive/MOD-08/README.md): **146** documented scenarios, **0** tests implemented/executed, **DEFERRED / NOT VERIFIED**. Full TYPE-01/general SK-11 and richer model-kind validators remain absent. No API/database/compiler/runtime or automatic source processing. Stop MOD-08.

## MOD-09 — Model diagnostic integration

Model-authoring adds immutable origin/semantic-target associations around original existing diagnostics. Model-loader tooling integrates loading and domain result diagnostics into source-aware reports, preserving original codes/severities/messages, producer phases, exact owners/FieldIds, MOD-08 status/readiness/stage outcomes and reliable primary/related locations. Fixed phase/emission ordering, derived counts and immutable filter/group helpers never decide validation outcomes. Explicit JSON-ready presentation omits source/semantic/message details by default; no new HTTP endpoint or ORM persistence.

[Contract and unexecuted Mini Sales usage](docs/model/model-validation-diagnostics.md), [ADR-0031](docs/architecture/decisions/ADR-0031-model-diagnostic-integration.md), [implementation/static record](docs/architecture/mod09-verification.md), [archive](test-archive/MOD-09/README.md): **148** documented scenarios, **0** tests implemented/executed, **DEFERRED / NOT VERIFIED**. General SK-11/full TYPE-01 remain absent; exact constraint-source mapping and stronger source pairing are explicit gaps. No upstream validation/resolution/canonicalization execution. Stop MOD-09.

## CMP-01 — Compiler foundation

Existing compiler-core now exposes immutable compiler request/context/phase/state/result contracts and ModelCompiler. Entry requires original MOD-08 VALID/READY evidence bound to the same canonical object. Ordered explicit phases preserve diagnostics and atomic output semantics. Foundation-preparation produces a preparation inventory only; artifact-build remains INCOMPLETE without future concrete generator/output. Stable artifact metadata/key/kind protocol lives in compiled-contracts; no fake artifacts or universal IR.

MOD-09 consumes an explicit model-authoring-owned diagnostic projection without source tooling importing compiler implementation. No validation/resolution/canonicalization execution, artifact publication/DB/API/runtime or deployment authority. [Contract/unexecuted Mini Sales](docs/compiler/compiler-foundation.md), [ADR-0032](docs/architecture/decisions/ADR-0032-compiler-foundation.md), [static record](docs/architecture/cmp01-verification.md), [archive](test-archive/CMP-01/README.md): **156** cases, **0** automated tests implemented/executed, **DEFERRED / NOT VERIFIED**. General SK-11/full TYPE-01 remain gaps. Stop CMP-01.

## CMP-02 — Compilation diagnostics

Compiler-core composes original diagnostics with explicit responsibility, exact semantic and independent artifact associations. Existing MOD-09 projection retains phase prerequisites/execution evidence, original status/validation evidence, lossless occurrence ordering and compiler-only summaries/filters. Existing source enrichment and safe transport preserve physical mapping boundaries; no generator, validator or new HTTP route. [Contract/unexecuted Mini Sales](docs/compiler/compilation-diagnostics.md), [ADR-0033](docs/architecture/decisions/ADR-0033-compilation-diagnostics.md), [implementation record](docs/architecture/cmp02-verification.md), [archive](test-archive/CMP-02/README.md): **137** scenarios, **0** tests implemented/executed, **DEFERRED / NOT VERIFIED**. General SK-11 and future generator/DRF contracts remain upstream gaps. Stop CMP-02.

## CMP-03 — Semantic IR Envelope

Existing compiler-core adds explicit request-scoped IR identity/schema, a closed immutable foundation-coordinate payload, exact canonical origins and typed producer commit/consumer handoff through existing phase state/results. IR remains intermediate and does not satisfy final artifact readiness. CMP-02 carries bounded IR diagnostic identity; transport hides it by default. No lowering/optimizer/generator/HTTP/ORM. [Contract/unexecuted Mini Sales](docs/compiler/semantic-ir-envelope.md), [ADR-0034](docs/architecture/decisions/ADR-0034-semantic-ir-envelope.md), [implementation record](docs/architecture/cmp03-verification.md), [archive](test-archive/CMP-03/README.md): **147** documented scenarios. Tests: **0**, **DEFERRED / NOT VERIFIED**. General SK-11/full domain IR/portable evidence remain gaps. Stop CMP-03.

## CMP-04 — Compiled Type IR

Existing compiler-core adds immutable compiled type/field payloads, reuses precise TYPE-04 constraints and TYPE-05 references and explicitly lowers accepted original canonical type/data members. The composed type phase preserves canonical/field order, requires explicit representation IDs and emits no partial successful set. CMP-03 explicitly supports compiled-type-ir; IR does not satisfy final artifact readiness. [Contract/unexecuted Mini Sales](docs/compiler/compiled-type-ir.md), [ADR-0035](docs/architecture/decisions/ADR-0035-compiled-type-ir.md), [record](docs/architecture/cmp04-verification.md), [archive](test-archive/CMP-04/README.md): **157** documented scenarios. Tests created/executed **0**, **DEFERRED / NOT VERIFIED**. No generator/API/ORM/runtime. Full TYPE-01/general SK-11/richer facets remain gaps. Stop CMP-04.

## CMP-05 — Type Compiler Pass

Existing compiler-core now exposes TypeCompilerPass, reusing CMP-04 lower_payload and CMP-03 factory; old CompiledTypeLoweringPhase aliases the same implementation/stable identity. Canonical multi-version ordering, explicit request-local IDs, collision/rerun/exact-origin guards and atomic existing coordinator handoff; no partial failure output. No dependency/module/HTTP/ORM/runtime/generator additions. [Contract and unexecuted Mini Sales](docs/compiler/type-compiler-pass.md). **129** deferred scenarios, tests created/executed **0**, **DEFERRED / NOT VERIFIED**. Stop CMP-05.

## CMP-06 — Deterministic Compilation

Original compiler now requires frozen phase implementations with approved immutable options, captures complete configuration/classes and rejects ambiguity/drift with CMP-029/030. Existing type pass normalizes exact binding mappings; supported semantic comparison uses actual canonical/payload equality separately from original request ownership and physical presentation. No new orchestrator/module/dependency/route/ORM/generator/serialization/hash/runtime. [Contract and unexecuted Mini Sales](docs/compiler/deterministic-compilation.md). **139** archived scenarios; tests implemented/executed **0**, **DEFERRED / NOT VERIFIED**. Mutable old extension phases need adaptation; unsupported artifact/byte equality remains explicit. Stop CMP-06.

## CMP-07 — Runtime Artifact Manifest

Shared compiled-contracts owns immutable artifact origins/dependencies/descriptors; compiler-core owns bound manifest/V0/assembly using original result status and complete final artifact collection. Original result gains trailing optional request/configuration output origin; legacy unbound result cannot authorize manifest. Typed artifact/manifest diagnostic associations extend compatibly; semantic comparison includes them. No generator/runtime imports/API/ORM/storage/hash/deploy added. Current Type IR-only build stays INCOMPLETE, default runtime-kind approvals empty. [Contract and unexecuted Mini Sales](docs/compiler/runtime-artifact-manifest.md). **144** deferred scenarios, tests implemented/executed **0**, **DEFERRED / NOT VERIFIED**. Stop CMP-07.

### CMP-08 — Artifact Writer

Pure original-result/manifest/byte-source contracts and deterministic plan, plus separate tooling-owned secure Linux filesystem writer with private staging, exact integrity checks, exclusive whole-directory commit, explicit synchronization policy and immutable receipt. [Contract](docs/compiler/artifact-writer.md) · [Source/static record](docs/architecture/cmp08-verification.md) · [158 deferred scenarios](test-archive/CMP-08/CMP-08-deferred-tests.md). Tests created/executed **0**, **DEFERRED / NOT VERIFIED**. No real final byte producer exists yet; Type IR is not written as runtime artifacts. No publication/deployment/HTTP endpoint. Stop after CMP-08.

### CMP-09 — Artifact Reader

Manifest/receipt-driven identity selections, trusted root resolution, server-bounded read limits, safe Linux regular-file access, exact bytes/length/declared-digest verification and atomic immutable selected results. Separate reader in existing tooling, no repair/decoder/runtime/API. [Contract](docs/compiler/artifact-reader.md) · [Source/static record](docs/architecture/cmp09-verification.md) · [173 deferred scenarios](test-archive/CMP-09/CMP-09-deferred-tests.md). Tests created/executed **0**, **DEFERRED / NOT VERIFIED**. Actual final producer/receipt prerequisite absent; Mini Sales is conceptual only. Stop CMP-09.

### CMP-10 — IR Inspector

Read-only in-memory Compiled Type IR inspection with exact envelope/type/field/reference/constraint/origin views, bounded selection and optional escaped developer text. Preserves source IR and independent compilation status; no parsing/validation/lowering/artifact/runtime behavior. [Contract](docs/compiler/ir-inspector.md) · [Source/static record](docs/architecture/cmp10-verification.md) · [179 deferred scenarios](test-archive/CMP-10/CMP-10-deferred-tests.md). Tests created/executed **0**, **DEFERRED / NOT VERIFIED**. Foundation/future payload handlers unavailable, source maps optional. Stop CMP-10.

## RUN-01 — Runtime Artifact Loader

Pure bounded runtime coordinator with explicit trusted authorization, complete digest-verified CMP-07/08/09 source integration, immutable decoder approvals/representations, compatibility/dependency diagnostics and atomic inactive results. New tooling bridge preserves runtime independence; no real format/decoder or authority is invented. No HTTP endpoint or ORM. [Contract and conceptual Mini Sales](docs/runtime/runtime-artifact-loader.md), [ADR-0042](docs/architecture/decisions/ADR-0042-runtime-artifact-loader.md), [static completion report](docs/architecture/run01-verification.md). [188 deferred cases](test-archive/RUN-01/RUN-01-deferred-tests.md), executable tests created/executed **0**, **DEFERRED / NOT VERIFIED**. Stop RUN-01.

## RUN-02 — Runtime Model Registry

Pure application-owned in-memory registry with original RUN-01 evidence, explicit definition extraction/registration/inspection authority, exact scoped semantic versions, atomic locked copy-on-write updates, immutable snapshots, bounded name/version inspection and conflict diagnostics. No default registry, implicit latest, decoder, authority, activation, ORM or endpoint. [Contract and conditional Mini Sales](docs/runtime/runtime-model-registry.md), [ADR-0043](docs/architecture/decisions/ADR-0043-runtime-model-registry.md), [completion record](docs/architecture/run02-verification.md). [198 deferred cases](test-archive/RUN-02/RUN-02-deferred-tests.md), executable tests created/executed **0**, **DEFERRED / NOT VERIFIED**. Stop RUN-02.

## RUN-03 — Semantic Instance Runtime

Pure Python application-owned create/update/inspect orchestration consumes original exact RUN-02 entries, existing FieldId/presence/nullability/constraint semantics and explicitly approved authoritative TYPE-08 ports. New immutable states preserve ID/version/context, with local expected revisions and independently bound permissions. Actual TYPE-08/schema/decoder/authority integrations are **unavailable**: defaults fail closed, no canonical instance/sentinel/decoder or successful demo is fabricated. No persistence/ORM/endpoint/activation/action/event/workflow. [Contract and conditional Mini Sales](docs/runtime/semantic-instance-runtime.md), [ADR-0044](docs/architecture/decisions/ADR-0044-semantic-instance-runtime.md), [source/completion record](docs/architecture/run03-verification.md), [200 deferred cases](test-archive/RUN-03/RUN-03-deferred-tests.md). Tests created/executed **0**, **DEFERRED / NOT VERIFIED**. Stop RUN-03; RUN-04 not started.
