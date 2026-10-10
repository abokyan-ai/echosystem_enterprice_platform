"""Internal evolving snapshot mapping, not a final authoring schema or public API.

Only plain wire mappings cross this boundary. Model constructors own invariants;
no JSON/framework attributes enter definitions. Field shape remains an evolving snapshot schema.
"""
from semantic_kernel.public import PrimitiveType, ElementRef
from model_core.public import (
    TypeRef, TypeRefKind, PrimitiveTypeRef, SemanticTypeRef, TypeRefError,
    FieldPresence, FieldNullability, FieldConstraintSet, FieldConstraintError,
    MinLengthConstraint, MaxLengthConstraint, MinimumConstraint, MaximumConstraint,
    PrecisionConstraint, ScaleConstraint, PatternConstraint, NumericConstraintValue,
    ConstraintKind, FieldDefinition, FieldId, FieldName,
)


_CONSTRUCTORS = {
    'min-length': MinLengthConstraint,
    'max-length': MaxLengthConstraint,
    'minimum': MinimumConstraint,
    'maximum': MaximumConstraint,
    'pattern': PatternConstraint,
    'precision': PrecisionConstraint,
    'scale': ScaleConstraint,
}


def _shape(value, keys):
    if type(value) is not dict or set(value) != set(keys):
        raise FieldConstraintError('TYPE-CONSTRAINT-015', 'Snapshot mapping requires exactly its documented members.')


def constraints_to_wire(constraints: FieldConstraintSet) -> dict:
    if type(constraints) is not FieldConstraintSet:
        raise FieldConstraintError('TYPE-CONSTRAINT-015', 'Expected a typed FieldConstraintSet snapshot.')
    return {
        'presence': constraints.presence.value,
        'nullability': constraints.nullability.value,
        'values': [{'kind': str(c.kind), 'value': str(c.value) if isinstance(c.value, NumericConstraintValue) else c.value} for c in constraints.value_constraints],
    }


def constraints_from_wire(wire: dict) -> FieldConstraintSet:
    _shape(wire, ('presence', 'nullability', 'values'))
    if type(wire['presence']) is not str:
        raise FieldConstraintError('TYPE-CONSTRAINT-010', 'Wire presence requires canonical text.')
    if type(wire['nullability']) is not str:
        raise FieldConstraintError('TYPE-CONSTRAINT-011', 'Wire nullability requires canonical text.')
    try:
        presence = FieldPresence(wire['presence'])
    except (ValueError, TypeError):
        raise FieldConstraintError('TYPE-CONSTRAINT-010', 'Wire presence must use a canonical explicit string.') from None
    try:
        nullability = FieldNullability(wire['nullability'])
    except (ValueError, TypeError):
        raise FieldConstraintError('TYPE-CONSTRAINT-011', 'Wire nullability must use a canonical explicit string.') from None
    if type(wire['values']) is not list:
        raise FieldConstraintError('TYPE-CONSTRAINT-015', 'Wire values require an explicit array.')
    values = []
    for entry in wire['values']:
        _shape(entry, ('kind', 'value'))
        kind = ConstraintKind.parse(entry['kind'])
        constructor = _CONSTRUCTORS.get(str(kind))
        if constructor is None:
            raise FieldConstraintError('TYPE-CONSTRAINT-014', 'Valid kind has no supported concrete v0 wire payload.')
        values.append(constructor(entry['value']))
    return FieldConstraintSet.create(presence, nullability, values)


def field_to_wire(field: FieldDefinition) -> dict:
    if type(field) is not FieldDefinition:
        raise FieldConstraintError('TYPE-CONSTRAINT-015', 'Expected a typed FieldDefinition snapshot.')
    return {'id': str(field.id), 'name': str(field.name), 'type': type_ref_to_wire(field.type), 'constraints': constraints_to_wire(field.constraints)}


def field_from_wire(wire: dict) -> FieldDefinition:
    _shape(wire, ('id', 'name', 'type', 'constraints'))
    return FieldDefinition.create(FieldId.parse(wire['id']), FieldName.parse(wire['name']), type_ref_from_wire(wire['type']), constraints_from_wire(wire['constraints']))



def type_ref_to_wire(reference: TypeRef) -> dict:
    """Explicit internal discriminator; no repr/class-name/compact heuristics."""
    if type(reference) is PrimitiveTypeRef:
        return {'kind': reference.kind.value, 'primitive': str(reference.primitive)}
    if type(reference) is SemanticTypeRef:
        return {'kind': reference.kind.value, 'elementRef': str(reference.target)}
    raise TypeRefError('TYPE-REF-004', 'Expected a canonical primitive or semantic reference.')


def type_ref_from_wire(wire: dict) -> TypeRef:
    if wire is None:
        raise TypeRefError('TYPE-REF-001', 'Type reference wire value is required.')
    if type(wire) is not dict or type(wire.get('kind')) is not str:
        raise TypeRefError('TYPE-REF-004', 'Type reference requires an explicit canonical discriminator.')
    try:
        kind = TypeRefKind(wire['kind'])
    except ValueError:
        raise TypeRefError('TYPE-REF-004', 'Unsupported type reference discriminator.') from None
    key = 'primitive' if kind is TypeRefKind.PRIMITIVE else 'elementRef'
    if set(wire) != {'kind', key}:
        raise TypeRefError('TYPE-REF-004', 'Type reference requires exactly its variant members.')
    if kind is TypeRefKind.PRIMITIVE:
        return PrimitiveTypeRef(PrimitiveType.parse(wire[key]))
    return SemanticTypeRef(ElementRef.parse(wire[key]))
