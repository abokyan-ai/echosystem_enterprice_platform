"""Pure loading/registry and execution context; explicit authority, no activation."""
from dataclasses import dataclass, field, fields, is_dataclass, replace
from enum import Enum
from datetime import datetime, timezone
from uuid import UUID
from threading import Lock
from types import MappingProxyType
import re
from typing import Protocol, Mapping
from semantic_kernel.public import SemanticContextRef, ElementVersionRef, ElementRef, SemanticElementId, SemanticVersion, QualifiedName, Namespace
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
    REGISTRY_PREFLIGHT = 'registry-preflight'
    REGISTRY_AUTHORIZATION = 'registry-authorization'
    REGISTRY_EXTRACTION = 'registry-extraction'
    REGISTRY_COMMIT = 'registry-commit'
    REGISTRY_LOOKUP = 'registry-lookup'
    REGISTRY_SNAPSHOT = 'registry-snapshot'


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
    REGISTRY_INVALID_REQUEST = 'RUN-101'
    REGISTRY_INVALID_SCOPE = 'RUN-102'
    REGISTRY_AUTHORIZATION_UNAVAILABLE = 'RUN-103'
    REGISTRY_AUTHORIZATION_MISMATCH = 'RUN-104'
    REGISTRY_LOAD_NOT_SUCCESSFUL = 'RUN-105'
    REGISTRY_LOAD_ASSOCIATION_MISMATCH = 'RUN-106'
    REGISTRY_UNSUPPORTED_DEFINITION = 'RUN-107'
    REGISTRY_INVALID_IDENTITY = 'RUN-108'
    REGISTRY_CONTEXT_MISMATCH = 'RUN-109'
    REGISTRY_TARGET_MISMATCH = 'RUN-110'
    REGISTRY_DUPLICATE_BATCH_IDENTITY = 'RUN-111'
    REGISTRY_DEFINITION_CONFLICT = 'RUN-112'
    REGISTRY_MUTABLE_DEFINITION = 'RUN-113'
    REGISTRY_NOT_FOUND = 'RUN-114'
    REGISTRY_AMBIGUOUS_NAME = 'RUN-115'
    REGISTRY_VERSION_REQUIRED = 'RUN-116'
    REGISTRY_SNAPSHOT_UNAVAILABLE = 'RUN-117'
    REGISTRY_RESOURCE_LIMIT_EXCEEDED = 'RUN-118'
    REGISTRY_EXTRACTION_FAILED = 'RUN-119'
    REGISTRY_NO_DEFINITIONS = 'RUN-120'
    REGISTRY_INTEGRITY_FAILURE = 'RUN-121'


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
    registry_scope: 'RuntimeModelRegistryScope | None' = None
    definition_identity: ElementVersionRef | None = None
    qualified_name: QualifiedName | None = None
    definition_kind: 'RuntimeModelDefinitionKind | None' = None
    registry_operation: 'RuntimeModelRegistryOperation | None' = None

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
        for value, expected in ((self.registry_scope, RuntimeModelRegistryScope), (self.definition_identity, ElementVersionRef), (self.qualified_name, QualifiedName), (self.definition_kind, RuntimeModelDefinitionKind), (self.registry_operation, RuntimeModelRegistryOperation)):
            if value is not None and type(value) is not expected:
                raise TypeError('Registry diagnostic coordinates must use actual immutable runtime/Kernel types.')
        if self.registry_scope is not None and (self.runtime_target not in (None, self.registry_scope.runtime_target) or self.semantic_context not in (None, self.registry_scope.semantic_context)):
            raise ValueError('Registry diagnostic scope cannot contradict runtime/context associations.')


class RuntimeArtifactLoadError(ValueError):
    def __init__(self, diagnostics: tuple[RuntimeArtifactLoadDiagnostic, ...], status: RuntimeArtifactLoadStatus = RuntimeArtifactLoadStatus.FAILED) -> None:
        if not _tuple(diagnostics, RuntimeArtifactLoadDiagnostic) or not diagnostics or status not in (RuntimeArtifactLoadStatus.FAILED, RuntimeArtifactLoadStatus.INCOMPLETE):
            raise TypeError('Expected load rejection has actual diagnostics and non-success status.')
        self.diagnostics = diagnostics
        self.status = status
        super().__init__('Runtime operation rejected; inspect structured diagnostics.')


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


_IMMUTABLE_CONTRACTS = (SemanticContextRef, SemanticElementId, SemanticVersion, ElementVersionRef, ElementRef, QualifiedName, Namespace,
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
                d.artifact_kind, d.runtime_target, d.semantic_context, d.semantic_origins, causes,
                d.registry_scope, d.definition_identity, d.qualified_name, d.definition_kind, d.registry_operation)
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


# RUN-02: registry consumes verified RUN-01 objects, never compiler/source bytes.
@dataclass(frozen=True, slots=True)
class RuntimeModelRegistryScope:
    semantic_context: SemanticContextRef
    runtime_target: RuntimeTargetId

    def __post_init__(self) -> None:
        if type(self.semantic_context) is not SemanticContextRef or type(self.semantic_context.context_id) is not SemanticElementId or type(self.runtime_target) is not RuntimeTargetId:
            raise TypeError('Registry scope is actual semantic context and explicit runtime target, never tenant/name.')


@dataclass(frozen=True, slots=True, order=True)
class RuntimeModelDefinitionKind:
    """Explicit supported runtime definition category; no actual kinds approved here."""
    value: str

    def __post_init__(self) -> None:
        RuntimeArtifactFormatId(self.value)


@dataclass(frozen=True, slots=True)
class RuntimeModelRegistryKey:
    scope: RuntimeModelRegistryScope
    identity: ElementVersionRef

    def __post_init__(self) -> None:
        if type(self.scope) is not RuntimeModelRegistryScope or not _registry_exact(self.identity):
            raise TypeError('Registry key requires scope plus actual exact semantic identity/version.')


def _registry_exact(value: object) -> bool:
    return type(value) is ElementVersionRef and type(value.element_id) is SemanticElementId and type(value.version) is SemanticVersion


def _registry_identity_order(reference: ElementVersionRef) -> tuple[str, int, int, int]:
    return (reference.element_id.value, reference.version.major, reference.version.minor, reference.version.patch)


def _registry_scope_order(scope: RuntimeModelRegistryScope) -> tuple[str, str]:
    return (scope.semantic_context.context_id.value, scope.runtime_target.value)


def _registry_key_order(key: RuntimeModelRegistryKey) -> tuple:
    return (*_registry_scope_order(key.scope), *_registry_identity_order(key.identity))


class RuntimeModelEmptyRegistrationPolicy(Enum):
    REJECT_EMPTY = 'reject-empty'
    ALLOW_VERIFIED_NO_CHANGE = 'allow-verified-no-change'


class RuntimeModelConflictPolicy(Enum):
    REJECT_CONFLICTS = 'reject-conflicts'


@dataclass(frozen=True, slots=True)
class RuntimeModelRegistryPolicy:
    maximum_definitions_per_registration: int = 1024
    maximum_definitions_per_scope: int = 8192
    maximum_total_definitions: int = 32768
    maximum_snapshot_entries: int = 8192
    conflict_policy: RuntimeModelConflictPolicy = RuntimeModelConflictPolicy.REJECT_CONFLICTS
    empty_registration: RuntimeModelEmptyRegistrationPolicy = RuntimeModelEmptyRegistrationPolicy.REJECT_EMPTY

    def __post_init__(self) -> None:
        if any(type(v) is not int or v <= 0 for v in (self.maximum_definitions_per_registration, self.maximum_definitions_per_scope, self.maximum_total_definitions, self.maximum_snapshot_entries)) or self.conflict_policy is not RuntimeModelConflictPolicy.REJECT_CONFLICTS or type(self.empty_registration) is not RuntimeModelEmptyRegistrationPolicy:
            raise ValueError('Registry policy requires positive actual limits and explicit supported conflict/empty policies.')

    def bounded_by(self, server: 'RuntimeModelRegistryPolicy') -> 'RuntimeModelRegistryPolicy':
        if type(server) is not RuntimeModelRegistryPolicy:
            raise TypeError('Registry ceilings require trusted immutable server policy.')
        empty = RuntimeModelEmptyRegistrationPolicy.REJECT_EMPTY if RuntimeModelEmptyRegistrationPolicy.REJECT_EMPTY in (self.empty_registration, server.empty_registration) else RuntimeModelEmptyRegistrationPolicy.ALLOW_VERIFIED_NO_CHANGE
        return RuntimeModelRegistryPolicy(min(self.maximum_definitions_per_registration, server.maximum_definitions_per_registration),
            min(self.maximum_definitions_per_scope, server.maximum_definitions_per_scope),
            min(self.maximum_total_definitions, server.maximum_total_definitions),
            min(self.maximum_snapshot_entries, server.maximum_snapshot_entries), empty_registration=empty)


class RuntimeModelRegistryOperation(Enum):
    REGISTER = 'register'
    LOOKUP = 'lookup'
    INSPECT_NAME = 'inspect-name'
    ENUMERATE_VERSIONS = 'enumerate-versions'
    SNAPSHOT = 'snapshot'


@dataclass(frozen=True, slots=True, eq=False)
class RuntimeModelRegistryBinding:
    """Instance-specific authority association, not a semantic key or deployment ID."""
    scopes: tuple[RuntimeModelRegistryScope, ...]
    __hash__ = None

    def __post_init__(self) -> None:
        if type(self.scopes) is not tuple or not 1 <= len(self.scopes) <= 128 or not _tuple(self.scopes, RuntimeModelRegistryScope) or len(set(self.scopes)) != len(self.scopes):
            raise ValueError('Registry owner declares a bounded distinct immutable scope allowlist.')
        object.__setattr__(self, 'scopes', tuple(sorted(self.scopes, key=_registry_scope_order)))


@dataclass(frozen=True, slots=True)
class RuntimeModelRegistrationRequest:
    scope: RuntimeModelRegistryScope
    load_result: RuntimeArtifactLoadResult = field(repr=False)
    policy: RuntimeModelRegistryPolicy = field(default_factory=RuntimeModelRegistryPolicy)

    def __post_init__(self) -> None:
        if type(self.scope) is not RuntimeModelRegistryScope or type(self.load_result) is not RuntimeArtifactLoadResult or type(self.policy) is not RuntimeModelRegistryPolicy:
            raise TypeError('Registration requires actual RUN-01 outcome, scope and policy; no caller definition or Boolean grant.')


@dataclass(frozen=True, slots=True)
class RuntimeModelLookupRequest:
    scope: RuntimeModelRegistryScope
    reference: ElementVersionRef | ElementRef

    def __post_init__(self) -> None:
        if type(self.scope) is not RuntimeModelRegistryScope or not (_registry_exact(self.reference) or type(self.reference) is ElementRef and type(self.reference.element_id) is SemanticElementId):
            raise TypeError('Lookup requires actual scope and exact reference or explicit versionless ElementRef.')


@dataclass(frozen=True, slots=True)
class RuntimeModelNameInspectionRequest:
    scope: RuntimeModelRegistryScope
    qualified_name: QualifiedName

    def __post_init__(self) -> None:
        if type(self.scope) is not RuntimeModelRegistryScope or type(self.qualified_name) is not QualifiedName or type(self.qualified_name.namespace) is not Namespace:
            raise TypeError('Name inspection uses actual explicit scope and Kernel QualifiedName.')


@dataclass(frozen=True, slots=True)
class RuntimeModelVersionInspectionRequest:
    scope: RuntimeModelRegistryScope
    reference: ElementRef

    def __post_init__(self) -> None:
        if type(self.scope) is not RuntimeModelRegistryScope or type(self.reference) is not ElementRef or type(self.reference.element_id) is not SemanticElementId:
            raise TypeError('Version enumeration is an explicit identity-only inspection operation.')


