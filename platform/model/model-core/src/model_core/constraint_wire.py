"""Internal evolving snapshot mapping, not a final authoring schema or public API.

Only plain wire mappings cross this boundary. Model constructors own invariants;
no JSON/framework attributes enter definitions. TYPE-05 will evolve field shape.
"""
from model_core.public import (
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
    return {'id': str(field.id), 'name': str(field.name), 'constraints': constraints_to_wire(field.constraints)}


def field_from_wire(wire: dict) -> FieldDefinition:
    _shape(wire, ('id', 'name', 'constraints'))
    return FieldDefinition.create(FieldId.parse(wire['id']), FieldName.parse(wire['name']), constraints_from_wire(wire['constraints']))
