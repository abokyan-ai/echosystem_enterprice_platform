"""Pure model contracts for owned semantic structural members."""
from dataclasses import dataclass as _dataclass
import re as _re
from semantic_kernel.public import FacetKind, FacetKinds, FacetApplicability, SemanticElementKind, SemanticElementKinds, SemanticElement, SemanticElementId, QualifiedName, SemanticContextRef, SemanticVersion

MODULE_NAME = "model-core"
__all__ = ["MODULE_NAME", "FieldId", "FieldIdError", "FieldName", "FieldNameError", "FieldDefinition", "FieldDefinitionError", "DataFacet", "DataFacetError", "DATA_FACET_APPLICABILITY", "TypeDataComposition"]

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


@_dataclass(frozen=True, slots=True)
class FieldDefinition:
    """Owned structural member snapshot, not a first-class SemanticElement.

    TYPE-02 supplies only identity and local name. Compare .id for identity;
    snapshot equality/hash includes both fields. The full shape evolves through
    TYPE-04/05; there are no type/constraint placeholders or owner back pointers.
    """
    id: FieldId
    name: FieldName

    def __post_init__(self):
        if self.id is None:
            raise FieldDefinitionError("TYPE-FIELD-001", "Field ID is required.")
        if not isinstance(self.id, FieldId):
            raise FieldDefinitionError("TYPE-FIELD-002", "Field definition requires a validated FieldId value.")
        if self.name is None:
            raise FieldDefinitionError("TYPE-FIELD-003", "Field name is required.")
        if not isinstance(self.name, FieldName):
            raise FieldDefinitionError("TYPE-FIELD-004", "Field definition requires a validated FieldName value.")

    @classmethod
    def create(cls, id: FieldId, name: FieldName) -> "FieldDefinition":
        """Construct from typed values without reparsing, generation or lookup."""
        return cls(id, name)


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
