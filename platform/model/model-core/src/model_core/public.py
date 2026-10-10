"""Pure model contracts for owned semantic structural members."""
from dataclasses import dataclass as _dataclass, field as _field
import re as _re
from enum import Enum as _Enum
from decimal import Decimal as _Decimal
from typing import Protocol as _Protocol, Mapping as _Mapping
from types import MappingProxyType as _MappingProxyType
from semantic_kernel.public import Namespace, ElementVersionRef, PrimitiveTypes, PrimitiveType, ElementRef, FacetKind, FacetKinds, FacetApplicability, SemanticElementKind, SemanticElementKinds, SemanticElement, SemanticElementId, QualifiedName, SemanticContextRef, SemanticVersion

MODULE_NAME = "model-core"
__all__ = ["MODULE_NAME", "FieldId", "FieldIdError", "FieldName", "FieldNameError", "FieldDefinition", "FieldDefinitionError", "DataFacet", "DataFacetError", "DATA_FACET_APPLICABILITY", "TypeDataComposition", "FieldConstraintError", "FieldPresence", "FieldNullability", "ConstraintKind", "ConstraintKinds", "ValueConstraint", "NumericConstraintValue", "MinLengthConstraint", "MaxLengthConstraint", "MinimumConstraint", "MaximumConstraint", "PatternConstraint", "PrecisionConstraint", "ScaleConstraint", "FieldConstraintSet", "TypeRef", "TypeRefKind", "PrimitiveTypeRef", "SemanticTypeRef", "TypeRefError", "TypeLookup", "TypeValidationContext", "TypeValidationRule", "TypeValidationResult", "TypeValidator", "TypeValidationDiagnostic", "TypeValidationSeverity", "TypeValidationPath", "FieldConstraintValidationRule", "SemanticReferenceValidationRule", "primitive_constraint_kinds", "StructuralTypeValidationRule", "TypeRegistry", "TypeRegistrationResult", "TypeRegistrationOutcome", "TypeRegistrationFailure", "TypeRegistrationDiagnostic", "TypeRegistryLookup", "TypeRegistryAmbiguityError"]

# Same UUIDv4 representation strategy as SK-01, with distinct model-owned intent.
_FIELD_ID = _re.compile(r"fld_[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-4[0-9a-fA-F]{3}-[89aAbB][0-9a-fA-F]{3}-[0-9a-fA-F]{12}")
_FIELD_NAME = _re.compile(r"[A-Za-z][A-Za-z0-9_]*")


class FieldIdError(ValueError):
    """Field identity diagnostic without retaining rejected input."""
    def __init__(self, code: str, message: str):
        self.code = code
        self.message = message
        super().__init__(f"{code}: {message}")


@_dataclass(frozen=True, slots=True)
class FieldId:
    """Opaque fld_<UUIDv4> member identity, independent of name and owner spelling.

    Hex case normalizes to lowercase; prefix and UUID version/variant are strict.
    No generation, registry, name derivation or movement/migration inference.
    """
    value: str

    def __post_init__(self):
        value = self.value
        if value is None or isinstance(value, str) and (not value or str.isspace(value)):
            raise FieldIdError("TYPE-FIELD-001", "Field ID is required.")
        if not isinstance(value, str) or len(value) != 40 or _FIELD_ID.fullmatch(value) is None:
            raise FieldIdError("TYPE-FIELD-002", "Expected fld_ followed by a hyphenated UUIDv4 with the RFC variant.")
        object.__setattr__(self, "value", str.lower(value))

    @classmethod
    def parse(cls, value: str) -> "FieldId":
        return cls(value)

    @classmethod
    def try_parse(cls, value: object) -> "FieldId | None":
        """Return None for expected identity errors; unexpected failures propagate."""
        try:
            return cls(value)
        except FieldIdError:
            return None

    def __str__(self) -> str:
        return self.value


class FieldNameError(ValueError):
    """Local name diagnostic, without style or projection rules."""
    def __init__(self, code: str, message: str):
        self.code = code
        self.message = message
        super().__init__(f"{code}: {message}")


@_dataclass(frozen=True, slots=True)
class FieldName:
    """Case-sensitive local ASCII semantic identifier; never a QName or label."""
    value: str

    def __post_init__(self):
        value = self.value
        if value is None or isinstance(value, str) and (not value or str.isspace(value)):
            raise FieldNameError("TYPE-FIELD-003", "Field name is required.")
        if not isinstance(value, str) or _FIELD_NAME.fullmatch(value) is None:
            raise FieldNameError("TYPE-FIELD-004", "Expected a local ASCII letter followed by ASCII letters, digits or underscores; whitespace, dots and other separators are forbidden.")
        object.__setattr__(self, "value", str.__str__(value))

    @classmethod
    def parse(cls, value: str) -> "FieldName":
        return cls(value)

    @classmethod
    def try_parse(cls, value: object) -> "FieldName | None":
        """Return None for expected name errors; unexpected failures propagate."""
        try:
            return cls(value)
        except FieldNameError:
            return None

    def __str__(self) -> str:
        return self.value


class FieldDefinitionError(ValueError):
    """Typed construction diagnostic, independent of collection validation."""
    def __init__(self, code: str, message: str):
        self.code = code
        self.message = message
        super().__init__(f"{code}: {message}")


class FieldConstraintError(ValueError):
    """Local definition diagnostic; paths await SK-11, rejected input is not retained."""
    def __init__(self, code: str, message: str, constraint_index: int | None = None, previous_index: int | None = None):
        self.code = code
        self.message = message
        self.constraint_index = constraint_index
        self.previous_index = previous_index
        super().__init__(f"{code}: {message}")


class FieldPresence(_Enum):
    REQUIRED = "required"
    OPTIONAL = "optional"


class FieldNullability(_Enum):
    NULLABLE = "nullable"
    NON_NULL = "non-null"


_CONSTRAINT_SEGMENT = _re.compile(r"[a-z][a-z0-9]*(?:-[a-z0-9]+)*")


@_dataclass(frozen=True, slots=True)
class ConstraintKind:
    """Open lower-case dot/kebab identifier; identifier validity is not payload support.

    Model-owned vocabulary follows kernel kind spelling without importing its
    private parser or misusing FacetKind/SemanticElementKind identity types.
    """
    value: str

    def __post_init__(self):
        if not isinstance(self.value, str) or not self.value or any(_CONSTRAINT_SEGMENT.fullmatch(s) is None for s in str.split(self.value, '.')):
            raise FieldConstraintError("TYPE-CONSTRAINT-012", "Expected a canonical lower-case dot/kebab constraint kind.")
        object.__setattr__(self, 'value', str.__str__(self.value))

    @classmethod
    def parse(cls, value: str) -> "ConstraintKind":
        return cls(value)

    @classmethod
    def try_parse(cls, value: object) -> "ConstraintKind | None":
        try:
            return cls(value)
        except FieldConstraintError:
            return None

    def __str__(self) -> str:
        return self.value


@_dataclass(frozen=True, slots=True)
class _CoreConstraintKinds:
    MIN_LENGTH: ConstraintKind = ConstraintKind('min-length')
    MAX_LENGTH: ConstraintKind = ConstraintKind('max-length')
    MINIMUM: ConstraintKind = ConstraintKind('minimum')
    MAXIMUM: ConstraintKind = ConstraintKind('maximum')
    PATTERN: ConstraintKind = ConstraintKind('pattern')
    PRECISION: ConstraintKind = ConstraintKind('precision')
    SCALE: ConstraintKind = ConstraintKind('scale')

    @property
    def ALL(self) -> tuple[ConstraintKind, ...]:
        return (self.MIN_LENGTH, self.MAX_LENGTH, self.MINIMUM, self.MAXIMUM, self.PATTERN, self.PRECISION, self.SCALE)

    def is_core(self, kind: ConstraintKind) -> bool:
        return isinstance(kind, ConstraintKind) and kind in self.ALL


