# ADR-0035 — Preserve canonical type structure in explicit immutable compiled IR

Date: 2026-10-11. Status: implemented for existing type/data seam; behavior unverified.

## Context

MOD-04 supports actual immutable TypeDataComposition with captured five-value host, optional DataFacet and existing immutable field/reference/constraint contracts. Full TYPE-01/general SK-11/richer facets remain absent. CMP-03 provides closed IR payloads and original request handoff; no target generator exists.

## Decision

Add compiled type/field value objects and reuse exact TYPE-04/05 contracts with aliases, preserving source type/version/QName/context, FieldId/name, established field order, identity-only semantic references, independent presence/nullability and precise constraint values. Intrinsic collection checks delegate to existing DataFacet; semantic applicability remains TYPE-06/MOD-08.

A focused lowerer requires original VALID/READY request and actual accepted preparation/evidence, exact original canonical member and explicit caller representation identity. The explicit type phase requires one binding per selected canonical definition, processes canonical order, collects deterministic diagnostics and emits no partial envelope set on failure/incomplete capability. Absent DataFacet is INCOMPLETE; explicit empty present DataFacet is supported. No fabricated TypeDefinition/facet or full semantic model recreation.

Extend the closed CMP-03 payload union/discriminator to COMPILED_TYPE_IR, requiring exactly one matching origin/scope and full original field/name structure. Use existing phase result/error/diagnostics/handoff, no second result hierarchy. Default compiler composition is unchanged; caller explicitly adds fixed type phase. IR never satisfies final artifact capability/readiness.

## Consequences

Original semantic values retain precise meaning without target mappings or reference resolution. Request/preparation/member associations remain trusted in-process, not authenticated/portable snapshots or permissions. Explicit ID coverage/configuration and upstream richer-facet/SK-11 ownership are caller/dependency obligations. No SQL/ORM/API/UI/runtime generation, graph closure, optimizer, endpoint, persistence/cache or publishing. Deferred documentation mandatory; tests remain 0 / DEFERRED / NOT VERIFIED. Stop CMP-04.
