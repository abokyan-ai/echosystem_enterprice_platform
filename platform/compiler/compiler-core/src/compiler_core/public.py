"""CMP-01 deterministic compiler foundation; no concrete generators or hosting."""
from dataclasses import dataclass, field, fields, is_dataclass, replace, InitVar
from collections import Counter, deque
from enum import Enum
from typing import Protocol, Mapping
from types import MappingProxyType
import re
from semantic_kernel.public import SemanticContextRef, SemanticElementId, ElementVersionRef, SemanticVersion, QualifiedName, PrimitiveType, ElementRef, SemanticElementKinds
from model_core.public import (CanonicalModel, TypeValidationSeverity, TypeDataComposition,
    FieldId, FieldName, FieldDefinition, FieldConstraintSet, DataFacet, DataFacetError,
    PrimitiveTypeRef, SemanticTypeRef, TypeRef)
from model_authoring.public import (
    ModelValidationResult, ModelValidationStatus, CompilationReadiness,
    CanonicalSourceAssociation, ModelDiagnosticContext, ModelDiagnosticEntry,
    ModelDiagnosticOrigin, ModelDiagnosticTarget, ModelDiagnosticTargetKind,
    associate_model_diagnostic, CompilationDiagnosticReport, CompilerPhaseDiagnosticView,
    CompilationDiagnosticOrigin, CompilationDiagnosticDetails, CompilationArtifactDiagnosticView,
    AuthoringSchemaPath,
)
from compiled_contracts.public import (CompilationArtifact, CompilationArtifactKey, CompilationArtifactKind,
    RuntimeArtifactDependencyRef, RuntimeArtifactMetadata, RuntimeArtifactDescriptor)

MODULE_NAME = 'compiler-core'


class CompilationStatus(Enum):
    SUCCEEDED = 'succeeded'
    FAILED = 'failed'
    INCOMPLETE = 'incomplete'


class CompilationPhaseStatus(Enum):
    COMPLETED = 'completed'
    FAILED = 'failed'
    INCOMPLETE = 'incomplete'
    SKIPPED = 'skipped'


class CompilationCapability(Enum):
    PREPARE = 'prepare'
    EMIT_ARTIFACTS = 'emit-artifacts'
    EMIT_IR = 'emit-ir'


@dataclass(frozen=True, slots=True)
class CompilationTargetId:
    value: str

    def __post_init__(self) -> None:
        if type(self.value) is not str or re.fullmatch(r'[a-z][a-z0-9]*(?:-[a-z0-9]+)*', self.value) is None or len(self.value) > 80:
            raise ValueError('Compilation target requires a bounded explicit logical token.')


PREPARATION_TARGET = CompilationTargetId('foundation-preparation')
BUILD_TARGET = CompilationTargetId('artifact-build')


class CompilationFailure(Enum):
    INVALID_INPUT = 'CMP-001'
    VALIDATION_NOT_READY = 'CMP-002'
    VALIDATION_EVIDENCE_UNBOUND = 'CMP-003'
    MODEL_MISMATCH = 'CMP-004'
    CONTEXT_MISMATCH = 'CMP-005'
    UNSUPPORTED_TARGET = 'CMP-006'
    PHASE_UNAVAILABLE = 'CMP-007'
    PHASE_FAILED = 'CMP-008'
    ARTIFACT_CONFLICT = 'CMP-009'
    INCOMPLETE_BUILD = 'CMP-010'
    IR_INVALID_ENVELOPE = 'CMP-011'
    IR_UNSUPPORTED_SCHEMA = 'CMP-012'
    IR_INVALID_IDENTITY = 'CMP-013'
    IR_CONTEXT_MISMATCH = 'CMP-014'
    IR_INPUT_MISMATCH = 'CMP-015'
    IR_UNSUPPORTED_KIND = 'CMP-016'
    IR_PAYLOAD_MISMATCH = 'CMP-017'
    IR_MISSING_PAYLOAD = 'CMP-018'
    IR_INCOMPATIBLE_HANDOFF = 'CMP-019'
    IR_DUPLICATE_IDENTITY = 'CMP-020'
    TYPE_IR_UNSUPPORTED_DEFINITION = 'CMP-021'
    TYPE_IR_MISSING_DATA_FACET = 'CMP-022'
    TYPE_IR_INVALID_FIELD = 'CMP-023'
    TYPE_IR_UNSUPPORTED_REFERENCE = 'CMP-024'
    TYPE_IR_UNSUPPORTED_CONSTRAINT = 'CMP-025'
    TYPE_IR_INPUT_MISMATCH = 'CMP-026'
    TYPE_IR_IDENTITY_COVERAGE = 'CMP-027'
    TYPE_IR_INVALID_PAYLOAD = 'CMP-028'
    NONDETERMINISTIC_CONFIGURATION = 'CMP-029'
    CONFIGURATION_CHANGED = 'CMP-030'
    MANIFEST_COMPILATION_NOT_SUCCESSFUL = 'CMP-031'
    MANIFEST_UNSUPPORTED_SCHEMA = 'CMP-032'
    MANIFEST_INVALID_IDENTITY = 'CMP-033'
    MANIFEST_CONTEXT_MISMATCH = 'CMP-034'
    MANIFEST_TARGET_MISMATCH = 'CMP-035'
    MANIFEST_SNAPSHOT_MISMATCH = 'CMP-036'
    MANIFEST_UNSUPPORTED_KIND = 'CMP-037'
    MANIFEST_OUTPUT_UNBOUND = 'CMP-038'
    MANIFEST_INCOMPLETE_METADATA = 'CMP-039'
    MANIFEST_UNKNOWN_DEPENDENCY = 'CMP-040'
    MANIFEST_DUPLICATE_ARTIFACT = 'CMP-041'
    MANIFEST_INCOMPLETE_OUTPUT = 'CMP-042'
    MANIFEST_IDENTITY_COLLISION = 'CMP-043'
    WRITE_INVALID_INPUT = 'CMP-044'
    WRITE_COMPILATION_NOT_READY = 'CMP-045'
    WRITE_MANIFEST_MISMATCH = 'CMP-046'
    WRITE_CONTENT_MEMBERSHIP = 'CMP-047'
    WRITE_UNSUPPORTED_CONTENT = 'CMP-048'
    WRITE_INVALID_DESTINATION = 'CMP-049'
    WRITE_UNSAFE_PATH = 'CMP-050'
    WRITE_LOCATION_CONFLICT = 'CMP-051'
    WRITE_UNSUPPORTED_POLICY = 'CMP-052'
    WRITE_DESTINATION_EXISTS = 'CMP-053'
    WRITE_STAGING_FAILED = 'CMP-054'
    WRITE_IO_FAILED = 'CMP-055'
    WRITE_INTEGRITY_MISMATCH = 'CMP-056'
    WRITE_COMMIT_FAILED = 'CMP-057'
    WRITE_CLEANUP_FAILED = 'CMP-058'
    WRITE_UNSUPPORTED_ATOMICITY = 'CMP-059'
    WRITE_UNSUPPORTED_DURABILITY = 'CMP-060'
    WRITE_UNSUPPORTED_ENCODING = 'CMP-061'
    READ_INVALID_REQUEST = 'CMP-062'
    READ_MANIFEST_MISMATCH = 'CMP-063'
    READ_RECEIPT_MISMATCH = 'CMP-064'
    READ_UNKNOWN_ARTIFACT = 'CMP-065'
    READ_INVALID_SELECTION = 'CMP-066'
    READ_UNSUPPORTED_SOURCE = 'CMP-067'
    READ_UNSAFE_PATH = 'CMP-068'
    READ_UNSUPPORTED_FILE_TYPE = 'CMP-069'
    READ_MISSING_FILE = 'CMP-070'
    READ_ACCESS_DENIED = 'CMP-071'
    READ_SIZE_LIMIT_EXCEEDED = 'CMP-072'
    READ_SIZE_MISMATCH = 'CMP-073'
    READ_DIGEST_MISMATCH = 'CMP-074'
    READ_REQUIRED_DIGEST_MISSING = 'CMP-075'
    READ_IO_FAILED = 'CMP-076'
    READ_INCOMPLETE_SET = 'CMP-077'
    READ_CONCURRENT_MODIFICATION = 'CMP-078'
    READ_UNSUPPORTED_DIGEST = 'CMP-079'
    READ_INVALID_POLICY = 'CMP-080'


def _phase_id(value: str) -> None:
    if type(value) is not str or re.fullmatch(r'CMP-PHASE-[A-Z0-9]+(?:-[A-Z0-9]+)*', value) is None:
        raise ValueError('Phase requires a stable CMP-PHASE identifier.')


@dataclass(frozen=True, slots=True)
class CompilationArtifactTarget:
    """Existing artifact identities; no artifact must have been constructed."""
    key: CompilationArtifactKey | None = None
    kind: CompilationArtifactKind | None = None
    target: CompilationTargetId | None = None

    def __post_init__(self) -> None:
        for value, expected in ((self.key, CompilationArtifactKey), (self.kind, CompilationArtifactKind), (self.target, CompilationTargetId)):
            if value is not None and type(value) is not expected:
                raise TypeError('Artifact diagnostic association reuses owned typed identifiers.')
        if self.key is None and self.kind is None and self.target is None:
            raise ValueError('Provide an actual key/kind or intended compiler target.')

    @property
    def diagnostic_view(self) -> CompilationArtifactDiagnosticView:
        return CompilationArtifactDiagnosticView(None if self.key is None else self.key.value, None if self.kind is None else self.kind.value, None if self.target is None else self.target.value)


@dataclass(frozen=True, slots=True)
class CompilationDiagnosticAssociation:
    origin: CompilationDiagnosticOrigin
    phase_id: str | None = None
    semantic_target: ModelDiagnosticTarget | None = None
    artifact_target: CompilationArtifactTarget | None = None
    related_targets: tuple[ModelDiagnosticTarget, ...] = ()
    source_path: AuthoringSchemaPath | None = None
    related_paths: tuple[AuthoringSchemaPath, ...] = ()
    semantic_context: SemanticContextRef | None = None
    ir_identity: 'SemanticIRId | None' = None
    related_artifact_targets: tuple[CompilationArtifactTarget, ...] = ()
    manifest_identity: 'RuntimeArtifactManifestId | None' = None
    write_stage: 'ArtifactWriteStage | None' = None
    output_location: 'ArtifactRelativeLocation | None' = None
    read_stage: 'ArtifactReadStage | None' = None
    read_source_type: 'ArtifactReadSourceType | None' = None

    def __post_init__(self) -> None:
        if self.write_stage is not None and type(self.write_stage) is not ArtifactWriteStage:
            raise TypeError('Write diagnostics require an explicit bounded stage.')
        if self.read_stage is not None and type(self.read_stage) is not ArtifactReadStage:
            raise TypeError('Read diagnostics require an explicit bounded stage.')
        if self.read_source_type is not None and type(self.read_source_type) is not ArtifactReadSourceType:
            raise TypeError('Read diagnostics require an explicit bounded source type.')
        if self.output_location is not None and type(self.output_location) is not ArtifactRelativeLocation:
            raise TypeError('Write diagnostics expose only validated relative locations.')
        if self.artifact_target is not None and type(self.artifact_target) is not CompilationArtifactTarget:
            raise TypeError('Artifact target must be a bounded association.')
        if self.ir_identity is not None and type(self.ir_identity) is not SemanticIRId:
            raise TypeError('IR diagnostic identity is independent of semantic/artifact identity.')
        if self.manifest_identity is not None and type(self.manifest_identity) is not RuntimeArtifactManifestId:
            raise TypeError('Manifest diagnostic identity is independent of artifact and semantic identities.')
        if type(self.related_artifact_targets) not in (tuple, list) or any(type(a) is not CompilationArtifactTarget for a in self.related_artifact_targets):
            raise TypeError('Related artifact associations require immutable typed artifact targets.')
        object.__setattr__(self, 'related_artifact_targets', tuple(self.related_artifact_targets))
        CompilationDiagnosticDetails(self.origin, self.phase_id, None if self.artifact_target is None else self.artifact_target.diagnostic_view, self.semantic_context, None if self.ir_identity is None else self.ir_identity.value)
        if self.semantic_target is not None and type(self.semantic_target) is not ModelDiagnosticTarget:
            raise TypeError('Reuse the existing semantic target; fields keep their owned FieldId.')
        if self.semantic_target is not None and type(self.semantic_target.reference) is not ElementVersionRef:
            raise ValueError('Compiler definition association must preserve an exact version.')
        for name, expected in (('related_targets', ModelDiagnosticTarget), ('related_paths', AuthoringSchemaPath)):
            values = getattr(self, name)
            if type(values) not in (tuple, list) or any(type(v) is not expected for v in values):
                raise TypeError('Related associations are explicit finite ordered typed sequences.')
            object.__setattr__(self, name, tuple(values))
        if any(type(t.reference) is not ElementVersionRef for t in self.related_targets):
            raise ValueError('Related compiler definitions retain exact versions.')
        if self.source_path is not None and type(self.source_path) is not AuthoringSchemaPath:
            raise TypeError('Explicit source association requires an existing authoring path.')


@dataclass(frozen=True, slots=True)
class CompilationDiagnostic:
    """Narrow compiler prerequisite/capability seam pending full SK-11."""
    code: CompilationFailure
    message: str
    severity: TypeValidationSeverity
    phase_id: str | None = None
    reference: ElementVersionRef | None = None
    cause_code: str | None = None
    association: CompilationDiagnosticAssociation | None = None

    def __post_init__(self) -> None:
        if self.association is not None:
            if type(self.association) is not CompilationDiagnosticAssociation:
                raise TypeError('Compiler diagnostic association must be explicitly typed.')
            if self.phase_id is not None and self.phase_id != self.association.phase_id:
                raise ValueError('Diagnostic and association phase evidence cannot conflict.')
            if self.reference is not None and self.association.semantic_target is not None and self.reference != self.association.semantic_target.reference:
                raise ValueError('Diagnostic and association semantic evidence cannot conflict.')
        if type(self.code) is not CompilationFailure or type(self.message) is not str or not self.message or type(self.severity) is not TypeValidationSeverity:
            raise TypeError('Compilation diagnostics require actual bounded code/message/severity.')
        if self.phase_id is not None:
            _phase_id(self.phase_id)
        if self.reference is not None and type(self.reference) is not ElementVersionRef:
            raise TypeError('Compiler diagnostic subject must retain an exact semantic coordinate.')
        if self.cause_code is not None and (type(self.cause_code) is not str or not self.cause_code):
            raise TypeError('Delegated compiler failure code must be nonempty text.')


@dataclass(frozen=True, slots=True)
class CompilationContext:
    scope: SemanticContextRef
    target: CompilationTargetId

    def __post_init__(self) -> None:
        if type(self.scope) is not SemanticContextRef or type(self.scope.context_id) is not SemanticElementId or type(self.target) is not CompilationTargetId:
            raise TypeError('Compiler context requires explicit canonical scope and typed target.')


@dataclass(frozen=True, slots=True)
class CompilationRequest:
    canonical_model: CanonicalModel
    validation_evidence: ModelValidationResult | None
    context: CompilationContext
    source_associations: tuple[CanonicalSourceAssociation, ...] = ()

    def __post_init__(self) -> None:
        if type(self.canonical_model) is not CanonicalModel or type(self.context) is not CompilationContext:
            raise TypeError('Compiler input is actual MOD-04 CanonicalModel plus explicit compiler context.')
        if self.validation_evidence is not None and type(self.validation_evidence) is not ModelValidationResult:
            raise TypeError('Evidence must be original actual MOD-08 result or explicitly unavailable.')
        associations = ModelDiagnosticContext(self.context.scope, self.source_associations)
        object.__setattr__(self, 'source_associations', associations.source_associations)


@dataclass(frozen=True, slots=True)
class CompilationPhaseDescriptor:
    id: str
    prerequisites: tuple[str, ...] = ()
    capabilities: frozenset[CompilationCapability] = frozenset()
    targets: frozenset[CompilationTargetId] = frozenset()

    def __post_init__(self) -> None:
        _phase_id(self.id)
        if type(self.prerequisites) not in (tuple, list):
            raise TypeError('Phase prerequisites require an explicit ordered sequence.')
        prerequisites = tuple(self.prerequisites)
        for prerequisite in prerequisites:
            _phase_id(prerequisite)
        if len(set(prerequisites)) != len(prerequisites) or self.id in prerequisites:
            raise ValueError('Phase prerequisites cannot repeat or depend on self.')
        for values, expected in ((self.capabilities, CompilationCapability), (self.targets, CompilationTargetId)):
            if type(values) not in (frozenset, set, tuple, list) or any(type(v) is not expected for v in values):
                raise TypeError('Phase capabilities/target support must be explicit typed finite sets.')
        object.__setattr__(self, 'prerequisites', prerequisites)
        object.__setattr__(self, 'capabilities', frozenset(self.capabilities))
        object.__setattr__(self, 'targets', frozenset(self.targets))


@dataclass(frozen=True, slots=True)
class PreparedCompilationInput:
    """Preparation inventory, not universal IR or target artifact payload."""
    model: CanonicalModel
    context: CompilationContext

    def __post_init__(self) -> None:
        if type(self.model) is not CanonicalModel or type(self.context) is not CompilationContext or self.model.scope != self.context.scope:
            raise TypeError('Prepared input must retain the original scoped canonical snapshot.')

    @property
    def definitions(self) -> tuple[ElementVersionRef, ...]:
        return self.model.references


def _artifacts(values: tuple[CompilationArtifact, ...]) -> tuple[CompilationArtifact, ...]:
    if type(values) not in (tuple, list):
        raise TypeError('Artifacts require explicit ordered immutable value implementations.')
    artifacts = tuple(values)
    for artifact in artifacts:
        # Future owned payloads must be immutable dataclass value implementations.
        if not is_dataclass(artifact) or isinstance(artifact, type) or not artifact.__dataclass_params__.frozen:
            raise TypeError('Artifact implementation must be an immutable typed value, not a dict/blob.')
        if type(artifact.key) is not CompilationArtifactKey or type(artifact.kind) is not CompilationArtifactKind or type(artifact.scope) is not SemanticContextRef or type(artifact.target) is not str:
            raise TypeError('Artifact violated its explicit metadata contract.')
        CompilationTargetId(artifact.target)
        if type(artifact.semantic_dependencies) is not tuple or any(type(r) is not ElementVersionRef for r in artifact.semantic_dependencies):
            raise TypeError('Artifact dependencies require exact immutable semantic references.')
    return tuple(sorted(artifacts, key=lambda a: a.key.value))


class CompilationArtifactConflict(ValueError):
    def __init__(self, key: CompilationArtifactKey) -> None:
        self.key = key
        super().__init__('Duplicate artifact key; no last-write-wins or implicit equality policy.')


@dataclass(frozen=True, slots=True)
class CompilationArtifactCollection:
    artifacts: tuple[CompilationArtifact, ...] = ()
    _by_key: Mapping[CompilationArtifactKey, CompilationArtifact] = field(init=False, repr=False, compare=False, hash=False)

    def __post_init__(self) -> None:
        artifacts = _artifacts(self.artifacts)
        by_key = {}
        for artifact in artifacts:
            if artifact.key in by_key:
                raise CompilationArtifactConflict(artifact.key)
            by_key[artifact.key] = artifact
        object.__setattr__(self, 'artifacts', artifacts)
        object.__setattr__(self, '_by_key', MappingProxyType(by_key))

    def find(self, key: CompilationArtifactKey) -> CompilationArtifact | None:
        if type(key) is not CompilationArtifactKey:
            raise TypeError('Artifact lookup requires its independent logical key.')
        return self._by_key.get(key)


