# ADR-0044 — Immutable instance orchestration with explicit unavailable TYPE-08 integration

Date: 2026-10-11. Status: Accepted as a source architecture decision; runtime behavior **DEFERRED / NOT VERIFIED**.

## Context

RUN-02 supplies scoped exact immutable definition entries and separately authorized lookup. TYPE-02/04/05/06 supply FieldId and definition constraint/reference semantics, but concrete TYPE-08 identity/instances/values, general SK-11 and a genuine runtime schema/decoder are absent. Runtime-core cannot import model-core under current architectural policy. Compiled IR is not a runtime schema. No authenticated applicable Django/DRF endpoint exists.

## Decision

Declare one pure Python application composition module, semantic-instance-runtime, with existing allowed application-zone public dependencies on Kernel/model-core/compiled-contracts/runtime-core and no activation. Do not change core edges/policy or relocate established contracts.

Implement real conditional create/update/inspect orchestration around opaque authoritative TYPE-08 ports and explicit owner-approved canonical immutable classes. No concrete duplicate SemanticInstance, InstanceId, Missing/Null/Value, reference value or fake adapter is introduced. Default unavailable authority/canonical/schema integration fails closed with structured runtime-style diagnostics. TYPE-08 integration is not claimed completed.

Use one authorized exact RUN-02 lookup per operation. Optional coherent snapshot must retain the same original selected entry; no implicit latest/load/compiler/TypeRegistry fallback. Complete instance-schema approval is explicit and source-bound; original encoded fields/order are required. Current loader does not admit model enum leaves and no actual encoded FieldDefinition tuple exists: future authoritative loader-compatible schemas must be integrated before positive behavior is possible.

Reuse original FieldId/presence/nullability/references/constraints. Preserve canonical Missing/Null/Value distinctions, exact native primitive representations and deep immutability. Enforce simple inclusive numeric/code-point-length constraints using TYPE-06 applicability. Pattern/precision/scale require a trusted explicitly bound evaluator, with no invented engine or silent skip. Semantic-reference values remain unsupported.

Return new canonical instances only after complete validation; wrap them with original definition/scope and local revision metadata. Revision0 on create, revision+1 on every successful update including explicit no-op; expected revision required, ceiling explicit. This is a pure transformation, not shared-store CAS or identity uniqueness. Inspection is independently authorized and returns no values on rejection. No storage/ORM/REST/activation/events/actions/workflow.

## Consequences and limits

Production branches and failures are implemented, but genuine end-to-end integration is blocked by missing authoritative TYPE-08/schema/decoder/authority/evaluator prerequisites. Canonical admission currently supports frozen/slotted dataclass variants only; future real TYPE-08 representation/revision decisions require compatible explicit integration. Configured adapters are trusted owner code, not a sandbox. Graph/provenance checks have bounded-count traversal cost, not exact process quotas. No persistence or cross-process coordination; no behavior is verified by static CI.

Exactly one RUN-03 deferred Markdown archive, no executable tests/scenarios. Stop after RUN-03. See [detailed contract](../../runtime/semantic-instance-runtime.md) and [completion record](../run03-verification.md).
