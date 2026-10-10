# Minimal primitive vocabulary prerequisite for TYPE-05

Inspection found no SK-09 PrimitiveType, existing TypeRef, primitive placeholder or raw production field type to reconcile. TYPE-05 explicitly needs seven semantic primitives. This change supplies that **minimal prerequisite** in semantic_kernel.public, without claiming the full unseen SK-09 specification has been implemented. Future SK-09 must reconcile/refine this single contract rather than introduce a competing vocabulary.

PrimitiveType is a frozen nominal value with a closed canonical vocabulary; PrimitiveTypes is its frozen typed catalog:

| Catalog member | Canonical token | Semantic intent |
| --- | --- | --- |
| STRING | string | Text value |
| BOOLEAN | boolean | Logical value |
| INTEGER | integer | Integral numeric value, without machine width |
| DECIMAL | decimal | Exact decimal numeric value, without binary float mapping |
| DATE | date | Calendar date |
| DATETIME | datetime | Date and time; detailed temporal policy awaits SK-09 |
| UUID | uuid | UUID semantic value, not a programming/database class |

Constructor, parse, try_parse and str preserve canonical lowercase tokens without alias inference or trimming. Unknown tokens, runtime classes, DB names, collections, Any/Object/Dynamic/Unknown, bool and numeric ordinals fail. Typed equality/hash and immutable slots follow existing kernel conventions. PrimitiveTypeError uses code/message ValueError: SEM-PRIMITIVE-001 missing scalar, SEM-PRIMITIVE-002 invalid type/token. try_parse catches only expected primitive errors.

These are identifiers for semantic value types, not actual instance values. No runtime parsing, coercion, assignability, date/time timezone policy, storage widths, constraint compatibility or serializer/framework types are introduced. The kernel imports remain dataclasses/re/typing and has no model dependencies. Type-specific references are owned by model-core and reuse this public vocabulary.

See [TYPE-05](../model/type-references.md) and [ADR-0020](../architecture/decisions/ADR-0020-semantic-type-reference-strategy.md). Full SK-09 and missing SK-11/TYPE-01 remain explicit roadmap gaps.
