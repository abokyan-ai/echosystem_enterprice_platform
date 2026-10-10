"""Pure model contracts for owned semantic structural members."""
from dataclasses import dataclass as _dataclass
import re as _re

MODULE_NAME = "model-core"
__all__ = ["MODULE_NAME", "FieldId", "FieldIdError", "FieldName", "FieldNameError", "FieldDefinition", "FieldDefinitionError"]

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
