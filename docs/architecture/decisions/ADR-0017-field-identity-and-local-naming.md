# ADR-0017 — Field Identity and Local Naming Strategy

Status: Accepted
Date: 2026-10-10

## Context and alternatives

Structural members need rename-safe identity independent of names and projections. Name-derived hashes, ordinals, SemanticElementId/QName reuse and first-class SemanticElement inheritance would conflate owned components with global definitions and physical layouts. Inspected main lacks TYPE-01, SK-09 and SK-11; implement only independent TYPE-02 components without claiming those prerequisites. ADR numbers through 0016 are occupied; choose 0017 rather than the illustrative 0018.

## Decision

Place FieldId, FieldName and FieldDefinition in model_core.public. FieldId follows existing opaque UUIDv4 convention with distinct fld_ prefix, strict version/variant/shape and lowercase hex canonicalization. It is a nominal model-owned value, not a Kernel alias/subclass. No shared cross-module private parser or speculative generic ID hierarchy is introduced; the small independent model regex follows the same established representation strategy. Generation and authoring allocation remain external; never generate during parse or derive from names/order. Assigned persisted/published IDs must survive edits unless intentionally replaced.

FieldName is local ASCII [A-Za-z][A-Za-z0-9_]*, case-sensitive without trimming/style conversion. Keywords remain valid; names imply no hidden type/security/audit/relationship semantics. FieldName is not QName, semantic path, physical name or localized label.

FieldDefinition is an immutable snapshot containing exactly typed id/name. Identity compares id; snapshot equality/hash compares both. Same ID with renamed name is representable without automatic migration/compatibility inference. No SemanticElement inheritance, owner pointer, global registry, independent version, ordinal, projection metadata, constraints/requiredness or type placeholder. Ownership belongs to future DataFacet/type containment; copying an ID to another type does not automatically establish movement continuity. A future precise FieldRef may require owner plus ID.

Only explicit primitive scalar mappings and a test-only evolving internal two-field model representation are demonstrated outside model-core. No final external wire schema or serializer is published. Existing code/message exceptions supply local TYPE-FIELD-001..004 while SK-11 is missing. Full FieldDefinition property/wire shape evolves through TYPE-04/05; stable identity/name semantics remain intact.

## Consequences and future seams

Stable IDs enable future diff/rename/projection tracking without physical-name identity. Collection uniqueness/case collisions and authoring order belong to TYPE-03/06, while ordering never becomes identity. Requiredness/null/default/value semantics need explicit TYPE-04 design; primitive/semantic TypeRef belongs to TYPE-05. No runtime/compiler/infrastructure dependency is introduced and Kernel stays independent.

Existing 44 Fitness rules plus actual model ownership/shape/MRO/import tests suffice; no duplicate rule or external static checker is added. Complete missing SK-09/SK-11/TYPE-01 before integrating DataFacet. Revisit full field composition only with the dedicated type/constraint contracts; revisit wire stability after at least TYPE-05. Published identity retention, owner-aware movement, collection collisions and compatibility/migration remain future governance, not local value inference.
