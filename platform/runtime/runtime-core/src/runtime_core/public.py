"""RUN-01 pure runtime loading: explicit authority, verified bytes, no activation."""
from dataclasses import dataclass, field, fields, is_dataclass, replace
from enum import Enum
import re
from typing import Protocol
from semantic_kernel.public import SemanticContextRef, ElementVersionRef, ElementRef, SemanticElementId, SemanticVersion
from compiled_contracts.public import (CompilationArtifactKey, CompilationArtifactKind,
    RuntimeArtifactDescriptor, RuntimeArtifactMetadata, RuntimeArtifactDependencyRef,
    RuntimeArtifactFormatId, RuntimeArtifactFormatVersion, RuntimeTargetId,
    RuntimeCapabilityId, RuntimeCompatibilityVersion, RuntimeArtifactContentDeclaration)

MODULE_NAME = 'runtime-core'


class RuntimeArtifactLoadStatus(Enum):
    SUCCEEDED = 'succeeded'
    FAILED = 'failed'
    INCOMPLETE = 'incomplete'


class RuntimeLoadSeverity(Enum):
    ERROR = 'error'
    WARNING = 'warning'
    INFO = 'info'


class RuntimeArtifactLoadStage(Enum):
    PREFLIGHT = 'preflight'
    AUTHORIZATION = 'authorization'
    READ = 'read'
    COMPATIBILITY = 'compatibility'
    DECODE = 'decode'
    ASSEMBLY = 'assembly'


class RuntimeArtifactLoadFailure(Enum):
    INVALID_REQUEST = 'RUN-001'
    AUTHORIZATION_UNAVAILABLE = 'RUN-002'
    AUTHORIZATION_SCOPE_MISMATCH = 'RUN-003'
    MANIFEST_MISMATCH = 'RUN-004'
    RECEIPT_MISMATCH = 'RUN-005'
    READER_FAILED = 'RUN-006'
    INTEGRITY_INSUFFICIENT = 'RUN-007'
    UNSUPPORTED_ARTIFACT_KIND = 'RUN-008'
    UNSUPPORTED_FORMAT = 'RUN-009'
    UNSUPPORTED_FORMAT_VERSION = 'RUN-010'
    DECODER_UNAVAILABLE = 'RUN-011'
    DECODE_FAILED = 'RUN-012'
    TARGET_INCOMPATIBLE = 'RUN-013'
    CONTEXT_MISMATCH = 'RUN-014'
    REQUIRED_CAPABILITY_MISSING = 'RUN-015'
    DEPENDENCY_MISSING = 'RUN-016'
    DUPLICATE_ARTIFACT = 'RUN-017'
    RESOURCE_LIMIT_EXCEEDED = 'RUN-018'
    INCOMPLETE_SET = 'RUN-019'
    INVALID_REPRESENTATION = 'RUN-020'
    COMPATIBILITY_VERSION_MISMATCH = 'RUN-021'


def _tuple(values: object, expected: type) -> bool:
    return type(values) is tuple and all(type(v) is expected for v in values)


@dataclass(frozen=True, slots=True)
class RuntimeArtifactReaderDiagnostic:
    """Neutral reader report projection; bridge also retains original CMP diagnostics."""
    code: str
    message: str
    severity: RuntimeLoadSeverity
    read_stage: str | None = None
    manifest_identity: str | None = None
    artifact_key: CompilationArtifactKey | None = None
    artifact_kind: CompilationArtifactKind | None = None
    output_location: str | None = None
    source_type: str | None = None

    def __post_init__(self) -> None:
        if type(self.code) is not str or not self.code or type(self.message) is not str or type(self.severity) is not RuntimeLoadSeverity:
            raise TypeError('Reader diagnostics preserve actual code/message and typed severity.')
        for value in (self.read_stage, self.manifest_identity, self.output_location, self.source_type):
            if value is not None and type(value) is not str:
                raise TypeError('Reader association projections are optional exact text.')
        if self.artifact_key is not None and type(self.artifact_key) is not CompilationArtifactKey or self.artifact_kind is not None and type(self.artifact_kind) is not CompilationArtifactKind:
            raise TypeError('Reader associations preserve typed artifact coordinates.')


@dataclass(frozen=True, slots=True)
class RuntimeArtifactLoadDiagnostic:
    code: RuntimeArtifactLoadFailure
    message: str
    severity: RuntimeLoadSeverity
    stage: RuntimeArtifactLoadStage
    manifest_identity: str | None = None
    artifact_key: CompilationArtifactKey | None = None
    artifact_kind: CompilationArtifactKind | None = None
    runtime_target: RuntimeTargetId | None = None
    semantic_context: SemanticContextRef | None = None
    semantic_origins: tuple[ElementVersionRef, ...] = ()
    reader_diagnostics: tuple[RuntimeArtifactReaderDiagnostic, ...] = ()

    def __post_init__(self) -> None:
        if type(self.code) is not RuntimeArtifactLoadFailure or type(self.message) is not str or not self.message or type(self.severity) is not RuntimeLoadSeverity or type(self.stage) is not RuntimeArtifactLoadStage:
            raise TypeError('Runtime diagnostics require closed code/severity/stage and a message.')
        if self.manifest_identity is not None and type(self.manifest_identity) is not str:
            raise TypeError('Manifest diagnostic uses existing identity token projection.')
        for value, expected in ((self.artifact_key, CompilationArtifactKey), (self.artifact_kind, CompilationArtifactKind), (self.runtime_target, RuntimeTargetId), (self.semantic_context, SemanticContextRef)):
            if value is not None and type(value) is not expected:
                raise TypeError('Runtime diagnostic associations require actual typed coordinates.')
        if not _tuple(self.semantic_origins, ElementVersionRef) or not _tuple(self.reader_diagnostics, RuntimeArtifactReaderDiagnostic):
            raise TypeError('Diagnostic origins and reader causes are immutable typed tuples.')


class RuntimeArtifactLoadError(ValueError):
    def __init__(self, diagnostics: tuple[RuntimeArtifactLoadDiagnostic, ...], status: RuntimeArtifactLoadStatus = RuntimeArtifactLoadStatus.FAILED) -> None:
        if not _tuple(diagnostics, RuntimeArtifactLoadDiagnostic) or not diagnostics or status not in (RuntimeArtifactLoadStatus.FAILED, RuntimeArtifactLoadStatus.INCOMPLETE):
            raise TypeError('Expected load rejection has actual diagnostics and non-success status.')
        self.diagnostics = diagnostics
        self.status = status
        super().__init__('Runtime loading rejected; inspect structured diagnostics.')


