# MOD-08 — Validation Pipeline

Date: 2026-10-11. Implementation provided; behavioral verification **DEFERRED / NOT VERIFIED**. No automated tests, resolver/validator scenarios or example execution.

## Actual dependency assessment

Kernel exposes canonical identity/context/name/kind/version/reference values. General SK-11 is absent. TYPE-06 exposes TypeValidator, mandatory TypeValidationContext(TypeLookup), immutable TypeValidationDiagnostic/Result and three mandatory structural/constraint/reference rules. Full TYPE-01 is absent; TYPE-06 and MOD-04 support the existing frozen five-property host plus TypeDataComposition/DataFacet seam. TYPE-07 supplies read-only TypeLookup and explicit version-bound views; bare lookup can raise TypeRegistryAmbiguityError. TYPE-08 instances are not validation inputs here. MOD-01 owns decoded-tree structural validation/projection; MOD-02/03 own source loading/locations; MOD-04 constructors enforce scope/member/kind/exact uniqueness; MOD-05 preserves exact definition/FieldId source associations; MOD-06/07 resolve/bind references separately.

No missing standalone namespace, instance, universal model consistency or general diagnostic validator is fabricated. No existing Django/DRF HTTP endpoint requires changes. Core remains pure Python under existing model-authoring, and tooling presentation remains in model-loader. No dependency upgrades, new module or API/database/persistence.

## Public boundary

ModelValidationRequest consumes the actual CanonicalModel and ModelValidationContext(scope, type_lookup, warning_policy), plus optional actual MOD-05 CanonicalSourceAssociation values. All configuration/result sequences are copied into immutable tuples; source indexes are read-only. Source targets must identify exact model members and owned FieldIds, with no duplicate target association. Context disagreement remains a structured blocked result rather than transport exception. Wrong/unrepresentable input types fail at constructors or entry guards. There is no authoring entry point: existing MOD-01 validation remains separate and is not called automatically.

ModelValidationStage is an explicit protocol with stable id and validate(request). ModelValidationStageResult retains stage ID, completed/blocked/incomplete/skipped status, ordered reports and an explicit reason when not completed. ModelValidationReport retains the entire original TYPE-06 diagnostic or narrow orchestration diagnostic plus stage origin, exact definition owner and supplied source association path. No delegated code/severity/message/FieldId/target/typed semantic path is translated or deduplicated. Narrow MOD-VALIDATION-001..005 codes cover only scope, missing/ambiguous lookup and snapshot disagreement while general SK-11 is absent.

## Mandatory composition and ordering

1. MOD-STAGE-CANONICAL-INTEGRITY reuses MOD-04 constructor guarantees and checks request scope agreement. Invalid kind/context/duplicate member construction cannot be represented by the supported immutable model; the pipeline does not rebuild or duplicate those algorithms. Future unsupported kinds need an actual canonical admission extension and owned validator before receiving readiness.
2. MOD-STAGE-TYPE-SEMANTIC prepares a finite stable lookup capture, checks canonical/lookup metadata consistency and calls the existing full TypeValidator exactly once per member in canonical order. TYPE-06 itself runs structural, constraint and reference rules in its existing order. Reference validation is integrated here, without a second reference traversal/rule engine. No additional universal model-level stage exists because no separate cross-definition validator exists.
3. Explicit additional stages run in caller-supplied order, are mandatory for this invocation and cannot replace/reorder/remove the two core stages. Injected actual TypeValidator may carry its existing additional rules; the mandatory TYPE-06 rules remain intact. Empty additional stages is valid; empty core configuration is unrepresentable. No reflection, dynamic imports, arbitrary profiles or exclusion loophole.

Completed stages with model errors do not prevent safe later stages from collecting diagnostics. Blocked/incomplete/skipped stages stop dependent execution; every remaining configured stage is reported skipped with the prerequisite ID and no fabricated validator reports. Unexpected defects and malformed custom-stage outputs propagate as programming errors; only the actual TYPE-07 ambiguity exception is translated into unavailable prerequisite evidence.

## Explicit lookup policy

The caller supplies a pure stable read-only TypeLookup, normally an explicit TYPE-07 bound view. No automatic registry registration or model overlay. The stage captures model identities plus direct SemanticTypeRef field targets once per distinct identity in stable ID order. Returned five-property metadata is copied into frozen targets before TYPE-06; no live port remains in its per-operation context and no global cache exists.

Every canonical identity must be visible in the supplied view at an exact version present in that model with matching name/kind/context. None for a canonical member is an explicit environment mismatch, not a synthesized local fallback. Multiple model versions are all validated, while the supplied identity lookup must explicitly select one matching version for references; the pipeline never picks it. A selected version outside canonical membership is a mismatch. TYPE-07 ambiguity yields INCOMPLETE, retaining TYPE-REG-006. Missing lookup also yields INCOMPLETE even for primitive-only/empty models because the full TYPE-06 contract requires it. With a supplied valid lookup, an empty canonical model can complete vacuously.

