"""RUN-01 explicit CMP-07/08/09 bridge; no filesystem or transport implementation."""
from dataclasses import dataclass, field, replace
from compiler_core.public import (ArtifactReader, ArtifactReadRequest, ArtifactReadPlanner,
    ArtifactReadPolicy, ArtifactReadIntegrity, ArtifactReadResult, ArtifactReadError,
    ArtifactReadSelectionMode, CompilationStatus, CompilationDiagnostic, CompilationFailure)
from runtime_core.public import (RuntimeArtifactLoadPolicy, RuntimeArtifactLoadContext,
    RuntimeArtifactLoadBinding, RuntimeArtifactLoadRequest, RuntimeArtifactLoadResult,
    RuntimeArtifactLoadStatus, RuntimeArtifactLoadFailure, RuntimeArtifactLoadStage,
    RuntimeLoadSeverity, RuntimeArtifactLoadDiagnostic, RuntimeArtifactReaderDiagnostic,
    RuntimeArtifactSourceEvidence, RuntimeVerifiedArtifactBytes, RuntimeArtifactByteReadResult,
    RuntimeArtifactLoadAuthorizer, UnavailableRuntimeArtifactLoadAuthorizer,
    RuntimeArtifactDecoderCatalog, DefaultRuntimeArtifactLoader)
from runtime_core.public import RuntimeLoadDiagnostics

MODULE_NAME = 'runtime-artifact-loader'


def _reader_diagnostics(values: tuple[CompilationDiagnostic, ...]) -> tuple[RuntimeArtifactReaderDiagnostic, ...]:
    projected = []
    for diagnostic in values:
        association = diagnostic.association
        artifact = None if association is None else association.artifact_target
        projected.append(RuntimeArtifactReaderDiagnostic(diagnostic.code.value, diagnostic.message,
            RuntimeLoadSeverity(diagnostic.severity.value),
            None if association is None or association.read_stage is None else association.read_stage.value,
            None if association is None or association.manifest_identity is None else association.manifest_identity.value,
            None if artifact is None else artifact.key, None if artifact is None else artifact.kind,
            None if association is None or association.output_location is None else association.output_location.value,
            None if association is None or association.read_source_type is None else association.read_source_type.value))
    return tuple(projected)


def _read_policy(policy: RuntimeArtifactLoadPolicy, original: ArtifactReadPolicy) -> ArtifactReadPolicy:
    return ArtifactReadPolicy(min(policy.maximum_artifact_bytes, original.maximum_artifact_bytes),
        min(policy.maximum_aggregate_bytes, original.maximum_aggregate_bytes),
        min(policy.maximum_artifact_count, original.maximum_artifact_count), ArtifactReadIntegrity.DIGEST_VERIFIED)


def _read_status(status: CompilationStatus) -> RuntimeArtifactLoadStatus:
    return {CompilationStatus.SUCCEEDED: RuntimeArtifactLoadStatus.SUCCEEDED,
        CompilationStatus.FAILED: RuntimeArtifactLoadStatus.FAILED,
        CompilationStatus.INCOMPLETE: RuntimeArtifactLoadStatus.INCOMPLETE}[status]


@dataclass(frozen=True, slots=True)
class CmpRuntimeArtifactLoadRequest:
    """Application resolves these real existing contracts; no paths/bytes/Boolean grant."""
    read_request: ArtifactReadRequest
    context: RuntimeArtifactLoadContext
    policy: RuntimeArtifactLoadPolicy = field(default_factory=RuntimeArtifactLoadPolicy)

    def __post_init__(self) -> None:
        if type(self.read_request) is not ArtifactReadRequest or type(self.context) is not RuntimeArtifactLoadContext or type(self.policy) is not RuntimeArtifactLoadPolicy:
            raise TypeError('Application request requires actual CMP-09 request and typed runtime context/policy.')