@dataclass(frozen=True, slots=True)
class RuntimeArtifactLoadPolicy:
    """Runtime v0 always requires digest evidence and a complete manifest set."""
    maximum_artifact_count: int = 128
    maximum_artifact_bytes: int = 32 * 1024 * 1024
    maximum_aggregate_bytes: int = 128 * 1024 * 1024
    maximum_decoded_depth: int = 32
    maximum_decoded_elements: int = 100000
    maximum_decoded_scalar_bytes: int = 32 * 1024 * 1024

    def __post_init__(self) -> None:
        if any(type(getattr(self, f.name)) is not int or getattr(self, f.name) <= 0 for f in fields(self)):
            raise ValueError('Load limits require positive actual integers, never Boolean limits.')

    def bounded_by(self, server: 'RuntimeArtifactLoadPolicy') -> 'RuntimeArtifactLoadPolicy':
        if type(server) is not RuntimeArtifactLoadPolicy:
            raise TypeError('Load ceilings are trusted typed policy.')
        return RuntimeArtifactLoadPolicy(*(min(getattr(self, f.name), getattr(server, f.name)) for f in fields(self)))


@dataclass(frozen=True, slots=True)
class RuntimeArtifactLoadContext:
    semantic_context: SemanticContextRef
    runtime_target: RuntimeTargetId

    def __post_init__(self) -> None:
        if type(self.semantic_context) is not SemanticContextRef or type(self.runtime_target) is not RuntimeTargetId:
            raise TypeError('Loading context requires actual semantic scope and explicit runtime target.')


@dataclass(frozen=True, slots=True, eq=False)
class RuntimeArtifactLoadBinding:
    """Trusted bridge projection of checked CMP-07/08/09 scope, not a new manifest.

    Identity equality intentionally does not authorize another materialization.
    The bridge retains the actual manifest/receipt/request; no compiler graph
    or authoring structure crosses this runtime boundary.
    """
    manifest_identity: str
    manifest_schema_version: str
    semantic_context: SemanticContextRef
    compilation_target: str
    artifacts: tuple[RuntimeArtifactDescriptor, ...]
    selected_keys: tuple[CompilationArtifactKey, ...]
    complete_set: bool
    __hash__ = None

    def __post_init__(self) -> None:
        if type(self.manifest_identity) is not str or len(self.manifest_identity) > 160 or re.fullmatch(r'manifest-[a-z][a-z0-9]*(?:[.-][a-z0-9]+)*', self.manifest_identity) is None:
            raise ValueError('Binding preserves an existing validated CMP-07 manifest token.')
        if type(self.manifest_schema_version) is not str or type(self.semantic_context) is not SemanticContextRef or type(self.compilation_target) is not str or type(self.complete_set) is not bool:
            raise TypeError('Binding requires actual manifest version/context/target/completeness facts.')
        if not _tuple(self.artifacts, RuntimeArtifactDescriptor) or not self.artifacts or not _tuple(self.selected_keys, CompilationArtifactKey) or not self.selected_keys:
            raise TypeError('Binding requires finite typed manifest inventory and explicit selected keys.')
        if len({d.key for d in self.artifacts}) != len(self.artifacts):
            raise ValueError('Binding cannot contain duplicate artifact identities.')
        if tuple(sorted(self.artifacts, key=lambda d: d.key.value)) != self.artifacts or len(set(self.selected_keys)) != len(self.selected_keys):
            raise ValueError('Binding preserves manifest order and distinct selection.')
        selected = tuple(d.key for d in self.artifacts if d.key in self.selected_keys)
        if selected != self.selected_keys or self.complete_set and selected != tuple(d.key for d in self.artifacts):
            raise ValueError('Binding cannot substitute or omit selected declared identities.')


@dataclass(frozen=True, slots=True)
class RuntimeArtifactLoadRequest:
    binding: RuntimeArtifactLoadBinding
    context: RuntimeArtifactLoadContext
    policy: RuntimeArtifactLoadPolicy = field(default_factory=RuntimeArtifactLoadPolicy)

    def __post_init__(self) -> None:
        if type(self.binding) is not RuntimeArtifactLoadBinding or type(self.context) is not RuntimeArtifactLoadContext or type(self.policy) is not RuntimeArtifactLoadPolicy:
            raise TypeError('Load request is typed bound scope/context/policy; no caller callback or authorization flag.')


class RuntimeLoadDiagnostics:
    @staticmethod
    def create(code: RuntimeArtifactLoadFailure, message: str, *, request: RuntimeArtifactLoadRequest | None = None, descriptor: RuntimeArtifactDescriptor | None = None, stage: RuntimeArtifactLoadStage = RuntimeArtifactLoadStage.PREFLIGHT, incomplete: bool = False, causes: tuple[RuntimeArtifactReaderDiagnostic, ...] = ()) -> RuntimeArtifactLoadDiagnostic:
        return RuntimeArtifactLoadDiagnostic(code, message, RuntimeLoadSeverity.WARNING if incomplete else RuntimeLoadSeverity.ERROR, stage,
            None if request is None else request.binding.manifest_identity,
            None if descriptor is None else descriptor.key, None if descriptor is None else descriptor.kind,
            None if request is None else request.context.runtime_target,
            None if request is None else request.context.semantic_context,
            () if descriptor is None else descriptor.metadata.semantic_origins, causes)

    @staticmethod
    def reject(code: RuntimeArtifactLoadFailure, message: str, **associations: object) -> None:
        raise RuntimeArtifactLoadError((RuntimeLoadDiagnostics.create(code, message, **associations),),
            RuntimeArtifactLoadStatus.INCOMPLETE if associations.get('incomplete') else RuntimeArtifactLoadStatus.FAILED)


@dataclass(frozen=True, slots=True)
class RuntimeArtifactLoadAuthorization:
    """Only a trusted injected authorizer issues this decision; callers cannot submit it."""
    source_reference: str
    decision_reference: str
    binding: RuntimeArtifactLoadBinding
    context: RuntimeArtifactLoadContext
    authorized_keys: tuple[CompilationArtifactKey, ...]

    def __post_init__(self) -> None:
        for value in (self.source_reference, self.decision_reference):
            if type(value) is not str or len(value) > 160 or re.fullmatch(r'[a-z][a-z0-9]*(?:[.-][a-z0-9]+)*', value) is None:
                raise ValueError('Authority references are explicit non-secret bounded logical tokens.')
        if type(self.binding) is not RuntimeArtifactLoadBinding or type(self.context) is not RuntimeArtifactLoadContext or not _tuple(self.authorized_keys, CompilationArtifactKey) or len(set(self.authorized_keys)) != len(self.authorized_keys):
            raise TypeError('Authority must bind actual invocation scope/context and distinct typed keys.')