@dataclass(frozen=True, slots=True)
class CompilationState:
    preparation: PreparedCompilationInput | None = None
    artifacts: CompilationArtifactCollection = field(default_factory=CompilationArtifactCollection)
    ir_envelopes: tuple['SemanticIREnvelope', ...] = ()
    phase_outcomes: tuple['CompilationPhaseOutcome', ...] = ()

    def __post_init__(self) -> None:
        object.__setattr__(self, 'ir_envelopes', _ir_values(self.ir_envelopes))
        if type(self.phase_outcomes) not in (tuple, list) or any(type(o) is not CompilationPhaseOutcome for o in self.phase_outcomes):
            raise TypeError('Internal state preserves original ordered phase outcomes.')
        object.__setattr__(self, 'phase_outcomes', tuple(self.phase_outcomes))
        if len({o.descriptor.id for o in self.phase_outcomes}) != len(self.phase_outcomes):
            raise ValueError('Internal state cannot repeat phase evidence.')
        if self.preparation is not None and type(self.preparation) is not PreparedCompilationInput or type(self.artifacts) is not CompilationArtifactCollection:
            raise TypeError('Compiler state uses explicit preparation/artifact contracts, never a metadata bag.')


@dataclass(frozen=True, slots=True)
class CompilationPhaseResult:
    status: CompilationPhaseStatus
    diagnostics: tuple[CompilationDiagnostic, ...] = ()
    preparation: PreparedCompilationInput | None = None
    artifacts: tuple[CompilationArtifact, ...] = ()
    reason: str | None = None
    ir_envelopes: tuple['SemanticIREnvelope', ...] = ()

    def __post_init__(self) -> None:
        object.__setattr__(self, 'ir_envelopes', _ir_candidates(self.ir_envelopes))
        if type(self.status) is not CompilationPhaseStatus or type(self.diagnostics) not in (tuple, list) or any(type(d) is not CompilationDiagnostic for d in self.diagnostics):
            raise TypeError('Phase result requires explicit status and typed diagnostics.')
        object.__setattr__(self, 'diagnostics', tuple(self.diagnostics))
        object.__setattr__(self, 'artifacts', _artifacts(self.artifacts))
        if self.preparation is not None and type(self.preparation) is not PreparedCompilationInput:
            raise TypeError('Phase preparation must use its explicit contract.')
        if self.status is not CompilationPhaseStatus.COMPLETED:
            if self.artifacts or self.preparation is not None or self.ir_envelopes:
                raise ValueError('Failed/incomplete/skipped phase cannot expose successful outputs.')
            if type(self.reason) is not str or not self.reason:
                raise ValueError('Noncompleted phase requires an explicit reason.')
        if self.status is CompilationPhaseStatus.COMPLETED and any(d.severity is TypeValidationSeverity.ERROR for d in self.diagnostics):
            raise ValueError('A completed phase cannot carry a blocking error.')
        if self.status is CompilationPhaseStatus.SKIPPED and self.diagnostics:
            raise ValueError('Skipped phase cannot claim executed diagnostics.')
        if self.reason is not None and (type(self.reason) is not str or not self.reason):
            raise TypeError('Phase reason must be nonempty text.')


class CompilationPhase(Protocol):
    @property
    def descriptor(self) -> CompilationPhaseDescriptor:
        ...

    def execute(self, request: CompilationRequest, state: CompilationState) -> CompilationPhaseResult:
        ...


@dataclass(frozen=True, slots=True)
class CompilationPreparationPhase:
    descriptor: CompilationPhaseDescriptor = field(default_factory=lambda: CompilationPhaseDescriptor('CMP-PHASE-PREPARE', capabilities=frozenset({CompilationCapability.PREPARE}), targets=frozenset({PREPARATION_TARGET, BUILD_TARGET})), init=False)

    def execute(self, request: CompilationRequest, state: CompilationState) -> CompilationPhaseResult:
        if type(request) is not CompilationRequest or type(state) is not CompilationState:
            raise TypeError('Preparation consumes actual compiler request/state.')
        return CompilationPhaseResult(CompilationPhaseStatus.COMPLETED, preparation=PreparedCompilationInput(request.canonical_model, request.context))


@dataclass(frozen=True, slots=True)
class CompilationPhaseOutcome:
    descriptor: CompilationPhaseDescriptor
    status: CompilationPhaseStatus
    diagnostics: tuple[CompilationDiagnostic, ...] = ()
    reason: str | None = None
    executed: bool | None = None

    def __post_init__(self) -> None:
        if self.executed is not None and type(self.executed) is not bool or self.status is CompilationPhaseStatus.SKIPPED and self.executed is True:
            raise ValueError('Execution evidence must be explicit and cannot contradict skipped outcome.')
        if type(self.descriptor) is not CompilationPhaseDescriptor:
            raise TypeError('Phase outcome retains its actual descriptor.')
        result = CompilationPhaseResult(self.status, self.diagnostics, reason=self.reason)
        object.__setattr__(self, 'diagnostics', result.diagnostics)


@dataclass(frozen=True, slots=True)
class CompilationResult:
    status: CompilationStatus
    target: CompilationTargetId | None = None
    diagnostics: tuple[CompilationDiagnostic, ...] = ()
    phase_outcomes: tuple[CompilationPhaseOutcome, ...] = ()
    preparation: PreparedCompilationInput | None = None
    artifacts: CompilationArtifactCollection = field(default_factory=CompilationArtifactCollection)
    validation_evidence: ModelValidationResult | None = None
    diagnostic_context: ModelDiagnosticContext = field(default_factory=ModelDiagnosticContext)
    output_origin: 'CompilationOutputOrigin | None' = field(default=None, repr=False, compare=False, hash=False)

    def __post_init__(self) -> None:
        if type(self.status) is not CompilationStatus or self.target is not None and type(self.target) is not CompilationTargetId:
            raise TypeError('Compiler result requires explicit status/target.')
        for name, expected in (('diagnostics', CompilationDiagnostic), ('phase_outcomes', CompilationPhaseOutcome)):
            values = getattr(self, name)
            if type(values) not in (tuple, list) or any(type(v) is not expected for v in values):
                raise TypeError('Compiler result requires immutable typed outcome sequences.')
            object.__setattr__(self, name, tuple(values))
        if self.output_origin is not None:
            if type(self.output_origin) is not CompilationOutputOrigin:
                raise TypeError('Output origin must retain the actual compilation input/configuration binding.')
            original = self.output_origin.request
            if self.target != original.context.target or self.validation_evidence is not original.validation_evidence or self.preparation is not None and (self.preparation.model is not original.canonical_model or self.preparation.context != original.context):
                raise ValueError('Compilation output origin cannot contradict actual target/input/evidence.')
        if type(self.artifacts) is not CompilationArtifactCollection or type(self.diagnostic_context) is not ModelDiagnosticContext:
            raise TypeError('Compiler result output/report contracts must be typed.')
        if self.validation_evidence is not None and type(self.validation_evidence) is not ModelValidationResult:
            raise TypeError('Compiler result preserves original actual validation evidence.')
        if len({o.descriptor.id for o in self.phase_outcomes}) != len(self.phase_outcomes):
            raise ValueError('Compiler phase outcomes cannot duplicate an ID.')
        diagnostic_membership = Counter(id(d) for d in self.diagnostics)
        phase_membership = Counter(id(d) for o in self.phase_outcomes for d in o.diagnostics)
        if any(count > diagnostic_membership[identity] for identity, count in phase_membership.items()):
            raise ValueError('Compiler result must preserve every original phase diagnostic occurrence.')
        if self.status is CompilationStatus.SUCCEEDED:
            evidence = self.validation_evidence
            if type(self.preparation) is not PreparedCompilationInput or evidence is None or evidence.status is not ModelValidationStatus.VALID or evidence.readiness is not CompilationReadiness.READY or evidence.validated_model is not self.preparation.model:
                raise ValueError('Successful compiler result requires preparation and exact bound VALID/READY evidence.')
            if self.target != self.preparation.context.target or self.target not in (PREPARATION_TARGET, BUILD_TARGET) or not self.phase_outcomes or any(o.status is not CompilationPhaseStatus.COMPLETED for o in self.phase_outcomes) or any(d.severity is TypeValidationSeverity.ERROR for d in self.diagnostics):
                raise ValueError('Success requires a supported objective and all mandatory phases completed without errors.')
            capabilities = frozenset(c for o in self.phase_outcomes for c in o.descriptor.capabilities)
            if CompilationCapability.PREPARE not in capabilities or self.target == BUILD_TARGET and (CompilationCapability.EMIT_ARTIFACTS not in capabilities or not self.artifacts.artifacts) or self.target == PREPARATION_TARGET and self.artifacts.artifacts:
                raise ValueError('Successful target result must satisfy its declared capability/output objective.')
            if any(a.scope != self.preparation.context.scope or a.target != self.target.value or any(not self.preparation.model.contains(r) for r in a.semantic_dependencies) for a in self.artifacts.artifacts):
                raise ValueError('Successful artifact metadata must retain the actual input scope/target/exact membership.')
        elif self.preparation is not None or self.artifacts.artifacts:
            raise ValueError('Unsuccessful build cannot expose preparation/artifacts as successful outputs.')

    @property
    def diagnostic_report(self) -> CompilationDiagnosticReport:
        return CompilationDiagnosticReporter().report(self)

    @property
    def diagnostic_entries(self) -> tuple[ModelDiagnosticEntry, ...]:
        return self.diagnostic_report.entries


@dataclass(frozen=True, slots=True)
class ModelCompiler:
    additional_phases: tuple[CompilationPhase, ...] = ()
    _descriptors: tuple[CompilationPhaseDescriptor, ...] = field(init=False, repr=False)
    _configurations: tuple[tuple[tuple[str, object], ...], ...] = field(init=False, repr=False)
    _phase_types: tuple[type, ...] = field(init=False, repr=False)

    def __post_init__(self) -> None:
        if type(self.additional_phases) not in (tuple, list):
            _configuration_reject('Compiler composition requires an explicit ordered finite phase sequence; unordered/live collections are unsupported.')
        phases = tuple(self.additional_phases)
        descriptors = [CompilationPreparationPhase().descriptor]
        for phase in phases:
            descriptor = getattr(phase, 'descriptor', None)
            if type(descriptor) is not CompilationPhaseDescriptor or not callable(getattr(phase, 'execute', None)):
                raise TypeError('Compiler phase must implement the explicit descriptor/execute protocol.')
            descriptors.append(descriptor)
        ids = [d.id for d in descriptors]
        if len(set(ids)) != len(ids):
            _configuration_reject('Duplicate phases cannot replace mandatory preparation.')
        positions = {id: i for i, id in enumerate(ids)}
        for descriptor in descriptors:
            if any(p in positions and positions[p] >= positions[descriptor.id] for p in descriptor.prerequisites):
                _configuration_reject('Configured prerequisites must precede their consumer; no dependency scheduler/reordering.', descriptor.id)
        object.__setattr__(self, 'additional_phases', phases)
        configurations = tuple(_phase_configuration(phase, descriptor) for phase, descriptor in zip((CompilationPreparationPhase(), *phases), descriptors))
        object.__setattr__(self, '_descriptors', tuple(descriptors))
        object.__setattr__(self, '_configurations', configurations)
        object.__setattr__(self, '_phase_types', tuple(type(p) for p in self.phases))

    @property
    def phases(self) -> tuple[CompilationPhase, ...]:
        return (CompilationPreparationPhase(), *self.additional_phases)

    def _configuration_diagnostics(self) -> tuple[CompilationDiagnostic, ...]:
        diagnostics = []
        if type(self.additional_phases) is not tuple or len(self.additional_phases) + 1 != len(self._descriptors):
            return (_configuration_diagnostic(CompilationFailure.CONFIGURATION_CHANGED, 'Captured compiler phase composition changed after construction.'),)
        for phase, descriptor, captured, implementation in zip(self.phases, self._descriptors, self._configurations, self._phase_types):
            try:
                current = _phase_configuration(phase, descriptor)
            except CompilationConfigurationError:
                current = None
            if type(phase) is not implementation or current != captured:
                diagnostics.append(_configuration_diagnostic(CompilationFailure.CONFIGURATION_CHANGED, 'Configured phase descriptor or immutable options changed after compiler construction.', descriptor.id))
        return tuple(diagnostics)

    def compile(self, request: CompilationRequest) -> CompilationResult:
        if type(request) is not CompilationRequest:
            d = CompilationDiagnostic(CompilationFailure.INVALID_INPUT, 'Supply the actual canonical compilation request, never authoring source.', TypeValidationSeverity.ERROR)
            return CompilationResult(CompilationStatus.FAILED, diagnostics=(d,))
        evidence = request.validation_evidence
        context = ModelDiagnosticContext(request.context.scope, request.source_associations)
        diagnostics = []
        gate_status = None
        if request.context.scope != request.canonical_model.scope:
            diagnostics.append(CompilationDiagnostic(CompilationFailure.CONTEXT_MISMATCH, 'Compiler context differs from canonical scope.', TypeValidationSeverity.ERROR))
            gate_status = CompilationStatus.FAILED
        if evidence is None or evidence.status is not ModelValidationStatus.VALID or evidence.readiness is not CompilationReadiness.READY:
            invalid = evidence is not None and evidence.status is ModelValidationStatus.INVALID
            diagnostics.append(CompilationDiagnostic(CompilationFailure.VALIDATION_NOT_READY, 'Compilation requires explicitly supplied bound VALID/READY validation; no validation is rerun.', TypeValidationSeverity.ERROR if invalid else TypeValidationSeverity.WARNING))
            gate_status = CompilationStatus.FAILED if invalid or gate_status is CompilationStatus.FAILED else CompilationStatus.INCOMPLETE
        if evidence is not None:
            if evidence.validated_model is None:
                diagnostics.append(CompilationDiagnostic(CompilationFailure.VALIDATION_EVIDENCE_UNBOUND, 'Legacy/unbound validation evidence cannot establish the compiler input snapshot.', TypeValidationSeverity.WARNING))
                gate_status = gate_status or CompilationStatus.INCOMPLETE
            elif evidence.validated_model is not request.canonical_model:
                diagnostics.append(CompilationDiagnostic(CompilationFailure.MODEL_MISMATCH, 'Validation evidence belongs to another canonical object; context/count/membership/content similarity does not bind it.', TypeValidationSeverity.ERROR))
                gate_status = CompilationStatus.FAILED
        if request.context.target not in (PREPARATION_TARGET, BUILD_TARGET):
            diagnostics.append(CompilationDiagnostic(CompilationFailure.UNSUPPORTED_TARGET, 'Unknown target has no approved compiler objective/capability.', TypeValidationSeverity.WARNING))
            gate_status = gate_status or CompilationStatus.INCOMPLETE
        # Audit the entire captured composition before any phase executes.
        if gate_status is None:
            changed = self._configuration_diagnostics()
            if changed:
                diagnostics.extend(changed)
                gate_status = CompilationStatus.FAILED
        outcomes = []
        state = CompilationState()
        completed = set()
        capabilities = set()
        blocker = 'prerequisite gate' if gate_status is not None else None
        status = gate_status
        for phase, descriptor in zip(self.phases, self._descriptors):
            if blocker is not None:
                outcomes.append(CompilationPhaseOutcome(descriptor, CompilationPhaseStatus.SKIPPED, reason='Blocked by ' + blocker + '.', executed=False))
                continue
            missing = tuple(p for p in descriptor.prerequisites if p not in completed)
            if missing or request.context.target not in descriptor.targets:
                d = CompilationDiagnostic(CompilationFailure.PHASE_UNAVAILABLE, 'Required phase prerequisite or explicitly declared target support is unavailable.', TypeValidationSeverity.WARNING, descriptor.id)
                diagnostics.append(d)
                outcomes.append(CompilationPhaseOutcome(descriptor, CompilationPhaseStatus.INCOMPLETE, (d,), 'Phase prerequisites/target capability are unavailable.', executed=False))
                blocker, status = descriptor.id, CompilationStatus.INCOMPLETE
                continue
            result = phase.execute(request, state)
            if type(result) is not CompilationPhaseResult or any(d.phase_id is not None and d.phase_id != descriptor.id or d.association is not None and d.association.phase_id is not None and d.association.phase_id != descriptor.id for d in result.diagnostics):
                raise TypeError('Phase implementation violated its result/diagnostic origin contract.')
            diagnostics.extend(result.diagnostics)
            # Contract drift cannot be committed, even when output appears complete.
            changed = self._configuration_diagnostics()
            if changed:
                diagnostics.extend(changed)
                current = tuple(d for d in changed if d.phase_id == descriptor.id)
                if not current:
                    current = (_configuration_diagnostic(CompilationFailure.CONFIGURATION_CHANGED, 'Executing phase invalidated captured compiler configuration.', descriptor.id),)
                    diagnostics.extend(current)
                outcomes.append(CompilationPhaseOutcome(descriptor, CompilationPhaseStatus.FAILED, (*result.diagnostics, *current), 'Compiler configuration changed during execution.', executed=True))
                blocker, status = descriptor.id, CompilationStatus.FAILED
                continue
            if result.status is not CompilationPhaseStatus.COMPLETED:
                phase_diagnostics = result.diagnostics
                if result.status is CompilationPhaseStatus.FAILED and not any(d.severity is TypeValidationSeverity.ERROR for d in phase_diagnostics):
                    d = CompilationDiagnostic(CompilationFailure.PHASE_FAILED, 'Configured compiler phase explicitly failed.', TypeValidationSeverity.ERROR, descriptor.id)
                    diagnostics.append(d)
                    phase_diagnostics = (*phase_diagnostics, d)
                outcomes.append(CompilationPhaseOutcome(descriptor, result.status, phase_diagnostics, result.reason, executed=True))
                if result.status is CompilationPhaseStatus.FAILED or any(d.severity is TypeValidationSeverity.ERROR for d in result.diagnostics):
                    status = CompilationStatus.FAILED
                else:
                    status = CompilationStatus.INCOMPLETE
                blocker = descriptor.id
                continue
            preparation = result.preparation if result.preparation is not None else state.preparation
            if result.preparation is not None and (CompilationCapability.PREPARE not in descriptor.capabilities or preparation.model is not request.canonical_model or preparation.context != request.context):
                raise TypeError('Phase cannot replace canonical input/context or produce undeclared preparation.')
            if result.artifacts and (CompilationCapability.EMIT_ARTIFACTS not in descriptor.capabilities or request.context.target != BUILD_TARGET):
                raise TypeError('Phase produced artifacts outside the explicitly supported build capability.')
            if any(a.scope != request.context.scope or a.target != request.context.target.value or any(not request.canonical_model.contains(r) for r in a.semantic_dependencies) for a in result.artifacts):
                raise TypeError('Artifact scope/target disagrees with compilation contract.')
            try:
                ir_envelopes = _merge_ir(state.ir_envelopes, result.ir_envelopes, request, descriptor)
            except SemanticIREnvelopeError as failure:
                diagnostics.extend(failure.diagnostics)
                outcomes.append(CompilationPhaseOutcome(descriptor, CompilationPhaseStatus.FAILED, (*result.diagnostics, *failure.diagnostics), 'IR output handoff rejected.', executed=True))
                blocker, status = descriptor.id, CompilationStatus.FAILED
                continue
            try:
                artifacts = CompilationArtifactCollection((*state.artifacts.artifacts, *result.artifacts))
            except CompilationArtifactConflict as conflict:
                d = CompilationDiagnostic(CompilationFailure.ARTIFACT_CONFLICT, 'Duplicate artifact key conflicts with atomic deterministic output membership.', TypeValidationSeverity.ERROR, descriptor.id, association=CompilationDiagnosticAssociation(CompilationDiagnosticOrigin.ARTIFACT_COLLECTION, descriptor.id, artifact_target=CompilationArtifactTarget(key=conflict.key, target=request.context.target), related_targets=tuple(ModelDiagnosticTarget(ModelDiagnosticTargetKind.DEFINITION, r) for a in (*state.artifacts.artifacts, *result.artifacts) if a.key == conflict.key for r in a.semantic_dependencies)))
                diagnostics.append(d)
                outcomes.append(CompilationPhaseOutcome(descriptor, CompilationPhaseStatus.FAILED, (*result.diagnostics, d), 'Artifact key conflict.', executed=True))
                blocker, status = descriptor.id, CompilationStatus.FAILED
                continue
            outcome = CompilationPhaseOutcome(descriptor, CompilationPhaseStatus.COMPLETED, result.diagnostics, executed=True)
            outcomes.append(outcome)
            state = CompilationState(preparation, artifacts, ir_envelopes, tuple(outcomes))
            completed.add(descriptor.id)
            capabilities.update(descriptor.capabilities)
        if status is None and (state.preparation is None or request.context.target == BUILD_TARGET and (CompilationCapability.EMIT_ARTIFACTS not in capabilities or not state.artifacts.artifacts)):
            diagnostics.append(CompilationDiagnostic(CompilationFailure.INCOMPLETE_BUILD, 'Required target artifact generation/output is unavailable; preparation is not a compiled build.', TypeValidationSeverity.WARNING))
            status = CompilationStatus.INCOMPLETE
        status = status or CompilationStatus.SUCCEEDED
        return CompilationResult(status, request.context.target, diagnostics, outcomes, state.preparation if status is CompilationStatus.SUCCEEDED else None, state.artifacts if status is CompilationStatus.SUCCEEDED else CompilationArtifactCollection(), evidence, context, CompilationOutputOrigin(request, self))


