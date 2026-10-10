"""Pure semantic identity, naming and reference contracts, independent of infrastructure."""
from dataclasses import dataclass as _dataclass, field as _field
import re as _re
from typing import Protocol as _Protocol

MODULE_NAME = "semantic-kernel"
__all__ = ["MODULE_NAME", "SemanticElementId", "SemanticElementIdError", "Namespace", "NamespaceError", "QualifiedName", "QualifiedNameError", "SemanticContextRef", "SemanticContextRefError", "SemanticElement", "SemanticElementKind", "SemanticElementKindError", "SemanticElementKinds", "SemanticVersion", "SemanticVersionError", "ElementVersionRef", "ElementVersionRefError"]

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


_LOCAL_NAME = _re.compile(r"[A-Za-z][A-Za-z0-9_]*")


class QualifiedNameError(ValueError):
    """Naming diagnostic; namespace failures preserve their code and segment index."""
    def __init__(self, code: str, message: str, segment_index: int | None = None, namespace_code: str | None = None):
        self.code = code
        self.message = message
        self.segment_index = segment_index
        self.namespace_code = namespace_code
        super().__init__(f"{code}: {message}")


@_dataclass(frozen=True, slots=True)
class QualifiedName:
    """Structured semantic name: canonical Namespace plus case-sensitive local name.

    Local names match ASCII [A-Za-z][A-Za-z0-9_]*. Names carry no stable
    identity, version, kind, tenant, display-name or resolution semantics.
    """
    namespace: Namespace
    local_name: str

    def __post_init__(self):
        if self.namespace is None:
            raise QualifiedNameError("SEM-QN-002", "Qualified name requires an explicit Namespace.")
        if not isinstance(self.namespace, Namespace):
            raise QualifiedNameError("SEM-QN-003", "Namespace component must be a validated Namespace value.")
        local = self.local_name
        index = len(self.namespace.segments)
        if local is None or isinstance(local, str) and not local:
            raise QualifiedNameError("SEM-QN-005", "Qualified name contains an empty local segment.", index)
        if not isinstance(local, str) or _LOCAL_NAME.fullmatch(local) is None:
            raise QualifiedNameError("SEM-QN-004", "Invalid local semantic name: expected an ASCII letter followed by ASCII letters, digits or underscores; whitespace, dots and other characters are forbidden.", index)
        # Preserve exact case while retaining a plain string with standard equality/hash.
        object.__setattr__(self, "local_name", str.__str__(local))

    @classmethod
    def create(cls, namespace: Namespace, local_name: str) -> "QualifiedName":
        """Construct from a validated namespace and one local name."""
        return cls(namespace, local_name)

    @classmethod
    def parse(cls, value: str) -> "QualifiedName":
        """Split at the last dot and delegate the namespace portion to SK-02."""
        if value is None or isinstance(value, str) and (not value or str.isspace(value)):
            raise QualifiedNameError("SEM-QN-001", "Qualified name must not be empty.")
        if not isinstance(value, str):
            raise QualifiedNameError("SEM-QN-006", "Qualified name requires a string representation.")
        namespace_text, separator, local = str.rpartition(value, ".")
        if not separator:
            raise QualifiedNameError("SEM-QN-002", "Qualified name must contain an explicit namespace.")
        try:
            namespace = Namespace.parse(namespace_text)
        except NamespaceError as error:
            code = "SEM-QN-005" if error.code == "SEM-NS-004" or not namespace_text else "SEM-QN-003"
            index = error.segment_index if error.segment_index is not None else 0
            raise QualifiedNameError(code, "Invalid namespace portion: " + error.message, index, error.code) from error
        return cls(namespace, local)

    @classmethod
    def try_parse(cls, value: object) -> "QualifiedName | None":
        """Return None for rejected input; unexpected implementation failures propagate."""
        try:
            return cls.parse(value)
        except QualifiedNameError:
            return None

    def __str__(self) -> str:
        return str(self.namespace) + "." + self.local_name