class RuntimeArtifactLoadAuthorizer(Protocol):
    def authorize(self, request: RuntimeArtifactLoadRequest) -> RuntimeArtifactLoadAuthorization:
        """Trusted boundary must authenticate/authorize; absence raises a load rejection."""
        ...


@dataclass(frozen=True, slots=True)
class UnavailableRuntimeArtifactLoadAuthorizer:
    def authorize(self, request: RuntimeArtifactLoadRequest) -> RuntimeArtifactLoadAuthorization:
        RuntimeLoadDiagnostics.reject(RuntimeArtifactLoadFailure.AUTHORIZATION_UNAVAILABLE,
            'No trusted load authorization integration is configured.', request=request,
            stage=RuntimeArtifactLoadStage.AUTHORIZATION, incomplete=True)


@dataclass(frozen=True, slots=True)
class RuntimeArtifactSourceEvidence:
    binding: RuntimeArtifactLoadBinding
    artifact_key: CompilationArtifactKey
    root_reference: str
    output_directory: str
    location: str
    byte_length: int
    sha256: str

    def __post_init__(self) -> None:
        if type(self.binding) is not RuntimeArtifactLoadBinding or type(self.artifact_key) is not CompilationArtifactKey or type(self.byte_length) is not int or self.byte_length < 0 or type(self.sha256) is not str or re.fullmatch(r'[0-9a-f]{64}', self.sha256) is None:
            raise ValueError('Source evidence requires actual bound identity/length/verified SHA-256.')
        if any(type(v) is not str or not v or len(v) > 240 or '/' in v or '\\' in v or any(ord(c) < 32 or ord(c) == 127 for c in v) for v in (self.root_reference, self.output_directory, self.location)):
            raise ValueError('Source evidence exposes logical CMP locations only, never absolute paths.')


@dataclass(frozen=True, slots=True)
class RuntimeVerifiedArtifactBytes:
    descriptor: RuntimeArtifactDescriptor
    evidence: RuntimeArtifactSourceEvidence
    content: bytes = field(repr=False)

    def __post_init__(self) -> None:
        if type(self.descriptor) is not RuntimeArtifactDescriptor or type(self.evidence) is not RuntimeArtifactSourceEvidence or type(self.content) is not bytes or self.descriptor.key != self.evidence.artifact_key or len(self.content) != self.evidence.byte_length:
            raise TypeError('Verified bytes retain actual descriptor, immutable bytes and consistent source evidence.')


@dataclass(frozen=True, slots=True)
class RuntimeArtifactByteReadResult:
    status: RuntimeArtifactLoadStatus
    binding: RuntimeArtifactLoadBinding
    artifacts: tuple[RuntimeVerifiedArtifactBytes, ...] = ()
    diagnostics: tuple[RuntimeArtifactReaderDiagnostic, ...] = ()

    def __post_init__(self) -> None:
        if type(self.status) is not RuntimeArtifactLoadStatus or type(self.binding) is not RuntimeArtifactLoadBinding or not _tuple(self.artifacts, RuntimeVerifiedArtifactBytes) or not _tuple(self.diagnostics, RuntimeArtifactReaderDiagnostic):
            raise TypeError('Read projection requires actual status/binding and typed immutable inventories.')
        if self.status is RuntimeArtifactLoadStatus.SUCCEEDED:
            expected = tuple(d for d in self.binding.artifacts if d.key in self.binding.selected_keys)
            if tuple(a.descriptor for a in self.artifacts) != expected or any(a.evidence.binding is not self.binding for a in self.artifacts) or any(d.severity is RuntimeLoadSeverity.ERROR for d in self.diagnostics):
                raise ValueError('Read success retains every selected descriptor and original source binding without errors.')
        elif self.artifacts or not self.diagnostics:
            raise ValueError('Failed/incomplete retrieval has diagnostics and no partial byte outputs.')


class RuntimeArtifactByteSource(Protocol):
    def read(self, binding: RuntimeArtifactLoadBinding, policy: RuntimeArtifactLoadPolicy) -> RuntimeArtifactByteReadResult:
        ...


class RuntimeArtifactRepresentation(Protocol):
    """Concrete approval is additionally mandatory; no unrestricted dictionary payload."""
    @property
    def semantic_context(self) -> SemanticContextRef:
        ...

    @property
    def semantic_origins(self) -> tuple[ElementVersionRef, ...]:
        ...

    @property
    def model_wide(self) -> bool:
        ...


@dataclass(frozen=True, slots=True)
class RuntimeArtifactDecodeResult:
    status: RuntimeArtifactLoadStatus
    representation: RuntimeArtifactRepresentation | None = field(default=None, repr=False)
    diagnostics: tuple[RuntimeArtifactLoadDiagnostic, ...] = ()

    def __post_init__(self) -> None:
        if type(self.status) is not RuntimeArtifactLoadStatus or not _tuple(self.diagnostics, RuntimeArtifactLoadDiagnostic):
            raise TypeError('Decode outcome requires explicit status and actual runtime diagnostics.')
        if self.status is RuntimeArtifactLoadStatus.SUCCEEDED:
            if self.representation is None or any(d.severity is RuntimeLoadSeverity.ERROR for d in self.diagnostics):
                raise ValueError('Decoder success has a representation and no errors; loader checks concrete approval.')
        elif self.representation is not None or not self.diagnostics:
            raise ValueError('Decoder non-success has diagnostics and exposes no representation.')


class RuntimeArtifactDecoder(Protocol):
    def decode(self, artifact: RuntimeVerifiedArtifactBytes, context: RuntimeArtifactLoadContext, limits: RuntimeArtifactLoadPolicy) -> RuntimeArtifactDecodeResult:
        """Approved implementation must enforce depth/elements during parsing, before allocation."""
        ...


def _frozen_class(value: type) -> bool:
    return isinstance(value, type) and is_dataclass(value) and value.__dataclass_params__.frozen and '__slots__' in value.__dict__ and value.__dictoffset__ == 0


