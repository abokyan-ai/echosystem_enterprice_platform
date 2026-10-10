# ADR-0021: Semantic type validation architecture

Status: accepted for TYPE-06; production host and unified diagnostics integration remain provisional.

## Context

TYPE-02..05 canonical constructors guarantee local structural invariants but allow cross-object semantic mismatches. Field constraints and TypeRef representation must not acquire self-validation, registry, physical mapping or instance execution. TYPE-07 follows this stage. Production TYPE-01 and SK-11 remain absent; a minimal SK-09 vocabulary exists without full stage readiness.

## Decision

Keep type-specific validation in model-core. TypeValidator accepts the actual TypeDataComposition seam and mandatory TypeValidationContext(TypeLookup). TypeLookup declares only find(ElementRef)->SemanticElement|None; broad return supports separate missing/non-Type diagnostics without concrete Registry dependency. Views must be deterministic, unambiguous and identity-preserving; TYPE-07 can implement the Protocol later.

Always execute structural, field-constraint and semantic-reference core rules, then explicitly supplied additional rules. Core checks cannot be disabled/replaced. Rule IDs/order are stable, rule collections immutable, diagnostics aggregated deterministically and validity derived from ERROR severity. No service locator, mutable global registry, discovery, caching or source/metadata bag is added. External rule/provider implementations must honor the deterministic/read-only contract; programming failures propagate.

Canonical constructors retain field completeness/uniqueness, one data slot and local bound checks; do not duplicate their algorithms. A current-kind structural rule protects the provisional retained Protocol host boundary, whose external implementation may be mutable. Missing/empty data on a type host is valid.

One immutable validation-owned applicability policy permits string length/pattern, integer numeric bounds and decimal bounds/precision/scale; boolean/date/datetime/uuid admit no current value constraints. Integer bounds must be exact integral canonical text, without float/int conversion. Precision/scale remain independently declarable; patterns are never compiled. Presence/nullability stay field-level and independent across every variant.

Semantic targets require existence, matching identity and type-definition kind in the supplied view. Self/mutual refs are allowed; check each direct target without recursively judging its data. No latest/version selection occurs. Primitive value constraints on semantic types fail conservatively pending explicit ValueType/base-type support. Unknown constraints fail closed: constructors currently reject payloads, and defensive validation produces unsupported diagnostics if an entry reaches the boundary. No arbitrary payload admission is introduced.

Use frozen TypeValidationDiagnostic/TypeValidationPath/Severity as a type-specific seam because SK-11 is absent, not a claimed replacement for its future general Diagnostic/SemanticPath. Paths are readable coordinates with separate FieldId and ElementRef context, not identity/ordinals. No SourceLocation is put onto semantic definitions.

## Consequences

Valid representation remains distinct from semantic validity. Validation never fixes/canonicalizes/mutates definitions or validates instances. Current input is a provisional host/data wrapper tested with frozen test-only hosts, so production TYPE-01 integration is still incomplete. TYPE-07 needs no reverse dependency change to satisfy TypeLookup. Future ValueType propagation, full diagnostics and primitive semantics require explicit reconciliation. Compiler/runtime/SQL/API/UI validation, assignability/coercion, compatibility/migration and global model orchestration remain separate.

See [actual contracts, matrix and examples](../../model/type-validation.md).
