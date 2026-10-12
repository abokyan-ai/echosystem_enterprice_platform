# ADR-0047 — Observational runtime failure composition and controlled presentation

Date: 2026-10-12. Accepted for RUN-06 implementation; **NOT VERIFIED**.

## Context

RUN-01…05 already own authoritative results, statuses, diagnostics and narrow expected exceptions. General SK-11 is absent; MOD-09/CMP-02 have separate existing typed associations, with neutral CMP-09 reader evidence crossing RUN-01. FieldId/InstanceId associations cannot enter runtime-core through a forbidden model edge. No actual runtime DRF endpoint/response/authentication contract exists.

## Decision

Place RuntimeErrorDetail (avoids builtin exception shadowing), closed code/category/operation/context/target/cause/collection/factory/result-association and presentation contracts in existing application composition public API. No new module, lower-core import relaxation or reverse service dependencies. Reuse actual Kernel/model/runtime identities, RuntimeLoadSeverity, original diagnostics and status enums. No generic Diagnostic/SK-11 implementation invented.

Preserve109 RUN codes and20 actual neutral CMP reader codes. Only new controlled fallbacks501 INTERNAL,502 OSError infrastructure,503 unknown cause detail,505 public nondisclosure. Category compatibility/source-sensitive reader integrity determined by explicit code/evidence mapping, never message text. Safe messages fixed, catalogs read-only. No error occurrence ID/clock/random/compiler replay.

Map actual results observationally with explicit compatible operation. Keep NOT_FOUND/AMBIGUOUS routine, VALID/INVALID/INCOMPLETE and independent complete flag exact. Expected narrow exceptions map to equivalent non-success source result only. Source result remains authoritative; no generic result replacement, mutation or re-execution. Unknown detail explicit rather than invented diagnosis.

Original immutable diagnostics repr-hidden, typed targets internal only, actual lower failures flat bounded cause snapshots. Warn/info related conditions not direct failure causes; correlation never creates causal proof. Duplicate occurrences preserved in source order. Overflow/omissions/depth limit explicit and detail completeness independent from outcome. No recursive error/exception graphs or synthetic root cause.

Unexpected transform only at explicitly owned outer boundary; never install broad catches around domain methods. Keep expected rejection distinct, rethrow termination/cancellation/groups, no exception text/type/trace serialization or new logging/recovery infrastructure. Default public projection one generic505 and no identifiers; trusted server allowlist controls known code and exact permitted correlation only. No targets/causes/credentials public, HTTP/envelope/security semantics remain future applicable DRF/application owner responsibility.

## Consequences

Production factories/result adapters and safe projection implemented; actual source interactions and semantic behavior deferred. Missing SK-11/canonical TYPE-08/trust/DRF interface/evaluator/source-fixture integration retained explicitly. Source reference sharing and bounded output are not CPU/RSS quotas, cryptographic origin proof or authorization. Original internal diagnostics may contain sensitive text and must remain behind approved boundaries. No retry, persistence, tracing, business execution or RUN-07.

Exactly one RUN-06 deferred archive; no executable tests or mapping experiments. Static syntax/marker/build/architecture/code-table/document checks do not verify semantics. Stop RUN-06.
