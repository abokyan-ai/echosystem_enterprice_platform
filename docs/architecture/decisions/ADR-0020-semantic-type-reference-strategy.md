# ADR-0020: Semantic type reference strategy

Status: accepted for TYPE-05; minimal primitive prerequisite with full SK-09 reconciliation deferred.

## Context

Fields have identity/name/constraints but no type. Kernel stable ElementRef and exact ElementVersionRef exist; no TypeRef placeholder or SK-09 PrimitiveType exists. Production TYPE-01 and SK-11 remain missing. Canonical type identity must survive rename without coupling model to registry or physical representations.

## Decision

Provide minimal Kernel PrimitiveType vocabulary for the seven TYPE-05 tokens and reuse it from model-core PrimitiveTypeRef. Do not create model-local primitives or claim full unseen SK-09 scope complete. Keep kernel free of model dependencies; later SK-09 must refine this single owned contract.

Use a closed Python union TypeRef = PrimitiveTypeRef | SemanticTypeRef, with closed typed TypeRefKind primitive/semantic discriminators and exact-class payload/field checks. Frozen primitive refs hold PrimitiveType; frozen semantic refs hold identity-only ElementRef, never names, loaded definitions or resolver pointers. No custom/Any/Object/Unknown variants or ambiguous optional payloads exist.

FieldDefinition requires id,name,type,constraints with no type default. Type changes retain FieldId in new snapshots; equality includes type and constraints. Presence and nullability stay in FieldConstraintSet. No nullable/optional wrappers, collections or generics are added. References represent value type, not relationships, foreign keys or runtime classes.

Semantic refs are identity-pinned logical dependencies; target rename, context or version change does not alter identity. Authoring QualifiedName resolution and exact ElementVersionRef selection occur later through separate contracts. No optional version, latest/ranges or lookup/assignability/coercion methods exist. Self and mutual graphs remain finite ID references, without eager object recursion.

Extend the internal evolving snapshot codec with explicit kind/primitive or kind/elementRef mappings. Canonical target serialization reuses SK-08; primitive tokens use Kernel vocabulary. Legacy missing-type mappings fail; no hidden default or serializer framework dependency enters public contracts.

## Consequences

All prior field fixtures/examples must supply explicit types; generic structural fixtures use explicit STRING, while the Sales demo uses STRING/BOOLEAN/DECIMAL and a semantic Customer target. Existing DataFacet uniqueness/order and constraint local checks remain unchanged. Applicability, target existence/kind and assignability require TYPE-06/07; construction does not prove them. Host integration remains test-only pending TYPE-01, diagnostics local pending SK-11, and temporal/runtime primitive semantics pending full SK-09. Pattern dialect remains provisional from TYPE-04. No registry, authoring resolver, compiler/runtime value system or physical projections are implemented.

See [actual contracts and examples](../../model/type-references.md).
