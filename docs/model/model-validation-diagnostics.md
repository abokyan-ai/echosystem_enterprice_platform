# MOD-09 — Model Validation Diagnostics

Date: 2026-10-11. Implementation available; behavioral status **DEFERRED / NOT VERIFIED**. No automated test, reporter/enrichment/transport scenario or usage example executed.

## Actual prerequisite assessment

General SK-11 is absent. Existing contracts provide actual narrow immutable AuthoringSchemaDiagnostic, ModelLoadDiagnostic, CanonicalConstructionDiagnostic, CanonicalizationDiagnostic, NamespaceResolutionDiagnostic, SemanticReferenceDiagnostic, TypeValidationDiagnostic and ModelValidationDiagnostic. Existing TYPE-06 severity is ERROR/WARNING/INFO; loading severity is the existing scalar error. MOD-09 retains these actual diagnostic objects instead of creating a competing generic diagnostic/code/severity model or claiming SK-11 completion.

MOD-03 owns physical SourceLocation/Index, SourceNodePath and ModelSourceId in model-loader tooling. MOD-05 retains exact definition/FieldId associations, but no constraint-specific source association. MOD-08 retains authoritative status/readiness, stage outcomes and original TypeValidationDiagnostic reports. Full TYPE-01 and general SK-11 remain missing. No standalone Action/Event/Policy/facet diagnostic identity is fabricated. No existing Django/DRF diagnostic API is present; no endpoint/serializer/ORM/dependency change is needed.

## Domain associations

model_authoring.public owns ModelDiagnosticOrigin, ModelDiagnosticTargetKind/Target, ModelDiagnosticContext, ModelDiagnosticPayload (a bounded union of actual existing diagnostics), ModelDiagnosticEntry and associate_model_diagnostic. The entry contains the original diagnostic plus auxiliary associations; code/severity/message are not copied into a second model. Origin is a bounded producing-component vocabulary, selected from explicit actual-contract adapters, never message parsing, class-name strings or reflection.

Target kind is definition, owned field or reference. References retain actual ElementRef/ElementVersionRef semantics; FieldId stays distinct. A TYPE-06 field report from MOD-08 supplies the exact owning definition plus FieldId. Direct TypeValidationResult has no owner identity: retain the diagnostic's typed QName/FieldId/path but do not invent an owning stable ID from its name. Reference targets describe explicitly requested/diagnosed coordinates, not proof of resolved existence. Namespace candidates remain alternatives, not a chosen target. Source/document/model-only diagnostics may have no semantic target. Canonical construction retains exact primary/related references; delegated diagnostics remain on the original objects and cause codes are exposed without replacement.

Context has optional explicit semantic scope and actual MOD-05 associations; no model/registry is mandatory. It does not validate or resolve scope/target existence. Equal repeated associations share the same coordinate; conflicting distinct paths for one target are ambiguous and return no location, rather than first-match or a broader guessed fallback. Missing field association may use one explicitly supplied exact definition association. Identity-only references cannot match exact source associations by implicit version selection. These associations are caller-supplied auxiliary evidence, not a security/authority/provenance certificate.

## Source integration boundary

model_loader.public owns the source-aware integration/presentation values ModelDiagnosticSourceTarget, ModelDiagnosticSourceContext, LocatedModelDiagnosticEntry, ModelDiagnosticOperation and ModelDiagnosticReport. This placement preserves existing tooling -> model-authoring imports; physical source types never enter semantic domain imports. All are pure Python immutable values and transformations without Django startup.

Source context requires explicitly supplied actual MOD-03 indexes, at most one selected snapshot per ModelSourceId. Domain paths need an explicit default_source_id; even one supplied index does not authorize inferred source pairing. Loading diagnostics retain their original source ID. Source-only targets retain source ID and optional SourceNodePath without semantic identity. Physical spans come only from original locations or exact index.find, never raw-text search or synthetic offsets.

