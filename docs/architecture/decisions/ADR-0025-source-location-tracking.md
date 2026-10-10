# ADR-0025: Immutable source locations associated with authoring snapshots

Date: 2026-10-10 (Asia/Riyadh). Status: implemented for MOD-03; **NOT_RUN — DEFERRED / NOT VERIFIED**.

## Context

MOD-02 has a source identity and line/column value object; YAML exposes native node marks, whereas json.loads alone discards spans. MOD-01 exposes deterministic structural paths/related paths. General SK-11 is missing. No Django project/API/serializer exists; local Django/DRF distributions are absent and PyYAML is the pinned 6.0.3 dependency. Introducing ORM/persistence/API machinery would expand an internal source-location task.

## Decision

Reuse/extend existing model_loader.public contracts with defaulted additive fields. Keep locations auxiliary to authoring snapshots and separate from Kernel/semantic identity. SourcePosition adds optional zero-based Python Unicode character offset; positions are one-based and retain native parser newline semantics. SourceSpan is half-open, allows zero width, rejects reversed/inconsistent coordinates. SourceLocation retains MOD-02 ModelSourceId. No universal byte/UTF-16 conversion is assumed.

Use typed pointer tokens with empty root and ~0/~1 escaping. Index typed entries for both value/container and optional property-key spans. Defensively copy/sort entries, own a private read-only map, reject conflicting paths/source mismatch, allow idempotent duplicates and explicit absence. Lexicographic pointer enumeration is deterministic. Optionally digest exact acquired source text using SHA-256 UTF-8; built-in adapters always supply it and loader checks it when present. Hash identifies snapshot content, not semantic authority/provenance.

Instrument stdlib JSON scanner/object/array callbacks and scanstring to obtain spans from the same parse creating values. Do not implement a separate JSON grammar or search text for matching declarations. This deliberately uses stdlib implementation callback interfaces; document compatibility risk and deferred Python matrix cases. Add no parser dependency and change no version requirement. Preserve strict JSON failure/safety policy and add precise duplicate/syntax spans.

Extend the existing PyYAML node projection with native marks for keys and values; retain approved YAML 1.1 rejection policy and bounded preflight. No aliases/tags or extra source formats are enabled. Do not expose parser AST nodes.

Map actual MOD-01 diagnostic paths to exact value/key spans, original related paths to immutable related locations and missing properties to a reliable existing containing node. Retain original diagnostic causes. General SK-11 integration cannot occur until that contract exists; extend the actual provisional loading seam without building a second general Diagnostic model. Do not fabricate unknown coordinates/spans. Keep legacy position-only decoders and generated objects compatible.

No HTTP endpoint/serializer/Django model is added because no existing endpoint requires adaptation. Future APIs must use DRF at its approved boundary. Source tracking does not resolve, canonicalize, register, compile or execute semantic data.

## Consequences

Locations and typed paths are deterministic within one source snapshot, not edit-stable semantic IDs. JSON native callback compatibility, YAML native newline/mark semantics and source resource costs require future verification. Standalone values cannot prove raw-text coordinate truth; custom injected metadata without a digest is a trusted contract. Primary diagnostics require same-source locations; related locations preserve separate source association. Missing SK-11 and full TYPE-01/TYPE-08/SK-09 are explicitly visible. No test source is created or changed; one detailed Markdown file documents future scenarios, with archive navigation files retaining standing naming conventions. No suite or example is executed. Stop at MOD-03.
