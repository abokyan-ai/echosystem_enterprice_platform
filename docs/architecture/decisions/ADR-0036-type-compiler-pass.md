# ADR-0036 — Coordinate canonical type lowering through one atomic compiler pass

Date: 2026-10-11. Status: implemented; behavior NOT VERIFIED.

## Context

CMP-04 already includes a gated single-type lowerer and an explicit multi-type phase. CMP-03 uses caller-owned request-local IDs and CMP-01 owns immutable atomic state transitions. Current canonical membership is closed type/data; full TYPE-01/general SK-11/richer facets and target generators remain absent.

## Decision

Promote existing orchestration into TypeCompilerPass, with CompiledTypeLoweringPhase as a compatibility alias and the same stable CMP-PHASE-COMPILED-TYPE-IR descriptor. Split payload lowering from envelope wrapping by adding lower_payload to the original lowerer; preserve original lower through an adapter. Reuse all payload, field, result and diagnostic contracts. Pass selects actual canonical types in canonical numeric-version order, requires explicit exact bindings, coordinates envelopes and aggregates expected failures without partial output. Unexpected defects propagate.

Check original evidence/preparation/outcome/request associations on direct invocation. Reject rerun/outcome slots, repeated representation IDs and occupied exact compiled-type origins; preserve unrelated original state. Preflight existing CMP-03 merge and let CMP-01 commit once atomically. Phase emission order is canonical; committed inventory remains identity-sorted. No global registry/idempotent overwrite policy.

Zero types is valid empty completed work, not a dummy type or whole-build success. Multiple exact versions remain distinct; references remain versionless with no expansion/recursion. Other semantic-kind coverage is an upstream contract gap; no semantic-invalid relabeling or invented generic pass. Source provenance only uses original sidecars.

## Consequences

Old callers retain lower/phase APIs while orchestration has one implementation. Explicit IDs/accepted state are caller obligations and trusted in-process. Static checks cannot establish semantic correctness; deferred scenarios await explicit authorization and prerequisite fixtures. No framework route/ORM/generator/runtime/storage/deploy change. Stop CMP-05.