class SemanticContextRefError(ValueError):
    """Reference construction diagnostic, with the delegated identity code when parsed."""
    def __init__(self, code: str, message: str, identity_code: str | None = None):
        self.code = code
        self.message = message
        self.identity_code = identity_code
        super().__init__(f"{code}: {message}")


@_dataclass(frozen=True, slots=True)
class SemanticContextRef:
    """Typed stable identity reference to an intended semantic meaning context.

    Validation establishes identity syntax only, never target existence/kind,
    activity, accessibility or ownership. Resolution belongs outside Kernel.
    """
    context_id: SemanticElementId

    def __post_init__(self):
        if self.context_id is None:
            raise SemanticContextRefError("SEM-CTXREF-001", "Semantic context reference is required.")
        if not isinstance(self.context_id, SemanticElementId):
            raise SemanticContextRefError("SEM-CTXREF-002", "Context reference requires a validated SemanticElementId value.")

    @classmethod
    def from_id(cls, context_id: SemanticElementId) -> "SemanticContextRef":
        """Wrap an already validated identity without resolving or reparsing it."""
        return cls(context_id)

    @classmethod
    def parse(cls, value: str) -> "SemanticContextRef":
        """Reuse SemanticElementId scalar validation and canonicalization."""
        try:
            identity = SemanticElementId.parse(value)
        except SemanticElementIdError as error:
            code = {"SEM-ID-001": "SEM-CTXREF-001", "SEM-ID-003": "SEM-CTXREF-002"}.get(error.code, "SEM-CTXREF-003")
            raise SemanticContextRefError(code, "Invalid semantic identity in context reference: " + error.message, error.code) from error
        return cls(identity)

    @classmethod
    def try_parse(cls, value: object) -> "SemanticContextRef | None":
        """Return None for rejected input; unexpected implementation failures propagate."""
        try:
            return cls.parse(value)
        except SemanticContextRefError:
            return None

    def __str__(self) -> str:
        return str(self.context_id)


_KIND_SEGMENT = _re.compile(r"[a-z][a-z0-9]*(?:-[a-z0-9]+)*")


class SemanticElementKindError(ValueError):
    """Lexical classification diagnostic, not an unsupported-kind result."""
    def __init__(self, code: str, message: str, segment_index: int | None = None):
        self.code = code
        self.message = message
        self.segment_index = segment_index
        super().__init__(f"{code}: {message}")


@_dataclass(frozen=True, slots=True)
class SemanticElementKind:
    """Open, canonical lowercase kind identifier, independent of known vocabulary.

    Dot-separated kebab-case segments express identifier scope, not ownership.
    Unknown valid values are preserved without registry or compiler checks.
    """
    value: str

    def __post_init__(self):
        value = self.value
        if value is None or isinstance(value, str) and (not value or str.isspace(value)):
            raise SemanticElementKindError("SEM-KIND-001", "Semantic element kind is required.")
        if not isinstance(value, str):
            raise SemanticElementKindError("SEM-KIND-002", "Semantic element kind requires a string representation.")
        for index, segment in enumerate(str.split(value, ".")):
            if _KIND_SEGMENT.fullmatch(segment) is None:
                raise SemanticElementKindError("SEM-KIND-002", f"Invalid semantic element kind format at segment {index}: expected lowercase ASCII kebab-case starting with a letter; empty segments, whitespace and other separators are forbidden.", index)
        object.__setattr__(self, "value", str.__str__(value))

    @classmethod
    def parse(cls, value: str) -> "SemanticElementKind":
        return cls(value)

    @classmethod
    def try_parse(cls, value: object) -> "SemanticElementKind | None":
        """Return None for lexical rejection; unexpected failures propagate."""
        try:
            return cls(value)
        except SemanticElementKindError:
            return None

    def __str__(self) -> str:
        return self.value