A None target outside canonical membership remains the actual TYPE-06 missing-target judgment. Wrong target kind is delegated to TYPE-06. Wrong identity or cross-context metadata blocks unsafe validation as an environment error. Invalid returned host types are an infrastructure/programming TypeError, not ordinary authored-model failure. Coordinate consistency cannot compare absent data/facet payload on the TypeLookup return or certify unseen registry history. Port purity/stability across capture is a caller obligation. Additional rules querying undeclared identities outside the finite snapshot fail explicitly; no speculative catalog discovery.

Self-references and cycles use captured direct targets without recursion. Current TYPE-05 canonical fields contain only identity ElementRef; authoring names/unresolved expressions and exact field-version pins cannot enter this stage. Exact canonical membership and explicit selected versions remain unchanged. No re-resolution, binding, repair, canonicalization or definition reconstruction.

## Status and readiness

ModelValidationResult derives status/readiness from all stage outcomes, with no independent mutable validated flag. Any error gives INVALID. Otherwise any noncompleted stage gives INCOMPLETE. After all stages complete, warning policy ALLOW permits warnings and BLOCK gives INVALID on warnings; INFO never blocks. INVALID/INCOMPLETE always yield NOT_READY. VALID gives READY only under the current supported host/data contract and mandatory configured stages, not full missing TYPE-01 semantics or compiler success. Missing dependencies are warning-severity orchestration reports accompanied by mandatory INCOMPLETE status, so unavailable infrastructure never appears valid or as a missing-target error. When errors and incompleteness coexist, INVALID takes precedence but stage outcomes retain the incomplete evidence.

Diagnostic order is stage order, then lookup prerequisite reports in stable identity order/model membership order, then TYPE-06 canonical member/rule/emission order. No message sorting, object-ID ordering, generic deduplication or loss of prior reports. Configuration extensions must honor the stage protocol's purity, deterministic order, stable immutable implementation state and reported coverage; frozen containers do not prove arbitrary injected code pure. Direct result construction is a typed reporting contract, not a tamper-proof verification certificate.

## Source-aware presentation

Existing MOD-05 definition/field associations are auxiliary. The exact owner/FieldId association wins; only an explicitly supplied definition association is a broader fallback. Constraint diagnostics retain the original typed constraint path and FieldId but use the actual field/definition source node because MOD-05 has no constraint association vocabulary. No constraint ordinal/physical span is guessed. Missing association remains None.

model_loader.public.locate_model_validation(result, loaded) attaches actual MOD-03 nodes at these paths externally. It preserves every report and uses no nearest-node inference, parsing, loading, validation rerun or model mutation. Missing index/node remains None. Callers must pair the original source snapshot; stronger source provenance is not claimed.

## Mini Sales usage — not executed

The established examples/authoring/mini-sales.json remains unchanged: Customer name string required/non-null max-length 200; active boolean required/non-null; creditLimit decimal optional/non-null minimum 0 precision 18 scale 2. Assume the caller has already loaded, structurally validated, resolved and canonicalized it using earlier boundaries and has supplied a compatible explicitly bound lookup containing Customer. Those transformations are not performed by MOD-08.

```python
from model_authoring.public import (
    ModelValidationContext, ModelValidationRequest, ModelValidationPipeline,
    ValidationWarningPolicy,
)
from model_loader.public import locate_model_validation

# supplied canonicalized is an actual successful MOD-05 CanonicalizationResult;
# supplied selected_lookup is an actual stable TYPE-07 TypeLookup bound view;
# supplied loaded is the original actual MOD-03 loaded source snapshot.
request = ModelValidationRequest(
    canonicalized.model,
    ModelValidationContext(canonicalized.model.scope, selected_lookup,
                           ValidationWarningPolicy.ALLOW),
    canonicalized.source_associations,
)
result = ModelValidationPipeline().validate(request)
located_reports = locate_model_validation(result, loaded)
```

This snippet is production usage documentation, not an executed test or runner. Expected valid complete processing is VALID/READY. String precision and fractional integer bounds use actual TYPE-06 diagnostics, not new rules. Unknown semantic target yields TYPE-VAL-REF-001 and INVALID/NOT_READY with a functioning lookup; missing lookup yields INCOMPLETE/NOT_READY. Self/cycles are not rejected solely as cycles.

See [ADR-0030](../architecture/decisions/ADR-0030-validation-orchestration.md), [static record](../architecture/mod08-verification.md) and [deferred archive](../../test-archive/MOD-08/MOD-08-deferred-tests.md). Stop after MOD-08.
