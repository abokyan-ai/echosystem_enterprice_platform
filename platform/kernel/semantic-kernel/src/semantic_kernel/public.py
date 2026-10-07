"""Pure semantic identity contracts, independent of naming and infrastructure."""
from dataclasses import dataclass as _dataclass
import re as _re

MODULE_NAME = "semantic-kernel"
__all__ = ["MODULE_NAME", "SemanticElementId", "SemanticElementIdError"]

# The version/variant bits are validated, not rewritten; no UUID generation occurs here.
_SEMANTIC_ID = _re.compile(r"sem_[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-4[0-9a-fA-F]{3}-[89aAbB][0-9a-fA-F]{3}-[0-9a-fA-F]{12}")


class SemanticElementIdError(ValueError):
    """Small parsing diagnostic; the rejected input is deliberately not retained."""
    def __init__(self, code: str, message: str):
        self.code = code
        self.message = message
        super().__init__(f"{code}: {message}")


@_dataclass(frozen=True, slots=True)
class SemanticElementId:
    """Opaque, immutable sem_<UUIDv4> identity. Hex case normalizes to lowercase.

    Public construction and parse share validation. Prefix case and separators are
    strict; whitespace, alternate UUID forms and non-v4 UUIDs are not accepted.
    Generation and serializer integration belong to callers, outside this value.
    """
    value: str

    def __post_init__(self):
        value = self.value
        if value is None or isinstance(value, str) and (not value or str.isspace(value)):
            raise SemanticElementIdError("SEM-ID-001", "SemanticElementId must not be empty.")
        if not isinstance(value, str):
            raise SemanticElementIdError("SEM-ID-003", "SemanticElementId requires a string representation.")
        if len(value) != 40 or _SEMANTIC_ID.fullmatch(value) is None:
            raise SemanticElementIdError("SEM-ID-002", "Expected sem_ followed by a hyphenated UUIDv4 with the RFC variant.")
        # The built-in method avoids accepting a str subclass's overridden normalization.
        object.__setattr__(self, "value", str.lower(value))

    @classmethod
    def parse(cls, value: str) -> "SemanticElementId":
        """Parse an external scalar; invalid input raises SemanticElementIdError."""
        return cls(value)

    @classmethod
    def try_parse(cls, value: object) -> "SemanticElementId | None":
        """Return None for rejected input; unexpected implementation failures propagate."""
        try:
            return cls(value)
        except SemanticElementIdError:
            return None

    def __str__(self) -> str:
        return self.value