__all__ = ['MODULE_NAME', 'CompilationStatus', 'CompilationPhaseStatus', 'CompilationCapability',
           'CompilationTargetId', 'PREPARATION_TARGET', 'BUILD_TARGET', 'CompilationFailure',
           'CompilationDiagnostic', 'CompilationContext', 'CompilationRequest', 'CompilationPhaseDescriptor',
           'PreparedCompilationInput', 'CompilationArtifactConflict', 'CompilationArtifactCollection',
           'CompilationState', 'CompilationPhaseResult', 'CompilationPhase', 'CompilationPreparationPhase',
           'CompilationPhaseOutcome', 'CompilationResult', 'ModelCompiler']


_LEGACY_DIAGNOSTIC_OWNERS = MappingProxyType({
    CompilationFailure.INVALID_INPUT: CompilationDiagnosticOrigin.PREREQUISITE,
    CompilationFailure.VALIDATION_NOT_READY: CompilationDiagnosticOrigin.PREREQUISITE,
    CompilationFailure.VALIDATION_EVIDENCE_UNBOUND: CompilationDiagnosticOrigin.PREREQUISITE,
    CompilationFailure.MODEL_MISMATCH: CompilationDiagnosticOrigin.PREREQUISITE,
    CompilationFailure.CONTEXT_MISMATCH: CompilationDiagnosticOrigin.PREREQUISITE,
    CompilationFailure.UNSUPPORTED_TARGET: CompilationDiagnosticOrigin.PREREQUISITE,
    CompilationFailure.PHASE_UNAVAILABLE: CompilationDiagnosticOrigin.ORCHESTRATOR,
    CompilationFailure.PHASE_FAILED: CompilationDiagnosticOrigin.PHASE,
    CompilationFailure.ARTIFACT_CONFLICT: CompilationDiagnosticOrigin.ARTIFACT_COLLECTION,
    CompilationFailure.INCOMPLETE_BUILD: CompilationDiagnosticOrigin.RESULT,
    CompilationFailure.IR_INVALID_ENVELOPE: CompilationDiagnosticOrigin.ORCHESTRATOR,
    CompilationFailure.IR_UNSUPPORTED_SCHEMA: CompilationDiagnosticOrigin.ORCHESTRATOR,
    CompilationFailure.IR_INVALID_IDENTITY: CompilationDiagnosticOrigin.ORCHESTRATOR,
    CompilationFailure.IR_CONTEXT_MISMATCH: CompilationDiagnosticOrigin.ORCHESTRATOR,
    CompilationFailure.IR_INPUT_MISMATCH: CompilationDiagnosticOrigin.ORCHESTRATOR,
    CompilationFailure.IR_UNSUPPORTED_KIND: CompilationDiagnosticOrigin.ORCHESTRATOR,
    CompilationFailure.IR_PAYLOAD_MISMATCH: CompilationDiagnosticOrigin.ORCHESTRATOR,
    CompilationFailure.IR_MISSING_PAYLOAD: CompilationDiagnosticOrigin.ORCHESTRATOR,
    CompilationFailure.IR_INCOMPATIBLE_HANDOFF: CompilationDiagnosticOrigin.ORCHESTRATOR,
    CompilationFailure.IR_DUPLICATE_IDENTITY: CompilationDiagnosticOrigin.ORCHESTRATOR,
    CompilationFailure.TYPE_IR_UNSUPPORTED_DEFINITION: CompilationDiagnosticOrigin.PHASE,
    CompilationFailure.TYPE_IR_MISSING_DATA_FACET: CompilationDiagnosticOrigin.PHASE,
    CompilationFailure.TYPE_IR_INVALID_FIELD: CompilationDiagnosticOrigin.PHASE,
    CompilationFailure.TYPE_IR_UNSUPPORTED_REFERENCE: CompilationDiagnosticOrigin.PHASE,
    CompilationFailure.TYPE_IR_UNSUPPORTED_CONSTRAINT: CompilationDiagnosticOrigin.PHASE,
    CompilationFailure.TYPE_IR_INPUT_MISMATCH: CompilationDiagnosticOrigin.PHASE,
    CompilationFailure.TYPE_IR_IDENTITY_COVERAGE: CompilationDiagnosticOrigin.PHASE,
    CompilationFailure.TYPE_IR_INVALID_PAYLOAD: CompilationDiagnosticOrigin.PHASE,
    CompilationFailure.NONDETERMINISTIC_CONFIGURATION: CompilationDiagnosticOrigin.ORCHESTRATOR,
    CompilationFailure.CONFIGURATION_CHANGED: CompilationDiagnosticOrigin.ORCHESTRATOR,
    CompilationFailure.MANIFEST_COMPILATION_NOT_SUCCESSFUL: CompilationDiagnosticOrigin.RESULT,
    CompilationFailure.MANIFEST_UNSUPPORTED_SCHEMA: CompilationDiagnosticOrigin.RESULT,
    CompilationFailure.MANIFEST_INVALID_IDENTITY: CompilationDiagnosticOrigin.RESULT,
    CompilationFailure.MANIFEST_CONTEXT_MISMATCH: CompilationDiagnosticOrigin.RESULT,
    CompilationFailure.MANIFEST_TARGET_MISMATCH: CompilationDiagnosticOrigin.RESULT,
    CompilationFailure.MANIFEST_SNAPSHOT_MISMATCH: CompilationDiagnosticOrigin.RESULT,
    CompilationFailure.MANIFEST_UNSUPPORTED_KIND: CompilationDiagnosticOrigin.RESULT,
    CompilationFailure.MANIFEST_OUTPUT_UNBOUND: CompilationDiagnosticOrigin.RESULT,
    CompilationFailure.MANIFEST_INCOMPLETE_METADATA: CompilationDiagnosticOrigin.RESULT,
    CompilationFailure.MANIFEST_UNKNOWN_DEPENDENCY: CompilationDiagnosticOrigin.RESULT,
    CompilationFailure.MANIFEST_DUPLICATE_ARTIFACT: CompilationDiagnosticOrigin.RESULT,
    CompilationFailure.MANIFEST_INCOMPLETE_OUTPUT: CompilationDiagnosticOrigin.RESULT,
    CompilationFailure.MANIFEST_IDENTITY_COLLISION: CompilationDiagnosticOrigin.RESULT,

})


@dataclass(frozen=True, slots=True)
class CompilationDiagnosticContext:
    """Optional occurrence-indexed caller evidence, not a registry/resolver."""
    associations: tuple[tuple[int, CompilationDiagnosticAssociation], ...] = ()

    def __post_init__(self) -> None:
        if type(self.associations) not in (tuple, list):
            raise TypeError('Association overrides require an ordered finite sequence.')
        values = []
        for pair in self.associations:
            if type(pair) not in (tuple, list) or len(pair) != 2 or type(pair[0]) is not int or pair[0] < 0 or type(pair[1]) is not CompilationDiagnosticAssociation:
                raise TypeError('Associate each compiler diagnostic by its nonnegative occurrence index.')
            values.append(tuple(pair))
        if len({i for i, _ in values}) != len(values):
            raise ValueError('Conflicting evidence for one diagnostic occurrence is not last-write-wins.')
        object.__setattr__(self, 'associations', tuple(values))


@dataclass(frozen=True, slots=True)
class CompilationDiagnosticEntry:
    """Compiler association wrapper; scalar semantics stay on original diagnostic."""
    diagnostic: CompilationDiagnostic
    association: CompilationDiagnosticAssociation

    def __post_init__(self) -> None:
        if type(self.diagnostic) is not CompilationDiagnostic or type(self.association) is not CompilationDiagnosticAssociation:
            raise TypeError('Entry composes actual immutable diagnostic and bounded association.')
        d, a = self.diagnostic, self.association
        if d.association is not None and d.association != a or d.phase_id is not None and d.phase_id != a.phase_id or d.reference is not None and a.semantic_target is not None and d.reference != a.semantic_target.reference:
            raise ValueError('Caller enrichment cannot replace existing producer evidence.')

    def model_entry(self, context: ModelDiagnosticContext) -> ModelDiagnosticEntry:
        if type(context) is not ModelDiagnosticContext:
            raise TypeError('Reuse MOD-09 canonical source associations.')
        a, d = self.association, self.diagnostic
        target = a.semantic_target
        if target is None and d.reference is not None:
            target = ModelDiagnosticTarget(ModelDiagnosticTargetKind.DEFINITION, d.reference)
        path = a.source_path if a.source_path is not None else context.source_path(target)
        related_paths = a.related_paths if a.related_paths else tuple(path for t in a.related_targets if (path := context.source_path(t)) is not None)
        details = CompilationDiagnosticDetails(a.origin, a.phase_id, None if a.artifact_target is None else a.artifact_target.diagnostic_view, a.semantic_context, None if a.ir_identity is None else a.ir_identity.value)
        return ModelDiagnosticEntry(d, target, a.related_targets, path, related_paths, extension_origin=ModelDiagnosticOrigin.COMPILER, compilation_details=details)


@dataclass(frozen=True, slots=True)
class CompilationDiagnosticReporter:
    def report(self, result: CompilationResult, context: CompilationDiagnosticContext | None = None) -> CompilationDiagnosticReport:
        if type(result) is not CompilationResult or context is not None and type(context) is not CompilationDiagnosticContext:
            raise TypeError('Reporting accepts the original compiler result and optional typed associations.')
        overrides = {} if context is None else dict(context.associations)
        if any(i >= len(result.diagnostics) for i in overrides):
            raise ValueError('Association occurrence is outside the original result.')
        # Phase ownership uses occurrence identity and producer outcome order, not text/equality deduplication.
        owners = {}
        occurrences: dict[int, deque[int]] = {}
        for index, diagnostic in enumerate(result.diagnostics):
            occurrences.setdefault(id(diagnostic), deque()).append(index)
        for outcome in result.phase_outcomes:
            for diagnostic in outcome.diagnostics:
                slots = occurrences.get(id(diagnostic))
                if not slots:
                    raise ValueError('Phase diagnostics require original occurrence identity in the compiler result.')
                owners[slots.popleft()] = outcome
        phases = {o.descriptor.id: o for o in result.phase_outcomes}
        validation = () if result.validation_evidence is None else tuple(associate_model_diagnostic(d, result.diagnostic_context) for d in result.validation_evidence.diagnostics)
        compiler = []
        for i, diagnostic in enumerate(result.diagnostics):
            owner = owners.get(i)
            association = overrides.get(i, diagnostic.association)
            if association is None:
                phase_id = diagnostic.phase_id if diagnostic.phase_id is not None else None if owner is None else owner.descriptor.id
                origin = _LEGACY_DIAGNOSTIC_OWNERS[diagnostic.code]
                if origin is CompilationDiagnosticOrigin.PREREQUISITE and owner is not None:
                    origin = CompilationDiagnosticOrigin.PHASE
                association = CompilationDiagnosticAssociation(origin, phase_id, semantic_context=result.diagnostic_context.semantic_context)
            if association.phase_id is not None:
                outcome = phases.get(association.phase_id)
                if outcome is None or owner is not None and outcome is not owner:
                    raise ValueError('Phase association must refer to the actual producer outcome.')
                if association.origin in (CompilationDiagnosticOrigin.PHASE, CompilationDiagnosticOrigin.ARTIFACT_CONSTRUCTION) and (outcome.status is CompilationPhaseStatus.SKIPPED or outcome.executed is False):
                    raise ValueError('Nonexecuted phase cannot own an execution diagnostic.')
            compiler.append(CompilationDiagnosticEntry(diagnostic, association).model_entry(result.diagnostic_context))
        # CMP-01 emission order is authoritative; preserve every occurrence, validation remains first.
        phase_views = tuple(CompilerPhaseDiagnosticView(o.descriptor.id, o.status.value, o.reason, o.descriptor.prerequisites, o.executed) for o in result.phase_outcomes)
        return CompilationDiagnosticReport(result.status.value, None if result.target is None else result.target.value, (*validation, *compiler), phase_views, result.validation_evidence, len(result.artifacts.artifacts))


__all__ += ['CompilationDiagnosticOrigin', 'CompilationArtifactTarget',
            'CompilationDiagnosticAssociation', 'CompilationDiagnosticContext',
            'CompilationDiagnosticEntry', 'CompilationDiagnosticReporter']


class SemanticIREnvelopeError(ValueError):
    """Expected intrinsic/handoff rejection with existing compiler diagnostics."""
    def __init__(self, diagnostics: tuple[CompilationDiagnostic, ...]) -> None:
        if type(diagnostics) is not tuple or not diagnostics or any(type(d) is not CompilationDiagnostic for d in diagnostics):
            raise TypeError('IR failure retains actual nonempty diagnostic evidence.')
        self.diagnostics = diagnostics
        super().__init__('Semantic IR contract rejected; inspect structured compiler diagnostics.')

    def phase_failure(self, phase_id: str | None = None) -> CompilationPhaseResult:
        if phase_id is not None:
            _phase_id(phase_id)
        diagnostics = []
        for diagnostic in self.diagnostics:
            if phase_id is not None and diagnostic.phase_id is not None and diagnostic.phase_id != phase_id:
                raise ValueError('Failure adapter cannot replace original consumer phase evidence.')
            if phase_id is not None and diagnostic.phase_id is None:
                association = CompilationDiagnosticAssociation(CompilationDiagnosticOrigin.ORCHESTRATOR, phase_id) if diagnostic.association is None else replace(diagnostic.association, phase_id=phase_id)
                diagnostic = replace(diagnostic, phase_id=phase_id, association=association)
            diagnostics.append(diagnostic)
        return CompilationPhaseResult(CompilationPhaseStatus.FAILED, tuple(diagnostics), reason='Mandatory IR input or output contract rejected.')


def _ir_reject(code: CompilationFailure, message: str, *, identity: 'SemanticIRId | None' = None, phase_id: str | None = None, scope: SemanticContextRef | None = None, reference: ElementVersionRef | None = None) -> None:
    target = None if reference is None else ModelDiagnosticTarget(ModelDiagnosticTargetKind.DEFINITION, reference)
    association = CompilationDiagnosticAssociation(CompilationDiagnosticOrigin.ORCHESTRATOR, phase_id, semantic_target=target, semantic_context=scope, ir_identity=identity)
    raise SemanticIREnvelopeError((CompilationDiagnostic(code, message, TypeValidationSeverity.ERROR, phase_id, reference, association=association),))


@dataclass(frozen=True, slots=True, order=True)
class SemanticIRId:
    """Explicit representation token scoped to one accepted compilation request."""
    value: str

    def __post_init__(self) -> None:
        if type(self.value) is not str or len(self.value) > 160 or re.fullmatch(r'ir-[a-z][a-z0-9]*(?:[.-][a-z0-9]+)*', self.value) is None:
            _ir_reject(CompilationFailure.IR_INVALID_IDENTITY, 'IR identity requires a bounded explicit ir- representation token.')


class SemanticIRSchemaVersion(Enum):
    V0 = '0'


class SemanticIRPayloadKind(Enum):
    FOUNDATION_COORDINATES = 'foundation-coordinates'
    COMPILED_TYPE_IR = 'compiled-type-ir'


@dataclass(frozen=True, slots=True)
class SemanticIRFoundationPayload:
    """Explicit input-coordinate inventory, not lowered Type IR or executable content."""
    definitions: tuple[ElementVersionRef, ...]

    def __post_init__(self) -> None:
        if type(self.definitions) not in (tuple, list) or any(type(r) is not ElementVersionRef or type(r.element_id) is not SemanticElementId or type(r.version) is not SemanticVersion for r in self.definitions):
            _ir_reject(CompilationFailure.IR_PAYLOAD_MISMATCH, 'Foundation payload requires a finite ordered exact-reference sequence.')
        values = tuple(self.definitions)
        if len(set(values)) != len(values):
            _ir_reject(CompilationFailure.IR_PAYLOAD_MISMATCH, 'Foundation coordinates cannot repeat an exact definition.')
        object.__setattr__(self, 'definitions', values)

    @property
    def kind(self) -> SemanticIRPayloadKind:
        return SemanticIRPayloadKind.FOUNDATION_COORDINATES


# Reuse existing closed immutable references/constraints without redundant wrappers.
CompiledTypeReferenceIR = TypeRef
CompiledFieldConstraintsIR = FieldConstraintSet


@dataclass(frozen=True, slots=True)
class CompiledFieldIR:
    id: FieldId
    name: FieldName
    type: CompiledTypeReferenceIR
    constraints: CompiledFieldConstraintsIR

    def __post_init__(self) -> None:
        if type(self.id) is not FieldId or type(self.name) is not FieldName:
            _ir_reject(CompilationFailure.TYPE_IR_INVALID_FIELD, 'Compiled field retains exact owned FieldId and FieldName values.')
        if type(self.type) not in (PrimitiveTypeRef, SemanticTypeRef):
            _ir_reject(CompilationFailure.TYPE_IR_UNSUPPORTED_REFERENCE, 'Compiled field uses only the two approved TYPE-05 reference variants.')
        if type(self.type) is PrimitiveTypeRef and type(self.type.primitive) is not PrimitiveType or type(self.type) is SemanticTypeRef and (type(self.type.target) is not ElementRef or type(self.type.target.element_id) is not SemanticElementId):
            _ir_reject(CompilationFailure.TYPE_IR_UNSUPPORTED_REFERENCE, 'Compiled reference retains actual immutable Kernel primitive or identity-only element reference.')
        if type(self.constraints) is not FieldConstraintSet:
            _ir_reject(CompilationFailure.TYPE_IR_UNSUPPORTED_CONSTRAINT, 'Compiled constraints reuse the closed immutable TYPE-04 contract.')