@dataclass(frozen=True, slots=True, eq=False)
class RuntimeModelRegistryAuthorizationRequest:
    registry_binding: RuntimeModelRegistryBinding
    scope: RuntimeModelRegistryScope
    operation: RuntimeModelRegistryOperation
    identities: tuple[ElementVersionRef, ...] = ()
    qualified_name: QualifiedName | None = None
    element_reference: ElementRef | None = None
    load_result: RuntimeArtifactLoadResult | None = field(default=None, repr=False)
    __hash__ = None

    def __post_init__(self) -> None:
        if type(self.registry_binding) is not RuntimeModelRegistryBinding or type(self.scope) is not RuntimeModelRegistryScope or self.scope not in self.registry_binding.scopes or type(self.operation) is not RuntimeModelRegistryOperation or not _tuple(self.identities, ElementVersionRef) or any(not _registry_exact(r) for r in self.identities) or len(set(self.identities)) != len(self.identities):
            raise TypeError('Authority request preserves declared registry instance, scope, operation and distinct exact keys.')
        if self.qualified_name is not None and type(self.qualified_name) is not QualifiedName or self.element_reference is not None and type(self.element_reference) is not ElementRef or self.load_result is not None and type(self.load_result) is not RuntimeArtifactLoadResult:
            raise TypeError('Authority uses typed optional name/reference/original load association.')
        if self.operation is RuntimeModelRegistryOperation.REGISTER:
            if self.load_result is None or self.qualified_name is not None or self.element_reference is not None:
                raise ValueError('Registration authority binds the actual loaded output and extracted exact identities.')
        elif self.load_result is not None:
            raise ValueError('Inspection authority cannot reuse a load/registration grant.')
        if self.operation is RuntimeModelRegistryOperation.INSPECT_NAME and self.qualified_name is None or self.operation is RuntimeModelRegistryOperation.ENUMERATE_VERSIONS and self.element_reference is None:
            raise ValueError('Inspection authority retains its exact requested selector.')
        if self.operation is RuntimeModelRegistryOperation.LOOKUP and (self.qualified_name is not None or not (len(self.identities) == 1 and self.element_reference is None or not self.identities and self.element_reference is not None)):
            raise ValueError('Lookup authority has one exact key or one identity-only reference, never a fallback selector.')
        if self.operation is RuntimeModelRegistryOperation.INSPECT_NAME and (self.identities or self.element_reference is not None) or self.operation is RuntimeModelRegistryOperation.ENUMERATE_VERSIONS and (self.identities or self.qualified_name is not None) or self.operation is RuntimeModelRegistryOperation.SNAPSHOT and (self.identities or self.element_reference is not None or self.qualified_name is not None):
            raise ValueError('Inspection selector must match the exact requested operation.')


@dataclass(frozen=True, slots=True)
class RuntimeModelRegistryAuthority:
    """Trusted injected authorizer issues this; caller cannot submit it to register/read."""
    request: RuntimeModelRegistryAuthorizationRequest
    source_reference: str
    decision_reference: str

    def __post_init__(self) -> None:
        if type(self.request) is not RuntimeModelRegistryAuthorizationRequest:
            raise TypeError('Registry decision binds the exact internal authorization invocation.')
        for value in (self.source_reference, self.decision_reference):
            if type(value) is not str or len(value) > 160 or re.fullmatch(r'[a-z][a-z0-9]*(?:[.-][a-z0-9]+)*', value) is None:
                raise ValueError('Authority references require bounded non-secret logical tokens.')


class RuntimeModelRegistryAuthorizer(Protocol):
    def authorize(self, request: RuntimeModelRegistryAuthorizationRequest) -> RuntimeModelRegistryAuthority:
        ...


class RuntimeRegistryDiagnostics:
    """Registry-specific association factory using the existing runtime diagnostic model."""
    @staticmethod
    def create(code: RuntimeArtifactLoadFailure, message: str, *, scope: RuntimeModelRegistryScope | None = None,
               operation: RuntimeModelRegistryOperation | None = None, stage: RuntimeArtifactLoadStage = RuntimeArtifactLoadStage.REGISTRY_PREFLIGHT,
               identity: ElementVersionRef | None = None, name: QualifiedName | None = None,
               kind: RuntimeModelDefinitionKind | None = None, artifact: LoadedRuntimeArtifact | None = None,
               incomplete: bool = False, routine: bool = False) -> RuntimeArtifactLoadDiagnostic:
        return RuntimeArtifactLoadDiagnostic(code, message,
            RuntimeLoadSeverity.INFO if routine else RuntimeLoadSeverity.WARNING if incomplete else RuntimeLoadSeverity.ERROR,
            stage, manifest_identity=None if artifact is None else artifact.source_evidence.binding.manifest_identity,
            artifact_key=None if artifact is None else artifact.descriptor.key,
            artifact_kind=None if artifact is None else artifact.descriptor.kind,
            runtime_target=None if scope is None else scope.runtime_target,
            semantic_context=None if scope is None else scope.semantic_context,
            semantic_origins=() if artifact is None else artifact.descriptor.metadata.semantic_origins,
            registry_scope=scope, definition_identity=identity, qualified_name=name, definition_kind=kind,
            registry_operation=operation)

    @staticmethod
    def reject(code: RuntimeArtifactLoadFailure, message: str, **associations: object) -> None:
        raise RuntimeArtifactLoadError((RuntimeRegistryDiagnostics.create(code, message, **associations),),
            RuntimeArtifactLoadStatus.INCOMPLETE if associations.get('incomplete') else RuntimeArtifactLoadStatus.FAILED)


@dataclass(frozen=True, slots=True)
class UnavailableRuntimeModelRegistryAuthorizer:
    def authorize(self, request: RuntimeModelRegistryAuthorizationRequest) -> RuntimeModelRegistryAuthority:
        RuntimeRegistryDiagnostics.reject(RuntimeArtifactLoadFailure.REGISTRY_AUTHORIZATION_UNAVAILABLE,
            'No trusted registry registration/inspection authorization integration is configured.',
            scope=request.scope, operation=request.operation,
            stage=RuntimeArtifactLoadStage.REGISTRY_AUTHORIZATION, incomplete=True)


class RuntimeModelDefinitionRepresentation(Protocol):
    """Explicit approved decoded node; no business-instance or new wire format."""
    @property
    def identity(self) -> ElementVersionRef:
        ...

    @property
    def semantic_context(self) -> SemanticContextRef:
        ...

    @property
    def runtime_target(self) -> RuntimeTargetId:
        ...

    @property
    def qualified_name(self) -> QualifiedName | None:
        ...

    @property
    def definition_kind(self) -> RuntimeModelDefinitionKind:
        ...


@dataclass(frozen=True, slots=True)
class RuntimeModelDefinitionExtractionResult:
    status: RuntimeArtifactLoadStatus
    definitions: tuple[RuntimeModelDefinitionRepresentation, ...] = field(default=(), repr=False)
    diagnostics: tuple[RuntimeArtifactLoadDiagnostic, ...] = ()

    def __post_init__(self) -> None:
        if type(self.status) is not RuntimeArtifactLoadStatus or type(self.definitions) is not tuple or not _tuple(self.diagnostics, RuntimeArtifactLoadDiagnostic):
            raise TypeError('Extraction returns explicit status and immutable inventories; concrete nodes are checked by registry.')
        if self.status is RuntimeArtifactLoadStatus.SUCCEEDED:
            if any(d.severity is RuntimeLoadSeverity.ERROR for d in self.diagnostics):
                raise ValueError('Successful extraction cannot contain errors.')
        elif self.definitions or not self.diagnostics:
            raise ValueError('Non-successful extraction exposes diagnostics and no partial definition nodes.')


class RuntimeModelDefinitionExtractor(Protocol):
    def extract(self, artifact: LoadedRuntimeArtifact, maximum_definitions: int) -> RuntimeModelDefinitionExtractionResult:
        """Select existing explicitly decoded definition nodes, bounded before collection allocation."""
        ...


@dataclass(frozen=True, slots=True)
class RuntimeModelDefinitionExtractionSupport:
    decoder_registration: RuntimeArtifactDecoderRegistration = field(repr=False)
    definition_types: tuple[type, ...]
    supported_kinds: tuple[RuntimeModelDefinitionKind, ...]
    extractor: RuntimeModelDefinitionExtractor = field(repr=False)
    allows_no_definitions: bool = False

    def __post_init__(self) -> None:
        if type(self.decoder_registration) is not RuntimeArtifactDecoderRegistration or type(self.definition_types) is not tuple or not self.definition_types or len(self.definition_types) > 128 or len(set(self.definition_types)) != len(self.definition_types):
            raise TypeError('Extraction approval binds the actual decoder approval and explicit bounded node classes.')
        required = {'identity', 'semantic_context', 'runtime_target', 'qualified_name', 'definition_kind'}
        if any(not _frozen_class(t) or t not in self.decoder_registration.representation_types or not required <= {f.name for f in fields(t)} for t in self.definition_types):
            raise TypeError('Definition nodes must be declared immutable classes already approved in the decoder graph.')
        if not _tuple(self.supported_kinds, RuntimeModelDefinitionKind) or not 1 <= len(self.supported_kinds) <= 128 or len(set(self.supported_kinds)) != len(self.supported_kinds) or type(self.allows_no_definitions) is not bool:
            raise ValueError('Extraction approval declares actual supported kinds and explicit empty-artifact behavior.')
        if not _frozen_class(type(self.extractor)) or not callable(getattr(type(self.extractor), 'extract', None)):
            raise TypeError('Extractor is an explicitly injected frozen slotted implementation, not an arbitrary callback.')
        _inspect_immutable(self.extractor, (type(self.extractor), RuntimeModelDefinitionKind), RuntimeArtifactLoadPolicy())
        object.__setattr__(self, 'supported_kinds', tuple(sorted(self.supported_kinds)))


@dataclass(frozen=True, slots=True)
class RuntimeModelDefinitionExtractionCatalog:
    supports: tuple[RuntimeModelDefinitionExtractionSupport, ...] = ()

    def __post_init__(self) -> None:
        if type(self.supports) is not tuple or len(self.supports) > 128 or not _tuple(self.supports, RuntimeModelDefinitionExtractionSupport) or len({s.decoder_registration.dispatch_key for s in self.supports}) != len(self.supports):
            raise ValueError('Trusted extraction support is bounded and unambiguous; default catalog is empty.')
        object.__setattr__(self, 'supports', tuple(sorted(self.supports, key=lambda s: s.decoder_registration.dispatch_key)))

    def select(self, artifact: LoadedRuntimeArtifact, scope: RuntimeModelRegistryScope) -> RuntimeModelDefinitionExtractionSupport:
        support = next((s for s in self.supports if s.decoder_registration is artifact.decoder_registration), None)
        if support is None:
            RuntimeRegistryDiagnostics.reject(RuntimeArtifactLoadFailure.REGISTRY_UNSUPPORTED_DEFINITION,
                'Loaded format has no approved definition extraction contract.', scope=scope,
                artifact=artifact, stage=RuntimeArtifactLoadStage.REGISTRY_EXTRACTION, incomplete=True)
        return support


def _registry_node_membership(artifact: LoadedRuntimeArtifact, nodes: tuple[RuntimeModelDefinitionRepresentation, ...]) -> bool:
    """Object association only: no inferred extraction, reference resolution or content equivalence.

    RUN-01's bounded graph inspection has already checked this graph. Identity
    proves a returned node belongs to the original decoded artifact, never a
    registry key, duplicate equivalence, authority token or semantic identity.
    """
    sought = {id(n) for n in nodes}
    seen: set[int] = set()
    stack = [artifact.representation]
    while stack and sought:
        value = stack.pop()
        sought.discard(id(value))
        if id(value) in seen:
            continue
        seen.add(id(value))
        if type(value) is tuple:
            stack.extend(value)
        elif type(value) in (*artifact.decoder_registration.representation_types, *_IMMUTABLE_CONTRACTS):
            stack.extend(getattr(value, f.name) for f in fields(type(value)))
    return not sought