@_dataclass(frozen=True, slots=True)
class _CoreSemanticElementKinds:
    """Immutable well-known value catalog; never a parser allowlist or registry."""
    TYPE_DEFINITION: SemanticElementKind = SemanticElementKind("type-definition")
    RELATIONSHIP_DEFINITION: SemanticElementKind = SemanticElementKind("relationship-definition")
    BEHAVIOR_DEFINITION: SemanticElementKind = SemanticElementKind("behavior-definition")
    CAPABILITY_DEFINITION: SemanticElementKind = SemanticElementKind("capability-definition")
    ACTION_DEFINITION: SemanticElementKind = SemanticElementKind("action-definition")
    EVENT_DEFINITION: SemanticElementKind = SemanticElementKind("event-definition")
    PROCESS_DEFINITION: SemanticElementKind = SemanticElementKind("process-definition")
    RULE_DEFINITION: SemanticElementKind = SemanticElementKind("rule-definition")
    POLICY_DEFINITION: SemanticElementKind = SemanticElementKind("policy-definition")
    CONTRACT_DEFINITION: SemanticElementKind = SemanticElementKind("contract-definition")
    COMPOSITION_DEFINITION: SemanticElementKind = SemanticElementKind("composition-definition")
    EXTENSION_DEFINITION: SemanticElementKind = SemanticElementKind("extension-definition")

    @property
    def ALL(self) -> tuple[SemanticElementKind, ...]:
        return (self.TYPE_DEFINITION, self.RELATIONSHIP_DEFINITION, self.BEHAVIOR_DEFINITION, self.CAPABILITY_DEFINITION, self.ACTION_DEFINITION, self.EVENT_DEFINITION, self.PROCESS_DEFINITION, self.RULE_DEFINITION, self.POLICY_DEFINITION, self.CONTRACT_DEFINITION, self.COMPOSITION_DEFINITION, self.EXTENSION_DEFINITION)

    def is_core(self, kind: SemanticElementKind) -> bool:
        """Known-vocabulary membership only; no support, ownership or validity claim."""
        return isinstance(kind, SemanticElementKind) and kind in self.ALL


SemanticElementKinds = _CoreSemanticElementKinds()


# Components use the portable non-negative signed 64-bit range.
_VERSION_COMPONENT_MAX = 9223372036854775807
_VERSION_COMPONENT = _re.compile(r"0|[1-9][0-9]*")


class SemanticVersionError(ValueError):
    """Exact-version diagnostic, optionally identifying the invalid component."""
    def __init__(self, code: str, message: str, component_index: int | None = None):
        self.code = code
        self.message = message
        self.component_index = component_index
        super().__init__(f"{code}: {message}")


@_dataclass(frozen=True, slots=True, order=True)
class SemanticVersion:
    """Exact major.minor.patch coordinate; numeric order does not imply compatibility.

    Components are plain integers in 0..9223372036854775807. No selectors,
    prerelease/build suffixes, normalization or implicit increment policy.
    """
    major: int
    minor: int
    patch: int

    def __post_init__(self):
        for index, component in enumerate((self.major, self.minor, self.patch)):
            if type(component) is not int or not 0 <= component <= _VERSION_COMPONENT_MAX:
                raise SemanticVersionError("SEM-VER-003", f"Invalid version component at index {index}: expected a plain integer in 0..9223372036854775807.", index)

    @classmethod
    def parse(cls, value: str) -> "SemanticVersion":
        """Parse exactly three canonical ASCII components; never trim or coerce."""
        if value is None or isinstance(value, str) and (not value or str.isspace(value)):
            raise SemanticVersionError("SEM-VER-001", "Semantic version is required.")
        if not isinstance(value, str):
            raise SemanticVersionError("SEM-VER-002", "Expected canonical ASCII major.minor.patch, for example 1.0.0.")
        parts = str.split(value, ".")
        if len(parts) != 3 or any(_VERSION_COMPONENT.fullmatch(part) is None for part in parts):
            raise SemanticVersionError("SEM-VER-002", "Expected canonical ASCII major.minor.patch without leading zeros, whitespace, prefixes, ranges or suffixes; for example 1.0.0.")
        for index, part in enumerate(parts):
            # Check length before int conversion, independent of Python's digit limit.
            if len(part) > 19 or int(part) > _VERSION_COMPONENT_MAX:
                raise SemanticVersionError("SEM-VER-003", f"Version component at index {index} exceeds 9223372036854775807.", index)
        return cls(*(int(part) for part in parts))

    @classmethod
    def try_parse(cls, value: object) -> "SemanticVersion | None":
        """Return None for version diagnostics only; unexpected failures propagate."""
        try:
            return cls.parse(value)
        except SemanticVersionError:
            return None

    def __str__(self) -> str:
        return f"{self.major}.{self.minor}.{self.patch}"


