# MOD-03 — Source Location Tracking: repository archive

Task identifier/title: **MOD-03 — Source Location Tracking**. Date: **2026-10-10 (Asia/Riyadh)**.
Testing status: **DEFERRED / NOT VERIFIED**. Every case: **NOT_RUN — DEFERRED**.
Tests implemented: **0**. Tests executed: **0**. Detailed scenarios: **103**.
Single detailed file: [MOD-03-deferred-tests.md](MOD-03-deferred-tests.md).
Standing-name navigation: [MOD-03-deferred-test-spec.md](MOD-03-deferred-test-spec.md).

## Scope and architectural dependencies

Existing model_loader.public SourcePosition gains optional offsets; new frozen SourceSpan/Location/NodePath/NodeKind/LocationEntry/LocationIndex/LocationTracker provide half-open physical spans, typed pointer addressing and immutable deterministic indexing. Existing JSON/YAML adapters retain parser-native key/value/container locations; decoded/loaded results and existing loading diagnostics gain defaulted optional index/primary/related fields. Snapshot digest verifies exact acquired text when supplied. MOD-01 schema and Kernel semantic contracts are unchanged. No tests or executable examples are added/changed.

Dependencies: MOD-01/MOD-02 actual public contracts and their current provisional diagnostic seam; general SK-11 is absent and remains a reconciliation dependency. Python stdlib JSON callback adapter and existing pinned PyYAML==6.0.3 operate in the already approved tooling boundary. No module/profile change, Django/DRF endpoint/serializer/ORM/database or runtime dependency is introduced. Missing TYPE-01/TYPE-08/full SK-09 remain explicitly documented.

Production change: [model_loader.public](../../tools/model-loader/src/model_loader/public.py). Documentation changes and exact file list: [mod03-verification.md](../../docs/architecture/mod03-verification.md). Contract/Mini Sales path examples: [source-location-tracking.md](../../docs/model/source-location-tracking.md). Decision: [ADR-0025](../../docs/architecture/decisions/ADR-0025-source-location-tracking.md).

## Future execution conditions and limitations

Require explicit user authorization, fixed source/archive revision, Python/version matrix, module paths, pinned YAML parser, exact source-text fixtures/options/newline conventions and recorded lexical span/diagnostic evidence. Future API serialization cases require a later authorized real DRF endpoint and its existing access controls; they are conditional specifications, not implemented transport. No test infrastructure is added solely for this archive. Preserve cases and stable IDs/history when updating.

General SK-11 integration remains provisional. Stdlib JSON scanner/object/array callbacks are implementation-level APIs and require deferred compatibility verification. JSON and YAML retain their native line-break conventions; offsets are Unicode characters, not bytes/graphemes/UTF-16 units. Standalone coordinates/undigested custom adapters cannot certify raw-text truth. YAML strict v0 rejects anchors/aliases/tags/multiple documents. No parser AST escapes, location cache, source rewriting, semantic resolver/canonicalizer, full provenance graph or source-download API exists. Current behavior and Mini Sales remain unverified despite static checks.

Readiness: contracts and adapter integration are implemented for review by later authoring stages, with limitations visible. Stop at MOD-03; do not start MOD-04.
