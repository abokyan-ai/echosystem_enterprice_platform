# MOD-04 — Canonical Model Contract

Date: 2026-10-10 (Asia/Riyadh). Pure Python domain implementation. Behavioral status: **NOT_RUN — DEFERRED / NOT VERIFIED**. No model construction/example or test case was executed.

## Assessment of actual foundations

Kernel implements typed SemanticElementId, QualifiedName/Namespace, explicit SemanticContextRef, SemanticElement five-property protocol, SemanticElementKind, numeric SemanticVersion, ElementRef/ElementVersionRef, primitives and Facet base. model-core implements immutable fields/DataFacet/constraints, closed TYPE-05 references, independent TYPE-06 validation and TYPE-07 version catalog. MOD-01/02/03 own authoring structure, source acquisition/decoding and auxiliary source positions.

**Production TYPE-01 TypeDefinition is absent.** The existing TypeDataComposition is the actual public host/DataFacet carrier, not a complete TypeDefinition. Its host may initially be an external mutable SemanticElement protocol object. TYPE-07 already has a frozen private five-value host capture and exact immutable nested-value admission helper. MOD-04 reuses those existing helpers/carrier rather than creating a duplicate canonical TypeDefinition or copying fields into a new canonical definition class. The exposed supported seam consists only of those five root values plus current optional DataFacet. Extra arbitrary host attributes and unsupported/future facets are outside that existing seam, not advertised as preserved complete semantic content. Full TYPE-01 reconciliation remains mandatory before claiming complete type-definition modeling.

**General SK-11 is absent.** Reuse current TypeValidationSeverity.ERROR and TypeValidationPath semantics, with a narrow intrinsic CanonicalConstructionDiagnostic analogous to the established TYPE-07 diagnostic seam. This does not implement a second general Diagnostic model or claim full SK-11 integration. TYPE-08 and full SK-09 remain incomplete. Those gaps are explicit architectural dependencies, not reasons to invent instances/ontologies.

Local read-only distribution inspection: Python 3.12.14; PyYAML 6.0.3; Django and djangorestframework absent. Supported repository baseline remains Python 3.11+. No existing Django project/canonical HTTP API/view/serializer requires modification. No dependency/version upgrade, endpoint, DRF Serializer, Django ORM model, migration or database is added. Future HTTP presentation must use the already approved Django/DRF adapter boundary.

## Domain ownership and supported membership

Canonical contracts are defined in existing model_core.public, their actual domain owner. No new module, dependency edge, authoring/parser/tooling dependency, framework import or inventory count is added. Runtime still cannot import model-core. Future compilation/validation consumers can use this public semantic contract without parsing authoring documents. No existing semantic value class is redefined.

CanonicalModel is a context-scoped aggregation root with only `scope` and immutable `definitions`; it is not automatically a SemanticElement. It has no model ID, version, source path, tenant/org, arbitrary metadata, compiler method or persistence identity.

`CanonicalDefinition` is the explicit v0 closed payload alias to the existing TypeDataComposition. `CANONICAL_DEFINITION_KINDS` currently contains only the actual supported type-definition kind. Bare SemanticElement protocol objects, authoring declarations, source text/maps and unsupported kinds are not canonical payloads. The root's typed membership vocabulary is intentionally explicit; future definition kinds require an actual owned semantic contract and explicit alias/kind/admission extension, not arbitrary duck typing or a plugin/global registry. No unsupported action/event/policy/capability definition is invented. This is not a promise that the missing full TypeDefinition exists.

## Scope, exact versions and immutable construction

Scope is one exact canonical SemanticContextRef, consistent with TYPE-07. Each captured member context must equal it. No rewrite/inference from namespace/path/tenant/org/route occurs. Multiple exact versions of one identity are allowed **only when explicitly provided by the caller**. Membership does not import all registry versions or references. Bare IDs and qualified names never select a latest/default version.