Original loading primary/related locations win. Legacy positions are preserved and are not upgraded into fabricated spans; optional index enrichment cannot contradict the original line/column/offset. Already located entries passed to enrich_model_diagnostic remain unchanged, preserving original reliable evidence over a competing context. Missing source/index/node stays None. Related paths retain positional None slots when unavailable. Loading batch related_input_index remains original evidence, not an invented related source.

Direct authoring/resolution/canonicalization paths identify exact authored nodes. TYPE-06 constraint diagnostics retain their constraint-kind semantic path, but MOD-05 currently only supplies field/definition associations: use the broader actual source node and never derive a constraint ordinal from kind/text. Source indexes cannot prove a caller paired the original authoring snapshot with canonical associations; this remains an explicit caller obligation.

## Result adapters and processing status

ModelDiagnosticReporter.report takes a finite sequence of actual results and immutable source context. It supports ModelLoadResult/BatchResult, AuthoringSchemaValidationResult, NamespaceResolutionResult/EnvironmentResult/SymbolSnapshotResult, SemanticReferenceResolutionResult/BatchResult/ResolvedAuthoringInputResult, CanonicalModelConstructionResult, CanonicalizationResult, TypeValidationResult and ModelValidationResult. Unsupported raw objects/exceptions/diagnostic dictionaries fail TypeError; no guessed unavailable origin or translated programming defect.

Adapters only inspect supplied outcomes/diagnostics; no loading/schema validation/namespace or reference resolution/canonicalization/type validation/pipeline execution occurs. Loading schema failures remain MODEL_LOADER-origin outer diagnostics with their nested MOD-01 cause retained, rather than being relabeled or emitted twice automatically. A directly supplied MOD-01 result produces AUTHORING_SCHEMA entries. Reference-stage delegated namespace failures remain REFERENCE_RESOLVER outer entries with the original namespace diagnostic/code/candidates attached; supplying both source results explicitly preserves both entries.

Processing outcome is separate from canonical validation: unavailable/succeeded/failed/incomplete/partial are derived from actual supplied producer outcomes, not diagnostic counts. Partial loading/reference batches remain partial; empty loading batch is unavailable; empty reference batch follows its actual all-resolved semantics. The report summarizes only supplied operations, not unobserved workflow completion. Aggregate precedence is unavailable, failed, partial, incomplete, succeeded; operation outcomes retain their individual states so precedence hides no evidence.

Only an actual MOD-08 result supplies validation_status, compilation_readiness and stage_outcomes. One report preserves at most one such authoritative run; separate model/runs require separate reports. Zero diagnostics with skipped/incomplete mandatory stages remains INCOMPLETE/NOT_READY. Filtering does not recompute or alter those statuses. Direct typed report/operation constructors are reporting values, not verification certificates; validation operations require exactly the original MOD-08 diagnostic sequence/status.

## Aggregation, summary and queries

Fixed phase order: loading, authoring schema, namespace resolution, reference resolution, canonical construction, canonicalization, standalone type validation, model validation. Stable sorting preserves caller order within the same phase; producer emission sequence remains unchanged, including MOD-08 stage/canonical definition/rule order. No localized-message sort, random IDs, semantic deduplication, hash iteration dependency or causal-report removal.

Every repeated entry is preserved by default. No deduplication API is supplied. ModelDiagnosticReport.entries is an immutable flattened view; summary derives total/error/warning/info counts each time from actual severities. Counts are not semantic validity or compilation readiness.

by_severity uses the existing scalar severity spellings without a second enum or escalation. by_origin, by_semantic_target (exact primary association) and by_source (primary/related supplied source identities) return tuples in original order. group_by_origin and group_by_severity return read-only maps of tuples in bounded vocabulary order. Empty groups are omitted; every entry remains in exactly one group. Filtering cannot mutate the full report or alter readiness; summarize_model_diagnostics can count a separate filtered view explicitly.

