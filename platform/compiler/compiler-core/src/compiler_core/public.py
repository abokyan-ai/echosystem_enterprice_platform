"""CMP-01 deterministic compiler foundation; no concrete generators or hosting."""
from dataclasses import dataclass, field, is_dataclass, replace
from collections import Counter, deque
from enum import Enum
from typing import Protocol, Mapping
from types import MappingProxyType
import re
from semantic_kernel.public import SemanticContextRef, SemanticElementId, ElementVersionRef, SemanticVersion
from model_core.public import CanonicalModel, TypeValidationSeverity
from model_authoring.public import (
    ModelValidationResult, ModelValidationStatus, CompilationReadiness,
    CanonicalSourceAssociation, ModelDiagnosticContext, ModelDiagnosticEntry,
    ModelDiagnosticOrigin, ModelDiagnosticTarget, ModelDiagnosticTargetKind,
    associate_model_diagnostic, CompilationDiagnosticReport, CompilerPhaseDiagnosticView,
    CompilationDiagnosticOrigin, CompilationDiagnosticDetails, CompilationArtifactDiagnosticView,
    AuthoringSchemaPath,
)
from compiled_contracts.public import CompilationArtifact, CompilationArtifactKey, CompilationArtifactKind

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

    def __post_init__(self) -> None:
        if self.artifact_target is not None and type(self.artifact_target) is not CompilationArtifactTarget:
            raise TypeError('Artifact target must be a bounded association.')
        if self.ir_identity is not None and type(self.ir_identity) is not SemanticIRId:
            raise TypeError('IR diagnostic identity is independent of semantic/artifact identity.')
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

    def __post_init__(self) -> None:
        if type(self.status) is not CompilationStatus or self.target is not None and type(self.target) is not CompilationTargetId:
            raise TypeError('Compiler result requires explicit status/target.')
        for name, expected in (('diagnostics', CompilationDiagnostic), ('phase_outcomes', CompilationPhaseOutcome)):
            values = getattr(self, name)
            if type(values) not in (tuple, list) or any(type(v) is not expected for v in values):
                raise TypeError('Compiler result requires immutable typed outcome sequences.')
            object.__setattr__(self, name, tuple(values))
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

    def __post_init__(self) -> None:
        if type(self.additional_phases) not in (tuple, list):
            raise TypeError('Compiler composition requires explicit ordered phase implementations.')
        phases = tuple(self.additional_phases)
        descriptors = [CompilationPreparationPhase().descriptor]
        for phase in phases:
            descriptor = getattr(phase, 'descriptor', None)
            if type(descriptor) is not CompilationPhaseDescriptor or not callable(getattr(phase, 'execute', None)):
                raise TypeError('Compiler phase must implement the explicit descriptor/execute protocol.')
            descriptors.append(descriptor)
        ids = [d.id for d in descriptors]
        if len(set(ids)) != len(ids):
            raise ValueError('Duplicate phases cannot replace mandatory preparation.')
        positions = {id: i for i, id in enumerate(ids)}
        for descriptor in descriptors:
            if any(p in positions and positions[p] >= positions[descriptor.id] for p in descriptor.prerequisites):
                raise ValueError('Configured prerequisites must precede their consumer; no dependency scheduler/reordering.')
        object.__setattr__(self, 'additional_phases', phases)
        object.__setattr__(self, '_descriptors', tuple(descriptors))

    @property
    def phases(self) -> tuple[CompilationPhase, ...]:
        return (CompilationPreparationPhase(), *self.additional_phases)

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
        return CompilationResult(status, request.context.target, diagnostics, outcomes, state.preparation if status is CompilationStatus.SUCCEEDED else None, state.artifacts if status is CompilationStatus.SUCCEEDED else CompilationArtifactCollection(), evidence, context)


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


# Closed v0 payload type; future extensions must add explicitly owned immutable contracts.
SemanticIRPayload = SemanticIRFoundationPayload


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
        if self.payload_kind is not SemanticIRPayloadKind.FOUNDATION_COORDINATES:
            _ir_reject(CompilationFailure.IR_UNSUPPORTED_KIND, 'Only the explicit foundation-coordinate payload contract is supported.', identity=identity)
        if self.payload is None:
            _ir_reject(CompilationFailure.IR_MISSING_PAYLOAD, 'Mandatory IR payload cannot be absent.', identity=identity)
        if type(self.payload) is not SemanticIRFoundationPayload:
            _ir_reject(CompilationFailure.IR_PAYLOAD_MISMATCH, 'IR does not accept mutable bags, arbitrary implementations or artifact payloads.', identity=identity)
        if type(self.model_wide) is not bool or type(self.definition_origins) not in (tuple, list) or any(type(r) is not ElementVersionRef or type(r.element_id) is not SemanticElementId or type(r.version) is not SemanticVersion for r in self.definition_origins):
            _ir_reject(CompilationFailure.IR_INVALID_ENVELOPE, 'Origins require explicit exact references and a boolean model-wide declaration.', identity=identity)
        origins = tuple(self.definition_origins)
        if len(set(origins)) != len(origins) or not origins and not self.model_wide or origins != self.payload.definitions:
            _ir_reject(CompilationFailure.IR_PAYLOAD_MISMATCH, 'Foundation coordinates must match ordered exact origins; empty origins require explicit model-wide scope.', identity=identity)
        for reference in origins:
            if not request.canonical_model.contains(reference):
                _ir_reject(CompilationFailure.IR_INPUT_MISMATCH, 'IR origin is outside its exact canonical snapshot.', identity=identity, reference=reference)
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
        if required_kind is not SemanticIRPayloadKind.FOUNDATION_COORDINATES:
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
