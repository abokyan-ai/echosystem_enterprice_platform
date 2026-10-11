# ADR-0045 — One read-only runtime validator with explicit completeness

Date:2026-10-11. Accepted source decision; behavior **DEFERRED / NOT VERIFIED**.

## Decision

Use existing pure Python application composition module to own RuntimeValidator and immutable context/request/status/result/evidence/diagnostic/limit contracts. Reuse TYPE-04/05/06 applicability and existing RUN-03 canonical/schema ports. Shared structural source-schema resolver and one value/constraint engine; remove RUN-03's scattered `_value` checks. No module/core dependency/activation change or import cycle.

Consume one authorized application-selected original exact RUN-02 definition/snapshot view without registry/network/loader/TypeRegistry/compiler calls. Read-only complete-instance scope only. No normalization, sentinel/candidate construction, revision increment or persistence in validator. Observe Missing/Null/Value, exact primitives and existing numeric/code-point length semantics. Do not infer complete schemas or reference/cross-field rules from names/tokens.

VALID requires actual completed mandatory checks; INVALID outranks INCOMPLETE while retaining unavailable evidence, completeness independent. Preserve typed identity/version/context/revision and elementary rule outcomes, no timestamp/object-address fingerprint/certification or modified instance. Rejected arbitrary/mutable inputs are not retained as immutable result evidence. Fixed diagnostic order and owner-only bounded graph/check/output resources, explicit terminal unavailable record at caps.

Precision/Scale use existing approved external port; Pattern requires new genuinely bounded owner integration with dialect/work limits, never the ordinary unrestricted evaluator. No actual safe regex engine or missing evaluator is invented. Named model-level capabilities remain unavailable even when server token claims support. No policy/expression/persistence/cross-instance engine.

RUN-03 constructs private whole candidate then accepts only matching complete VALID; failure retains original validation result without accepted candidate/state. The existing public operation result gets only a trailing optional evidence field. Original state and revision stay unchanged on failed acceptance. Injection is owner-side, never request/model data. Existing authorization stays outside validator.

## Consequences

TYPE-08 canonical objects, actual loader-compatible field schema/decoder/authority/evaluators are absent; integration remains blocked and defaults fail closed. Same-process trusted adapters must be pure/deterministic and enforce declared budgets; these ports are not a sandbox. Count limits are not exact RSS/time guarantees. No endpoint/ORM/migration/activation/action/event/workflow or next task. Static green CI is not behavioral verification. Exactly one RUN-04 deferred Markdown archive, zero executable tests/scenarios. [Contract](../../runtime/runtime-validation.md), [completion record](../run04-verification.md).
