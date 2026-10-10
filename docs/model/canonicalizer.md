# MOD-05 — Canonicalizer

Date: 2026-10-10 (Asia/Riyadh). Implementation is available within the actual supported contracts. Behavioral verification: **NOT_RUN — DEFERRED / NOT VERIFIED**. No test or example was executed.

## Repository assessment and ownership

The semantic transformation belongs to `model_authoring.public`, which already depends on the public Kernel and model-core APIs. It is a distinct operation from MOD-01 schema projection. MOD-04 remains the canonical membership authority in `model_core.public`. MOD-02/03 remain source-loading/location tools. No new module, dependency, technology profile or activation marker is necessary.

Python metadata currently reports 3.12.14 and existing PyYAML 6.0.3. Django and djangorestframework distributions are absent, and no existing canonical-building Django API was found. No framework upgrade, ORM model, migration, database, HTTP endpoint or DRF serializer is introduced. A future applicable HTTP boundary must use DRF, with explicit transport/domain diagnostic presentation; the pure transformation does not import Django.

Full TYPE-01 TypeDefinition and general SK-11 diagnostics remain missing. Current output is the existing `TypeDataComposition`: its five-value frozen host plus optional existing DataFacet. The public model-core `create_type_data_definition` construction function reuses its existing frozen capture and deep-value admission helpers; it does not create a new TypeDefinition class or concrete TypeRegistry. No complete TYPE-01/future facet semantics are claimed. Current diagnostics reuse the actual severity, source path and MOD-04 contracts through a narrow MOD-05 seam. TYPE-08/full SK-09 remain incomplete and are not fabricated.

## Explicit input and structural binding checks

`ResolvedAuthoringModel(document, declarations, retain_source_associations=True)` owns one existing immutable MOD-01 document and a copied tuple of `ResolvedTypeBinding` values. Each type binding contains a nonnegative declaration index, existing SemanticElementId, QualifiedName, SemanticContextRef, exact SemanticVersion and copied tuple of `ResolvedFieldBinding` values. Each field binding contains nonnegative facet/field coordinates, an existing FieldId and optional existing ElementRef/ElementVersionRef target.

Binding constructors reject raw dictionaries, untyped identities, booleans used as indices, subclasses and invalid nested references through TypeError. This is developer contract misuse; expected authoring/binding coverage mistakes return structured diagnostics through `Canonicalizer.canonicalize`. The canonicalizer rejects wrong root input and unsupported schema version, duplicate/out-of-range coordinates, missing definition/field bindings, context mismatch, changed IDs/versions/names and changed FieldIds. Fields require bindings even when primitive, so no name-derived identity is ever introduced.

Binding coordinates locate an authored construct within this exact document. They are not semantic IDs. Binding identity/version must agree with the authored scalar after its established Kernel normalization. QName must agree with the document's explicit namespace and declaration local name. This is local consistency comparison, not name search, alias expansion or namespace discovery. The supplied QName is retained in the output.

All constructors own typed immutable values. Public contracts are not hardened against deliberate frozen-dataclass bypass via object.__setattr__, corrupted unpickling or malicious monkeypatching. Resolution authority and target existence belong to the caller/resolver and later validation; typed bindings are not an authority certificate.

## Transformation and exact representation limits

The stateless frozen Canonicalizer has one pure operation: `canonicalize(resolved_model) -> CanonicalizationResult`. No parser, source provider, registry, filesystem, database, network, clock, locale, random generator or mutable global registry is injected or accessed. Binding tables are private local dictionaries; no mutable collection escapes.

Approved primitive vocabulary has already been parsed by MOD-01 using SK-09's existing PrimitiveType.parse. MOD-05 constructs PrimitiveTypeRef directly from that typed value. All seven current primitives are supported. Unsupported raw tokens cannot enter MOD-01's closed primitive expression contract; MOD-01 reports them, and raw dictionaries passed to MOD-05 fail INVALID_INPUT. No duplicate primitive parser/inference vocabulary is introduced.

