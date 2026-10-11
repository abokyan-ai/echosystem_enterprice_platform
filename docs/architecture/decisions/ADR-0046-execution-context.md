# ADR-0046 — Immutable explicitly verified execution context

Date: 2026-10-11. Status: Accepted for RUN-05 conditional implementation; **NOT VERIFIED**.

## Context

Execution invocation metadata differs from semantic meaning, registry membership, instance validity and authority. RUN-01/02/03/04 have narrow specialized contracts and operation-specific authorizations. No actual principal/execution authorization, delegation, cancellation, executor accounting or active deployment contract exists. Django/DRF remains mandatory HTTP technology but no installed framework or applicable protected endpoint exists.

## Decision

Implement pure contracts/factory in existing runtime-core.public using only its existing Kernel/compiled-contracts edges. Reuse SemanticContextRef, ElementVersionRef, RUN-02 scope/snapshot/original definitions and existing runtime status/severity. No new module or backwards RUN-03/04 dependency. Explicit operational UUID4 invocation/correlation wrappers differ from semantic/instance identities; immediate invocation cause only.

Exact nonempty finite reference selection carries actual same-scoped immutable membership snapshot with stable numeric-version order; no latest, graph resolution, synthetic deployment/hash, activation or live lookup. Original selected definitions receive existing structural integrity checks, never semantic or instance validation/load/registration.

Principal/decision association wrappers admit actual approved immutable non-secret references structurally, but do not establish trust. An explicitly configured pure owner verifier checks real prior authentication/authorization evidence and returns a typed original-invocation projection containing scope, operation, exact models and bounds. Missing or insufficient evidence fails closed. Existing load/registry/instance permissions cannot grant execution. No actual implementation/category approved, new policy solver, authentication provider or fabricated trusted fixture. Future owner approval must reflect actual evidence dimensions and recheck audience/lifetime/revocation where supported.

Root explicit coordinates only; context immutable and propagation explicit. Derived context requires same owner boundary, fresh parent/child evidence verification, unchanged principal/context/target/operation/correlation, immediate parent cause, new child invocation, same snapshot model subset and strict bounded constraint narrowing. No delegation/principal override or generic scope-comparison lattice. Source pointer association is local original-evidence coherence, not semantic identity, cryptographic provenance or a bearer certificate.

Finite depth/nested ceilings and absolute fixed-offset aware deadline are descriptive. Deadline observation takes explicit trusted now; no implicit clock/execution/cancellation. No sibling accounting ledger/enforcement guarantee. Unsupported mandatory enforcers or required active deployment produce INCOMPLETE. Registry membership is not active deployment. Context creation is not execution start or permanent permission.

No Django request/domain import, ORM, migration, endpoint, serializer permission engine, contextvars/global current context, raw credentials, mutable metadata or full ancestor context. Only genuine applicable existing DRF application integration would consume authenticated approved associations; none exists to modify here.

## Consequences

Conditional production creation and strict derivation logic implemented; actual trusted end-to-end integration blocked. Reference admission deliberately restricted to approved frozen/slotted bounded immutable reference graphs; future real contracts must be reconciled, not replaced. Owner adapters remain trusted Python code, not a sandbox; syntax cannot detect arbitrary secrets. Original selected-node graph checks cost bounded traversals without claiming CPU/RSS guarantees. Unexpected programming faults propagate without false success.

Exactly one deferred archive, no tests implemented/executed or manual context experiments. Static checks are separate from behavioral verification. Ready for review and later authorized genuine prerequisite integration. Stop RUN-05; no RUN-06.
