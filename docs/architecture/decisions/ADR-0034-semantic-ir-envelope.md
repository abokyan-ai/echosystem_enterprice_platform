# ADR-0034 — Explicit bounded semantic IR envelope and trusted phase handoff

Date: 2026-10-11. Status: implemented within actual available contracts; behavior unverified.

## Context

CMP-01 supplies immutable canonical request/evidence, compiler state/phase results and artifact boundary. CMP-02 supplies diagnostic association/reporting. No concrete IR payload exists; no general SK-11 contract or applicable compiler HTTP interface exists. A universal metadata bag, complete invented Type IR or artifact substitute would bypass ownership.

## Decision

Introduce an explicit request-scoped ir- representation identity, envelope schema V0 and one closed immutable foundation-coordinate payload. This small contract carries selected exact semantic coordinates only, not lowered definitions. Require explicit original request/VALID-READY snapshot binding, exact member origins and optional existing source/phase associations. Empty inventory is valid only for explicitly model-wide scope; missing payload is rejection.

Extend existing phase result/state minimally with ordered candidate/committed envelope tuples and original phase outcomes. Future producer must declare EMIT_IR; coordinator commits valid candidates with artifact state atomically, retaining actual producer evidence and rejecting duplicate IDs. Consumer boundary requires same committed envelope, same request/preparation context, completed executed producer and declared prerequisite. No lowering phase/consumer is installed. IR never satisfies artifact capability/output readiness.

Expected structural/handoff failures use existing compiler diagnostic/error and phase FAILED pattern; no extra result ecosystem. CMP-02 carries typed IR association with a narrow authoring token projection; existing transport defaults hide IR identity/payload. General SK-11 remains an explicit unmet dependency, not replaced.

## Consequences

Original request and outcome references are trusted in-process association, not semantic equality, portable hash or authenticated provenance. Envelope equality uses the same declared values and original request association; no serialization/content addressing. State order is explicit token order, origin/payload order is preserved. Future schemas/payload kinds require explicit owned extensions. No new module/profile/dependency, ORM/API, canonical-to-IR lowering, optimizer, generator, publisher, runtime or global registry. Deferred documentation is mandatory; tests remain 0 / DEFERRED / NOT VERIFIED. Stop CMP-03.