Semantic-name and semantic-ID expressions require an explicit target; absent target yields UNRESOLVED_REFERENCE. An identity expression's authored ElementRef must match the resolved target. A primitive must not carry a semantic target. Self, cyclic and outside-model targets remain representable without recursive traversal or existence checks.

TYPE-05 currently supports identity-only SemanticTypeRef(ElementRef). Exact authoring-version expressions or ElementVersionRef bindings fail UNREPRESENTABLE_VERSION with delegated TYPE-REF-003. Even a sole matching model member does not authorize discarding a version pin. No latest selection, coercion to ElementRef or target version inference occurs. Expanding TYPE-05 requires its own architectural task.

Each field uses the bound FieldId and existing FieldName parser, FieldDefinition.create, PrimitiveTypeRef/SemanticTypeRef and FieldConstraintSet.create. Seven existing constraint factories are reused through the immutable MOD-01 mapping. Explicit presence and nullability remain independent. Numeric text is normalized through TYPE-04 NumericConstraintValue, never through binary floats. Constraint enumeration follows TYPE-04's kind sorting; local lower/upper and precision/scale checks remain owned by TYPE-04. Pattern text is retained without compiling a regex. TYPE-06 applicability/target lookup is not run: a structurally representable precision-on-string candidate remains available for later validation.

Absent facet remains None; a declared empty data facet remains DataFacet(()). More than one facet yields UNSUPPORTED_FACET / TYPE-DATA-005, without merging. MOD-01's closed declaration contracts reject unknown kinds/facets before this stage; arbitrary unsupported dictionaries are not accepted as resolved input. Existing DataFacet constructor enforces duplicate FieldId, duplicate/case-portability FieldName checks with delegated TYPE-DATA codes. Field order is the authored order as required by TYPE-03; fields are never sorted by name or identity.

## Atomic assembly, diagnostics and determinism

Successfully transformed supported definitions are assembled with the existing MOD-04 CanonicalModelFactory. MOD-04 owns exact scope, ID/numeric-version ordering, idempotent equal exact entries, conflicting exact content and selected qualified-name ownership. Multiple explicitly selected versions remain distinct. No historical names of omitted registry versions are imported. No concrete TypeRegistry is created/registered/mutated.

A failure anywhere returns model=None, nonempty typed diagnostics and no successful source associations. Valid temporary candidates can be checked for additional membership conflicts but are not returned as a partial successful model. The same resolved input gives equivalent supported content across repeated calls; CanonicalModel is not accepted as authoring input, and no second pass/hash/serialization is added.

Stable MOD-TRANSFORM-001..012 codes cover invalid input, invalid binding, missing binding, unresolved target, scope, facet, unrepresentable version, expression, constraint, field, definition and membership failures. Delegated construction codes are retained in cause_code. MOD-04's complete diagnostic is retained in membership_diagnostic, including exact semantic references; candidate indices are translated back to original authoring paths. Duplicate-field and membership diagnostics retain related paths. No successful warnings or semantic-validation outcomes are manufactured.

Diagnostics are emitted in deterministic phases: binding sequence preflight, declaration/field authoring order, then MOD-04 member order. Equivalent successful input permutations produce equivalent canonical models when coordinates are adjusted; field-order changes can legitimately change DataFacet content. Diagnostic/source-sidecar order is source-oriented and is not claimed to be permutation-invariant. Expected domain construction exceptions are narrowly caught; unexpected programming errors remain visible.

## Optional external source associations

CanonicalSourceTarget identifies an exact ElementVersionRef and optional stable FieldId. CanonicalSourceAssociation associates that target with the original AuthoringSchemaPath. Reordering canonical definitions does not change target identity. Identical exact declarations may contribute multiple source paths to one canonical member. No positional canonical-array index, physical filename or provenance claim is embedded in the model.

