"""Pure semantic identity and naming contracts, independent of infrastructure."""
from dataclasses import dataclass as _dataclass, field as _field
import re as _re

MODULE_NAME = "semantic-kernel"
__all__ = ["MODULE_NAME", "SemanticElementId", "SemanticElementIdError", "Namespace", "NamespaceError"]

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


_NAMESPACE_SEGMENT = _re.compile(r"[A-Za-z][A-Za-z0-9_-]*")


class NamespaceError(ValueError):
    """Parsing diagnostic with a zero-based segment index, without retaining input."""
    def __init__(self, code: str, message: str, segment_index: int | None = None):
        self.code = code
        self.message = message
        self.segment_index = segment_index
        super().__init__(f"{code}: {message}")


@_dataclass(frozen=True, slots=True)
class Namespace:
    """Dot-separated ASCII naming scope; only letter case is normalized.

    Segments match [a-z][a-z0-9_-]* after lowercase canonicalization.
    No empty root, implicit trimming, reserved words or inheritance semantics.
    """
    value: str
    _segments: tuple[str, ...] = _field(init=False, repr=False, compare=False, hash=False)

    def __post_init__(self):
        value = self.value
        if value is None or isinstance(value, str) and (not value or str.isspace(value)):
            raise NamespaceError("SEM-NS-001", "Namespace must not be empty.")
        if not isinstance(value, str):
            raise NamespaceError("SEM-NS-002", "Namespace requires a string representation.")
        # Built-in operations prevent str subclasses from overriding validation/normalization.
        segments = tuple(str.split(value, "."))
        for index, segment in enumerate(segments):
            if not segment:
                raise NamespaceError("SEM-NS-004", f"Empty namespace segment at index {index}.", index)
            if _NAMESPACE_SEGMENT.fullmatch(segment) is None:
                raise NamespaceError("SEM-NS-003", f"Invalid namespace segment at index {index}: expected an ASCII letter followed by ASCII letters, digits, underscores or hyphens; whitespace and other characters are forbidden.", index)
        canonical = tuple(str.lower(segment) for segment in segments)
        object.__setattr__(self, "_segments", canonical)
        object.__setattr__(self, "value", ".".join(canonical))

    @classmethod
    def parse(cls, value: str) -> "Namespace":
        """Parse a scalar naming scope; rejected input raises NamespaceError."""
        return cls(value)

    @classmethod
    def try_parse(cls, value: object) -> "Namespace | None":
        """Return None for rejected input; unexpected implementation failures propagate."""
        try:
            return cls(value)
        except NamespaceError:
            return None

    @property
    def segments(self) -> tuple[str, ...]:
        """Immutable canonical segments, cached at construction."""
        return self._segments

    def parent(self) -> "Namespace | None":
        """Remove one naming segment; a single-segment scope has no parent."""
        if len(self._segments) == 1:
            return None
        return Namespace(".".join(self._segments[:-1]))

    def child(self, segment: str) -> "Namespace":
        """Append exactly one validated segment, creating a new naming value."""
        child = Namespace.parse(segment)
        if len(child.segments) != 1:
            raise NamespaceError("SEM-NS-003", "A child requires exactly one namespace segment.", len(self._segments))
        return Namespace(self.value + "." + child.value)

    def __str__(self) -> str:
        return self.value