ConstraintKinds = _CoreConstraintKinds()


class ValueConstraint(_Protocol):
    """Structural definition contract only; each implementation owns its typed payload."""
    @property
    def kind(self) -> ConstraintKind:
        ...


_NUMERIC_LITERAL = _re.compile(r"-?[0-9]+(?:\.[0-9]+)?")


@_dataclass(frozen=True, slots=True)
class NumericConstraintValue:
    """Exact fixed-point ASCII text; up to 4096 digits, no exponent or binary float.

    Leading integer zeros, trailing fraction zeros and signed zero normalize.
    Decimal construction/comparison is exact and does not round to its context;
    no arithmetic or context-sensitive normalize operation is performed.
    """
    value: str

    def __post_init__(self):
        if not isinstance(self.value, str) or len(self.value) > 4098 or _NUMERIC_LITERAL.fullmatch(self.value) is None:
            raise FieldConstraintError("TYPE-CONSTRAINT-013", "Expected exact fixed-point ASCII numeric text, without exponent or whitespace, up to 4096 digits.")
        text = str.__str__(self.value)
        if sum(c in '0123456789' for c in text) > 4096:
            raise FieldConstraintError("TYPE-CONSTRAINT-013", "Numeric literal exceeds the 4096-digit representation limit.")
        negative = text.startswith('-')
        whole, dot, fraction = text.lstrip('-').partition('.')
        whole = whole.lstrip('0') or '0'
        fraction = fraction.rstrip('0')
        canonical = whole + ('.' + fraction if fraction else '')
        if negative and canonical != '0':
            canonical = '-' + canonical
        object.__setattr__(self, 'value', canonical)

    @classmethod
    def parse(cls, value: str) -> "NumericConstraintValue":
        return cls(value)

    @classmethod
    def try_parse(cls, value: object) -> "NumericConstraintValue | None":
        try:
            return cls(value)
        except FieldConstraintError:
            return None

    def __str__(self) -> str:
        return self.value


def _integer_payload(value: object, minimum: int, code: str):
    if type(value) is not int or value < minimum:
        raise FieldConstraintError(code, "Constraint requires a plain integer within its non-negative/positive domain.")


@_dataclass(frozen=True, slots=True)
class MinLengthConstraint:
    value: int

    def __post_init__(self):
        _integer_payload(self.value, 0, "TYPE-CONSTRAINT-001")

    @property
    def kind(self) -> ConstraintKind:
        return ConstraintKinds.MIN_LENGTH


@_dataclass(frozen=True, slots=True)
class MaxLengthConstraint:
    value: int

    def __post_init__(self):
        _integer_payload(self.value, 0, "TYPE-CONSTRAINT-002")

    @property
    def kind(self) -> ConstraintKind:
        return ConstraintKinds.MAX_LENGTH


@_dataclass(frozen=True, slots=True)
class PrecisionConstraint:
    """Maximum total decimal digits; applicability is deferred to TYPE-06."""
    value: int

    def __post_init__(self):
        _integer_payload(self.value, 1, "TYPE-CONSTRAINT-005")

    @property
    def kind(self) -> ConstraintKind:
        return ConstraintKinds.PRECISION


@_dataclass(frozen=True, slots=True)
class ScaleConstraint:
    """Declared fractional decimal digits; no rounding or execution policy here."""
    value: int

    def __post_init__(self):
        _integer_payload(self.value, 0, "TYPE-CONSTRAINT-006")

    @property
    def kind(self) -> ConstraintKind:
        return ConstraintKinds.SCALE


@_dataclass(frozen=True, slots=True)
class MinimumConstraint:
    """Inclusive exact lower bound, independent of future target type."""
    value: NumericConstraintValue

    def __post_init__(self):
        # Explicit convenience parsing retains a typed canonical payload.
        if isinstance(self.value, str):
            object.__setattr__(self, 'value', NumericConstraintValue.parse(self.value))
        if type(self.value) is not NumericConstraintValue:
            raise FieldConstraintError("TYPE-CONSTRAINT-013", "Numeric bound requires NumericConstraintValue or exact numeric text.")

    @property
    def kind(self) -> ConstraintKind:
        return ConstraintKinds.MINIMUM


@_dataclass(frozen=True, slots=True)
class MaximumConstraint:
    """Inclusive exact upper bound, independent of future target type."""
    value: NumericConstraintValue

    def __post_init__(self):
        if isinstance(self.value, str):
            object.__setattr__(self, 'value', NumericConstraintValue.parse(self.value))
        if type(self.value) is not NumericConstraintValue:
            raise FieldConstraintError("TYPE-CONSTRAINT-013", "Numeric bound requires NumericConstraintValue or exact numeric text.")

    @property
    def kind(self) -> ConstraintKind:
        return ConstraintKinds.MAXIMUM


@_dataclass(frozen=True, slots=True)
class PatternConstraint:
    """Non-empty exact pattern text, not compiled/evaluated or portability-certified.

    Regex dialect/syntax and execution limits await compiler/runtime design.
    No trim, anchoring, engine flags or assumed full-match/search semantics.
    """
    value: str

    def __post_init__(self):
        if not isinstance(self.value, str) or not self.value:
            raise FieldConstraintError("TYPE-CONSTRAINT-009", "Pattern requires non-empty text; engine syntax is not evaluated here.")
        object.__setattr__(self, 'value', str.__str__(self.value))

    @property
    def kind(self) -> ConstraintKind:
        return ConstraintKinds.PATTERN


_BUILTIN_CONSTRAINT_TYPES = (MinLengthConstraint, MaxLengthConstraint, MinimumConstraint, MaximumConstraint, PatternConstraint, PrecisionConstraint, ScaleConstraint)


@_dataclass(frozen=True, slots=True)
class FieldConstraintSet:
    """Explicit presence/nullability and normalized, immutable built-in values.

    At most one of each kind; kind-sorted enumeration, equality and hash ignore
    input order. Closed concrete v0 set prevents mutable/unknown payload escape
    hatches while ConstraintKind remains open. No type inference or validation.
    """
    presence: FieldPresence
    nullability: FieldNullability
    value_constraints: tuple[ValueConstraint, ...]

    def __post_init__(self):
        if not isinstance(self.presence, FieldPresence):
            raise FieldConstraintError("TYPE-CONSTRAINT-010", "Explicit typed field presence is required.")
        if not isinstance(self.nullability, FieldNullability):
            raise FieldConstraintError("TYPE-CONSTRAINT-011", "Explicit typed field nullability is required.")
        if type(self.value_constraints) not in (tuple, list):
            raise FieldConstraintError("TYPE-CONSTRAINT-014", "Values require an explicit ordered list or tuple of built-in constraints.")
        values = tuple(self.value_constraints)
        by_kind = {}
        indices = {}
        for index, constraint in enumerate(values):
            if type(constraint) not in _BUILTIN_CONSTRAINT_TYPES:
                raise FieldConstraintError("TYPE-CONSTRAINT-014", "Unsupported or invalid concrete v0 constraint.", index)
            if constraint.kind in by_kind:
                raise FieldConstraintError("TYPE-CONSTRAINT-008", "Duplicate constraint kind; implicit replacement is forbidden.", index, indices[constraint.kind])
            by_kind[constraint.kind] = constraint
            indices[constraint.kind] = index
        for lower, upper, code in ((ConstraintKinds.MIN_LENGTH, ConstraintKinds.MAX_LENGTH, '003'), (ConstraintKinds.MINIMUM, ConstraintKinds.MAXIMUM, '004'), (ConstraintKinds.SCALE, ConstraintKinds.PRECISION, '007')):
            if lower in by_kind and upper in by_kind:
                a, b = by_kind[lower].value, by_kind[upper].value
                if lower == ConstraintKinds.MINIMUM:
                    a, b = _Decimal(str(a)), _Decimal(str(b))
                if a > b:
                    raise FieldConstraintError('TYPE-CONSTRAINT-' + code, "Local constraint lower bound exceeds its upper bound.")
        object.__setattr__(self, 'value_constraints', tuple(sorted(values, key=lambda c: str(c.kind))))

    @classmethod
    def create(cls, presence: FieldPresence, nullability: FieldNullability, value_constraints: tuple[ValueConstraint, ...] | list[ValueConstraint]) -> "FieldConstraintSet":
        return cls(presence, nullability, value_constraints)

    def find_by_kind(self, kind: ConstraintKind) -> ValueConstraint | None:
        if not isinstance(kind, ConstraintKind):
            raise FieldConstraintError("TYPE-CONSTRAINT-012", "Constraint lookup requires a typed ConstraintKind.")
        return next((c for c in self.value_constraints if c.kind == kind), None)