@dataclass(frozen=True, slots=True)
class CmpRuntimeArtifactByteSource:
    """Read once through injected CMP-09 reader; retain authoritative request in tooling."""
    request: ArtifactReadRequest = field(repr=False)
    binding: RuntimeArtifactLoadBinding
    reader: ArtifactReader = field(repr=False)

    def __post_init__(self) -> None:
        if type(self.request) is not ArtifactReadRequest or type(self.binding) is not RuntimeArtifactLoadBinding or not callable(getattr(type(self.reader), 'read', None)):
            raise TypeError('Bridge requires actual CMP request, bound neutral scope and trusted reader.')
        manifest = self.request.manifest
        if (self.binding.manifest_identity, self.binding.manifest_schema_version, self.binding.semantic_context, self.binding.compilation_target, self.binding.artifacts) != (manifest.identity.value, manifest.schema_version.value, manifest.semantic_context, manifest.target.value, manifest.artifacts):
            raise ValueError('Bridge cannot substitute another manifest declaration.')
        if self.request.selection.mode is not ArtifactReadSelectionMode.ALL_DECLARED_ARTIFACTS or not self.binding.complete_set:
            raise ValueError('Runtime v0 source requires a complete ALL selection.')

    def read(self, binding: RuntimeArtifactLoadBinding, policy: RuntimeArtifactLoadPolicy) -> RuntimeArtifactByteReadResult:
        if binding is not self.binding or type(policy) is not RuntimeArtifactLoadPolicy:
            raise ValueError('Source cannot serve another bound loading invocation.')
        request = replace(self.request, policy=_read_policy(policy, self.request.policy))
        try:
            result = self.reader.read(request)
        except ArtifactReadError as error:
            return RuntimeArtifactByteReadResult(_read_status(error.status), binding, diagnostics=_reader_diagnostics(error.diagnostics))
        if type(result) is not ArtifactReadResult:
            RuntimeLoadDiagnostics.reject(RuntimeArtifactLoadFailure.READER_FAILED, 'CMP-09 reader returned an invalid outcome contract.', stage=RuntimeArtifactLoadStage.READ)
        causes = _reader_diagnostics(result.diagnostics)
        if result.status is not CompilationStatus.SUCCEEDED:
            return RuntimeArtifactByteReadResult(_read_status(result.status), binding, diagnostics=causes)
        # Reject an incorrectly wired reader before interpreting any returned payload.
        if result.plan is None or result.plan.request is not request or not result.plan.complete_set or result.plan.effective_policy.required_integrity is not ArtifactReadIntegrity.DIGEST_VERIFIED:
            RuntimeLoadDiagnostics.reject(RuntimeArtifactLoadFailure.READER_FAILED, 'CMP-09 reader did not preserve actual request and mandatory digest policy.', stage=RuntimeArtifactLoadStage.READ)
        effective = result.plan.effective_policy
        if effective.maximum_artifact_count > request.policy.maximum_artifact_count or effective.maximum_artifact_bytes > request.policy.maximum_artifact_bytes or effective.maximum_aggregate_bytes > request.policy.maximum_aggregate_bytes:
            RuntimeLoadDiagnostics.reject(RuntimeArtifactLoadFailure.RESOURCE_LIMIT_EXCEEDED, 'CMP-09 reader increased requested runtime ceilings.', stage=RuntimeArtifactLoadStage.READ)
        entries = request.receipt.artifacts
        if tuple(result.plan.entries) != entries or tuple(a.descriptor for a in result.artifacts) != binding.artifacts:
            RuntimeLoadDiagnostics.reject(RuntimeArtifactLoadFailure.RECEIPT_MISMATCH, 'CMP-09 read did not preserve complete selected materialization evidence.', stage=RuntimeArtifactLoadStage.READ)
        artifacts = []
        for artifact, entry in zip(result.artifacts, entries):
            digest = artifact.verification.verified_digest
            if digest is None or entry.verified_digest is None or digest != entry.verified_digest or digest.algorithm != 'sha256':
                diagnostic = RuntimeArtifactReaderDiagnostic(CompilationFailure.READ_REQUIRED_DIGEST_MISSING.value,
                    'Runtime loading requires the original CMP-09 verified SHA-256 evidence.', RuntimeLoadSeverity.WARNING,
                    'verify', binding.manifest_identity, artifact.descriptor.key, artifact.descriptor.kind, artifact.location.value, 'local-filesystem')
                return RuntimeArtifactByteReadResult(RuntimeArtifactLoadStatus.INCOMPLETE, binding, diagnostics=(*causes, diagnostic))
            evidence = RuntimeArtifactSourceEvidence(binding, artifact.descriptor.key, request.source.root_reference,
                request.source.output_directory, artifact.location.value, artifact.verification.actual_byte_length, digest.value)
            artifacts.append(RuntimeVerifiedArtifactBytes(artifact.descriptor, evidence, artifact.content))
        return RuntimeArtifactByteReadResult(RuntimeArtifactLoadStatus.SUCCEEDED, binding, tuple(artifacts), causes)


