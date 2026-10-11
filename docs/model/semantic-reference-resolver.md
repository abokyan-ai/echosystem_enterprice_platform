# MOD-07 — Semantic Reference Resolver

Date: 2026-10-11 (Asia/Riyadh). Implemented for actual supported contracts. Behavioral verification: **NOT_RUN — DEFERRED / NOT VERIFIED**. No resolution, document readiness, binding, example or source attachment scenario was executed.

## Repository assessment

Pure resolution lives in the existing model-authoring module and reuses MOD-06 without altering its namespace precedence, alias semantics, visibility indexes or request/result contracts. Existing Kernel ElementRef/ElementVersionRef and semantic kinds/context remain authoritative. TYPE-05 SemanticTypeRef still accepts only ElementRef. MOD-05 owns final field/reference/facet/definition construction and canonical assembly.

Python metadata: 3.12.14, existing PyYAML 6.0.3; Django/djangorestframework absent. Source conventions contain no applicable model-authoring DRF endpoint. No API, serializer, ORM entity/migration, database or framework upgrade is added. Domain code stays framework-independent; future applicable HTTP transport must use DRF with existing authentication/permissions and explicit diagnostic presentation.

Full TYPE-01, general SK-11, TYPE-08/full SK-09 remain architectural gaps. Current diagnostics reuse actual severity/source-path/namespace diagnostics via a narrow MOD-REFERENCE seam, not a fabricated general Diagnostics Model. No instance-reference class or cross-language migration is introduced.

## Explicit requirements and requests

SemanticReferenceRequirement separates expected_kind, ReferenceVersionRequirement (IDENTITY_ONLY / EXACT_VERSION), and ReferenceConsumer (SEMANTIC_DEFINITION / SEMANTIC_TYPE_FIELD). The default consumer is a general semantic definition. Type-field consumer explicitly requires existing TYPE_DEFINITION kind. No version range/latest/current/default/preferred/highest policy is supported.

SemanticReferenceResolutionRequest contains the existing MOD-06 expression variant, explicit context, requirement, optional exact_version and optional AuthoringSchemaPath. Constructors reject untyped dictionaries, primitive/instance/unknown expression variants, invalid nested values and unsupported requirement tokens. Ordinary supported unresolved targets return diagnostics, while developer contract misuse raises existing TypeError/value-object errors.

An identity-only requirement rejects any authored/requested exact pin; it cannot silently downgrade it. An exact requirement needs either an explicit request pin or the existing authored ElementVersionRef expression. Conflicting request/authored pins are delegated to MOD-06 and retain its diagnostic. Exact requirements without a pin fail MOD-REFERENCE-009, even if only one version exists.

## MOD-06 delegation and evidence

SemanticReferenceResolver is a frozen service with explicit actual NamespaceResolver dependency. Every supported semantic name/alias/identity/exact expression delegates to that service. No second parser, namespace search, alias expansion, precedence engine or foreign-context lookup is implemented. Identity expressions remain identity-based under MOD-06, never substituted through names.

MOD-06 failure diagnostics are retained whole inside SemanticReferenceDiagnostic.namespace_diagnostic, with bounded mapped MOD-REFERENCE codes and original request. Candidate IDs/names/versions, delegated code/message/path/related paths remain available. Ambiguity remains an error before kind/version filters can choose an identity. Missing visibility is not treated as known existence.

ReferenceTargetEvidence holds an existing versioned SemanticSymbol and explicit LOCAL_DECLARATION / VISIBLE_SYMBOL origin. Evidence is drawn only from the immutable environment's declared collections and must match resolved identity/context/expected kind/matching names and any exact pin. Reference success needs nonempty evidence. Several visible versions establish identity existence without selecting any one as canonical target. No target definitions/facets/field graphs are embedded or recursively validated.

VISIBLE_SYMBOL intentionally does not claim registered authority: symbols may be supplied through an actual selected TYPE-07 adapter or another explicitly approved source. Local symbols need actual stable ID, kind, context, exact declared version and QName; a name-only placeholder is not accepted. Caller owns the truth/authority of supplied declaration/lookup evidence. A typed binding is a bounded resolution record, not a security or enterprise provenance certificate.