@dataclass(frozen=True, slots=True)
class RuntimeModelDefinition:
    """Registry entry wraps one existing decoded node without copying its model data."""
    key: RuntimeModelRegistryKey
    qualified_name: QualifiedName | None
    definition_kind: RuntimeModelDefinitionKind
    representation: RuntimeModelDefinitionRepresentation = field(repr=False)
    load_result: RuntimeArtifactLoadResult = field(repr=False)
    loaded_artifact: LoadedRuntimeArtifact = field(repr=False)
    extraction_support: RuntimeModelDefinitionExtractionSupport = field(repr=False)

    def __post_init__(self) -> None:
        if type(self.key) is not RuntimeModelRegistryKey or type(self.definition_kind) is not RuntimeModelDefinitionKind or self.qualified_name is not None and (type(self.qualified_name) is not QualifiedName or type(self.qualified_name.namespace) is not Namespace) or type(self.load_result) is not RuntimeArtifactLoadResult or type(self.loaded_artifact) is not LoadedRuntimeArtifact or type(self.extraction_support) is not RuntimeModelDefinitionExtractionSupport:
            raise TypeError('Registry definition uses actual exact key, typed name/kind and original loaded associations.')
        loaded = self.load_result.loaded_set
        artifact = self.loaded_artifact
        support = self.extraction_support
        if self.load_result.status is not RuntimeArtifactLoadStatus.SUCCEEDED or type(loaded) is not LoadedRuntimeArtifactSet or not any(a is artifact for a in loaded.artifacts) or support.decoder_registration is not artifact.decoder_registration or type(self.representation) not in support.definition_types:
            RuntimeRegistryDiagnostics.reject(RuntimeArtifactLoadFailure.REGISTRY_LOAD_ASSOCIATION_MISMATCH, 'Definition requires a successful original load and approved original artifact node.', scope=self.key.scope, identity=self.key.identity)
        if self.definition_kind not in support.supported_kinds:
            RuntimeRegistryDiagnostics.reject(RuntimeArtifactLoadFailure.REGISTRY_UNSUPPORTED_DEFINITION, 'Definition kind has no explicit registry approval.', scope=self.key.scope, identity=self.key.identity, kind=self.definition_kind, artifact=artifact, incomplete=True)
        _inspect_immutable(self.representation, artifact.decoder_registration.representation_types, loaded.effective_policy)
        if not _registry_node_membership(artifact, (self.representation,)):
            RuntimeRegistryDiagnostics.reject(RuntimeArtifactLoadFailure.REGISTRY_LOAD_ASSOCIATION_MISMATCH, 'Definition node is not part of the original loaded representation.', scope=self.key.scope, identity=self.key.identity, artifact=artifact)
        node = self.representation
        if not _registry_exact(node.identity) or (node.identity, node.qualified_name, node.definition_kind) != (self.key.identity, self.qualified_name, self.definition_kind):
            RuntimeRegistryDiagnostics.reject(RuntimeArtifactLoadFailure.REGISTRY_INVALID_IDENTITY, 'Entry must preserve exact encoded identity/name/kind.', scope=self.key.scope, artifact=artifact)
        if type(node.semantic_context) is not SemanticContextRef or node.semantic_context != self.key.scope.semantic_context or loaded.context.semantic_context != self.key.scope.semantic_context:
            RuntimeRegistryDiagnostics.reject(RuntimeArtifactLoadFailure.REGISTRY_CONTEXT_MISMATCH, 'Encoded definition and original load differ from destination context.', scope=self.key.scope, identity=self.key.identity, artifact=artifact)
        if type(node.runtime_target) is not RuntimeTargetId or node.runtime_target != self.key.scope.runtime_target or loaded.context.runtime_target != self.key.scope.runtime_target:
            RuntimeRegistryDiagnostics.reject(RuntimeArtifactLoadFailure.REGISTRY_TARGET_MISMATCH, 'Encoded definition and original load differ from destination runtime target.', scope=self.key.scope, identity=self.key.identity, artifact=artifact)
        metadata = artifact.descriptor.metadata
        if not metadata.model_wide and self.key.identity not in metadata.semantic_origins:
            RuntimeRegistryDiagnostics.reject(RuntimeArtifactLoadFailure.REGISTRY_LOAD_ASSOCIATION_MISMATCH, 'Definition identity is outside the artifact’s exact declared origins.', scope=self.key.scope, identity=self.key.identity, artifact=artifact)

    @property
    def identity(self) -> ElementVersionRef:
        return self.key.identity

    @property
    def semantic_context(self) -> SemanticContextRef:
        return self.key.scope.semantic_context

    @property
    def runtime_target(self) -> RuntimeTargetId:
        return self.key.scope.runtime_target

    @property
    def source_evidence(self) -> RuntimeArtifactSourceEvidence:
        return self.loaded_artifact.source_evidence


@dataclass(frozen=True, slots=True)
class RuntimeModelRegistrySnapshot:
    scope: RuntimeModelRegistryScope
    definitions: tuple[RuntimeModelDefinition, ...] = field(default=(), repr=False)

    def __post_init__(self) -> None:
        if type(self.scope) is not RuntimeModelRegistryScope or not _tuple(self.definitions, RuntimeModelDefinition) or any(d.key.scope != self.scope for d in self.definitions):
            raise TypeError('Snapshot contains actual immutable definitions from exactly one explicit scope.')
        keys = tuple(d.key for d in self.definitions)
        if len(set(keys)) != len(keys) or tuple(sorted(keys, key=_registry_key_order)) != keys:
            raise ValueError('Snapshot preserves distinct exact keys in numeric semantic version order.')


@dataclass(frozen=True, slots=True)
class RuntimeModelRegistrationResult:
    status: RuntimeArtifactLoadStatus
    scope: RuntimeModelRegistryScope | None = None
    registered_identities: tuple[ElementVersionRef, ...] = ()
    load_result: RuntimeArtifactLoadResult | None = field(default=None, repr=False)
    diagnostics: tuple[RuntimeArtifactLoadDiagnostic, ...] = ()

    def __post_init__(self) -> None:
        if type(self.status) is not RuntimeArtifactLoadStatus or self.scope is not None and type(self.scope) is not RuntimeModelRegistryScope or not _tuple(self.registered_identities, ElementVersionRef) or any(not _registry_exact(r) for r in self.registered_identities) or not _tuple(self.diagnostics, RuntimeArtifactLoadDiagnostic):
            raise TypeError('Registration outcome retains explicit status, scope, immutable keys and actual diagnostics.')
        if len(set(self.registered_identities)) != len(self.registered_identities) or tuple(sorted(self.registered_identities, key=_registry_identity_order)) != self.registered_identities:
            raise ValueError('Committed identities are unique and numerically ordered.')
        if self.status is RuntimeArtifactLoadStatus.SUCCEEDED:
            if self.scope is None or type(self.load_result) is not RuntimeArtifactLoadResult or self.load_result.status is not RuntimeArtifactLoadStatus.SUCCEEDED or any(d.severity is RuntimeLoadSeverity.ERROR for d in self.diagnostics):
                raise ValueError('Registration success requires original successful load, scope and no errors.')
        elif self.registered_identities or self.load_result is not None or not self.diagnostics:
            raise ValueError('Non-success exposes no partial committed membership/evidence.')


class RuntimeModelLookupStatus(Enum):
    FOUND = 'found'
    NOT_FOUND = 'not-found'
    INVALID_REQUEST = 'invalid-request'
    VERSION_REQUIRED = 'version-required'
    AMBIGUOUS = 'ambiguous'
    FAILED = 'failed'
    INCOMPLETE = 'incomplete'


@dataclass(frozen=True, slots=True)
class RuntimeModelLookupResult:
    status: RuntimeModelLookupStatus
    definitions: tuple[RuntimeModelDefinition, ...] = field(default=(), repr=False)
    diagnostics: tuple[RuntimeArtifactLoadDiagnostic, ...] = ()

    def __post_init__(self) -> None:
        if type(self.status) is not RuntimeModelLookupStatus or not _tuple(self.definitions, RuntimeModelDefinition) or not _tuple(self.diagnostics, RuntimeArtifactLoadDiagnostic):
            raise TypeError('Lookup has explicit routine/failure status and immutable definition candidates/diagnostics.')
        if self.status in (RuntimeModelLookupStatus.FOUND, RuntimeModelLookupStatus.AMBIGUOUS):
            if (len(self.definitions) != 1 if self.status is RuntimeModelLookupStatus.FOUND else len(self.definitions) < 2) or any(d.severity is RuntimeLoadSeverity.ERROR for d in self.diagnostics):
                raise ValueError('Found is one exact definition; ambiguous exposes multiple ordered candidates.')
            keys = tuple(d.key for d in self.definitions)
            if len(set(keys)) != len(keys) or len({k.scope for k in keys}) != 1 or tuple(sorted(keys, key=_registry_key_order)) != keys:
                raise ValueError('Lookup candidates require unique ordered keys in one scope.')
        elif self.definitions or not self.diagnostics:
            raise ValueError('Negative/failed lookup exposes diagnostics and no placeholder definitions.')


@dataclass(frozen=True, slots=True)
class RuntimeModelMembershipResult:
    status: RuntimeModelLookupStatus
    present: bool | None
    diagnostics: tuple[RuntimeArtifactLoadDiagnostic, ...] = ()

    def __post_init__(self) -> None:
        if type(self.status) is not RuntimeModelLookupStatus or not _tuple(self.diagnostics, RuntimeArtifactLoadDiagnostic) or self.present is not (True if self.status is RuntimeModelLookupStatus.FOUND else False if self.status is RuntimeModelLookupStatus.NOT_FOUND else None):
            raise ValueError('Membership is true/false only for authorized found/not-found; otherwise unknown.')
        if self.status is not RuntimeModelLookupStatus.FOUND and not self.diagnostics or self.status is RuntimeModelLookupStatus.FOUND and any(d.severity is RuntimeLoadSeverity.ERROR for d in self.diagnostics):
            raise ValueError('Membership retains negative/failure evidence; found cannot contain errors.')


@dataclass(frozen=True, slots=True)
class RuntimeModelVersionInspectionResult:
    status: RuntimeModelLookupStatus
    identities: tuple[ElementVersionRef, ...] = ()
    diagnostics: tuple[RuntimeArtifactLoadDiagnostic, ...] = ()

    def __post_init__(self) -> None:
        if type(self.status) is not RuntimeModelLookupStatus or not _tuple(self.identities, ElementVersionRef) or any(not _registry_exact(r) for r in self.identities) or not _tuple(self.diagnostics, RuntimeArtifactLoadDiagnostic):
            raise TypeError('Version inspection contains actual explicit status and exact identities.')
        if self.status is RuntimeModelLookupStatus.FOUND:
            if not self.identities or len(set(self.identities)) != len(self.identities) or len({r.element_id for r in self.identities}) != 1 or tuple(sorted(self.identities, key=_registry_identity_order)) != self.identities or any(d.severity is RuntimeLoadSeverity.ERROR for d in self.diagnostics):
                raise ValueError('Successful enumeration retains every ordered exact version for one identity.')
        elif self.identities or not self.diagnostics:
            raise ValueError('Negative/failed enumeration exposes no partial candidates.')


@dataclass(frozen=True, slots=True)
class RuntimeModelRegistrySnapshotResult:
    status: RuntimeArtifactLoadStatus
    snapshot: RuntimeModelRegistrySnapshot | None = field(default=None, repr=False)
    diagnostics: tuple[RuntimeArtifactLoadDiagnostic, ...] = ()

    def __post_init__(self) -> None:
        if type(self.status) is not RuntimeArtifactLoadStatus or not _tuple(self.diagnostics, RuntimeArtifactLoadDiagnostic):
            raise TypeError('Snapshot result requires explicit status and actual runtime diagnostics.')
        if self.status is RuntimeArtifactLoadStatus.SUCCEEDED:
            if type(self.snapshot) is not RuntimeModelRegistrySnapshot or any(d.severity is RuntimeLoadSeverity.ERROR for d in self.diagnostics):
                raise ValueError('Snapshot success contains a coherent immutable snapshot and no errors.')
        elif self.snapshot is not None or not self.diagnostics:
            raise ValueError('Non-successful snapshot exposes no partial or unauthorized membership.')


@dataclass(frozen=True, slots=True)
class _RuntimeModelRegistryState:
    definitions: tuple[RuntimeModelDefinition, ...]
    exact: 'Mapping[RuntimeModelRegistryKey, RuntimeModelDefinition]' = field(repr=False)
    by_scope: 'Mapping[RuntimeModelRegistryScope, tuple[RuntimeModelDefinition, ...]]' = field(repr=False)
    by_name: 'Mapping[tuple[RuntimeModelRegistryScope, QualifiedName], tuple[RuntimeModelDefinition, ...]]' = field(repr=False)
    by_identity: 'Mapping[tuple[RuntimeModelRegistryScope, SemanticElementId], tuple[ElementVersionRef, ...]]' = field(repr=False)


def _registry_state(definitions: tuple[RuntimeModelDefinition, ...]) -> _RuntimeModelRegistryState:
    ordered = tuple(sorted(definitions, key=lambda d: _registry_key_order(d.key)))
    exact = {d.key: d for d in ordered}
    if len(exact) != len(ordered):
        raise ValueError('Internal state cannot contain duplicate exact scoped keys.')
    scopes: dict[RuntimeModelRegistryScope, list[RuntimeModelDefinition]] = {}
    names: dict[tuple[RuntimeModelRegistryScope, QualifiedName], list[RuntimeModelDefinition]] = {}
    identities: dict[tuple[RuntimeModelRegistryScope, SemanticElementId], list[ElementVersionRef]] = {}
    for definition in ordered:
        scopes.setdefault(definition.key.scope, []).append(definition)
        identities.setdefault((definition.key.scope, definition.identity.element_id), []).append(definition.identity)
        if definition.qualified_name is not None:
            names.setdefault((definition.key.scope, definition.qualified_name), []).append(definition)
    return _RuntimeModelRegistryState(ordered, MappingProxyType(exact),
        MappingProxyType({k: tuple(v) for k, v in scopes.items()}),
        MappingProxyType({k: tuple(v) for k, v in names.items()}),
        MappingProxyType({k: tuple(v) for k, v in identities.items()}))


class RuntimeModelRegistry(Protocol):
    def register(self, request: RuntimeModelRegistrationRequest) -> RuntimeModelRegistrationResult:
        ...

    def lookup(self, request: RuntimeModelLookupRequest) -> RuntimeModelLookupResult:
        ...

    def contains(self, request: RuntimeModelLookupRequest) -> RuntimeModelMembershipResult:
        ...

    def inspect_name(self, request: RuntimeModelNameInspectionRequest) -> RuntimeModelLookupResult:
        ...

    def versions(self, request: RuntimeModelVersionInspectionRequest) -> RuntimeModelVersionInspectionResult:
        ...

    def snapshot(self, scope: RuntimeModelRegistryScope) -> RuntimeModelRegistrySnapshotResult:
        ...


