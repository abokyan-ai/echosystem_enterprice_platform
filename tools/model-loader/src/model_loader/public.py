"""MOD-02 loading contracts. No semantic resolution, registration or execution."""
from dataclasses import dataclass, field
from enum import Enum
from typing import Callable, Mapping, Protocol
from types import MappingProxyType
import re
from bisect import bisect_right
from hashlib import sha256
from model_authoring.public import (
    AuthoringModelDocument, AuthoringSchemaPath, AuthoringSchemaDiagnostic,
    AuthoringSchemaValidator,
    CanonicalizationResult, CanonicalizationDiagnostic, CanonicalSourceAssociation,
    NamespaceResolutionResult, NamespaceResolutionDiagnostic,
    SemanticReferenceDiagnostic, ModelValidationReport, ModelValidationResult,
    ModelDiagnosticOrigin, ModelDiagnosticTarget, ModelDiagnosticContext,
    ModelDiagnosticEntry, ModelDiagnosticPayload, associate_model_diagnostic,
    ModelValidationStatus, CompilationReadiness, ModelValidationStageResult,
    CompilationDiagnosticReport, CompilerPhaseDiagnosticView,
    CompilationDiagnosticOrigin, CompilationArtifactDiagnosticView,
    AuthoringSchemaValidationResult, NamespaceEnvironmentResult,
    NamespaceSymbolSnapshotResult, SemanticReferenceResolutionResult,
    SemanticReferenceBatchResult, ResolvedAuthoringInputResult,
    CanonicalModelConstructionResult, TypeValidationResult,
)

MODULE_NAME = 'model-loader'
__all__ = [
    'SourceSpan', 'SourceLocation', 'SourceNodePath', 'SourceNodeKind',
    'SourceLocationEntry', 'SourceLocationIndex', 'SourceLocationTracker',
    'MODULE_NAME', 'ModelSourceId', 'ModelSourceFormat', 'InMemoryModelSource',
    'FileModelSource', 'ModelSource', 'ModelSourceInformation', 'ModelLoadOptions',
    'ModelSourceProvider', 'InMemorySourceProvider', 'LocalFileSourceProvider',
    'SourceContentResult', 'SourcePosition', 'ModelLoadStage', 'ModelLoadDiagnostic',
    'SourceDecodeResult', 'ModelDecoder', 'JsonModelDecoder', 'YamlModelDecoder',
    'LoadedAuthoringDocument', 'ModelLoadResult', 'ModelLoadBatchStatus',
    'ModelLoadBatchResult', 'ModelLoader',
]


@dataclass(frozen=True, slots=True)
class ModelSourceId:
    """Caller-owned, case-sensitive operation identity; never a semantic ID."""
    value: str

    def __post_init__(self):
        if type(self.value) is not str or not self.value or len(self.value) > 256 or self.value != self.value.strip() or any(ord(c) < 32 or ord(c) == 127 or 0xD800 <= ord(c) <= 0xDFFF for c in self.value):
            raise ValueError('Source identity requires 1..256 characters without outer whitespace or controls.')


class ModelSourceFormat(str, Enum):
    JSON = 'json'
    YAML = 'yaml'


class ModelLoadStage(str, Enum):
    ACQUISITION = 'acquisition'
    DECODING = 'decoding'
    SCHEMA = 'schema'
    BATCH = 'batch'


@dataclass(frozen=True, slots=True)
class ModelSourceInformation:
    source_id: ModelSourceId
    format: str
    location: str | None = None

    def __post_init__(self):
        if type(self.source_id) is not ModelSourceId or type(self.format) not in (str, ModelSourceFormat) or not self.format:
            raise TypeError('Source metadata requires a dedicated identity and explicit format.')
        if self.location is not None and (type(self.location) is not str or not self.location):
            raise TypeError('A supplied location must be nonempty text.')


@dataclass(frozen=True, slots=True)
class InMemoryModelSource:
    source_id: ModelSourceId
    format: str
    content: str

    def __post_init__(self):
        ModelSourceInformation(self.source_id, self.format)
        if type(self.content) is not str:
            raise TypeError('In-memory content requires Unicode text, not a parsed tree.')

    @property
    def information(self) -> ModelSourceInformation:
        return ModelSourceInformation(self.source_id, self.format)


@dataclass(frozen=True, slots=True)
class FileModelSource:
    source_id: ModelSourceId
    format: str
    path: str

    def __post_init__(self):
        ModelSourceInformation(self.source_id, self.format, self.path)
        if '\x00' in self.path:
            raise ValueError('File paths must not contain NUL.')

    @property
    def information(self) -> ModelSourceInformation:
        return ModelSourceInformation(self.source_id, self.format, self.path)


ModelSource = InMemoryModelSource | FileModelSource


@dataclass(frozen=True, slots=True)
class ModelLoadOptions:
    max_source_bytes: int = 1_048_576
    max_depth: int = 64
    max_nodes: int = 100_000

    def __post_init__(self):
        if any(type(v) is not int or v < 1 for v in (self.max_source_bytes, self.max_depth, self.max_nodes)):
            raise ValueError('Resource limits must be positive integers.')
        if self.max_depth > 128:
            raise ValueError('Depth cannot exceed the implementation recursion safety ceiling of 128.')


@dataclass(frozen=True, slots=True)
class SourcePosition:
    """One-based native-parser line/column; optional zero-based Unicode character offset."""
    line: int
    column: int
    offset: int | None = None

    def __post_init__(self):
        if any(type(v) is not int or v < 1 for v in (self.line, self.column)):
            raise ValueError('Positions require positive one-based coordinates.')
        if self.offset is not None and (type(self.offset) is not int or self.offset < 0):
            raise ValueError('Offsets require nonnegative Python Unicode character indexes.')
        if self.offset is not None and self.offset < self.line + self.column - 2:
            raise ValueError('Offset cannot precede the minimum coordinate character count.')


@dataclass(frozen=True, slots=True)
class SourceSpan:
    """Half-open [start,end); optional offsets count Python Unicode characters."""
    start: SourcePosition
    end: SourcePosition

    def __post_init__(self) -> None:
        if type(self.start) is not SourcePosition or type(self.end) is not SourcePosition:
            raise TypeError('Span endpoints require canonical SourcePosition values.')
        a, b = (self.start.line, self.start.column), (self.end.line, self.end.column)
        if a > b:
            raise ValueError('Source span coordinates are reversed.')
        if self.start.offset is not None and self.end.offset is not None:
            if self.start.offset > self.end.offset or (a == b) != (self.start.offset == self.end.offset):
                raise ValueError('Span offsets and line/column ordering must agree.')
            if self.start.line == self.end.line and self.end.offset - self.start.offset != self.end.column - self.start.column:
                raise ValueError('Same-line offset and column distances must agree.')


@dataclass(frozen=True, slots=True)
class SourceLocation:
    source_id: ModelSourceId
    span: SourceSpan

    def __post_init__(self) -> None:
        if type(self.source_id) is not ModelSourceId or type(self.span) is not SourceSpan:
            raise TypeError('Locations require the existing source identity and immutable span.')


@dataclass(frozen=True, slots=True)
class SourceNodePath:
    """RFC 6901-style pointer tokens: empty tuple is root; / is empty property."""
    tokens: tuple[str, ...] = ()

    def __post_init__(self) -> None:
        if type(self.tokens) not in (list, tuple) or any(type(t) is not str or any(0xD800 <= ord(c) <= 0xDFFF for c in t) for t in self.tokens):
            raise TypeError('Node paths require an ordered sequence of Unicode string tokens.')
        object.__setattr__(self, 'tokens', tuple(self.tokens))

    @classmethod
    def parse(cls, pointer: str) -> 'SourceNodePath':
        if type(pointer) is not str or pointer and not pointer.startswith('/'):
            raise ValueError('Node pointer must be empty root or start with /.')
        if not pointer:
            return cls()
        tokens = []
        for token in pointer[1:].split('/'):
            i = 0
            while i < len(token):
                if token[i] == '~':
                    if i + 1 == len(token) or token[i + 1] not in '01':
                        raise ValueError('Pointer escapes are only ~0 and ~1.')
                    i += 1
                i += 1
            tokens.append(token.replace('~1', '/').replace('~0', '~'))
        return cls(tuple(tokens))

    @classmethod
    def from_authoring_path(cls, path: AuthoringSchemaPath) -> 'SourceNodePath':
        if type(path) is not AuthoringSchemaPath:
            raise TypeError('Path conversion requires the existing MOD-01 coordinate.')
        return cls(tuple(str(t) for t in path.segments))

    @property
    def pointer(self) -> str:
        return ''.join('/' + t.replace('~', '~0').replace('/', '~1') for t in self.tokens)

    @property
    def parent(self) -> 'SourceNodePath | None':
        return SourceNodePath(self.tokens[:-1]) if self.tokens else None


class SourceNodeKind(str, Enum):
    OBJECT = 'object'
    ARRAY = 'array'
    SCALAR = 'scalar'


@dataclass(frozen=True, slots=True)
class SourceLocationEntry:
    path: SourceNodePath
    location: SourceLocation
    kind: SourceNodeKind
    key_location: SourceLocation | None = None

    def __post_init__(self) -> None:
        if type(self.path) is not SourceNodePath or type(self.location) is not SourceLocation or type(self.kind) is not SourceNodeKind:
            raise TypeError('Index entries require typed node paths, locations and kinds.')
        if self.key_location is not None and (type(self.key_location) is not SourceLocation or self.key_location.source_id != self.location.source_id or not self.path.tokens):
            raise ValueError('Property key location requires a non-root node in the same source.')