Source retention can be disabled explicitly. Core canonicalization remains possible without any physical location index. The existing tooling module provides `locate_canonicalization(result, loaded)` and frozen CanonicalizationSourceLocations / LocatedCanonicalSourceAssociation / LocatedCanonicalizationDiagnostic values. This thin optional presentation adapter attaches actual MOD-03 SourceLocation values by exact path lookup, including related diagnostic paths; absent index/node gives None. It neither loads/parses source nor reruns canonicalization. No nearest-node fallback is used.

Callers must pair the result with the exact LoadedAuthoringDocument that produced the resolved input. Existing MOD-03 source/index checks preserve source-ID alignment; this helper cannot certify transformation provenance or detect a wrong same-shaped document. Source traceability is not an authority/provenance graph. Future governed SK-11/provenance contracts must define stronger cross-stage associations.

## Mini Sales usage — documented, not executed

The established `examples/authoring/mini-sales.json` and `.yaml` use Kernel-compliant sem_<UUIDv4> / fld_<UUIDv4> identities. Illustrative typ_customer_123, fld_name and sales-context strings from the conceptual prompt are not accepted IDs. The existing examples are unchanged: Customer@1.0.0 has name/string/max-length 200, active/boolean and creditLimit/decimal/minimum exact text 0/precision 18/scale 2. Required name/active and optional creditLimit are independently non-null.

The following usage assumes `loaded` is an existing successful LoadedAuthoringDocument for that example, supplied by the upstream boundary. This snippet is documentation only; it has not been run. The explicit values below are supplied bindings, not identities generated by the Canonicalizer.

```python
from semantic_kernel.public import SemanticElementId, SemanticContextRef, QualifiedName, SemanticVersion, ElementVersionRef
from model_core.public import FieldId
from model_authoring.public import ResolvedAuthoringModel, ResolvedTypeBinding, ResolvedFieldBinding, Canonicalizer
from model_loader.public import locate_canonicalization

customer_id = SemanticElementId.parse('sem_550e8400-e29b-41d4-a716-000000000001')
version = SemanticVersion.parse('1.0.0')
binding = ResolvedTypeBinding(
    declaration_index=0,
    id=customer_id,
    qualified_name=QualifiedName.parse('sales.Customer'),
    context=SemanticContextRef.parse('sem_550e8400-e29b-41d4-a716-999999999999'),
    version=version,
    fields=(
        ResolvedFieldBinding(0, 0, FieldId.parse('fld_550e8400-e29b-41d4-a716-000000000001')),
        ResolvedFieldBinding(0, 1, FieldId.parse('fld_550e8400-e29b-41d4-a716-000000000002')),
        ResolvedFieldBinding(0, 2, FieldId.parse('fld_550e8400-e29b-41d4-a716-000000000003')),
    ),
)
result = Canonicalizer().canonicalize(ResolvedAuthoringModel(loaded.document, (binding,)))
if result.is_success:
    customer = result.model.find(ElementVersionRef(customer_id, version))
    locations = locate_canonicalization(result, loaded)
```

Expected design output is one current TypeDataComposition for sales.Customer@1.0.0 with the existing immutable DataFacet and three ordered fields. No assertion of observed execution is made. An unbound Employee expression fails rather than generating an ID; two fields sharing a FieldId fail with TYPE-DATA-001; scope mismatch fails rather than rewriting context; differing same-ID/version definitions fail with MOD-CANON-006; unknown facets fail at MOD-01, without being silently discarded.

## Deferred verification and readiness

[Detailed specification](../../test-archive/MOD-05/MOD-05-deferred-tests.md) records all deferred cases. Tests implemented: 0. Tests executed: 0. Syntax/build/dependency checks are recorded separately in [implementation record](../architecture/mod05-verification.md). Static success is not behavioral verification.

Current contract integrations are implemented for the supported five-value host/data seam and available diagnostics, with full TYPE-01, general SK-11 and exact-version TYPE-05 support explicitly unresolved. No broader resolver, semantic validation orchestration, compiler or next task is implemented. Stop after MOD-05.