class TypeRefError(ValueError):
    """Reference construction error, never an existence/kind-resolution diagnostic."""
    def __init__(self, code: str, message: str):
        self.code = code
        self.message = message
        super().__init__(f"{code}: {message}")


class TypeRefKind(_Enum):
    PRIMITIVE = 'primitive'
    SEMANTIC = 'semantic'


@_dataclass(frozen=True, slots=True)
class PrimitiveTypeRef:
    """Built-in semantic primitive reference; never a raw or programming type."""
    primitive: PrimitiveType

    def __post_init__(self):
        if type(self.primitive) is not PrimitiveType:
            raise TypeRefError('TYPE-REF-002', 'Primitive reference requires a validated PrimitiveType.')

    @property
    def kind(self) -> TypeRefKind:
        return TypeRefKind.PRIMITIVE


@_dataclass(frozen=True, slots=True)
class SemanticTypeRef:
    """Identity-pinned intent to target a TypeDefinition; no lookup is performed.

    Target existence/kind and exact version resolution require later model context.
    No host object, name hint, registry, optional version or relationship semantics.
    """
    target: ElementRef

    def __post_init__(self):
        if self.target is None:
            raise TypeRefError('TYPE-REF-005', 'Semantic type reference target is required.')
        if type(self.target) is not ElementRef:
            raise TypeRefError('TYPE-REF-003', 'Semantic type reference requires an identity-only ElementRef.')

    @property
    def kind(self) -> TypeRefKind:
        return TypeRefKind.SEMANTIC


# Closed two-variant algebra, not a Protocol accepting arbitrary unknown payloads.
TypeRef = PrimitiveTypeRef | SemanticTypeRef


@_dataclass(frozen=True, slots=True)
class FieldDefinition:
    """Owned structural member snapshot, not a first-class SemanticElement.

    Compare .id for identity; snapshot equality/hash includes explicit constraints.
    Required TypeRef records semantic intent; no type inference or owner back pointers.
    """
    id: FieldId
    name: FieldName
    type: TypeRef
    constraints: FieldConstraintSet

    def __post_init__(self):
        if self.id is None:
            raise FieldDefinitionError("TYPE-FIELD-001", "Field ID is required.")
        if not isinstance(self.id, FieldId):
            raise FieldDefinitionError("TYPE-FIELD-002", "Field definition requires a validated FieldId value.")
        if self.name is None:
            raise FieldDefinitionError("TYPE-FIELD-003", "Field name is required.")
        if not isinstance(self.name, FieldName):
            raise FieldDefinitionError("TYPE-FIELD-004", "Field definition requires a validated FieldName value.")

        if self.type is None:
            raise TypeRefError('TYPE-REF-001', 'Field type reference is required.')
        if type(self.type) not in (PrimitiveTypeRef, SemanticTypeRef):
            raise TypeRefError('TYPE-REF-004', 'Field type requires one of the two canonical TypeRef variants.')
        if type(self.constraints) is not FieldConstraintSet:
            raise FieldDefinitionError("TYPE-FIELD-005", "Field definition requires an explicit FieldConstraintSet.")

    @classmethod
    def create(cls, id: FieldId, name: FieldName, type: TypeRef, constraints: FieldConstraintSet) -> "FieldDefinition":
        """Construct from typed values without reparsing, generation or lookup."""
        return cls(id, name, type, constraints)


class DataFacetError(ValueError):
    """Deterministic local structural/composition diagnostic without rejected input."""
    def __init__(self, code: str, message: str, field_index: int | None = None, previous_index: int | None = None):
        self.code = code
        self.message = message
        self.field_index = field_index
        self.previous_index = previous_index
        super().__init__(f"{code}: {message}")


DATA_FACET_APPLICABILITY = FacetApplicability(FacetKinds.DATA, frozenset({SemanticElementKinds.TYPE_DEFINITION}))


@_dataclass(frozen=True, slots=True)
class DataFacet:
    """Ordered immutable structural membership; fixed data concern, not instance values.

    Local uniqueness/case portability only, without type/constraint/projection rules.
    """
    fields: tuple[FieldDefinition, ...]

    def __post_init__(self):
        if type(self.fields) not in (tuple, list):
            raise DataFacetError("TYPE-DATA-004", "Fields require an explicit ordered list or tuple of FieldDefinition snapshots.")
        fields = tuple(self.fields)
        ids = {}
        names = {}
        folded = {}
        for index, field in enumerate(fields):
            if not isinstance(field, FieldDefinition):
                raise DataFacetError("TYPE-DATA-004", "DataFacet contains an invalid or null FieldDefinition.", index)
            if field.id in ids:
                raise DataFacetError("TYPE-DATA-001", "Duplicate FieldId in DataFacet.", index, ids[field.id])
            if field.name in names:
                raise DataFacetError("TYPE-DATA-002", "Duplicate FieldName in DataFacet.", index, names[field.name])
            key = str(field.name).lower()  # FieldName grammar is ASCII; locale-independent.
            if key in folded:
                raise DataFacetError("TYPE-DATA-003", "Field-name portability collision in DataFacet.", index, folded[key])
            ids[field.id] = index
            names[field.name] = index
            folded[key] = index
        object.__setattr__(self, "fields", fields)

    @property
    def kind(self) -> FacetKind:
        return FacetKinds.DATA

    @classmethod
    def create(cls, fields: tuple[FieldDefinition, ...] | list[FieldDefinition]) -> "DataFacet":
        return cls(fields)

    def find_by_id(self, id: FieldId) -> FieldDefinition | None:
        """Exact typed lookup; missing returns None, never an approximate match."""
        if not isinstance(id, FieldId):
            raise DataFacetError("TYPE-DATA-004", "ID lookup requires a validated FieldId.")
        return next((field for field in self.fields if field.id == id), None)

    def find_by_name(self, name: FieldName) -> FieldDefinition | None:
        """Case-sensitive typed lookup; collision validation does not change equality."""
        if not isinstance(name, FieldName):
            raise DataFacetError("TYPE-DATA-004", "Name lookup requires a validated FieldName.")
        return next((field for field in self.fields if field.name == name), None)