class LocalRuntimeModelRegistry:
    """Application-owned local catalog. Private lock + immutable copy-on-write state.

    No default/global instance, activation pointer, IO, parsing or cross-process
    synchronization. Every public read/mutation invokes the trusted authorizer.
    User-supplied extractors/authority cannot be attached through request data.
    """
    __slots__ = ('_binding', '_authorizer', '_catalog', '_policy', '_lock', '_state')

    def __init__(self, scopes: tuple[RuntimeModelRegistryScope, ...], *,
                 authorizer: RuntimeModelRegistryAuthorizer | None = None,
                 extraction_catalog: RuntimeModelDefinitionExtractionCatalog | None = None,
                 policy: RuntimeModelRegistryPolicy | None = None) -> None:
        self._binding = RuntimeModelRegistryBinding(scopes)
        self._authorizer = UnavailableRuntimeModelRegistryAuthorizer() if authorizer is None else authorizer
        self._catalog = RuntimeModelDefinitionExtractionCatalog() if extraction_catalog is None else extraction_catalog
        self._policy = RuntimeModelRegistryPolicy() if policy is None else policy
        if not callable(getattr(type(self._authorizer), 'authorize', None)) or type(self._catalog) is not RuntimeModelDefinitionExtractionCatalog or type(self._policy) is not RuntimeModelRegistryPolicy:
            raise TypeError('Registry owner supplies trusted authority, immutable extraction approvals and server policy.')
        self._lock = Lock()
        self._state = _registry_state(())

    def _current_state(self) -> _RuntimeModelRegistryState:
        """Called only under the private lock; detect malformed internal index shapes."""
        state = self._state
        if type(state) is not _RuntimeModelRegistryState or type(state.definitions) is not tuple or any(type(index) is not MappingProxyType for index in (state.exact, state.by_scope, state.by_name, state.by_identity)):
            RuntimeRegistryDiagnostics.reject(RuntimeArtifactLoadFailure.REGISTRY_INTEGRITY_FAILURE,
                'Internal registry state does not satisfy its immutable index contract.')
        return state

    def _read_definitions(self, definitions: tuple[RuntimeModelDefinition, ...], scope: RuntimeModelRegistryScope,
                          operation: RuntimeModelRegistryOperation, name: QualifiedName | None = None) -> None:
        if not _tuple(definitions, RuntimeModelDefinition) or any(type(d.key) is not RuntimeModelRegistryKey or d.key.scope != scope or name is not None and d.qualified_name != name for d in definitions):
            RuntimeRegistryDiagnostics.reject(RuntimeArtifactLoadFailure.REGISTRY_INTEGRITY_FAILURE,
                'Internal inspection index contains a definition outside its requested key/scope.', scope=scope, operation=operation)
        keys = tuple(d.key for d in definitions)
        if len(set(keys)) != len(keys) or tuple(sorted(keys, key=_registry_key_order)) != keys:
            RuntimeRegistryDiagnostics.reject(RuntimeArtifactLoadFailure.REGISTRY_INTEGRITY_FAILURE,
                'Internal inspection index contains duplicate or unordered exact keys.', scope=scope, operation=operation)

    def _scope(self, scope: RuntimeModelRegistryScope, operation: RuntimeModelRegistryOperation) -> None:
        if type(scope) is not RuntimeModelRegistryScope or scope not in self._binding.scopes:
            RuntimeRegistryDiagnostics.reject(RuntimeArtifactLoadFailure.REGISTRY_INVALID_SCOPE,
                'Requested registry scope is not explicitly declared by this instance.',
                scope=scope if type(scope) is RuntimeModelRegistryScope else None, operation=operation)

    def _authorize(self, scope: RuntimeModelRegistryScope, operation: RuntimeModelRegistryOperation,
                   *, identities: tuple[ElementVersionRef, ...] = (), name: QualifiedName | None = None,
                   reference: ElementRef | None = None, loaded: RuntimeArtifactLoadResult | None = None) -> None:
        self._scope(scope, operation)
        invocation = RuntimeModelRegistryAuthorizationRequest(self._binding, scope, operation,
            identities, name, reference, loaded)
        authority = self._authorizer.authorize(invocation)
        if type(authority) is not RuntimeModelRegistryAuthority or authority.request is not invocation:
            RuntimeRegistryDiagnostics.reject(RuntimeArtifactLoadFailure.REGISTRY_AUTHORIZATION_MISMATCH,
                'Trusted decision must bind this exact registry instance, operation, scope, selector and loaded batch.',
                scope=scope, operation=operation, stage=RuntimeArtifactLoadStage.REGISTRY_AUTHORIZATION)

    def _prepare(self, request: RuntimeModelRegistrationRequest, policy: RuntimeModelRegistryPolicy,
                 diagnostics: list[RuntimeArtifactLoadDiagnostic]) -> tuple[RuntimeModelDefinition, ...]:
        reject = RuntimeRegistryDiagnostics.reject
        loaded_result = request.load_result
        loaded = loaded_result.loaded_set
        if loaded_result.status is not RuntimeArtifactLoadStatus.SUCCEEDED:
            reject(RuntimeArtifactLoadFailure.REGISTRY_LOAD_NOT_SUCCESSFUL,
                'Registration requires an actual successful RUN-01 result, not a tuple or failed/incomplete output.',
                scope=request.scope, operation=RuntimeModelRegistryOperation.REGISTER,
                incomplete=loaded_result.status is RuntimeArtifactLoadStatus.INCOMPLETE)
        if type(loaded) is not LoadedRuntimeArtifactSet:
            reject(RuntimeArtifactLoadFailure.REGISTRY_LOAD_ASSOCIATION_MISMATCH, 'Successful load must retain its actual complete loaded set.', scope=request.scope)
        if loaded.context.semantic_context != request.scope.semantic_context:
            reject(RuntimeArtifactLoadFailure.REGISTRY_CONTEXT_MISMATCH, 'Loaded context differs from destination registry scope.', scope=request.scope)
        if loaded.context.runtime_target != request.scope.runtime_target:
            reject(RuntimeArtifactLoadFailure.REGISTRY_TARGET_MISMATCH, 'Loaded target differs from destination registry scope.', scope=request.scope)
        # Recheck existing immutable value/evidence contracts; never read/decode/recompile.
        RuntimeArtifactLoadResult(loaded_result.status, loaded, loaded_result.diagnostics)
        LoadedRuntimeArtifactSet(loaded.binding, loaded.context, loaded.authorization, loaded.artifacts, loaded.effective_policy)
        if len(loaded.artifacts) > loaded.effective_policy.maximum_artifact_count:
            reject(RuntimeArtifactLoadFailure.REGISTRY_RESOURCE_LIMIT_EXCEEDED, 'Loaded artifact count exceeds original verified bounds.', scope=request.scope)
        entries: list[RuntimeModelDefinition] = []
        for artifact in loaded.artifacts:
            try:
                LoadedRuntimeArtifact(artifact.descriptor, artifact.context, artifact.representation,
                    artifact.source_evidence, artifact.decoder_registration, artifact.limits)
            except RuntimeArtifactLoadError as error:
                diagnostic = RuntimeRegistryDiagnostics.create(RuntimeArtifactLoadFailure.REGISTRY_MUTABLE_DEFINITION,
                    'Loaded representation no longer meets its approved immutable RUN-01 invariants.',
                    scope=request.scope, artifact=artifact, stage=RuntimeArtifactLoadStage.REGISTRY_EXTRACTION)
                raise RuntimeArtifactLoadError((*error.diagnostics, diagnostic)) from error
            support = self._catalog.select(artifact, request.scope)
            remaining = policy.maximum_definitions_per_registration - len(entries)
            # Zero is intentionally allowed: an explicitly non-registrable artifact may return ().
            extracted = support.extractor.extract(artifact, remaining)
            if type(extracted) is not RuntimeModelDefinitionExtractionResult:
                reject(RuntimeArtifactLoadFailure.REGISTRY_EXTRACTION_FAILED, 'Approved extractor returned an invalid result contract.', scope=request.scope, artifact=artifact, stage=RuntimeArtifactLoadStage.REGISTRY_EXTRACTION)
            for diagnostic in extracted.diagnostics:
                if diagnostic.registry_scope not in (None, request.scope) or diagnostic.semantic_context not in (None, request.scope.semantic_context) or diagnostic.runtime_target not in (None, request.scope.runtime_target) or diagnostic.artifact_key not in (None, artifact.key) or diagnostic.artifact_kind not in (None, artifact.descriptor.kind) or diagnostic.manifest_identity not in (None, loaded.binding.manifest_identity) or diagnostic.registry_operation not in (None, RuntimeModelRegistryOperation.REGISTER) or diagnostic.semantic_origins and diagnostic.semantic_origins != artifact.semantic_origins:
                    reject(RuntimeArtifactLoadFailure.REGISTRY_EXTRACTION_FAILED, 'Extractor diagnostic association contradicts the current loaded scope/artifact.', scope=request.scope, artifact=artifact, stage=RuntimeArtifactLoadStage.REGISTRY_EXTRACTION)
                diagnostics.append(replace(diagnostic, registry_scope=request.scope,
                    semantic_context=request.scope.semantic_context, runtime_target=request.scope.runtime_target,
                    artifact_key=artifact.key, artifact_kind=artifact.descriptor.kind,
                    manifest_identity=loaded.binding.manifest_identity, semantic_origins=artifact.semantic_origins,
                    registry_operation=RuntimeModelRegistryOperation.REGISTER))
            if extracted.status is not RuntimeArtifactLoadStatus.SUCCEEDED:
                raise RuntimeArtifactLoadError((RuntimeRegistryDiagnostics.create(RuntimeArtifactLoadFailure.REGISTRY_EXTRACTION_FAILED,
                    'A mandatory artifact definition extraction did not succeed.', scope=request.scope, artifact=artifact,
                    stage=RuntimeArtifactLoadStage.REGISTRY_EXTRACTION, incomplete=extracted.status is RuntimeArtifactLoadStatus.INCOMPLETE),), extracted.status)
            if len(extracted.definitions) > remaining:
                reject(RuntimeArtifactLoadFailure.REGISTRY_RESOURCE_LIMIT_EXCEEDED, 'Extracted definition batch exceeds effective limits; no truncation.', scope=request.scope, artifact=artifact)
            if not extracted.definitions and not support.allows_no_definitions:
                reject(RuntimeArtifactLoadFailure.REGISTRY_NO_DEFINITIONS, 'Artifact contract requires registrable definitions but exposes none.', scope=request.scope, artifact=artifact, incomplete=True)
            if any(type(node) not in support.definition_types for node in extracted.definitions):
                reject(RuntimeArtifactLoadFailure.REGISTRY_UNSUPPORTED_DEFINITION, 'Extractor returned an unapproved concrete definition representation.', scope=request.scope, artifact=artifact, incomplete=True)
            if not _registry_node_membership(artifact, extracted.definitions):
                reject(RuntimeArtifactLoadFailure.REGISTRY_LOAD_ASSOCIATION_MISMATCH, 'Extracted nodes are not part of the original decoded artifact; copied/new nodes cannot substitute.', scope=request.scope, artifact=artifact)
            for node in extracted.definitions:
                if not _registry_exact(node.identity):
                    reject(RuntimeArtifactLoadFailure.REGISTRY_INVALID_IDENTITY, 'Definition requires its actual encoded exact semantic identity.', scope=request.scope, artifact=artifact)
                if node.qualified_name is not None and (type(node.qualified_name) is not QualifiedName or type(node.qualified_name.namespace) is not Namespace):
                    reject(RuntimeArtifactLoadFailure.REGISTRY_INVALID_IDENTITY, 'Optional definition name must be an actual Kernel QualifiedName.', scope=request.scope, identity=node.identity, artifact=artifact)
                if type(node.definition_kind) is not RuntimeModelDefinitionKind or node.definition_kind not in support.supported_kinds:
                    reject(RuntimeArtifactLoadFailure.REGISTRY_UNSUPPORTED_DEFINITION, 'Encoded definition kind is outside trusted extraction approval.', scope=request.scope, identity=node.identity, artifact=artifact, incomplete=True)
                entries.append(RuntimeModelDefinition(RuntimeModelRegistryKey(request.scope, node.identity), node.qualified_name,
                    node.definition_kind, node, loaded_result, artifact, support))
        ordered = tuple(sorted(entries, key=lambda d: _registry_key_order(d.key)))
        seen: set[RuntimeModelRegistryKey] = set()
        conflicts = []
        for definition in ordered:
            if definition.key in seen:
                conflicts.append(RuntimeRegistryDiagnostics.create(RuntimeArtifactLoadFailure.REGISTRY_DUPLICATE_BATCH_IDENTITY,
                    'Duplicate exact definition identity within the batch is never merged or exempted by equality.',
                    scope=request.scope, identity=definition.identity, kind=definition.definition_kind,
                    artifact=definition.loaded_artifact, operation=RuntimeModelRegistryOperation.REGISTER))
            seen.add(definition.key)
        if conflicts:
            raise RuntimeArtifactLoadError(tuple(conflicts))
        if not ordered and policy.empty_registration is RuntimeModelEmptyRegistrationPolicy.REJECT_EMPTY:
            reject(RuntimeArtifactLoadFailure.REGISTRY_NO_DEFINITIONS, 'No individually registrable definitions; empty registration is not approved by policy.', scope=request.scope, incomplete=True)
        return ordered

    def register(self, request: RuntimeModelRegistrationRequest) -> RuntimeModelRegistrationResult:
        diagnostics: list[RuntimeArtifactLoadDiagnostic] = []
        scope = request.scope if type(request) is RuntimeModelRegistrationRequest else None
        try:
            if type(request) is not RuntimeModelRegistrationRequest:
                RuntimeRegistryDiagnostics.reject(RuntimeArtifactLoadFailure.REGISTRY_INVALID_REQUEST, 'Registry requires an actual typed registration request.', operation=RuntimeModelRegistryOperation.REGISTER)
            self._scope(request.scope, RuntimeModelRegistryOperation.REGISTER)
            policy = request.policy.bounded_by(self._policy)
            proposed = self._prepare(request, policy, diagnostics)
            identities = tuple(d.identity for d in proposed)
            # Extraction is pure and bounded; authority checks exact extracted membership before mutation.
            self._authorize(request.scope, RuntimeModelRegistryOperation.REGISTER, identities=identities, loaded=request.load_result)
            with self._lock:
                old = self._current_state()
                conflicts = tuple(RuntimeRegistryDiagnostics.create(RuntimeArtifactLoadFailure.REGISTRY_DEFINITION_CONFLICT,
                    'Exact scoped identity is already registered; no overwrite or guessed idempotent replay.',
                    scope=request.scope, identity=d.identity, kind=d.definition_kind, artifact=d.loaded_artifact,
                    operation=RuntimeModelRegistryOperation.REGISTER, stage=RuntimeArtifactLoadStage.REGISTRY_COMMIT)
                    for d in proposed if d.key in old.exact)
                if conflicts:
                    raise RuntimeArtifactLoadError(conflicts)
                if len(old.definitions) + len(proposed) > policy.maximum_total_definitions or len(old.by_scope.get(request.scope, ())) + len(proposed) > policy.maximum_definitions_per_scope:
                    RuntimeRegistryDiagnostics.reject(RuntimeArtifactLoadFailure.REGISTRY_RESOURCE_LIMIT_EXCEEDED,
                        'Atomic registration would exceed trusted total or scope capacity.', scope=request.scope,
                        operation=RuntimeModelRegistryOperation.REGISTER, stage=RuntimeArtifactLoadStage.REGISTRY_COMMIT)
                # Construct state and result fully before the single publication assignment.
                new_state = _registry_state((*old.definitions, *proposed)) if proposed else old
                result = RuntimeModelRegistrationResult(RuntimeArtifactLoadStatus.SUCCEEDED, request.scope,
                    identities, request.load_result, tuple(diagnostics))
                self._state = new_state
                return result
        except RuntimeArtifactLoadError as error:
            associated = tuple(replace(d, registry_operation=RuntimeModelRegistryOperation.REGISTER)
                if d.code.name.startswith('REGISTRY_') and d.registry_operation is None else d for d in error.diagnostics)
            return RuntimeModelRegistrationResult(error.status, scope=scope, diagnostics=(*diagnostics, *associated))

    def lookup(self, request: RuntimeModelLookupRequest) -> RuntimeModelLookupResult:
        try:
            if type(request) is not RuntimeModelLookupRequest:
                RuntimeRegistryDiagnostics.reject(RuntimeArtifactLoadFailure.REGISTRY_INVALID_REQUEST, 'Exact lookup requires an actual typed request.', operation=RuntimeModelRegistryOperation.LOOKUP)
            exact = type(request.reference) is ElementVersionRef
            self._authorize(request.scope, RuntimeModelRegistryOperation.LOOKUP,
                identities=(request.reference,) if exact else (), reference=None if exact else request.reference)
            if not exact:
                diagnostic = RuntimeRegistryDiagnostics.create(RuntimeArtifactLoadFailure.REGISTRY_VERSION_REQUIRED,
                    'ElementRef does not select one exact version; use authorized version enumeration and explicit selection.',
                    scope=request.scope, operation=RuntimeModelRegistryOperation.LOOKUP,
                    stage=RuntimeArtifactLoadStage.REGISTRY_LOOKUP, routine=True)
                return RuntimeModelLookupResult(RuntimeModelLookupStatus.VERSION_REQUIRED, diagnostics=(diagnostic,))
            with self._lock:
                key = RuntimeModelRegistryKey(request.scope, request.reference)
                index = self._current_state().exact
                present = key in index
                definition = index.get(key)
            if present and (type(definition) is not RuntimeModelDefinition or definition.key != key):
                RuntimeRegistryDiagnostics.reject(RuntimeArtifactLoadFailure.REGISTRY_INTEGRITY_FAILURE,
                    'Internal exact index contains a mismatched definition key.', scope=request.scope,
                    identity=request.reference, operation=RuntimeModelRegistryOperation.LOOKUP,
                    stage=RuntimeArtifactLoadStage.REGISTRY_LOOKUP)
            if definition is None:
                diagnostic = RuntimeRegistryDiagnostics.create(RuntimeArtifactLoadFailure.REGISTRY_NOT_FOUND,
                    'Exact scoped version is not registered; no semantic validity judgment or fallback.',
                    scope=request.scope, identity=request.reference, operation=RuntimeModelRegistryOperation.LOOKUP,
                    stage=RuntimeArtifactLoadStage.REGISTRY_LOOKUP, routine=True)
                return RuntimeModelLookupResult(RuntimeModelLookupStatus.NOT_FOUND, diagnostics=(diagnostic,))
            return RuntimeModelLookupResult(RuntimeModelLookupStatus.FOUND, (definition,))
        except RuntimeArtifactLoadError as error:
            invalid = any(d.code is RuntimeArtifactLoadFailure.REGISTRY_INVALID_REQUEST for d in error.diagnostics)
            status = RuntimeModelLookupStatus.INVALID_REQUEST if invalid else RuntimeModelLookupStatus.INCOMPLETE if error.status is RuntimeArtifactLoadStatus.INCOMPLETE else RuntimeModelLookupStatus.FAILED
            return RuntimeModelLookupResult(status, diagnostics=error.diagnostics)

    def contains(self, request: RuntimeModelLookupRequest) -> RuntimeModelMembershipResult:
        result = self.lookup(request)
        return RuntimeModelMembershipResult(result.status,
            True if result.status is RuntimeModelLookupStatus.FOUND else False if result.status is RuntimeModelLookupStatus.NOT_FOUND else None, result.diagnostics)

    def inspect_name(self, request: RuntimeModelNameInspectionRequest) -> RuntimeModelLookupResult:
        try:
            if type(request) is not RuntimeModelNameInspectionRequest:
                RuntimeRegistryDiagnostics.reject(RuntimeArtifactLoadFailure.REGISTRY_INVALID_REQUEST, 'Name inspection requires a typed scoped QualifiedName request.', operation=RuntimeModelRegistryOperation.INSPECT_NAME)
            self._authorize(request.scope, RuntimeModelRegistryOperation.INSPECT_NAME, name=request.qualified_name)
            with self._lock:
                candidates = self._current_state().by_name.get((request.scope, request.qualified_name), ())
            if type(candidates) is not tuple:
                RuntimeRegistryDiagnostics.reject(RuntimeArtifactLoadFailure.REGISTRY_INTEGRITY_FAILURE, 'Internal name index is not an immutable candidate tuple.', scope=request.scope, name=request.qualified_name, operation=RuntimeModelRegistryOperation.INSPECT_NAME)
            if len(candidates) > self._policy.maximum_snapshot_entries:
                RuntimeRegistryDiagnostics.reject(RuntimeArtifactLoadFailure.REGISTRY_SNAPSHOT_UNAVAILABLE, 'Name candidate inventory exceeds bounded inspection capacity; no truncation.', scope=request.scope, name=request.qualified_name, operation=RuntimeModelRegistryOperation.INSPECT_NAME, incomplete=True)
            self._read_definitions(candidates, request.scope, RuntimeModelRegistryOperation.INSPECT_NAME, request.qualified_name)
            if not candidates:
                diagnostic = RuntimeRegistryDiagnostics.create(RuntimeArtifactLoadFailure.REGISTRY_NOT_FOUND, 'No registered exact definition has this scoped name.', scope=request.scope, name=request.qualified_name, operation=RuntimeModelRegistryOperation.INSPECT_NAME, stage=RuntimeArtifactLoadStage.REGISTRY_LOOKUP, routine=True)
                return RuntimeModelLookupResult(RuntimeModelLookupStatus.NOT_FOUND, diagnostics=(diagnostic,))
            if len(candidates) == 1:
                return RuntimeModelLookupResult(RuntimeModelLookupStatus.FOUND, candidates)
            diagnostic = RuntimeRegistryDiagnostics.create(RuntimeArtifactLoadFailure.REGISTRY_AMBIGUOUS_NAME, 'Name matches multiple exact versions/identities; none selected implicitly.', scope=request.scope, name=request.qualified_name, operation=RuntimeModelRegistryOperation.INSPECT_NAME, stage=RuntimeArtifactLoadStage.REGISTRY_LOOKUP, routine=True)
            return RuntimeModelLookupResult(RuntimeModelLookupStatus.AMBIGUOUS, candidates, (diagnostic,))
        except RuntimeArtifactLoadError as error:
            status = RuntimeModelLookupStatus.INVALID_REQUEST if any(d.code is RuntimeArtifactLoadFailure.REGISTRY_INVALID_REQUEST for d in error.diagnostics) else RuntimeModelLookupStatus.INCOMPLETE if error.status is RuntimeArtifactLoadStatus.INCOMPLETE else RuntimeModelLookupStatus.FAILED
            return RuntimeModelLookupResult(status, diagnostics=error.diagnostics)

    def versions(self, request: RuntimeModelVersionInspectionRequest) -> RuntimeModelVersionInspectionResult:
        try:
            if type(request) is not RuntimeModelVersionInspectionRequest:
                RuntimeRegistryDiagnostics.reject(RuntimeArtifactLoadFailure.REGISTRY_INVALID_REQUEST, 'Version enumeration requires a typed scoped ElementRef request.', operation=RuntimeModelRegistryOperation.ENUMERATE_VERSIONS)
            self._authorize(request.scope, RuntimeModelRegistryOperation.ENUMERATE_VERSIONS, reference=request.reference)
            with self._lock:
                references = self._current_state().by_identity.get((request.scope, request.reference.element_id), ())
            if type(references) is not tuple:
                RuntimeRegistryDiagnostics.reject(RuntimeArtifactLoadFailure.REGISTRY_INTEGRITY_FAILURE, 'Internal version index is not an immutable reference tuple.', scope=request.scope, operation=RuntimeModelRegistryOperation.ENUMERATE_VERSIONS)
            if len(references) > self._policy.maximum_snapshot_entries:
                RuntimeRegistryDiagnostics.reject(RuntimeArtifactLoadFailure.REGISTRY_SNAPSHOT_UNAVAILABLE, 'Version inventory exceeds inspection capacity; no truncated resolution.', scope=request.scope, operation=RuntimeModelRegistryOperation.ENUMERATE_VERSIONS, incomplete=True)
            if not _tuple(references, ElementVersionRef) or any(not _registry_exact(r) or r.element_id != request.reference.element_id for r in references) or len(set(references)) != len(references) or tuple(sorted(references, key=_registry_identity_order)) != references:
                RuntimeRegistryDiagnostics.reject(RuntimeArtifactLoadFailure.REGISTRY_INTEGRITY_FAILURE, 'Internal version index violates exact identity/order invariants.', scope=request.scope, operation=RuntimeModelRegistryOperation.ENUMERATE_VERSIONS)
            if not references:
                diagnostic = RuntimeRegistryDiagnostics.create(RuntimeArtifactLoadFailure.REGISTRY_NOT_FOUND, 'No exact versions registered for the scoped identity.', scope=request.scope, operation=RuntimeModelRegistryOperation.ENUMERATE_VERSIONS, stage=RuntimeArtifactLoadStage.REGISTRY_LOOKUP, routine=True)
                return RuntimeModelVersionInspectionResult(RuntimeModelLookupStatus.NOT_FOUND, diagnostics=(diagnostic,))
            return RuntimeModelVersionInspectionResult(RuntimeModelLookupStatus.FOUND, references)
        except RuntimeArtifactLoadError as error:
            status = RuntimeModelLookupStatus.INVALID_REQUEST if any(d.code is RuntimeArtifactLoadFailure.REGISTRY_INVALID_REQUEST for d in error.diagnostics) else RuntimeModelLookupStatus.INCOMPLETE if error.status is RuntimeArtifactLoadStatus.INCOMPLETE else RuntimeModelLookupStatus.FAILED
            return RuntimeModelVersionInspectionResult(status, diagnostics=error.diagnostics)

    def snapshot(self, scope: RuntimeModelRegistryScope) -> RuntimeModelRegistrySnapshotResult:
        try:
            self._authorize(scope, RuntimeModelRegistryOperation.SNAPSHOT)
            with self._lock:
                definitions = self._current_state().by_scope.get(scope, ())
            if type(definitions) is not tuple:
                RuntimeRegistryDiagnostics.reject(RuntimeArtifactLoadFailure.REGISTRY_INTEGRITY_FAILURE, 'Internal scope index is not an immutable definition tuple.', scope=scope, operation=RuntimeModelRegistryOperation.SNAPSHOT)
            if len(definitions) > self._policy.maximum_snapshot_entries:
                RuntimeRegistryDiagnostics.reject(RuntimeArtifactLoadFailure.REGISTRY_SNAPSHOT_UNAVAILABLE,
                    'Complete scoped snapshot exceeds inspection capacity; no partial snapshot.',
                    scope=scope, operation=RuntimeModelRegistryOperation.SNAPSHOT,
                    stage=RuntimeArtifactLoadStage.REGISTRY_SNAPSHOT, incomplete=True)
            self._read_definitions(definitions, scope, RuntimeModelRegistryOperation.SNAPSHOT)
            return RuntimeModelRegistrySnapshotResult(RuntimeArtifactLoadStatus.SUCCEEDED,
                RuntimeModelRegistrySnapshot(scope, definitions))
        except RuntimeArtifactLoadError as error:
            return RuntimeModelRegistrySnapshotResult(error.status, diagnostics=error.diagnostics)