@dataclass(frozen=True, slots=True)
class CompiledTypeIR:
    type_identity: ElementVersionRef
    qualified_name: QualifiedName
    semantic_context: SemanticContextRef
    fields: tuple[CompiledFieldIR, ...]

    def __post_init__(self) -> None:
        if type(self.type_identity) is not ElementVersionRef or type(self.type_identity.element_id) is not SemanticElementId or type(self.type_identity.version) is not SemanticVersion or type(self.qualified_name) is not QualifiedName or type(self.semantic_context) is not SemanticContextRef or type(self.semantic_context.context_id) is not SemanticElementId:
            _ir_reject(CompilationFailure.TYPE_IR_INVALID_PAYLOAD, 'Compiled type requires exact source identity/version, qualified name and semantic scope.')
        if type(self.fields) not in (tuple, list) or any(type(f) is not CompiledFieldIR for f in self.fields):
            _ir_reject(CompilationFailure.TYPE_IR_INVALID_FIELD, 'Compiled type fields require an explicit ordered immutable snapshot sequence.', reference=self.type_identity)
        fields = tuple(self.fields)
        # Reuse DataFacet intrinsic uniqueness/portability guarantees, never TYPE-06 applicability rules.
        try:
            DataFacet(tuple(FieldDefinition(f.id, f.name, f.type, f.constraints) for f in fields))
        except DataFacetError as failure:
            association = CompilationDiagnosticAssociation(CompilationDiagnosticOrigin.ORCHESTRATOR, semantic_target=ModelDiagnosticTarget(ModelDiagnosticTargetKind.DEFINITION, self.type_identity))
            diagnostic = CompilationDiagnostic(CompilationFailure.TYPE_IR_INVALID_FIELD, 'Compiled field collection violates existing intrinsic DataFacet membership.', TypeValidationSeverity.ERROR, reference=self.type_identity, cause_code=failure.code, association=association)
            raise SemanticIREnvelopeError((diagnostic,)) from failure
        object.__setattr__(self, 'fields', fields)

    @property
    def kind(self) -> SemanticIRPayloadKind:
        return SemanticIRPayloadKind.COMPILED_TYPE_IR


# Explicit closed extension; no plugin registry or arbitrary immutable implementation.
SemanticIRPayload = SemanticIRFoundationPayload | CompiledTypeIR


@dataclass(frozen=True, slots=True, eq=False)
class SemanticIRCanonicalInput:
    """Original in-process snapshot/evidence binding; not a semantic equality/hash."""
    request: CompilationRequest
    __hash__ = None

    def __post_init__(self) -> None:
        if type(self.request) is not CompilationRequest:
            _ir_reject(CompilationFailure.IR_INPUT_MISMATCH, 'IR must retain the actual canonical compilation request.')
        request = self.request
        evidence = request.validation_evidence
        if request.canonical_model.scope != request.context.scope:
            _ir_reject(CompilationFailure.IR_CONTEXT_MISMATCH, 'Canonical input scope disagrees with compiler context.', scope=request.context.scope)
        if request.context.target not in (PREPARATION_TARGET, BUILD_TARGET) or evidence is None or evidence.status is not ModelValidationStatus.VALID or evidence.readiness is not CompilationReadiness.READY or evidence.validated_model is not request.canonical_model:
            _ir_reject(CompilationFailure.IR_INPUT_MISMATCH, 'IR input association requires original bound VALID/READY evidence and supported compiler context.', scope=request.context.scope)

    def __eq__(self, other: object) -> bool:
        if type(other) is not SemanticIRCanonicalInput:
            return NotImplemented
        return self.request is other.request


@dataclass(frozen=True, slots=True)
class SemanticIREnvelope:
    identity: SemanticIRId
    schema_version: SemanticIRSchemaVersion
    semantic_context: SemanticContextRef
    canonical_input: SemanticIRCanonicalInput
    payload_kind: SemanticIRPayloadKind
    payload: SemanticIRPayload
    definition_origins: tuple[ElementVersionRef, ...]
    model_wide: bool = False
    produced_by_phase: str | None = None
    source_associations: tuple[CanonicalSourceAssociation, ...] = ()
    __hash__ = None

    def __post_init__(self) -> None:
        if type(self.identity) is not SemanticIRId:
            _ir_reject(CompilationFailure.IR_INVALID_IDENTITY, 'IR uses its own explicit representation identity.')
        identity = self.identity
        if self.schema_version is not SemanticIRSchemaVersion.V0:
            _ir_reject(CompilationFailure.IR_UNSUPPORTED_SCHEMA, 'Only explicitly declared IR envelope schema 0 is supported.', identity=identity)
        if type(self.semantic_context) is not SemanticContextRef or type(self.semantic_context.context_id) is not SemanticElementId:
            _ir_reject(CompilationFailure.IR_CONTEXT_MISMATCH, 'IR scope requires the existing typed semantic context.', identity=identity)
        if type(self.canonical_input) is not SemanticIRCanonicalInput:
            _ir_reject(CompilationFailure.IR_INPUT_MISMATCH, 'IR requires an actual validated canonical input association.', identity=identity)
        request = self.canonical_input.request
        if self.semantic_context != request.context.scope:
            _ir_reject(CompilationFailure.IR_CONTEXT_MISMATCH, 'IR scope differs from its declared canonical input.', identity=identity, scope=self.semantic_context)
        if type(self.payload_kind) is not SemanticIRPayloadKind:
            _ir_reject(CompilationFailure.IR_UNSUPPORTED_KIND, 'IR kind must be an explicitly supported discriminator.', identity=identity)
        if self.payload is None:
            _ir_reject(CompilationFailure.IR_MISSING_PAYLOAD, 'Mandatory IR payload cannot be absent.', identity=identity)
        expected_payload = SemanticIRFoundationPayload if self.payload_kind is SemanticIRPayloadKind.FOUNDATION_COORDINATES else CompiledTypeIR
        if type(self.payload) is not expected_payload:
            _ir_reject(CompilationFailure.IR_PAYLOAD_MISMATCH, 'IR does not accept mutable bags, arbitrary implementations or artifact payloads.', identity=identity)
        if type(self.model_wide) is not bool or type(self.definition_origins) not in (tuple, list) or any(type(r) is not ElementVersionRef or type(r.element_id) is not SemanticElementId or type(r.version) is not SemanticVersion for r in self.definition_origins):
            _ir_reject(CompilationFailure.IR_INVALID_ENVELOPE, 'Origins require explicit exact references and a boolean model-wide declaration.', identity=identity)
        origins = tuple(self.definition_origins)
        if len(set(origins)) != len(origins) or not origins and not self.model_wide:
            _ir_reject(CompilationFailure.IR_PAYLOAD_MISMATCH, 'Origins cannot repeat and absent origins require explicit model-wide scope.', identity=identity)
        if self.payload_kind is SemanticIRPayloadKind.FOUNDATION_COORDINATES:
            if origins != self.payload.definitions:
                _ir_reject(CompilationFailure.IR_PAYLOAD_MISMATCH, 'Foundation payload retains the exact ordered origin coordinates.', identity=identity)
        elif self.model_wide or origins != (self.payload.type_identity,) or self.payload.semantic_context != self.semantic_context:
            _ir_reject(CompilationFailure.IR_PAYLOAD_MISMATCH, 'Compiled type payload requires one exact source origin and matching scope.', identity=identity)
        for reference in origins:
            if not request.canonical_model.contains(reference):
                _ir_reject(CompilationFailure.IR_INPUT_MISMATCH, 'IR origin is outside its exact canonical snapshot.', identity=identity, reference=reference)
        if self.payload_kind is SemanticIRPayloadKind.COMPILED_TYPE_IR:
            definition = request.canonical_model.find(self.payload.type_identity)
            if definition.data is None or definition.type_definition.qualified_name != self.payload.qualified_name or len(definition.data.fields) != len(self.payload.fields) or any((f.id, f.name, f.type, f.constraints) != (original.id, original.name, original.type, original.constraints) for f, original in zip(self.payload.fields, definition.data.fields)):
                _ir_reject(CompilationFailure.IR_INPUT_MISMATCH, 'Compiled payload must preserve the exact original canonical data structure and name.', identity=identity, reference=self.payload.type_identity)
        if self.produced_by_phase is not None and (type(self.produced_by_phase) is not str or re.fullmatch(r'CMP-PHASE-[A-Z0-9]+(?:-[A-Z0-9]+)*', self.produced_by_phase) is None):
            _ir_reject(CompilationFailure.IR_INCOMPATIBLE_HANDOFF, 'Optional candidate producer uses an existing compiler phase identifier.', identity=identity)
        if type(self.source_associations) not in (tuple, list) or any(type(a) is not CanonicalSourceAssociation for a in self.source_associations):
            _ir_reject(CompilationFailure.IR_INVALID_ENVELOPE, 'Source provenance seam uses actual canonical source associations.', identity=identity)
        associations = tuple(self.source_associations)
        if any(a not in request.source_associations or a.target.definition not in origins for a in associations):
            _ir_reject(CompilationFailure.IR_INPUT_MISMATCH, 'IR source associations must come from original request and declared exact origins.', identity=identity)
        object.__setattr__(self, 'definition_origins', origins)
        object.__setattr__(self, 'source_associations', associations)


@dataclass(frozen=True, slots=True)
class SemanticIREnvelopeFactory:
    def create(self, *, identity: SemanticIRId, schema_version: SemanticIRSchemaVersion, canonical_input: SemanticIRCanonicalInput, semantic_context: SemanticContextRef, payload_kind: SemanticIRPayloadKind, payload: SemanticIRPayload, definition_origins: tuple[ElementVersionRef, ...], model_wide: bool = False, produced_by_phase: str | None = None, source_associations: tuple[CanonicalSourceAssociation, ...] = ()) -> SemanticIREnvelope:
        return SemanticIREnvelope(identity, schema_version, semantic_context, canonical_input, payload_kind, payload, definition_origins, model_wide, produced_by_phase, source_associations)


def _ir_candidates(values: tuple[SemanticIREnvelope, ...]) -> tuple[SemanticIREnvelope, ...]:
    if type(values) not in (tuple, list) or any(type(e) is not SemanticIREnvelope for e in values):
        _ir_reject(CompilationFailure.IR_INVALID_ENVELOPE, 'Phase IR output is an explicit finite sequence of actual envelopes.')
    return tuple(values)


def _ir_values(values: tuple[SemanticIREnvelope, ...]) -> tuple[SemanticIREnvelope, ...]:
    envelopes = _ir_candidates(values)
    seen = set()
    for envelope in envelopes:
        if envelope.identity in seen:
            _ir_reject(CompilationFailure.IR_DUPLICATE_IDENTITY, 'Duplicate IR representation identity; no overwrite or equality exemption.', identity=envelope.identity)
        seen.add(envelope.identity)
    return tuple(sorted(envelopes, key=lambda e: e.identity.value))


def _ir_current(envelope: SemanticIREnvelope, request: CompilationRequest, phase_id: str | None = None) -> None:
    if type(envelope) is not SemanticIREnvelope or type(request) is not CompilationRequest:
        _ir_reject(CompilationFailure.IR_INVALID_ENVELOPE, 'Handoff accepts actual typed envelope and compilation request.', phase_id=phase_id)
    original = envelope.canonical_input.request
    if envelope.semantic_context != request.context.scope or original.context != request.context:
        _ir_reject(CompilationFailure.IR_CONTEXT_MISMATCH, 'IR target/context is incompatible with current compilation.', identity=envelope.identity, phase_id=phase_id, scope=request.context.scope)
    if original is not request:
        _ir_reject(CompilationFailure.IR_INPUT_MISMATCH, 'IR representation belongs to another compilation request, even if snapshots appear equal.', identity=envelope.identity, phase_id=phase_id, scope=request.context.scope)


def _merge_ir(existing: tuple[SemanticIREnvelope, ...], candidates: tuple[SemanticIREnvelope, ...], request: CompilationRequest, producer: CompilationPhaseDescriptor) -> tuple[SemanticIREnvelope, ...]:
    if candidates and CompilationCapability.EMIT_IR not in producer.capabilities:
        _ir_reject(CompilationFailure.IR_INCOMPATIBLE_HANDOFF, 'Phase cannot emit IR without explicit descriptor capability.', phase_id=producer.id)
    seen = {e.identity for e in existing}
    for envelope in candidates:
        _ir_current(envelope, request, producer.id)
        if envelope.produced_by_phase != producer.id:
            _ir_reject(CompilationFailure.IR_INCOMPATIBLE_HANDOFF, 'Candidate must declare its actual producing phase at commit boundary.', identity=envelope.identity, phase_id=producer.id)
        if envelope.identity in seen:
            _ir_reject(CompilationFailure.IR_DUPLICATE_IDENTITY, 'IR output collides with existing or same-phase representation identity.', identity=envelope.identity, phase_id=producer.id)
        seen.add(envelope.identity)
    return _ir_values((*existing, *candidates))


@dataclass(frozen=True, slots=True)
class SemanticIRHandoff:
    def require(self, envelope: SemanticIREnvelope, *, request: CompilationRequest, state: CompilationState, consumer: CompilationPhaseDescriptor, required_kind: SemanticIRPayloadKind, required_schema: SemanticIRSchemaVersion = SemanticIRSchemaVersion.V0) -> SemanticIREnvelope:
        if type(state) is not CompilationState or type(consumer) is not CompilationPhaseDescriptor:
            raise TypeError('Handoff requires actual compiler state and consumer descriptor.')
        _ir_current(envelope, request, consumer.id)
        if required_schema is not SemanticIRSchemaVersion.V0 or envelope.schema_version is not required_schema:
            _ir_reject(CompilationFailure.IR_UNSUPPORTED_SCHEMA, 'Consumer requires an unsupported or mismatched envelope schema.', identity=envelope.identity, phase_id=consumer.id)
        if type(required_kind) is not SemanticIRPayloadKind:
            _ir_reject(CompilationFailure.IR_UNSUPPORTED_KIND, 'Consumer payload contract is not implemented.', identity=envelope.identity, phase_id=consumer.id)
        if envelope.payload_kind is not required_kind:
            _ir_reject(CompilationFailure.IR_PAYLOAD_MISMATCH, 'Consumer does not accept the supplied IR payload contract.', identity=envelope.identity, phase_id=consumer.id)
        if request.context.target not in consumer.targets:
            _ir_reject(CompilationFailure.IR_INCOMPATIBLE_HANDOFF, 'Consumer descriptor does not support this compilation target.', identity=envelope.identity, phase_id=consumer.id)
        if state.preparation is None or state.preparation.model is not request.canonical_model or state.preparation.context != request.context:
            _ir_reject(CompilationFailure.IR_INPUT_MISMATCH, 'Handoff state must retain preparation for this exact current input/context.', identity=envelope.identity, phase_id=consumer.id)
        producer = next((o for o in state.phase_outcomes if o.descriptor.id == envelope.produced_by_phase), None)
        if not any(e is envelope for e in state.ir_envelopes) or producer is None or producer.status is not CompilationPhaseStatus.COMPLETED or producer.executed is not True or CompilationCapability.EMIT_IR not in producer.descriptor.capabilities or producer.descriptor.id == consumer.id or producer.descriptor.id not in consumer.prerequisites:
            _ir_reject(CompilationFailure.IR_INCOMPATIBLE_HANDOFF, 'Mandatory IR requires committed membership and completed executed producer evidence declared as a consumer prerequisite.', identity=envelope.identity, phase_id=consumer.id)
        return envelope


__all__ += ['SemanticIREnvelopeError', 'SemanticIRId', 'SemanticIRSchemaVersion',
            'SemanticIRPayloadKind', 'SemanticIRFoundationPayload', 'SemanticIRPayload',
            'SemanticIRCanonicalInput', 'SemanticIREnvelope', 'SemanticIREnvelopeFactory', 'SemanticIRHandoff']


COMPILED_TYPE_IR_PHASE = CompilationPhaseDescriptor(
    'CMP-PHASE-COMPILED-TYPE-IR', ('CMP-PHASE-PREPARE',),
    frozenset({CompilationCapability.EMIT_IR}), frozenset({PREPARATION_TARGET, BUILD_TARGET}),
)

# Reuse the existing atomic phase result, with successful payload carried in its envelope.
TypeLoweringResult = CompilationPhaseResult


def _type_ir_gate(request: CompilationRequest, state: CompilationState) -> SemanticIRCanonicalInput:
    if type(request) is not CompilationRequest or type(state) is not CompilationState:
        raise TypeError('Type lowering requires actual compiler request and state, never Boolean validation flags.')
    canonical_input = SemanticIRCanonicalInput(request)
    preparation = state.preparation
    outcome = next((o for o in state.phase_outcomes if o.descriptor.id == 'CMP-PHASE-PREPARE'), None)
    if preparation is None or preparation.model is not request.canonical_model or preparation.context != request.context or outcome is None or outcome.status is not CompilationPhaseStatus.COMPLETED or outcome.executed is not True or CompilationCapability.PREPARE not in outcome.descriptor.capabilities:
        _ir_reject(CompilationFailure.TYPE_IR_INPUT_MISMATCH, 'Type lowering requires matching accepted preparation and original executed mandatory phase evidence.', phase_id=COMPILED_TYPE_IR_PHASE.id, scope=request.context.scope)
    return canonical_input


def _type_ir_diagnostic(code: CompilationFailure, message: str, *, reference: ElementVersionRef | None = None, field_id: FieldId | None = None, severity: TypeValidationSeverity = TypeValidationSeverity.ERROR, cause_code: str | None = None, identity: SemanticIRId | None = None) -> CompilationDiagnostic:
    target = None if reference is None else ModelDiagnosticTarget(ModelDiagnosticTargetKind.DEFINITION if field_id is None else ModelDiagnosticTargetKind.FIELD, reference, field_id)
    association = CompilationDiagnosticAssociation(CompilationDiagnosticOrigin.PHASE, COMPILED_TYPE_IR_PHASE.id, semantic_target=target, ir_identity=identity)
    return CompilationDiagnostic(code, message, severity, COMPILED_TYPE_IR_PHASE.id, reference, cause_code, association)


