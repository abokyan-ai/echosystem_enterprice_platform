"""CMP-01 deterministic compiler foundation; no concrete generators or hosting."""
from dataclasses import dataclass, field, is_dataclass
from enum import Enum
from typing import Protocol, Mapping
from types import MappingProxyType
import re
from semantic_kernel.public import SemanticContextRef, SemanticElementId, ElementVersionRef
from model_core.public import CanonicalModel, TypeValidationSeverity
from model_authoring.public import (
    ModelValidationResult, ModelValidationStatus, CompilationReadiness,
    CanonicalSourceAssociation, ModelDiagnosticContext, ModelDiagnosticEntry,
    ModelDiagnosticOrigin, ModelDiagnosticTarget, ModelDiagnosticTargetKind,
    associate_model_diagnostic, CompilationDiagnosticReport, CompilerPhaseDiagnosticView,
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


def _phase_id(value: str) -> None:
    if type(value) is not str or re.fullmatch(r'CMP-PHASE-[A-Z0-9]+(?:-[A-Z0-9]+)*', value) is None:
        raise ValueError('Phase requires a stable CMP-PHASE identifier.')


@dataclass(frozen=True, slots=True)
class CompilationDiagnostic:
    """Narrow compiler prerequisite/capability seam pending full SK-11."""
    code: CompilationFailure
    message: str
    severity: TypeValidationSeverity
    phase_id: str | None = None
    reference: ElementVersionRef | None = None
    cause_code: str | None = None

    def __post_init__(self) -> None:
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

    def __post_init__(self) -> None:
        if self.preparation is not None and type(self.preparation) is not PreparedCompilationInput or type(self.artifacts) is not CompilationArtifactCollection:
            raise TypeError('Compiler state uses explicit preparation/artifact contracts, never a metadata bag.')


@dataclass(frozen=True, slots=True)
class CompilationPhaseResult:
    status: CompilationPhaseStatus
    diagnostics: tuple[CompilationDiagnostic, ...] = ()
    preparation: PreparedCompilationInput | None = None
    artifacts: tuple[CompilationArtifact, ...] = ()
    reason: str | None = None

    def __post_init__(self) -> None:
        if type(self.status) is not CompilationPhaseStatus or type(self.diagnostics) not in (tuple, list) or any(type(d) is not CompilationDiagnostic for d in self.diagnostics):
            raise TypeError('Phase result requires explicit status and typed diagnostics.')
        object.__setattr__(self, 'diagnostics', tuple(self.diagnostics))
        object.__setattr__(self, 'artifacts', _artifacts(self.artifacts))
        if self.preparation is not None and type(self.preparation) is not PreparedCompilationInput:
            raise TypeError('Phase preparation must use its explicit contract.')
        if self.status is not CompilationPhaseStatus.COMPLETED:
            if self.artifacts or self.preparation is not None:
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

    def __post_init__(self) -> None:
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
        diagnostic_membership = frozenset(self.diagnostics)
        if any(d not in diagnostic_membership for o in self.phase_outcomes for d in o.diagnostics):
            raise ValueError('Compiler result must preserve every phase diagnostic.')
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
        return CompilationDiagnosticReport(self.status.value, None if self.target is None else self.target.value, self.diagnostic_entries, tuple(CompilerPhaseDiagnosticView(o.descriptor.id, o.status.value, o.reason) for o in self.phase_outcomes), self.validation_evidence)

    @property
    def diagnostic_entries(self) -> tuple[ModelDiagnosticEntry, ...]:
        validation = () if self.validation_evidence is None else tuple(associate_model_diagnostic(d, self.diagnostic_context) for d in self.validation_evidence.diagnostics)
        compiler = []
        for d in self.diagnostics:
            target = None if d.reference is None else ModelDiagnosticTarget(ModelDiagnosticTargetKind.DEFINITION, d.reference)
            compiler.append(ModelDiagnosticEntry(d, target=target, source_path=self.diagnostic_context.source_path(target), extension_origin=ModelDiagnosticOrigin.COMPILER))
        return (*validation, *compiler)


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
                outcomes.append(CompilationPhaseOutcome(descriptor, CompilationPhaseStatus.SKIPPED, reason='Blocked by ' + blocker + '.'))
                continue
            missing = tuple(p for p in descriptor.prerequisites if p not in completed)
            if missing or request.context.target not in descriptor.targets:
                d = CompilationDiagnostic(CompilationFailure.PHASE_UNAVAILABLE, 'Required phase prerequisite or explicitly declared target support is unavailable.', TypeValidationSeverity.WARNING, descriptor.id)
                diagnostics.append(d)
                outcomes.append(CompilationPhaseOutcome(descriptor, CompilationPhaseStatus.INCOMPLETE, (d,), 'Phase prerequisites/target capability are unavailable.'))
                blocker, status = descriptor.id, CompilationStatus.INCOMPLETE
                continue
            result = phase.execute(request, state)
            if type(result) is not CompilationPhaseResult or any(d.phase_id is not None and d.phase_id != descriptor.id for d in result.diagnostics):
                raise TypeError('Phase implementation violated its result/diagnostic origin contract.')
            diagnostics.extend(result.diagnostics)
            if result.status is not CompilationPhaseStatus.COMPLETED:
                phase_diagnostics = result.diagnostics
                if result.status is CompilationPhaseStatus.FAILED and not any(d.severity is TypeValidationSeverity.ERROR for d in phase_diagnostics):
                    d = CompilationDiagnostic(CompilationFailure.PHASE_FAILED, 'Configured compiler phase explicitly failed.', TypeValidationSeverity.ERROR, descriptor.id)
                    diagnostics.append(d)
                    phase_diagnostics = (*phase_diagnostics, d)
                outcomes.append(CompilationPhaseOutcome(descriptor, result.status, phase_diagnostics, result.reason))
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
                artifacts = CompilationArtifactCollection((*state.artifacts.artifacts, *result.artifacts))
            except CompilationArtifactConflict:
                d = CompilationDiagnostic(CompilationFailure.ARTIFACT_CONFLICT, 'Duplicate artifact key conflicts with atomic deterministic output membership.', TypeValidationSeverity.ERROR, descriptor.id)
                diagnostics.append(d)
                outcomes.append(CompilationPhaseOutcome(descriptor, CompilationPhaseStatus.FAILED, (*result.diagnostics, d), 'Artifact key conflict.'))
                blocker, status = descriptor.id, CompilationStatus.FAILED
                continue
            state = CompilationState(preparation, artifacts)
            outcomes.append(CompilationPhaseOutcome(descriptor, CompilationPhaseStatus.COMPLETED, result.diagnostics))
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