@_dataclass(frozen=True, slots=True)
class TypeDataComposition:
    """Minimal explicit host/data association, without duplicate structural fields.

    Host must supply the five typed SemanticElement properties and type-definition
    kind. Concrete hosts own immutable snapshot invariants; this wrapper retains
    their reference rather than implementing TypeDefinition or copying its state.
    None means absent; DataFacet(()) means explicitly empty. Future general facet
    hosting requires its own design, not an untyped map or merge here.
    """
    type_definition: SemanticElement
    data: DataFacet | None = None

    def __post_init__(self):
        expected = (("id", SemanticElementId), ("qualified_name", QualifiedName), ("context", SemanticContextRef), ("kind", SemanticElementKind), ("version", SemanticVersion))
        if any(not isinstance(getattr(self.type_definition, name, None), value_type) for name, value_type in expected):
            raise DataFacetError("TYPE-DATA-006", "Type data composition requires all five typed SemanticElement properties.")
        if self.type_definition.kind not in DATA_FACET_APPLICABILITY.allowed_element_kinds:
            raise DataFacetError("TYPE-DATA-006", "DataFacet v0 is applicable only to type-definition hosts.")
        if self.data is not None and not isinstance(self.data, DataFacet):
            raise DataFacetError("TYPE-DATA-005", "Exactly one DataFacet or None is permitted; duplicate facets and implicit merging are forbidden.")


# TYPE-06: definition validation. No instance values, registry or physical adapters.
class TypeValidationSeverity(_Enum):
    ERROR = 'error'
    WARNING = 'warning'
    INFO = 'info'


@_dataclass(frozen=True, slots=True)
class TypeValidationPath:
    """Provisional typed model path pending SK-11, never semantic identity.

    QName/field name render a readable coordinate; diagnostics retain FieldId
    separately for identity across field reorder/rename. No ordinal/source bag.
    """
    type_name: QualifiedName
    field_name: FieldName | None = None
    constraint_kind: ConstraintKind | None = None

    def __post_init__(self):
        if not isinstance(self.type_name, QualifiedName):
            raise TypeError('Validation path requires a typed QualifiedName.')
        if self.field_name is not None and not isinstance(self.field_name, FieldName):
            raise TypeError('Validation path requires a typed FieldName.')
        if self.constraint_kind is not None and (not isinstance(self.constraint_kind, ConstraintKind) or self.field_name is None):
            raise TypeError('Constraint path requires a typed kind and a field coordinate.')

    def __str__(self) -> str:
        text = str(self.type_name)
        if self.field_name is not None:
            text += '.data.fields.' + str(self.field_name)
        if self.constraint_kind is not None:
            text += '.constraints.' + str(self.constraint_kind)
        return text


@_dataclass(frozen=True, slots=True)
class TypeValidationDiagnostic:
    """Type-specific diagnostic seam, not a replacement/full SK-11 core model."""
    code: str
    message: str
    severity: TypeValidationSeverity
    path: TypeValidationPath
    field_id: FieldId | None = None
    target: ElementRef | None = None

    def __post_init__(self):
        if type(self.code) is not str or _re.fullmatch(r'TYPE-VAL-(?:[A-Z]+-)?[0-9]{3}', self.code) is None:
            raise ValueError('Expected a stable TYPE-VAL diagnostic code.')
        if type(self.message) is not str or not self.message:
            raise ValueError('Diagnostic requires a non-empty message.')
        if not isinstance(self.severity, TypeValidationSeverity) or type(self.path) is not TypeValidationPath:
            raise TypeError('Diagnostic requires typed severity and path.')
        if self.field_id is not None and not isinstance(self.field_id, FieldId):
            raise TypeError('Diagnostic field identity must be a FieldId.')
        if self.target is not None and type(self.target) is not ElementRef:
            raise TypeError('Diagnostic target must be an identity-only ElementRef.')


class TypeLookup(_Protocol):
    """Read-only unambiguous semantic-element view, without registration/version selection.

    A broad return permits distinct missing versus existing non-Type diagnostics.
    Implementations must return the requested identity in a stable model snapshot.
    """
    def find(self, reference: ElementRef) -> SemanticElement | None:
        ...


@_dataclass(frozen=True, slots=True)
class TypeValidationContext:
    """Mandatory supplied lookup: full validation never silently skips references."""
    type_lookup: TypeLookup

    def __post_init__(self):
        if not callable(getattr(self.type_lookup, 'find', None)):
            raise TypeError('Full type validation requires a read-only TypeLookup implementation.')


class TypeValidationRule(_Protocol):
    @property
    def id(self) -> str:
        ...

    def validate(self, type_definition: TypeDataComposition, context: TypeValidationContext) -> tuple[TypeValidationDiagnostic, ...]:
        ...


@_dataclass(frozen=True, slots=True)
class TypeValidationResult:
    diagnostics: tuple[TypeValidationDiagnostic, ...]

    def __post_init__(self):
        if type(self.diagnostics) not in (list, tuple) or any(type(d) is not TypeValidationDiagnostic for d in self.diagnostics):
            raise TypeError('Validation result requires explicit typed diagnostics.')
        object.__setattr__(self, 'diagnostics', tuple(self.diagnostics))

    @property
    def is_valid(self) -> bool:
        return not any(d.severity is TypeValidationSeverity.ERROR for d in self.diagnostics)


# Single immutable policy definition: rows and permitted sets cannot be mutated.
_PRIMITIVE_CONSTRAINT_POLICY = (
    (PrimitiveTypes.STRING, frozenset({ConstraintKinds.MIN_LENGTH, ConstraintKinds.MAX_LENGTH, ConstraintKinds.PATTERN})),
    (PrimitiveTypes.BOOLEAN, frozenset()),
    (PrimitiveTypes.INTEGER, frozenset({ConstraintKinds.MINIMUM, ConstraintKinds.MAXIMUM})),
    (PrimitiveTypes.DECIMAL, frozenset({ConstraintKinds.MINIMUM, ConstraintKinds.MAXIMUM, ConstraintKinds.PRECISION, ConstraintKinds.SCALE})),
    (PrimitiveTypes.DATE, frozenset()),
    (PrimitiveTypes.DATETIME, frozenset()),
    (PrimitiveTypes.UUID, frozenset()),
)


def primitive_constraint_kinds(primitive: PrimitiveType) -> frozenset[ConstraintKind]:
    """Validation-owned v0 applicability policy, also usable for documentation."""
    if type(primitive) is not PrimitiveType:
        raise TypeError('Constraint policy requires a validated PrimitiveType.')
    return next(kinds for candidate, kinds in _PRIMITIVE_CONSTRAINT_POLICY if candidate == primitive)


def _type_diagnostic(code: str, message: str, definition: TypeDataComposition, field: FieldDefinition, kind: ConstraintKind | None = None, target: ElementRef | None = None) -> TypeValidationDiagnostic:
    return TypeValidationDiagnostic(code, message, TypeValidationSeverity.ERROR, TypeValidationPath(definition.type_definition.qualified_name, field.name, kind), field.id, target)


@_dataclass(frozen=True, slots=True)
class StructuralTypeValidationRule:
    """Check current host kind across the provisional retained Protocol boundary.

    Canonical constructors own field completeness/uniqueness and one data slot;
    do not repeat those algorithms. A mutable external host could change kind
    after composition construction, so check its current semantic category.
    """
    @property
    def id(self) -> str:
        return 'TYPE-RULE-STRUCTURAL'

    def validate(self, type_definition: TypeDataComposition, context: TypeValidationContext) -> tuple[TypeValidationDiagnostic, ...]:
        if type_definition.type_definition.kind != SemanticElementKinds.TYPE_DEFINITION:
            return (TypeValidationDiagnostic('TYPE-VAL-STRUCTURAL-001', 'Validation subject is not a type-definition; data facet applicability is not satisfied.', TypeValidationSeverity.ERROR, TypeValidationPath(type_definition.type_definition.qualified_name)),)
        return ()