@dataclass(frozen=True, slots=True)
class CmpRuntimeArtifactLoadResult:
    """Application outcome retains the exact original reader diagnostic objects."""
    runtime_result: RuntimeArtifactLoadResult
    reader_diagnostics: tuple[CompilationDiagnostic, ...] = ()

    def __post_init__(self) -> None:
        if type(self.runtime_result) is not RuntimeArtifactLoadResult or type(self.reader_diagnostics) is not tuple or any(type(d) is not CompilationDiagnostic for d in self.reader_diagnostics):
            raise TypeError('Application result preserves actual runtime outcome and original CMP diagnostics.')


class _RecordingReader:
    """Operation-local adapter; no global mutable registry, bytes or cross-call state."""
    def __init__(self, reader: ArtifactReader) -> None:
        self.reader = reader
        self.diagnostics: tuple[CompilationDiagnostic, ...] = ()

    def read(self, request: ArtifactReadRequest) -> ArtifactReadResult:
        try:
            result = self.reader.read(request)
        except ArtifactReadError as error:
            self.diagnostics = error.diagnostics
            raise
        if type(result) is not ArtifactReadResult:
            RuntimeLoadDiagnostics.reject(RuntimeArtifactLoadFailure.READER_FAILED, 'CMP-09 reader returned an invalid outcome contract.', stage=RuntimeArtifactLoadStage.READ)
        self.diagnostics = result.diagnostics
        return result