@dataclass(frozen=True, slots=True)
class SourceLocationIndex:
    source_id: ModelSourceId
    entries: tuple[SourceLocationEntry, ...] = ()
    source_digest: str | None = None
    _by_path: Mapping[SourceNodePath, SourceLocationEntry] = field(init=False, repr=False, compare=False, hash=False)

    def __post_init__(self) -> None:
        if type(self.source_id) is not ModelSourceId or type(self.entries) not in (list, tuple):
            raise TypeError('Indexes require a source identity and ordered entry sequence.')
        if self.source_digest is not None and (type(self.source_digest) is not str or len(self.source_digest) != 64 or any(c not in '0123456789abcdef' for c in self.source_digest)):
            raise ValueError('Source digest must be lowercase SHA-256 hex or absent.')
        owned = {}
        for entry in self.entries:
            if type(entry) is not SourceLocationEntry or entry.location.source_id != self.source_id:
                raise ValueError('Every indexed entry must belong to this source snapshot.')
            if entry.path in owned and owned[entry.path] != entry:
                raise ValueError('Conflicting registration for a source node path.')
            owned[entry.path] = entry
        for entry in owned.values():
            parent = owned.get(entry.path.parent)
            if entry.key_location is not None and parent is not None and parent.kind is not SourceNodeKind.OBJECT:
                raise ValueError('A property key cannot be attached to an array/scalar child.')
        entries = tuple(sorted(owned.values(), key=lambda e: e.path.pointer))
        object.__setattr__(self, 'entries', entries)
        object.__setattr__(self, '_by_path', MappingProxyType(owned))

    def entry(self, path: SourceNodePath) -> SourceLocationEntry | None:
        if type(path) is not SourceNodePath:
            raise TypeError('Location lookup requires a SourceNodePath.')
        return self._by_path.get(path)

    def find(self, path: SourceNodePath) -> SourceLocation | None:
        entry = self.entry(path)
        return None if entry is None else entry.location

    def find_key(self, path: SourceNodePath) -> SourceLocation | None:
        entry = self.entry(path)
        return None if entry is None else entry.key_location

    def contains(self, path: SourceNodePath) -> bool:
        return self.entry(path) is not None

    def list_locations(self) -> tuple[SourceLocationEntry, ...]:
        return self.entries


@dataclass(frozen=True, slots=True)
class SourceLocationTracker:
    """Consumes reliable parser metadata; performs no parsing or semantic judgment."""
    def build(self, source_id: ModelSourceId, entries: tuple[SourceLocationEntry, ...], *, source_text: str | None = None) -> SourceLocationIndex:
        if source_text is not None and type(source_text) is not str:
            raise TypeError('Snapshot digest requires original Unicode source text.')
        digest = None if source_text is None else sha256(source_text.encode('utf-8')).hexdigest()
        return SourceLocationIndex(source_id, entries, digest)

    def locate(self, index: SourceLocationIndex | None, path: SourceNodePath, *, containing: bool = False, key: bool = False) -> SourceLocation | None:
        if type(path) is not SourceNodePath or index is not None and type(index) is not SourceLocationIndex:
            raise TypeError('Tracking requires an optional index and typed path.')
        if index is None:
            return None
        result = index.find_key(path) if key else index.find(path)
        if result is not None or not containing:
            return result
        parent = path.parent
        while parent is not None:
            entry = index.entry(parent)
            if entry is not None and entry.kind in (SourceNodeKind.OBJECT, SourceNodeKind.ARRAY):
                return entry.location
            parent = parent.parent
        return None


@dataclass(frozen=True, slots=True)
class ModelLoadDiagnostic:
    """Narrow loading diagnostic seam pending the absent general SK-11 contract."""
    source: ModelSourceInformation
    stage: ModelLoadStage
    code: str
    message: str
    position: SourcePosition | None = None
    schema_diagnostic: AuthoringSchemaDiagnostic | None = None
    related_input_index: int | None = None
    source_location: SourceLocation | None = None
    related_locations: tuple[SourceLocation, ...] = ()

    def __post_init__(self):
        if type(self.source) is not ModelSourceInformation or type(self.stage) is not ModelLoadStage or self.code not in {f'MOD-LOAD-{i:03}' for i in range(1, 15)} or type(self.message) is not str or not self.message:
            raise ValueError('Invalid loading diagnostic contract.')
        if self.position is not None and type(self.position) is not SourcePosition:
            raise TypeError('Position must be a loading coordinate.')
        if (self.stage is ModelLoadStage.SCHEMA) != (self.schema_diagnostic is not None):
            raise ValueError('Only schema diagnostics retain the original MOD-01 diagnostic.')
        if self.schema_diagnostic is not None and type(self.schema_diagnostic) is not AuthoringSchemaDiagnostic:
            raise TypeError('Schema failures require the original structural diagnostic.')
        if self.related_input_index is not None and (type(self.related_input_index) is not int or self.related_input_index < 0):
            raise ValueError('Related batch index must be nonnegative.')
        if self.source_location is not None:
            if type(self.source_location) is not SourceLocation or self.source_location.source_id != self.source.source_id:
                raise ValueError('Diagnostic location must belong to its explicit source.')
            start = self.source_location.span.start
            if self.position is None:
                object.__setattr__(self, 'position', start)
            elif (self.position.line, self.position.column) != (start.line, start.column) or self.position.offset is not None and start.offset is not None and self.position.offset != start.offset:
                raise ValueError('Legacy diagnostic position and physical span start must agree.')
        if type(self.related_locations) not in (list, tuple) or any(type(loc) is not SourceLocation for loc in self.related_locations):
            raise TypeError('Related locations require immutable source locations.')
        object.__setattr__(self, 'related_locations', tuple(self.related_locations))


    @property
    def severity(self) -> str:
        return 'error'


def _diagnostics(values):
    if type(values) not in (tuple, list) or any(type(d) is not ModelLoadDiagnostic for d in values):
        raise TypeError('Diagnostics require an ordered sequence of immutable loading diagnostics.')
    return tuple(values)


@dataclass(frozen=True, slots=True)
class SourceContentResult:
    source: ModelSourceInformation
    content: str | None
    diagnostics: tuple[ModelLoadDiagnostic, ...] = ()

    def __post_init__(self):
        object.__setattr__(self, 'diagnostics', _diagnostics(self.diagnostics))
        if type(self.source) is not ModelSourceInformation or (self.content is not None and type(self.content) is not str) or (self.content is None) != bool(self.diagnostics) or any(d.source != self.source for d in self.diagnostics):
            raise ValueError('Acquisition results require either source text or associated diagnostics.')


class ModelSourceProvider(Protocol):
    def acquire(self, source: ModelSource, options: ModelLoadOptions) -> SourceContentResult: ...


@dataclass(frozen=True, slots=True)
class InMemorySourceProvider:
    def acquire(self, source: InMemoryModelSource, options: ModelLoadOptions) -> SourceContentResult:
        if type(source) is not InMemoryModelSource:
            raise TypeError('In-memory provider accepts only in-memory sources.')
        return check_text(source.information, source.content, options)


@dataclass(frozen=True, slots=True)
class LocalFileSourceProvider:
    """Read-only bounded UTF-8 regular-file adapter; no discovery or rewriting."""
    def acquire(self, source: FileModelSource, options: ModelLoadOptions) -> SourceContentResult:
        if type(source) is not FileModelSource:
            raise TypeError('File provider accepts only explicit file sources.')
        return read_file(source, options)


@dataclass(frozen=True, slots=True)
class SourceDecodeResult:
    """Untrusted candidate tree belongs to decoding, never to the loaded snapshot."""
    source: ModelSourceInformation
    value: object | None
    diagnostics: tuple[ModelLoadDiagnostic, ...] = ()
    positions: tuple[tuple[AuthoringSchemaPath, SourcePosition], ...] = ()
    locations: SourceLocationIndex | None = None

    def __post_init__(self):
        object.__setattr__(self, 'diagnostics', _diagnostics(self.diagnostics))
        object.__setattr__(self, 'positions', tuple(self.positions))
        if type(self.source) is not ModelSourceInformation or (self.value is None) != bool(self.diagnostics) or any(d.source != self.source for d in self.diagnostics):
            raise ValueError('Decoding results require either a candidate or associated diagnostics.')
        if any(type(p) is not tuple or len(p) != 2 or type(p[0]) is not AuthoringSchemaPath or type(p[1]) is not SourcePosition for p in self.positions):
            raise TypeError('Decoder positions require immutable path/coordinate pairs.')
        if self.locations is not None and (type(self.locations) is not SourceLocationIndex or self.locations.source_id != self.source.source_id):
            raise ValueError('Decoder index must belong to its source snapshot.')
        if self.locations is not None:
            for path, position in self.positions:
                location = self.locations.find(SourceNodePath.from_authoring_path(path))
                if location is not None and ((position.line, position.column) != (location.span.start.line, location.span.start.column) or position.offset is not None and location.span.start.offset is not None and position.offset != location.span.start.offset):
                    raise ValueError('Legacy decoder positions and indexed span starts must agree.')


class ModelDecoder(Protocol):
    def decode(self, content: SourceContentResult, options: ModelLoadOptions) -> SourceDecodeResult: ...


@dataclass(frozen=True, slots=True)
class JsonModelDecoder:
    def decode(self, content: SourceContentResult, options: ModelLoadOptions) -> SourceDecodeResult:
        return decode_json(content, options)


@dataclass(frozen=True, slots=True)
class YamlModelDecoder:
    def decode(self, content: SourceContentResult, options: ModelLoadOptions) -> SourceDecodeResult:
        return decode_yaml(content, options)


@dataclass(frozen=True, slots=True)
class LoadedAuthoringDocument:
    source: ModelSourceInformation
    document: AuthoringModelDocument
    locations: SourceLocationIndex | None = None

    def __post_init__(self):
        if type(self.source) is not ModelSourceInformation or type(self.document) is not AuthoringModelDocument:
            raise TypeError('Loaded snapshots require explicit source metadata and MOD-01 authoring contracts.')
        if self.locations is not None and (type(self.locations) is not SourceLocationIndex or self.locations.source_id != self.source.source_id):
            raise ValueError('Loaded locations must belong to the same authoring source snapshot.')


@dataclass(frozen=True, slots=True)
class ModelLoadResult:
    source: ModelSourceInformation
    loaded: LoadedAuthoringDocument | None
    diagnostics: tuple[ModelLoadDiagnostic, ...] = ()

    def __post_init__(self):
        object.__setattr__(self, 'diagnostics', _diagnostics(self.diagnostics))
        if type(self.source) is not ModelSourceInformation or (self.loaded is None) != bool(self.diagnostics) or any(d.source != self.source for d in self.diagnostics):
            raise ValueError('Load results require a successful snapshot or associated errors.')
        if self.loaded is not None and (type(self.loaded) is not LoadedAuthoringDocument or self.loaded.source != self.source):
            raise ValueError('Loaded document must retain the exact source association.')

    @property
    def is_success(self) -> bool:
        return self.loaded is not None


class ModelLoadBatchStatus(str, Enum):
    EMPTY = 'empty'
    ALL_LOADED = 'all-loaded'
    PARTIAL = 'partial'
    ALL_FAILED = 'all-failed'