# The new kind is an immutable coordinate, not automatic definition-kind approval.
_IMMUTABLE_CONTRACTS += (RuntimeModelDefinitionKind,)

__all__ += ['RuntimeModelRegistryScope', 'RuntimeModelDefinitionKind', 'RuntimeModelRegistryKey',
    'RuntimeModelEmptyRegistrationPolicy', 'RuntimeModelConflictPolicy', 'RuntimeModelRegistryPolicy',
    'RuntimeModelRegistryOperation', 'RuntimeModelRegistryBinding', 'RuntimeModelRegistrationRequest',
    'RuntimeModelLookupRequest', 'RuntimeModelNameInspectionRequest', 'RuntimeModelVersionInspectionRequest',
    'RuntimeModelRegistryAuthorizationRequest', 'RuntimeModelRegistryAuthority', 'RuntimeModelRegistryAuthorizer',
    'RuntimeRegistryDiagnostics', 'UnavailableRuntimeModelRegistryAuthorizer', 'RuntimeModelDefinitionRepresentation',
    'RuntimeModelDefinitionExtractionResult', 'RuntimeModelDefinitionExtractor', 'RuntimeModelDefinitionExtractionSupport',
    'RuntimeModelDefinitionExtractionCatalog', 'RuntimeModelDefinition', 'RuntimeModelRegistrySnapshot',
    'RuntimeModelRegistrationResult', 'RuntimeModelLookupStatus', 'RuntimeModelLookupResult',
    'RuntimeModelMembershipResult', 'RuntimeModelVersionInspectionResult', 'RuntimeModelRegistrySnapshotResult',
    'RuntimeModelRegistry', 'LocalRuntimeModelRegistry']