@dataclass(frozen=True, slots=True)
class CompiledTypeLowerer:
    def lower_payload(self, definition: TypeDataComposition, *, request: CompilationRequest, state: CompilationState, identity: SemanticIRId) -> CompiledTypeIR | TypeLoweringResult:
        """Single-type lowering only; existing phase result represents expected failure."""
        try:
            _type_ir_gate(request, state)
        except SemanticIREnvelopeError as failure:
            return failure.phase_failure(COMPILED_TYPE_IR_PHASE.id)
        if type(identity) is not SemanticIRId:
            diagnostic = _type_ir_diagnostic(CompilationFailure.IR_INVALID_IDENTITY, 'Type lowering requires an explicit representation identity.')
            return CompilationPhaseResult(CompilationPhaseStatus.FAILED, (diagnostic,), reason='Invalid IR identity.')
        if type(definition) is not TypeDataComposition:
            diagnostic = _type_ir_diagnostic(CompilationFailure.TYPE_IR_UNSUPPORTED_DEFINITION, 'Only the existing canonical type/data composition is supported.', severity=TypeValidationSeverity.WARNING, identity=identity)
            return CompilationPhaseResult(CompilationPhaseStatus.INCOMPLETE, (diagnostic,), reason='Unsupported definition capability.')
        host = definition.type_definition
        reference = ElementVersionRef(host.id, host.version)
        if request.canonical_model.find(reference) is not definition or host.context != request.context.scope:
            diagnostic = _type_ir_diagnostic(CompilationFailure.TYPE_IR_INPUT_MISMATCH, 'Type must be the original exact member of the accepted canonical snapshot.', reference=reference, identity=identity)
            return CompilationPhaseResult(CompilationPhaseStatus.FAILED, (diagnostic,), reason='Canonical type association mismatch.')
        if host.kind != SemanticElementKinds.TYPE_DEFINITION:
            diagnostic = _type_ir_diagnostic(CompilationFailure.TYPE_IR_UNSUPPORTED_DEFINITION, 'Non-type semantic kinds have no compiled type lowering capability.', reference=reference, severity=TypeValidationSeverity.WARNING, identity=identity)
            return CompilationPhaseResult(CompilationPhaseStatus.INCOMPLETE, (diagnostic,), reason='Unsupported semantic kind.')
        if definition.data is None:
            diagnostic = _type_ir_diagnostic(CompilationFailure.TYPE_IR_MISSING_DATA_FACET, 'Absent DataFacet has no v0 structural type lowering capability; no empty facet is fabricated.', reference=reference, severity=TypeValidationSeverity.WARNING, identity=identity)
            return CompilationPhaseResult(CompilationPhaseStatus.INCOMPLETE, (diagnostic,), reason='DataFacet capability unavailable.')
        fields = []
        diagnostics = []
        for field_definition in definition.data.fields:
            try:
                fields.append(CompiledFieldIR(field_definition.id, field_definition.name, field_definition.type, field_definition.constraints))
            except SemanticIREnvelopeError as failure:
                for diagnostic in failure.diagnostics:
                    diagnostics.append(_type_ir_diagnostic(diagnostic.code, diagnostic.message, reference=reference, field_id=field_definition.id, cause_code=diagnostic.cause_code, identity=identity))
        if diagnostics:
            return CompilationPhaseResult(CompilationPhaseStatus.FAILED, tuple(diagnostics), reason='Mandatory field lowering rejected atomically.')
        try:
            payload = CompiledTypeIR(reference, host.qualified_name, host.context, tuple(fields))
        except SemanticIREnvelopeError as failure:
            return failure.phase_failure(COMPILED_TYPE_IR_PHASE.id)
        return payload

    def lower(self, definition: TypeDataComposition, *, request: CompilationRequest, state: CompilationState, identity: SemanticIRId) -> TypeLoweringResult:
        """Backward-compatible CMP-04 single-type envelope adapter."""
        payload = self.lower_payload(definition, request=request, state=state, identity=identity)
        if type(payload) is CompilationPhaseResult:
            return payload
        try:
            sources = tuple(a for a in request.source_associations if a.target.definition == payload.type_identity)
            envelope = SemanticIREnvelopeFactory().create(identity=identity, schema_version=SemanticIRSchemaVersion.V0, canonical_input=SemanticIRCanonicalInput(request), semantic_context=request.context.scope, payload_kind=SemanticIRPayloadKind.COMPILED_TYPE_IR, payload=payload, definition_origins=(payload.type_identity,), produced_by_phase=COMPILED_TYPE_IR_PHASE.id, source_associations=sources)
        except SemanticIREnvelopeError as failure:
            return failure.phase_failure(COMPILED_TYPE_IR_PHASE.id)
        return CompilationPhaseResult(CompilationPhaseStatus.COMPLETED, ir_envelopes=(envelope,))


@dataclass(frozen=True, slots=True)
class CompiledTypeIRIdentityBinding:
    definition: ElementVersionRef
    identity: SemanticIRId

    def __post_init__(self) -> None:
        if type(self.definition) is not ElementVersionRef or type(self.definition.element_id) is not SemanticElementId or type(self.definition.version) is not SemanticVersion or type(self.identity) is not SemanticIRId:
            raise TypeError('Representation assignment binds an explicit exact source coordinate to an existing IR token.')


def _type_pass_diagnostics(diagnostics: tuple[CompilationDiagnostic, ...], reference: ElementVersionRef, identity: SemanticIRId) -> tuple[CompilationDiagnostic, ...]:
    """Add only missing local type/IR context; retain existing field/cause evidence."""
    values = []
    for diagnostic in diagnostics:
        association = diagnostic.association
        if diagnostic.reference is not None and diagnostic.reference != reference or association is not None and association.semantic_target is not None and association.semantic_target.reference != reference:
            raise TypeError('Single-type failure diagnostic belongs to another canonical definition.')
        if association is None:
            association = CompilationDiagnosticAssociation(CompilationDiagnosticOrigin.PHASE, COMPILED_TYPE_IR_PHASE.id)
        target = association.semantic_target or ModelDiagnosticTarget(ModelDiagnosticTargetKind.DEFINITION, reference)
        if diagnostic.reference is None or association.semantic_target is None or association.ir_identity is None:
            association = replace(association, semantic_target=target, ir_identity=association.ir_identity or identity)
            diagnostic = replace(diagnostic, reference=reference, association=association)
        values.append(diagnostic)
    return tuple(values)


@dataclass(frozen=True, slots=True)
class TypeCompilerPass:
    """Canonical type orchestration; coordinator alone commits immutable state."""
    identities: tuple[CompiledTypeIRIdentityBinding, ...]
    descriptor: CompilationPhaseDescriptor = field(default=COMPILED_TYPE_IR_PHASE, init=False)

    def __post_init__(self) -> None:
        if type(self.identities) not in (tuple, list) or any(type(i) is not CompiledTypeIRIdentityBinding for i in self.identities):
            raise TypeError('Type phase requires explicit finite typed representation assignments.')
        identities = tuple(self.identities)
        if len({i.definition for i in identities}) != len(identities):
            raise ValueError('A source type cannot receive ambiguous representation assignments.')
        object.__setattr__(self, 'identities', tuple(sorted(identities, key=lambda i: (i.definition.element_id.value, i.definition.version.major, i.definition.version.minor, i.definition.version.patch))))

    def execute(self, request: CompilationRequest, state: CompilationState) -> CompilationPhaseResult:
        try:
            canonical_input = _type_ir_gate(request, state)
            for envelope in state.ir_envelopes:
                _ir_current(envelope, request, self.descriptor.id)
            if any(o.descriptor.id == self.descriptor.id for o in state.phase_outcomes) or any(e.produced_by_phase == self.descriptor.id for e in state.ir_envelopes):
                _ir_reject(CompilationFailure.IR_INCOMPATIBLE_HANDOFF, 'Type pass output slot is already occupied; rerun is not idempotent.', phase_id=self.descriptor.id)
        except SemanticIREnvelopeError as failure:
            return failure.phase_failure(self.descriptor.id)
        by_definition = {i.definition: i.identity for i in self.identities}
        definitions = tuple(d for d in request.canonical_model.list_definitions() if d.type_definition.kind == SemanticElementKinds.TYPE_DEFINITION)
        references = tuple(ElementVersionRef(d.type_definition.id, d.type_definition.version) for d in definitions)
        extra = tuple(sorted((i.definition for i in self.identities if not request.canonical_model.contains(i.definition)), key=lambda r: (r.element_id.value, r.version.major, r.version.minor, r.version.patch)))
        missing = tuple(r for r in references if r not in by_definition)
        if extra or missing:
            diagnostics = tuple(_type_ir_diagnostic(CompilationFailure.TYPE_IR_INPUT_MISMATCH, 'Representation assignment is outside current canonical membership.', reference=r) for r in extra) + tuple(_type_ir_diagnostic(CompilationFailure.TYPE_IR_IDENTITY_COVERAGE, 'A selected canonical type has no explicit representation identity.', reference=r, severity=TypeValidationSeverity.WARNING) for r in missing)
            return CompilationPhaseResult(CompilationPhaseStatus.FAILED if extra else CompilationPhaseStatus.INCOMPLETE, diagnostics, reason='Explicit representation coverage is unavailable or inconsistent.')
        candidates = []
        diagnostics = []
        statuses = []
        seen = {e.identity for e in state.ir_envelopes}
        occupied = {e.payload.type_identity for e in state.ir_envelopes if e.payload_kind is SemanticIRPayloadKind.COMPILED_TYPE_IR}
        for reference in references:
            identity = by_definition[reference]
            if identity in seen:
                diagnostics.append(_type_ir_diagnostic(CompilationFailure.IR_DUPLICATE_IDENTITY, 'Explicit type representation identity collides with existing or same-pass output.', reference=reference, identity=identity))
            if reference in occupied:
                diagnostics.append(_type_ir_diagnostic(CompilationFailure.IR_INCOMPATIBLE_HANDOFF, 'An exact compiled type output slot is already occupied.', reference=reference, identity=identity))
            seen.add(identity)
        if diagnostics:
            return CompilationPhaseResult(CompilationPhaseStatus.FAILED, tuple(diagnostics), reason='Type output identity or exact source slot conflict; no partial output.')
        lowerer = CompiledTypeLowerer()
        factory = SemanticIREnvelopeFactory()
        for definition in definitions:
            reference = ElementVersionRef(definition.type_definition.id, definition.type_definition.version)
            identity = by_definition[reference]
            result = lowerer.lower_payload(definition, request=request, state=state, identity=identity)
            if type(result) is CompilationPhaseResult:
                # A successful lowerer payload is mandatory, never an empty COMPLETED result.
                if result.status not in (CompilationPhaseStatus.FAILED, CompilationPhaseStatus.INCOMPLETE):
                    raise TypeError('Payload lowerer must return a compiled type or expected failed/incomplete phase result.')
                statuses.append(result.status)
                diagnostics.extend(_type_pass_diagnostics(result.diagnostics, reference, identity))
                continue
            if type(result) is not CompiledTypeIR:
                raise TypeError('Payload lowerer returned an unsupported result contract.')
            try:
                sources = tuple(a for a in request.source_associations if a.target.definition == reference)
                candidates.append(factory.create(identity=identity, schema_version=SemanticIRSchemaVersion.V0, canonical_input=canonical_input, semantic_context=request.context.scope, payload_kind=SemanticIRPayloadKind.COMPILED_TYPE_IR, payload=result, definition_origins=(reference,), produced_by_phase=self.descriptor.id, source_associations=sources))
            except SemanticIREnvelopeError as failure:
                rejected = failure.phase_failure(self.descriptor.id)
                statuses.append(rejected.status)
                diagnostics.extend(_type_pass_diagnostics(rejected.diagnostics, reference, identity))
                continue
            statuses.append(CompilationPhaseStatus.COMPLETED)
        if any(status is not CompilationPhaseStatus.COMPLETED for status in statuses):
            status = CompilationPhaseStatus.FAILED if CompilationPhaseStatus.FAILED in statuses else CompilationPhaseStatus.INCOMPLETE
            return CompilationPhaseResult(status, tuple(diagnostics), reason='One or more selected type definitions could not be lowered; no partial IR output.')
        try:
            # Preflight the actual commit contract; preserve canonical emission order.
            _merge_ir(state.ir_envelopes, tuple(candidates), request, self.descriptor)
        except SemanticIREnvelopeError as failure:
            return failure.phase_failure(self.descriptor.id)
        return CompilationPhaseResult(CompilationPhaseStatus.COMPLETED, tuple(diagnostics), ir_envelopes=tuple(candidates))


# One implementation/phase identity; old composition remains source compatible.
CompiledTypeLoweringPhase = TypeCompilerPass
TYPE_COMPILER_PASS_PHASE = COMPILED_TYPE_IR_PHASE


__all__ += ['CompiledTypeReferenceIR', 'CompiledFieldConstraintsIR', 'CompiledFieldIR',
            'CompiledTypeIR', 'COMPILED_TYPE_IR_PHASE', 'TypeLoweringResult',
            'CompiledTypeLowerer', 'CompiledTypeIRIdentityBinding', 'CompiledTypeLoweringPhase',
            'TypeCompilerPass', 'TYPE_COMPILER_PASS_PHASE']


# CMP-06: narrow immutable phase configuration, not a general metadata framework.
class CompilationConfigurationError(ValueError):
    def __init__(self, diagnostic: CompilationDiagnostic) -> None:
        self.diagnostics = (diagnostic,)
        super().__init__(diagnostic.message)


def _configuration_diagnostic(code: CompilationFailure, message: str, phase_id: str | None = None) -> CompilationDiagnostic:
    association = CompilationDiagnosticAssociation(CompilationDiagnosticOrigin.ORCHESTRATOR, phase_id)
    return CompilationDiagnostic(code, message, TypeValidationSeverity.ERROR, phase_id, association=association)


def _configuration_reject(message: str, phase_id: str | None = None) -> None:
    raise CompilationConfigurationError(_configuration_diagnostic(CompilationFailure.NONDETERMINISTIC_CONFIGURATION, message, phase_id))


def _configuration_value(value: object) -> bool:
    # Closed actual immutable values; no arbitrary recursive object traversal.
    if type(value) in (type(None), bool, int, str, bytes, CompilationPhaseDescriptor,
                       CompiledTypeIRIdentityBinding, SemanticIRId, CompilationTargetId,
                       ElementVersionRef, SemanticVersion, SemanticElementId,
                       SemanticContextRef, QualifiedName, FieldId, FieldName,
                       FieldConstraintSet, PrimitiveTypeRef, SemanticTypeRef):
        return True
    if type(value) in (CompilationCapability, CompilationPhaseStatus, CompilationStatus, SemanticIRPayloadKind, SemanticIRSchemaVersion):
        return True
    if type(value) is tuple:
        return all(_configuration_value(v) for v in value)
    return False


def _phase_configuration(phase: CompilationPhase, descriptor: CompilationPhaseDescriptor) -> tuple[tuple[str, object], ...]:
    if not is_dataclass(phase) or isinstance(phase, type) or not phase.__dataclass_params__.frozen:
        _configuration_reject('Configured phases must be frozen dataclass implementations with explicit immutable options.', descriptor.id)
    if phase.descriptor != descriptor:
        _configuration_reject('Configured phase descriptor differs from its captured declaration.', descriptor.id)
    values = tuple((f.name, getattr(phase, f.name)) for f in fields(phase))
    if any(not _configuration_value(value) for _, value in values):
        _configuration_reject('Phase options require approved immutable compiler values or immutable value sequences; live containers/services are unsupported.', descriptor.id)
    return values


def _diagnostic_semantics(diagnostic: CompilationDiagnostic) -> tuple[object, ...]:
    association = diagnostic.association
    targets = None if association is None else (
        association.origin, association.phase_id, association.semantic_target,
        association.artifact_target, association.related_targets,
        association.semantic_context, association.ir_identity,
        association.related_artifact_targets, association.manifest_identity,
        association.write_stage, association.output_location,
        association.read_stage, association.read_source_type,
    )
    # Message and source paths are presentation, never diagnostic ordering keys.
    return (diagnostic.code, diagnostic.severity, diagnostic.phase_id,
            diagnostic.reference, diagnostic.cause_code, targets)


def _outcome_semantics(outcome: CompilationPhaseOutcome) -> tuple[object, ...]:
    return (outcome.descriptor, outcome.status, outcome.executed,
            tuple(_diagnostic_semantics(d) for d in outcome.diagnostics))


@dataclass(frozen=True, slots=True)
class CompilationResultEquivalence:
    """Supported semantic comparison only; neither evidence authorization nor bytes."""
    def requests(self, left: CompilationRequest, right: CompilationRequest) -> bool:
        if type(left) is not CompilationRequest or type(right) is not CompilationRequest:
            raise TypeError('Input comparison requires actual compiler requests.')
        for request in (left, right):
            evidence = request.validation_evidence
            if evidence is None or evidence.status is not ModelValidationStatus.VALID or evidence.readiness is not CompilationReadiness.READY or evidence.validated_model is not request.canonical_model or request.canonical_model.scope != request.context.scope or request.context.target not in (PREPARATION_TARGET, BUILD_TARGET):
                return False
        return left.context == right.context and left.canonical_model.same_supported_content(right.canonical_model)

    def configurations(self, left: ModelCompiler, right: ModelCompiler) -> bool:
        if type(left) is not ModelCompiler or type(right) is not ModelCompiler:
            raise TypeError('Configuration comparison requires actual compiler compositions.')
        if left._configuration_diagnostics() or right._configuration_diagnostics():
            return False
        # Same in-process implementation classes, not a package version identity.
        return (tuple(type(p) for p in left.phases) == tuple(type(p) for p in right.phases)
                and left._descriptors == right._descriptors and left._configurations == right._configurations)

    def ir_envelopes(self, left: tuple[SemanticIREnvelope, ...], right: tuple[SemanticIREnvelope, ...]) -> bool:
        left, right = _ir_candidates(left), _ir_candidates(right)
        if len(left) != len(right):
            return False
        for a, b in zip(left, right):
            if not self.requests(a.canonical_input.request, b.canonical_input.request):
                return False
            if (a.identity, a.schema_version, a.semantic_context, a.payload_kind,
                a.payload, a.definition_origins, a.model_wide, a.produced_by_phase) != (
                b.identity, b.schema_version, b.semantic_context, b.payload_kind,
                b.payload, b.definition_origins, b.model_wide, b.produced_by_phase):
                return False
        return True

    def results(self, left: CompilationResult, right: CompilationResult) -> bool:
        """Compare compiler result observables; does not establish input equivalence."""
        if type(left) is not CompilationResult or type(right) is not CompilationResult:
            raise TypeError('Result comparison requires actual compiler results.')
        if left.artifacts.artifacts or right.artifacts.artifacts:
            raise ValueError('Concrete artifact payload equivalence is not implemented; metadata equality is insufficient.')
        if (left.status, left.target, left.diagnostic_context.semantic_context, tuple(_diagnostic_semantics(d) for d in left.diagnostics),
            tuple(_outcome_semantics(o) for o in left.phase_outcomes)) != (
            right.status, right.target, right.diagnostic_context.semantic_context, tuple(_diagnostic_semantics(d) for d in right.diagnostics),
            tuple(_outcome_semantics(o) for o in right.phase_outcomes)):
            return False
        if left.preparation is None or right.preparation is None:
            return left.preparation is right.preparation
        return (left.preparation.context == right.preparation.context
                and left.preparation.model.same_supported_content(right.preparation.model))

    def states(self, left: CompilationState, right: CompilationState) -> bool:
        if type(left) is not CompilationState or type(right) is not CompilationState:
            raise TypeError('State comparison requires actual compiler states.')
        if left.artifacts.artifacts or right.artifacts.artifacts:
            raise ValueError('Concrete artifact state equivalence is not implemented.')
        if tuple(_outcome_semantics(o) for o in left.phase_outcomes) != tuple(_outcome_semantics(o) for o in right.phase_outcomes):
            return False
        if left.preparation is None or right.preparation is None:
            prepared = left.preparation is right.preparation
        else:
            prepared = (left.preparation.context == right.preparation.context
                        and left.preparation.model.same_supported_content(right.preparation.model))
        return prepared and self.ir_envelopes(left.ir_envelopes, right.ir_envelopes)


__all__ += ['CompilationConfigurationError', 'CompilationResultEquivalence']


# CMP-07 retains input/configuration provenance without retaining artifact payloads.
@dataclass(frozen=True, slots=True, eq=False)
class CompilationOutputOrigin:
    request: CompilationRequest
    compiler: ModelCompiler
    __hash__ = None

    def __post_init__(self) -> None:
        if type(self.request) is not CompilationRequest or type(self.compiler) is not ModelCompiler:
            raise TypeError('Output origin uses the actual original request and compiler configuration.')