@dataclass(frozen=True, slots=True)
class ModelLoadBatchResult:
    entries: tuple[ModelLoadResult, ...]

    def __post_init__(self):
        if type(self.entries) not in (list, tuple) or any(type(e) is not ModelLoadResult for e in self.entries):
            raise TypeError('Batches require ordered loading results.')
        object.__setattr__(self, 'entries', tuple(self.entries))

    @property
    def status(self) -> ModelLoadBatchStatus:
        if not self.entries:
            return ModelLoadBatchStatus.EMPTY
        count = sum(e.is_success for e in self.entries)
        return ModelLoadBatchStatus.ALL_LOADED if count == len(self.entries) else ModelLoadBatchStatus.ALL_FAILED if count == 0 else ModelLoadBatchStatus.PARTIAL

    @property
    def successful_documents(self) -> tuple[LoadedAuthoringDocument, ...]:
        return tuple(e.loaded for e in self.entries if e.loaded is not None)

    @property
    def failed_sources(self) -> tuple[ModelSourceInformation, ...]:
        return tuple(e.source for e in self.entries if not e.is_success)

    @property
    def diagnostics(self) -> tuple[ModelLoadDiagnostic, ...]:
        return tuple(d for e in self.entries for d in e.diagnostics)


@dataclass(frozen=True, slots=True)
class ModelLoader:
    options: ModelLoadOptions = ModelLoadOptions()
    memory_provider: ModelSourceProvider = InMemorySourceProvider()
    file_provider: ModelSourceProvider = LocalFileSourceProvider()
    json_decoder: ModelDecoder = JsonModelDecoder()
    yaml_decoder: ModelDecoder = YamlModelDecoder()

    def __post_init__(self):
        if type(self.options) is not ModelLoadOptions:
            raise TypeError('Loading requires explicit resource options.')
        if any(not callable(getattr(p, 'acquire', None)) for p in (self.memory_provider, self.file_provider)) or any(not callable(getattr(d, 'decode', None)) for d in (self.json_decoder, self.yaml_decoder)):
            raise TypeError('Providers and decoders require their explicit operations.')

    def load(self, source: ModelSource) -> ModelLoadResult:
        if type(source) not in (InMemoryModelSource, FileModelSource):
            raise TypeError('Loading accepts only explicit v0 source contracts.')
        info = source.information
        if info.format not in (ModelSourceFormat.JSON, ModelSourceFormat.YAML):
            return ModelLoadResult(info, None, (ModelLoadDiagnostic(info, ModelLoadStage.DECODING, 'MOD-LOAD-003', 'Unsupported explicit source format.'),))
        provider = self.memory_provider if type(source) is InMemoryModelSource else self.file_provider
        acquired = provider.acquire(source, self.options)
        if type(acquired) is not SourceContentResult or acquired.source != info:
            raise TypeError('Source provider violated its result/association contract.')
        if acquired.diagnostics:
            return ModelLoadResult(info, None, acquired.diagnostics)
        # An injected provider must not bypass the shared source resource boundary.
        bounded = check_text(info, acquired.content, self.options)
        if bounded.diagnostics:
            return ModelLoadResult(info, None, bounded.diagnostics)
        decoder = self.json_decoder if info.format == ModelSourceFormat.JSON else self.yaml_decoder
        decoded = decoder.decode(bounded, self.options)
        if type(decoded) is not SourceDecodeResult or decoded.source != info:
            raise TypeError('Decoder violated its result/association contract.')
        if decoded.locations is not None and decoded.locations.source_digest is not None and decoded.locations.source_digest != sha256(bounded.content.encode('utf-8')).hexdigest():
            raise TypeError('Decoder index belongs to a different source-content snapshot.')
        if decoded.diagnostics:
            return ModelLoadResult(info, None, decoded.diagnostics)
        tree_error = inspect_tree(decoded.value, self.options)
        if tree_error is not None:
            return ModelLoadResult(info, None, (ModelLoadDiagnostic(info, ModelLoadStage.DECODING, tree_error[0], tree_error[1]),))
        validated = AuthoringSchemaValidator().validate(decoded.value)
        if not validated.is_valid:
            positions = dict(decoded.positions)
            diagnostics = tuple(_schema_diagnostic(info, d, decoded.locations, positions) for d in validated.diagnostics)
            return ModelLoadResult(info, None, diagnostics)
        return ModelLoadResult(info, LoadedAuthoringDocument(info, validated.document, decoded.locations))

    def load_many(self, sources: tuple[ModelSource, ...]) -> ModelLoadBatchResult:
        if type(sources) not in (list, tuple) or any(type(s) not in (InMemoryModelSource, FileModelSource) for s in sources):
            raise TypeError('Batch loading requires an explicit ordered source sequence.')
        sources = tuple(sources)
        first = {}
        counts = {}
        for i, source in enumerate(sources):
            first.setdefault(source.source_id, i)
            counts[source.source_id] = counts.get(source.source_id, 0) + 1
        entries = []
        for source in sources:
            if counts[source.source_id] > 1:
                info = source.information
                entries.append(ModelLoadResult(info, None, (ModelLoadDiagnostic(info, ModelLoadStage.BATCH, 'MOD-LOAD-011', 'All submissions sharing this source identity are rejected before acquisition.', related_input_index=first[source.source_id]),)))
            else:
                entries.append(self.load(source))
        return ModelLoadBatchResult(tuple(entries))


"""Bounded read-only acquisition; no filesystem operation in the memory provider."""
import os
import stat


def failure(info, code, message):
    return SourceContentResult(info, None, (ModelLoadDiagnostic(info, ModelLoadStage.ACQUISITION, code, message),))


def check_text(info, content, options):
    try:
        if len(content) > options.max_source_bytes or len(content.encode('utf-8')) > options.max_source_bytes:
            return failure(info, 'MOD-LOAD-012', 'Source exceeds the explicit UTF-8 byte limit.')
    except UnicodeError:
        return failure(info, 'MOD-LOAD-013', 'Source contains invalid Unicode scalar values.')
    if content.startswith("\ufeff"):
        return failure(info, 'MOD-LOAD-013', 'A source must not begin with a Unicode byte-order mark.')
    if not content.strip():
        return failure(info, 'MOD-LOAD-004', 'Source content is empty or whitespace only.')
    return SourceContentResult(info, content)


def read_file(source, options):
    info = source.information
    descriptor = None
    try:
        # NONBLOCK prevents a supplied FIFO from blocking before regular-file checks.
        descriptor = os.open(source.path, os.O_RDONLY | getattr(os, 'O_NONBLOCK', 0))
        metadata = os.fstat(descriptor)
        if not stat.S_ISREG(metadata.st_mode):
            return failure(info, 'MOD-LOAD-002', 'Source must be a readable regular file.')
        if metadata.st_size > options.max_source_bytes:
            return failure(info, 'MOD-LOAD-012', 'File exceeds the explicit byte limit.')
        with os.fdopen(descriptor, 'rb') as stream:
            descriptor = None
            content = stream.read(options.max_source_bytes + 1)
        if len(content) > options.max_source_bytes:
            return failure(info, 'MOD-LOAD-012', 'File exceeds the explicit byte limit.')
        return check_text(info, content.decode('utf-8'), options)
    except FileNotFoundError:
        return failure(info, 'MOD-LOAD-001', 'Explicit source file does not exist.')
    except UnicodeError:
        return failure(info, 'MOD-LOAD-013', 'File content must be valid UTF-8 without a byte-order mark.')
    except OSError:
        return failure(info, 'MOD-LOAD-002', 'Explicit source file could not be read.')
    finally:
        if descriptor is not None:
            os.close(descriptor)


"""Established JSON/PyYAML parsers plus strict resource and tree boundaries."""
import json
import math
from contextlib import closing



class DecodeFailure(ValueError):
    def __init__(self, code: str, message: str, position: SourcePosition | None = None, location: SourceLocation | None = None, related: tuple[SourceLocation, ...] = ()) -> None:
        super().__init__(message)
        self.code, self.message, self.position = code, message, position
        self.location, self.related = location, related


def failed(content: SourceContentResult, code: str, message: str, position: SourcePosition | None = None, *, location: SourceLocation | None = None, related: tuple[SourceLocation, ...] = ()) -> SourceDecodeResult:
    diagnostic = ModelLoadDiagnostic(content.source, ModelLoadStage.DECODING, code, message, position, source_location=location, related_locations=related)
    return SourceDecodeResult(content.source, None, (diagnostic,))


def _schema_diagnostic(info: ModelSourceInformation, diagnostic: AuthoringSchemaDiagnostic, index: SourceLocationIndex | None, legacy: Mapping[AuthoringSchemaPath, SourcePosition]) -> ModelLoadDiagnostic:
    tracker = SourceLocationTracker()
    path = SourceNodePath.from_authoring_path(diagnostic.path)
    location = tracker.locate(index, path, containing=diagnostic.code == 'MOD-SCHEMA-002', key=diagnostic.code == 'MOD-SCHEMA-003')
    related = ()
    if diagnostic.related_path is not None:
        original = tracker.locate(index, SourceNodePath.from_authoring_path(diagnostic.related_path))
        if original is not None:
            related = (original,)
    return ModelLoadDiagnostic(info, ModelLoadStage.SCHEMA, 'MOD-LOAD-010', diagnostic.message, None if location is not None else legacy.get(diagnostic.path), diagnostic, source_location=location, related_locations=related)


@dataclass(frozen=True, slots=True)
class _JsonNode:
    start: int
    end: int
    children: tuple['_JsonNode', ...] = ()
    keys: tuple[tuple[str, int, int], ...] = ()


@dataclass(slots=True)
class _JsonFrame:
    children: list[_JsonNode] = field(default_factory=list)
    keys: tuple[tuple[str, int, int], ...] = ()


