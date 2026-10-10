# ADR-0019: Field presence, nullability and constraint model

Status: accepted for TYPE-04, with deferred pattern dialect and type applicability.

## Context

FieldDefinition id/name snapshots and DataFacet membership exist; constraints/types do not. Missing members and present null values have different meanings for instances, partial updates and events. TYPE-05 TypeRef and TYPE-06 applicability are later stages. TYPE-01, SK-09 and SK-11 are absent, so host integration remains test-only and diagnostics follow existing local code/message errors.

## Decision

Use distinct FieldPresence and FieldNullability enums, with all four combinations allowed. Required means member existence, not non-null. Optional permits absence, not automatically null. A required nullable member must exist and may hold null. A canonical FieldConstraintSet requires both typed axes and an explicit value collection, with no constructor defaults.

Represent seven fixed-kind constraints as frozen typed values; ValueConstraint exposes a read-only ConstraintKind only. ConstraintKind vocabulary is open, but supported concrete v0 payloads are closed and exact class checked, including rejecting subclasses. No generic JSON payload or mutable custom implementation is accepted. Future extension schemas are a separate contract.

Defensively copy ordered input, reject repeated kinds rather than last-write-wins, then sort by kind. Equality/hash ignore input ordering. Check only local length bounds, inclusive exact numeric bounds and scale <= precision. NumericConstraintValue is fixed-point ASCII canonical text, limited to 4096 digits, without floats or exponent notation; stdlib Decimal comparison performs no rounding arithmetic. Pattern holds non-empty exact text; no dialect, portability, compiled engine or evaluation is promised.

FieldDefinition requires FieldConstraintSet explicitly. Changes yield new snapshots; owner version and compatibility policy belong elsewhere. Internal constraint_wire mapping evolves the field schema without serializer attributes or public API exports. Missing/extra members and unsupported payload kinds fail explicitly.

## Boundaries and consequences

Model contracts remain in model-core with approved standard library and Kernel public contracts only. Kernel never depends on constraints. Instance validation and compiler lowering are separate; constraints execute no behavior. Type-specific compatibility follows TYPE-05/06; constraints never infer field types. SQL NOT NULL/NULL/CHECK, API required flags and UI required markers are projections, not source semantics.

Existing two-argument FieldDefinition calls must supply explicit constraints; all repository fixtures/code examples are updated, while prior verification records remain historical. No silent legacy mapping defaults are introduced. The evolving wire schema is not released as final authoring schema. Missing production host and unified diagnostics remain explicit gaps. Pattern dialect, instance length units, decimal execution semantics, resource limits and extension payload support need later decisions. No runtime validation, cross-field rules, defaults, uniqueness, compatibility classification or migrations are implemented.

See [contract and truth table](../../model/field-constraints.md).