@_dataclass(frozen=True, slots=True)
class FieldConstraintValidationRule:
    """Applicability/unsupported/integer exact-bound checks; no local revalidation."""
    @property
    def id(self) -> str:
        return 'TYPE-RULE-FIELD-CONSTRAINT'

    def validate(self, type_definition: TypeDataComposition, context: TypeValidationContext) -> tuple[TypeValidationDiagnostic, ...]:
        diagnostics = []
        fields = type_definition.data.fields if type_definition.data is not None else ()
        for field in fields:
            for constraint in field.constraints.value_constraints:
                # Canonical constructors currently close payload admission. Keep
                # this fail-closed boundary for future extensions/unsafe input;
                # do not introduce arbitrary custom payloads to exercise it.
                kind = getattr(constraint, 'kind', None)
                if type(constraint) not in _BUILTIN_CONSTRAINT_TYPES:
                    diagnostics.append(_type_diagnostic('TYPE-VAL-CONSTRAINT-003', 'Constraint is unsupported by the current semantic type validator.', type_definition, field, kind if isinstance(kind, ConstraintKind) else None))
                    continue
                if type(field.type) is SemanticTypeRef or kind not in primitive_constraint_kinds(field.type.primitive):
                    diagnostics.append(_type_diagnostic('TYPE-VAL-CONSTRAINT-001', 'Constraint is not applicable to the declared field type.', type_definition, field, kind))
                elif field.type.primitive == PrimitiveTypes.INTEGER and type(constraint) in (MinimumConstraint, MaximumConstraint) and '.' in str(constraint.value):
                    # TYPE-04 canonicalizes fractional trailing zeros: 1.0 is 1.
                    # Exact textual integrality, no float/int conversion or width.
                    diagnostics.append(_type_diagnostic('TYPE-VAL-CONSTRAINT-002', 'Integer field bound must be an integral value.', type_definition, field, kind))
        return tuple(diagnostics)


@_dataclass(frozen=True, slots=True)
class SemanticReferenceValidationRule:
    """Check current field targets once, without recursively validating target data."""
    @property
    def id(self) -> str:
        return 'TYPE-RULE-SEMANTIC-REFERENCE'

    def validate(self, type_definition: TypeDataComposition, context: TypeValidationContext) -> tuple[TypeValidationDiagnostic, ...]:
        diagnostics = []
        fields = type_definition.data.fields if type_definition.data is not None else ()
        for field in fields:
            if type(field.type) is not SemanticTypeRef:
                continue
            reference = field.type.target
            target = context.type_lookup.find(reference)
            if target is None:
                diagnostics.append(_type_diagnostic('TYPE-VAL-REF-001', 'Unable to resolve semantic type reference.', type_definition, field, target=reference))
                continue
            expected = (("id", SemanticElementId), ("qualified_name", QualifiedName), ("context", SemanticContextRef), ("kind", SemanticElementKind), ("version", SemanticVersion))
            if any(not isinstance(getattr(target, name, None), value_type) for name, value_type in expected):
                raise TypeError('TypeLookup returned an object outside its typed SemanticElement contract.')
            if target.id != reference.element_id:
                diagnostics.append(_type_diagnostic('TYPE-VAL-REF-003', 'Lookup returned a different semantic identity than requested.', type_definition, field, target=reference))
            elif target.kind != SemanticElementKinds.TYPE_DEFINITION:
                diagnostics.append(_type_diagnostic('TYPE-VAL-REF-002', 'Semantic type reference does not target a type-definition.', type_definition, field, target=reference))
        return tuple(diagnostics)


@_dataclass(frozen=True, slots=True)
class TypeValidator:
    """Full current-definition pipeline: mandatory core plus explicit extra rules.

    TYPE-01 is absent; the existing TypeDataComposition host/data seam is the
    actual accepted input. Constructors protect structural/local invariants.
    Rules run in core order, then supplied order; field/kind order is preserved.
    No intrinsic-only mode, missing lookup, global discovery, recursion or cache.
    Additional rules cannot replace/disable core checks or repair the model.
    """
    additional_rules: tuple[TypeValidationRule, ...] = ()

    def __post_init__(self):
        if type(self.additional_rules) not in (tuple, list):
            raise TypeError('Additional rules require an explicit ordered collection.')
        rules = tuple(self.additional_rules)
        ids = {StructuralTypeValidationRule().id, FieldConstraintValidationRule().id, SemanticReferenceValidationRule().id}
        for rule in rules:
            id = getattr(rule, 'id', None)
            if type(id) is not str or _re.fullmatch(r'TYPE-RULE-[A-Z0-9]+(?:-[A-Z0-9]+)*', id) is None or not callable(getattr(rule, 'validate', None)):
                raise TypeError('Expected a typed rule with stable ID and validate method.')
            if id in ids:
                raise ValueError('Duplicate validation rule ID; core rules cannot be replaced.')
            ids.add(id)
        object.__setattr__(self, 'additional_rules', rules)

    @property
    def rules(self) -> tuple[TypeValidationRule, ...]:
        return (StructuralTypeValidationRule(), FieldConstraintValidationRule(), SemanticReferenceValidationRule(), *self.additional_rules)

    def validate(self, type_definition: TypeDataComposition, context: TypeValidationContext) -> TypeValidationResult:
        if type(type_definition) is not TypeDataComposition or type(context) is not TypeValidationContext:
            raise TypeError('Full validation requires canonical TypeDataComposition and explicit TypeValidationContext.')
        diagnostics = []
        for rule in self.rules:
            result = TypeValidationResult(rule.validate(type_definition, context))
            diagnostics.extend(result.diagnostics)
        return TypeValidationResult(diagnostics)


# TYPE-07: context-scoped immutable registration, separate from TYPE-06 judgment.
class TypeRegistrationFailure(_Enum):
    INVALID_REGISTRY_ENTRY = 'TYPE-REG-001'
    UNSUPPORTED_ELEMENT_KIND = 'TYPE-REG-002'
    SCOPE_MISMATCH = 'TYPE-REG-003'
    DUPLICATE_CONFLICT = 'TYPE-REG-004'
    QUALIFIED_NAME_COLLISION = 'TYPE-REG-005'


class TypeRegistrationOutcome(_Enum):
    REGISTERED = 'registered'
    ALREADY_REGISTERED = 'already-registered'
    REJECTED = 'rejected'


@_dataclass(frozen=True, slots=True)
class TypeRegistrationDiagnostic:
    """Registration-specific typed diagnostic seam pending SK-11, not a framework."""
    code: TypeRegistrationFailure
    message: str
    reference: ElementVersionRef | None = None
    qualified_name: QualifiedName | None = None
    context: SemanticContextRef | None = None

    def __post_init__(self):
        if type(self.code) is not TypeRegistrationFailure or type(self.message) is not str or not self.message:
            raise TypeError('Registration diagnostics require a supported code and message.')
        for value, expected in ((self.reference, ElementVersionRef), (self.qualified_name, QualifiedName), (self.context, SemanticContextRef)):
            if value is not None and type(value) is not expected:
                raise TypeError('Registration diagnostic coordinates require canonical typed values.')

    @property
    def severity(self) -> TypeValidationSeverity:
        return TypeValidationSeverity.ERROR

    @property
    def path(self) -> TypeValidationPath | None:
        return None if self.qualified_name is None else TypeValidationPath(self.qualified_name)


@_dataclass(frozen=True, slots=True)
class _RegisteredTypeElement:
    """Five-property immutable capture of the provisional host; not full TYPE-01."""
    id: SemanticElementId
    qualified_name: QualifiedName
    context: SemanticContextRef
    kind: SemanticElementKind
    version: SemanticVersion