class _JsonLocationAdapter:
    """Instrument stdlib parsing callbacks, not a second JSON grammar/parser.

    Value boundaries come from scanner returns; key boundaries come from stdlib
    scanstring at already parsed member coordinates. No matching-string search.
    """
    def __init__(self, source_id: ModelSourceId, text: str, options: ModelLoadOptions) -> None:
        self.source_id, self.text, self.options = source_id, text, options
        self.node_count = 0
        self.line_starts = (0, *(i + 1 for i, c in enumerate(text) if c == '\n'))
        self.frames: list[_JsonFrame] = []
        self.root: _JsonNode | None = None
        self.decoder = json.JSONDecoder(parse_constant=reject_constant)
        self.decoder.parse_object = self._object
        self.decoder.parse_array = self._array
        scanner = json.scanner.py_make_scanner(self.decoder)
        self.decoder.scan_once = lambda text, start: self._scan(scanner, text, start)

    def position(self, offset: int) -> SourcePosition:
        line = bisect_right(self.line_starts, offset)
        return SourcePosition(line, offset - self.line_starts[line - 1] + 1, offset)

    def location(self, start: int, end: int) -> SourceLocation:
        return SourceLocation(self.source_id, SourceSpan(self.position(start), self.position(end)))

    def _scan(self, scanner: Callable[[str, int], tuple[object, int]], text: str, start: int) -> tuple[object, int]:
        self.node_count += 1
        if self.node_count > self.options.max_nodes:
            raise DecodeFailure('MOD-LOAD-014', 'JSON parser node limit exceeded.', location=self.location(start, start))
        frame = _JsonFrame()
        self.frames.append(frame)
        try:
            value, end = scanner(text, start)
        finally:
            self.frames.pop()
        node = _JsonNode(start, end, tuple(frame.children), frame.keys)
        if self.frames:
            self.frames[-1].children.append(node)
        else:
            self.root = node
        return value, end

    def _object(self, source: tuple[str, int], strict: bool, scanner: Callable[[str, int], tuple[object, int]], object_hook: object, object_pairs_hook: object, memo: dict[str, str] | None = None) -> tuple[object, int]:
        text, start = source
        frame = self.frames[-1]

        def pairs(values: list[tuple[str, object]]) -> dict[str, object]:
            cursor = start
            keys = []
            result = {}
            first = {}
            for i, (key, value) in enumerate(values):
                if i:
                    cursor = json.decoder.WHITESPACE.match(text, frame.children[i - 1].end).end() + 1
                cursor = json.decoder.WHITESPACE.match(text, cursor).end()
                _, end = json.decoder.scanstring(text, cursor + 1, strict)
                key_location = self.location(cursor, end)
                self.node_count += 1
                if self.node_count > self.options.max_nodes:
                    raise DecodeFailure('MOD-LOAD-014', 'JSON parser key/node limit exceeded.', location=key_location)
                if any(0xD800 <= ord(c) <= 0xDFFF for c in key):
                    raise DecodeFailure('MOD-LOAD-008', 'JSON property key contains invalid Unicode scalar values.', location=key_location)
                if key in result:
                    raise DecodeFailure('MOD-LOAD-006', 'Duplicate JSON object key is unsupported.', location=key_location, related=(first[key],))
                keys.append((key, cursor, end))
                result[key], first[key] = value, key_location
            frame.keys = tuple(keys)
            return result

        return json.decoder.JSONObject(source, strict, lambda text, offset: self._scan(scanner, text, offset), object_hook, pairs, memo)

    def _array(self, source: tuple[str, int], scanner: Callable[[str, int], tuple[object, int]]) -> tuple[object, int]:
        return json.decoder.JSONArray(source, lambda text, offset: self._scan(scanner, text, offset))

    def decode(self) -> tuple[object, SourceLocationIndex, tuple[tuple[AuthoringSchemaPath, SourcePosition], ...]]:
        value = self.decoder.decode(self.text)
        entries: list[SourceLocationEntry] = []
        positions: list[tuple[AuthoringSchemaPath, SourcePosition]] = []

        def visit(item: object, node: _JsonNode, path: tuple[str | int, ...], key_location: SourceLocation | None = None) -> None:
            location = self.location(node.start, node.end)
            if type(item) is str and any(0xD800 <= ord(c) <= 0xDFFF for c in item):
                raise DecodeFailure('MOD-LOAD-013', 'JSON string contains invalid Unicode scalar values.', location=location)
            if type(item) is float and not math.isfinite(item):
                raise DecodeFailure('MOD-LOAD-008', 'Non-finite JSON numbers are unsupported.', location=location)
            kind = SourceNodeKind.OBJECT if type(item) is dict else SourceNodeKind.ARRAY if type(item) is list else SourceNodeKind.SCALAR
            entries.append(SourceLocationEntry(SourceNodePath(tuple(str(t) for t in path)), location, kind, key_location))
            positions.append((AuthoringSchemaPath(path), location.span.start))
            if type(item) is dict:
                for (key, start, end), child in zip(node.keys, node.children):
                    visit(item[key], child, (*path, key), self.location(start, end))
            elif type(item) is list:
                for i, child in enumerate(node.children):
                    visit(item[i], child, (*path, i))

        if self.root is None:
            raise RuntimeError('JSON parser returned no source root metadata.')
        visit(value, self.root, ())
        return value, SourceLocationTracker().build(self.source_id, tuple(entries), source_text=self.text), tuple(positions)


def inspect_tree(value, options):
    """Iterative check also protects against cyclic/incompatible injected candidates."""
    if type(value) is not dict:
        return 'MOD-LOAD-009', 'Decoded document root must be an object.'
    stack = [(value, 1)]
    seen = set()
    count = 0
    while stack:
        item, depth = stack.pop()
        count += 1
        if count > options.max_nodes or depth > options.max_depth:
            return 'MOD-LOAD-014', 'Decoded document exceeds depth or node limits.'
        if type(item) in (dict, list):
            if id(item) in seen:
                return 'MOD-LOAD-008', 'Cyclic or shared parsed containers are unsupported.'
            seen.add(id(item))
            if len(item) > options.max_nodes - count:
                return 'MOD-LOAD-014', 'Decoded collection exceeds the node budget.'
            if type(item) is dict:
                if any(type(key) is not str or any(0xD800 <= ord(c) <= 0xDFFF for c in key) for key in item):
                    return 'MOD-LOAD-008', 'Object keys must be valid Unicode strings.'
                count += len(item)  # Keys consume complexity budget too.
                stack.extend((child, depth + 1) for child in item.values())
            else:
                stack.extend((child, depth + 1) for child in item)
        elif type(item) not in (str, int, float, bool, type(None)):
            return 'MOD-LOAD-008', 'Decoded values must be plain JSON-compatible objects.'
        elif type(item) is float and not math.isfinite(item):
            return 'MOD-LOAD-008', 'Non-finite numbers are unsupported.'
        elif type(item) is str and any(0xD800 <= ord(c) <= 0xDFFF for c in item):
            return 'MOD-LOAD-013', 'Decoded strings contain invalid Unicode scalar values.'
        if count > options.max_nodes:
            return 'MOD-LOAD-014', 'Decoded document exceeds the node limit.'
    return None


def json_depth(text, options):
    depth = 0
    quoted = escaped = False
    for c in text:
        if quoted:
            if escaped:
                escaped = False
            elif c == '\\':
                escaped = True
            elif c == '"':
                quoted = False
        elif c == '"':
            quoted = True
        elif c in '[{':
            depth += 1
            if depth > options.max_depth:
                raise DecodeFailure('MOD-LOAD-014', 'JSON container nesting exceeds the depth limit.')
        elif c in ']}':
            depth -= 1