class RuntimeArtifactManifestError(ValueError):
    def __init__(self, diagnostics: tuple[CompilationDiagnostic, ...], status: CompilationStatus = CompilationStatus.FAILED) -> None:
        if type(diagnostics) not in (tuple, list) or not diagnostics or any(type(d) is not CompilationDiagnostic for d in diagnostics) or type(status) is not CompilationStatus or status not in (CompilationStatus.FAILED, CompilationStatus.INCOMPLETE):
            raise TypeError('Manifest rejection requires diagnostics and an existing non-success status.')
        self.diagnostics, self.status = tuple(diagnostics), status
        super().__init__('Runtime artifact manifest assembly rejected.')


def _manifest_diagnostic(code: CompilationFailure, message: str, *, identity: 'RuntimeArtifactManifestId | None' = None, key: CompilationArtifactKey | None = None, kind: CompilationArtifactKind | None = None, target: CompilationTargetId | None = None, reference: ElementVersionRef | None = None, dependency: CompilationArtifactKey | None = None, conflicts: tuple[RuntimeArtifactDescriptor, ...] = (), severity: TypeValidationSeverity = TypeValidationSeverity.ERROR) -> CompilationDiagnostic:
    artifact = None if key is None and kind is None and target is None else CompilationArtifactTarget(key, kind, target)
    semantic = None if reference is None else ModelDiagnosticTarget(ModelDiagnosticTargetKind.DEFINITION, reference)
    related = (() if dependency is None else (CompilationArtifactTarget(key=dependency, target=target),)) + tuple(CompilationArtifactTarget(key=d.key, kind=d.kind, target=target) for d in conflicts)
    origins = tuple(ModelDiagnosticTarget(ModelDiagnosticTargetKind.DEFINITION, r) for d in conflicts for r in d.metadata.semantic_origins)
    association = CompilationDiagnosticAssociation(CompilationDiagnosticOrigin.RESULT, semantic_target=semantic, artifact_target=artifact, related_targets=origins, related_artifact_targets=related, manifest_identity=identity)
    return CompilationDiagnostic(code, message, severity, reference=reference, association=association)


def _manifest_reject(code: CompilationFailure, message: str, **associations: object) -> None:
    raise RuntimeArtifactManifestError((_manifest_diagnostic(code, message, **associations),))


@dataclass(frozen=True, slots=True, order=True)
class RuntimeArtifactManifestId:
    value: str

    def __post_init__(self) -> None:
        if type(self.value) is not str or re.fullmatch(r'manifest-[a-z][a-z0-9]*(?:[.-][a-z0-9]+)*', self.value) is None or len(self.value) > 160:
            _manifest_reject(CompilationFailure.MANIFEST_INVALID_IDENTITY, 'Manifest identity requires an explicit independent bounded manifest token.')


class RuntimeArtifactManifestSchemaVersion(Enum):
    V0 = '0'


@dataclass(frozen=True, slots=True)
class RuntimeArtifactKindSupport:
    """Explicit application/compiler-owner approval of a concrete output contract."""
    kind: CompilationArtifactKind
    artifact_type: type

    def __post_init__(self) -> None:
        if type(self.kind) is not CompilationArtifactKind or not isinstance(self.artifact_type, type) or not is_dataclass(self.artifact_type) or not self.artifact_type.__dataclass_params__.frozen:
            _manifest_reject(CompilationFailure.MANIFEST_UNSUPPORTED_KIND, 'Runtime kind approval requires an existing kind and concrete immutable artifact class.')
        if not {'key', 'kind', 'scope', 'target', 'semantic_dependencies', 'manifest_metadata'} <= {f.name for f in fields(self.artifact_type)}:
            _manifest_reject(CompilationFailure.MANIFEST_INCOMPLETE_METADATA, 'Approved artifact contract must declare existing artifact metadata and explicit manifest_metadata fields.', kind=self.kind)


def _manifest_support(values: tuple[RuntimeArtifactKindSupport, ...]) -> tuple[RuntimeArtifactKindSupport, ...]:
    if type(values) not in (tuple, list) or any(type(v) is not RuntimeArtifactKindSupport for v in values):
        _manifest_reject(CompilationFailure.MANIFEST_UNSUPPORTED_KIND, 'Runtime artifact support must be an explicit finite typed approval sequence.')
    values = tuple(sorted(values, key=lambda v: v.kind.value))
    if len({v.kind for v in values}) != len(values):
        _manifest_reject(CompilationFailure.MANIFEST_UNSUPPORTED_KIND, 'Artifact kind approval cannot be ambiguous or repeated.')
    return values


def _runtime_descriptors(result: CompilationResult, request: CompilationRequest, support: tuple[RuntimeArtifactKindSupport, ...]) -> tuple[RuntimeArtifactDescriptor, ...]:
    allowed = {s.kind: s.artifact_type for s in support}
    descriptors, diagnostics = [], []
    for artifact in result.artifacts.artifacts:
        if artifact.kind not in allowed or type(artifact) is not allowed.get(artifact.kind):
            diagnostics.append(_manifest_diagnostic(CompilationFailure.MANIFEST_UNSUPPORTED_KIND, 'Actual emitted artifact kind/concrete contract has no explicit runtime-consumable approval.', key=artifact.key, kind=artifact.kind, target=request.context.target))
            continue
        metadata = artifact.manifest_metadata
        if type(metadata) is not RuntimeArtifactMetadata:
            diagnostics.append(_manifest_diagnostic(CompilationFailure.MANIFEST_INCOMPLETE_METADATA, 'Artifact has no actual closed immutable runtime manifest metadata.', key=artifact.key, kind=artifact.kind))
            continue
        invalid = tuple(r for r in metadata.semantic_origins if not request.canonical_model.contains(r))
        if invalid:
            diagnostics.extend(_manifest_diagnostic(CompilationFailure.MANIFEST_SNAPSHOT_MISMATCH, 'Artifact semantic origin is outside the exact validated canonical membership.', key=artifact.key, reference=r) for r in invalid)
            continue
        descriptors.append(RuntimeArtifactDescriptor(artifact.key, artifact.kind, metadata))
    if diagnostics:
        raise RuntimeArtifactManifestError(tuple(diagnostics))
    return tuple(descriptors)


def _manifest_inventory(values: tuple[RuntimeArtifactDescriptor, ...]) -> tuple[RuntimeArtifactDescriptor, ...]:
    if type(values) not in (tuple, list) or any(type(v) is not RuntimeArtifactDescriptor for v in values):
        _manifest_reject(CompilationFailure.MANIFEST_INCOMPLETE_METADATA, 'Manifest inventory requires finite actual immutable descriptors, never artifacts or IR.')
    # Extra keys resolve invalid duplicate diagnostic order only; valid inventory still uses artifact key order.
    values = tuple(sorted(values, key=lambda v: (v.key.value, v.kind.value, tuple((r.element_id.value, r.version.major, r.version.minor, r.version.patch) for r in v.metadata.semantic_origins), v.metadata.model_wide, tuple(d.key.value for d in v.metadata.dependencies))))
    keys, diagnostics = set(), []
    for descriptor in values:
        if descriptor.key in keys:
            diagnostics.append(_manifest_diagnostic(CompilationFailure.MANIFEST_DUPLICATE_ARTIFACT, 'Duplicate artifact descriptors are never overwritten or exempted by equality.', key=descriptor.key, kind=descriptor.kind, conflicts=tuple(d for d in values if d.key == descriptor.key)))
        keys.add(descriptor.key)
    for descriptor in values:
        for dependency in descriptor.metadata.dependencies:
            if dependency.key not in keys:
                diagnostics.append(_manifest_diagnostic(CompilationFailure.MANIFEST_UNKNOWN_DEPENDENCY, 'Internal dependency target is absent from the complete declared artifact set.', key=descriptor.key, dependency=dependency.key))
    if diagnostics:
        raise RuntimeArtifactManifestError(tuple(diagnostics))
    return values


def _manifest_binding(result: CompilationResult, request: CompilationRequest, compiler: ModelCompiler) -> None:
    if type(result) is not CompilationResult or type(request) is not CompilationRequest or type(compiler) is not ModelCompiler:
        _manifest_reject(CompilationFailure.INVALID_INPUT, 'Manifest assembly requires actual compiler result, original request and explicit compiler configuration.')
    if result.status is not CompilationStatus.SUCCEEDED:
        severity = TypeValidationSeverity.ERROR if result.status is CompilationStatus.FAILED else TypeValidationSeverity.WARNING
        diagnostic = _manifest_diagnostic(CompilationFailure.MANIFEST_COMPILATION_NOT_SUCCESSFUL, 'Authoritative compilation is not successful; no complete runtime manifest can be assembled.', target=request.context.target, severity=severity)
        raise RuntimeArtifactManifestError((*result.diagnostics, diagnostic), result.status)
    if request.context.target != BUILD_TARGET or result.target != request.context.target:
        _manifest_reject(CompilationFailure.MANIFEST_TARGET_MISMATCH, 'Only the actual artifact-build objective supports runtime artifact manifests; preparation is not a runtime target.', target=request.context.target)
    if request.canonical_model.scope != request.context.scope or result.preparation is None or result.preparation.context.scope != request.context.scope:
        _manifest_reject(CompilationFailure.MANIFEST_CONTEXT_MISMATCH, 'Manifest canonical/compiler/result semantic scopes disagree.', target=request.context.target)
    if result.preparation.model is not request.canonical_model or result.preparation.context != request.context or result.validation_evidence is not request.validation_evidence:
        _manifest_reject(CompilationFailure.MANIFEST_SNAPSHOT_MISMATCH, 'Successful result is not bound to this exact original canonical input/evidence/context.')
    origin = result.output_origin
    if origin is None or origin.request is not request or origin.compiler is not compiler:
        _manifest_reject(CompilationFailure.MANIFEST_OUTPUT_UNBOUND, 'Manifest requires original compiler-produced request/configuration output association, not equal-looking results.')
    changed = compiler._configuration_diagnostics()
    if changed:
        raise RuntimeArtifactManifestError(changed)
    if tuple(o.descriptor for o in result.phase_outcomes) != compiler._descriptors or any(o.status is not CompilationPhaseStatus.COMPLETED or o.executed is not True for o in result.phase_outcomes):
        _manifest_reject(CompilationFailure.MANIFEST_OUTPUT_UNBOUND, 'Successful configured phase completion/execution evidence does not match original composition.')
    if not result.artifacts.artifacts or not any(CompilationCapability.EMIT_ARTIFACTS in o.descriptor.capabilities for o in result.phase_outcomes):
        diagnostic = _manifest_diagnostic(CompilationFailure.MANIFEST_INCOMPLETE_OUTPUT, 'Runtime target requires actual complete final artifact output; IR and zero artifacts cannot substitute.', severity=TypeValidationSeverity.WARNING)
        raise RuntimeArtifactManifestError((diagnostic,), CompilationStatus.INCOMPLETE)


@dataclass(frozen=True, slots=True, eq=False)
class RuntimeArtifactManifestCompilationAssociation:
    """Capture checked completion metadata only; InitVar result payloads are not kept."""
    result: InitVar[CompilationResult]
    request: CompilationRequest
    compiler: ModelCompiler
    support: tuple[RuntimeArtifactKindSupport, ...]
    output_origin: CompilationOutputOrigin = field(init=False)
    artifacts: tuple[RuntimeArtifactDescriptor, ...] = field(init=False)
    phase_outcomes: tuple[CompilationPhaseOutcome, ...] = field(init=False)
    __hash__ = None

    def __post_init__(self, result: CompilationResult) -> None:
        _manifest_binding(result, self.request, self.compiler)
        support = _manifest_support(self.support)
        descriptors = _manifest_inventory(_runtime_descriptors(result, self.request, support))
        object.__setattr__(self, 'support', support)
        object.__setattr__(self, 'output_origin', result.output_origin)
        object.__setattr__(self, 'artifacts', descriptors)
        object.__setattr__(self, 'phase_outcomes', result.phase_outcomes)


@dataclass(frozen=True, slots=True, eq=False)
class RuntimeArtifactManifest:
    identity: RuntimeArtifactManifestId
    schema_version: RuntimeArtifactManifestSchemaVersion
    semantic_context: SemanticContextRef
    target: CompilationTargetId
    compilation_association: RuntimeArtifactManifestCompilationAssociation
    artifacts: tuple[RuntimeArtifactDescriptor, ...]
    __hash__ = None

    def __post_init__(self) -> None:
        if type(self.identity) is not RuntimeArtifactManifestId:
            _manifest_reject(CompilationFailure.MANIFEST_INVALID_IDENTITY, 'Manifest identity cannot reuse semantic, IR or artifact identity.')
        if self.schema_version is not RuntimeArtifactManifestSchemaVersion.V0:
            _manifest_reject(CompilationFailure.MANIFEST_UNSUPPORTED_SCHEMA, 'Only explicitly supported manifest schema V0 is accepted.', identity=self.identity)
        if type(self.compilation_association) is not RuntimeArtifactManifestCompilationAssociation:
            _manifest_reject(CompilationFailure.MANIFEST_OUTPUT_UNBOUND, 'Manifest requires actual checked complete compilation association.', identity=self.identity)
        request = self.compilation_association.request
        if type(self.semantic_context) is not SemanticContextRef or self.semantic_context != request.context.scope:
            _manifest_reject(CompilationFailure.MANIFEST_CONTEXT_MISMATCH, 'Manifest scope differs from its original compilation scope.', identity=self.identity)
        if type(self.target) is not CompilationTargetId or self.target != request.context.target or self.target != BUILD_TARGET:
            _manifest_reject(CompilationFailure.MANIFEST_TARGET_MISMATCH, 'Manifest target must be original supported artifact-build objective.', identity=self.identity)
        artifacts = _manifest_inventory(self.artifacts)
        if artifacts != self.compilation_association.artifacts or not artifacts:
            _manifest_reject(CompilationFailure.MANIFEST_INCOMPLETE_OUTPUT, 'Manifest must preserve the entire checked final artifact inventory exactly; no subset, extras or empty replacement.', identity=self.identity)
        object.__setattr__(self, 'artifacts', artifacts)

    def same_declaration(self, other: 'RuntimeArtifactManifest') -> bool:
        """Supported manifest metadata equivalence, not artifact payload equality."""
        if type(other) is not RuntimeArtifactManifest:
            raise TypeError('Manifest declaration comparison requires another actual manifest.')
        left, right = self.compilation_association, other.compilation_association
        comparison = CompilationResultEquivalence()
        return ((self.identity, self.schema_version, self.semantic_context, self.target, self.artifacts) ==
                (other.identity, other.schema_version, other.semantic_context, other.target, other.artifacts)
                and left.support == right.support
                and comparison.requests(left.request, right.request)
                and comparison.configurations(left.compiler, right.compiler)
                and tuple(_outcome_semantics(o) for o in left.phase_outcomes) == tuple(_outcome_semantics(o) for o in right.phase_outcomes))


@dataclass(frozen=True, slots=True)
class RuntimeArtifactManifestAssemblyResult:
    status: CompilationStatus
    manifest: RuntimeArtifactManifest | None = None
    diagnostics: tuple[CompilationDiagnostic, ...] = ()

    def __post_init__(self) -> None:
        if type(self.status) is not CompilationStatus or type(self.diagnostics) not in (tuple, list) or any(type(d) is not CompilationDiagnostic for d in self.diagnostics):
            raise TypeError('Assembly uses original compilation statuses and immutable actual diagnostics.')
        diagnostics = tuple(self.diagnostics)
        if self.status is CompilationStatus.SUCCEEDED:
            if type(self.manifest) is not RuntimeArtifactManifest or any(d.severity is TypeValidationSeverity.ERROR for d in diagnostics):
                raise ValueError('Successful assembly requires complete checked manifest without errors.')
        elif self.manifest is not None or not diagnostics:
            raise ValueError('Non-success assembly has diagnostics and no complete/partial manifest.')
        object.__setattr__(self, 'diagnostics', diagnostics)


@dataclass(frozen=True, slots=True)
class RuntimeArtifactManifestAssembler:
    support: tuple[RuntimeArtifactKindSupport, ...] = ()

    def __post_init__(self) -> None:
        object.__setattr__(self, 'support', _manifest_support(self.support))

    def assemble(self, result: CompilationResult, request: CompilationRequest, *, compiler: ModelCompiler, identity: RuntimeArtifactManifestId, schema_version: RuntimeArtifactManifestSchemaVersion = RuntimeArtifactManifestSchemaVersion.V0, existing_manifests: tuple[RuntimeArtifactManifest, ...] = ()) -> RuntimeArtifactManifestAssemblyResult:
        try:
            if type(identity) is not RuntimeArtifactManifestId:
                _manifest_reject(CompilationFailure.MANIFEST_INVALID_IDENTITY, 'Assembly requires explicit independent manifest identity.')
            if schema_version is not RuntimeArtifactManifestSchemaVersion.V0:
                _manifest_reject(CompilationFailure.MANIFEST_UNSUPPORTED_SCHEMA, 'Unsupported manifest schema has no automatic migration.', identity=identity)
            if type(existing_manifests) not in (tuple, list) or any(type(m) is not RuntimeArtifactManifest for m in existing_manifests):
                _manifest_reject(CompilationFailure.INVALID_INPUT, 'Existing manifest membership must be an explicit finite immutable inventory.')
            existing_manifests = tuple(existing_manifests)
            association = RuntimeArtifactManifestCompilationAssociation(result, request, compiler, self.support)
            seen = set()
            for previous in sorted((m for m in existing_manifests if m.compilation_association.output_origin is association.output_origin), key=lambda m: m.identity.value):
                if previous.identity in seen:
                    _manifest_reject(CompilationFailure.MANIFEST_IDENTITY_COLLISION, 'Existing manifest inventory repeats identity in original compilation-output scope.', identity=previous.identity)
                seen.add(previous.identity)
            if identity in seen:
                _manifest_reject(CompilationFailure.MANIFEST_IDENTITY_COLLISION, 'Manifest identity already exists within this original compilation-output scope.', identity=identity)
            manifest = RuntimeArtifactManifest(identity, schema_version, request.context.scope, request.context.target, association, association.artifacts)
        except RuntimeArtifactManifestError as failure:
            return RuntimeArtifactManifestAssemblyResult(failure.status, diagnostics=failure.diagnostics)
        return RuntimeArtifactManifestAssemblyResult(CompilationStatus.SUCCEEDED, manifest, result.diagnostics)


__all__ += ['CompilationOutputOrigin', 'RuntimeArtifactDependencyRef', 'RuntimeArtifactMetadata',
            'RuntimeArtifactDescriptor', 'RuntimeArtifactManifestError', 'RuntimeArtifactManifestId',
            'RuntimeArtifactManifestSchemaVersion', 'RuntimeArtifactKindSupport',
            'RuntimeArtifactManifestCompilationAssociation', 'RuntimeArtifactManifest',
            'RuntimeArtifactManifestAssemblyResult', 'RuntimeArtifactManifestAssembler']


class ArtifactWriteStage(Enum):
    PREFLIGHT = 'preflight'
    DESTINATION = 'destination'
    STAGING = 'staging'
    WRITE = 'write'
    VERIFY = 'verify'
    COMMIT = 'commit'
    SYNC = 'sync'
    CLEANUP = 'cleanup'


class ArtifactWritePolicy(Enum):
    FAIL_IF_EXISTS = 'fail-if-exists'


class ArtifactDurabilityPolicy(Enum):
    VISIBLE_COMMIT = 'visible-commit'
    SYNCHRONIZED_COMMIT = 'synchronized-commit'