class TypeRegistryAmbiguityError(ValueError):
    """Bare-ID TypeLookup cannot express several versions; bind an explicit view."""
    def __init__(self, references: tuple[ElementVersionRef, ...]):
        self.code = 'TYPE-REG-006'
        self.references = references
        super().__init__('TYPE-REG-006: Multiple registered versions; supply an explicit version-bound lookup view.')


@_dataclass(frozen=True, slots=True)
class TypeRegistry:
    """One context, copy-on-write indexes, no latest/default/version inference.

    Stores current TypeDataComposition contracts, capturing the five host values
    to prevent external Protocol-host mutation. Known facets have structural
    equality. Unknown host extension members are outside this provisional seam.
    Names belong to recorded versions, with historical ownership reserved.
    """
    context: SemanticContextRef
    _exact_index: _Mapping[ElementVersionRef, TypeDataComposition] = _field(init=False, repr=False, compare=True, default_factory=lambda: _MappingProxyType({}))
    _identity_index: _Mapping[SemanticElementId, tuple[TypeDataComposition, ...]] = _field(init=False, repr=False, compare=False, default_factory=lambda: _MappingProxyType({}))
    _name_index: _Mapping[QualifiedName, tuple[TypeDataComposition, ...]] = _field(init=False, repr=False, compare=False, default_factory=lambda: _MappingProxyType({}))

    def __post_init__(self):
        if type(self.context) is not SemanticContextRef or type(self.context.context_id) is not SemanticElementId:
            raise TypeError('Registry requires one explicit canonical semantic context.')

    @property
    def entries(self) -> tuple[TypeDataComposition, ...]:
        """ID scalar order then existing numeric SemanticVersion order."""
        return tuple(self._exact_index.values())

    def register(self, definition: TypeDataComposition) -> 'TypeRegistrationResult':
        """Return a new snapshot on success; expected failures retain this snapshot.

        Only registration structure is checked. No validator execution, repair,
        serialization/hash comparison or reference traversal takes place.
        """
        if type(definition) is not TypeDataComposition:
            owner = _registry_capture_owner(definition)
            code = TypeRegistrationFailure.UNSUPPORTED_ELEMENT_KIND if owner is not None and owner.kind != SemanticElementKinds.TYPE_DEFINITION else TypeRegistrationFailure.INVALID_REGISTRY_ENTRY
            return _registration_rejected(self, code, 'Expected the existing TypeDataComposition registration contract.', owner)
        owner = _registry_capture_owner(definition.type_definition)
        if owner is None:
            return _registration_rejected(self, TypeRegistrationFailure.INVALID_REGISTRY_ENTRY, 'Expected all five canonical typed semantic identity properties.')
        if owner.kind != SemanticElementKinds.TYPE_DEFINITION:
            return _registration_rejected(self, TypeRegistrationFailure.UNSUPPORTED_ELEMENT_KIND, 'Only type-definition hosts may be registered.', owner)
        if owner.context != self.context:
            return _registration_rejected(self, TypeRegistrationFailure.SCOPE_MISMATCH, 'Definition context differs from registry scope.', owner)
        if not _registry_data_is_canonical(definition.data):
            return _registration_rejected(self, TypeRegistrationFailure.INVALID_REGISTRY_ENTRY, 'Only canonical immutable DataFacet/field/constraint snapshots may be registered.', owner)
        entry = TypeDataComposition(owner, definition.data)
        reference = ElementVersionRef(owner.id, owner.version)
        existing = self._exact_index.get(reference)
        if existing is not None:
            if existing == entry:
                return TypeRegistrationResult(self, TypeRegistrationOutcome.ALREADY_REGISTERED)
            return _registration_rejected(self, TypeRegistrationFailure.DUPLICATE_CONFLICT, 'The exact identity/version already has different registration content.', owner)
        named = self._name_index.get(owner.qualified_name, ())
        if named and named[0].type_definition.id != owner.id:
            return _registration_rejected(self, TypeRegistrationFailure.QUALIFIED_NAME_COLLISION, 'Qualified name is owned by another identity in this context.', owner)
        return TypeRegistrationResult(_registry_snapshot(self.context, (*self.entries, entry)), TypeRegistrationOutcome.REGISTERED)

    def find_by_id(self, id: SemanticElementId) -> tuple[TypeDataComposition, ...]:
        if type(id) is not SemanticElementId:
            raise TypeError('ID lookup requires a canonical SemanticElementId.')
        return self._identity_index.get(id, ())

    def find_by_version(self, reference: ElementVersionRef) -> TypeDataComposition | None:
        if type(reference) is not ElementVersionRef or type(reference.element_id) is not SemanticElementId or type(reference.version) is not SemanticVersion:
            raise TypeError('Exact lookup requires a canonical ElementVersionRef.')
        return self._exact_index.get(reference)

    def find_by_qualified_name(self, name: QualifiedName) -> tuple[TypeDataComposition, ...]:
        if type(name) is not QualifiedName or type(name.namespace) is not Namespace:
            raise TypeError('Name lookup requires a canonical QualifiedName.')
        return self._name_index.get(name, ())

    def list_versions(self, id: SemanticElementId) -> tuple[SemanticVersion, ...]:
        return tuple(entry.type_definition.version for entry in self.find_by_id(id))

    def contains(self, reference: ElementVersionRef) -> bool:
        return self.find_by_version(reference) is not None

    def find(self, reference: ElementRef) -> SemanticElement | None:
        """TYPE-06 lookup only when an identity has zero or one version.

        Several versions are an explicit orchestration error, never missing or
        latest. Use bind_versions for a total unambiguous TypeLookup view.
        """
        if type(reference) is not ElementRef or type(reference.element_id) is not SemanticElementId:
            raise TypeError('TypeLookup requires a canonical identity-only ElementRef.')
        entries = self.find_by_id(reference.element_id)
        if len(entries) > 1:
            raise TypeRegistryAmbiguityError(tuple(ElementVersionRef(e.type_definition.id, e.type_definition.version) for e in entries))
        return None if not entries else entries[0].type_definition

    def bind_versions(self, references: tuple[ElementVersionRef, ...] | list[ElementVersionRef]) -> 'TypeRegistryLookup':
        """Explicit selected-only view; unselected identities are absent in it."""
        return TypeRegistryLookup(self, references)


def _registry_capture_owner(source: SemanticElement) -> _RegisteredTypeElement | None:
    values = tuple(getattr(source, name, None) for name in ('id', 'qualified_name', 'context', 'kind', 'version'))
    expected = (SemanticElementId, QualifiedName, SemanticContextRef, SemanticElementKind, SemanticVersion)
    if any(type(value) is not value_type for value, value_type in zip(values, expected)) or type(values[1].namespace) is not Namespace or type(values[2].context_id) is not SemanticElementId:
        return None
    return _RegisteredTypeElement(*values)


def _registry_data_is_canonical(data: DataFacet | None) -> bool:
    if data is None:
        return True
    if type(data) is not DataFacet or type(data.fields) is not tuple:
        return False
    for field in data.fields:
        if type(field) is not FieldDefinition or type(field.id) is not FieldId or type(field.name) is not FieldName or type(field.constraints) is not FieldConstraintSet:
            return False
        if type(field.type) is PrimitiveTypeRef:
            if type(field.type.primitive) is not PrimitiveType:
                return False
        elif type(field.type) is SemanticTypeRef:
            if type(field.type.target) is not ElementRef or type(field.type.target.element_id) is not SemanticElementId:
                return False
        else:
            return False
        constraints = field.constraints
        if type(constraints.presence) is not FieldPresence or type(constraints.nullability) is not FieldNullability or type(constraints.value_constraints) is not tuple:
            return False
        for value in constraints.value_constraints:
            if type(value) not in (MinLengthConstraint, MaxLengthConstraint, MinimumConstraint, MaximumConstraint, PatternConstraint, PrecisionConstraint, ScaleConstraint):
                return False
            if type(value) in (MinimumConstraint, MaximumConstraint) and type(value.value) is not NumericConstraintValue:
                return False
    return True