def unique_pairs(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise DecodeFailure('MOD-LOAD-006', 'Duplicate JSON object key is unsupported.')
        result[key] = value
    return result


def reject_constant(value):
    raise DecodeFailure('MOD-LOAD-008', 'Non-standard JSON numeric constants are unsupported.')


def decode_json(content: SourceContentResult, options: ModelLoadOptions) -> SourceDecodeResult:
    if content.diagnostics:
        return SourceDecodeResult(content.source, None, content.diagnostics)
    adapter = _JsonLocationAdapter(content.source.source_id, content.content, options)
    try:
        json_depth(content.content, options)
        value, index, positions = adapter.decode()
        error = inspect_tree(value, options)
        if error:
            return failed(content, *error, location=index.find(SourceNodePath()))
        return SourceDecodeResult(content.source, value, positions=positions, locations=index)
    except json.JSONDecodeError as exc:
        location = adapter.location(exc.pos, exc.pos)
        return failed(content, 'MOD-LOAD-005', 'Malformed strict JSON: ' + exc.msg, location=location)
    except DecodeFailure as exc:
        return failed(content, exc.code, exc.message, exc.position, location=exc.location, related=exc.related)
    except (ValueError, RecursionError, OverflowError):
        return failed(content, 'MOD-LOAD-014', 'JSON numeric or parser resource limits were exceeded.')


def decode_yaml(content: SourceContentResult, options: ModelLoadOptions) -> SourceDecodeResult:
    if content.diagnostics:
        return SourceDecodeResult(content.source, None, content.diagnostics)
    # Lazy parser import: neutral contracts/JSON/memory acquisition work without YAML.
    try:
        import yaml
    except ImportError:
        return failed(content, 'MOD-LOAD-003', 'YAML decoder dependency is unavailable; install requirements-model-loader.txt.')
    loader = None
    try:
        depth = nodes = documents = 0
        with closing(yaml.parse(content.content, Loader=yaml.SafeLoader)) as events:
            for event in events:
                position = SourcePosition(event.start_mark.line + 1, event.start_mark.column + 1, event.start_mark.index)
                event_end = SourcePosition(event.end_mark.line + 1, event.end_mark.column + 1, event.end_mark.index)
                event_location = SourceLocation(content.source.source_id, SourceSpan(position, event_end))
                if isinstance(event, yaml.events.DocumentStartEvent):
                    documents += 1
                    if documents > 1:
                        raise DecodeFailure('MOD-LOAD-007', 'Only one YAML document is allowed per source.', location=event_location)
                    if event.version not in (None, (1, 1)) or event.tags:
                        raise DecodeFailure('MOD-LOAD-008', 'Only YAML 1.1 without tag directives is supported.', location=event_location)
                if isinstance(event, yaml.events.AliasEvent) or getattr(event, 'anchor', None) is not None or getattr(event, 'tag', None) is not None:
                    raise DecodeFailure('MOD-LOAD-008', 'YAML aliases, anchors and explicit tags are unsupported.', location=event_location)
                if isinstance(event, (yaml.events.MappingStartEvent, yaml.events.SequenceStartEvent, yaml.events.ScalarEvent)):
                    nodes += 1
                    if nodes > options.max_nodes:
                        raise DecodeFailure('MOD-LOAD-014', 'YAML node limit exceeded.', location=event_location)
                    if isinstance(event, (yaml.events.MappingStartEvent, yaml.events.SequenceStartEvent)):
                        depth += 1
                    if depth > options.max_depth:
                        raise DecodeFailure('MOD-LOAD-014', 'YAML nesting limit exceeded.', location=event_location)
                elif isinstance(event, (yaml.events.MappingEndEvent, yaml.events.SequenceEndEvent)):
                    depth -= 1
        loader = yaml.SafeLoader(content.content)
        root = loader.get_single_node()
        positions: list[tuple[AuthoringSchemaPath, SourcePosition]] = []
        entries: list[SourceLocationEntry] = []

        def mark_position(mark) -> SourcePosition:
            return SourcePosition(mark.line + 1, mark.column + 1, mark.index)

        def node_location(node) -> SourceLocation:
            return SourceLocation(content.source.source_id, SourceSpan(mark_position(node.start_mark), mark_position(node.end_mark)))

        def project(node, path: tuple[str | int, ...], key_location: SourceLocation | None = None) -> object:
            location = node_location(node)
            position = location.span.start
            positions.append((AuthoringSchemaPath(path), position))
            kind = SourceNodeKind.OBJECT if isinstance(node, yaml.nodes.MappingNode) else SourceNodeKind.ARRAY if isinstance(node, yaml.nodes.SequenceNode) else SourceNodeKind.SCALAR
            entries.append(SourceLocationEntry(SourceNodePath(tuple(str(t) for t in path)), location, kind, key_location))
            if isinstance(node, yaml.nodes.MappingNode):
                if node.tag != 'tag:yaml.org,2002:map':
                    raise DecodeFailure('MOD-LOAD-008', 'Unsupported YAML mapping tag.', location=location)
                value = {}
                first_locations = {}
                for key, child in node.value:
                    if not isinstance(key, yaml.nodes.ScalarNode) or key.tag != 'tag:yaml.org,2002:str':
                        raise DecodeFailure('MOD-LOAD-008', 'YAML mapping keys must resolve to strings; merge keys are unsupported.', location=node_location(key))
                    if any(0xD800 <= ord(c) <= 0xDFFF for c in key.value):
                        raise DecodeFailure('MOD-LOAD-008', 'YAML property key contains invalid Unicode scalar values.', location=node_location(key))
                    if key.value in value:
                        raise DecodeFailure('MOD-LOAD-006', 'Duplicate YAML mapping key is unsupported.', location=node_location(key), related=(first_locations[key.value],))
                    first_locations[key.value] = node_location(key)
                    value[key.value] = project(child, path + (key.value,), first_locations[key.value])
                return value
            if isinstance(node, yaml.nodes.SequenceNode) and node.tag == 'tag:yaml.org,2002:seq':
                return [project(child, path + (i,)) for i, child in enumerate(node.value)]
            if isinstance(node, yaml.nodes.ScalarNode) and node.tag in {f'tag:yaml.org,2002:{tag}' for tag in ('str', 'int', 'float', 'bool', 'null')}:
                scalar = loader.construct_object(node)
                if type(scalar) is float and not math.isfinite(scalar):
                    raise DecodeFailure('MOD-LOAD-008', 'Non-finite YAML numbers are unsupported.', location=location)
                if type(scalar) is str and any(0xD800 <= ord(c) <= 0xDFFF for c in scalar):
                    raise DecodeFailure('MOD-LOAD-013', 'YAML string contains invalid Unicode scalar values.', location=location)
                return scalar
            raise DecodeFailure('MOD-LOAD-008', 'Unsupported YAML scalar or collection type; quote dates/timestamps.', location=location)

        value = None if root is None else project(root, ())
        index = SourceLocationTracker().build(content.source.source_id, tuple(entries), source_text=content.content)
        error = inspect_tree(value, options)
        if error:
            return failed(content, *error, location=index.find(SourceNodePath()))
        return SourceDecodeResult(content.source, value, positions=tuple(positions), locations=index)
    except DecodeFailure as exc:
        return failed(content, exc.code, exc.message, exc.position, location=exc.location, related=exc.related)
    except yaml.YAMLError as exc:
        mark = getattr(exc, 'problem_mark', None)
        position = None if mark is None else SourcePosition(mark.line + 1, mark.column + 1, mark.index)
        location = None if position is None else SourceLocation(content.source.source_id, SourceSpan(position, position))
        return failed(content, 'MOD-LOAD-005', 'Malformed YAML source.', location=location)
    except (ValueError, RecursionError, OverflowError):
        return failed(content, 'MOD-LOAD-014', 'YAML numeric or parser resource limits were exceeded.')
    finally:
        if loader is not None:
            loader.dispose()


# MOD-05 location presentation: no loading/parsing/canonicalization is performed.
@dataclass(frozen=True, slots=True)
class LocatedCanonicalSourceAssociation:
    association: CanonicalSourceAssociation
    location: SourceLocation | None

    def __post_init__(self) -> None:
        if type(self.association) is not CanonicalSourceAssociation or self.location is not None and type(self.location) is not SourceLocation:
            raise TypeError('Located canonical associations require existing typed values.')


@dataclass(frozen=True, slots=True)
class LocatedCanonicalizationDiagnostic:
    diagnostic: CanonicalizationDiagnostic
    location: SourceLocation | None
    related_location: SourceLocation | None = None

    def __post_init__(self) -> None:
        if type(self.diagnostic) is not CanonicalizationDiagnostic or any(value is not None and type(value) is not SourceLocation for value in (self.location, self.related_location)):
            raise TypeError('Located transformation diagnostics require existing typed values.')


@dataclass(frozen=True, slots=True)
class CanonicalizationSourceLocations:
    """External presentation only; identity/content equality remains in MOD-04."""
    associations: tuple[LocatedCanonicalSourceAssociation, ...]
    diagnostics: tuple[LocatedCanonicalizationDiagnostic, ...]

    def __post_init__(self) -> None:
        for name, expected in (('associations', LocatedCanonicalSourceAssociation), ('diagnostics', LocatedCanonicalizationDiagnostic)):
            values = getattr(self, name)
            if type(values) not in (tuple, list) or any(type(value) is not expected for value in values):
                raise TypeError('Location sidecars require immutable typed member sequences.')
            object.__setattr__(self, name, tuple(values))


def locate_canonicalization(result: CanonicalizationResult, loaded: LoadedAuthoringDocument) -> CanonicalizationSourceLocations:
    """Attach existing MOD-03 coordinates to the caller-paired MOD-05 result.

    Caller must pair the exact loaded authoring snapshot that was canonicalized;
    source tracking proves index/source alignment, not semantic transformation
    provenance. No fallback to nearby nodes, inference or canonicalizer re-run.
    Absent index/node => None; all semantic targets/diagnostics are preserved.
    """
    if type(result) is not CanonicalizationResult or type(loaded) is not LoadedAuthoringDocument:
        raise TypeError('Location attachment requires typed transformation and loading results.')
    index = loaded.locations
    def location(path: AuthoringSchemaPath | None) -> SourceLocation | None:
        return None if index is None or path is None else index.find(SourceNodePath.from_authoring_path(path))
    return CanonicalizationSourceLocations(
        tuple(LocatedCanonicalSourceAssociation(a, location(a.path)) for a in result.source_associations),
        tuple(LocatedCanonicalizationDiagnostic(d, location(d.path), location(d.related_path)) for d in result.diagnostics),
    )


__all__ += ['LocatedCanonicalSourceAssociation', 'LocatedCanonicalizationDiagnostic', 'CanonicalizationSourceLocations', 'locate_canonicalization']


# MOD-06 location presentation remains outside pure namespace resolution.
@dataclass(frozen=True, slots=True)
class LocatedNamespaceResolutionDiagnostic:
    diagnostic: NamespaceResolutionDiagnostic
    location: SourceLocation | None
    related_locations: tuple[SourceLocation | None, ...] = ()

    def __post_init__(self) -> None:
        if type(self.diagnostic) is not NamespaceResolutionDiagnostic or self.location is not None and type(self.location) is not SourceLocation:
            raise TypeError('Located namespace diagnostics require typed domain/location values.')
        if type(self.related_locations) not in (tuple, list) or any(v is not None and type(v) is not SourceLocation for v in self.related_locations):
            raise TypeError('Related locations require a typed immutable sequence, allowing missing nodes.')
        values = tuple(self.related_locations)
        if len(values) != len(self.diagnostic.related_paths):
            raise ValueError('Related location positions must preserve every supplied diagnostic path.')
        object.__setattr__(self, 'related_locations', values)


@dataclass(frozen=True, slots=True)
class NamespaceResolutionSourceLocations:
    result: NamespaceResolutionResult
    expression_location: SourceLocation | None
    diagnostics: tuple[LocatedNamespaceResolutionDiagnostic, ...]

    def __post_init__(self) -> None:
        if type(self.result) is not NamespaceResolutionResult or self.expression_location is not None and type(self.expression_location) is not SourceLocation:
            raise TypeError('Namespace location sidecars require existing typed results and locations.')
        if type(self.diagnostics) not in (tuple, list) or any(type(d) is not LocatedNamespaceResolutionDiagnostic for d in self.diagnostics):
            raise TypeError('Located namespace diagnostics require an immutable typed sequence.')
        diagnostics = tuple(self.diagnostics)
        if tuple(d.diagnostic for d in diagnostics) != self.result.diagnostics:
            raise ValueError('Location presentation must retain original namespace diagnostics.')
        object.__setattr__(self, 'diagnostics', diagnostics)


def locate_namespace_diagnostics(diagnostics: tuple[NamespaceResolutionDiagnostic, ...], loaded: LoadedAuthoringDocument) -> tuple[LocatedNamespaceResolutionDiagnostic, ...]:
    """Present resolution/environment/capture/bridge diagnostics uniformly."""
    if type(diagnostics) not in (tuple, list) or any(type(d) is not NamespaceResolutionDiagnostic for d in diagnostics) or type(loaded) is not LoadedAuthoringDocument:
        raise TypeError('Location presentation requires typed namespace diagnostics and a loaded snapshot.')
    def location(path: AuthoringSchemaPath | None) -> SourceLocation | None:
        return None if loaded.locations is None or path is None else loaded.locations.find(SourceNodePath.from_authoring_path(path))
    return tuple(LocatedNamespaceResolutionDiagnostic(d, location(d.path), tuple(location(p) for p in d.related_paths)) for d in diagnostics)


def locate_namespace_resolution(result: NamespaceResolutionResult, loaded: LoadedAuthoringDocument) -> NamespaceResolutionSourceLocations:
    """Attach actual MOD-03 locations by exact path without loading/resolution.

    Caller pairs the original loaded document with request and declaration paths.
    External registry symbols normally have no document path. Cross-document
    provenance is not inferred. Missing path/index/node remains None.
    """
    if type(result) is not NamespaceResolutionResult or type(loaded) is not LoadedAuthoringDocument:
        raise TypeError('Location presentation requires typed resolution and loading results.')
    def location(path: AuthoringSchemaPath | None) -> SourceLocation | None:
        return None if loaded.locations is None or path is None else loaded.locations.find(SourceNodePath.from_authoring_path(path))
    diagnostics = locate_namespace_diagnostics(result.diagnostics, loaded)
    return NamespaceResolutionSourceLocations(result, location(result.path), diagnostics)


__all__ += ['LocatedNamespaceResolutionDiagnostic', 'NamespaceResolutionSourceLocations', 'locate_namespace_resolution', 'locate_namespace_diagnostics']


# MOD-07 physical presentation: semantic references never contain coordinates.
@dataclass(frozen=True, slots=True)
class LocatedSemanticReferenceDiagnostic:
    diagnostic: SemanticReferenceDiagnostic
    location: SourceLocation | None
    related_locations: tuple[SourceLocation | None, ...] = ()

    def __post_init__(self) -> None:
        if type(self.diagnostic) is not SemanticReferenceDiagnostic or self.location is not None and type(self.location) is not SourceLocation:
            raise TypeError('Located reference failures require actual typed domain/location values.')
        if type(self.related_locations) not in (tuple, list) or any(v is not None and type(v) is not SourceLocation for v in self.related_locations):
            raise TypeError('Related reference locations require typed optional immutable members.')
        values = tuple(self.related_locations)
        if len(values) != len(self.diagnostic.related_paths):
            raise ValueError('Reference related locations must preserve each delegated source path.')
        object.__setattr__(self, 'related_locations', values)


def locate_semantic_reference_diagnostics(diagnostics: tuple[SemanticReferenceDiagnostic, ...], loaded: LoadedAuthoringDocument) -> tuple[LocatedSemanticReferenceDiagnostic, ...]:
    """Attach actual MOD-03 primary/related spans to single/batch/readiness errors.

    Pair the exact original loaded document; this is source traceability, not
    provenance proof. No parsing/loading/resolution or nearest-node inference.
    """
    if type(diagnostics) not in (tuple, list) or any(type(d) is not SemanticReferenceDiagnostic for d in diagnostics) or type(loaded) is not LoadedAuthoringDocument:
        raise TypeError('Reference location attachment requires typed failures and a loaded snapshot.')
    def location(path: AuthoringSchemaPath | None) -> SourceLocation | None:
        return None if loaded.locations is None or path is None else loaded.locations.find(SourceNodePath.from_authoring_path(path))
    return tuple(LocatedSemanticReferenceDiagnostic(d, location(d.path), tuple(location(p) for p in d.related_paths)) for d in diagnostics)


__all__ += ['LocatedSemanticReferenceDiagnostic', 'locate_semantic_reference_diagnostics']


# MOD-08 physical enrichment stays outside pure semantic validation.
@dataclass(frozen=True, slots=True)
class LocatedModelValidationReport:
    report: ModelValidationReport
    location: SourceLocation | None

    def __post_init__(self) -> None:
        if type(self.report) is not ModelValidationReport or self.location is not None and type(self.location) is not SourceLocation:
            raise TypeError('Located validation reports require original typed reports and optional actual locations.')


def locate_model_validation(result: ModelValidationResult, loaded: LoadedAuthoringDocument) -> tuple[LocatedModelValidationReport, ...]:
    """Attach exact MOD-03 nodes from explicit MOD-05 associations.

    Existing associations only identify definition/field nodes: constraint-level
    diagnostics retain their typed TYPE-06 path but use that actual broader node.
    No guessed constraint indexes, synthetic spans or nearest-node inference.
    Caller must pair the original loaded authoring source, not a different file.
    """
    if type(result) is not ModelValidationResult or type(loaded) is not LoadedAuthoringDocument:
        raise TypeError('Validation enrichment requires original typed validation/loading snapshots.')
    index = loaded.locations
    return tuple(LocatedModelValidationReport(report, None if index is None or report.source_path is None else index.find(SourceNodePath.from_authoring_path(report.source_path))) for report in result.diagnostics)


__all__ += ['LocatedModelValidationReport', 'locate_model_validation']


# MOD-09: source/report presentation at the existing tooling boundary.
class ModelDiagnosticProcessingStatus(str, Enum):
    UNAVAILABLE = 'unavailable'
    SUCCEEDED = 'succeeded'
    FAILED = 'failed'
    INCOMPLETE = 'incomplete'
    PARTIAL = 'partial'


class ModelDiagnosticPhase(str, Enum):
    LOADING = 'loading'
    AUTHORING_SCHEMA = 'authoring-schema'
    NAMESPACE_RESOLUTION = 'namespace-resolution'
    REFERENCE_RESOLUTION = 'reference-resolution'
    CANONICAL_CONSTRUCTION = 'canonical-construction'
    CANONICALIZATION = 'canonicalization'
    TYPE_VALIDATION = 'type-validation'
    MODEL_VALIDATION = 'model-validation'
    COMPILATION = 'compilation'


@dataclass(frozen=True, slots=True)
class ModelDiagnosticSourceTarget:
    source_id: ModelSourceId
    path: SourceNodePath | None = None

    def __post_init__(self) -> None:
        if type(self.source_id) is not ModelSourceId or self.path is not None and type(self.path) is not SourceNodePath:
            raise TypeError('Source-only target requires existing source identity and optional node path.')


@dataclass(frozen=True, slots=True)
class ModelDiagnosticSourceContext:
    semantic: ModelDiagnosticContext = field(default_factory=ModelDiagnosticContext)
    indexes: tuple[SourceLocationIndex, ...] = ()
    default_source_id: ModelSourceId | None = None
    _indexes: Mapping[ModelSourceId, SourceLocationIndex] = field(init=False, repr=False, compare=False, hash=False)

    def __post_init__(self) -> None:
        if type(self.semantic) is not ModelDiagnosticContext or type(self.indexes) not in (tuple, list) or any(type(i) is not SourceLocationIndex for i in self.indexes):
            raise TypeError('Diagnostic source context requires actual immutable semantic context/indexes.')
        if self.default_source_id is not None and type(self.default_source_id) is not ModelSourceId:
            raise TypeError('Default source must be explicitly identified, never inferred from filenames.')
        indexes = tuple(self.indexes)
        if len({i.source_id for i in indexes}) != len(indexes):
            raise ValueError('Several snapshots for one source are ambiguous; supply one explicitly selected index.')
        object.__setattr__(self, 'indexes', indexes)
        object.__setattr__(self, '_indexes', MappingProxyType({i.source_id: i for i in indexes}))

    def location(self, target: ModelDiagnosticSourceTarget | None) -> SourceLocation | None:
        if target is None or target.path is None:
            return None
        index = self._indexes.get(target.source_id)
        return None if index is None else index.find(target.path)


@dataclass(frozen=True, slots=True)
class LocatedModelDiagnosticEntry:
    entry: ModelDiagnosticEntry | ModelLoadDiagnostic
    source_target: ModelDiagnosticSourceTarget | None = None
    location: SourceLocation | None = None
    related_source_targets: tuple[ModelDiagnosticSourceTarget | None, ...] = ()
    related_locations: tuple[SourceLocation | None, ...] = ()

    def __post_init__(self) -> None:
        if type(self.entry) not in (ModelDiagnosticEntry, ModelLoadDiagnostic):
            raise TypeError('Located entry retains the actual typed domain envelope or loading diagnostic.')
        if self.source_target is not None and type(self.source_target) is not ModelDiagnosticSourceTarget:
            raise TypeError('Source target must be typed or absent.')
        if self.location is not None and type(self.location) is not SourceLocation:
            raise TypeError('Primary location must be an actual source location.')
        for name, expected in (('related_source_targets', ModelDiagnosticSourceTarget), ('related_locations', SourceLocation)):
            values = getattr(self, name)
            if type(values) not in (tuple, list) or any(v is not None and type(v) is not expected for v in values):
                raise TypeError('Related source information is an immutable typed sequence with explicit absence.')
            object.__setattr__(self, name, tuple(values))
        if len(self.related_source_targets) != len(self.related_locations):
            raise ValueError('Related source/location slots must retain positional correspondence.')
        pairs = ((self.source_target, self.location), *zip(self.related_source_targets, self.related_locations))
        if any(t is not None and loc is not None and t.source_id != loc.source_id for t, loc in pairs):
            raise ValueError('Source association and physical location must agree on source identity.')
        if type(self.entry) is ModelLoadDiagnostic:
            if self.source_target is None or self.source_target.source_id != self.entry.source.source_id:
                raise ValueError('Loading entry must preserve its original source identity.')
            if self.entry.source_location is not None and self.location != self.entry.source_location:
                raise ValueError('Existing reliable loading location must be preserved.')
            if self.related_locations[:len(self.entry.related_locations)] != self.entry.related_locations:
                raise ValueError('Original related loading locations must remain intact and ordered.')

    @property
    def diagnostic(self) -> ModelDiagnosticPayload | ModelLoadDiagnostic:
        return self.entry.diagnostic if type(self.entry) is ModelDiagnosticEntry else self.entry

    @property
    def origin(self) -> ModelDiagnosticOrigin:
        return self.entry.origin if type(self.entry) is ModelDiagnosticEntry else ModelDiagnosticOrigin.MODEL_LOADER

    @property
    def severity(self) -> str:
        severity = self.diagnostic.severity
        return severity.value if isinstance(severity, Enum) else severity

    @property
    def target(self) -> ModelDiagnosticTarget | None:
        return self.entry.target if type(self.entry) is ModelDiagnosticEntry else None

    @property
    def stage_id(self) -> str | None:
        return self.entry.stage_id if type(self.entry) is ModelDiagnosticEntry else None


def enrich_model_diagnostic(entry: ModelDiagnosticEntry | ModelLoadDiagnostic | LocatedModelDiagnosticEntry, context: ModelDiagnosticSourceContext) -> LocatedModelDiagnosticEntry:
    if type(context) is not ModelDiagnosticSourceContext or type(entry) not in (ModelDiagnosticEntry, ModelLoadDiagnostic, LocatedModelDiagnosticEntry):
        raise TypeError('Enrichment requires an actual immutable diagnostic entry and source context.')
    if type(entry) is LocatedModelDiagnosticEntry:
        return entry  # explicit existing location evidence takes precedence over optional enrichment
    if type(entry) is ModelLoadDiagnostic:
        source_id = entry.source.source_id
        path = None if entry.schema_diagnostic is None else SourceNodePath.from_authoring_path(entry.schema_diagnostic.path)
        source = ModelDiagnosticSourceTarget(source_id, path)
        location = entry.source_location if entry.source_location is not None else context.location(source)
        if entry.position is not None and location is not None:
            start = location.span.start
            if (start.line, start.column) != (entry.position.line, entry.position.column) or start.offset is not None and entry.position.offset is not None and start.offset != entry.position.offset:
                location = entry.source_location  # incompatible optional index cannot replace original evidence
        related_sources = [ModelDiagnosticSourceTarget(loc.source_id) for loc in entry.related_locations]
        related_locations = list(entry.related_locations)
        if not related_locations and entry.schema_diagnostic is not None and entry.schema_diagnostic.related_path is not None:
            related = ModelDiagnosticSourceTarget(source_id, SourceNodePath.from_authoring_path(entry.schema_diagnostic.related_path))
            related_sources.append(related)
            related_locations.append(context.location(related))
        return LocatedModelDiagnosticEntry(entry, source, location, related_sources, related_locations)
    source_id = context.default_source_id
    source = None if source_id is None else ModelDiagnosticSourceTarget(source_id, None if entry.source_path is None else SourceNodePath.from_authoring_path(entry.source_path))
    related_sources = tuple(None if source_id is None else ModelDiagnosticSourceTarget(source_id, SourceNodePath.from_authoring_path(path)) for path in entry.related_paths)
    return LocatedModelDiagnosticEntry(entry, source, context.location(source), related_sources, tuple(context.location(t) for t in related_sources))


@dataclass(frozen=True, slots=True)
class ModelDiagnosticOperation:
    phase: ModelDiagnosticPhase
    status: ModelDiagnosticProcessingStatus
    entries: tuple[LocatedModelDiagnosticEntry, ...] = ()
    validation_result: ModelValidationResult | None = None
    compilation_report: CompilationDiagnosticReport | None = None

    def __post_init__(self) -> None:
        if type(self.phase) is not ModelDiagnosticPhase or type(self.status) is not ModelDiagnosticProcessingStatus:
            raise TypeError('Operation outcome uses explicit processing phase/status, not diagnostic counts.')
        if type(self.entries) not in (tuple, list) or any(type(e) is not LocatedModelDiagnosticEntry for e in self.entries):
            raise TypeError('Operation entries must be immutable typed snapshots.')
        object.__setattr__(self, 'entries', tuple(self.entries))
        if (self.phase is ModelDiagnosticPhase.MODEL_VALIDATION) != (self.validation_result is not None):
            raise ValueError('Only actual MOD-08 outcomes supply validation status/readiness.')
        if (self.phase is ModelDiagnosticPhase.COMPILATION) != (self.compilation_report is not None):
            raise ValueError('Only actual compiler outcomes supply compilation status/phase results.')
        if self.compilation_report is not None:
            if type(self.compilation_report) is not CompilationDiagnosticReport or tuple(e.entry for e in self.entries) != self.compilation_report.entries or self.status.value != self.compilation_report.status:
                raise ValueError('Compiler operation must preserve its original outcome/diagnostic entry sequence.')
        if self.validation_result is not None:
            if type(self.validation_result) is not ModelValidationResult:
                raise TypeError('Validation outcome must be the original actual MOD-08 result.')
            original = tuple(e.entry.validation_report if type(e.entry) is ModelDiagnosticEntry else None for e in self.entries)
            if original != self.validation_result.diagnostics:
                raise ValueError('Validation operation must preserve every MOD-08 report in original order.')
            if self.status.value != {'valid': 'succeeded', 'invalid': 'failed', 'incomplete': 'incomplete'}[self.validation_result.status.value]:
                raise ValueError('Processing status cannot contradict the authoritative MOD-08 outcome.')


@dataclass(frozen=True, slots=True)
class ModelDiagnosticSummary:
    total: int
    errors: int
    warnings: int
    info: int

    def __post_init__(self) -> None:
        if any(type(v) is not int or v < 0 for v in (self.total, self.errors, self.warnings, self.info)) or self.total != self.errors + self.warnings + self.info:
            raise ValueError('Summary counts must be nonnegative and consistent.')


def summarize_model_diagnostics(entries: tuple[LocatedModelDiagnosticEntry, ...]) -> ModelDiagnosticSummary:
    if type(entries) not in (tuple, list) or any(type(e) is not LocatedModelDiagnosticEntry for e in entries):
        raise TypeError('Summary requires actual immutable diagnostic entries.')
    counts = {'error': 0, 'warning': 0, 'info': 0}
    for entry in entries:
        counts[entry.severity] += 1
    return ModelDiagnosticSummary(len(entries), counts['error'], counts['warning'], counts['info'])


@dataclass(frozen=True, slots=True)
class ModelDiagnosticReport:
    operations: tuple[ModelDiagnosticOperation, ...] = ()

    def __post_init__(self) -> None:
        if type(self.operations) not in (tuple, list) or any(type(o) is not ModelDiagnosticOperation for o in self.operations):
            raise TypeError('Report requires immutable explicit operation snapshots.')
        rank = {phase: i for i, phase in enumerate(ModelDiagnosticPhase)}
        operations = tuple(sorted(self.operations, key=lambda o: rank[o.phase]))
        validations = tuple(o.validation_result for o in operations if o.validation_result is not None) + tuple(o.compilation_report.validation_evidence for o in operations if o.compilation_report is not None and o.compilation_report.validation_evidence is not None)
        if validations and any(v is not validations[0] for v in validations):
            raise ValueError('One report preserves one authoritative validation run; compiler and validation operations must share the actual evidence object.')
        if sum(o.compilation_report is not None for o in operations) > 1:
            raise ValueError('Use separate reports for multiple compilation runs.')
        object.__setattr__(self, 'operations', operations)

    @property
    def entries(self) -> tuple[LocatedModelDiagnosticEntry, ...]:
        return tuple(e for operation in self.operations for e in operation.entries)

    @property
    def validation_result(self) -> ModelValidationResult | None:
        direct = next((o.validation_result for o in self.operations if o.validation_result is not None), None)
        return direct if direct is not None else None if self.compilation_report is None else self.compilation_report.validation_evidence

    @property
    def compilation_report(self) -> CompilationDiagnosticReport | None:
        return next((o.compilation_report for o in self.operations if o.compilation_report is not None), None)

    @property
    def compilation_status(self) -> str | None:
        return None if self.compilation_report is None else self.compilation_report.status

    @property
    def compilation_phase_outcomes(self) -> tuple[CompilerPhaseDiagnosticView, ...]:
        return () if self.compilation_report is None else self.compilation_report.phase_outcomes

    @property
    def validation_status(self) -> ModelValidationStatus | None:
        return None if self.validation_result is None else self.validation_result.status

    @property
    def compilation_readiness(self) -> CompilationReadiness | None:
        return None if self.validation_result is None else self.validation_result.readiness

    @property
    def stage_outcomes(self) -> tuple[ModelValidationStageResult, ...]:
        return () if self.validation_result is None else self.validation_result.stage_outcomes

    @property
    def processing_status(self) -> ModelDiagnosticProcessingStatus:
        statuses = tuple(o.status for o in self.operations)
        if not statuses or ModelDiagnosticProcessingStatus.UNAVAILABLE in statuses:
            return ModelDiagnosticProcessingStatus.UNAVAILABLE
        if ModelDiagnosticProcessingStatus.FAILED in statuses:
            return ModelDiagnosticProcessingStatus.FAILED
        if ModelDiagnosticProcessingStatus.PARTIAL in statuses:
            return ModelDiagnosticProcessingStatus.PARTIAL
        if ModelDiagnosticProcessingStatus.INCOMPLETE in statuses:
            return ModelDiagnosticProcessingStatus.INCOMPLETE
        return ModelDiagnosticProcessingStatus.SUCCEEDED

    @property
    def summary(self) -> ModelDiagnosticSummary:
        return summarize_model_diagnostics(self.entries)

    def by_severity(self, severity: str) -> tuple[LocatedModelDiagnosticEntry, ...]:
        if type(severity) is not str or severity not in ('error', 'warning', 'info'):
            raise ValueError('Use existing severity scalar values; no escalation/new severity model.')
        return tuple(e for e in self.entries if e.severity == severity)

    def by_origin(self, origin: ModelDiagnosticOrigin) -> tuple[LocatedModelDiagnosticEntry, ...]:
        if type(origin) is not ModelDiagnosticOrigin:
            raise TypeError('Origin filtering requires a supported origin.')
        return tuple(e for e in self.entries if e.origin is origin)

    def by_semantic_target(self, target: ModelDiagnosticTarget) -> tuple[LocatedModelDiagnosticEntry, ...]:
        if type(target) is not ModelDiagnosticTarget:
            raise TypeError('Target filtering requires an actual stable target association.')
        return tuple(e for e in self.entries if e.target == target)

    def by_source(self, source_id: ModelSourceId) -> tuple[LocatedModelDiagnosticEntry, ...]:
        if type(source_id) is not ModelSourceId:
            raise TypeError('Source filtering requires an explicit ModelSourceId.')
        return tuple(e for e in self.entries if any(t is not None and t.source_id == source_id for t in (e.source_target, *e.related_source_targets)))

    def by_compilation_origin(self, origin: CompilationDiagnosticOrigin) -> tuple[LocatedModelDiagnosticEntry, ...]:
        if type(origin) is not CompilationDiagnosticOrigin:
            raise TypeError('Use the explicit compiler responsibility.')
        return tuple(e for e in self.entries if type(e.entry) is ModelDiagnosticEntry and e.entry.compilation_details is not None and e.entry.compilation_details.origin is origin)

    def by_compilation_phase(self, phase_id: str | None) -> tuple[LocatedModelDiagnosticEntry, ...]:
        if phase_id is not None and (type(phase_id) is not str or re.fullmatch(r'CMP-PHASE-[A-Z0-9]+(?:-[A-Z0-9]+)*', phase_id) is None):
            raise ValueError('Use the actual compiler phase identifier or explicit absence.')
        return tuple(e for e in self.entries if type(e.entry) is ModelDiagnosticEntry and e.entry.compilation_details is not None and e.entry.compilation_details.phase_id == phase_id)

    def by_artifact_target(self, artifact: CompilationArtifactDiagnosticView) -> tuple[LocatedModelDiagnosticEntry, ...]:
        if type(artifact) is not CompilationArtifactDiagnosticView:
            raise TypeError('Artifact filtering uses the original bounded metadata projection.')
        return tuple(e for e in self.entries if type(e.entry) is ModelDiagnosticEntry and e.entry.compilation_details is not None and e.entry.compilation_details.artifact == artifact)

    def group_by_origin(self) -> Mapping[ModelDiagnosticOrigin, tuple[LocatedModelDiagnosticEntry, ...]]:
        groups = {origin: [] for origin in ModelDiagnosticOrigin}
        for entry in self.entries:
            groups[entry.origin].append(entry)
        return MappingProxyType({origin: tuple(entries) for origin, entries in groups.items() if entries})

    def group_by_severity(self) -> Mapping[str, tuple[LocatedModelDiagnosticEntry, ...]]:
        groups = {'error': [], 'warning': [], 'info': []}
        for entry in self.entries:
            groups[entry.severity].append(entry)
        return MappingProxyType({severity: tuple(entries) for severity, entries in groups.items() if entries})


ModelDiagnosticInput = CompilationDiagnosticReport | ModelLoadResult | ModelLoadBatchResult | AuthoringSchemaValidationResult | NamespaceResolutionResult | NamespaceEnvironmentResult | NamespaceSymbolSnapshotResult | SemanticReferenceResolutionResult | SemanticReferenceBatchResult | ResolvedAuthoringInputResult | CanonicalModelConstructionResult | CanonicalizationResult | TypeValidationResult | ModelValidationResult


@dataclass(frozen=True, slots=True)
class ModelDiagnosticReporter:
    def report(self, results: tuple[ModelDiagnosticInput, ...], context: ModelDiagnosticSourceContext) -> ModelDiagnosticReport:
        if type(results) not in (tuple, list) or type(context) is not ModelDiagnosticSourceContext:
            raise TypeError('Reporter requires explicit finite operation results and immutable source context.')
        operations = []
        for result in results:
            original_validation = None
            if type(result) is CompilationDiagnosticReport:
                entries = tuple(enrich_model_diagnostic(e, context) for e in result.entries)
                operations.append(ModelDiagnosticOperation(ModelDiagnosticPhase.COMPILATION, ModelDiagnosticProcessingStatus(result.status), entries, compilation_report=result))
                continue
            if type(result) in (ModelLoadResult, ModelLoadBatchResult):
                phase = ModelDiagnosticPhase.LOADING
                if type(result) is ModelLoadResult:
                    status = ModelDiagnosticProcessingStatus.SUCCEEDED if result.is_success else ModelDiagnosticProcessingStatus.FAILED
                else:
                    status = {ModelLoadBatchStatus.EMPTY: ModelDiagnosticProcessingStatus.UNAVAILABLE, ModelLoadBatchStatus.ALL_LOADED: ModelDiagnosticProcessingStatus.SUCCEEDED, ModelLoadBatchStatus.PARTIAL: ModelDiagnosticProcessingStatus.PARTIAL, ModelLoadBatchStatus.ALL_FAILED: ModelDiagnosticProcessingStatus.FAILED}[result.status]
                entries = tuple(enrich_model_diagnostic(d, context) for d in result.diagnostics)
                operations.append(ModelDiagnosticOperation(phase, status, entries))
                continue
            if type(result) is AuthoringSchemaValidationResult:
                phase, successful = ModelDiagnosticPhase.AUTHORING_SCHEMA, result.is_valid
            elif type(result) in (NamespaceResolutionResult, NamespaceEnvironmentResult, NamespaceSymbolSnapshotResult):
                phase, successful = ModelDiagnosticPhase.NAMESPACE_RESOLUTION, result.is_success
            elif type(result) is SemanticReferenceResolutionResult:
                phase, successful = ModelDiagnosticPhase.REFERENCE_RESOLUTION, result.is_success
            elif type(result) is SemanticReferenceBatchResult:
                phase, successful = ModelDiagnosticPhase.REFERENCE_RESOLUTION, result.all_required_bindings_satisfied
            elif type(result) is ResolvedAuthoringInputResult:
                phase, successful = ModelDiagnosticPhase.REFERENCE_RESOLUTION, result.ready_for_canonicalization
            elif type(result) is CanonicalModelConstructionResult:
                phase, successful = ModelDiagnosticPhase.CANONICAL_CONSTRUCTION, result.is_success
            elif type(result) is CanonicalizationResult:
                phase, successful = ModelDiagnosticPhase.CANONICALIZATION, result.is_success
            elif type(result) is TypeValidationResult:
                phase, successful = ModelDiagnosticPhase.TYPE_VALIDATION, result.is_valid
            elif type(result) is ModelValidationResult:
                phase, successful = ModelDiagnosticPhase.MODEL_VALIDATION, result.status.value == 'valid'
                original_validation = result
            else:
                raise TypeError('Unsupported operation result; origin/status cannot be guessed from messages or class names.')
            status = ModelDiagnosticProcessingStatus.SUCCEEDED if successful else ModelDiagnosticProcessingStatus.FAILED
            if type(result) is SemanticReferenceBatchResult and result.status.value == 'partially-resolved':
                status = ModelDiagnosticProcessingStatus.PARTIAL
            if original_validation is not None and original_validation.status.value == 'incomplete':
                status = ModelDiagnosticProcessingStatus.INCOMPLETE
            entries = tuple(enrich_model_diagnostic(associate_model_diagnostic(d, context.semantic), context) for d in result.diagnostics)
            operations.append(ModelDiagnosticOperation(phase, status, entries, original_validation))
        return ModelDiagnosticReport(operations)


def model_diagnostic_report_payload(report: ModelDiagnosticReport, *, include_messages: bool = False, include_source_details: bool = False, include_semantic_targets: bool = False, include_artifact_targets: bool = False, include_ir_identities: bool = False) -> dict[str, object]:
    """Explicit JSON-ready presentation, no HTTP/permission policy or repr dump.

    Caller uses existing authorization before opting into source/ID/text details.
    Defaults expose no arbitrary diagnostic text, source paths or semantic IDs.
    No absolute physical filename/source content/stack trace fields are emitted.
    """
    if type(report) is not ModelDiagnosticReport or any(type(v) is not bool for v in (include_messages, include_source_details, include_semantic_targets, include_artifact_targets, include_ir_identities)):
        raise TypeError('Transport requires the actual report and explicit disclosure booleans.')
    def location(loc: SourceLocation | None) -> dict[str, object] | None:
        if loc is None:
            return None
        return {'source_id': loc.source_id.value, 'start': {'line': loc.span.start.line, 'column': loc.span.start.column, 'offset': loc.span.start.offset}, 'end': {'line': loc.span.end.line, 'column': loc.span.end.column, 'offset': loc.span.end.offset}}
    def target(value: ModelDiagnosticTarget | None) -> dict[str, object] | None:
        if value is None:
            return None
        # Existing ref kinds determine representation, never infer exact version.
        reference = value.reference
        return {'kind': value.kind.value, 'element_id': reference.element_id.value, 'version': value.exact_version, 'field_id': None if value.field_id is None else value.field_id.value}
    entries = []
    for entry in report.entries:
        d = entry.diagnostic
        code = d.code.value if isinstance(d.code, Enum) else d.code
        item = {'code': code, 'severity': entry.severity, 'origin': entry.origin.value, 'validation_stage': entry.stage_id}
        if type(entry.entry) is ModelLoadDiagnostic:
            item['loading_stage'] = entry.entry.stage.value
            item['cause_codes'] = [] if entry.entry.schema_diagnostic is None else [entry.entry.schema_diagnostic.code]
            item['related_input_index'] = entry.entry.related_input_index
        else:
            item['cause_codes'] = list(entry.entry.cause_codes)
            if entry.origin is ModelDiagnosticOrigin.COMPILER:
                details = entry.entry.compilation_details
                item['compilation_phase'] = d.phase_id if details is None else details.phase_id
                item['compilation_origin'] = None if details is None else details.origin.value
                if include_ir_identities:
                    item['ir_identity'] = None if details is None else details.ir_identity
                if include_artifact_targets:
                    artifact = None if details is None else details.artifact
                    item['artifact_target'] = None if artifact is None else {'key': artifact.key, 'kind': artifact.kind, 'target': artifact.target}
                if include_semantic_targets:
                    scope = None if details is None else details.semantic_context
                    item['semantic_context'] = None if scope is None else scope.context_id.value
                if d.cause_code is not None:
                    item['cause_codes'].append(d.cause_code)
        if include_messages:
            item['message'] = d.message
        if include_semantic_targets:
            item['target'] = target(entry.target)
            item['related_targets'] = [] if type(entry.entry) is ModelLoadDiagnostic else [target(t) for t in entry.entry.related_targets]
        if include_source_details:
            item['source'] = None if entry.source_target is None else {'source_id': entry.source_target.source_id.value, 'path': None if entry.source_target.path is None else entry.source_target.path.pointer}
            item['location'] = location(entry.location)
            item['related_locations'] = [location(loc) for loc in entry.related_locations]
            item['related_sources'] = [None if t is None else {'source_id': t.source_id.value, 'path': None if t.path is None else t.path.pointer} for t in entry.related_source_targets]
            if type(entry.entry) is ModelLoadDiagnostic and entry.entry.position is not None:
                p = entry.entry.position
                item['position'] = {'line': p.line, 'column': p.column, 'offset': p.offset}
        entries.append(item)
    summary = report.summary
    return {'processing_status': report.processing_status.value,
            'validation_status': None if report.validation_status is None else report.validation_status.value,
            'compilation_readiness': None if report.compilation_readiness is None else report.compilation_readiness.value,
            'compilation_status': report.compilation_status,
            'compilation_artifact_count': None if report.compilation_report is None else report.compilation_report.artifact_count,
            'compilation_summary': None if report.compilation_report is None else {'total': report.compilation_report.summary.total, 'errors': report.compilation_report.summary.errors, 'warnings': report.compilation_report.summary.warnings, 'info': report.compilation_report.summary.info},
            'compilation_target': None if report.compilation_report is None or report.compilation_report.target is None else report.compilation_report.target,
            'compilation_phase_outcomes': [{'phase_id': o.phase_id, 'status': o.status, 'prerequisites': list(o.prerequisites), 'executed': o.executed, **({'reason': o.reason} if include_messages else {})} for o in report.compilation_phase_outcomes],
            'operations': [{'phase': o.phase.value, 'status': o.status.value} for o in report.operations],
            'stage_outcomes': [{'stage_id': s.stage_id, 'status': s.status.value, **({'reason': s.reason} if include_messages else {})} for s in report.stage_outcomes],
            'entries': entries, 'summary': {'total': summary.total, 'errors': summary.errors, 'warnings': summary.warnings, 'info': summary.info}}


__all__ += ['ModelDiagnosticProcessingStatus', 'ModelDiagnosticPhase', 'ModelDiagnosticSourceTarget',
            'ModelDiagnosticSourceContext', 'LocatedModelDiagnosticEntry', 'enrich_model_diagnostic',
            'ModelDiagnosticOperation', 'ModelDiagnosticSummary', 'summarize_model_diagnostics',
            'ModelDiagnosticReport', 'ModelDiagnosticInput', 'ModelDiagnosticReporter',
            'model_diagnostic_report_payload']
