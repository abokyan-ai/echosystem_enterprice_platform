# MOD-06 — Namespace Resolver

Date: 2026-10-10 (Asia/Riyadh). Current supported resolution contracts implemented. Behavioral verification: **NOT_RUN — DEFERRED / NOT VERIFIED**. No resolver, symbol-capture, binding-bridge or example scenario was executed.

## Repository assessment and ownership

Pure name resolution is a separate public operation in the existing model-authoring module. It reuses the Kernel's Namespace, QualifiedName, SemanticContextRef, SemanticElementKind, SemanticVersion, ElementRef and ElementVersionRef, the actual TYPE-07 TypeLookup port and the existing MOD-05 ResolvedFieldBinding. No new module/dependency/profile/activation marker is introduced. The resolver does not invoke the Canonicalizer or create definitions, facets, fields, registries or canonical models.

Actual stack metadata: Python 3.12.14, existing PyYAML 6.0.3; Django and djangorestframework are absent. Source inspection found no existing applicable DRF model-authoring endpoint. No HTTP API, ORM model/migration, serializer, database or framework upgrade is added. Future applicable HTTP presentation must use the established DRF boundary and authentication/permissions, outside domain resolution.

General SK-11 and full TYPE-01 remain missing; the narrow NamespaceResolutionDiagnostic reuses actual severity and authoring source-path conventions without claiming a completed general diagnostics model. TYPE-08/full SK-09 remain incomplete. Existing Python contracts are retained; no TypeScript/Angular interface migration is undertaken.

## Symbols and immutable visibility

SemanticSymbol contains an existing context, qualified name, exact ElementVersionRef, semantic kind and optional original AuthoringSchemaPath. It records declared coordinates, not a duplicated SemanticElement/TypeDefinition or definition content. No facets, field values, persistence/UI/API/runtime metadata or arbitrary map is stored.

NamespaceResolutionEnvironment contains explicit context, current_namespace, local_symbols, visible_symbols, aliases and search_namespaces. Collections are copied to deterministic tuples; internal name/identity/alias maps are owned MappingProxyType values with tuple members. The environment retains no live lookup port. Symbols and aliases must use exact existing immutable value classes. Intentional corruption of frozen values/monkeypatching is outside the public contract.

V0 permits only a single semantic context. Foreign-context symbols cause a structured environment failure rather than becoming implicitly visible. There is no cross-context opt-in syntax in the existing architecture. Semantic visibility is not authorization, tenancy, organization membership or runtime deployment.

Local and explicitly visible symbols have equal standing; neither overrides the other. The same exact identity/version must have one name and kind; one stable identity must have one kind across versions. Distinct identities cannot own one qualified name across the explicitly supplied versions. NamespaceEnvironmentFactory returns typed diagnostics and no snapshot on those domain conflicts, while direct construction raises NamespaceEnvironmentError carrying the same diagnostics. Wrong raw payload types are developer misuse and raise TypeError.

Same-identity versions may have renamed qualified names. Same exact metadata contributed by both sources is idempotent; distinct source paths can remain visible for diagnostics. Full definition content conflicts cannot be detected from these minimal symbol records and remain owned by MOD-04/TYPE-07 construction. The resolver enforces name ownership within the selected visible snapshot; unseen TYPE-07 history remains governed by registry registration, never inferred or fetched globally.

`local_authoring_symbols(document)` projects existing declared IDs, versions, context and document-namespace/local-name coordinates into symbols before field binding or registration. It uses existing parsers, generates no IDs and does not read/construct field graphs. It returns an atomic NamespaceSymbolSnapshotResult; source declaration paths are retained. It rejects unsupported root/schema shape. Symbol ownership is checked when building the environment.

## Requests and resolution semantics

NamespaceResolutionRequest has expression, explicit context, optional expected_kind, optional exact_version and optional source path. NamespaceResolver.resolve(request, environment) returns NamespaceResolutionResult with one ResolvedSemanticTarget or nonempty typed diagnostics. Raw/unsupported request or environment roots fail through MOD-NAMESPACE-001/002. Constructors reject malformed typed payloads and invalid name syntax through the existing value contracts before ordinary resolution.

Supported variants are existing AuthoringNameExpression, AuthoringIdentityExpression and AuthoringVersionExpression, plus an explicit resolver-only AliasQualifiedNameExpression. Primitive expressions are not names and are rejected at the request contract. MOD-01 decoded schema syntax remains unchanged.