def _registry_snapshot(context: SemanticContextRef, entries: tuple[TypeDataComposition, ...]) -> TypeRegistry:
    ordered = sorted(entries, key=lambda e: (str(e.type_definition.id), e.type_definition.version))
    exact = {}
    identities = {}
    names = {}
    for entry in ordered:
        owner = entry.type_definition
        exact[ElementVersionRef(owner.id, owner.version)] = entry
        identities.setdefault(owner.id, []).append(entry)
        names.setdefault(owner.qualified_name, []).append(entry)
    registry = TypeRegistry(context)
    object.__setattr__(registry, '_exact_index', _MappingProxyType(exact))
    object.__setattr__(registry, '_identity_index', _MappingProxyType({key: tuple(value) for key, value in identities.items()}))
    object.__setattr__(registry, '_name_index', _MappingProxyType({key: tuple(value) for key, value in names.items()}))
    return registry


def _registration_rejected(registry: TypeRegistry, code: TypeRegistrationFailure, message: str, owner: _RegisteredTypeElement | None = None) -> 'TypeRegistrationResult':
    diagnostic = TypeRegistrationDiagnostic(code, message, None if owner is None else ElementVersionRef(owner.id, owner.version), None if owner is None else owner.qualified_name, None if owner is None else owner.context)
    return TypeRegistrationResult(registry, TypeRegistrationOutcome.REJECTED, (diagnostic,))


@_dataclass(frozen=True, slots=True)
class TypeRegistrationResult:
    registry: TypeRegistry
    outcome: TypeRegistrationOutcome
    diagnostics: tuple[TypeRegistrationDiagnostic, ...] = ()

    def __post_init__(self):
        if type(self.registry) is not TypeRegistry or type(self.outcome) is not TypeRegistrationOutcome:
            raise TypeError('Registration result requires a typed registry and outcome.')
        if type(self.diagnostics) not in (list, tuple) or any(type(d) is not TypeRegistrationDiagnostic for d in self.diagnostics):
            raise TypeError('Registration result requires typed ordered diagnostics.')
        diagnostics = tuple(self.diagnostics)
        if bool(diagnostics) != (self.outcome is TypeRegistrationOutcome.REJECTED):
            raise ValueError('Only rejected registration results have failure diagnostics.')
        object.__setattr__(self, 'diagnostics', diagnostics)

    @property
    def is_success(self) -> bool:
        return self.outcome is not TypeRegistrationOutcome.REJECTED


@_dataclass(frozen=True, slots=True)
class TypeRegistryLookup:
    """Read-only explicit exact-version projection implementing existing TypeLookup.

    No hidden defaults: only selected identities are visible. Binding unknown
    versions or selecting two versions for one identity is a programming error.
    """
    registry: TypeRegistry
    references: tuple[ElementVersionRef, ...]

    def __post_init__(self):
        if type(self.registry) is not TypeRegistry or type(self.references) not in (tuple, list):
            raise TypeError('A bound lookup requires a registry and explicit ordered references.')
        references = tuple(self.references)
        ids = set()
        for reference in references:
            if type(reference) is not ElementVersionRef:
                raise TypeError('Bound lookup selections must be exact ElementVersionRef values.')
            if reference.element_id in ids:
                raise ValueError('Bound lookup requires one exact version per selected identity.')
            if not self.registry.contains(reference):
                raise ValueError('Cannot bind an unregistered exact version.')
            ids.add(reference.element_id)
        object.__setattr__(self, 'references', tuple(sorted(references, key=lambda r: str(r.element_id))))

    def find(self, reference: ElementRef) -> SemanticElement | None:
        if type(reference) is not ElementRef or type(reference.element_id) is not SemanticElementId:
            raise TypeError('TypeLookup requires a canonical identity-only ElementRef.')
        selected = next((r for r in self.references if r.element_id == reference.element_id), None)
        if selected is None:
            return None
        entry = self.registry.find_by_version(selected)
        if entry is None:
            raise RuntimeError('Bound lookup snapshot lost a previously verified exact entry.')
        return entry.type_definition


# MOD-04: selected semantic membership, not registration or canonicalization.
# Closed supported payload vocabulary. Future kinds need actual owned definition
# contracts plus an explicit alias/capture extension; arbitrary Protocols fail shut.
CanonicalDefinition = TypeDataComposition
CANONICAL_DEFINITION_KINDS: tuple[SemanticElementKind, ...] = (SemanticElementKinds.TYPE_DEFINITION,)


class CanonicalConstructionFailure(_Enum):
    INVALID_SCOPE = 'MOD-CANON-001'
    INVALID_COLLECTION = 'MOD-CANON-002'
    UNSUPPORTED_DEFINITION = 'MOD-CANON-003'
    INVALID_DEFINITION = 'MOD-CANON-004'
    SCOPE_MISMATCH = 'MOD-CANON-005'
    EXACT_CONFLICT = 'MOD-CANON-006'
    QUALIFIED_NAME_COLLISION = 'MOD-CANON-007'


@_dataclass(frozen=True, slots=True)
class CanonicalConstructionDiagnostic:
    """Intrinsic construction seam pending general SK-11; no semantic judgment."""
    code: CanonicalConstructionFailure
    message: str
    reference: ElementVersionRef | None = None
    qualified_name: QualifiedName | None = None
    context: SemanticContextRef | None = None
    input_index: int | None = None
    related_reference: ElementVersionRef | None = None
    related_input_index: int | None = None

    def __post_init__(self) -> None:
        if type(self.code) is not CanonicalConstructionFailure or type(self.message) is not str or not self.message:
            raise TypeError('Canonical diagnostics require a supported intrinsic code and message.')
        for value, expected in ((self.reference, ElementVersionRef), (self.related_reference, ElementVersionRef), (self.qualified_name, QualifiedName), (self.context, SemanticContextRef)):
            if value is not None and type(value) is not expected:
                raise TypeError('Canonical diagnostic coordinates require existing typed contracts.')
        for value in (self.input_index, self.related_input_index):
            if value is not None and (type(value) is not int or value < 0):
                raise ValueError('Candidate input indices must be nonnegative integers.')

    @property
    def severity(self) -> TypeValidationSeverity:
        return TypeValidationSeverity.ERROR

    @property
    def path(self) -> TypeValidationPath | None:
        return None if self.qualified_name is None else TypeValidationPath(self.qualified_name)


class CanonicalModelConstructionError(ValueError):
    """Direct-constructor intrinsic failure; factory returns its exact diagnostics."""
    def __init__(self, diagnostics: tuple[CanonicalConstructionDiagnostic, ...]) -> None:
        if type(diagnostics) is not tuple or not diagnostics or any(type(d) is not CanonicalConstructionDiagnostic for d in diagnostics):
            raise TypeError('Construction errors require immutable nonempty intrinsic diagnostics.')
        self.diagnostics = diagnostics
        super().__init__('Canonical model construction rejected by intrinsic membership invariants.')