# RUN-05: execution metadata is neither authority nor business execution.
@dataclass(frozen=True, slots=True)
class RuntimeInvocationId:
    value: UUID

    def __post_init__(self) -> None:
        if type(self.value) is not UUID or self.value.version != 4:
            raise ValueError('Invocation requires an explicitly supplied UUID4, distinct from semantic identities.')


@dataclass(frozen=True, slots=True)
class ExecutionCorrelationId:
    value: UUID

    def __post_init__(self) -> None:
        if type(self.value) is not UUID or self.value.version != 4:
            raise ValueError('Correlation requires an explicitly supplied UUID4; no clock/random allocation here.')


@dataclass(frozen=True, slots=True)
class ExecutionCausationRef:
    invocation_identity: RuntimeInvocationId

    def __post_init__(self) -> None:
        if type(self.invocation_identity) is not RuntimeInvocationId:
            raise TypeError('Causation references an immediate invocation, never correlation or a full parent.')


@dataclass(frozen=True, slots=True)
class ExecutionOperationRef:
    """Non-secret approved operation token; carries no executable handler or policy."""
    value: str

    def __post_init__(self) -> None:
        RuntimeCapabilityId(self.value)


def _execution_deadline(value: object) -> bool:
    # Closed fixed-offset timezone avoids executing arbitrary tzinfo callbacks.
    return type(value) is datetime and type(value.tzinfo) is timezone


@dataclass(frozen=True, slots=True)
class ExecutionConstraints:
    """Descriptions, not consumed-budget accounting or executor guarantees.

    remaining_depth bounds a later child path; nested count is a per-invocation
    ceiling, not a shared sibling ledger. None deadline means NOT SPECIFIED.
    Every requested capability requires a real enforcer; none exists in v0.
    """
    remaining_depth: int = 16
    maximum_nested_invocations: int = 64
    deadline: datetime | None = None
    required_capabilities: tuple[RuntimeCapabilityId, ...] = ()

    def __post_init__(self) -> None:
        if any(type(v) is not int or not 0 <= v <= 2 ** 31 - 1 for v in (self.remaining_depth, self.maximum_nested_invocations)):
            raise ValueError('Execution limits are bounded nonnegative actual integers, not Boolean/unlimited budgets.')
        if self.deadline is not None and not _execution_deadline(self.deadline):
            raise TypeError('Deadline is an explicit absolute fixed-offset aware datetime, not relative timeout.')
        if not _tuple(self.required_capabilities, RuntimeCapabilityId) or len(self.required_capabilities) > 32 or len(set(self.required_capabilities)) != len(self.required_capabilities):
            raise TypeError('Required enforcers use a bounded distinct immutable existing capability inventory.')
        if tuple(sorted(self.required_capabilities)) != self.required_capabilities:
            raise ValueError('Required execution capabilities retain deterministic token order.')

    def bounded_by(self, parent: 'ExecutionConstraints', *, child: bool = False) -> bool:
        if type(parent) is not ExecutionConstraints or type(child) is not bool:
            raise TypeError('Constraint comparison uses actual immutable descriptions.')
        return (self.remaining_depth <= parent.remaining_depth - int(child)
            and self.maximum_nested_invocations <= parent.maximum_nested_invocations
            and (parent.deadline is None or self.deadline is not None and self.deadline <= parent.deadline)
            and set(parent.required_capabilities) <= set(self.required_capabilities))


class ExecutionDeadlineStatus(Enum):
    NOT_SPECIFIED = 'not-specified'
    BEFORE_DEADLINE = 'before-deadline'
    REACHED = 'reached'


@dataclass(frozen=True, slots=True)
class ExecutionModelSelection:
    references: tuple[ElementVersionRef | ElementRef, ...]
    snapshot: RuntimeModelRegistrySnapshot | None = field(default=None, repr=False)

    def __post_init__(self) -> None:
        if type(self.references) is not tuple or not self.references or len(self.references) > 128 or any(type(r) not in (ElementVersionRef, ElementRef) for r in self.references):
            raise TypeError('Selection requires a bounded explicit nonempty tuple of actual semantic references.')
        if self.snapshot is not None and type(self.snapshot) is not RuntimeModelRegistrySnapshot:
            raise TypeError('Model association uses the actual immutable RUN-02 snapshot, never a live registry.')


@dataclass(frozen=True, slots=True)
class ExecutionContextCreateRequest:
    invocation_identity: RuntimeInvocationId
    semantic_context: SemanticContextRef
    registry_scope: RuntimeModelRegistryScope
    operation: ExecutionOperationRef
    model_selection: ExecutionModelSelection
    correlation_identity: ExecutionCorrelationId
    constraints: ExecutionConstraints
    principal: 'ExecutionPrincipalRef | None' = field(default=None, repr=False)
    authorization: 'ExecutionAuthorizationInput | None' = field(default=None, repr=False)
    causation: ExecutionCausationRef | None = None
    requires_active_deployment: bool = False

    def __post_init__(self) -> None:
        for value, expected in ((self.invocation_identity, RuntimeInvocationId), (self.semantic_context, SemanticContextRef), (self.registry_scope, RuntimeModelRegistryScope), (self.operation, ExecutionOperationRef), (self.model_selection, ExecutionModelSelection), (self.correlation_identity, ExecutionCorrelationId), (self.constraints, ExecutionConstraints)):
            if type(value) is not expected:
                raise TypeError('Execution creation has mandatory explicit typed coordinates and limits.')
        if self.causation is not None and type(self.causation) is not ExecutionCausationRef or type(self.requires_active_deployment) is not bool:
            raise TypeError('Causation and active-deployment requirement are explicit typed associations.')
        if self.principal is not None and type(self.principal) is not ExecutionPrincipalRef or self.authorization is not None and type(self.authorization) is not ExecutionAuthorizationInput:
            raise TypeError('Input evidence is an approved immutable reference association, never raw client metadata.')
        # Structural association admission does not authenticate or authorize.
        # Only the configured owner verifier establishes trust for this invocation.


@dataclass(frozen=True, slots=True)
class ExecutionTrustInvocation:
    request: ExecutionContextCreateRequest = field(repr=False)

    def __post_init__(self) -> None:
        if type(self.request) is not ExecutionContextCreateRequest:
            raise TypeError('Trust verification is bound to one explicit internal invocation.')


class ExecutionTrustDecision(Enum):
    VERIFIED = 'verified'
    DENIED = 'denied'
    UNAVAILABLE = 'unavailable'


@dataclass(frozen=True, slots=True)
class ExecutionTrustVerification:
    """Trusted boundary projection of EXISTING evidence, not a policy decision engine.

    The owner must verify authentication, audience/lifetime/revocation and actual
    original decision dimensions offline before returning VERIFIED. No genuine
    principal/decision implementation or category is approved in this revision.
    """
    invocation: ExecutionTrustInvocation = field(repr=False)
    decision: ExecutionTrustDecision
    principal: 'ExecutionPrincipalRef | None' = field(default=None, repr=False)
    authorization: 'ExecutionAuthorizationInput | None' = field(default=None, repr=False)
    approved_scope: RuntimeModelRegistryScope | None = None
    approved_operation: ExecutionOperationRef | None = None
    approved_models: tuple[ElementVersionRef, ...] = ()
    approved_constraints: ExecutionConstraints | None = None

    def __post_init__(self) -> None:
        if type(self.invocation) is not ExecutionTrustInvocation or type(self.decision) is not ExecutionTrustDecision or not _tuple(self.approved_models, ElementVersionRef) or len(self.approved_models) > 128 or any(not _registry_exact(r) for r in self.approved_models):
            raise TypeError('Trust projection retains an actual invocation and bounded exact model coordinates.')
        if len(set(self.approved_models)) != len(self.approved_models) or tuple(sorted(self.approved_models, key=_registry_identity_order)) != self.approved_models:
            raise ValueError('Approved exact model inventory must be distinct and deterministically ordered.')
        if self.approved_scope is not None and type(self.approved_scope) is not RuntimeModelRegistryScope or self.approved_operation is not None and type(self.approved_operation) is not ExecutionOperationRef or self.approved_constraints is not None and type(self.approved_constraints) is not ExecutionConstraints:
            raise TypeError('Trust projection dimensions use actual immutable typed contracts.')
        if self.principal is not None and type(self.principal) is not ExecutionPrincipalRef or self.authorization is not None and type(self.authorization) is not ExecutionAuthorizationInput:
            raise TypeError('Verification exposes only actual immutable owner-approved reference associations.')
        if self.decision is ExecutionTrustDecision.VERIFIED and (self.principal is None or self.authorization is None or self.approved_scope is None or self.approved_operation is None or not self.approved_models or self.approved_constraints is None):
            raise ValueError('VERIFIED requires actual principal/decision references and all mandatory scope dimensions.')
        if self.decision is not ExecutionTrustDecision.VERIFIED and (self.principal is not None or self.authorization is not None or self.approved_scope is not None or self.approved_operation is not None or self.approved_models or self.approved_constraints is not None):
            raise ValueError('Denied/unavailable verification exposes no partial trusted associations.')


class ExecutionTrustVerifier(Protocol):
    def verify(self, invocation: ExecutionTrustInvocation) -> ExecutionTrustVerification:
        """Pure owner verification of existing authenticated evidence; no hidden policy/network execution."""
        ...


def _execution_frozen(t: object) -> bool:
    return isinstance(t, type) and is_dataclass(t) and t.__dataclass_params__.frozen and hasattr(t, '__slots__')