1. Identity expressions bypass qualified-name re-resolution, but still require explicitly visible identity/context and kind/version safeguards.
2. Explicit AliasQualifiedNameExpression expands exactly one declared direct alias and performs scoped lookup.
3. An ordinary dotted AuthoringNameExpression performs exact qualified-name lookup, never alias interpretation.
4. An unqualified AuthoringNameExpression composes existing QualifiedName values in the current namespace plus explicitly supplied search_namespaces.

Current namespace is always included in local-name search; extra namespaces must be supplied explicitly. All matches have equal standing. A default current-namespace-only environment can resolve Customer in sales even if unrelated visible namespaces exist. If sales and crm are both explicitly searchable and contain different Customer identities, ambiguity fails closed. No wildcard import, first-match, local-over-registry shadowing, shortest-name, alphabetical choice or hidden fallback exists. Qualified lookup can use any explicitly supplied symbol namespace within the same context, regardless of local-name search list.

Candidate tuples sort by ID scalar, numeric SemanticVersion, qualified-name text, kind and source-path text. Input-order permutations of equivalent symbols/aliases/search namespaces do not select a different target or alter diagnostic ordering. Source paths never select semantic identity.

## Aliases

NamespaceAlias uses a single canonical Namespace segment as alias and a concrete Namespace target, scoped to this environment. No alias-to-alias reference variant exists. Equal duplicate targets are idempotent; conflicting targets produce MOD-NAMESPACE-006, identifying the alias/targets and source declaration paths when supplied.

Ordinary `AuthoringNameExpression('crm.Customer')` means the real crm namespace. Only `AliasQualifiedNameExpression(Namespace.parse('crm'), 'Customer')` uses an explicitly supplied alias. This internal capability does not extend MOD-01's accepted JSON/YAML schema or fabricate a discriminator from source text. It never overrides an unrelated qualified name. Unknown aliases fail MOD-NAMESPACE-005 even if a real namespace with that name exists. No global aliases, wildcard aliases, automatic aliases or historical-name aliases are created.

Alias targets always mean concrete namespaces. An alias whose target has the same spelling as another alias is not recursively expanded; even mappings a→b and b→a are direct concrete namespace targets, not an alias graph. Alias-chain/cycle traversal is therefore inapplicable in v0; no recursive chain syntax is accepted or evaluated. Alias names do not leak into ElementRef/ElementVersionRef or canonical semantic identity.

## Identity, exact versions and renamed names

Without an exact requirement, a unique stable identity resolves to ElementRef even when many declared versions match. No version is chosen or placed in the target. ResolvedSemanticTarget includes context, kind and the deterministic tuple of matching qualified_names. Explicit ID lookup can retain several recorded names across versions rather than declaring one arbitrary current name.

An exact_version request or existing AuthoringVersionExpression must find that exact coordinate among the visible candidates. It returns ElementVersionRef without changing its pin. A conflicting request pin and authored pin fails MOD-NAMESPACE-001. Missing exact version fails MOD-NAMESPACE-009; no latest/default/preferred/compatibility selection is attempted. A name at an older declared version does not act as a permanent alias for a renamed newer version: exact name/version matching must be present explicitly.

Ambiguity between identities is evaluated before expected kind/exact version; neither filter is an implicit identity selection policy. Kind mismatch is MOD-NAMESPACE-008, not conversion to TYPE_DEFINITION. Missing name/identity is MOD-NAMESPACE-003. Candidate identities/names/versions and request context/expression/pin/source path are preserved in relevant diagnostics.

Forward/self/mutual references work because declared coordinates are visible before definitions are constructed. Each request resolves one target. No recursive reference graph traversal, target construction or cycle rejection occurs.

## TYPE-07 adapter

TypeLookupSymbolAdapter accepts the existing read-only TypeLookup abstraction and captures only caller-supplied ElementRef selections under an explicit context. It snapshots the five existing host values once per selected identity, verifies canonical nested values, requested identity, context and type-definition kind, then returns minimal immutable symbols. The actual TYPE-07 port has no name/version enumeration API; the adapter does not invent a universal registry abstraction or enumerate global visibility.

A caller may supply an existing TypeRegistryLookup produced externally from explicit exact selections. If a plain multi-version TypeLookup raises TypeRegistryAmbiguityError, capture returns MOD-NAMESPACE-011 with TYPE-REG-006 and the selected identity, never binds a version itself. To expose several versions of one ID, the caller may combine symbol snapshots captured from separately and explicitly bound views. Any missing/invalid/context/kind/ambiguous capture returns diagnostics and no partial symbol tuple. Unexpected port implementation errors remain visible.

Lookup port purity/stability is a caller contract. The adapter has no mutation operation, but cannot prevent side effects in a malicious/custom port implementation or synchronize a mutable port. Use actual immutable TYPE-07 bound snapshots. Resolver requests themselves consult only the frozen environment and never call a live port.

