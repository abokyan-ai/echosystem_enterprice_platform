"""MOD-02 loading contracts. No semantic resolution, registration or execution."""
from dataclasses import dataclass
from enum import Enum
from typing import Protocol
from model_authoring.public import (
    AuthoringModelDocument, AuthoringSchemaPath, AuthoringSchemaDiagnostic,
    AuthoringSchemaValidator,
)

MODULE_NAME = 'model-loader'
__all__ = [
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
    """One-based Unicode character line/column; no invented schema positions."""
    line: int
    column: int

    def __post_init__(self):
        if any(type(v) is not int or v < 1 for v in (self.line, self.column)):
            raise ValueError('Positions require positive one-based coordinates.')


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

    def __post_init__(self):
        object.__setattr__(self, 'diagnostics', _diagnostics(self.diagnostics))
        object.__setattr__(self, 'positions', tuple(self.positions))
        if type(self.source) is not ModelSourceInformation or (self.value is None) != bool(self.diagnostics) or any(d.source != self.source for d in self.diagnostics):
            raise ValueError('Decoding results require either a candidate or associated diagnostics.')
        if any(type(p) is not tuple or len(p) != 2 or type(p[0]) is not AuthoringSchemaPath or type(p[1]) is not SourcePosition for p in self.positions):
            raise TypeError('Decoder positions require immutable path/coordinate pairs.')


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

    def __post_init__(self):
        if type(self.source) is not ModelSourceInformation or type(self.document) is not AuthoringModelDocument:
            raise TypeError('Loaded snapshots require explicit source metadata and MOD-01 authoring contracts.')


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
        if decoded.diagnostics:
            return ModelLoadResult(info, None, decoded.diagnostics)
        tree_error = inspect_tree(decoded.value, self.options)
        if tree_error is not None:
            return ModelLoadResult(info, None, (ModelLoadDiagnostic(info, ModelLoadStage.DECODING, tree_error[0], tree_error[1]),))
        validated = AuthoringSchemaValidator().validate(decoded.value)
        if not validated.is_valid:
            positions = dict(decoded.positions)
            diagnostics = tuple(ModelLoadDiagnostic(info, ModelLoadStage.SCHEMA, 'MOD-LOAD-010', d.message, positions.get(d.path), d) for d in validated.diagnostics)
            return ModelLoadResult(info, None, diagnostics)
        return ModelLoadResult(info, LoadedAuthoringDocument(info, validated.document))

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
    def __init__(self, code, message, position=None):
        super().__init__(message)
        self.code, self.message, self.position = code, message, position


def failed(content, code, message, position=None):
    return SourceDecodeResult(content.source, None, (ModelLoadDiagnostic(content.source, ModelLoadStage.DECODING, code, message, position),))


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


def decode_json(content, options):
    if content.diagnostics:
        return SourceDecodeResult(content.source, None, content.diagnostics)
    try:
        json_depth(content.content, options)
        value = json.loads(content.content, object_pairs_hook=unique_pairs, parse_constant=reject_constant)
        error = inspect_tree(value, options)
        if error:
            return failed(content, *error)
        return SourceDecodeResult(content.source, value)
    except json.JSONDecodeError as exc:
        return failed(content, 'MOD-LOAD-005', 'Malformed strict JSON: ' + exc.msg, SourcePosition(exc.lineno, exc.colno))
    except DecodeFailure as exc:
        return failed(content, exc.code, exc.message, exc.position)
    except (ValueError, RecursionError, OverflowError):
        return failed(content, 'MOD-LOAD-014', 'JSON numeric or parser resource limits were exceeded.')


def decode_yaml(content, options):
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
                position = SourcePosition(event.start_mark.line + 1, event.start_mark.column + 1)
                if isinstance(event, yaml.events.DocumentStartEvent):
                    documents += 1
                    if documents > 1:
                        raise DecodeFailure('MOD-LOAD-007', 'Only one YAML document is allowed per source.', position)
                    if event.version not in (None, (1, 1)) or event.tags:
                        raise DecodeFailure('MOD-LOAD-008', 'Only YAML 1.1 without tag directives is supported.', position)
                if isinstance(event, yaml.events.AliasEvent) or getattr(event, 'anchor', None) is not None or getattr(event, 'tag', None) is not None:
                    raise DecodeFailure('MOD-LOAD-008', 'YAML aliases, anchors and explicit tags are unsupported.', position)
                if isinstance(event, (yaml.events.MappingStartEvent, yaml.events.SequenceStartEvent, yaml.events.ScalarEvent)):
                    nodes += 1
                    if nodes > options.max_nodes:
                        raise DecodeFailure('MOD-LOAD-014', 'YAML node limit exceeded.', position)
                    if isinstance(event, (yaml.events.MappingStartEvent, yaml.events.SequenceStartEvent)):
                        depth += 1
                    if depth > options.max_depth:
                        raise DecodeFailure('MOD-LOAD-014', 'YAML nesting limit exceeded.', position)
                elif isinstance(event, (yaml.events.MappingEndEvent, yaml.events.SequenceEndEvent)):
                    depth -= 1
        loader = yaml.SafeLoader(content.content)
        root = loader.get_single_node()
        positions = []

        def project(node, path):
            position = SourcePosition(node.start_mark.line + 1, node.start_mark.column + 1)
            positions.append((AuthoringSchemaPath(path), position))
            if isinstance(node, yaml.nodes.MappingNode):
                if node.tag != 'tag:yaml.org,2002:map':
                    raise DecodeFailure('MOD-LOAD-008', 'Unsupported YAML mapping tag.', position)
                value = {}
                for key, child in node.value:
                    if not isinstance(key, yaml.nodes.ScalarNode) or key.tag != 'tag:yaml.org,2002:str':
                        raise DecodeFailure('MOD-LOAD-008', 'YAML mapping keys must resolve to strings; merge keys are unsupported.', position)
                    if key.value in value:
                        raise DecodeFailure('MOD-LOAD-006', 'Duplicate YAML mapping key is unsupported.', SourcePosition(key.start_mark.line + 1, key.start_mark.column + 1))
                    value[key.value] = project(child, path + (key.value,))
                return value
            if isinstance(node, yaml.nodes.SequenceNode) and node.tag == 'tag:yaml.org,2002:seq':
                return [project(child, path + (i,)) for i, child in enumerate(node.value)]
            if isinstance(node, yaml.nodes.ScalarNode) and node.tag in {f'tag:yaml.org,2002:{tag}' for tag in ('str', 'int', 'float', 'bool', 'null')}:
                return loader.construct_object(node)
            raise DecodeFailure('MOD-LOAD-008', 'Unsupported YAML scalar or collection type; quote dates/timestamps.', position)

        value = None if root is None else project(root, ())
        error = inspect_tree(value, options)
        if error:
            return failed(content, *error)
        return SourceDecodeResult(content.source, value, positions=tuple(positions))
    except DecodeFailure as exc:
        return failed(content, exc.code, exc.message, exc.position)
    except yaml.YAMLError as exc:
        mark = getattr(exc, 'problem_mark', None)
        position = None if mark is None else SourcePosition(mark.line + 1, mark.column + 1)
        return failed(content, 'MOD-LOAD-005', 'Malformed YAML source.', position)
    except (ValueError, RecursionError, OverflowError):
        return failed(content, 'MOD-LOAD-014', 'YAML numeric or parser resource limits were exceeded.')
    finally:
        if loader is not None:
            loader.dispose()