@dataclass(frozen=True, slots=True)
class RuntimeArtifactDecoderRegistration:
    kind: CompilationArtifactKind
    format: RuntimeArtifactFormatId
    version: RuntimeArtifactFormatVersion
    runtime_target: RuntimeTargetId
    compatibility_version: RuntimeCompatibilityVersion
    supported_capabilities: tuple[RuntimeCapabilityId, ...]
    decoder: RuntimeArtifactDecoder = field(repr=False)
    representation_type: type
    representation_types: tuple[type, ...]
    enforces_parse_limits: bool

    def __post_init__(self) -> None:
        for value, expected in ((self.kind, CompilationArtifactKind), (self.format, RuntimeArtifactFormatId), (self.version, RuntimeArtifactFormatVersion), (self.runtime_target, RuntimeTargetId), (self.compatibility_version, RuntimeCompatibilityVersion)):
            if type(value) is not expected:
                raise TypeError('Decoder dispatch uses exact typed kind/format/version/runtime coordinates.')
        if not _tuple(self.supported_capabilities, RuntimeCapabilityId) or len(self.supported_capabilities) > 128 or len(set(self.supported_capabilities)) != len(self.supported_capabilities):
            raise ValueError('Approved decoder has bounded distinct explicit capabilities.')
        if not _frozen_class(type(self.decoder)) or not callable(getattr(type(self.decoder), 'decode', None)):
            raise TypeError('Approved decoder must be an explicitly injected frozen slotted implementation.')
        if type(self.representation_types) is not tuple or not self.representation_types or len(self.representation_types) > 128 or any(not _frozen_class(t) for t in self.representation_types) or len(set(self.representation_types)) != len(self.representation_types) or self.representation_type not in self.representation_types:
            raise TypeError('Approved representation graph declares concrete immutable slotted classes.')
        if not {'semantic_context', 'semantic_origins', 'model_wide'} <= {f.name for f in fields(self.representation_type)}:
            raise TypeError('Runtime representation explicitly declares scope and exact producer origin fields.')
        if self.enforces_parse_limits is not True:
            raise ValueError('Unsafe/unbounded decoder cannot be approved; parse limits must precede allocation.')
        object.__setattr__(self, 'supported_capabilities', tuple(sorted(self.supported_capabilities)))
        _inspect_immutable(self.decoder, (type(self.decoder),), RuntimeArtifactLoadPolicy())

    @property
    def dispatch_key(self) -> tuple[str, str, str, str, str]:
        return (self.kind.value, self.format.value, self.version.value, self.runtime_target.value, self.compatibility_version.value)


@dataclass(frozen=True, slots=True)
class RuntimeArtifactDecoderCatalog:
    registrations: tuple[RuntimeArtifactDecoderRegistration, ...] = ()
    recognized_kinds: tuple[CompilationArtifactKind, ...] = ()

    def __post_init__(self) -> None:
        if not _tuple(self.registrations, RuntimeArtifactDecoderRegistration) or len(self.registrations) > 128 or len({r.dispatch_key for r in self.registrations}) != len(self.registrations):
            raise ValueError('Trusted decoder approvals are bounded, explicit and unambiguous.')
        object.__setattr__(self, 'registrations', tuple(sorted(self.registrations, key=lambda r: r.dispatch_key)))
        if not _tuple(self.recognized_kinds, CompilationArtifactKind) or len(self.recognized_kinds) > 128 or len(set(self.recognized_kinds)) != len(self.recognized_kinds):
            raise ValueError('Recognized producer kinds require a distinct bounded explicit inventory.')
        object.__setattr__(self, 'recognized_kinds', tuple(sorted(set((*self.recognized_kinds, *(r.kind for r in self.registrations))), key=lambda k: k.value)))
        if len(self.recognized_kinds) > 128:
            raise ValueError('Combined recognized decoder-kind inventory exceeds its trusted catalog ceiling.')

    def select(self, request: RuntimeArtifactLoadRequest, descriptor: RuntimeArtifactDescriptor) -> RuntimeArtifactDecoderRegistration:
        reject = RuntimeLoadDiagnostics.reject
        associations = dict(request=request, descriptor=descriptor, stage=RuntimeArtifactLoadStage.COMPATIBILITY)
        candidates = tuple(r for r in self.registrations if r.kind == descriptor.kind)
        if descriptor.kind not in self.recognized_kinds:
            reject(RuntimeArtifactLoadFailure.UNSUPPORTED_ARTIFACT_KIND, 'Artifact kind has no approved runtime decoder capability.', incomplete=True, **associations)
        declaration = descriptor.metadata.content_declaration
        if declaration is None:
            reject(RuntimeArtifactLoadFailure.UNSUPPORTED_FORMAT, 'Producer has not declared a runtime content format.', incomplete=True, **associations)
        if not candidates:
            reject(RuntimeArtifactLoadFailure.DECODER_UNAVAILABLE, 'Recognized producer kind has no approved decoder implementation.', incomplete=True, **associations)
        candidates = tuple(r for r in candidates if r.format == declaration.format)
        if not candidates:
            reject(RuntimeArtifactLoadFailure.UNSUPPORTED_FORMAT, 'Content format has no approved decoder; filename is irrelevant.', incomplete=True, **associations)
        candidates = tuple(r for r in candidates if r.version == declaration.version)
        if not candidates:
            reject(RuntimeArtifactLoadFailure.UNSUPPORTED_FORMAT_VERSION, 'Exact artifact format version is unsupported; no migration.', incomplete=True, **associations)
        if declaration.runtime_target != request.context.runtime_target:
            reject(RuntimeArtifactLoadFailure.TARGET_INCOMPATIBLE, 'Declared runtime target differs from authorized loading target.', **associations)
        candidates = tuple(r for r in candidates if r.runtime_target == declaration.runtime_target)
        if not candidates:
            reject(RuntimeArtifactLoadFailure.TARGET_INCOMPATIBLE, 'No approved decoder supports this explicit runtime target.', incomplete=True, **associations)
        candidates = tuple(r for r in candidates if r.compatibility_version == declaration.compatibility_version)
        if not candidates:
            reject(RuntimeArtifactLoadFailure.COMPATIBILITY_VERSION_MISMATCH, 'Exact runtime compatibility declaration is unsupported.', incomplete=True, **associations)
        registration = candidates[0]
        if any(c not in registration.supported_capabilities for c in declaration.required_capabilities):
            reject(RuntimeArtifactLoadFailure.REQUIRED_CAPABILITY_MISSING, 'An explicit required runtime capability is not supported.', incomplete=True, **associations)
        return registration