## MOD-05 bridge and source locations

`bind_namespace_target(result, facet_index, field_index, field_id)` produces the existing ResolvedFieldBinding through NamespaceFieldBindingResult. It does not create a second reference-binding representation, choose the field's identity, build the entire resolved model or invoke canonicalization. Failure diagnostics propagate; non-type targets fail kind validation. Source coordinates and stable FieldId are supplied explicitly.

Identity-only results are directly compatible with current TYPE-05/MOD-05 semantic fields. Exact results remain exact in ResolvedFieldBinding: current Canonicalizer will reject such field pins until TYPE-05 can represent them. This is a documented downstream representation gap, not permission to downgrade them. Definition ResolvedTypeBinding/ResolvedAuthoringModel orchestration remains with the caller/future reference-binding stage. MOD-07 is not implemented.

Physical location presentation lives in the existing tooling module. `locate_namespace_resolution(result, loaded)` returns NamespaceResolutionSourceLocations and LocatedNamespaceResolutionDiagnostic using actual MOD-03 SourceLocation values. `locate_namespace_diagnostics(diagnostics, loaded)` also presents environment/capture/bridge diagnostics without wrapping them as successful resolution. It attaches expression and diagnostic primary/related paths by exact lookup. Missing index/path/node remains None; related positions preserve missing entries. Domain diagnostics are retained unchanged. No parsing, loading, resolution rerun, fabricated coordinates or nearest-node fallback occurs.

Caller must pair the original loaded document with request/local declaration/alias paths. External registry symbols normally have no source path. Same-shaped cross-document inputs cannot be provenance-certified by this helper. No source location establishes identity or grants authority; no full provenance graph is claimed.

## Mini Sales usage — documentation only, not executed

Existing Mini Sales files use Kernel-compliant identities: Customer is sem_550e8400-e29b-41d4-a716-000000000001@1.0.0 and scope is sem_550e8400-e29b-41d4-a716-999999999999. Conceptual typ_customer_123/sales-context placeholders are not valid repository IDs. The existing JSON/YAML examples remain unchanged.

The following assumes `loaded` is the existing successful LoadedAuthoringDocument for Mini Sales. It is unexecuted usage documentation, not a test or observed result.

```python
from semantic_kernel.public import Namespace, SemanticVersion, SemanticElementKinds
from model_authoring.public import (
    local_authoring_symbols, NamespaceEnvironmentFactory, NamespaceResolver,
    NamespaceResolutionRequest, AuthoringNameExpression,
)
from model_loader.public import locate_namespace_resolution

symbols = local_authoring_symbols(loaded.document)
environment_result = NamespaceEnvironmentFactory().create(
    loaded.document.context, Namespace.parse('sales'), local_symbols=symbols.symbols,
)
if symbols.is_success and environment_result.is_success:
    request = NamespaceResolutionRequest(
        AuthoringNameExpression('Customer'), loaded.document.context,
        expected_kind=SemanticElementKinds.TYPE_DEFINITION,
    )
    result = NamespaceResolver().resolve(request, environment_result.environment)
    exact = NamespaceResolver().resolve(
        NamespaceResolutionRequest(
            AuthoringNameExpression('sales.Customer'), loaded.document.context,
            expected_kind=SemanticElementKinds.TYPE_DEFINITION,
            exact_version=SemanticVersion.parse('1.0.0'),
        ),
        environment_result.environment,
    )
    source_locations = locate_namespace_resolution(result, loaded)
```

Expected design outcome: identity-only Customer returns ElementRef without inferred version; exact Customer@1.0.0 returns ElementVersionRef. Even if 1.1.0 is explicitly visible, 1.0.0 remains exact. Local Employee self-reference resolves its predeclared identity without registration. A resolver-only crm→customer_management alias uses AliasQualifiedNameExpression and a supplied visible symbol; ordinary crm.Customer continues to mean the real namespace. Adding two searchable Customer identities yields explicit ambiguity.

## Deferred verification and readiness

[Detailed archive](../../test-archive/MOD-06/MOD-06-deferred-tests.md) holds future positive/negative/collision/boundary/integration scenarios; no automated tests are created or executed. [Implementation/static record](../architecture/mod06-verification.md) separates syntax/build/dependency evidence from behavioral verification.

Current name-resolution and minimal binding compatibility are implemented within explicit v0 scope. Full SK-11/TYPE-01, stronger cross-document provenance, cross-context semantic visibility and richer alias schema remain separate gaps. Exact field pins remain incompatible with current TYPE-05 canonicalization. Stop at MOD-06; do not start MOD-07 automatically.
