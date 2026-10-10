# ADR-0015 — Semantic Reference Model

Status: Accepted
Date: 2026-10-10

## Context and alternatives

Canonical consumers need to distinguish stable identity references from exact version coordinates and authoring names. Raw strings obscure whether a value is an ID, QualifiedName, relative spelling, selector or resolved target. SK-07 already supplies ElementVersionRef; SemanticContextRef has specialized meaning. A unified ElementRef with optional version, runtime generic hierarchy, name hints or registry-backed construction would introduce ambiguity/coupling. ADR-0013/0014 are occupied, so this decision uses 0015 rather than the illustrative prompt number.

## Decision

Introduce only frozen ElementRef(element_id: SemanticElementId). Identity-pinned references carry no version and imply no latest lookup. Reuse SemanticElementId.parse and canonical text without duplicated ID grammar. Typed construction/from_id retain a validated value; parse/try_parse, value equality/hash and str follow existing Kernel conventions. No new infrastructure dependency, module, bootstrap registration or root property is needed.

Retain ElementVersionRef unchanged as identity plus one required exact SemanticVersion. Keep the two contracts distinct; no nullable version, selector, implicit pin selection or silent pin dropping. Callers can explicitly use an exact reference's ID to construct a logical ElementRef. Keep SemanticContextRef as a distinct specialized type, not an alias/subclass replacement.

QualifiedName and source spelling stay outside stable references. Symbolic/unresolved contracts belong to future Authoring/Canonical layers; parsing, namespace/import/alias resolution and symbol lookup produce stable coordinates outside Kernel. Optional external version selection then produces exact coordinates. Loaded definitions/ResolutionResult belong to future Compiler/Resolution, not reference values. No target existence/kind/visibility check, runtime pointer, source location, package/tenant/security state, relationship/dependency semantics or generic runtime-class parameter enters these contracts.

JSON maps ElementRef explicitly to a canonical ID scalar in a typed field; exact JSON remains the SK-07 elementId/version object. Serializer boundaries/schema declare reference intent because scalar syntax alone cannot distinguish identity/context/generic references. Tests demonstrate converters outside Kernel; no framework serializer is introduced.

## Consequences and future governance

Stable references survive rename, namespace/context move and version evolution; exact references preserve the version coordinate needed by future manifests, migration plans and provenance. Neither coordinate establishes availability, compatibility, authority, content integrity or reproducibility by itself. Definition references are distinct from future business/execution InstanceRef. No TypeRef/ActionRef wrapper expansion is introduced before its roadmap stage.

Existing 44 Fitness rules already protect dependency/public neutrality; focused behavior/shape tests cover the specific reference invariants. Python nominal dataclasses and construction validation protect local intent, while static annotations alone are not runtime validators. No external type checker was added/run. The single-field public/wire contract must remain stable; any future pinning, hints or source usage metadata requires a separately justified contract rather than optional fields here. ContextDefinition ownership remains gated by ADR-0012. Next: SK-09, SK-10, SK-11.