CanonicalModelFactory.create(scope, definitions) accepts a plain tuple/list of already constructed supported domain members (empty is valid) and returns CanonicalModelConstructionResult. It executes only intrinsic admission, scope, equality/name collision and index invariants. It does not invoke TypeRegistry.register, TypeValidator, a parser, name resolver, canonicalizer or compiler. No concrete registry is constructed/wrapped/inherited. Direct CanonicalModel(scope, definitions) runs the same intrinsic boundary and raises CanonicalModelConstructionError with the exact typed diagnostics on expected failure; the factory converts only that expected exception to a result. Unexpected implementation/property-getter exceptions propagate rather than masquerading as successfully handled input errors.

The existing TYPE-07 capture helper reads each host identity/name/context/kind/version property once into its already established frozen value. Existing deeply immutable DataFacet, FieldDefinition, FieldId, FieldName, TypeRef and constraint objects are reused/shared, with exact-class admission rejecting mutable/noncanonical nested variants. None facet remains distinct from an empty DataFacet. Input collection is defensively copied; frozen host/data compositions detach successful models from later external host mutation. This captures the current protocol boundary, not a synchronized atomic read of concurrently mutating arbitrary hosts or unknown facets. Future TYPE-01 immutable definitions should replace the provisional seam through an explicit compatible contract decision.

All candidates are checked before a model is returned. Any diagnostic means model=None, no partial success and no mutation of existing models/registries/input collections. Direct construction cannot bypass intrinsic checks. Creating a different immutable membership collection yields a new model; the old model remains unchanged. No mutable setters/register/remove/cache are implemented.

## Ordering, lookup, collision policy and equality

Canonical definitions sort by `SemanticElementId.value` using ordinal Python scalar order, then by the existing numeric SemanticVersion comparison. Version 1.2.0 precedes 1.10.0. One context removes the need to include context in the per-model ordering key. No authoring/filesystem/input order, insertion-order dependence, locale or random ID controls canonical contents.

A private MappingProxyType over an owned exact-reference map provides deterministic read-only membership lookup. Public behavior:

- `find(ElementVersionRef)` returns existing TypeDataComposition snapshot or None.
- `contains(ElementVersionRef)` checks exact membership.
- `list_definitions()` returns the canonical immutable tuple.
- `references` returns canonical ordered exact references.
- `same_membership(other)` compares scope and selected exact references only.
- `same_supported_content(other)` compares scope and the complete **currently supported host/data seam**.

Bare SemanticElementId/ElementRef/name/string lookup is programmer misuse and raises TypeError; unknown valid exact reference yields None. No by-name resolution or ambiguous bare-ID convenience is introduced. A type host is accessible through returned composition.type_definition; returning an invented production TypeDefinition is not claimed.

| Candidate relationship | Policy |
| --- | --- |
| Same ID/version, equal supported content | Idempotent: one member |
| Same ID/version, different supported content | Reject exact conflict |
| Same ID, different versions | Keep every explicitly supplied exact version |
| Different IDs, same QualifiedName in selected scope | Reject ambiguous name ownership |
| Same ID renamed across selected versions | Preserve identity and both version-specific names |
| Wrong semantic context | Reject without rewrite |
| Unsupported kind/carrier | Reject closed membership vocabulary |
| Unknown exact lookup | None |

Collision/equality policies reuse TYPE-07's current capture/nested equality semantics. Name ownership here covers only explicit canonical membership. TYPE-07 may retain historical names of versions omitted from this selected snapshot; MOD-04 does not consult/reserve unselected registry history. That difference follows selected membership versus version-catalog responsibility, not a different semantic identity rule. Field-level order/content remains the existing DataFacet/constraint equality semantics; MOD-04 does not re-sort internal fields or rewrite references.

Dataclass model equality compares scope and supported canonical content, with indexes excluded; same membership alone does not prove same content. Unsupported host/facet semantics and canonical serialized bytes are not covered. Object addresses/repr are never semantic comparison keys. CanonicalModel deliberately has no hash contract; no serialized content digest or snapshot-version identity is invented.