ResolvedReferenceBinding retains the approved reference, requirement/context, sorted immutable evidence and original occurrence path. It enforces version-form agreement, nonempty coordinate-consistent evidence and current type-field reference representation. It has no mutable maps, generated IDs, source line/column, arbitrary metadata, runtime instance or database foreign key.

## Identity versus exact compatibility

Identity-only success returns ElementRef even with several visible versions. Exact general-definition success returns only the explicitly verified ElementVersionRef. Missing exact coordinates fail MOD-REFERENCE-007; no fallback, compatibility substitution or range interpretation occurs.

A verified exact reference requested for SEMANTIC_TYPE_FIELD fails MOD-REFERENCE-008 because current TYPE-05 cannot represent that pin. The diagnostic retains the verified exact target rather than discarding its version. Target existence/kind/exact verification happens first; a missing exact target still reports the actual target/version failure. General exact definitions remain supported independently of current field canonicalization.

Final SemanticTypeRef construction remains in MOD-05. MOD-07 returns verified references and the existing authoring bindings, not canonical TypeRefs, fields, DataFacets, TypeDefinitions or CanonicalModel. Primitive authoring expressions bypass semantic/name resolution entirely when preparing a document; the Canonicalizer later converts their existing approved vocabulary.

## Local and registered targets

Use existing local_authoring_symbols to predeclare a complete document before resolving fields. Local forward, self and mutual references do not require registration or definition construction. Symbol ownership/conflicting kind/context/name coordinates remain checked by the existing MOD-06 environment factory. Minimal coordinate evidence cannot compare full target field content; full definition conflict and semantic applicability remain later responsibilities.

External type contribution uses the actual existing TypeLookupSymbolAdapter and TYPE-06 TypeLookup port. Caller supplies explicit identity selections and stable immutable TYPE-07 bound views; capture failures are not silently ignored. Several explicit views may contribute different versions of one identity. The resolver holds no concrete registry and requests do not call live ports, enumerate hidden catalogs, mutate/register targets or implicitly bind versions. A plain multi-version lookup still requires caller-supplied binding; no version is chosen solely to prove identity.

Cross-context visibility is unsupported by the current MOD-06 v0 environment. Request/document context mismatch returns explicit diagnostics. No extra allowed-context/security rule is fabricated. Semantic context is not tenant/organization and visibility grants no authority.

## Finite batches and whole-document readiness

resolve_many(requests, environment) copies a typed finite ordered sequence and returns SemanticReferenceBatchResult preserving one result per request in input order. Status is ALL_RESOLVED, PARTIALLY_RESOLVED or NONE_RESOLVED. Empty batch is vacuously ALL_RESOLVED. Successful partial bindings remain available inside an explicitly incomplete batch; no failed request is omitted. Diagnostics flatten in request order with MOD-06's deterministic candidate ordering. Original occurrence paths distinguish repeated text; no object-memory address is a persistent key.

all_required_bindings_satisfied is a condition for that supplied batch only, not proof that every model occurrence was supplied. canonicalizer_compatible additionally requires all successes to use the type-field consumer and ElementRef. A complete generic exact batch can be valid reference resolution while incompatible with current field canonicalization.

resolve_document(document, environment, retain_source_associations=True) prepares the actual existing ResolvedAuthoringModel. The document must use current MOD-01 schema, matching context/current namespace, and each declaration must have matching explicit local ID/name/kind/version evidence. No unrelated documents are merged, no sources/imports are loaded and no environment is mutated.

The operation enumerates all source fields once. Primitive fields get existing ResolvedFieldBinding with target=None and never enter NamespaceResolver. Semantic field requests use explicit type-field requirements, retain source occurrence paths, and resolve as one finite batch. Exact authored field pins retain exact intent and fail current representation compatibility. Every definition and every field receives its existing typed binding only when all required references and local coordinates are satisfied.

ResolvedAuthoringInputResult contains the complete existing ResolvedAuthoringModel or diagnostics, plus the batch for partial reporting. Its invariant checks exact declaration/field coverage, stable authored IDs/versions/context/names/FieldIds, primitive bypass, corresponding verified semantic occurrence paths/targets and absence of extra/missing batch occurrences. Failure exposes no partial successful ResolvedAuthoringModel. ready_for_canonicalization means reference-binding completeness, not full schema/TYPE-06/model semantic validity: later MOD-05 intrinsic construction and validation may still reject structural/semantic content.