def _execution_reference_safe(value: object, approved: tuple[type, ...]) -> bool:
    """Narrow owner-approved reference graph; do not change RUN-01 admission.

    Owner approvals must expose references, never raw authentication material.
    Token syntax alone cannot identify secrets; credential exclusion is an
    explicit responsibility of the trusted existing authentication boundary.
    Closed bounded traversal precedes any verifier invocation. No attributes on
    arbitrary unapproved objects, arbitrary tzinfo, bytes, dict/list or Enum.
    """
    stack, count, units = [(value, 0, frozenset())], 0, 0
    while stack:
        node, depth, ancestors = stack.pop()
        count += 1
        if count > 1024 or depth > 16:
            return False
        t, children = type(node), ()
        if node is None or t in (bool, UUID):
            pass
        elif t is datetime:
            if not _execution_deadline(node):
                return False
        elif t is str:
            # References are bounded logical tokens, not credentials or payloads.
            if len(node) > 160 or re.fullmatch(r'[a-zA-Z0-9][a-zA-Z0-9_.:@-]*', node) is None:
                return False
            units += len(node)
        elif t is int:
            units += max(1, (node.bit_length() + 7) // 8)
        elif t is tuple:
            children = node
        elif t in approved:
            if not _execution_frozen(t) or hasattr(node, '__dict__'):
                return False
            children = tuple(getattr(node, f.name) for f in fields(t))
        else:
            return False
        if units > 4096 or count + len(stack) + len(children) > 1024:
            return False
        if children:
            if id(node) in ancestors:
                return False
            stack.extend((n, depth + 1, ancestors | {id(node)}) for n in reversed(children))
    return True


@dataclass(frozen=True, slots=True)
class ExecutionTrustSupport:
    principal_types: tuple[type, ...]
    authorization_types: tuple[type, ...]
    verifier: ExecutionTrustVerifier = field(repr=False)
    nested_reference_types: tuple[type, ...] = ()

    def __post_init__(self) -> None:
        combined = (*self.principal_types, *self.authorization_types, *self.nested_reference_types) if all(type(v) is tuple for v in (self.principal_types, self.authorization_types, self.nested_reference_types)) else ()
        if not self.principal_types or not self.authorization_types or not combined or len(combined) > 32 or len(set(combined)) != len(combined) or any(not _execution_frozen(t) for t in combined):
            raise TypeError('Only explicit distinct actual owner-approved immutable principal/decision reference classes qualify.')
        if not _execution_frozen(type(self.verifier)) or not _execution_reference_safe(self.verifier, (type(self.verifier), *self.nested_reference_types)) or not callable(getattr(type(self.verifier), 'verify', None)):
            raise TypeError('Execution verifier requires trusted immutable bounded configuration, not HTTP/session state.')

    @property
    def reference_types(self) -> tuple[type, ...]:
        return (*self.principal_types, *self.authorization_types, *self.nested_reference_types)


@dataclass(frozen=True, slots=True)
class ExecutionPrincipalRef:
    support: ExecutionTrustSupport = field(repr=False)
    reference: object = field(repr=False)

    def __post_init__(self) -> None:
        if type(self.support) is not ExecutionTrustSupport or type(self.reference) not in self.support.principal_types or not _execution_reference_safe(self.reference, self.support.reference_types):
            raise TypeError('Principal association retains an actual approved immutable non-secret identity reference.')


@dataclass(frozen=True, slots=True)
class ExecutionAuthorizationInput:
    """Structural immutable original decision reference, NOT verified authority."""
    support: ExecutionTrustSupport = field(repr=False)
    reference: object = field(repr=False)

    def __post_init__(self) -> None:
        if type(self.support) is not ExecutionTrustSupport or type(self.reference) not in self.support.authorization_types or not _execution_reference_safe(self.reference, self.support.reference_types):
            raise TypeError('Decision input retains only actual approved immutable evidence references, never Boolean authority.')


@dataclass(frozen=True, slots=True)
class ExecutionAuthorizationRef:
    support: ExecutionTrustSupport = field(repr=False)
    verification: ExecutionTrustVerification = field(repr=False)

    def __post_init__(self) -> None:
        if type(self.support) is not ExecutionTrustSupport or type(self.verification) is not ExecutionTrustVerification or self.verification.decision is not ExecutionTrustDecision.VERIFIED:
            raise TypeError('Authorization association needs actual owner verification, never caller Boolean authority.')
        proof = self.verification
        if proof.principal.support is not self.support or proof.authorization.support is not self.support or not _execution_reference_safe((proof.principal.reference, proof.authorization.reference), self.support.reference_types):
            raise TypeError('Trusted evidence carries only approved deeply immutable reference representations.')
        if proof.principal is not proof.invocation.request.principal or proof.authorization is not proof.invocation.request.authorization:
            raise ValueError('Trust projection must retain the original explicitly submitted reference associations.')


class ExecutionContextFailure(Enum):
    INVALID_REQUEST = 'RUN-401'
    INVALID_INVOCATION = 'RUN-402'
    INVALID_SEMANTIC_SCOPE = 'RUN-403'
    REGISTRY_SCOPE_MISMATCH = 'RUN-404'
    RUNTIME_TARGET_MISMATCH = 'RUN-405'
    VERSION_REQUIRED = 'RUN-406'
    MODEL_SELECTION_MISMATCH = 'RUN-407'
    PRINCIPAL_UNAVAILABLE = 'RUN-408'
    UNTRUSTED_PRINCIPAL = 'RUN-409'
    AUTHORIZATION_UNAVAILABLE = 'RUN-410'
    AUTHORIZATION_MISMATCH = 'RUN-411'
    INVALID_CORRELATION = 'RUN-412'
    INVALID_CAUSATION = 'RUN-413'
    INVALID_DEADLINE = 'RUN-414'
    UNSUPPORTED_CONSTRAINT = 'RUN-415'
    SCOPE_ESCALATION = 'RUN-416'
    DEADLINE_EXTENSION = 'RUN-417'
    PRINCIPAL_MISMATCH = 'RUN-418'
    PREREQUISITE_UNAVAILABLE = 'RUN-419'
    RESOURCE_LIMIT = 'RUN-420'
    DEPTH_EXHAUSTED = 'RUN-421'
    TRUST_DENIED = 'RUN-422'
    INVALID_PARENT = 'RUN-423'
    ACTIVATION_UNAVAILABLE = 'RUN-424'


@dataclass(frozen=True, slots=True)
class ExecutionContextDiagnostic:
    code: ExecutionContextFailure
    message: str
    severity: RuntimeLoadSeverity = RuntimeLoadSeverity.ERROR
    invocation_identity: RuntimeInvocationId | None = None
    semantic_context: SemanticContextRef | None = None
    registry_scope: RuntimeModelRegistryScope | None = None
    definition_identity: ElementVersionRef | None = None
    correlation_identity: ExecutionCorrelationId | None = None
    causation: ExecutionCausationRef | None = None

    def __post_init__(self) -> None:
        if type(self.code) is not ExecutionContextFailure or type(self.message) is not str or not self.message or type(self.severity) is not RuntimeLoadSeverity:
            raise TypeError('Context diagnostics use runtime codes and severity, no compiler phases.')
        for v, t in ((self.invocation_identity, RuntimeInvocationId), (self.semantic_context, SemanticContextRef), (self.registry_scope, RuntimeModelRegistryScope), (self.definition_identity, ElementVersionRef), (self.correlation_identity, ExecutionCorrelationId), (self.causation, ExecutionCausationRef)):
            if v is not None and type(v) is not t:
                raise TypeError('Context diagnostic coordinates must be actual typed immutable identities.')


@dataclass(frozen=True, slots=True)
class ExecutionContext:
    """Explicit propagation value. Possession is not permanent authority or execution."""
    invocation_identity: RuntimeInvocationId
    semantic_context: SemanticContextRef
    registry_scope: RuntimeModelRegistryScope
    operation: ExecutionOperationRef
    model_selection: ExecutionModelSelection
    principal: ExecutionPrincipalRef = field(repr=False)
    authorization: ExecutionAuthorizationRef = field(repr=False)
    correlation_identity: ExecutionCorrelationId
    constraints: ExecutionConstraints
    causation: ExecutionCausationRef | None = None

    def __post_init__(self) -> None:
        if type(self.principal) is not ExecutionPrincipalRef or type(self.authorization) is not ExecutionAuthorizationRef or self.principal.support is not self.authorization.support:
            raise TypeError('Execution context requires matching trusted principal and authorization associations.')
        proof = self.authorization.verification
        request = proof.invocation.request
        coordinates = (self.invocation_identity, self.semantic_context, self.registry_scope, self.operation, self.model_selection, self.correlation_identity, self.constraints, self.causation)
        expected = (request.invocation_identity, request.semantic_context, request.registry_scope, request.operation, request.model_selection, request.correlation_identity, request.constraints, request.causation)
        if any(type(v) is not type(e) for v, e in zip(coordinates, expected)) or coordinates != expected:
            raise ValueError('Context must preserve the complete verified immutable invocation coordinates.')
        if self.semantic_context != self.registry_scope.semantic_context or proof.approved_scope != self.registry_scope or proof.approved_operation != self.operation or self.principal is not proof.principal:
            raise ValueError('Context principal, operation and semantic/runtime scope must match original verification.')
        refs = self.model_selection.references
        snapshot = self.model_selection.snapshot
        if any(not _registry_exact(r) for r in refs) or len(set(refs)) != len(refs) or tuple(sorted(refs, key=_registry_identity_order)) != refs or any(r not in proof.approved_models for r in refs):
            raise ValueError('Context selection must retain distinct ordered explicitly approved exact definitions.')
        if snapshot is None or snapshot.scope != self.registry_scope or any(not any(d.identity == r for d in snapshot.definitions) for r in refs):
            raise ValueError('Context needs the actual coherent exact membership snapshot; no active deployment implied.')
        if not self.constraints.bounded_by(proof.approved_constraints) or self.constraints.required_capabilities or request.requires_active_deployment:
            raise ValueError('Context cannot claim unsupported mandatory execution/activation capability or widen approved bounds.')
        if self.causation is not None and self.causation.invocation_identity == self.invocation_identity:
            raise ValueError('Immediate causation cannot name the same invocation.')

    def deadline_status(self, now: datetime) -> ExecutionDeadlineStatus:
        """Explicit trusted current time only; no clock read, cancellation or execution."""
        if not _execution_deadline(now):
            raise TypeError('Deadline observation requires an explicitly supplied fixed-offset aware datetime.')
        if self.constraints.deadline is None:
            return ExecutionDeadlineStatus.NOT_SPECIFIED
        return ExecutionDeadlineStatus.REACHED if now >= self.constraints.deadline else ExecutionDeadlineStatus.BEFORE_DEADLINE


@dataclass(frozen=True, slots=True)
class ExecutionContextCreationResult:
    status: RuntimeArtifactLoadStatus
    context: ExecutionContext | None = field(default=None, repr=False)
    diagnostics: tuple[ExecutionContextDiagnostic, ...] = ()

    def __post_init__(self) -> None:
        if type(self.status) is not RuntimeArtifactLoadStatus or not _tuple(self.diagnostics, ExecutionContextDiagnostic):
            raise TypeError('Creation outcome reuses runtime statuses and immutable context diagnostics.')
        if self.status is RuntimeArtifactLoadStatus.SUCCEEDED:
            if type(self.context) is not ExecutionContext or any(d.severity is RuntimeLoadSeverity.ERROR for d in self.diagnostics):
                raise ValueError('Success needs a complete trusted context and no errors.')
        elif self.context is not None or not self.diagnostics:
            raise ValueError('Failed/incomplete context creation has diagnostics and no partial context.')


@dataclass(frozen=True, slots=True)
class ExecutionContextDerivationRequest:
    invocation_identity: RuntimeInvocationId
    model_selection: ExecutionModelSelection
    constraints: ExecutionConstraints
    authorization: 'ExecutionAuthorizationInput | None' = field(default=None, repr=False)

    def __post_init__(self) -> None:
        if type(self.invocation_identity) is not RuntimeInvocationId or type(self.model_selection) is not ExecutionModelSelection or type(self.constraints) is not ExecutionConstraints:
            raise TypeError('Derivation allows only explicit new invocation, model restriction, bounds and fresh authority reference.')
        if self.authorization is not None and type(self.authorization) is not ExecutionAuthorizationInput:
            raise TypeError('Child supplies only immutable existing decision evidence for fresh verification.')
        # No principal/target/operation/semantic/correlation override or delegation.


@dataclass(frozen=True, slots=True)
class ExecutionContextPolicy:
    maximum_selected_models: int = 128
    maximum_snapshot_definitions: int = 10000
    maximum_depth: int = 64
    maximum_nested_invocations: int = 4096

    def __post_init__(self) -> None:
        if any(type(getattr(self, f.name)) is not int or getattr(self, f.name) <= 0 for f in fields(self)) or self.maximum_selected_models > 128:
            raise ValueError('Trusted factory ceilings are positive integers; model inventory cannot exceed contract bound128.')


class _ExecutionContextRejected(Exception):
    def __init__(self, diagnostic: ExecutionContextDiagnostic, incomplete: bool):
        self.diagnostic, self.incomplete = diagnostic, incomplete


class ExecutionContextFactory:
    """Pure structural/trust association verification. No actual trust adapter exists."""
    __slots__ = ('_trust', '_policy')

    def __init__(self, *, trust_support: ExecutionTrustSupport | None = None, policy: ExecutionContextPolicy | None = None):
        if trust_support is not None and type(trust_support) is not ExecutionTrustSupport or policy is not None and type(policy) is not ExecutionContextPolicy:
            raise TypeError('Factory owner supplies explicit immutable trust integration and construction policy.')
        self._trust = trust_support
        self._policy = ExecutionContextPolicy() if policy is None else policy

    def _reject(self, code, message, request=None, *, incomplete=False, reference=None):
        actual = request if type(request) is ExecutionContextCreateRequest else None
        raise _ExecutionContextRejected(ExecutionContextDiagnostic(code, message,
            invocation_identity=actual.invocation_identity if actual is not None else None,
            semantic_context=actual.semantic_context if actual is not None else None,
            registry_scope=actual.registry_scope if actual is not None else None,
            definition_identity=reference,
            correlation_identity=actual.correlation_identity if actual is not None else None,
            causation=actual.causation if actual is not None else None), incomplete)

    def _verify(self, request: ExecutionContextCreateRequest) -> tuple[ExecutionPrincipalRef, ExecutionAuthorizationRef]:
        reject = self._reject
        if type(request) is not ExecutionContextCreateRequest:
            reject(ExecutionContextFailure.INVALID_REQUEST, 'Actual typed execution-context request is required.')
        if type(request.invocation_identity) is not RuntimeInvocationId or type(request.invocation_identity.value) is not UUID or request.invocation_identity.value.version != 4:
            reject(ExecutionContextFailure.INVALID_INVOCATION, 'Explicit independent invocation UUID4 is required.', request)
        if type(request.semantic_context) is not SemanticContextRef or type(request.semantic_context.context_id) is not SemanticElementId:
            reject(ExecutionContextFailure.INVALID_SEMANTIC_SCOPE, 'Actual explicit semantic context identity is required.', request)
        if request.semantic_context != request.registry_scope.semantic_context:
            reject(ExecutionContextFailure.REGISTRY_SCOPE_MISMATCH, 'Semantic context differs from the explicit registry scope.', request)
        if type(request.correlation_identity) is not ExecutionCorrelationId or type(request.correlation_identity.value) is not UUID or request.correlation_identity.value.version != 4:
            reject(ExecutionContextFailure.INVALID_CORRELATION, 'Explicit independent correlation UUID4 is required.', request)
        if request.causation is not None and request.causation.invocation_identity == request.invocation_identity:
            reject(ExecutionContextFailure.INVALID_CAUSATION, 'Causation cannot reference the current invocation.', request)
        refs, snapshot = request.model_selection.references, request.model_selection.snapshot
        if len(refs) > self._policy.maximum_selected_models:
            reject(ExecutionContextFailure.RESOURCE_LIMIT, 'Model selection exceeds the trusted construction ceiling.', request)
        if any(not _registry_exact(r) for r in refs):
            reject(ExecutionContextFailure.VERSION_REQUIRED, 'Every selected model requires an exact version, without latest fallback.', request)
        if len(set(refs)) != len(refs) or tuple(sorted(refs, key=_registry_identity_order)) != refs:
            reject(ExecutionContextFailure.MODEL_SELECTION_MISMATCH, 'Selected exact references must be distinct and deterministically ordered.', request)
        if snapshot is None:
            reject(ExecutionContextFailure.PREREQUISITE_UNAVAILABLE, 'Actual coherent registered-definition snapshot is unavailable.', request, incomplete=True)
        if snapshot.scope != request.registry_scope:
            reject(ExecutionContextFailure.RUNTIME_TARGET_MISMATCH if snapshot.scope.runtime_target != request.registry_scope.runtime_target else ExecutionContextFailure.REGISTRY_SCOPE_MISMATCH,
                'Snapshot scope/target differs from the explicitly requested registry.', request)
        if len(snapshot.definitions) > self._policy.maximum_snapshot_definitions:
            reject(ExecutionContextFailure.RESOURCE_LIMIT, 'Snapshot exceeds trusted inspection capacity.', request)
        try:
            snapshot.__post_init__()
        except (TypeError, ValueError):
            reject(ExecutionContextFailure.MODEL_SELECTION_MISMATCH, 'Snapshot violates the actual immutable membership contract.', request)
        inventory = {d.identity: d for d in snapshot.definitions}
        for reference in refs:
            definition = inventory.get(reference)
            if definition is None:
                reject(ExecutionContextFailure.MODEL_SELECTION_MISMATCH, 'Exact selected model is absent from supplied snapshot; no fallback.', request, reference=reference)
            try:
                definition.__post_init__()
            except RuntimeArtifactLoadError:
                reject(ExecutionContextFailure.PREREQUISITE_UNAVAILABLE, 'Original loaded/registered definition association is unavailable.', request, incomplete=True, reference=reference)
        if request.constraints.remaining_depth > self._policy.maximum_depth or request.constraints.maximum_nested_invocations > self._policy.maximum_nested_invocations:
            reject(ExecutionContextFailure.RESOURCE_LIMIT, 'Execution descriptions exceed the trusted factory ceiling.', request)
        if request.constraints.required_capabilities:
            reject(ExecutionContextFailure.UNSUPPORTED_CONSTRAINT, 'Requested mandatory executor/cancellation/accounting capability has no approved enforcer.', request, incomplete=True)
        if request.requires_active_deployment:
            reject(ExecutionContextFailure.ACTIVATION_UNAVAILABLE, 'Registered model membership provides no active-deployment evidence.', request, incomplete=True)
        if request.principal is None:
            reject(ExecutionContextFailure.PRINCIPAL_UNAVAILABLE, 'Trusted authenticated principal reference is unavailable.', request, incomplete=True)
        if request.authorization is None:
            reject(ExecutionContextFailure.AUTHORIZATION_UNAVAILABLE, 'Existing execution authorization evidence is unavailable.', request, incomplete=True)
        if self._trust is None:
            reject(ExecutionContextFailure.PREREQUISITE_UNAVAILABLE, 'No approved principal/authorization verification boundary exists.', request, incomplete=True)
        if request.principal.support is not self._trust or not _execution_reference_safe(request.principal.reference, self._trust.reference_types):
            reject(ExecutionContextFailure.UNTRUSTED_PRINCIPAL, 'Principal must be an actual approved immutable non-secret reference, not client metadata.', request)
        if request.authorization.support is not self._trust or not _execution_reference_safe((request.principal.reference, request.authorization.reference), self._trust.reference_types):
            reject(ExecutionContextFailure.AUTHORIZATION_MISMATCH, 'Authorization must be approved immutable evidence, never Boolean/credentials.', request)
        invocation = ExecutionTrustInvocation(request)
        proof = self._trust.verifier.verify(invocation)
        if type(proof) is not ExecutionTrustVerification or proof.invocation is not invocation:
            reject(ExecutionContextFailure.AUTHORIZATION_MISMATCH, 'Verification does not belong to the original internal invocation.', request)
        if proof.decision is ExecutionTrustDecision.UNAVAILABLE:
            reject(ExecutionContextFailure.AUTHORIZATION_UNAVAILABLE, 'Trusted boundary cannot establish current authentication/authorization evidence.', request, incomplete=True)
        if proof.decision is ExecutionTrustDecision.DENIED:
            reject(ExecutionContextFailure.TRUST_DENIED, 'Trusted boundary denied the requested protected execution association.', request)
        if proof.principal is not request.principal or proof.authorization is not request.authorization:
            reject(ExecutionContextFailure.AUTHORIZATION_MISMATCH, 'Verification must preserve actual original principal/decision references.', request)
        if proof.approved_scope.runtime_target != request.registry_scope.runtime_target:
            reject(ExecutionContextFailure.RUNTIME_TARGET_MISMATCH, 'Authorization audience/runtime target differs from requested target.', request)
        if proof.approved_scope != request.registry_scope or proof.approved_operation != request.operation or any(r not in proof.approved_models for r in refs) or not request.constraints.bounded_by(proof.approved_constraints):
            reject(ExecutionContextFailure.AUTHORIZATION_MISMATCH, 'Original decision does not cover this exact operation/scope/models/constraints.', request)
        return proof.principal, ExecutionAuthorizationRef(self._trust, proof)

    @staticmethod
    def _failure(error: _ExecutionContextRejected) -> ExecutionContextCreationResult:
        return ExecutionContextCreationResult(RuntimeArtifactLoadStatus.INCOMPLETE if error.incomplete else RuntimeArtifactLoadStatus.FAILED, diagnostics=(error.diagnostic,))

    def create(self, request: ExecutionContextCreateRequest) -> ExecutionContextCreationResult:
        try:
            principal, authority = self._verify(request)
            context = ExecutionContext(request.invocation_identity, request.semantic_context,
                request.registry_scope, request.operation, request.model_selection, principal, authority,
                request.correlation_identity, request.constraints, request.causation)
            return ExecutionContextCreationResult(RuntimeArtifactLoadStatus.SUCCEEDED, context)
        except _ExecutionContextRejected as error:
            return self._failure(error)

    def derive(self, parent: ExecutionContext, request: ExecutionContextDerivationRequest) -> ExecutionContextCreationResult:
        try:
            if type(parent) is not ExecutionContext or type(request) is not ExecutionContextDerivationRequest:
                self._reject(ExecutionContextFailure.INVALID_PARENT, 'Derivation requires actual typed parent and restricted child request.')
            if self._trust is None:
                self._reject(ExecutionContextFailure.PREREQUISITE_UNAVAILABLE, 'No approved current trust boundary can verify parent/child evidence.', incomplete=True)
            if parent.principal.support is not self._trust:
                self._reject(ExecutionContextFailure.INVALID_PARENT, 'Parent uses a different owner trust integration; no ambient adoption.')
            try:
                parent.__post_init__()
            except (TypeError, ValueError):
                self._reject(ExecutionContextFailure.INVALID_PARENT, 'Parent context violates its verified structural associations.')
            child = ExecutionContextCreateRequest(request.invocation_identity, parent.semantic_context,
                parent.registry_scope, parent.operation, request.model_selection, parent.correlation_identity,
                request.constraints, parent.principal, request.authorization,
                ExecutionCausationRef(parent.invocation_identity))
            # Recheck original current evidence; a carried historical context is
            # not a permanent credential. No parent graph is retained by child.
            self._verify(parent.authorization.verification.invocation.request)
            if request.invocation_identity == parent.invocation_identity:
                self._reject(ExecutionContextFailure.INVALID_INVOCATION, 'Child invocation must have a new explicit identity.', child)
            if request.model_selection.snapshot is not parent.model_selection.snapshot or any(r not in parent.model_selection.references for r in request.model_selection.references):
                self._reject(ExecutionContextFailure.SCOPE_ESCALATION, 'Child cannot add model versions or replace the original membership view.', child)
            if parent.constraints.remaining_depth == 0 or parent.constraints.maximum_nested_invocations == 0:
                self._reject(ExecutionContextFailure.DEPTH_EXHAUSTED, 'Parent description permits no further child invocation.', child)
            if parent.constraints.deadline is not None and (request.constraints.deadline is None or request.constraints.deadline > parent.constraints.deadline):
                self._reject(ExecutionContextFailure.DEADLINE_EXTENSION, 'Child cannot drop or extend a mandatory parent deadline.', child)
            if not request.constraints.bounded_by(parent.constraints, child=True):
                self._reject(ExecutionContextFailure.SCOPE_ESCALATION, 'Child cannot reset depth, nested limits or mandatory constraint descriptions.', child)
            return self.create(child)
        except _ExecutionContextRejected as error:
            return self._failure(error)


__all__ += ['RuntimeInvocationId', 'ExecutionCorrelationId', 'ExecutionCausationRef',
    'ExecutionOperationRef', 'ExecutionConstraints', 'ExecutionDeadlineStatus',
    'ExecutionModelSelection', 'ExecutionContextCreateRequest', 'ExecutionTrustInvocation',
    'ExecutionTrustDecision', 'ExecutionTrustVerification', 'ExecutionTrustVerifier',
    'ExecutionTrustSupport', 'ExecutionPrincipalRef', 'ExecutionAuthorizationInput', 'ExecutionAuthorizationRef',
    'ExecutionContextFailure', 'ExecutionContextDiagnostic', 'ExecutionContext',
    'ExecutionContextCreationResult', 'ExecutionContextDerivationRequest',
    'ExecutionContextPolicy', 'ExecutionContextFactory']