@_dataclass(frozen=True, slots=True)
class CanonicalModel:
    """One explicit context, selected exact versions, immutable semantic members.

    TYPE-01 is absent: current members reuse TypeDataComposition and the existing
    TYPE-07 five-value host capture, not a newly invented TypeDefinition class.
    Only that declared seam is represented; no unknown facet/host payload is
    advertised as complete semantic content. No concrete TypeRegistry is used.
    """
    scope: SemanticContextRef
    definitions: tuple[CanonicalDefinition, ...] = ()
    _exact: _Mapping[ElementVersionRef, CanonicalDefinition] = _field(init=False, repr=False, compare=False, hash=False)
    __hash__ = None  # No model content/hash or serialized snapshot identity contract.

    def __post_init__(self) -> None:
        definitions, diagnostics = _canonical_members(self.scope, self.definitions)
        if diagnostics:
            raise CanonicalModelConstructionError(diagnostics)
        exact = {ElementVersionRef(d.type_definition.id, d.type_definition.version): d for d in definitions}
        object.__setattr__(self, 'definitions', definitions)
        object.__setattr__(self, '_exact', _MappingProxyType(exact))

    def find(self, reference: ElementVersionRef) -> CanonicalDefinition | None:
        """Exact-only membership. Bare IDs/names/latest are never resolved."""
        if type(reference) is not ElementVersionRef or type(reference.element_id) is not SemanticElementId or type(reference.version) is not SemanticVersion:
            raise TypeError('Canonical lookup requires an exact existing ElementVersionRef.')
        return self._exact.get(reference)

    def contains(self, reference: ElementVersionRef) -> bool:
        return self.find(reference) is not None

    def list_definitions(self) -> tuple[CanonicalDefinition, ...]:
        return self.definitions

    @property
    def references(self) -> tuple[ElementVersionRef, ...]:
        return tuple(self._exact)

    def same_membership(self, other: 'CanonicalModel') -> bool:
        if type(other) is not CanonicalModel:
            raise TypeError('Membership comparison requires another canonical snapshot.')
        return self.scope == other.scope and self.references == other.references

    def same_supported_content(self, other: 'CanonicalModel') -> bool:
        """Only current declared host/data seam equality, never all semantic facets."""
        if type(other) is not CanonicalModel:
            raise TypeError('Supported-content comparison requires another canonical snapshot.')
        return self.scope == other.scope and self.definitions == other.definitions


@_dataclass(frozen=True, slots=True)
class CanonicalModelConstructionResult:
    model: CanonicalModel | None
    diagnostics: tuple[CanonicalConstructionDiagnostic, ...] = ()

    def __post_init__(self) -> None:
        if type(self.diagnostics) not in (list, tuple) or any(type(d) is not CanonicalConstructionDiagnostic for d in self.diagnostics):
            raise TypeError('Canonical result diagnostics require typed immutable members.')
        object.__setattr__(self, 'diagnostics', tuple(self.diagnostics))
        if (self.model is None) != bool(self.diagnostics) or self.model is not None and type(self.model) is not CanonicalModel:
            raise ValueError('Canonical result requires a complete model or nonempty failure diagnostics.')

    @property
    def is_success(self) -> bool:
        return self.model is not None


@_dataclass(frozen=True, slots=True)
class CanonicalModelFactory:
    """Intrinsic construction only: accepts already constructed domain members."""
    def create(self, scope: SemanticContextRef, definitions: tuple[CanonicalDefinition, ...] | list[CanonicalDefinition] = ()) -> CanonicalModelConstructionResult:
        try:
            return CanonicalModelConstructionResult(CanonicalModel(scope, definitions))
        except CanonicalModelConstructionError as error:
            return CanonicalModelConstructionResult(None, error.diagnostics)


def _canonical_members(scope: SemanticContextRef, definitions: tuple[CanonicalDefinition, ...]) -> tuple[tuple[CanonicalDefinition, ...], tuple[CanonicalConstructionDiagnostic, ...]]:
    """Reuse TYPE-07's capture/deep-value admission; never construct a registry."""
    if type(scope) is not SemanticContextRef or type(scope.context_id) is not SemanticElementId:
        return (), (CanonicalConstructionDiagnostic(CanonicalConstructionFailure.INVALID_SCOPE, 'One explicit canonical SemanticContextRef is required.'),)
    if type(definitions) not in (tuple, list):
        return (), (CanonicalConstructionDiagnostic(CanonicalConstructionFailure.INVALID_COLLECTION, 'Supply an explicit ordered collection of already constructed semantic members.'),)
    definitions = tuple(definitions)
    diagnostics: list[CanonicalConstructionDiagnostic] = []
    exact: dict[ElementVersionRef, CanonicalDefinition] = {}
    first: dict[ElementVersionRef, int] = {}
    names: dict[QualifiedName, tuple[ElementVersionRef, int]] = {}
    for index, definition in enumerate(definitions):
        if type(definition) is not TypeDataComposition:
            diagnostics.append(CanonicalConstructionDiagnostic(CanonicalConstructionFailure.UNSUPPORTED_DEFINITION, 'Only the current explicit TypeDataComposition definition carrier is supported; new kinds require an owned contract.', input_index=index))
            continue
        # Existing TYPE-07 helper reads each declared host property once and
        # captures it into the existing frozen host value, preserving its policy.
        owner = _registry_capture_owner(definition.type_definition)
        if owner is None:
            diagnostics.append(CanonicalConstructionDiagnostic(CanonicalConstructionFailure.INVALID_DEFINITION, 'Definition host must supply the five canonical typed semantic values.', input_index=index))
            continue
        reference = ElementVersionRef(owner.id, owner.version)
        coordinates = {'reference': reference, 'qualified_name': owner.qualified_name, 'context': owner.context, 'input_index': index}
        if owner.kind not in CANONICAL_DEFINITION_KINDS:
            diagnostics.append(CanonicalConstructionDiagnostic(CanonicalConstructionFailure.UNSUPPORTED_DEFINITION, 'Unsupported semantic definition kind in the current canonical membership vocabulary.', **coordinates))
            continue
        if owner.context != scope:
            diagnostics.append(CanonicalConstructionDiagnostic(CanonicalConstructionFailure.SCOPE_MISMATCH, 'Definition context is incompatible with the explicit canonical scope.', **coordinates))
            continue
        if not _registry_data_is_canonical(definition.data):
            diagnostics.append(CanonicalConstructionDiagnostic(CanonicalConstructionFailure.INVALID_DEFINITION, 'Only existing deeply immutable DataFacet/field/reference/constraint values may be retained.', **coordinates))
            continue
        entry = TypeDataComposition(owner, definition.data)
        previous = exact.get(reference)
        if previous is not None and previous != entry:
            diagnostics.append(CanonicalConstructionDiagnostic(CanonicalConstructionFailure.EXACT_CONFLICT, 'The selected exact identity/version has conflicting declared semantic content.', **coordinates, related_reference=reference, related_input_index=first[reference]))
        named = names.get(owner.qualified_name)
        if named is not None and named[0].element_id != owner.id:
            diagnostics.append(CanonicalConstructionDiagnostic(CanonicalConstructionFailure.QUALIFIED_NAME_COLLISION, 'Qualified name is owned by another selected identity within this context.', **coordinates, related_reference=named[0], related_input_index=named[1]))
        if previous is None:
            exact[reference], first[reference] = entry, index
        names.setdefault(owner.qualified_name, (reference, index))
    if diagnostics:
        return (), tuple(diagnostics)
    ordered = tuple(sorted(exact.values(), key=lambda d: (d.type_definition.id.value, d.type_definition.version)))
    return ordered, ()


__all__ += [
    'CanonicalDefinition', 'CANONICAL_DEFINITION_KINDS', 'CanonicalModel',
    'CanonicalModelFactory', 'CanonicalModelConstructionResult',
    'CanonicalConstructionDiagnostic', 'CanonicalConstructionFailure',
    'CanonicalModelConstructionError',
]