class ArtifactWriteError(ValueError):
    def __init__(self, diagnostics: tuple[CompilationDiagnostic, ...], status: CompilationStatus = CompilationStatus.FAILED) -> None:
        if type(diagnostics) is not tuple or not diagnostics or any(type(d) is not CompilationDiagnostic for d in diagnostics) or status not in (CompilationStatus.FAILED, CompilationStatus.INCOMPLETE):
            raise TypeError('Write rejection retains actual nonempty compiler diagnostics.')
        self.diagnostics = diagnostics
        self.status = status
        super().__init__('Artifact materialization rejected; inspect structured diagnostics.')


def _write_diagnostic(code: CompilationFailure, message: str, *, stage: ArtifactWriteStage = ArtifactWriteStage.PREFLIGHT, manifest: RuntimeArtifactManifest | None = None, descriptor: RuntimeArtifactDescriptor | None = None, location: 'ArtifactRelativeLocation | None' = None, incomplete: bool = False) -> CompilationDiagnostic:
    association = CompilationDiagnosticAssociation(
        CompilationDiagnosticOrigin.RESULT,
        artifact_target=None if descriptor is None else CompilationArtifactTarget(descriptor.key, descriptor.kind),
        semantic_context=None if manifest is None else manifest.semantic_context,
        manifest_identity=None if manifest is None else manifest.identity,
        write_stage=stage, output_location=location)
    return CompilationDiagnostic(code, message, TypeValidationSeverity.WARNING if incomplete else TypeValidationSeverity.ERROR, association=association)


def _write_reject(code: CompilationFailure, message: str, **associations: object) -> None:
    diagnostic = _write_diagnostic(code, message, **associations)
    raise ArtifactWriteError((diagnostic,), CompilationStatus.INCOMPLETE if associations.get('incomplete') else CompilationStatus.FAILED)


def _write_sequence(values: object, expected: type) -> tuple:
    if type(values) not in (tuple, list) or any(type(v) is not expected for v in values):
        _write_reject(CompilationFailure.WRITE_INVALID_INPUT, 'An explicit finite typed inventory is required.')
    return tuple(values)


@dataclass(frozen=True, slots=True, order=True)
class ArtifactRelativeLocation:
    """v0 deliberately supports portable, flat ASCII filenames only."""
    value: str

    def __post_init__(self) -> None:
        if type(self.value) is not str or not 1 <= len(self.value) <= 240 or re.fullmatch(r'[a-z][a-z0-9_.-]*', self.value) is None or self.value.endswith('.') or self.value.split('.')[0] in {'con', 'prn', 'aux', 'nul', *(f'com{i}' for i in range(10)), *(f'lpt{i}' for i in range(10))}:
            _write_reject(CompilationFailure.WRITE_UNSAFE_PATH, 'Output requires a bounded unambiguous portable flat relative filename.')


@dataclass(frozen=True, slots=True)
class ArtifactWriteDestination:
    """Logical reference resolved exclusively through trusted adapter configuration."""
    root_reference: str
    output_directory: str

    def __post_init__(self) -> None:
        for value in (self.root_reference, self.output_directory):
            if type(value) is not str or len(value) > 100 or re.fullmatch(r'[a-z][a-z0-9]*(?:-[a-z0-9]+)*', value) is None:
                _write_reject(CompilationFailure.WRITE_INVALID_DESTINATION, 'Destination requires explicit bounded server root and output-set tokens.')
        ArtifactRelativeLocation(self.output_directory)


@dataclass(frozen=True, slots=True)
class ArtifactContentDigest:
    """Producer-declared exact byte digest; no signature/authenticity claim."""
    algorithm: str
    value: str

    def __post_init__(self) -> None:
        if self.algorithm != 'sha256' or type(self.algorithm) is not str or type(self.value) is not str or re.fullmatch(r'[0-9a-f]{64}', self.value) is None:
            _write_reject(CompilationFailure.WRITE_UNSUPPORTED_CONTENT, 'Only explicitly declared lowercase SHA-256 byte digests are supported.', incomplete=True)


@dataclass(frozen=True, slots=True)
class ArtifactByteContentSupport:
    """Owner approval of an existing immutable artifact field, never an encoder."""
    artifact_support: RuntimeArtifactKindSupport
    byte_field: str
    digest_field: str | None = None

    def __post_init__(self) -> None:
        if type(self.artifact_support) is not RuntimeArtifactKindSupport:
            _write_reject(CompilationFailure.WRITE_UNSUPPORTED_CONTENT, 'Byte support requires existing CMP-07 concrete kind approval.', incomplete=True)
        names = {f.name for f in fields(self.artifact_support.artifact_type)}
        forbidden = {'key', 'kind', 'scope', 'target', 'semantic_dependencies', 'manifest_metadata'}
        for name in (self.byte_field, self.digest_field):
            if name is not None and (type(name) is not str or not name.isidentifier() or name.startswith('_') or name not in names or name in forbidden):
                _write_reject(CompilationFailure.WRITE_UNSUPPORTED_CONTENT, 'Content approval must name a separate declared immutable producer field.', incomplete=True)
        if self.byte_field is None or self.byte_field == self.digest_field:
            _write_reject(CompilationFailure.WRITE_UNSUPPORTED_CONTENT, 'Byte and optional digest fields must be explicit and distinct.', incomplete=True)


@dataclass(frozen=True, slots=True, eq=False)
class ArtifactContentSource:
    """Actual compiler artifact object; bytes are read only from approved fields."""
    artifact: CompilationArtifact
    __hash__ = None

    def __post_init__(self) -> None:
        if not is_dataclass(self.artifact) or isinstance(self.artifact, type) or not self.artifact.__dataclass_params__.frozen:
            _write_reject(CompilationFailure.WRITE_UNSUPPORTED_CONTENT, 'Content source must retain an actual immutable producer artifact.', incomplete=True)


@dataclass(frozen=True, slots=True)
class ArtifactOutputMapping:
    key: CompilationArtifactKey
    kind: CompilationArtifactKind
    location: ArtifactRelativeLocation

    def __post_init__(self) -> None:
        if type(self.key) is not CompilationArtifactKey or type(self.kind) is not CompilationArtifactKind or type(self.location) is not ArtifactRelativeLocation:
            _write_reject(CompilationFailure.WRITE_INVALID_INPUT, 'Layout mappings require existing artifact identity/kind and validated location.')


@dataclass(frozen=True, slots=True)
class ArtifactOutputLayout:
    """Explicit complete mapping, or v0 deterministic kind__key.bin mapping."""
    mappings: tuple[ArtifactOutputMapping, ...] = ()

    def __post_init__(self) -> None:
        values = _write_sequence(self.mappings, ArtifactOutputMapping)
        if len({m.key for m in values}) != len(values):
            _write_reject(CompilationFailure.WRITE_LOCATION_CONFLICT, 'Layout cannot repeat an artifact identity.')
        object.__setattr__(self, 'mappings', tuple(sorted(values, key=lambda m: m.key.value)))


@dataclass(frozen=True, slots=True)
class ArtifactWriteRequest:
    compilation_result: CompilationResult
    manifest_assembly: RuntimeArtifactManifestAssemblyResult
    artifact_contents: tuple[ArtifactContentSource, ...]
    destination: ArtifactWriteDestination
    write_policy: ArtifactWritePolicy = ArtifactWritePolicy.FAIL_IF_EXISTS
    durability: ArtifactDurabilityPolicy = ArtifactDurabilityPolicy.VISIBLE_COMMIT
    layout: ArtifactOutputLayout = field(default_factory=ArtifactOutputLayout)

    def __post_init__(self) -> None:
        if type(self.compilation_result) is not CompilationResult or type(self.manifest_assembly) is not RuntimeArtifactManifestAssemblyResult or type(self.destination) is not ArtifactWriteDestination or type(self.layout) is not ArtifactOutputLayout:
            _write_reject(CompilationFailure.WRITE_INVALID_INPUT, 'Write request requires actual compiler/assembly evidence, destination and layout.')
        if self.write_policy is not ArtifactWritePolicy.FAIL_IF_EXISTS:
            _write_reject(CompilationFailure.WRITE_UNSUPPORTED_POLICY, 'Only exclusive complete-set FAIL_IF_EXISTS is supported.', incomplete=True)
        if type(self.durability) is not ArtifactDurabilityPolicy:
            _write_reject(CompilationFailure.WRITE_UNSUPPORTED_DURABILITY, 'Requested durability policy is not supported.', incomplete=True)
        object.__setattr__(self, 'artifact_contents', _write_sequence(self.artifact_contents, ArtifactContentSource))


@dataclass(frozen=True, slots=True)
class ArtifactPlannedOutput:
    descriptor: RuntimeArtifactDescriptor
    location: ArtifactRelativeLocation
    source: ArtifactContentSource
    content: bytes = field(repr=False)
    declared_digest: ArtifactContentDigest | None = None

    def __post_init__(self) -> None:
        if type(self.descriptor) is not RuntimeArtifactDescriptor or type(self.location) is not ArtifactRelativeLocation or type(self.source) is not ArtifactContentSource or type(self.content) is not bytes or self.declared_digest is not None and type(self.declared_digest) is not ArtifactContentDigest:
            _write_reject(CompilationFailure.WRITE_INVALID_INPUT, 'Planned output requires typed descriptor/location/source and exact immutable bytes.')

    @property
    def expected_byte_length(self) -> int:
        return len(self.content)


@dataclass(frozen=True, slots=True)
class ArtifactWritePlan:
    request: ArtifactWriteRequest
    outputs: tuple[ArtifactPlannedOutput, ...]

    def __post_init__(self) -> None:
        if type(self.request) is not ArtifactWriteRequest:
            _write_reject(CompilationFailure.WRITE_INVALID_INPUT, 'Plan requires the actual immutable write request.')
        values = _write_sequence(self.outputs, ArtifactPlannedOutput)
        manifest = self.request.manifest_assembly.manifest
        if self.request.manifest_assembly.status is not CompilationStatus.SUCCEEDED or manifest is None or tuple(o.descriptor for o in values) != manifest.artifacts or len({o.location for o in values}) != len(values):
            _write_reject(CompilationFailure.WRITE_MANIFEST_MISMATCH, 'Plan must contain the complete ordered manifest with unique output locations.')
        if any(o.source not in self.request.artifact_contents for o in values):
            _write_reject(CompilationFailure.WRITE_CONTENT_MEMBERSHIP, 'Plan sources must retain the supplied original artifact objects.')
        object.__setattr__(self, 'outputs', values)


@dataclass(frozen=True, slots=True)
class ArtifactWritePlanner:
    content_support: tuple[ArtifactByteContentSupport, ...] = ()

    def __post_init__(self) -> None:
        support = _write_sequence(self.content_support, ArtifactByteContentSupport)
        if len({s.artifact_support.kind for s in support}) != len(support):
            _write_reject(CompilationFailure.WRITE_UNSUPPORTED_CONTENT, 'Byte capability catalog cannot repeat a kind.', incomplete=True)
        object.__setattr__(self, 'content_support', tuple(sorted(support, key=lambda s: s.artifact_support.kind.value)))

    def plan(self, request: ArtifactWriteRequest) -> ArtifactWritePlan:
        if type(request) is not ArtifactWriteRequest:
            _write_reject(CompilationFailure.WRITE_INVALID_INPUT, 'Planner accepts an actual typed write request.')
        result, assembly = request.compilation_result, request.manifest_assembly
        if result.status is not CompilationStatus.SUCCEEDED:
            diagnostic = _write_diagnostic(CompilationFailure.WRITE_COMPILATION_NOT_READY, 'Authoritative compilation is not successful.')
            raise ArtifactWriteError((*result.diagnostics, diagnostic))
        if assembly.status is not CompilationStatus.SUCCEEDED or assembly.manifest is None:
            diagnostic = _write_diagnostic(CompilationFailure.WRITE_MANIFEST_MISMATCH, 'A complete successful CMP-07 assembly is required.')
            raise ArtifactWriteError((*assembly.diagnostics, diagnostic))
        manifest = assembly.manifest
        association = manifest.compilation_association
        try:
            current = RuntimeArtifactManifestCompilationAssociation(result, association.request, association.compiler, association.support)
            # Recheck structural completeness without modifying the accepted manifest.
            RuntimeArtifactManifest(manifest.identity, manifest.schema_version, manifest.semantic_context, manifest.target, association, manifest.artifacts)
        except RuntimeArtifactManifestError as error:
            diagnostic = _write_diagnostic(CompilationFailure.WRITE_MANIFEST_MISMATCH, 'Compiler result and manifest prerequisite binding failed.', manifest=manifest)
            raise ArtifactWriteError((*error.diagnostics, diagnostic)) from error
        if current.output_origin is not association.output_origin or current.artifacts != association.artifacts or current.phase_outcomes != association.phase_outcomes:
            _write_reject(CompilationFailure.WRITE_MANIFEST_MISMATCH, 'Manifest must describe this original compilation output, not another equal-looking invocation.', manifest=manifest)
        originals = result.artifacts.artifacts
        sources = request.artifact_contents
        if len(sources) != len(originals) or len({id(s.artifact) for s in sources}) != len(sources) or any(sum(s.artifact is a for s in sources) != 1 for a in originals):
            _write_reject(CompilationFailure.WRITE_CONTENT_MEMBERSHIP, 'Each final compiler artifact needs exactly one original source; missing, duplicate and extra sources are rejected.', manifest=manifest)
        if request.layout.mappings and tuple((m.key, m.kind) for m in request.layout.mappings) != tuple((d.key, d.kind) for d in manifest.artifacts):
            _write_reject(CompilationFailure.WRITE_LOCATION_CONFLICT, 'Explicit layout must cover exact manifest keys and kinds once.', manifest=manifest)
        outputs = []
        for descriptor, artifact in zip(manifest.artifacts, originals):
            source = next(s for s in sources if s.artifact is artifact)
            support = next((s for s in self.content_support if s.artifact_support.kind == descriptor.kind and s.artifact_support.artifact_type is type(artifact)), None)
            if support is None or support.artifact_support not in association.support:
                _write_reject(CompilationFailure.WRITE_UNSUPPORTED_CONTENT, 'Artifact has no explicit approved immutable byte-field capability.', manifest=manifest, descriptor=descriptor, incomplete=True)
            content = getattr(artifact, support.byte_field)
            if type(content) is not bytes:
                _write_reject(CompilationFailure.WRITE_UNSUPPORTED_ENCODING, 'Approved bytes must already be defined by the producer; implicit encoding is forbidden.', manifest=manifest, descriptor=descriptor, incomplete=True)
            digest = None if support.digest_field is None else getattr(artifact, support.digest_field)
            if support.digest_field is not None and type(digest) is not ArtifactContentDigest:
                _write_reject(CompilationFailure.WRITE_UNSUPPORTED_CONTENT, 'Declared digest capability needs an actual approved digest value.', manifest=manifest, descriptor=descriptor, incomplete=True)
            mapping = next((m for m in request.layout.mappings if m.key == descriptor.key), None)
            location = mapping.location if mapping else ArtifactRelativeLocation(descriptor.kind.value + '__' + descriptor.key.value + '.bin')
            if any(o.location == location for o in outputs):
                _write_reject(CompilationFailure.WRITE_LOCATION_CONFLICT, 'Distinct artifacts cannot share a normalized committed location.', manifest=manifest, descriptor=descriptor, location=location)
            outputs.append(ArtifactPlannedOutput(descriptor, location, source, content, digest))
        return ArtifactWritePlan(request, tuple(outputs))


@dataclass(frozen=True, slots=True)
class MaterializedArtifact:
    descriptor: RuntimeArtifactDescriptor
    location: ArtifactRelativeLocation
    byte_length: int
    verified_digest: ArtifactContentDigest | None = None

    def __post_init__(self) -> None:
        if type(self.descriptor) is not RuntimeArtifactDescriptor or type(self.location) is not ArtifactRelativeLocation or type(self.byte_length) is not int or self.byte_length < 0 or self.verified_digest is not None and type(self.verified_digest) is not ArtifactContentDigest:
            _write_reject(CompilationFailure.WRITE_INVALID_INPUT, 'Receipt entry requires actual typed identity/location/length and optional verified digest.')


@dataclass(frozen=True, slots=True)
class ArtifactMaterializationReceipt:
    """Complete-set facts only; retains no byte payload or staging path."""
    manifest: RuntimeArtifactManifest
    destination: ArtifactWriteDestination
    artifacts: tuple[MaterializedArtifact, ...]
    durability: ArtifactDurabilityPolicy

    def __post_init__(self) -> None:
        if type(self.manifest) is not RuntimeArtifactManifest or type(self.destination) is not ArtifactWriteDestination or type(self.durability) is not ArtifactDurabilityPolicy:
            _write_reject(CompilationFailure.WRITE_INVALID_INPUT, 'Receipt requires accepted manifest and committed logical destination/durability.')
        values = _write_sequence(self.artifacts, MaterializedArtifact)
        if tuple(v.descriptor for v in values) != self.manifest.artifacts or len({v.location for v in values}) != len(values):
            _write_reject(CompilationFailure.WRITE_MANIFEST_MISMATCH, 'Receipt must preserve complete manifest identity/kind/membership and unique committed locations.')
        object.__setattr__(self, 'artifacts', values)

    @property
    def manifest_identity(self) -> RuntimeArtifactManifestId:
        return self.manifest.identity

    @property
    def compilation_association(self) -> RuntimeArtifactManifestCompilationAssociation:
        return self.manifest.compilation_association


@dataclass(frozen=True, slots=True)
class ArtifactWriteResult:
    status: CompilationStatus
    receipt: ArtifactMaterializationReceipt | None = None
    diagnostics: tuple[CompilationDiagnostic, ...] = ()
    committed_destination: ArtifactWriteDestination | None = None

    def __post_init__(self) -> None:
        if type(self.status) is not CompilationStatus:
            raise TypeError('Writer uses existing compiler statuses.')
        diagnostics = _write_sequence(self.diagnostics, CompilationDiagnostic)
        if self.committed_destination is not None and type(self.committed_destination) is not ArtifactWriteDestination:
            raise TypeError('Visible post-commit failure must retain a typed logical destination.')
        if self.status is CompilationStatus.SUCCEEDED:
            if type(self.receipt) is not ArtifactMaterializationReceipt or self.committed_destination != self.receipt.destination or any(d.severity is TypeValidationSeverity.ERROR for d in diagnostics):
                raise ValueError('Success requires complete receipt and committed destination without errors.')
        elif self.receipt is not None or not diagnostics:
            raise ValueError('Non-success has diagnostics and no successful or partial receipt.')
        object.__setattr__(self, 'diagnostics', diagnostics)


class ArtifactWriter(Protocol):
    def write(self, request: ArtifactWriteRequest) -> ArtifactWriteResult:
        ...


class ArtifactWriteDiagnostics:
    """CMP-02 diagnostic construction shared with the owning filesystem adapter."""
    @staticmethod
    def create(code: CompilationFailure, message: str, **associations: object) -> CompilationDiagnostic:
        return _write_diagnostic(code, message, **associations)

    @staticmethod
    def reject(code: CompilationFailure, message: str, **associations: object) -> None:
        _write_reject(code, message, **associations)


# No legacy unassociated write diagnostic is interpreted as a semantic error.
_LEGACY_DIAGNOSTIC_OWNERS = MappingProxyType({**_LEGACY_DIAGNOSTIC_OWNERS,
    **{code: CompilationDiagnosticOrigin.RESULT for code in CompilationFailure if code.name.startswith('WRITE_')}})