## Explicit transport

model_diagnostic_report_payload is a JSON-ready external tooling adapter with explicit scalar fields, not repr/asdict/model serialization. It includes code, original severity, origin, cause codes, validation stage, processing operation statuses, original MOD-08 status/readiness/stage outcomes and derived counts. Loading stage and related input index are preserved. Optional semantic targets retain stable ID/FieldId/exact version; optional source details retain actual source IDs/node pointers, primary/related spans, legacy positions and absent slots. Domain diagnostics/models never import JSON or DRF.

Default disclosure omits arbitrary diagnostic messages, source IDs/paths/spans and semantic IDs. Caller may explicitly enable messages/source_details/semantic_targets only under existing applicable authorization. ModelSourceInformation.location (potential server absolute filename), source content, Python exceptions, stack trace fields, registry internals or unrelated metadata are never serialized. Messages/source IDs may themselves contain caller-controlled sensitive text; explicit detail opt-in is a caller access-policy obligation, not automatic sanitization. Treat returned text as data, escape it in UI, and never render it as trusted HTML/evaluate expressions.

No existing DRF interface requires extension, so no unrequested HTTP endpoint, serializer infrastructure or alternative HTTP error convention is introduced. Future approved DRF response adapters can consume this transport representation under existing permissions. Semantic severity/validation status never determines HTTP status here.

## Mini Sales usage — not executed

Reuse existing examples/authoring/mini-sales.json. Assume supplied validation_result is the actual MOD-08 result and canonicalized/loaded are original earlier MOD-05/MOD-03 snapshots; no upstream operation is performed by this example.

```python
from model_authoring.public import ModelDiagnosticContext
from model_loader.public import (
    ModelDiagnosticSourceContext, ModelDiagnosticReporter,
    model_diagnostic_report_payload,
)

context = ModelDiagnosticSourceContext(
    semantic=ModelDiagnosticContext(
        canonicalized.model.scope, canonicalized.source_associations),
    indexes=() if loaded.locations is None else (loaded.locations,),
    default_source_id=loaded.source.source_id,
)
report = ModelDiagnosticReporter().report((validation_result,), context)
errors = report.by_severity('error')
payload = model_diagnostic_report_payload(report)  # bounded disclosure by default
```

Expected future behavior: Customer name string precision diagnostic keeps TYPE-VAL-CONSTRAINT-001, TYPE_VALIDATOR origin, exact Customer owner and name FieldId; source uses the reliable actual field/definition node until a constraint association exists. Missing semantic reference retains its MOD-07 or TYPE-06 producing boundary. Missing lookup retains actual MOD-08 INCOMPLETE/NOT_READY, regardless of counts. Malformed source/loading failure can be reported without CanonicalModel or semantic target. This is documentation, not an executed scenario.

See [ADR-0031](../architecture/decisions/ADR-0031-model-diagnostic-integration.md), [static record](../architecture/mod09-verification.md), [single detailed archive](../../test-archive/MOD-09/MOD-09-deferred-tests.md). Stop MOD-09; no MOD-10.

### CMP-01 explicit presentation extension — 2026-10-11

MOD-09 now admits immutable compiler diagnostic values through ModelDiagnosticExtension with explicit COMPILER origin; existing producer origins remain fixed. CompilationDiagnosticReport/CompilerPhaseDiagnosticView are narrow presentation projections owned by model-authoring, carrying original entries, compiler status/target/phase views and actual optional MOD-08 evidence. They contain no artifacts/IR or compiler execution. Model-loader consumes only this inward contract; it does not import compiler-core. Reports preserve compiler status separately from validation readiness. A compilation projection plus directly supplied validation outcome must share the same actual evidence object; separate runs require separate reports. Duplicate diagnostic emissions remain preserved. Historical MOD-09 test documentation/evidence is unchanged. See [compiler foundation](../compiler/compiler-foundation.md).