Evidence indexing is local to each single operation/batch, built once per batch. Work is bounded by supplied declarations/fields/symbols and matching versions plus deterministic sorting. No graph closure, recursion, caching singleton, network discovery or reference target expansion is introduced.

## Diagnostics and actual physical source locations

Stable MOD-REFERENCE-001..012 codes cover invalid request/environment, missing/ambiguous target, context/kind/version failures, incompatible form, missing explicit pin, invalid local evidence, conflicting evidence and missing required binding categories. Whole namespace diagnostics remain intact; request records expose authored form/requirements/context/pin and source path. Known exact target coordinates stay in incompatibility diagnostics.

Existing tooling provides LocatedSemanticReferenceDiagnostic and locate_semantic_reference_diagnostics(diagnostics, loaded). It uses actual MOD-03 SourceLocationIndex/SourceNodePath conversion and exact lookup for primary/delegated related paths. Missing path/index/node remains None; no fabricated coordinates or nearest-node fallback. Single, batch and readiness diagnostics use the same presentation helper. Source metadata stays external to ElementRef and canonical semantic identity.

Caller must pair the original loaded document with request/local declaration paths; external symbols normally lack that document's path. This helper cannot prove cross-document provenance or identify wrong same-shaped sources. Unexpected lookup/service programming errors are not blanket-swallowed into ordinary missing-target outcomes.

## Mini Sales Employee/Department example — not executed

New production usage example `examples/authoring/mini-sales-references.json` extends the established sales context with Department declared before Employee. Department.manager uses semantic-name Employee; Employee.manager uses qualified sales.Employee and is a self-reference; Customer.name is primitive and bypasses reference resolution. IDs comply with actual Kernel sem_<UUIDv4>/fld_<UUIDv4> grammar; conceptual typ_employee_123 is not used. Original Mini Sales files are preserved.

The following is unexecuted documentation. Assume `loaded` is an existing successful LoadedAuthoringDocument for the new example; loading itself is upstream, not performed by MOD-07.

```python
from semantic_kernel.public import Namespace, SemanticVersion, SemanticElementKinds
from model_authoring.public import (
    local_authoring_symbols, NamespaceEnvironmentFactory,
    SemanticReferenceResolver, SemanticReferenceRequirement,
    SemanticReferenceResolutionRequest, ReferenceVersionRequirement,
    AuthoringNameExpression,
)
from model_loader.public import locate_semantic_reference_diagnostics

symbols = local_authoring_symbols(loaded.document)
if symbols.is_success:
    visibility = NamespaceEnvironmentFactory().create(
        loaded.document.context, Namespace.parse('sales'), local_symbols=symbols.symbols,
    )
    if visibility.is_success:
        resolver = SemanticReferenceResolver()
        prepared = resolver.resolve_document(loaded.document, visibility.environment)
        # prepared.resolved_model is the existing MOD-05 input when ready.
        locations = locate_semantic_reference_diagnostics(prepared.diagnostics, loaded)
        exact = resolver.resolve(
            SemanticReferenceResolutionRequest(
                AuthoringNameExpression('Employee'), loaded.document.context,
                SemanticReferenceRequirement(
                    SemanticElementKinds.TYPE_DEFINITION,
                    ReferenceVersionRequirement.EXACT_VERSION,
                ),
                exact_version=SemanticVersion.parse('1.0.0'),
            ),
            visibility.environment,
        )
```

Expected design meaning: both manager fields retain identity-only Employee references, including forward/self use; Customer primitive skips semantic lookup. Generic exact Employee@1.0.0 returns that coordinate, never substitutes 1.1.0. A field requiring exact pin receives current TYPE-05 incompatibility. A visible non-type manager target fails kind checking. No Canonicalizer call or resulting canonical model is observed/executed here.

## Deferred verification and readiness

[Detailed deferred archive](../../test-archive/MOD-07/MOD-07-deferred-tests.md) records future positive/negative/failure/boundary/integration cases. Tests implemented/executed: 0. [Separate static record](../architecture/mod07-verification.md) does not establish semantic correctness. Current supported reference boundary and complete existing authoring-input integration are ready for review and later authorized verification within the declared gaps. Stop after MOD-07; no MOD-08.