_IMMUTABLE_CONTRACTS = (SemanticContextRef, SemanticElementId, SemanticVersion, ElementVersionRef, ElementRef,
    CompilationArtifactKey, CompilationArtifactKind, RuntimeArtifactFormatId,
    RuntimeArtifactFormatVersion, RuntimeTargetId, RuntimeCapabilityId, RuntimeCompatibilityVersion)


def _inspect_immutable(root: object, approved: tuple[type, ...], limits: RuntimeArtifactLoadPolicy) -> tuple[int, int]:
    """Iterative bounded graph inspection; no recursive decode or unrestricted reflection.

    Counts every occurrence, including repeated immutable leaves. Scalar budget
    is conservative (four bytes per text character, integer bit-size estimate).
    Only approved declared dataclass fields, exact tuples and closed scalars.
    """
    stack = [(root, 1, False)]
    ancestors: set[int] = set()
    elements = scalar_bytes = 0
    pending_nodes = 1
    while stack:
        value, depth, closing = stack.pop()
        if closing:
            ancestors.remove(id(value))
            continue
        pending_nodes -= 1
        elements += 1
        if elements > limits.maximum_decoded_elements or depth > limits.maximum_decoded_depth:
            RuntimeLoadDiagnostics.reject(RuntimeArtifactLoadFailure.RESOURCE_LIMIT_EXCEEDED, 'Decoded structure exceeds effective depth/element limits.', stage=RuntimeArtifactLoadStage.DECODE)
        actual = type(value)
        children = ()
        if actual in (str, bytes):
            scalar_bytes += len(value) * (4 if actual is str else 1)
        elif actual is int:
            scalar_bytes += max(1, (value.bit_length() + 7) // 8)
        elif value is None or actual is bool:
            scalar_bytes += 1
        elif actual is tuple:
            if len(value) > limits.maximum_decoded_elements - elements:
                RuntimeLoadDiagnostics.reject(RuntimeArtifactLoadFailure.RESOURCE_LIMIT_EXCEEDED, 'Decoded tuple exceeds remaining element budget.', stage=RuntimeArtifactLoadStage.DECODE)
            children = value
        elif actual in (*approved, *_IMMUTABLE_CONTRACTS):
            members = fields(actual)
            if len(members) > limits.maximum_decoded_elements - elements:
                RuntimeLoadDiagnostics.reject(RuntimeArtifactLoadFailure.RESOURCE_LIMIT_EXCEEDED, 'Decoded fields exceed remaining element budget.', stage=RuntimeArtifactLoadStage.DECODE)
            children = tuple(getattr(value, f.name) for f in members)
        else:
            RuntimeLoadDiagnostics.reject(RuntimeArtifactLoadFailure.INVALID_REPRESENTATION, 'Representation contains an unapproved or mutable value type.', stage=RuntimeArtifactLoadStage.DECODE)
        if scalar_bytes > limits.maximum_decoded_scalar_bytes:
            RuntimeLoadDiagnostics.reject(RuntimeArtifactLoadFailure.RESOURCE_LIMIT_EXCEEDED, 'Decoded scalar data exceeds effective resource budget.', stage=RuntimeArtifactLoadStage.DECODE)
        if children:
            if elements + pending_nodes + len(children) > limits.maximum_decoded_elements:
                RuntimeLoadDiagnostics.reject(RuntimeArtifactLoadFailure.RESOURCE_LIMIT_EXCEEDED, 'Decoded frontier exceeds remaining element budget.', stage=RuntimeArtifactLoadStage.DECODE)
            if id(value) in ancestors:
                RuntimeLoadDiagnostics.reject(RuntimeArtifactLoadFailure.INVALID_REPRESENTATION, 'Runtime representation must not contain an actual object cycle.', stage=RuntimeArtifactLoadStage.DECODE)
            ancestors.add(id(value))
            stack.append((value, depth, True))
            stack.extend((child, depth + 1, False) for child in reversed(children))
            pending_nodes += len(children)
    return elements, scalar_bytes


@dataclass(frozen=True, slots=True)
class LoadedRuntimeArtifact:
    descriptor: RuntimeArtifactDescriptor
    context: RuntimeArtifactLoadContext
    representation: RuntimeArtifactRepresentation = field(repr=False)
    source_evidence: RuntimeArtifactSourceEvidence
    decoder_registration: RuntimeArtifactDecoderRegistration = field(repr=False)
    limits: RuntimeArtifactLoadPolicy = field(repr=False)
    decoded_elements: int = field(init=False)
    decoded_scalar_bytes: int = field(init=False)

    def __post_init__(self) -> None:
        if type(self.descriptor) is not RuntimeArtifactDescriptor or type(self.context) is not RuntimeArtifactLoadContext or type(self.source_evidence) is not RuntimeArtifactSourceEvidence or type(self.decoder_registration) is not RuntimeArtifactDecoderRegistration or type(self.limits) is not RuntimeArtifactLoadPolicy:
            raise TypeError('Loaded artifact requires typed descriptor/context/source/decoder/limits.')
        registration = self.decoder_registration
        declaration = self.descriptor.metadata.content_declaration
        if declaration is None or (self.descriptor.kind, declaration.format, declaration.version, declaration.runtime_target, declaration.compatibility_version) != (registration.kind, registration.format, registration.version, registration.runtime_target, registration.compatibility_version) or declaration.runtime_target != self.context.runtime_target or any(c not in registration.supported_capabilities for c in declaration.required_capabilities):
            RuntimeLoadDiagnostics.reject(RuntimeArtifactLoadFailure.TARGET_INCOMPATIBLE, 'Loaded representation does not match approved dispatch/compatibility.', stage=RuntimeArtifactLoadStage.ASSEMBLY)
        if type(self.representation) is not registration.representation_type:
            RuntimeLoadDiagnostics.reject(RuntimeArtifactLoadFailure.INVALID_REPRESENTATION, 'Decoder returned a concrete representation outside its explicit approval.', stage=RuntimeArtifactLoadStage.DECODE)
        elements, scalar_bytes = _inspect_immutable(self.representation, registration.representation_types, self.limits)
        if type(self.representation.semantic_context) is not SemanticContextRef or self.representation.semantic_context != self.context.semantic_context or self.source_evidence.binding.semantic_context != self.context.semantic_context:
            RuntimeLoadDiagnostics.reject(RuntimeArtifactLoadFailure.CONTEXT_MISMATCH, 'Decoded and source contexts must preserve the requested semantic scope.', stage=RuntimeArtifactLoadStage.DECODE)
        metadata = self.descriptor.metadata
        if not _tuple(self.representation.semantic_origins, ElementVersionRef) or type(self.representation.model_wide) is not bool or (self.representation.semantic_origins, self.representation.model_wide) != (metadata.semantic_origins, metadata.model_wide):
            RuntimeLoadDiagnostics.reject(RuntimeArtifactLoadFailure.INVALID_REPRESENTATION, 'Decoded representation must preserve exact declared origins/model-wide meaning.', stage=RuntimeArtifactLoadStage.DECODE)
        if self.source_evidence.artifact_key != self.descriptor.key or self.descriptor not in self.source_evidence.binding.artifacts:
            raise ValueError('Loaded source identity cannot substitute the manifest descriptor.')
        object.__setattr__(self, 'decoded_elements', elements)
        object.__setattr__(self, 'decoded_scalar_bytes', scalar_bytes)

    @property
    def key(self) -> CompilationArtifactKey:
        return self.descriptor.key

    @property
    def semantic_origins(self) -> tuple[ElementVersionRef, ...]:
        return self.descriptor.metadata.semantic_origins


@dataclass(frozen=True, slots=True)
class LoadedRuntimeArtifactSet:
    binding: RuntimeArtifactLoadBinding
    context: RuntimeArtifactLoadContext
    authorization: RuntimeArtifactLoadAuthorization = field(repr=False)
    artifacts: tuple[LoadedRuntimeArtifact, ...]
    effective_policy: RuntimeArtifactLoadPolicy

    def __post_init__(self) -> None:
        if type(self.binding) is not RuntimeArtifactLoadBinding or type(self.context) is not RuntimeArtifactLoadContext or type(self.authorization) is not RuntimeArtifactLoadAuthorization or type(self.effective_policy) is not RuntimeArtifactLoadPolicy or not _tuple(self.artifacts, LoadedRuntimeArtifact):
            raise TypeError('Loaded set requires original scope/context/authority and typed immutable artifacts.')
        if not self.binding.complete_set or self.binding.semantic_context != self.context.semantic_context or self.authorization.binding is not self.binding or self.authorization.context != self.context or self.authorization.authorized_keys != self.binding.selected_keys:
            raise ValueError('Loaded set must retain exactly authorized complete scope/context.')
        if tuple(a.descriptor for a in self.artifacts) != self.binding.artifacts or any(a.source_evidence.binding is not self.binding or a.context != self.context or a.limits != self.effective_policy for a in self.artifacts):
            raise ValueError('Loaded set preserves full manifest order/membership/source/effective limits.')
        policy = self.effective_policy
        if len(self.artifacts) > policy.maximum_artifact_count or any(a.source_evidence.byte_length > policy.maximum_artifact_bytes for a in self.artifacts) or sum(a.source_evidence.byte_length for a in self.artifacts) > policy.maximum_aggregate_bytes or sum(a.decoded_elements for a in self.artifacts) > policy.maximum_decoded_elements or sum(a.decoded_scalar_bytes for a in self.artifacts) > policy.maximum_decoded_scalar_bytes:
            raise ValueError('Loaded set cannot exceed any aggregate effective resource bound.')


@dataclass(frozen=True, slots=True)
class RuntimeArtifactLoadResult:
    status: RuntimeArtifactLoadStatus
    loaded_set: LoadedRuntimeArtifactSet | None = field(default=None, repr=False)
    diagnostics: tuple[RuntimeArtifactLoadDiagnostic, ...] = ()

    def __post_init__(self) -> None:
        if type(self.status) is not RuntimeArtifactLoadStatus or not _tuple(self.diagnostics, RuntimeArtifactLoadDiagnostic):
            raise TypeError('Load result has explicit status and immutable structured diagnostics.')
        if self.status is RuntimeArtifactLoadStatus.SUCCEEDED:
            if type(self.loaded_set) is not LoadedRuntimeArtifactSet or any(d.severity is RuntimeLoadSeverity.ERROR for d in self.diagnostics):
                raise ValueError('Load success requires full authorized immutable set and no errors.')
        elif self.loaded_set is not None or not self.diagnostics:
            raise ValueError('Non-success must expose diagnostics and no partial loaded set.')


class RuntimeArtifactLoader(Protocol):
    def load(self, request: RuntimeArtifactLoadRequest) -> RuntimeArtifactLoadResult:
        ...


@dataclass(frozen=True, slots=True)
class DefaultRuntimeArtifactLoader:
    """Trusted composition injects source/authority/catalog; no request-supplied services."""
    source: RuntimeArtifactByteSource = field(repr=False)
    authorizer: RuntimeArtifactLoadAuthorizer = field(default_factory=UnavailableRuntimeArtifactLoadAuthorizer, repr=False)
    decoders: RuntimeArtifactDecoderCatalog = field(default_factory=RuntimeArtifactDecoderCatalog)
    server_policy: RuntimeArtifactLoadPolicy = field(default_factory=RuntimeArtifactLoadPolicy)

    def __post_init__(self) -> None:
        if not callable(getattr(type(self.source), 'read', None)) or not callable(getattr(type(self.authorizer), 'authorize', None)) or type(self.decoders) is not RuntimeArtifactDecoderCatalog or type(self.server_policy) is not RuntimeArtifactLoadPolicy:
            raise TypeError('Loader requires explicitly injected trusted ports, immutable catalog and limits.')

    def load(self, request: RuntimeArtifactLoadRequest) -> RuntimeArtifactLoadResult:
        diagnostics: list[RuntimeArtifactLoadDiagnostic] = []
        descriptor = None
        try:
            reject = RuntimeLoadDiagnostics.reject
            if type(request) is not RuntimeArtifactLoadRequest:
                reject(RuntimeArtifactLoadFailure.INVALID_REQUEST, 'Loader requires an actual immutable bound request.')
            binding = request.binding
            policy = request.policy.bounded_by(self.server_policy)
            if binding.manifest_schema_version != '0' or binding.compilation_target != 'artifact-build':
                reject(RuntimeArtifactLoadFailure.MANIFEST_MISMATCH, 'Loading supports the original CMP-07 V0 artifact-build manifest only.', request=request)
            if binding.semantic_context != request.context.semantic_context:
                reject(RuntimeArtifactLoadFailure.CONTEXT_MISMATCH, 'Manifest context differs from loading context.', request=request)
            if len(binding.artifacts) > policy.maximum_artifact_count:
                reject(RuntimeArtifactLoadFailure.RESOURCE_LIMIT_EXCEEDED, 'Complete declared artifact count exceeds effective load policy.', request=request)
            if not binding.complete_set or binding.selected_keys != tuple(d.key for d in binding.artifacts):
                reject(RuntimeArtifactLoadFailure.INCOMPLETE_SET, 'Runtime v0 requires ALL_DECLARED_ARTIFACTS; no subset or implicit dependency expansion.', request=request)
            keys = set(binding.selected_keys)
            metadata_elements = 0
            for descriptor in binding.artifacts:
                if type(descriptor.metadata) is not RuntimeArtifactMetadata or type(descriptor.metadata.dependencies) is not tuple or type(descriptor.metadata.semantic_origins) is not tuple:
                    reject(RuntimeArtifactLoadFailure.DEPENDENCY_MISSING, 'Unsupported dependency contract; no external dependency resolution.', request=request, descriptor=descriptor)
                metadata_elements += len(descriptor.metadata.semantic_origins) + len(descriptor.metadata.dependencies)
                if metadata_elements > policy.maximum_decoded_elements:
                    reject(RuntimeArtifactLoadFailure.RESOURCE_LIMIT_EXCEEDED, 'Declared origin/dependency metadata exceeds the effective element budget.', request=request, descriptor=descriptor)
                if not _tuple(descriptor.metadata.dependencies, RuntimeArtifactDependencyRef) or any(d.key not in keys for d in descriptor.metadata.dependencies):
                    reject(RuntimeArtifactLoadFailure.DEPENDENCY_MISSING, 'Mandatory explicit artifact dependency is absent or unsupported in loading scope.', request=request, descriptor=descriptor)
            descriptor = None
            authorization = self.authorizer.authorize(request)
            if type(authorization) is not RuntimeArtifactLoadAuthorization or authorization.binding is not binding or authorization.context != request.context or authorization.authorized_keys != binding.selected_keys:
                reject(RuntimeArtifactLoadFailure.AUTHORIZATION_SCOPE_MISMATCH, 'Trusted authority must bind this exact source invocation, context, target and selected identities.', request=request, stage=RuntimeArtifactLoadStage.AUTHORIZATION)
            # Validate support before filesystem access or any decoder runs.
            registrations = tuple(self.decoders.select(request, d) for d in binding.artifacts)
            retrieved = self.source.read(binding, policy)
            if type(retrieved) is not RuntimeArtifactByteReadResult or retrieved.binding is not binding:
                reject(RuntimeArtifactLoadFailure.READER_FAILED, 'Trusted byte source returned an invalid or differently bound read result.', request=request, stage=RuntimeArtifactLoadStage.READ)
            if retrieved.status is not RuntimeArtifactLoadStatus.SUCCEEDED:
                reject(RuntimeArtifactLoadFailure.READER_FAILED, 'CMP-09 retrieval did not succeed; original reader causes are retained.', request=request, stage=RuntimeArtifactLoadStage.READ, incomplete=retrieved.status is RuntimeArtifactLoadStatus.INCOMPLETE, causes=retrieved.diagnostics)
            if retrieved.diagnostics:
                diagnostics.append(RuntimeLoadDiagnostics.create(RuntimeArtifactLoadFailure.READER_FAILED, 'Reader completed with original advisory diagnostics.', request=request, stage=RuntimeArtifactLoadStage.READ, incomplete=True, causes=retrieved.diagnostics))
            if len(retrieved.artifacts) > policy.maximum_artifact_count or any(len(a.content) > policy.maximum_artifact_bytes for a in retrieved.artifacts) or sum(len(a.content) for a in retrieved.artifacts) > policy.maximum_aggregate_bytes:
                reject(RuntimeArtifactLoadFailure.RESOURCE_LIMIT_EXCEEDED, 'Retrieved bytes exceed effective runtime load limits.', request=request, stage=RuntimeArtifactLoadStage.READ)
            loaded: list[LoadedRuntimeArtifact] = []
            used_elements = used_scalar_bytes = 0
            for artifact, registration in zip(retrieved.artifacts, registrations):
                descriptor = artifact.descriptor
                # Every approved decoder receives the remaining aggregate parse budget.
                remaining = RuntimeArtifactLoadPolicy(policy.maximum_artifact_count, policy.maximum_artifact_bytes, policy.maximum_aggregate_bytes, policy.maximum_decoded_depth, policy.maximum_decoded_elements - used_elements, policy.maximum_decoded_scalar_bytes - used_scalar_bytes)
                decoded = registration.decoder.decode(artifact, request.context, remaining)
                if type(decoded) is not RuntimeArtifactDecodeResult:
                    reject(RuntimeArtifactLoadFailure.DECODE_FAILED, 'Approved decoder returned an invalid outcome contract.', request=request, descriptor=descriptor, stage=RuntimeArtifactLoadStage.DECODE)
                for diagnostic in decoded.diagnostics:
                    if diagnostic.manifest_identity not in (None, binding.manifest_identity) or diagnostic.artifact_key not in (None, descriptor.key) or diagnostic.artifact_kind not in (None, descriptor.kind) or diagnostic.runtime_target not in (None, request.context.runtime_target) or diagnostic.semantic_context not in (None, request.context.semantic_context) or diagnostic.semantic_origins and diagnostic.semantic_origins != descriptor.metadata.semantic_origins:
                        reject(RuntimeArtifactLoadFailure.DECODE_FAILED, 'Decoder diagnostic association does not match the current artifact invocation.', request=request, descriptor=descriptor, stage=RuntimeArtifactLoadStage.DECODE)
                    diagnostics.append(replace(diagnostic, manifest_identity=binding.manifest_identity,
                        artifact_key=descriptor.key, artifact_kind=descriptor.kind,
                        runtime_target=request.context.runtime_target, semantic_context=request.context.semantic_context,
                        semantic_origins=descriptor.metadata.semantic_origins))
                if decoded.status is not RuntimeArtifactLoadStatus.SUCCEEDED:
                    return RuntimeArtifactLoadResult(decoded.status, diagnostics=tuple(diagnostics))
                item = LoadedRuntimeArtifact(descriptor, request.context, decoded.representation, artifact.evidence, registration, policy)
                used_elements += item.decoded_elements
                used_scalar_bytes += item.decoded_scalar_bytes
                if used_elements > policy.maximum_decoded_elements or used_scalar_bytes > policy.maximum_decoded_scalar_bytes or len(loaded) + 1 < len(retrieved.artifacts) and (used_elements == policy.maximum_decoded_elements or used_scalar_bytes == policy.maximum_decoded_scalar_bytes):
                    reject(RuntimeArtifactLoadFailure.RESOURCE_LIMIT_EXCEEDED, 'Decoded set exceeds or exhausts the remaining aggregate budget.', request=request, descriptor=descriptor, stage=RuntimeArtifactLoadStage.DECODE)
                loaded.append(item)
            return RuntimeArtifactLoadResult(RuntimeArtifactLoadStatus.SUCCEEDED,
                LoadedRuntimeArtifactSet(binding, request.context, authorization, tuple(loaded), policy), tuple(diagnostics))
        except RuntimeArtifactLoadError as error:
            # Preserve structured failure categories and enrich missing invocation associations.
            bound = request if type(request) is RuntimeArtifactLoadRequest else None
            enriched = tuple(replace(d,
                manifest_identity=d.manifest_identity if d.manifest_identity is not None else None if bound is None else bound.binding.manifest_identity,
                runtime_target=d.runtime_target if d.runtime_target is not None else None if bound is None else bound.context.runtime_target,
                semantic_context=d.semantic_context if d.semantic_context is not None else None if bound is None else bound.context.semantic_context,
                artifact_key=d.artifact_key if d.artifact_key is not None else None if descriptor is None else descriptor.key,
                artifact_kind=d.artifact_kind if d.artifact_kind is not None else None if descriptor is None else descriptor.kind,
                semantic_origins=d.semantic_origins if d.semantic_origins else () if descriptor is None else descriptor.metadata.semantic_origins) for d in error.diagnostics)
            return RuntimeArtifactLoadResult(error.status, diagnostics=(*diagnostics, *enriched))


__all__ = [name for name in (
    'MODULE_NAME', 'RuntimeArtifactLoadStatus', 'RuntimeLoadSeverity', 'RuntimeArtifactLoadStage',
    'RuntimeArtifactLoadFailure', 'RuntimeArtifactReaderDiagnostic', 'RuntimeArtifactLoadDiagnostic',
    'RuntimeArtifactLoadError', 'RuntimeArtifactLoadPolicy', 'RuntimeArtifactLoadContext',
    'RuntimeArtifactLoadBinding', 'RuntimeArtifactLoadRequest', 'RuntimeLoadDiagnostics',
    'RuntimeArtifactLoadAuthorization', 'RuntimeArtifactLoadAuthorizer',
    'UnavailableRuntimeArtifactLoadAuthorizer', 'RuntimeArtifactSourceEvidence',
    'RuntimeVerifiedArtifactBytes', 'RuntimeArtifactByteReadResult', 'RuntimeArtifactByteSource',
    'RuntimeArtifactRepresentation', 'RuntimeArtifactDecodeResult', 'RuntimeArtifactDecoder',
    'RuntimeArtifactDecoderRegistration', 'RuntimeArtifactDecoderCatalog', 'LoadedRuntimeArtifact',
    'LoadedRuntimeArtifactSet', 'RuntimeArtifactLoadResult', 'RuntimeArtifactLoader',
    'DefaultRuntimeArtifactLoader')]


def _same_immutable(left: object, right: object) -> bool:
    """Compare already bounded approved values structurally, without custom object equality."""
    stack = [(left, right)]
    while stack:
        a, b = stack.pop()
        if type(a) is not type(b):
            return False
        if a is None or type(a) in (str, bytes, int, bool):
            if a != b:
                return False
        elif type(a) is tuple:
            if len(a) != len(b):
                return False
            stack.extend(zip(a, b))
        else:
            stack.extend((getattr(a, f.name), getattr(b, f.name)) for f in fields(type(a)))
    return True


@dataclass(frozen=True, slots=True)
class RuntimeArtifactLoadEquivalence:
    """CMP-06-style supported observation comparison, not rerun/input authenticity proof.

    Successful results must share the exact trusted source binding. Different
    source invocations are deliberately unsupported; the tooling boundary owns
    actual compiler/receipt associations. Digest equality alone is not byte
    equality. Concrete implementation classes and immutable options matter.
    """
    def results(self, left: RuntimeArtifactLoadResult, right: RuntimeArtifactLoadResult) -> bool:
        if type(left) is not RuntimeArtifactLoadResult or type(right) is not RuntimeArtifactLoadResult:
            raise TypeError('Runtime comparison requires actual load outcomes.')
        def diagnostic_value(d: RuntimeArtifactLoadDiagnostic) -> tuple:
            causes = tuple((c.code, c.severity, c.read_stage, c.manifest_identity,
                c.artifact_key, c.artifact_kind, c.output_location, c.source_type) for c in d.reader_diagnostics)
            return (d.code, d.severity, d.stage, d.manifest_identity, d.artifact_key,
                d.artifact_kind, d.runtime_target, d.semantic_context, d.semantic_origins, causes)
        if left.status is not right.status or tuple(map(diagnostic_value, left.diagnostics)) != tuple(map(diagnostic_value, right.diagnostics)):
            return False
        if left.loaded_set is None or right.loaded_set is None:
            return left.loaded_set is right.loaded_set
        a, b = left.loaded_set, right.loaded_set
        if a.binding is not b.binding:
            raise ValueError('Cross-source invocation equivalence is unsupported without original association comparison.')
        if a.context != b.context or a.authorization != b.authorization or a.effective_policy != b.effective_policy or len(a.artifacts) != len(b.artifacts):
            return False
        for x, y in zip(a.artifacts, b.artifacts):
            p, q = x.decoder_registration, y.decoder_registration
            if (x.descriptor, x.source_evidence, p.dispatch_key, p.supported_capabilities, p.representation_type, p.representation_types, p.enforces_parse_limits) != (y.descriptor, y.source_evidence, q.dispatch_key, q.supported_capabilities, q.representation_type, q.representation_types, q.enforces_parse_limits):
                return False
            if not _same_immutable(p.decoder, q.decoder) or not _same_immutable(x.representation, y.representation):
                return False
        return True


__all__ += ['RuntimeArtifactLoadEquivalence']
