"""Frozen test-only host and read-only view; not production TYPE-01 or TYPE-07."""
from dataclasses import dataclass
from semantic_kernel.public import (
    SemanticElementId, QualifiedName, SemanticContextRef, SemanticElementKind,
    SemanticElementKinds, SemanticVersion, ElementRef, PrimitiveTypes,
)
from model_core.public import (
    TypeDataComposition, DataFacet, FieldDefinition, FieldId, FieldName,
    PrimitiveTypeRef, FieldConstraintSet, FieldPresence, FieldNullability,
)


@dataclass(frozen=True, slots=True)
class ValidationHost:
    id: SemanticElementId
    qualified_name: QualifiedName
    context: SemanticContextRef
    kind: SemanticElementKind
    version: SemanticVersion


def host(number=0, name='sales.Customer', kind=SemanticElementKinds.TYPE_DEFINITION):
    return ValidationHost(SemanticElementId(f'sem_550e8400-e29b-41d4-a716-{number:012d}'), QualifiedName.parse(name), SemanticContextRef(SemanticElementId('sem_550e8400-e29b-41d4-a716-999999999999')), kind, SemanticVersion(1, 0, 0))


@dataclass(frozen=True, slots=True)
class ReadOnlyLookup:
    elements: tuple[ValidationHost, ...]

    def find(self, reference: ElementRef):
        return next((element for element in self.elements if element.id == reference.element_id), None)


PLAIN = FieldConstraintSet(FieldPresence.REQUIRED, FieldNullability.NON_NULL, ())


def field(reference=PrimitiveTypeRef(PrimitiveTypes.STRING), values=(), number=0, name='value', presence=FieldPresence.REQUIRED, nullability=FieldNullability.NON_NULL):
    return FieldDefinition(FieldId(f'fld_550e8400-e29b-41d4-a716-{number:012d}'), FieldName(name), reference, FieldConstraintSet(presence, nullability, values))


def definition(*fields, owner=None, absent=False):
    return TypeDataComposition(owner if owner is not None else host(), None if absent else DataFacet(fields))