@dataclass(frozen=True, slots=True)
class RuntimeArtifactLoadingService:
    """Internal application orchestration. No Django request, endpoint or default authority.

    Hosting composition owns approved roots, authenticated authority and decoder
    approvals. Current defaults intentionally do not authorize or decode artifacts.
    """
    reader: ArtifactReader = field(repr=False)
    authorizer: RuntimeArtifactLoadAuthorizer = field(default_factory=UnavailableRuntimeArtifactLoadAuthorizer, repr=False)
    decoders: RuntimeArtifactDecoderCatalog = field(default_factory=RuntimeArtifactDecoderCatalog)
    server_policy: RuntimeArtifactLoadPolicy = field(default_factory=RuntimeArtifactLoadPolicy)
    planner: ArtifactReadPlanner = field(default_factory=ArtifactReadPlanner)

    def __post_init__(self) -> None:
        if not callable(getattr(type(self.reader), 'read', None)) or not callable(getattr(type(self.authorizer), 'authorize', None)) or type(self.decoders) is not RuntimeArtifactDecoderCatalog or type(self.server_policy) is not RuntimeArtifactLoadPolicy or type(self.planner) is not ArtifactReadPlanner:
            raise TypeError('Application composition requires trusted ports/catalog/policies and existing CMP planner.')

    def load(self, request: CmpRuntimeArtifactLoadRequest) -> CmpRuntimeArtifactLoadResult:
        if type(request) is not CmpRuntimeArtifactLoadRequest:
            diagnostic = RuntimeArtifactLoadDiagnostic(RuntimeArtifactLoadFailure.INVALID_REQUEST,
                'Application loading requires an actual typed CMP-bound request.', RuntimeLoadSeverity.ERROR, RuntimeArtifactLoadStage.PREFLIGHT)
            return CmpRuntimeArtifactLoadResult(RuntimeArtifactLoadResult(RuntimeArtifactLoadStatus.FAILED, diagnostics=(diagnostic,)))
        original = request.read_request
        manifest = original.manifest
        policy = request.policy.bounded_by(self.server_policy)
        def rejection(code: RuntimeArtifactLoadFailure, message: str, *, status: RuntimeArtifactLoadStatus = RuntimeArtifactLoadStatus.FAILED, originals: tuple[CompilationDiagnostic, ...] = ()) -> CmpRuntimeArtifactLoadResult:
            diagnostic = RuntimeArtifactLoadDiagnostic(code, message,
                RuntimeLoadSeverity.WARNING if status is RuntimeArtifactLoadStatus.INCOMPLETE else RuntimeLoadSeverity.ERROR,
                RuntimeArtifactLoadStage.PREFLIGHT, manifest.identity.value, runtime_target=request.context.runtime_target,
                semantic_context=request.context.semantic_context, reader_diagnostics=_reader_diagnostics(originals))
            return CmpRuntimeArtifactLoadResult(RuntimeArtifactLoadResult(status, diagnostics=(diagnostic,)), originals)
        if len(manifest.artifacts) > policy.maximum_artifact_count:
            return rejection(RuntimeArtifactLoadFailure.RESOURCE_LIMIT_EXCEEDED, 'Entire declared runtime package exceeds effective artifact-count ceiling.')
        if original.selection.mode is not ArtifactReadSelectionMode.ALL_DECLARED_ARTIFACTS:
            return rejection(RuntimeArtifactLoadFailure.INCOMPLETE_SET, 'Runtime v0 accepts only ALL_DECLARED_ARTIFACTS; no implicit closure.')
        # Pure planning: no read, compiler invocation, canonical revalidation or runtime execution.
        checked = replace(original, policy=_read_policy(policy, original.policy))
        try:
            plan = self.planner.plan(checked)
        except ArtifactReadError as error:
            codes = {d.code for d in error.diagnostics}
            code = RuntimeArtifactLoadFailure.RECEIPT_MISMATCH if CompilationFailure.READ_RECEIPT_MISMATCH in codes else RuntimeArtifactLoadFailure.INTEGRITY_INSUFFICIENT if CompilationFailure.READ_REQUIRED_DIGEST_MISSING in codes or CompilationFailure.READ_UNSUPPORTED_DIGEST in codes else RuntimeArtifactLoadFailure.RESOURCE_LIMIT_EXCEEDED if CompilationFailure.READ_SIZE_LIMIT_EXCEEDED in codes else RuntimeArtifactLoadFailure.MANIFEST_MISMATCH
            return rejection(code, 'Established CMP-09 preflight rejected manifest, materialization, integrity or resource prerequisites.', status=_read_status(error.status), originals=error.diagnostics)
        binding = RuntimeArtifactLoadBinding(manifest.identity.value, manifest.schema_version.value,
            manifest.semantic_context, manifest.target.value, manifest.artifacts, plan.selected_keys, plan.complete_set)
        recorder = _RecordingReader(self.reader)
        source = CmpRuntimeArtifactByteSource(checked, binding, recorder)
        loader = DefaultRuntimeArtifactLoader(source, self.authorizer, self.decoders, policy)
        result = loader.load(RuntimeArtifactLoadRequest(binding, request.context, policy))
        return CmpRuntimeArtifactLoadResult(result, recorder.diagnostics)


__all__ = ['MODULE_NAME', 'CmpRuntimeArtifactLoadRequest', 'CmpRuntimeArtifactByteSource',
    'CmpRuntimeArtifactLoadResult', 'RuntimeArtifactLoadingService']