## References, source locations and semantic judgment

Existing PrimitiveTypeRef/SemanticTypeRef are preserved unchanged. TYPE-05 semantic references are identity-only ElementRef, while model membership keys are exact ElementVersionRef. MOD-04 does not silently upgrade field references to versions or choose a target from multiple selected versions. A future explicitly scoped resolver/validator/compiler must define any required exact binding.

Self/cyclic/external/missing-target references are retained as structurally typed values; no graph traversal, recursive membership expansion or global target-existence verdict occurs. Absence from selected membership is not proof of global invalidity. Unresolved authoring strings/name expressions cannot masquerade as TypeRef or canonical members. Constraint applicability remains TYPE-06, separate from construction. Intrinsic consistency is not complete semantic verification.

Physical source positions and MOD-03 indexes stay outside model/definition identities and this domain package. A later transformation may associate exact ElementVersionRef with separate SourceLocation metadata through an application-owned adapter; no source-map propagation engine or cross-zone reverse dependency is introduced now. The root contains no universal metadata bag or mandatory tenant/organization/provenance/audit fields. Source associations, semantic content equality and provenance authority remain separate.

## Intrinsic diagnostics

| Code | Category |
| --- | --- |
| MOD-CANON-001 | Invalid/missing explicit scope |
| MOD-CANON-002 | Unsupported membership input collection |
| MOD-CANON-003 | Unsupported definition carrier/kind |
| MOD-CANON-004 | Invalid typed host or noncanonical mutable nested values |
| MOD-CANON-005 | Context mismatch |
| MOD-CANON-006 | Conflicting exact identity/version content |
| MOD-CANON-007 | Qualified-name ownership collision |

Diagnostic fields are closed typed values: code/message, exact reference/name/context, zero-based candidate input index and optional related exact reference/input index. Severity reuses current ERROR; path reuses TypeValidationPath when a canonical qualified name exists. No physical coordinate is fabricated. Failure diagnostics are deterministic for a fixed input sequence, in candidate order with exact-content conflict before name conflict. Input indices intentionally follow caller order; they are not semantic ordering or edit-stable IDs. Scope/collection invalidity yields its root failure and does not interpret candidates. Success always has no diagnostics; failure has at least one and no model.

## Mini Sales design usage (documentation only, NOT RUN)

Assume a caller already supplies the existing Customer TypeDataComposition with explicit sem_ UUID-v4 identity, sales.Customer, semantic context, version 1.0.0 and existing DataFacet fields name/active/creditLimit. Each field retains real fld_ IDs, FieldName, closed TypeRef, presence/nullability and typed constraints. The full TypeDefinition prerequisite is missing, so this example targets the actual provisional composition rather than fabricating a new semantic class/fixture. No authoring source is parsed or transformed here.

```python
# Illustration only; Customer compositions must already exist in domain code.
from model_core.public import CanonicalModelFactory
from semantic_kernel.public import ElementVersionRef
result = CanonicalModelFactory().create(sales_context, (customer_v1, customer_v11))
if result.model is not None:
    selected = result.model.find(ElementVersionRef(customer_id, customer_v1.type_definition.version))
    # Both explicitly supplied versions remain separate; never latest/default.
```

This is not an executed demo or authoring-to-canonical algorithm. Both 1.0.0 and 1.1.0 can coexist; a different-ID Customer name conflicts, and a same-ID later renamed version retains identity/name history for selected members. Source metadata can change separately without affecting semantic membership. No registry registration, Customer database table, Django model, CRUD endpoint or instance is created.

See [ADR-0026](../architecture/decisions/ADR-0026-canonical-model-contract.md), [single detailed deferred specification](../../test-archive/MOD-04/MOD-04-deferred-tests.md) and [static record](../architecture/mod04-verification.md). Contracts are ready for later pipeline design with missing foundations and deferred behavioral correctness explicit. Stop at MOD-04; no MOD-05.