__all__ += ['ArtifactWriteStage', 'ArtifactWritePolicy', 'ArtifactDurabilityPolicy',
            'ArtifactWriteError', 'ArtifactRelativeLocation', 'ArtifactWriteDestination',
            'ArtifactContentDigest', 'ArtifactByteContentSupport', 'ArtifactContentSource',
            'ArtifactOutputMapping', 'ArtifactOutputLayout', 'ArtifactWriteRequest',
            'ArtifactPlannedOutput', 'ArtifactWritePlan', 'ArtifactWritePlanner',
            'MaterializedArtifact', 'ArtifactMaterializationReceipt', 'ArtifactWriteResult',
            'ArtifactWriter', 'ArtifactWriteDiagnostics']


class ArtifactReadStage(Enum):
    PREFLIGHT = 'preflight'
    SOURCE = 'source'
    OPEN = 'open'
    READ = 'read'
    VERIFY = 'verify'
    CLOSE = 'close'


class ArtifactReadSourceType(Enum):
    LOCAL_FILESYSTEM = 'local-filesystem'


# Same approved logical root/output reference as CMP-08, without a second path model.
ArtifactReadSource = ArtifactWriteDestination


class ArtifactReadSelectionMode(Enum):
    ONE_ARTIFACT = 'one-artifact'
    EXPLICIT_ARTIFACT_SET = 'explicit-artifact-set'
    ALL_DECLARED_ARTIFACTS = 'all-declared-artifacts'


class ArtifactReadIntegrity(Enum):
    SIZE_VERIFIED = 'size-verified'
    DIGEST_VERIFIED = 'digest-verified'


class ArtifactReadError(ValueError):
    def __init__(self, diagnostics: tuple[CompilationDiagnostic, ...], status: CompilationStatus = CompilationStatus.FAILED) -> None:
        if type(diagnostics) is not tuple or not diagnostics or any(type(d) is not CompilationDiagnostic for d in diagnostics) or status not in (CompilationStatus.FAILED, CompilationStatus.INCOMPLETE):
            raise TypeError('Read failure preserves actual diagnostics and non-success status.')
        self.diagnostics = diagnostics
        self.status = status
        super().__init__('Artifact retrieval rejected; inspect structured diagnostics.')


class ArtifactReadDiagnostics:
    @staticmethod
    def create(code: CompilationFailure, message: str, *, stage: ArtifactReadStage = ArtifactReadStage.PREFLIGHT, manifest: RuntimeArtifactManifest | None = None, key: CompilationArtifactKey | None = None, entry: MaterializedArtifact | None = None, incomplete: bool = False) -> CompilationDiagnostic:
        artifact = CompilationArtifactTarget(entry.descriptor.key, entry.descriptor.kind) if entry is not None else None if key is None else CompilationArtifactTarget(key)
        association = CompilationDiagnosticAssociation(
            CompilationDiagnosticOrigin.RESULT, artifact_target=artifact,
            manifest_identity=None if manifest is None else manifest.identity,
            semantic_context=None if manifest is None else manifest.semantic_context,
            output_location=None if entry is None else entry.location,
            read_stage=stage, read_source_type=ArtifactReadSourceType.LOCAL_FILESYSTEM)
        return CompilationDiagnostic(code, message, TypeValidationSeverity.WARNING if incomplete else TypeValidationSeverity.ERROR, association=association)

    @staticmethod
    def reject(code: CompilationFailure, message: str, **associations: object) -> None:
        diagnostic = ArtifactReadDiagnostics.create(code, message, **associations)
        raise ArtifactReadError((diagnostic,), CompilationStatus.INCOMPLETE if associations.get('incomplete') else CompilationStatus.FAILED)


def _read_sequence(values: object, expected: type) -> tuple:
    if type(values) not in (tuple, list) or any(type(v) is not expected for v in values):
        ArtifactReadDiagnostics.reject(CompilationFailure.READ_INVALID_REQUEST, 'An explicit finite typed inventory is required.')
    return tuple(values)


@dataclass(frozen=True, slots=True)
class ArtifactReadSelection:
    mode: ArtifactReadSelectionMode
    keys: tuple[CompilationArtifactKey, ...] = ()

    def __post_init__(self) -> None:
        if type(self.mode) is not ArtifactReadSelectionMode:
            ArtifactReadDiagnostics.reject(CompilationFailure.READ_INVALID_SELECTION, 'Selection requires an explicit supported mode.')
        keys = _read_sequence(self.keys, CompilationArtifactKey)
        if len(set(keys)) != len(keys) or self.mode is ArtifactReadSelectionMode.ALL_DECLARED_ARTIFACTS and keys or self.mode is ArtifactReadSelectionMode.ONE_ARTIFACT and len(keys) != 1 or self.mode is ArtifactReadSelectionMode.EXPLICIT_ARTIFACT_SET and not keys:
            ArtifactReadDiagnostics.reject(CompilationFailure.READ_INVALID_SELECTION, 'ALL has no key overrides; ONE has one key; explicit SET is nonempty without duplicates.')
        object.__setattr__(self, 'keys', tuple(sorted(keys)))


@dataclass(frozen=True, slots=True)
class ArtifactReadPolicy:
    maximum_artifact_bytes: int = 32 * 1024 * 1024
    maximum_aggregate_bytes: int = 128 * 1024 * 1024
    maximum_artifact_count: int = 128
    required_integrity: ArtifactReadIntegrity = ArtifactReadIntegrity.SIZE_VERIFIED

    def __post_init__(self) -> None:
        if any(type(v) is not int or v <= 0 for v in (self.maximum_artifact_bytes, self.maximum_aggregate_bytes, self.maximum_artifact_count)) or type(self.required_integrity) is not ArtifactReadIntegrity:
            ArtifactReadDiagnostics.reject(CompilationFailure.READ_INVALID_POLICY, 'Read limits require positive actual integers and an explicit supported integrity requirement.')

    def bounded_by(self, server: 'ArtifactReadPolicy') -> 'ArtifactReadPolicy':
        if type(server) is not ArtifactReadPolicy:
            ArtifactReadDiagnostics.reject(CompilationFailure.READ_INVALID_POLICY, 'Read ceilings require trusted typed server configuration.')
        integrity = ArtifactReadIntegrity.DIGEST_VERIFIED if ArtifactReadIntegrity.DIGEST_VERIFIED in (self.required_integrity, server.required_integrity) else ArtifactReadIntegrity.SIZE_VERIFIED
        return ArtifactReadPolicy(min(self.maximum_artifact_bytes, server.maximum_artifact_bytes), min(self.maximum_aggregate_bytes, server.maximum_aggregate_bytes), min(self.maximum_artifact_count, server.maximum_artifact_count), integrity)


@dataclass(frozen=True, slots=True)
class ArtifactReadRequest:
    manifest: RuntimeArtifactManifest
    receipt: ArtifactMaterializationReceipt
    selection: ArtifactReadSelection
    source: ArtifactReadSource
    policy: ArtifactReadPolicy = field(default_factory=ArtifactReadPolicy)

    def __post_init__(self) -> None:
        for value, expected, code in (
            (self.manifest, RuntimeArtifactManifest, CompilationFailure.READ_MANIFEST_MISMATCH),
            (self.receipt, ArtifactMaterializationReceipt, CompilationFailure.READ_RECEIPT_MISMATCH),
            (self.selection, ArtifactReadSelection, CompilationFailure.READ_INVALID_SELECTION),
            (self.source, ArtifactReadSource, CompilationFailure.READ_UNSUPPORTED_SOURCE),
            (self.policy, ArtifactReadPolicy, CompilationFailure.READ_INVALID_POLICY)):
            if type(value) is not expected:
                ArtifactReadDiagnostics.reject(code, 'Read request requires actual manifest, committed receipt, explicit selection, logical source and bounded policy.')


@dataclass(frozen=True, slots=True)
class ArtifactReadPlan:
    request: ArtifactReadRequest
    effective_policy: ArtifactReadPolicy
    entries: tuple[MaterializedArtifact, ...]

    def __post_init__(self) -> None:
        if type(self.request) is not ArtifactReadRequest or type(self.effective_policy) is not ArtifactReadPolicy:
            ArtifactReadDiagnostics.reject(CompilationFailure.READ_INVALID_REQUEST, 'Read plan requires actual request and effective bounded policy.')
        entries = _read_sequence(self.entries, MaterializedArtifact)
        selected = self.request.selection
        expected = tuple(e for e in self.request.receipt.artifacts if selected.mode is ArtifactReadSelectionMode.ALL_DECLARED_ARTIFACTS or e.descriptor.key in selected.keys)
        if not entries or entries != expected:
            ArtifactReadDiagnostics.reject(CompilationFailure.READ_INCOMPLETE_SET, 'Read plan must retain every selected receipt entry in manifest order.')
        object.__setattr__(self, 'entries', entries)

    @property
    def selected_keys(self) -> tuple[CompilationArtifactKey, ...]:
        return tuple(e.descriptor.key for e in self.entries)

    @property
    def complete_set(self) -> bool:
        return self.request.selection.mode is ArtifactReadSelectionMode.ALL_DECLARED_ARTIFACTS


@dataclass(frozen=True, slots=True)
class ArtifactReadPlanner:
    server_policy: ArtifactReadPolicy = field(default_factory=ArtifactReadPolicy)

    def __post_init__(self) -> None:
        if type(self.server_policy) is not ArtifactReadPolicy:
            ArtifactReadDiagnostics.reject(CompilationFailure.READ_INVALID_POLICY, 'Planner requires trusted bounded server policy.')

    def plan(self, request: ArtifactReadRequest) -> ArtifactReadPlan:
        reject = ArtifactReadDiagnostics.reject
        if type(request) is not ArtifactReadRequest:
            reject(CompilationFailure.READ_INVALID_REQUEST, 'Reader requires an actual immutable request.')
        manifest, receipt = request.manifest, request.receipt
        association = manifest.compilation_association
        try:
            RuntimeArtifactManifest(manifest.identity, manifest.schema_version, manifest.semantic_context, manifest.target, association, manifest.artifacts)
        except RuntimeArtifactManifestError as error:
            diagnostic = ArtifactReadDiagnostics.create(CompilationFailure.READ_MANIFEST_MISMATCH, 'Declared manifest structure is not valid for retrieval.', manifest=manifest)
            raise ArtifactReadError((*error.diagnostics, diagnostic)) from error
        original = association.request
        evidence = original.validation_evidence
        if association.output_origin.request is not original or association.output_origin.compiler is not association.compiler or evidence is None or evidence.status is not ModelValidationStatus.VALID or evidence.readiness is not CompilationReadiness.READY or evidence.validated_model is not original.canonical_model or original.canonical_model.scope != manifest.semantic_context or original.context.scope != manifest.semantic_context or original.context.target != manifest.target:
            reject(CompilationFailure.READ_MANIFEST_MISMATCH, 'Manifest must retain original accepted canonical/evidence/scope/target/output binding.', manifest=manifest)
        if any(o.status is not CompilationPhaseStatus.COMPLETED or o.executed is not True for o in association.phase_outcomes) or not any(CompilationCapability.EMIT_ARTIFACTS in o.descriptor.capabilities for o in association.phase_outcomes):
            reject(CompilationFailure.READ_MANIFEST_MISMATCH, 'Manifest must retain complete original final artifact phase evidence.', manifest=manifest)
        if receipt.manifest.identity != manifest.identity or receipt.compilation_association is not association or (receipt.manifest.schema_version, receipt.manifest.semantic_context, receipt.manifest.target, receipt.manifest.artifacts) != (manifest.schema_version, manifest.semantic_context, manifest.target, manifest.artifacts) or receipt.destination != request.source:
            reject(CompilationFailure.READ_RECEIPT_MISMATCH, 'Receipt must retain exact manifest declaration, original association and selected committed destination.', manifest=manifest)
        if type(receipt.artifacts) is not tuple or any(type(e) is not MaterializedArtifact or type(e.descriptor) is not RuntimeArtifactDescriptor or type(e.location) is not ArtifactRelativeLocation for e in receipt.artifacts):
            reject(CompilationFailure.READ_RECEIPT_MISMATCH, 'Receipt entries must preserve actual immutable typed descriptor and locator contracts.', manifest=manifest)
        if tuple(e.descriptor for e in receipt.artifacts) != manifest.artifacts or len({e.location for e in receipt.artifacts}) != len(receipt.artifacts):
            reject(CompilationFailure.READ_RECEIPT_MISMATCH, 'Receipt requires complete ordered descriptor membership and unique locations.', manifest=manifest)
        for entry in receipt.artifacts:
            try:
                ArtifactRelativeLocation(entry.location.value)
            except ArtifactWriteError as error:
                reject(CompilationFailure.READ_UNSAFE_PATH, 'Receipt location does not satisfy the existing safe committed filename contract.', manifest=manifest)
            if type(entry.byte_length) is not int or entry.byte_length < 0:
                reject(CompilationFailure.READ_RECEIPT_MISMATCH, 'Receipt must contain an actual nonnegative expected byte length.', manifest=manifest, entry=entry)
            if entry.verified_digest is not None:
                if type(entry.verified_digest) is not ArtifactContentDigest:
                    reject(CompilationFailure.READ_UNSUPPORTED_DIGEST, 'Digest evidence must use the approved explicit digest contract.', manifest=manifest, entry=entry, incomplete=True)
                try:
                    ArtifactContentDigest(entry.verified_digest.algorithm, entry.verified_digest.value)
                except ArtifactWriteError as error:
                    reject(CompilationFailure.READ_UNSUPPORTED_DIGEST, 'Receipt digest is malformed or unsupported; no inferred algorithm.', manifest=manifest, entry=entry, incomplete=True)
        selection = request.selection
        membership = {d.key for d in manifest.artifacts}
        for key in selection.keys:
            if key not in membership:
                reject(CompilationFailure.READ_UNKNOWN_ARTIFACT, 'Selected artifact identity is absent from the declared manifest.', manifest=manifest, key=key)
        entries = tuple(e for e in receipt.artifacts if selection.mode is ArtifactReadSelectionMode.ALL_DECLARED_ARTIFACTS or e.descriptor.key in selection.keys)
        policy = request.policy.bounded_by(self.server_policy)
        if len(entries) > policy.maximum_artifact_count:
            reject(CompilationFailure.READ_SIZE_LIMIT_EXCEEDED, 'Selected artifact count exceeds effective server-bounded limits.', manifest=manifest)
        total = 0
        for entry in entries:
            total += entry.byte_length
            if entry.byte_length > policy.maximum_artifact_bytes or total > policy.maximum_aggregate_bytes:
                reject(CompilationFailure.READ_SIZE_LIMIT_EXCEEDED, 'Declared selected bytes exceed effective server-bounded limits.', manifest=manifest, entry=entry)
            if policy.required_integrity is ArtifactReadIntegrity.DIGEST_VERIFIED and entry.verified_digest is None:
                reject(CompilationFailure.READ_REQUIRED_DIGEST_MISSING, 'Mandatory byte-digest evidence is unavailable; no silent downgrade.', manifest=manifest, entry=entry, incomplete=True)
        return ArtifactReadPlan(request, policy, entries)


@dataclass(frozen=True, slots=True)
class ArtifactReadVerification:
    expected_byte_length: int
    actual_byte_length: int
    verified_digest: ArtifactContentDigest | None = None

    def __post_init__(self) -> None:
        if type(self.expected_byte_length) is not int or type(self.actual_byte_length) is not int or self.expected_byte_length < 0 or self.actual_byte_length != self.expected_byte_length or self.verified_digest is not None and type(self.verified_digest) is not ArtifactContentDigest:
            raise ValueError('Verification records actual equal byte lengths and optional approved verified digest.')

    @property
    def integrity(self) -> ArtifactReadIntegrity:
        return ArtifactReadIntegrity.SIZE_VERIFIED if self.verified_digest is None else ArtifactReadIntegrity.DIGEST_VERIFIED


@dataclass(frozen=True, slots=True)
class RetrievedArtifact:
    descriptor: RuntimeArtifactDescriptor
    location: ArtifactRelativeLocation
    content: bytes = field(repr=False)
    verification: ArtifactReadVerification

    def __post_init__(self) -> None:
        if type(self.descriptor) is not RuntimeArtifactDescriptor or type(self.location) is not ArtifactRelativeLocation or type(self.content) is not bytes or type(self.verification) is not ArtifactReadVerification:
            raise TypeError('Retrieved artifact is immutable descriptor/location/exact bytes/read evidence, not compiler output.')
        if len(self.content) != self.verification.actual_byte_length:
            raise ValueError('Retrieved content length must match actual recorded verification.')


@dataclass(frozen=True, slots=True)
class ArtifactReadResult:
    status: CompilationStatus
    plan: ArtifactReadPlan | None = None
    artifacts: tuple[RetrievedArtifact, ...] = ()
    diagnostics: tuple[CompilationDiagnostic, ...] = ()

    def __post_init__(self) -> None:
        if type(self.status) is not CompilationStatus or self.plan is not None and type(self.plan) is not ArtifactReadPlan:
            raise TypeError('Read result requires established status and optional actual selected plan.')
        artifacts = _read_sequence(self.artifacts, RetrievedArtifact)
        diagnostics = _read_sequence(self.diagnostics, CompilationDiagnostic)
        if self.status is CompilationStatus.SUCCEEDED:
            if self.plan is None or len(artifacts) != len(self.plan.entries) or any(d.severity is TypeValidationSeverity.ERROR for d in diagnostics):
                raise ValueError('Read success requires all selected artifacts and no errors.')
            if len(artifacts) > self.plan.effective_policy.maximum_artifact_count or self.plan.effective_policy.required_integrity is ArtifactReadIntegrity.DIGEST_VERIFIED and any(a.verification.verified_digest is None for a in artifacts):
                raise ValueError('Successful read must respect effective count and mandatory digest requirements.')
            for artifact, entry in zip(artifacts, self.plan.entries):
                if (artifact.descriptor, artifact.location, artifact.verification.expected_byte_length, artifact.verification.verified_digest) != (entry.descriptor, entry.location, entry.byte_length, entry.verified_digest):
                    raise ValueError('Successful read must preserve selected committed identity/location/length/digest facts.')
            if sum(len(a.content) for a in artifacts) > self.plan.effective_policy.maximum_aggregate_bytes or any(len(a.content) > self.plan.effective_policy.maximum_artifact_bytes for a in artifacts):
                raise ValueError('Successful retrieved bytes must respect effective limits.')
        elif artifacts or not diagnostics:
            raise ValueError('Non-success has diagnostics and exposes no partial retrieved payloads.')
        object.__setattr__(self, 'artifacts', artifacts)
        object.__setattr__(self, 'diagnostics', diagnostics)


class ArtifactReader(Protocol):
    def read(self, request: ArtifactReadRequest) -> ArtifactReadResult:
        ...


_LEGACY_DIAGNOSTIC_OWNERS = MappingProxyType({**_LEGACY_DIAGNOSTIC_OWNERS,
    **{code: CompilationDiagnosticOrigin.RESULT for code in CompilationFailure if code.name.startswith('READ_')}})

__all__ += ['ArtifactReadStage', 'ArtifactReadSourceType', 'ArtifactReadSource',
            'ArtifactReadSelectionMode', 'ArtifactReadIntegrity', 'ArtifactReadError',
            'ArtifactReadDiagnostics', 'ArtifactReadSelection', 'ArtifactReadPolicy',
            'ArtifactReadRequest', 'ArtifactReadPlan', 'ArtifactReadPlanner',
            'ArtifactReadVerification', 'RetrievedArtifact', 'ArtifactReadResult', 'ArtifactReader']
