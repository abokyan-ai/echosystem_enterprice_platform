"""Pure model contracts for owned semantic structural members."""
from dataclasses import dataclass as _dataclass
import re as _re
from enum import Enum as _Enum
from decimal import Decimal as _Decimal
from typing import Protocol as _Protocol
from semantic_kernel.public import FacetKind, FacetKinds, FacetApplicability, SemanticElementKind, SemanticElementKinds, SemanticElement, SemanticElementId, QualifiedName, SemanticContextRef, SemanticVersion

MODULE_NAME = "model-core"
__all__ = ["MODULE_NAME", "FieldId", "FieldIdError", "FieldName", "FieldNameError", "FieldDefinition", "FieldDefinitionError", "DataFacet", "DataFacetError", "DATA_FACET_APPLICABILITY", "TypeDataComposition", "FieldConstraintError", "FieldPresence", "FieldNullability", "ConstraintKind", "ConstraintKinds", "ValueConstraint", "NumericConstraintValue", "MinLengthConstraint", "MaxLengthConstraint", "MinimumConstraint", "MaximumConstraint", "PatternConstraint", "PrecisionConstraint", "ScaleConstraint", "FieldConstraintSet"]

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


@_dataclass(frozen=True, slots=True)
class FieldDefinition:
    """Owned structural member snapshot, not a first-class SemanticElement.

    Compare .id for identity; snapshot equality/hash includes explicit constraints.
    TYPE-05 will add type references; no type inference or owner back pointers.
    """
    id: FieldId
    name: FieldName
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

        if type(self.constraints) is not FieldConstraintSet:
            raise FieldDefinitionError("TYPE-FIELD-005", "Field definition requires an explicit FieldConstraintSet.")

    @classmethod
    def create(cls, id: FieldId, name: FieldName, constraints: FieldConstraintSet) -> "FieldDefinition":
        """Construct from typed values without reparsing, generation or lookup."""
        return cls(id, name, constraints)


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