class ElementVersionRefError(ValueError):
    """Exact-reference diagnostic preserving a delegated primitive code/cause."""
    def __init__(self, code: str, message: str, primitive_code: str | None = None):
        self.code = code
        self.message = message
        self.primitive_code = primitive_code
        super().__init__(f"{code}: {message}")


@_dataclass(frozen=True, slots=True)
class ElementVersionRef:
    """Stable element identity plus one exact definition version, without resolution.

    No name/context/kind, existence check, registry, latest lookup or compatibility
    semantics. A coordinate is not a content-integrity proof.
    """
    element_id: SemanticElementId
    version: SemanticVersion

    def __post_init__(self):
        if self.element_id is None:
            raise ElementVersionRefError("SEM-VREF-001", "Element version reference requires an element ID.")
        if self.version is None:
            raise ElementVersionRefError("SEM-VREF-002", "Element version reference requires a semantic version.")
        if not isinstance(self.element_id, SemanticElementId) or not isinstance(self.version, SemanticVersion):
            raise ElementVersionRefError("SEM-VREF-003", "Element version reference requires validated SemanticElementId and SemanticVersion values.")

    @classmethod
    def parse(cls, value: str) -> "ElementVersionRef":
        """Parse ID@version for human interchange; JSON should use two named fields."""
        if not isinstance(value, str) or str.count(value, "@") != 1:
            raise ElementVersionRefError("SEM-VREF-003", "Expected exactly one SemanticElementId@major.minor.patch reference.")
        identity_text, version_text = str.split(value, "@")
        try:
            identity = SemanticElementId.parse(identity_text)
        except SemanticElementIdError as error:
            code = "SEM-VREF-001" if error.code == "SEM-ID-001" else "SEM-VREF-003"
            raise ElementVersionRefError(code, "Invalid element identity: " + error.message, error.code) from error
        try:
            version = SemanticVersion.parse(version_text)
        except SemanticVersionError as error:
            code = "SEM-VREF-002" if error.code == "SEM-VER-001" else "SEM-VREF-003"
            raise ElementVersionRefError(code, "Invalid exact semantic version: " + error.message, error.code) from error
        return cls(identity, version)

    @classmethod
    def try_parse(cls, value: object) -> "ElementVersionRef | None":
        """Return None for reference diagnostics only; unexpected failures propagate."""
        try:
            return cls.parse(value)
        except ElementVersionRefError:
            return None

    def __str__(self) -> str:
        return str(self.element_id) + "@" + str(self.version)


class SemanticElement(_Protocol):
    """Minimal read-only contract for a first-class semantic definition snapshot.

    Implementations own local construction invariants and snapshot equality.
    Context is explicit and required; no name-derived ownership or resolution
    is implied. This contract is not a business instance or runtime execution.
    """
    @property
    def id(self) -> SemanticElementId:
        """Stable semantic identity, independent of name/context evolution."""
        ...

    @property
    def qualified_name(self) -> QualifiedName:
        """Canonical semantic name of this definition snapshot."""
        ...

    @property
    def context(self) -> SemanticContextRef:
        """Explicit reference to the intended meaning context; not resolved here."""
        ...

    @property
    def kind(self) -> SemanticElementKind:
        """Explicit open semantic category, independent of implementation class."""
        ...

    @property
    def version(self) -> SemanticVersion:
        """Explicit exact definition version; not a package/artifact version."""
        ...
