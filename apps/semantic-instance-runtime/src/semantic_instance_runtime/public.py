"""RUN-03 orchestration around authoritative TYPE-08 contracts when available.

No TYPE-08 implementation exists in this revision. Opaque Protocols below are
integration ports, not new identity, value or instance representations. An owner
must supply the actual canonical classes and their approved immutable adapter.
No successful instance can be produced by the default unavailable integration.
"""
from __future__ import annotations

from dataclasses import dataclass, field, fields, is_dataclass, replace
from datetime import date, datetime, timezone
from decimal import Decimal
from enum import Enum
from typing import Protocol
from uuid import UUID
from types import MappingProxyType
import re
from concurrent.futures import CancelledError as FutureCancelledError

from semantic_kernel.public import (SemanticContextRef, SemanticElementId,
    SemanticVersion, ElementVersionRef, ElementRef, PrimitiveTypes)
from model_core.public import (FieldId, FieldName, FieldDefinition, FieldConstraintSet,
    FieldPresence, FieldNullability, PrimitiveTypeRef, SemanticTypeRef,
    ConstraintKind, ConstraintKinds, MinimumConstraint, MaximumConstraint,
    MinLengthConstraint, MaxLengthConstraint, PatternConstraint, PrecisionConstraint,
    ScaleConstraint, NumericConstraintValue, primitive_constraint_kinds)
from compiled_contracts.public import RuntimeCapabilityId, RuntimeTargetId, CompilationArtifactKey, CompilationArtifactKind
from runtime_core.public import (RuntimeArtifactLoadStatus, RuntimeLoadSeverity,
    RuntimeArtifactLoadFailure, RuntimeArtifactReaderDiagnostic, RuntimeArtifactLoadResult, RuntimeModelRegistryOperation,
    RuntimeModelRegistrationResult, RuntimeModelMembershipResult,
    RuntimeModelVersionInspectionResult, RuntimeModelRegistrySnapshotResult,
    ExecutionContext, ExecutionContextCreationResult, ExecutionContextDiagnostic,
    ExecutionContextFailure, RuntimeInvocationId, ExecutionCorrelationId, ExecutionCausationRef,
    RuntimeArtifactLoadDiagnostic, RuntimeArtifactLoadError,
    RuntimeArtifactDecoderRegistration, RuntimeModelRegistry, RuntimeModelRegistryScope,
    RuntimeModelDefinition, RuntimeModelDefinitionKind, RuntimeModelRegistrySnapshot,
    RuntimeModelLookupRequest, RuntimeModelLookupResult, RuntimeModelLookupStatus)

MODULE_NAME = 'semantic-instance-runtime'


class SemanticInstanceIdentity(Protocol):
    """Opaque existing TYPE-08 InstanceId, admitted only by exact class approval."""


class SemanticFieldValue(Protocol):
    """Opaque existing TYPE-08 Missing/Null/Value, never an arbitrary object value."""


class SemanticInstance(Protocol):
    """Port for the existing TYPE-08 value, not a competing concrete instance."""


RuntimePrimitiveValue = str | bool | int | Decimal | date | datetime | UUID


class RuntimeInstanceValueKind(Enum):
    """Inspection tags only; these do not implement TYPE-08 sentinels."""
    MISSING = 'missing'
    NULL = 'null'
    VALUE = 'value'


class RuntimeInstanceOperation(Enum):
    CREATE = 'create'
    UPDATE = 'update'
    INSPECT = 'inspect'


class RuntimeInstanceFailure(Enum):
    INVALID_REQUEST = 'RUN-201'
    AUTHORIZATION_UNAVAILABLE = 'RUN-202'
    AUTHORIZATION_MISMATCH = 'RUN-203'
    INVALID_SCOPE = 'RUN-204'
    DEFINITION_NOT_FOUND = 'RUN-205'
    VERSION_REQUIRED = 'RUN-206'
    DEFINITION_MISMATCH = 'RUN-207'
    CONTEXT_MISMATCH = 'RUN-208'
    INVALID_IDENTITY = 'RUN-209'
    UNKNOWN_FIELD = 'RUN-210'
    DUPLICATE_FIELD = 'RUN-211'
    REQUIRED_FIELD_MISSING = 'RUN-212'
    NULL_NOT_ALLOWED = 'RUN-213'
    PRIMITIVE_TYPE_MISMATCH = 'RUN-214'
    CONSTRAINT_VIOLATION = 'RUN-215'
    UNSUPPORTED_FIELD_VALUE = 'RUN-216'
    VALIDATION_UNAVAILABLE = 'RUN-217'
    REVISION_MISMATCH = 'RUN-218'
    INTEGRITY_FAILURE = 'RUN-219'
    TYPE08_UNAVAILABLE = 'RUN-220'
    RESOURCE_LIMIT_EXCEEDED = 'RUN-221'
    LOOKUP_UNAVAILABLE = 'RUN-222'


def _typed_tuple(value: object, expected: type) -> bool:
    return type(value) is tuple and all(type(v) is expected for v in value)


def _frozen_type(value: object) -> bool:
    return isinstance(value, type) and is_dataclass(value) and value.__dataclass_params__.frozen and hasattr(value, '__slots__')


def _immutable(value: object, approved: tuple[type, ...], maximum_nodes: int,
               maximum_depth: int, maximum_scalar_units: int) -> bool:
    """Closed bounded field/instance graph admission; never reflective presentation."""
    stack = [(value, 0, frozenset())]
    count = units = 0
    leaves = (FieldId, FieldName, SemanticContextRef, SemanticElementId,
              SemanticVersion, ElementVersionRef, ElementRef)
    while stack:
        node, depth, ancestors = stack.pop()
        count += 1
        if count > maximum_nodes or depth > maximum_depth:
            return False
        t = type(node)
        children = ()
        if node is None or t in (bool, UUID, date):
            pass
        elif t is datetime:
            if node.tzinfo is not None and type(node.tzinfo) is not timezone:
                return False
        elif t is str:
            units += len(node)
        elif t is int:
            units += max(1, node.bit_length() // 8 + 1)
        elif t is Decimal:
            if not node.is_finite():
                return False
            units += len(node.as_tuple().digits) + abs(node.as_tuple().exponent)
        elif t is tuple:
            children = node
        elif t in (*approved, *leaves):
            if not _frozen_type(t) or hasattr(node, '__dict__'):
                return False
            children = tuple(getattr(node, f.name) for f in fields(t))
        else:
            return False
        if units > maximum_scalar_units or count + len(stack) + len(children) > maximum_nodes:
            return False
        if children:
            if id(node) in ancestors:
                return False
            next_ancestors = ancestors | {id(node)}
            stack.extend((child, depth + 1, next_ancestors) for child in reversed(children))
    return True


@dataclass(frozen=True, slots=True)
class RuntimeInstancePolicy:
    maximum_fields: int = 1024
    maximum_value_nodes: int = 100000
    maximum_value_depth: int = 32
    maximum_scalar_units: int = 1024 * 1024
    maximum_revision: int = 2 ** 63 - 1

    def __post_init__(self) -> None:
        if any(type(getattr(self, f.name)) is not int or getattr(self, f.name) <= 0 for f in fields(self)):
            raise ValueError('Instance budgets require positive actual integers.')


@dataclass(frozen=True, slots=True)
class RuntimeInstanceContext:
    scope: RuntimeModelRegistryScope
    snapshot: RuntimeModelRegistrySnapshot | None = field(default=None, repr=False)

    def __post_init__(self) -> None:
        if type(self.scope) is not RuntimeModelRegistryScope:
            raise TypeError('Runtime context uses the actual explicit RUN-02 scope.')
        if self.snapshot is not None and (type(self.snapshot) is not RuntimeModelRegistrySnapshot or self.snapshot.scope != self.scope):
            raise ValueError('Supplied coherent definition view must match the context scope.')


@dataclass(frozen=True, slots=True)
class RuntimeInstanceRevision:
    """Local state lineage only, not store CAS, SemanticVersion or a global clock."""
    value: int

    def __post_init__(self) -> None:
        if type(self.value) is not int or self.value < 0:
            raise ValueError('Revision requires a non-negative actual integer.')


@dataclass(frozen=True, slots=True)
class RuntimeInstanceFieldAssignment:
    field_id: FieldId
    value: SemanticFieldValue = field(repr=False)

    def __post_init__(self) -> None:
        if type(self.field_id) is not FieldId:
            raise TypeError('Values/changes are keyed by existing stable FieldId.')
        # The actual canonical value class is checked against the owner-supplied
        # TYPE-08 support before authorization and before any semantic operation.


@dataclass(frozen=True, slots=True)
class RuntimeInstanceValueView:
    kind: RuntimeInstanceValueKind
    primitive: RuntimePrimitiveValue | None = field(default=None, repr=False)

    def __post_init__(self) -> None:
        if type(self.kind) is not RuntimeInstanceValueKind:
            raise TypeError('Value inspection uses explicit Missing/Null/Value tags.')
        if self.kind is RuntimeInstanceValueKind.VALUE:
            if type(self.primitive) not in (str, bool, int, Decimal, date, datetime, UUID):
                raise TypeError('Only exact immutable supported primitive representations are projected.')
        elif self.primitive is not None:
            raise ValueError('Missing and Null projections carry no primitive payload.')


@dataclass(frozen=True, slots=True)
class RuntimeInstanceStateView:
    """Narrow canonical TYPE-08 inspection projection; no second instance object."""
    instance_identity: SemanticInstanceIdentity = field(repr=False)
    definition_identity: ElementVersionRef
    semantic_context: SemanticContextRef
    values: tuple[RuntimeInstanceFieldAssignment, ...] = field(repr=False)

    def __post_init__(self) -> None:
        if type(self.definition_identity) is not ElementVersionRef or type(self.semantic_context) is not SemanticContextRef or not _typed_tuple(self.values, RuntimeInstanceFieldAssignment):
            raise TypeError('Canonical state projection preserves typed binding and field inventory.')


class SemanticInstanceContractAdapter(Protocol):
    """Trusted TYPE-08 owner implements these around its actual canonical classes."""
    def valid_identity(self, identity: SemanticInstanceIdentity) -> bool: ...
    def inspect_value(self, value: SemanticFieldValue) -> RuntimeInstanceValueView | None:
        """None explicitly means this canonical value has no supported primitive projection."""
        ...
    def missing(self) -> SemanticFieldValue: ...
    def inspect_instance(self, instance: SemanticInstance) -> RuntimeInstanceStateView: ...
    def construct(self, identity: SemanticInstanceIdentity, definition: ElementVersionRef,
                  context: SemanticContextRef, values: tuple[RuntimeInstanceFieldAssignment, ...]) -> SemanticInstance: ...


@dataclass(frozen=True, slots=True, eq=False)
class RuntimeSemanticInstanceContractSupport:
    """Explicit canonical-class approval, never discovered/imported from a request.

    There is no actual approval or adapter in this revision. Supply the real
    TYPE-08 classes later; marker Protocols cannot qualify as concrete classes.
    """
    identity_type: type
    instance_type: type
    missing_type: type
    null_type: type
    value_type: type
    adapter: SemanticInstanceContractAdapter = field(repr=False)
    nested_types: tuple[type, ...] = ()

    def __post_init__(self) -> None:
        types = self.value_types + (self.identity_type, self.instance_type)
        if len(set(types)) != 5 or not all(_frozen_type(t) for t in types) or any(t in (SemanticElementId, FieldId, ElementVersionRef, ElementRef) for t in types):
            raise TypeError('Distinct actual frozen/slotted TYPE-08 identity/instance/value classes are required.')
        if type(self.nested_types) is not tuple or len(self.nested_types) > 128 or len(set(self.nested_types)) != len(self.nested_types) or not all(_frozen_type(t) for t in self.nested_types):
            raise TypeError('Additional immutable canonical nested classes need bounded explicit approval.')
        if not _frozen_type(type(self.adapter)) or not _immutable(self.adapter, (type(self.adapter),), 1024, 16, 4096):
            raise TypeError('Canonical TYPE-08 adapter has immutable configuration, never request callbacks.')
        if not all(callable(getattr(type(self.adapter), name, None)) for name in ('valid_identity', 'inspect_value', 'missing', 'inspect_instance', 'construct')):
            raise TypeError('Canonical contract adapter must implement all explicit operations.')

    @property
    def value_types(self) -> tuple[type, ...]:
        return (self.missing_type, self.null_type, self.value_type)

    @property
    def approved_types(self) -> tuple[type, ...]:
        return (self.identity_type, self.instance_type, *self.value_types, *self.nested_types)


@dataclass(frozen=True, slots=True, eq=False)
class RuntimeInstanceIdentityAssociation:
    """Retain the actual canonical identity without revealing its value in repr."""
    support: RuntimeSemanticInstanceContractSupport = field(repr=False)
    identity: SemanticInstanceIdentity = field(repr=False)

    def __post_init__(self) -> None:
        if type(self.support) is not RuntimeSemanticInstanceContractSupport or type(self.identity) is not self.support.identity_type or not _immutable(self.identity, self.support.approved_types, 1024, 16, 4096) or self.support.adapter.valid_identity(self.identity) is not True:
            raise TypeError('Diagnostic association needs an actual validated canonical InstanceId.')


@dataclass(frozen=True, slots=True)
class RuntimeInstanceDiagnostic:
    """Narrow instance association seam using existing runtime status/severity/causes.

    General SK-11 is absent. This is not a compiler diagnostic or a new generic
    diagnostic framework; field contents and exception representations are absent.
    """
    code: RuntimeInstanceFailure
    message: str
    severity: RuntimeLoadSeverity
    operation: RuntimeInstanceOperation
    scope: RuntimeModelRegistryScope | None = None
    definition_identity: ElementVersionRef | None = None
    instance_identity: RuntimeInstanceIdentityAssociation | None = field(default=None, repr=False)
    field_id: FieldId | None = None
    constraint_kind: ConstraintKind | None = None
    expected_revision: RuntimeInstanceRevision | None = None
    registry_causes: tuple[RuntimeArtifactLoadDiagnostic, ...] = ()

    def __post_init__(self) -> None:
        if type(self.code) is not RuntimeInstanceFailure or type(self.message) is not str or not self.message or type(self.severity) is not RuntimeLoadSeverity or type(self.operation) is not RuntimeInstanceOperation:
            raise TypeError('Instance diagnostics preserve closed codes and runtime severity.')
        for value, expected in ((self.scope, RuntimeModelRegistryScope), (self.definition_identity, ElementVersionRef), (self.instance_identity, RuntimeInstanceIdentityAssociation), (self.field_id, FieldId), (self.constraint_kind, ConstraintKind), (self.expected_revision, RuntimeInstanceRevision)):
            if value is not None and type(value) is not expected:
                raise TypeError('Instance diagnostics use actual typed associations.')
        if not _typed_tuple(self.registry_causes, RuntimeArtifactLoadDiagnostic):
            raise TypeError('Original RUN-02 diagnostic causes remain typed and immutable.')


class RuntimeInstanceError(ValueError):
    def __init__(self, diagnostics: tuple[RuntimeInstanceDiagnostic, ...], status: RuntimeArtifactLoadStatus = RuntimeArtifactLoadStatus.FAILED, validation_result: RuntimeValidationResult | None = None):
        if not _typed_tuple(diagnostics, RuntimeInstanceDiagnostic) or not diagnostics or status not in (RuntimeArtifactLoadStatus.FAILED, RuntimeArtifactLoadStatus.INCOMPLETE):
            raise TypeError('Expected instance rejection has actual diagnostics and non-success status.')
        self.diagnostics, self.status = diagnostics, status
        self.validation_result = validation_result
        super().__init__('Instance operation rejected; inspect structured diagnostics.')


@dataclass(frozen=True, slots=True)
class RuntimeInstanceState:
    """Compatible metadata wrapper; the sole value-bearing object is TYPE-08."""
    instance: SemanticInstance = field(repr=False)
    context: RuntimeInstanceContext
    definition: RuntimeModelDefinition = field(repr=False)
    revision: RuntimeInstanceRevision
    contract_support: RuntimeSemanticInstanceContractSupport = field(repr=False)

    def __post_init__(self) -> None:
        if type(self.context) is not RuntimeInstanceContext or type(self.definition) is not RuntimeModelDefinition or self.definition.key.scope != self.context.scope or type(self.revision) is not RuntimeInstanceRevision or type(self.contract_support) is not RuntimeSemanticInstanceContractSupport or type(self.instance) is not self.contract_support.instance_type:
            raise TypeError('Metadata wrapper requires original canonical instance, exact definition and scope.')


@dataclass(frozen=True, slots=True)
class RuntimeInstanceCreateRequest:
    context: RuntimeInstanceContext
    instance_identity: SemanticInstanceIdentity = field(repr=False)
    definition_identity: ElementVersionRef | ElementRef
    values: tuple[RuntimeInstanceFieldAssignment, ...] = field(default=(), repr=False)

    def __post_init__(self) -> None:
        if type(self.context) is not RuntimeInstanceContext or type(self.definition_identity) not in (ElementVersionRef, ElementRef) or not _typed_tuple(self.values, RuntimeInstanceFieldAssignment):
            raise TypeError('Create requires explicit context/reference and immutable FieldId assignments.')


@dataclass(frozen=True, slots=True)
class RuntimeInstanceUpdateRequest:
    context: RuntimeInstanceContext
    state: RuntimeInstanceState = field(repr=False)
    definition_identity: ElementVersionRef | ElementRef
    changes: tuple[RuntimeInstanceFieldAssignment, ...] = field(repr=False)
    expected_revision: RuntimeInstanceRevision

    def __post_init__(self) -> None:
        if type(self.context) is not RuntimeInstanceContext or type(self.state) is not RuntimeInstanceState or type(self.definition_identity) not in (ElementVersionRef, ElementRef) or not _typed_tuple(self.changes, RuntimeInstanceFieldAssignment) or type(self.expected_revision) is not RuntimeInstanceRevision:
            raise TypeError('Update requires immutable state, explicit changes and expected local revision.')


@dataclass(frozen=True, slots=True)
class RuntimeInstanceInspectRequest:
    context: RuntimeInstanceContext
    state: RuntimeInstanceState = field(repr=False)
    field_id: FieldId | None = None

    def __post_init__(self) -> None:
        if type(self.context) is not RuntimeInstanceContext or type(self.state) is not RuntimeInstanceState or self.field_id is not None and type(self.field_id) is not FieldId:
            raise TypeError('Inspection selects a typed FieldId or explicit complete instance view.')


@dataclass(frozen=True, slots=True, eq=False)
class RuntimeInstanceServiceBinding:
    scopes: tuple[RuntimeModelRegistryScope, ...]

    def __post_init__(self) -> None:
        if type(self.scopes) is not tuple or not 1 <= len(self.scopes) <= 128 or not _typed_tuple(self.scopes, RuntimeModelRegistryScope) or len(set(self.scopes)) != len(self.scopes):
            raise TypeError('Service owner explicitly declares bounded distinct scopes.')


@dataclass(frozen=True, slots=True, eq=False)
class RuntimeInstanceAuthorizationRequest:
    binding: RuntimeInstanceServiceBinding
    operation: RuntimeInstanceOperation
    request: RuntimeInstanceCreateRequest | RuntimeInstanceUpdateRequest | RuntimeInstanceInspectRequest = field(repr=False)

    def __post_init__(self) -> None:
        expected = {RuntimeInstanceOperation.CREATE: RuntimeInstanceCreateRequest, RuntimeInstanceOperation.UPDATE: RuntimeInstanceUpdateRequest, RuntimeInstanceOperation.INSPECT: RuntimeInstanceInspectRequest}.get(self.operation)
        if type(self.binding) is not RuntimeInstanceServiceBinding or expected is None or type(self.request) is not expected or self.request.context.scope not in self.binding.scopes:
            raise TypeError('Authority invocation is bound to this service, operation and original scoped request.')


@dataclass(frozen=True, slots=True, eq=False)
class RuntimeInstanceAuthority:
    request: RuntimeInstanceAuthorizationRequest = field(repr=False)
    authority_source: str
    decision_identity: str

    def __post_init__(self) -> None:
        if type(self.request) is not RuntimeInstanceAuthorizationRequest or any(type(v) is not str or not 1 <= len(v) <= 160 or not all(c.isascii() and (c.isalnum() or c in '._:-') for c in v) for v in (self.authority_source, self.decision_identity)):
            raise TypeError('Authority uses an actual invocation and non-secret logical decision tokens.')


class RuntimeInstanceAuthorizer(Protocol):
    def authorize(self, request: RuntimeInstanceAuthorizationRequest) -> RuntimeInstanceAuthority: ...


@dataclass(frozen=True, slots=True)
class RuntimeInstanceDefinitionSchema:
    definition: RuntimeModelDefinition = field(repr=False)
    fields: tuple[FieldDefinition, ...]
    required_capabilities: tuple[RuntimeCapabilityId, ...] = ()

    def __post_init__(self) -> None:
        if type(self.definition) is not RuntimeModelDefinition or not _typed_tuple(self.fields, FieldDefinition) or not _typed_tuple(self.required_capabilities, RuntimeCapabilityId) or len(set(self.required_capabilities)) != len(self.required_capabilities):
            raise TypeError('Schema projection selects original existing typed fields and explicit capabilities.')


class RuntimeInstanceSchemaProjector(Protocol):
    def project(self, definition: RuntimeModelDefinition, maximum_fields: int) -> RuntimeInstanceDefinitionSchema: ...


@dataclass(frozen=True, slots=True, eq=False)
class RuntimeInstanceDefinitionSupport:
    decoder_registration: RuntimeArtifactDecoderRegistration = field(repr=False)
    definition_type: type
    definition_kind: RuntimeModelDefinitionKind
    projector: RuntimeInstanceSchemaProjector = field(repr=False)
    instance_schema_complete: bool = False

    def __post_init__(self) -> None:
        if type(self.decoder_registration) is not RuntimeArtifactDecoderRegistration or self.definition_type not in self.decoder_registration.representation_types or type(self.definition_kind) is not RuntimeModelDefinitionKind or type(self.instance_schema_complete) is not bool:
            raise TypeError('Schema approval names an actual approved decoder/node/kind and explicit completeness decision.')
        if not _frozen_type(type(self.projector)) or not _immutable(self.projector, (type(self.projector),), 1024, 16, 4096) or not callable(getattr(type(self.projector), 'project', None)):
            raise TypeError('Schema projector is an owner-approved immutable configured integration.')


@dataclass(frozen=True, slots=True, eq=False)
class RuntimeInstanceConstraintRequest:
    definition: RuntimeModelDefinition = field(repr=False)
    field_definition: FieldDefinition
    constraint: PatternConstraint | PrecisionConstraint | ScaleConstraint
    primitive_value: RuntimePrimitiveValue = field(repr=False)

    def __post_init__(self) -> None:
        if type(self.definition) is not RuntimeModelDefinition or type(self.field_definition) is not FieldDefinition or type(self.constraint) not in (PatternConstraint, PrecisionConstraint, ScaleConstraint) or not any(c is self.constraint for c in self.field_definition.constraints.value_constraints) or type(self.primitive_value) not in (str, Decimal):
            raise TypeError('Constraint invocation retains actual declared field/constraint and checked primitive.')


class RuntimeInstanceConstraintDecision(Enum):
    SATISFIED = 'satisfied'
    VIOLATED = 'violated'
    UNAVAILABLE = 'unavailable'


@dataclass(frozen=True, slots=True)
class RuntimeInstanceConstraintResult:
    request: RuntimeInstanceConstraintRequest = field(repr=False)
    decision: RuntimeInstanceConstraintDecision

    def __post_init__(self) -> None:
        if type(self.request) is not RuntimeInstanceConstraintRequest or type(self.decision) is not RuntimeInstanceConstraintDecision:
            raise TypeError('Constraint outcome retains the actual invocation and closed decision.')


class RuntimeInstanceConstraintEvaluator(Protocol):
    def evaluate(self, request: RuntimeInstanceConstraintRequest) -> RuntimeInstanceConstraintResult: ...


@dataclass(frozen=True, slots=True)
class RuntimeInstanceConstraintSupport:
    kinds: tuple[ConstraintKind, ...]
    evaluator: RuntimeInstanceConstraintEvaluator = field(repr=False)

    def __post_init__(self) -> None:
        if not _typed_tuple(self.kinds, ConstraintKind) or not self.kinds or len(set(self.kinds)) != len(self.kinds) or any(k not in (ConstraintKinds.PATTERN, ConstraintKinds.PRECISION, ConstraintKinds.SCALE) for k in self.kinds):
            raise TypeError('Only explicitly approved missing pattern/decimal evaluators are supplied here.')
        if not _frozen_type(type(self.evaluator)) or not _immutable(self.evaluator, (type(self.evaluator),), 1024, 16, 4096) or not callable(getattr(type(self.evaluator), 'evaluate', None)):
            raise TypeError('Constraint evaluator requires trusted immutable configuration.')


@dataclass(frozen=True, slots=True)
class RuntimeInstanceOperationResult:
    status: RuntimeArtifactLoadStatus
    state: RuntimeInstanceState | None = field(default=None, repr=False)
    diagnostics: tuple[RuntimeInstanceDiagnostic, ...] = ()
    validation_result: RuntimeValidationResult | None = field(default=None, repr=False)

    def __post_init__(self) -> None:
        if type(self.status) is not RuntimeArtifactLoadStatus or not _typed_tuple(self.diagnostics, RuntimeInstanceDiagnostic):
            raise TypeError('Operation result uses existing runtime status and typed diagnostics.')
        if self.status is RuntimeArtifactLoadStatus.SUCCEEDED:
            if type(self.state) is not RuntimeInstanceState or any(d.severity is RuntimeLoadSeverity.ERROR for d in self.diagnostics):
                raise ValueError('Success requires a complete canonical instance and no errors.')
        elif self.state is not None or not self.diagnostics:
            raise ValueError('Failure/incomplete returns diagnostics without a partial state.')
        if self.validation_result is not None:
            if type(self.validation_result) is not RuntimeValidationResult:
                raise TypeError('Validation evidence uses the actual RUN-04 immutable result.')
            if self.status is RuntimeArtifactLoadStatus.SUCCEEDED and (self.validation_result.status is not RuntimeValidationStatus.VALID or not self.validation_result.complete):
                raise ValueError('Successful instance acceptance cannot carry incomplete/invalid validation.')
            if self.status is RuntimeArtifactLoadStatus.SUCCEEDED:
                bound = self.validation_result.request
                if bound is None or bound.instance != self.state.instance or bound.context.scope != self.state.context.scope or bound.definition_identity != self.state.definition.identity or bound.revision != self.state.revision:
                    raise ValueError('Successful validation evidence must bind the same immutable accepted state/version/revision.')

    @property
    def instance(self) -> SemanticInstance | None:
        return self.state.instance if self.state is not None else None


class RuntimeInstanceInspectionStatus(Enum):
    FOUND = 'found'
    MISSING = 'missing'
    INVALID_FIELD = 'invalid-field'
    INVALID_CONTEXT = 'invalid-context'
    FAILED = 'failed'
    INCOMPLETE = 'incomplete'


@dataclass(frozen=True, slots=True)
class RuntimeInstanceInspectionView:
    instance_identity: RuntimeInstanceIdentityAssociation = field(repr=False)
    definition_identity: ElementVersionRef
    context: RuntimeInstanceContext
    revision: RuntimeInstanceRevision
    values: tuple[RuntimeInstanceFieldAssignment, ...] = field(repr=False)

    def __post_init__(self) -> None:
        if type(self.instance_identity) is not RuntimeInstanceIdentityAssociation or type(self.definition_identity) is not ElementVersionRef or type(self.context) is not RuntimeInstanceContext or type(self.revision) is not RuntimeInstanceRevision or not _typed_tuple(self.values, RuntimeInstanceFieldAssignment):
            raise TypeError('Inspection presents only explicit typed canonical state coordinates.')


@dataclass(frozen=True, slots=True)
class RuntimeInstanceInspectionResult:
    status: RuntimeInstanceInspectionStatus
    view: RuntimeInstanceInspectionView | None = field(default=None, repr=False)
    diagnostics: tuple[RuntimeInstanceDiagnostic, ...] = ()

    def __post_init__(self) -> None:
        if type(self.status) is not RuntimeInstanceInspectionStatus or not _typed_tuple(self.diagnostics, RuntimeInstanceDiagnostic):
            raise TypeError('Inspection result uses explicit read outcomes.')
        if self.status in (RuntimeInstanceInspectionStatus.FOUND, RuntimeInstanceInspectionStatus.MISSING):
            if type(self.view) is not RuntimeInstanceInspectionView or any(d.severity is RuntimeLoadSeverity.ERROR for d in self.diagnostics):
                raise ValueError('Authorized read success requires a complete typed view.')
        elif self.view is not None or not self.diagnostics:
            raise ValueError('Rejected inspection exposes no values.')


class SemanticInstanceRuntime(Protocol):
    def create(self, request: RuntimeInstanceCreateRequest) -> RuntimeInstanceOperationResult: ...
    def update(self, request: RuntimeInstanceUpdateRequest) -> RuntimeInstanceOperationResult: ...
    def inspect(self, request: RuntimeInstanceInspectRequest) -> RuntimeInstanceInspectionResult: ...


def _resolve_instance_schema(definition, supports, capabilities, policy, request, operation, reject, check_capabilities=True):
    """One original-source schema resolver shared by creation and read-only validation."""
    support = next((s for s in supports if s.decoder_registration is definition.loaded_artifact.decoder_registration and s.definition_type is type(definition.representation) and s.definition_kind == definition.definition_kind), None)
    if support is None or not support.instance_schema_complete:
        reject(RuntimeInstanceFailure.VALIDATION_UNAVAILABLE, 'Loaded definition has no explicitly approved complete instance-schema projection.', operation, request, incomplete=True)
    schema = support.projector.project(definition, policy.maximum_fields)
    if type(schema) is not RuntimeInstanceDefinitionSchema or schema.definition is not definition:
        reject(RuntimeInstanceFailure.INTEGRITY_FAILURE, 'Schema projection does not retain the actual selected runtime definition.', operation, request)
    if len(schema.fields) > policy.maximum_fields:
        reject(RuntimeInstanceFailure.RESOURCE_LIMIT_EXCEEDED, 'Declared field inventory exceeds the service budget.', operation, request)
    if len(schema.required_capabilities) > 128:
        reject(RuntimeInstanceFailure.RESOURCE_LIMIT_EXCEEDED, 'Required schema capability inventory exceeds the trusted bound.', operation, request)
    if check_capabilities and any(c not in capabilities for c in schema.required_capabilities):
        reject(RuntimeInstanceFailure.VALIDATION_UNAVAILABLE, 'An explicit required instance-schema capability is unavailable.', operation, request, incomplete=True)
    # Require the actual encoded field tuple, not reconstructed definitions,
    # copied equal fields, omitted fields or alphabetically reordered values.
    stack, seen, found = [definition.representation], set(), False
    while stack:
        node = stack.pop()
        if node is schema.fields:
            found = True
            break
        if id(node) in seen:
            continue
        seen.add(id(node))
        if len(seen) > definition.load_result.loaded_set.effective_policy.maximum_decoded_elements:
            reject(RuntimeInstanceFailure.RESOURCE_LIMIT_EXCEEDED, 'Original schema association traversal exceeds the load budget.', operation, request)
        if type(node) is tuple:
            stack.extend(node)
        elif is_dataclass(node):
            stack.extend(getattr(node, f.name) for f in fields(type(node)))
    if not found:
        reject(RuntimeInstanceFailure.INTEGRITY_FAILURE, 'Projected field order is not the original encoded field tuple.', operation, request)
    ids = tuple(f.id for f in schema.fields)
    if not _typed_tuple(ids, FieldId) or len(set(ids)) != len(ids):
        reject(RuntimeInstanceFailure.INTEGRITY_FAILURE, 'Declared fields have invalid or duplicate stable identities.', operation, request)
    for member in schema.fields:
        if type(member.constraints) is not FieldConstraintSet or type(member.type) not in (PrimitiveTypeRef, SemanticTypeRef) or type(member.constraints.presence) is not FieldPresence or type(member.constraints.nullability) is not FieldNullability:
            reject(RuntimeInstanceFailure.INTEGRITY_FAILURE, 'Declared field representation is not the supported immutable model contract.', operation, request, field_id=member.id)
    return schema



class RuntimeValidationStatus(Enum):
    VALID = 'valid'
    INVALID = 'invalid'
    INCOMPLETE = 'incomplete'


class RuntimeValidationScope(Enum):
    COMPLETE_INSTANCE = 'complete-instance'


class RuntimeValidationRuleCategory(Enum):
    PREREQUISITES = 'prerequisites'
    DEFINITION = 'definition'
    INSTANCE = 'instance'
    MEMBERSHIP = 'membership'
    PRESENCE = 'presence'
    NULLABILITY = 'nullability'
    PRIMITIVE = 'primitive'
    CONSTRAINT = 'constraint'
    REFERENCE = 'reference'
    COMPLETENESS = 'completeness'


class RuntimeValidationOutcome(Enum):
    SATISFIED = 'satisfied'
    VIOLATED = 'violated'
    UNAVAILABLE = 'unavailable'
    NOT_APPLICABLE = 'not-applicable'


class RuntimeValidationFailure(Enum):
    INVALID_REQUEST = 'RUN-301'
    DEFINITION_UNAVAILABLE = 'RUN-302'
    DEFINITION_MISMATCH = 'RUN-303'
    CONTEXT_MISMATCH = 'RUN-304'
    VERSION_REQUIRED = 'RUN-305'
    CANONICAL_UNAVAILABLE = 'RUN-306'
    UNKNOWN_FIELD = 'RUN-307'
    DUPLICATE_FIELD = 'RUN-308'
    REQUIRED_MISSING = 'RUN-309'
    NULL_NOT_ALLOWED = 'RUN-310'
    PRIMITIVE_MISMATCH = 'RUN-311'
    MINIMUM = 'RUN-312'
    MAXIMUM = 'RUN-313'
    MIN_LENGTH = 'RUN-314'
    MAX_LENGTH = 'RUN-315'
    PATTERN = 'RUN-316'
    PRECISION = 'RUN-317'
    SCALE = 'RUN-318'
    RULE_UNAVAILABLE = 'RUN-319'
    RESOURCE_LIMIT = 'RUN-320'
    REPRESENTATION_UNAVAILABLE = 'RUN-321'


@dataclass(frozen=True, slots=True)
class RuntimeValidationContext:
    scope: RuntimeModelRegistryScope
    definition: RuntimeModelDefinition | None = field(default=None, repr=False)
    snapshot: RuntimeModelRegistrySnapshot | None = field(default=None, repr=False)

    def __post_init__(self) -> None:
        if type(self.scope) is not RuntimeModelRegistryScope or self.definition is not None and type(self.definition) is not RuntimeModelDefinition or self.snapshot is not None and type(self.snapshot) is not RuntimeModelRegistrySnapshot:
            raise TypeError('Validation context requires explicit actual scope and coherent immutable definition view.')
        if self.snapshot is not None and self.snapshot.scope != self.scope:
            raise ValueError('Validation snapshot must belong to the explicit requested scope.')


@dataclass(frozen=True, slots=True)
class RuntimeValidationRequest:
    instance: SemanticInstance = field(repr=False)
    context: RuntimeValidationContext
    definition_identity: ElementVersionRef | ElementRef
    revision: RuntimeInstanceRevision | None = None
    validation_scope: RuntimeValidationScope = RuntimeValidationScope.COMPLETE_INSTANCE

    def __post_init__(self) -> None:
        if type(self.context) is not RuntimeValidationContext or type(self.definition_identity) not in (ElementVersionRef, ElementRef) or self.revision is not None and type(self.revision) is not RuntimeInstanceRevision or self.validation_scope is not RuntimeValidationScope.COMPLETE_INSTANCE:
            raise TypeError('Only complete-instance validation with typed exact binding/context/revision is supported.')


@dataclass(frozen=True, slots=True)
class RuntimeValidationLimits:
    maximum_checks: int = 16384
    maximum_diagnostics: int = 1024

    def __post_init__(self) -> None:
        if type(self.maximum_checks) is not int or self.maximum_checks <= 0 or type(self.maximum_diagnostics) is not int or self.maximum_diagnostics <= 0:
            raise ValueError('Validation output/work limits are positive trusted actual integers.')


@dataclass(frozen=True, slots=True)
class RuntimeValidationPatternLimits:
    maximum_pattern_codepoints: int = 1024
    maximum_input_codepoints: int = 32768
    maximum_work_units: int = 100000

    def __post_init__(self) -> None:
        if any(type(getattr(self, f.name)) is not int or getattr(self, f.name) <= 0 for f in fields(self)):
            raise ValueError('Safe pattern limits require positive actual integers.')


@dataclass(frozen=True, slots=True)
class RuntimeValidationPatternResult:
    evaluation: RuntimeInstanceConstraintResult = field(repr=False)
    work_units: int
    exhausted: bool = False

    def __post_init__(self) -> None:
        if type(self.evaluation) is not RuntimeInstanceConstraintResult or type(self.work_units) is not int or self.work_units < 0 or type(self.exhausted) is not bool or self.exhausted and self.evaluation.decision is not RuntimeInstanceConstraintDecision.UNAVAILABLE:
            raise TypeError('Bounded pattern evidence cannot promote exhausted work to a decision.')


class RuntimeValidationPatternEvaluator(Protocol):
    def evaluate_bounded(self, request: RuntimeInstanceConstraintRequest, limits: RuntimeValidationPatternLimits) -> RuntimeValidationPatternResult:
        """Owner must implement approved dialect and genuinely bounded work; no engine exists here."""
        ...


@dataclass(frozen=True, slots=True)
class RuntimeValidationPatternSupport:
    evaluator: RuntimeValidationPatternEvaluator = field(repr=False)
    limits: RuntimeValidationPatternLimits = field(default_factory=RuntimeValidationPatternLimits)

    def __post_init__(self) -> None:
        if type(self.limits) is not RuntimeValidationPatternLimits or not _frozen_type(type(self.evaluator)) or not _immutable(self.evaluator, (type(self.evaluator),), 1024, 16, 4096) or not callable(getattr(type(self.evaluator), 'evaluate_bounded', None)):
            raise TypeError('Only an owner-approved immutable genuinely bounded pattern integration qualifies.')


@dataclass(frozen=True, slots=True)
class RuntimeValidationRuleEvidence:
    category: RuntimeValidationRuleCategory
    outcome: RuntimeValidationOutcome
    field_id: FieldId | None = None
    constraint_kind: ConstraintKind | None = None

    def __post_init__(self) -> None:
        if type(self.category) is not RuntimeValidationRuleCategory or type(self.outcome) is not RuntimeValidationOutcome or self.field_id is not None and type(self.field_id) is not FieldId or self.constraint_kind is not None and type(self.constraint_kind) is not ConstraintKind:
            raise TypeError('Evidence tracks actual typed rule outcomes, not inferred passes.')


@dataclass(frozen=True, slots=True)
class RuntimeValidationDiagnostic:
    code: RuntimeValidationFailure
    message: str
    severity: RuntimeLoadSeverity
    category: RuntimeValidationRuleCategory
    scope: RuntimeModelRegistryScope | None = None
    definition_identity: ElementVersionRef | None = None
    instance_identity: RuntimeInstanceIdentityAssociation | None = field(default=None, repr=False)
    revision: RuntimeInstanceRevision | None = None
    field_id: FieldId | None = None
    constraint_kind: ConstraintKind | None = None
    validation_scope: RuntimeValidationScope = RuntimeValidationScope.COMPLETE_INSTANCE

    def __post_init__(self) -> None:
        if type(self.code) is not RuntimeValidationFailure or type(self.message) is not str or not self.message or type(self.severity) is not RuntimeLoadSeverity or type(self.category) is not RuntimeValidationRuleCategory or self.validation_scope is not RuntimeValidationScope.COMPLETE_INSTANCE:
            raise TypeError('Validation diagnostics use runtime conventions, not compiler phase outcomes.')
        for value, expected in ((self.scope, RuntimeModelRegistryScope), (self.definition_identity, ElementVersionRef), (self.instance_identity, RuntimeInstanceIdentityAssociation), (self.revision, RuntimeInstanceRevision), (self.field_id, FieldId), (self.constraint_kind, ConstraintKind)):
            if value is not None and type(value) is not expected:
                raise TypeError('Validation associations are immutable actual semantic coordinates.')


@dataclass(frozen=True, slots=True)
class RuntimeValidationResult:
    status: RuntimeValidationStatus
    request: RuntimeValidationRequest | None = field(default=None, repr=False)
    instance_identity: RuntimeInstanceIdentityAssociation | None = field(default=None, repr=False)
    diagnostics: tuple[RuntimeValidationDiagnostic, ...] = ()
    evidence: tuple[RuntimeValidationRuleEvidence, ...] = ()
    complete: bool = False

    def __post_init__(self) -> None:
        if type(self.status) is not RuntimeValidationStatus or self.request is not None and type(self.request) is not RuntimeValidationRequest or self.instance_identity is not None and type(self.instance_identity) is not RuntimeInstanceIdentityAssociation or not _typed_tuple(self.diagnostics, RuntimeValidationDiagnostic) or not _typed_tuple(self.evidence, RuntimeValidationRuleEvidence) or type(self.complete) is not bool:
            raise TypeError('Validation results preserve explicit immutable scope, identity and completeness evidence.')
        violated = any(e.outcome is RuntimeValidationOutcome.VIOLATED for e in self.evidence)
        unavailable = any(e.outcome is RuntimeValidationOutcome.UNAVAILABLE for e in self.evidence)
        if self.request is not None and (self.instance_identity is None or type(self.request.instance) is not self.instance_identity.support.instance_type):
            raise TypeError('Results never retain an untyped/mutable rejected input as immutable instance evidence.')
        if self.status is RuntimeValidationStatus.VALID:
            categories = {e.category for e in self.evidence if e.outcome is RuntimeValidationOutcome.SATISFIED}
            mandatory = {RuntimeValidationRuleCategory.PREREQUISITES, RuntimeValidationRuleCategory.DEFINITION, RuntimeValidationRuleCategory.INSTANCE, RuntimeValidationRuleCategory.MEMBERSHIP, RuntimeValidationRuleCategory.COMPLETENESS}
            if not self.complete or violated or unavailable or self.request is None or self.instance_identity is None or not mandatory <= categories or any(d.severity is RuntimeLoadSeverity.ERROR for d in self.diagnostics):
                raise ValueError('VALID requires completed mandatory checks and actual exact-instance associations.')
        elif self.status is RuntimeValidationStatus.INVALID:
            if not violated or not self.diagnostics:
                raise ValueError('INVALID requires actual definite violation evidence.')
        elif violated or not unavailable:
            raise ValueError('INCOMPLETE needs unavailable evidence and no hidden definite violation.')
        if self.complete and unavailable:
            raise ValueError('Unavailable mandatory checks cannot be complete.')


class RuntimeValidator(Protocol):
    def validate(self, request: RuntimeValidationRequest) -> RuntimeValidationResult: ...


class _ValidationBudgetReached(Exception):
    """Private bounded-collection termination, never a successful skipped rule."""


class DefaultRuntimeValidator:
    """One read-only engine, with coherent explicit views and no registry/HTTP calls."""
    __slots__ = ('_contract', '_schemas', '_constraints', '_capabilities', '_policy', '_limits', '_patterns')

    def __init__(self, *, contract_support: RuntimeSemanticInstanceContractSupport | None = None,
                 definition_support: tuple[RuntimeInstanceDefinitionSupport, ...] = (),
                 constraint_support: RuntimeInstanceConstraintSupport | None = None,
                 supported_capabilities: tuple[RuntimeCapabilityId, ...] = (),
                 policy: RuntimeInstancePolicy | None = None, limits: RuntimeValidationLimits | None = None,
                 pattern_support: RuntimeValidationPatternSupport | None = None):
        if contract_support is not None and type(contract_support) is not RuntimeSemanticInstanceContractSupport or not _typed_tuple(definition_support, RuntimeInstanceDefinitionSupport) or len(definition_support) > 128 or constraint_support is not None and type(constraint_support) is not RuntimeInstanceConstraintSupport or not _typed_tuple(supported_capabilities, RuntimeCapabilityId) or len(supported_capabilities) > 128 or len(set(supported_capabilities)) != len(supported_capabilities):
            raise TypeError('Validator owner explicitly supplies existing immutable integration approvals.')
        keys = tuple((id(s.decoder_registration), s.definition_type, s.definition_kind) for s in definition_support)
        if len(set(keys)) != len(keys):
            raise ValueError('Schema dispatch approvals must be unambiguous.')
        self._contract, self._schemas, self._constraints = contract_support, definition_support, constraint_support
        self._capabilities = supported_capabilities
        self._policy = RuntimeInstancePolicy() if policy is None else policy
        self._limits = RuntimeValidationLimits() if limits is None else limits
        if type(self._policy) is not RuntimeInstancePolicy or type(self._limits) is not RuntimeValidationLimits:
            raise TypeError('Resource ceilings belong to the trusted validator owner, never client overrides.')
        if pattern_support is not None and type(pattern_support) is not RuntimeValidationPatternSupport:
            raise TypeError('Bounded pattern support is an explicit trusted owner approval.')
        self._patterns = pattern_support

    def validate(self, request: RuntimeValidationRequest) -> RuntimeValidationResult:
        evidence, diagnostics = [], []
        identity = None
        actual = request if type(request) is RuntimeValidationRequest else None
        scope = actual.context.scope if actual is not None else None
        exact = actual.definition_identity if actual is not None and type(actual.definition_identity) is ElementVersionRef else None
        revision = actual.revision if actual is not None else None
        completed = False
        bound_request = None

        def add(category, outcome, code=None, message=None, fid=None, kind=None):
            if len(evidence) >= self._limits.maximum_checks or code is not None and len(diagnostics) >= self._limits.maximum_diagnostics:
                raise _ValidationBudgetReached()
            evidence.append(RuntimeValidationRuleEvidence(category, outcome, fid, kind))
            if code is not None:
                diagnostics.append(RuntimeValidationDiagnostic(code, message, RuntimeLoadSeverity.ERROR,
                    category, scope, exact, identity, revision, fid, kind))

        def gap(code, message, category=RuntimeValidationRuleCategory.PREREQUISITES, fid=None, kind=None):
            add(category, RuntimeValidationOutcome.UNAVAILABLE, code, message, fid, kind)

        def reject_schema(code, message, operation, ignored, *, field_id=None, constraint=None, incomplete=False):
            # Shared resolver uses the existing narrow runtime rejection convention.
            raise RuntimeInstanceError((RuntimeInstanceDiagnostic(code, message, RuntimeLoadSeverity.ERROR,
                RuntimeInstanceOperation.INSPECT, scope, exact, field_id=field_id, constraint_kind=constraint),),
                RuntimeArtifactLoadStatus.INCOMPLETE if incomplete else RuntimeArtifactLoadStatus.FAILED)

        def run():
            nonlocal identity, completed, bound_request
            if actual is None:
                gap(RuntimeValidationFailure.INVALID_REQUEST, 'An actual typed immutable validation request is required.')
                return
            if exact is None or type(exact.element_id) is not SemanticElementId or type(exact.version) is not SemanticVersion:
                gap(RuntimeValidationFailure.VERSION_REQUIRED, 'Validation requires an exact definition version; no latest selection.')
                return
            if revision is not None and revision.value > self._policy.maximum_revision:
                gap(RuntimeValidationFailure.RESOURCE_LIMIT, 'Supplied local revision exceeds the trusted evidence budget.')
                return
            if self._contract is None:
                gap(RuntimeValidationFailure.CANONICAL_UNAVAILABLE, 'Authoritative TYPE-08 identity/instance/value contracts are unavailable.')
                return
            if type(actual.instance) is not self._contract.instance_type or not _immutable(actual.instance, self._contract.approved_types, self._policy.maximum_value_nodes, self._policy.maximum_value_depth, self._policy.maximum_scalar_units):
                gap(RuntimeValidationFailure.REPRESENTATION_UNAVAILABLE, 'Canonical instance representation is unsupported, mutable or outside trusted graph budgets.')
                return
            add(RuntimeValidationRuleCategory.PREREQUISITES, RuntimeValidationOutcome.SATISFIED)
            view = self._contract.adapter.inspect_instance(actual.instance)
            if type(view) is not RuntimeInstanceStateView or len(view.values) > self._policy.maximum_fields:
                gap(RuntimeValidationFailure.RESOURCE_LIMIT, 'Canonical projection is unavailable or exceeds the field budget.', RuntimeValidationRuleCategory.INSTANCE)
                return
            if type(view.instance_identity) is not self._contract.identity_type or not _immutable(view.instance_identity, self._contract.approved_types, min(1024, self._policy.maximum_value_nodes), min(16, self._policy.maximum_value_depth), min(4096, self._policy.maximum_scalar_units)) or self._contract.adapter.valid_identity(view.instance_identity) is not True:
                gap(RuntimeValidationFailure.REPRESENTATION_UNAVAILABLE, 'A trustworthy independent canonical instance identity is unavailable.', RuntimeValidationRuleCategory.INSTANCE)
                return
            identity = RuntimeInstanceIdentityAssociation(self._contract, view.instance_identity)
            bound_request = actual
            binding_invalid = view.definition_identity != exact or view.semantic_context != scope.semantic_context
            if view.definition_identity != exact:
                add(RuntimeValidationRuleCategory.INSTANCE, RuntimeValidationOutcome.VIOLATED, RuntimeValidationFailure.DEFINITION_MISMATCH, 'Instance exact definition binding differs from the validation request.')
            if view.semantic_context != scope.semantic_context:
                add(RuntimeValidationRuleCategory.INSTANCE, RuntimeValidationOutcome.VIOLATED, RuntimeValidationFailure.CONTEXT_MISMATCH, 'Instance semantic context differs from the explicit validation scope.')
            add(RuntimeValidationRuleCategory.INSTANCE, RuntimeValidationOutcome.SATISFIED)
            definition = actual.context.definition
            snapshot = actual.context.snapshot
            if snapshot is not None:
                if len(snapshot.definitions) > self._policy.maximum_value_nodes:
                    gap(RuntimeValidationFailure.RESOURCE_LIMIT, 'Snapshot inspection exceeds trusted bounded work.', RuntimeValidationRuleCategory.DEFINITION)
                    return
                candidates = tuple(d for d in snapshot.definitions if d.key.scope == scope and d.identity == exact)
                if len(candidates) != 1 or definition is not None and candidates[0] is not definition:
                    gap(RuntimeValidationFailure.DEFINITION_UNAVAILABLE, 'Snapshot lacks the original requested exact definition view.', RuntimeValidationRuleCategory.DEFINITION)
                    return
                definition = candidates[0]
            if definition is None:
                gap(RuntimeValidationFailure.DEFINITION_UNAVAILABLE, 'No coherent exact registered definition view is supplied.', RuntimeValidationRuleCategory.DEFINITION)
                return
            if definition.key.scope != scope or definition.identity != exact:
                gap(RuntimeValidationFailure.DEFINITION_UNAVAILABLE, 'Selected definition has a different scope/target/exact version.', RuntimeValidationRuleCategory.DEFINITION)
                return
            try:
                definition.__post_init__()
            except RuntimeArtifactLoadError:
                gap(RuntimeValidationFailure.DEFINITION_UNAVAILABLE, 'Original runtime definition/evidence integrity is unavailable.', RuntimeValidationRuleCategory.DEFINITION)
                return
            if binding_invalid:
                gap(RuntimeValidationFailure.RULE_UNAVAILABLE, 'Remaining value checks cannot judge an instance against conflicting exact binding/context.', RuntimeValidationRuleCategory.COMPLETENESS)
                return
            try:
                schema = _resolve_instance_schema(definition, self._schemas, self._capabilities,
                    self._policy, actual, RuntimeInstanceOperation.INSPECT, reject_schema, check_capabilities=False)
            except RuntimeInstanceError as error:
                for d in error.diagnostics:
                    gap(RuntimeValidationFailure.RESOURCE_LIMIT if d.code is RuntimeInstanceFailure.RESOURCE_LIMIT_EXCEEDED else RuntimeValidationFailure.RULE_UNAVAILABLE,
                        'Approved complete original runtime schema/capability is unavailable.', RuntimeValidationRuleCategory.DEFINITION, d.field_id, d.constraint_kind)
                return
            add(RuntimeValidationRuleCategory.DEFINITION, RuntimeValidationOutcome.SATISFIED)
            groups = {}
            for assignment in view.values:
                groups.setdefault(assignment.field_id, []).append(assignment.value)
            declared = {f.id for f in schema.fields}
            for fid in sorted(groups, key=lambda f: f.value):
                if fid not in declared:
                    add(RuntimeValidationRuleCategory.MEMBERSHIP, RuntimeValidationOutcome.VIOLATED, RuntimeValidationFailure.UNKNOWN_FIELD, 'FieldId is not declared by the selected exact definition.', fid)
                if len(groups[fid]) != 1:
                    add(RuntimeValidationRuleCategory.MEMBERSHIP, RuntimeValidationOutcome.VIOLATED, RuntimeValidationFailure.DUPLICATE_FIELD, 'Duplicate FieldId representations are forbidden, including equal values.', fid)
            add(RuntimeValidationRuleCategory.MEMBERSHIP, RuntimeValidationOutcome.SATISFIED)
            if not _immutable(tuple(a.value for a in view.values), self._contract.approved_types,
                    self._policy.maximum_value_nodes, self._policy.maximum_value_depth, self._policy.maximum_scalar_units):
                gap(RuntimeValidationFailure.RESOURCE_LIMIT, 'Aggregate projected values cannot be evaluated within trusted immutable representation budgets.', RuntimeValidationRuleCategory.PRIMITIVE)
                return
            primitive_types = ((PrimitiveTypes.STRING, str), (PrimitiveTypes.BOOLEAN, bool), (PrimitiveTypes.INTEGER, int), (PrimitiveTypes.DECIMAL, Decimal), (PrimitiveTypes.DATE, date), (PrimitiveTypes.DATETIME, datetime), (PrimitiveTypes.UUID, UUID))
            constraint_types = (MinimumConstraint, MaximumConstraint, MinLengthConstraint, MaxLengthConstraint, PatternConstraint, PrecisionConstraint, ScaleConstraint)
            constraint_codes = (RuntimeValidationFailure.MINIMUM, RuntimeValidationFailure.MAXIMUM, RuntimeValidationFailure.MIN_LENGTH, RuntimeValidationFailure.MAX_LENGTH, RuntimeValidationFailure.PATTERN, RuntimeValidationFailure.PRECISION, RuntimeValidationFailure.SCALE)
            for member in schema.fields:
                fid = member.id
                values = groups.get(fid, ())
                kind, primitive, usable = RuntimeInstanceValueKind.MISSING, None, True
                if len(values) > 1:
                    gap(RuntimeValidationFailure.REPRESENTATION_UNAVAILABLE, 'Duplicate representations cannot select one trustworthy field value.', RuntimeValidationRuleCategory.PRIMITIVE, fid)
                    usable = False
                elif values:
                    value = values[0]
                    if type(value) not in self._contract.value_types or not _immutable(value, self._contract.approved_types, self._policy.maximum_value_nodes, self._policy.maximum_value_depth, self._policy.maximum_scalar_units):
                        gap(RuntimeValidationFailure.REPRESENTATION_UNAVAILABLE, 'Canonical field representation is unsupported or outside resource limits.', RuntimeValidationRuleCategory.PRIMITIVE, fid)
                        usable = False
                    else:
                        projection = self._contract.adapter.inspect_value(value)
                        expected = {self._contract.missing_type: RuntimeInstanceValueKind.MISSING, self._contract.null_type: RuntimeInstanceValueKind.NULL, self._contract.value_type: RuntimeInstanceValueKind.VALUE}[type(value)]
                        if projection is None and expected is RuntimeInstanceValueKind.VALUE and type(member.type) is SemanticTypeRef:
                            gap(RuntimeValidationFailure.RULE_UNAVAILABLE, 'Canonical semantic instance-reference validation capability is unavailable.', RuntimeValidationRuleCategory.REFERENCE, fid)
                            usable = False
                            projection = None
                        if type(projection) is not RuntimeInstanceValueView or projection.kind is not expected or not _immutable(projection.primitive, (), self._policy.maximum_value_nodes, self._policy.maximum_value_depth, self._policy.maximum_scalar_units):
                            if usable:
                                gap(RuntimeValidationFailure.REPRESENTATION_UNAVAILABLE, 'Canonical field projection/variant is unavailable; no conversion or guessed reference.', RuntimeValidationRuleCategory.PRIMITIVE, fid)
                            usable = False
                        else:
                            kind, primitive = projection.kind, projection.primitive
                if usable:
                    missing = kind is RuntimeInstanceValueKind.MISSING
                    null = kind is RuntimeInstanceValueKind.NULL
                    invalid_presence = missing and member.constraints.presence is FieldPresence.REQUIRED
                    invalid_null = null and member.constraints.nullability is FieldNullability.NON_NULL
                    add(RuntimeValidationRuleCategory.PRESENCE, RuntimeValidationOutcome.VIOLATED if invalid_presence else RuntimeValidationOutcome.SATISFIED,
                        RuntimeValidationFailure.REQUIRED_MISSING if invalid_presence else None, 'Required field is Missing; validation applies no defaults.', fid)
                    add(RuntimeValidationRuleCategory.NULLABILITY, RuntimeValidationOutcome.VIOLATED if invalid_null else RuntimeValidationOutcome.SATISFIED,
                        RuntimeValidationFailure.NULL_NOT_ALLOWED if invalid_null else None, 'Explicit Null is forbidden independently of field presence.', fid)
                    if kind is RuntimeInstanceValueKind.VALUE:
                        if type(member.type) is SemanticTypeRef:
                            gap(RuntimeValidationFailure.RULE_UNAVAILABLE, 'Instance-reference representation/compatibility is not established; no recursive lookup.', RuntimeValidationRuleCategory.REFERENCE, fid)
                            usable = False
                        else:
                            expected_type = next((t for p, t in primitive_types if p == member.type.primitive), None)
                            if expected_type is None:
                                gap(RuntimeValidationFailure.RULE_UNAVAILABLE, 'Declared primitive representation is unsupported.', RuntimeValidationRuleCategory.PRIMITIVE, fid)
                                usable = False
                            elif type(primitive) is not expected_type:
                                add(RuntimeValidationRuleCategory.PRIMITIVE, RuntimeValidationOutcome.VIOLATED, RuntimeValidationFailure.PRIMITIVE_MISMATCH, 'Value has a different exact primitive type; validation performs no coercion.', fid)
                                usable = False
                            else:
                                add(RuntimeValidationRuleCategory.PRIMITIVE, RuntimeValidationOutcome.SATISFIED, fid=fid)
                    else:
                        add(RuntimeValidationRuleCategory.PRIMITIVE, RuntimeValidationOutcome.NOT_APPLICABLE, fid=fid)
                constraints = member.constraints.value_constraints
                if type(constraints) is not tuple or len(constraints) > 7:
                    gap(RuntimeValidationFailure.RULE_UNAVAILABLE, 'Mandatory constraint inventory is unsupported or unbounded.', RuntimeValidationRuleCategory.CONSTRAINT, fid)
                    continue
                # Stable TYPE-04 kind order, not display text or input insertion.
                for constraint in sorted(constraints, key=lambda c: c.kind.value if type(c) in constraint_types else ''):
                    t = type(constraint)
                    ck = constraint.kind if t in constraint_types else None
                    if t not in constraint_types or type(member.type) is SemanticTypeRef or ck not in primitive_constraint_kinds(member.type.primitive):
                        gap(RuntimeValidationFailure.RULE_UNAVAILABLE, 'Mandatory constraint has no compatible TYPE-06 runtime semantics.', RuntimeValidationRuleCategory.CONSTRAINT, fid, ck)
                        continue
                    if t in (MinimumConstraint, MaximumConstraint) and (type(constraint.value) is not NumericConstraintValue or member.type.primitive == PrimitiveTypes.INTEGER and '.' in constraint.value.value):
                        gap(RuntimeValidationFailure.RULE_UNAVAILABLE, 'Declared numeric boundary cannot be evaluated under exact TYPE-04/06 applicability.', RuntimeValidationRuleCategory.CONSTRAINT, fid, ck)
                        continue
                    external = t in (PatternConstraint, PrecisionConstraint, ScaleConstraint)
                    if t is PatternConstraint and (self._patterns is None or len(constraint.value) > self._patterns.limits.maximum_pattern_codepoints):
                        gap(RuntimeValidationFailure.RULE_UNAVAILABLE, 'Approved regex dialect/bounded work is unavailable; ordinary unrestricted regex is never executed.', RuntimeValidationRuleCategory.CONSTRAINT, fid, ck)
                        continue
                    if external and t is not PatternConstraint and (self._constraints is None or ck not in self._constraints.kinds):
                        gap(RuntimeValidationFailure.RULE_UNAVAILABLE, 'Required safe pattern/decimal evaluator is unavailable, including for absent optional values.', RuntimeValidationRuleCategory.CONSTRAINT, fid, ck)
                        continue
                    if not usable or kind is not RuntimeInstanceValueKind.VALUE:
                        add(RuntimeValidationRuleCategory.CONSTRAINT, RuntimeValidationOutcome.NOT_APPLICABLE if usable else RuntimeValidationOutcome.UNAVAILABLE, fid=fid, kind=ck)
                        continue
                    if t is MinimumConstraint:
                        violated = primitive < Decimal(constraint.value.value)
                    elif t is MaximumConstraint:
                        violated = primitive > Decimal(constraint.value.value)
                    elif t is MinLengthConstraint:
                        violated = len(primitive) < constraint.value
                    elif t is MaxLengthConstraint:
                        violated = len(primitive) > constraint.value
                    else:
                        invocation = RuntimeInstanceConstraintRequest(definition, member, constraint, primitive)
                        if t is PatternConstraint:
                            if len(primitive) > self._patterns.limits.maximum_input_codepoints:
                                gap(RuntimeValidationFailure.RESOURCE_LIMIT, 'Pattern input exceeds the approved bounded evaluator capacity.', RuntimeValidationRuleCategory.CONSTRAINT, fid, ck)
                                continue
                            bounded = self._patterns.evaluator.evaluate_bounded(invocation, self._patterns.limits)
                            if type(bounded) is not RuntimeValidationPatternResult or bounded.exhausted or bounded.work_units > self._patterns.limits.maximum_work_units:
                                gap(RuntimeValidationFailure.RULE_UNAVAILABLE, 'Safe pattern evaluation could not complete within its approved work budget.', RuntimeValidationRuleCategory.CONSTRAINT, fid, ck)
                                continue
                            result = bounded.evaluation
                        else:
                            result = self._constraints.evaluator.evaluate(invocation)
                        if type(result) is not RuntimeInstanceConstraintResult or result.request is not invocation or result.decision is RuntimeInstanceConstraintDecision.UNAVAILABLE:
                            gap(RuntimeValidationFailure.RULE_UNAVAILABLE, 'Required evaluator result/association/resource guarantees are unavailable.', RuntimeValidationRuleCategory.CONSTRAINT, fid, ck)
                            continue
                        violated = result.decision is RuntimeInstanceConstraintDecision.VIOLATED
                    add(RuntimeValidationRuleCategory.CONSTRAINT, RuntimeValidationOutcome.VIOLATED if violated else RuntimeValidationOutcome.SATISFIED,
                        constraint_codes[constraint_types.index(t)] if violated else None, 'Value violates the declared supported constraint without normalization.', fid, ck)
            # No named model-level/cross-field/external-data rule contract exists
            # in this revision. A server capability token alone is not execution.
            for capability in schema.required_capabilities:
                gap(RuntimeValidationFailure.RULE_UNAVAILABLE, 'Required named model-level capability has no approved runtime rule contract/evaluator.', RuntimeValidationRuleCategory.COMPLETENESS)
            completed = True
            if not any(e.outcome is RuntimeValidationOutcome.UNAVAILABLE for e in evidence):
                add(RuntimeValidationRuleCategory.COMPLETENESS, RuntimeValidationOutcome.SATISFIED)
            else:
                add(RuntimeValidationRuleCategory.COMPLETENESS, RuntimeValidationOutcome.UNAVAILABLE)

        try:
            run()
        except _ValidationBudgetReached:
            # One reserved terminal record beyond configured normal-output caps;
            # keep definite violations already found, never silently truncate VALID.
            evidence.append(RuntimeValidationRuleEvidence(RuntimeValidationRuleCategory.COMPLETENESS, RuntimeValidationOutcome.UNAVAILABLE))
            diagnostics.append(RuntimeValidationDiagnostic(RuntimeValidationFailure.RESOURCE_LIMIT,
                'Mandatory evaluation stopped at trusted check/diagnostic capacity.', RuntimeLoadSeverity.ERROR,
                RuntimeValidationRuleCategory.COMPLETENESS, scope, exact, identity, revision))
            completed = False
        violated = any(e.outcome is RuntimeValidationOutcome.VIOLATED for e in evidence)
        unavailable = any(e.outcome is RuntimeValidationOutcome.UNAVAILABLE for e in evidence)
        status = RuntimeValidationStatus.INVALID if violated else RuntimeValidationStatus.INCOMPLETE if unavailable or not completed else RuntimeValidationStatus.VALID
        return RuntimeValidationResult(status, bound_request, identity, tuple(diagnostics), tuple(evidence), completed and not unavailable)


class DefaultSemanticInstanceRuntime:
    """Pure immutable transformation service with no stored instance membership.

    Composition belongs to the application zone: it may reuse model FieldId and
    constraint contracts without adding a forbidden model edge to runtime-core.
    """
    __slots__ = ('_binding', '_registry', '_authorizer', '_contract', '_schemas',
                 '_constraints', '_capabilities', '_policy', '_validator')

    def __init__(self, scopes: tuple[RuntimeModelRegistryScope, ...], registry: RuntimeModelRegistry,
                 *, authorizer: RuntimeInstanceAuthorizer | None = None,
                 contract_support: RuntimeSemanticInstanceContractSupport | None = None,
                 definition_support: tuple[RuntimeInstanceDefinitionSupport, ...] = (),
                 constraint_support: RuntimeInstanceConstraintSupport | None = None,
                 supported_capabilities: tuple[RuntimeCapabilityId, ...] = (),
                 policy: RuntimeInstancePolicy | None = None, validator: RuntimeValidator | None = None):
        self._binding = RuntimeInstanceServiceBinding(scopes)
        if not callable(getattr(type(registry), 'lookup', None)) or authorizer is not None and not callable(getattr(type(authorizer), 'authorize', None)):
            raise TypeError('Owner supplies actual registry and independent instance authorization ports.')
        if contract_support is not None and type(contract_support) is not RuntimeSemanticInstanceContractSupport or not _typed_tuple(definition_support, RuntimeInstanceDefinitionSupport) or len(definition_support) > 128 or constraint_support is not None and type(constraint_support) is not RuntimeInstanceConstraintSupport:
            raise TypeError('Only explicit typed canonical/schema/constraint approvals are accepted.')
        if not _typed_tuple(supported_capabilities, RuntimeCapabilityId) or len(supported_capabilities) > 128 or len(set(supported_capabilities)) != len(supported_capabilities):
            raise TypeError('Runtime capabilities require bounded explicit distinct approval.')
        keys = tuple((id(s.decoder_registration), s.definition_type, s.definition_kind) for s in definition_support)
        if len(set(keys)) != len(keys):
            raise ValueError('Duplicate schema dispatch approvals are ambiguous.')
        self._registry, self._authorizer, self._contract = registry, authorizer, contract_support
        self._schemas, self._constraints, self._capabilities = definition_support, constraint_support, supported_capabilities
        self._policy = RuntimeInstancePolicy() if policy is None else policy
        if type(self._policy) is not RuntimeInstancePolicy:
            raise TypeError('Resource/revision limits belong to the trusted service owner.')
        self._validator = DefaultRuntimeValidator(contract_support=contract_support,
            definition_support=definition_support, constraint_support=constraint_support,
            supported_capabilities=supported_capabilities, policy=self._policy) if validator is None else validator
        if not callable(getattr(type(self._validator), 'validate', None)):
            raise TypeError('Owner supplies one authoritative runtime validator, never a request callback.')

    def _validate_instance(self, instance, definition, context, revision, request, operation, identity):
        validation_request = RuntimeValidationRequest(instance,
            RuntimeValidationContext(context.scope, definition, context.snapshot), definition.identity, revision)
        result = self._validator.validate(validation_request)
        if type(result) is not RuntimeValidationResult or result.request is not None and result.request != validation_request or result.instance_identity is not None and (result.instance_identity.support is not self._contract or result.instance_identity.identity != identity.identity):
            self._reject(RuntimeInstanceFailure.INTEGRITY_FAILURE, 'Validator result is not bound to this exact immutable candidate/context/revision.', operation, request, identity=identity)
        if result.status is not RuntimeValidationStatus.VALID or not result.complete:
            codes = {RuntimeValidationFailure.UNKNOWN_FIELD: RuntimeInstanceFailure.UNKNOWN_FIELD,
                RuntimeValidationFailure.DUPLICATE_FIELD: RuntimeInstanceFailure.DUPLICATE_FIELD,
                RuntimeValidationFailure.REQUIRED_MISSING: RuntimeInstanceFailure.REQUIRED_FIELD_MISSING,
                RuntimeValidationFailure.NULL_NOT_ALLOWED: RuntimeInstanceFailure.NULL_NOT_ALLOWED,
                RuntimeValidationFailure.PRIMITIVE_MISMATCH: RuntimeInstanceFailure.PRIMITIVE_TYPE_MISMATCH,
                RuntimeValidationFailure.DEFINITION_MISMATCH: RuntimeInstanceFailure.DEFINITION_MISMATCH,
                RuntimeValidationFailure.CONTEXT_MISMATCH: RuntimeInstanceFailure.CONTEXT_MISMATCH,
                RuntimeValidationFailure.RESOURCE_LIMIT: RuntimeInstanceFailure.RESOURCE_LIMIT_EXCEEDED}
            first = next((d for d in result.diagnostics if d.code in codes), result.diagnostics[0] if result.diagnostics else None)
            code = codes.get(first.code, RuntimeInstanceFailure.CONSTRAINT_VIOLATION if result.status is RuntimeValidationStatus.INVALID else RuntimeInstanceFailure.VALIDATION_UNAVAILABLE) if first is not None else RuntimeInstanceFailure.VALIDATION_UNAVAILABLE
            diagnostic = RuntimeInstanceDiagnostic(code, 'Authoritative complete runtime validation rejected the immutable state.', RuntimeLoadSeverity.ERROR, operation,
                context.scope, definition.identity, identity, first.field_id if first is not None else None,
                first.constraint_kind if first is not None else None,
                request.expected_revision if type(request) is RuntimeInstanceUpdateRequest else None)
            raise RuntimeInstanceError((diagnostic,), RuntimeArtifactLoadStatus.FAILED if result.status is RuntimeValidationStatus.INVALID else RuntimeArtifactLoadStatus.INCOMPLETE, result)
        return result

    def _reject(self, code: RuntimeInstanceFailure, message: str, operation: RuntimeInstanceOperation,
                request: object, *, identity: RuntimeInstanceIdentityAssociation | None = None,
                field_id: FieldId | None = None, constraint: ConstraintKind | None = None,
                causes: tuple[RuntimeArtifactLoadDiagnostic, ...] = (), incomplete: bool = False) -> None:
        context = request.context if type(request) in (RuntimeInstanceCreateRequest, RuntimeInstanceUpdateRequest, RuntimeInstanceInspectRequest) else None
        definition = request.state.definition.identity if type(request) is RuntimeInstanceInspectRequest else request.definition_identity if type(request) in (RuntimeInstanceCreateRequest, RuntimeInstanceUpdateRequest) else None
        revision = request.expected_revision if type(request) is RuntimeInstanceUpdateRequest else None
        diagnostic = RuntimeInstanceDiagnostic(code, message, RuntimeLoadSeverity.ERROR, operation,
            context.scope if context is not None else None, definition if type(definition) is ElementVersionRef else None,
            identity, field_id, constraint, revision, causes)
        raise RuntimeInstanceError((diagnostic,), RuntimeArtifactLoadStatus.INCOMPLETE if incomplete else RuntimeArtifactLoadStatus.FAILED)

    def _preflight(self, request: object, operation: RuntimeInstanceOperation) -> None:
        expected = {RuntimeInstanceOperation.CREATE: RuntimeInstanceCreateRequest, RuntimeInstanceOperation.UPDATE: RuntimeInstanceUpdateRequest, RuntimeInstanceOperation.INSPECT: RuntimeInstanceInspectRequest}[operation]
        if type(request) is not expected:
            self._reject(RuntimeInstanceFailure.INVALID_REQUEST, 'Actual typed instance request is required.', operation, request)
        if request.context.scope not in self._binding.scopes:
            self._reject(RuntimeInstanceFailure.INVALID_SCOPE, 'Scope is not declared by this runtime instance service.', operation, request)
        if self._authorizer is None:
            self._reject(RuntimeInstanceFailure.AUTHORIZATION_UNAVAILABLE, 'No trusted instance operation-authority integration is configured.', operation, request, incomplete=True)
        if self._contract is None:
            self._reject(RuntimeInstanceFailure.TYPE08_UNAVAILABLE, 'Canonical TYPE-08 identity, instance and Missing/Null/Value contracts are unavailable.', operation, request, incomplete=True)
        assignments = request.values if operation is RuntimeInstanceOperation.CREATE else request.changes if operation is RuntimeInstanceOperation.UPDATE else ()
        if len(assignments) > self._policy.maximum_fields:
            self._reject(RuntimeInstanceFailure.RESOURCE_LIMIT_EXCEEDED, 'Field input count exceeds the trusted service budget.', operation, request)
        for assignment in sorted(assignments, key=lambda a: a.field_id.value):
            if type(assignment.value) not in self._contract.value_types or not self._safe(assignment.value):
                self._reject(RuntimeInstanceFailure.UNSUPPORTED_FIELD_VALUE, 'Only approved immutable canonical field representations can enter authorization.', operation, request, field_id=assignment.field_id)
        if not self._safe(tuple(a.value for a in assignments)):
            self._reject(RuntimeInstanceFailure.RESOURCE_LIMIT_EXCEEDED, 'Aggregate input values exceed trusted service limits.', operation, request)
        if operation is RuntimeInstanceOperation.CREATE:
            self._identity(request.instance_identity, operation, request)
        elif request.state.contract_support is not self._contract or type(request.state.instance) is not self._contract.instance_type or not self._safe(request.state.instance):
            self._reject(RuntimeInstanceFailure.INTEGRITY_FAILURE, 'Existing state must use the approved deeply immutable canonical TYPE-08 contract.', operation, request)
        invocation = RuntimeInstanceAuthorizationRequest(self._binding, operation, request)
        authority = self._authorizer.authorize(invocation)
        if type(authority) is not RuntimeInstanceAuthority or authority.request is not invocation:
            self._reject(RuntimeInstanceFailure.AUTHORIZATION_MISMATCH, 'Authority does not match this exact service/operation/request invocation.', operation, request)

    def _identity(self, value: SemanticInstanceIdentity, operation: RuntimeInstanceOperation, request: object) -> RuntimeInstanceIdentityAssociation:
        support = self._contract
        if type(value) is not support.identity_type or not _immutable(value, support.approved_types,
                min(self._policy.maximum_value_nodes, 1024), min(self._policy.maximum_value_depth, 16),
                min(self._policy.maximum_scalar_units, 4096)) or support.adapter.valid_identity(value) is not True:
            self._reject(RuntimeInstanceFailure.INVALID_IDENTITY, 'A valid independent canonical TYPE-08 InstanceId is required.', operation, request)
        return RuntimeInstanceIdentityAssociation(support, value)

    def _safe(self, value: object) -> bool:
        return _immutable(value, self._contract.approved_types, self._policy.maximum_value_nodes,
            self._policy.maximum_value_depth, self._policy.maximum_scalar_units)

    def _definition(self, request: object, operation: RuntimeInstanceOperation, identity: ElementVersionRef | ElementRef) -> RuntimeModelDefinition:
        if type(identity) is not ElementVersionRef:
            self._reject(RuntimeInstanceFailure.VERSION_REQUIRED, 'An exact version is required; no implicit latest selection.', operation, request)
        if type(identity.element_id) is not SemanticElementId or type(identity.version) is not SemanticVersion:
            self._reject(RuntimeInstanceFailure.INVALID_IDENTITY, 'Definition binding requires actual validated exact coordinate leaves.', operation, request)
        try:
            result = self._registry.lookup(RuntimeModelLookupRequest(request.context.scope, identity))
        except RuntimeArtifactLoadError as error:
            self._reject(RuntimeInstanceFailure.LOOKUP_UNAVAILABLE, 'RUN-02 lookup rejected the explicit exact definition request.', operation, request, causes=error.diagnostics, incomplete=error.status is RuntimeArtifactLoadStatus.INCOMPLETE)
        if type(result) is not RuntimeModelLookupResult:
            self._reject(RuntimeInstanceFailure.INTEGRITY_FAILURE, 'Registry returned an unsupported lookup result contract.', operation, request)
        if result.status is not RuntimeModelLookupStatus.FOUND:
            code = RuntimeInstanceFailure.DEFINITION_NOT_FOUND if result.status is RuntimeModelLookupStatus.NOT_FOUND else RuntimeInstanceFailure.LOOKUP_UNAVAILABLE
            self._reject(code, 'Required registered exact definition is unavailable; no loading or upstream fallback.', operation, request, causes=result.diagnostics, incomplete=result.status is RuntimeModelLookupStatus.INCOMPLETE)
        definition = result.definitions[0]
        if definition.key.scope != request.context.scope or definition.identity != identity:
            self._reject(RuntimeInstanceFailure.DEFINITION_MISMATCH, 'Registry result differs from the requested exact scoped definition.', operation, request)
        # Recheck original RUN-01/RUN-02 typed association and graph integrity,
        # without reading, loading or decoding anything.
        try:
            definition.__post_init__()
        except RuntimeArtifactLoadError as error:
            self._reject(RuntimeInstanceFailure.INTEGRITY_FAILURE, 'Registered definition association no longer satisfies its runtime contract.', operation, request, causes=error.diagnostics)
        snapshot = request.context.snapshot
        if snapshot is not None:
            selected = tuple(d for d in snapshot.definitions if d.key == definition.key)
            if len(selected) != 1 or selected[0] is not definition:
                self._reject(RuntimeInstanceFailure.DEFINITION_NOT_FOUND, 'Supplied coherent snapshot does not contain the original selected exact registry entry.', operation, request)
        return definition

    def _schema(self, definition: RuntimeModelDefinition, request: object, operation: RuntimeInstanceOperation) -> RuntimeInstanceDefinitionSchema:
        return _resolve_instance_schema(definition, self._schemas, self._capabilities,
            self._policy, request, operation, self._reject)

    def _assignments(self, assignments: tuple[RuntimeInstanceFieldAssignment, ...], schema: RuntimeInstanceDefinitionSchema, request: object, operation: RuntimeInstanceOperation) -> dict[FieldId, SemanticFieldValue]:
        if len(assignments) > self._policy.maximum_fields:
            self._reject(RuntimeInstanceFailure.RESOURCE_LIMIT_EXCEEDED, 'Field assignment count exceeds the trusted budget.', operation, request)
        allowed = {f.id for f in schema.fields}
        result = {}
        # Sort only diagnostics for invalid input IDs; valid output follows the
        # encoded definition order, never caller insertion or alphabetic order.
        for assignment in sorted(assignments, key=lambda a: a.field_id.value):
            fid = assignment.field_id
            if fid not in allowed:
                self._reject(RuntimeInstanceFailure.UNKNOWN_FIELD, 'Assigned FieldId is not declared by this exact definition.', operation, request, field_id=fid)
            if fid in result:
                self._reject(RuntimeInstanceFailure.DUPLICATE_FIELD, 'Duplicate/conflicting assignment is forbidden even when values are equal.', operation, request, field_id=fid)
            if type(assignment.value) not in self._contract.value_types or not self._safe(assignment.value):
                self._reject(RuntimeInstanceFailure.UNSUPPORTED_FIELD_VALUE, 'Value is not an approved immutable canonical TYPE-08 representation within budget.', operation, request, field_id=fid)
            result[fid] = assignment.value
        if not self._safe(tuple(a.value for a in assignments)):
            self._reject(RuntimeInstanceFailure.RESOURCE_LIMIT_EXCEEDED, 'Aggregate immutable field values exceed the service budget.', operation, request)
        return result

    def _complete(self, assignments: dict[FieldId, SemanticFieldValue], schema: RuntimeInstanceDefinitionSchema, request: object, operation: RuntimeInstanceOperation, identity: RuntimeInstanceIdentityAssociation) -> tuple[RuntimeInstanceFieldAssignment, ...]:
        values = []
        for member in schema.fields:
            value = assignments.get(member.id)
            if member.id not in assignments:
                value = self._contract.adapter.missing()
                if type(value) is not self._contract.missing_type:
                    self._reject(RuntimeInstanceFailure.INTEGRITY_FAILURE, 'Canonical absent-field construction must return Missing, never Null or an invented default.', operation, request, identity=identity, field_id=member.id)
            if type(value) not in self._contract.value_types or not self._safe(value):
                self._reject(RuntimeInstanceFailure.INTEGRITY_FAILURE, 'Canonical Missing or retained value violates the approved immutable contract.', operation, request, identity=identity, field_id=member.id)
            values.append(RuntimeInstanceFieldAssignment(member.id, value))
        result = tuple(values)
        if not self._safe(tuple(a.value for a in result)):
            self._reject(RuntimeInstanceFailure.RESOURCE_LIMIT_EXCEEDED, 'Complete normalized values exceed aggregate service limits.', operation, request, identity=identity)
        return result

    def _canonical_view(self, instance: SemanticInstance, schema: RuntimeInstanceDefinitionSchema, request: object, operation: RuntimeInstanceOperation) -> tuple[RuntimeInstanceStateView, RuntimeInstanceIdentityAssociation]:
        if type(instance) is not self._contract.instance_type or not self._safe(instance):
            self._reject(RuntimeInstanceFailure.INTEGRITY_FAILURE, 'Canonical instance graph is not approved and deeply immutable within budget.', operation, request)
        view = self._contract.adapter.inspect_instance(instance)
        if type(view) is not RuntimeInstanceStateView:
            self._reject(RuntimeInstanceFailure.INTEGRITY_FAILURE, 'TYPE-08 adapter returned an unsupported instance projection.', operation, request)
        identity = self._identity(view.instance_identity, operation, request)
        if view.definition_identity != schema.definition.identity:
            self._reject(RuntimeInstanceFailure.DEFINITION_MISMATCH, 'Canonical instance is bound to a different exact definition.', operation, request, identity=identity)
        if view.semantic_context != request.context.scope.semantic_context:
            self._reject(RuntimeInstanceFailure.CONTEXT_MISMATCH, 'Canonical instance context differs from the selected operation scope.', operation, request, identity=identity)
        supplied = self._assignments(view.values, schema, request, operation)
        normalized = self._complete(supplied, schema, request, operation, identity)
        if view.values != normalized:
            self._reject(RuntimeInstanceFailure.INTEGRITY_FAILURE, 'Canonical instance projection must enumerate all fields in original declared order, including Missing.', operation, request, identity=identity)
        return view, identity

    def _old_state(self, state: RuntimeInstanceState, request: object, operation: RuntimeInstanceOperation, definition: RuntimeModelDefinition, schema: RuntimeInstanceDefinitionSchema) -> tuple[RuntimeInstanceStateView, RuntimeInstanceIdentityAssociation]:
        if state.context.scope != request.context.scope:
            self._reject(RuntimeInstanceFailure.CONTEXT_MISMATCH, 'Existing instance belongs to another semantic context/runtime target scope.', operation, request)
        if state.contract_support is not self._contract or state.definition is not definition:
            self._reject(RuntimeInstanceFailure.DEFINITION_MISMATCH, 'Instance must retain the same original exact registry entry and canonical contract approval.', operation, request)
        if state.revision.value > self._policy.maximum_revision:
            self._reject(RuntimeInstanceFailure.RESOURCE_LIMIT_EXCEEDED, 'Instance local revision exceeds trusted limits.', operation, request)
        view, identity = self._canonical_view(state.instance, schema, request, operation)
        self._validate_instance(state.instance, definition, request.context, state.revision, request, operation, identity)
        return view, identity

    def _construct(self, identity: RuntimeInstanceIdentityAssociation, values: tuple[RuntimeInstanceFieldAssignment, ...], schema: RuntimeInstanceDefinitionSchema, request: object, operation: RuntimeInstanceOperation, revision: RuntimeInstanceRevision) -> RuntimeInstanceState:
        instance = self._contract.adapter.construct(identity.identity, schema.definition.identity, request.context.scope.semantic_context, values)
        view, actual_identity = self._canonical_view(instance, schema, request, operation)
        if actual_identity.identity != identity.identity or view.values != values:
            self._reject(RuntimeInstanceFailure.INTEGRITY_FAILURE, 'Canonical construction changed identity or explicit validated values.', operation, request, identity=identity)
        if operation is RuntimeInstanceOperation.UPDATE and instance is request.state.instance:
            self._reject(RuntimeInstanceFailure.INTEGRITY_FAILURE, 'Successful update must return a new immutable canonical instance object.', operation, request, identity=identity)
        return RuntimeInstanceState(instance, request.context, schema.definition, revision, self._contract)

    def create(self, request: RuntimeInstanceCreateRequest) -> RuntimeInstanceOperationResult:
        operation = RuntimeInstanceOperation.CREATE
        identity = None
        try:
            self._preflight(request, operation)
            identity = self._identity(request.instance_identity, operation, request)
            definition = self._definition(request, operation, request.definition_identity)
            schema = self._schema(definition, request, operation)
            supplied = self._assignments(request.values, schema, request, operation)
            values = self._complete(supplied, schema, request, operation, identity)
            state = self._construct(identity, values, schema, request, operation, RuntimeInstanceRevision(0))
            validation = self._validate_instance(state.instance, definition, request.context, state.revision, request, operation, identity)
            return RuntimeInstanceOperationResult(RuntimeArtifactLoadStatus.SUCCEEDED, state, validation_result=validation)
        except RuntimeInstanceError as error:
            return RuntimeInstanceOperationResult(error.status, diagnostics=tuple(replace(d, instance_identity=d.instance_identity or identity) for d in error.diagnostics), validation_result=error.validation_result)

    def update(self, request: RuntimeInstanceUpdateRequest) -> RuntimeInstanceOperationResult:
        operation = RuntimeInstanceOperation.UPDATE
        identity = None
        try:
            self._preflight(request, operation)
            definition = self._definition(request, operation, request.definition_identity)
            schema = self._schema(definition, request, operation)
            view, identity = self._old_state(request.state, request, operation, definition, schema)
            if request.expected_revision != request.state.revision:
                self._reject(RuntimeInstanceFailure.REVISION_MISMATCH, 'Expected revision does not match the supplied immutable state.', operation, request, identity=identity)
            if request.state.revision.value >= self._policy.maximum_revision:
                self._reject(RuntimeInstanceFailure.RESOURCE_LIMIT_EXCEEDED, 'A new local revision would exceed trusted limits.', operation, request, identity=identity)
            supplied = {a.field_id: a.value for a in view.values}
            supplied.update(self._assignments(request.changes, schema, request, operation))
            values = self._complete(supplied, schema, request, operation, identity)
            state = self._construct(identity, values, schema, request, operation, RuntimeInstanceRevision(request.state.revision.value + 1))
            validation = self._validate_instance(state.instance, definition, request.context, state.revision, request, operation, identity)
            return RuntimeInstanceOperationResult(RuntimeArtifactLoadStatus.SUCCEEDED, state, validation_result=validation)
        except RuntimeInstanceError as error:
            return RuntimeInstanceOperationResult(error.status, diagnostics=tuple(replace(d, instance_identity=d.instance_identity or identity) for d in error.diagnostics), validation_result=error.validation_result)

    def inspect(self, request: RuntimeInstanceInspectRequest) -> RuntimeInstanceInspectionResult:
        operation = RuntimeInstanceOperation.INSPECT
        identity = None
        try:
            self._preflight(request, operation)
            definition = self._definition(request, operation, request.state.definition.identity)
            schema = self._schema(definition, request, operation)
            view, identity = self._old_state(request.state, request, operation, definition, schema)
            values = view.values
            status = RuntimeInstanceInspectionStatus.FOUND
            if request.field_id is not None:
                values = tuple(a for a in values if a.field_id == request.field_id)
                if not values:
                    self._reject(RuntimeInstanceFailure.UNKNOWN_FIELD, 'Requested FieldId is not declared by the selected exact definition.', operation, request, identity=identity, field_id=request.field_id)
                if type(values[0].value) is self._contract.missing_type:
                    status = RuntimeInstanceInspectionStatus.MISSING
            result = RuntimeInstanceInspectionView(identity, definition.identity, request.context, request.state.revision, values)
            return RuntimeInstanceInspectionResult(status, result)
        except RuntimeInstanceError as error:
            code = error.diagnostics[0].code
            status = RuntimeInstanceInspectionStatus.INVALID_FIELD if code is RuntimeInstanceFailure.UNKNOWN_FIELD else RuntimeInstanceInspectionStatus.INVALID_CONTEXT if code in (RuntimeInstanceFailure.CONTEXT_MISMATCH, RuntimeInstanceFailure.INVALID_SCOPE) else RuntimeInstanceInspectionStatus.INCOMPLETE if error.status is RuntimeArtifactLoadStatus.INCOMPLETE else RuntimeInstanceInspectionStatus.FAILED
            return RuntimeInstanceInspectionResult(status, diagnostics=tuple(replace(d, instance_identity=d.instance_identity or identity) for d in error.diagnostics))


__all__ = [name for name in globals() if name.startswith(('RuntimeInstance', 'RuntimeSemanticInstance', 'SemanticInstance', 'RuntimeValidation'))] + ['MODULE_NAME', 'SemanticFieldValue', 'RuntimePrimitiveValue', 'DefaultSemanticInstanceRuntime', 'RuntimeValidator', 'DefaultRuntimeValidator']


# RUN-06: observational application composition, no upward runtime-core imports.
class RuntimeErrorCategory(Enum):
    INVALID_REQUEST = 'invalid-request'
    INVALID_STATE = 'invalid-state'
    NOT_FOUND = 'not-found'
    CONFLICT = 'conflict'
    VALIDATION = 'validation'
    AUTHORIZATION = 'authorization'
    INTEGRITY = 'integrity'
    COMPATIBILITY = 'compatibility'
    UNSUPPORTED_CAPABILITY = 'unsupported-capability'
    RESOURCE_LIMIT = 'resource-limit'
    INFRASTRUCTURE = 'infrastructure'
    INTERNAL = 'internal'
    UNKNOWN = 'unknown'


class RuntimeErrorOperation(Enum):
    ARTIFACT_LOAD = 'artifact-load'
    ARTIFACT_READ = 'artifact-read'
    MODEL_REGISTER = 'model-register'
    MODEL_LOOKUP = 'model-lookup'
    MODEL_INSPECT_NAME = 'model-inspect-name'
    MODEL_ENUMERATE_VERSIONS = 'model-enumerate-versions'
    MODEL_MEMBERSHIP = 'model-membership'
    MODEL_SNAPSHOT = 'model-snapshot'
    INSTANCE_CREATE = 'instance-create'
    INSTANCE_UPDATE = 'instance-update'
    INSTANCE_INSPECT = 'instance-inspect'
    INSTANCE_VALIDATE = 'instance-validate'
    CONTEXT_CREATE = 'context-create'
    CONTEXT_DERIVE = 'context-derive'


# Closed original code mapping; category is never inferred from message text.
# Reader CMP-061..080 is the actual existing neutral RUN-01 reader projection,
# not a new compiler import/dependency or renamed compiler diagnostic.
_RUNTIME_ERROR_CATEGORY_GROUPS = (
    (RuntimeErrorCategory.INVALID_REQUEST, '001 101 102 108 109 110 116 201 204 206 209 301 305 307 308 401 402 403 404 405 406 407 409 412 413 414'),
    (RuntimeErrorCategory.AUTHORIZATION, '002 003 103 104 202 203 408 410 411 416 417 418 422'),
    (RuntimeErrorCategory.INTEGRITY, '004 005 007 020 105 106 113 121 207 208 219 303 304 423'),
    (RuntimeErrorCategory.COMPATIBILITY, '008 009 010 013 014 021'),
    (RuntimeErrorCategory.UNSUPPORTED_CAPABILITY, '011 015 016 019 107 117 119 120 216 217 220 222 302 306 319 321 415 419 424'),
    (RuntimeErrorCategory.RESOURCE_LIMIT, '018 118 221 320 420 421'),
    (RuntimeErrorCategory.CONFLICT, '017 111 112 115 211 218'),
    (RuntimeErrorCategory.NOT_FOUND, '114 205'),
    (RuntimeErrorCategory.VALIDATION, '012 210 212 213 214 215 309 310 311 312 313 314 315 316 317 318'),
)
_RUNTIME_ERROR_CATEGORIES = {'RUN-' + number: category for category, values in _RUNTIME_ERROR_CATEGORY_GROUPS for number in values.split()}
_RUNTIME_ERROR_CATEGORIES.update({'RUN-006': RuntimeErrorCategory.UNKNOWN,
    'RUN-207': RuntimeErrorCategory.INVALID_STATE, 'RUN-208': RuntimeErrorCategory.INVALID_STATE,
    'RUN-423': RuntimeErrorCategory.INVALID_STATE, 'RUN-409': RuntimeErrorCategory.AUTHORIZATION,
    'RUN-501': RuntimeErrorCategory.INTERNAL, 'RUN-502': RuntimeErrorCategory.INFRASTRUCTURE,
    'RUN-503': RuntimeErrorCategory.UNKNOWN, 'RUN-505': RuntimeErrorCategory.UNKNOWN})
_RUNTIME_ERROR_CATEGORIES.update({'CMP-' + str(n): category for category, numbers in (
    (RuntimeErrorCategory.INVALID_REQUEST, (61, 64, 65, 66, 68, 80)),
    (RuntimeErrorCategory.COMPATIBILITY, (62, 67, 69, 79)),
    (RuntimeErrorCategory.INTEGRITY, (63, 73, 74, 75, 77, 78)),
    (RuntimeErrorCategory.RESOURCE_LIMIT, (72,)),
    (RuntimeErrorCategory.INFRASTRUCTURE, (70, 71, 76))) for n in numbers})
# CMP code values contain exactly three digits.
_RUNTIME_ERROR_CATEGORIES.update({f'CMP-{n:03d}': _RUNTIME_ERROR_CATEGORIES.pop('CMP-' + str(n)) for n in range(61, 81)})
_RUNTIME_ERROR_MESSAGES = {
    RuntimeErrorCategory.INVALID_REQUEST: 'The runtime request is invalid.',
    RuntimeErrorCategory.INVALID_STATE: 'The runtime state does not permit this operation.',
    RuntimeErrorCategory.NOT_FOUND: 'The exact requested runtime resource was not found.',
    RuntimeErrorCategory.CONFLICT: 'The runtime operation conflicts with existing state.',
    RuntimeErrorCategory.VALIDATION: 'Runtime validation reported a definite violation.',
    RuntimeErrorCategory.AUTHORIZATION: 'The required runtime authority could not be established.',
    RuntimeErrorCategory.INTEGRITY: 'Runtime integrity evidence does not match the required association.',
    RuntimeErrorCategory.COMPATIBILITY: 'The runtime representation is incompatible with the requested operation.',
    RuntimeErrorCategory.UNSUPPORTED_CAPABILITY: 'A required runtime prerequisite or capability is unavailable.',
    RuntimeErrorCategory.RESOURCE_LIMIT: 'The runtime operation exceeds its supported resource limits.',
    RuntimeErrorCategory.INFRASTRUCTURE: 'The runtime operation encountered an infrastructure failure.',
    RuntimeErrorCategory.INTERNAL: 'The runtime operation encountered an internal failure.',
    RuntimeErrorCategory.UNKNOWN: 'The runtime failure has no usable cause detail.',
}


_RUNTIME_ERROR_CATEGORIES = MappingProxyType(_RUNTIME_ERROR_CATEGORIES)
_RUNTIME_ERROR_MESSAGES = MappingProxyType(_RUNTIME_ERROR_MESSAGES)

@dataclass(frozen=True, slots=True)
class RuntimeErrorCode:
    value: str

    def __post_init__(self) -> None:
        if type(self.value) is not str or self.value not in _RUNTIME_ERROR_CATEGORIES:
            raise ValueError('Error code must be a known original runtime/reader code or explicit safe boundary fallback.')


@dataclass(frozen=True, slots=True)
class RuntimeErrorContext:
    semantic_context: SemanticContextRef | None = None
    runtime_target: RuntimeTargetId | None = None
    registry_scope: RuntimeModelRegistryScope | None = None
    invocation_identity: RuntimeInvocationId | None = None
    correlation_identity: ExecutionCorrelationId | None = None
    causation: ExecutionCausationRef | None = None

    def __post_init__(self) -> None:
        for value, expected in ((self.semantic_context, SemanticContextRef), (self.runtime_target, RuntimeTargetId), (self.registry_scope, RuntimeModelRegistryScope), (self.invocation_identity, RuntimeInvocationId), (self.correlation_identity, ExecutionCorrelationId), (self.causation, ExecutionCausationRef)):
            if value is not None and type(value) is not expected:
                raise TypeError('Error context includes only actual available immutable coordinates, never a full request or credential.')
        if self.registry_scope is not None and (self.semantic_context not in (None, self.registry_scope.semantic_context) or self.runtime_target not in (None, self.registry_scope.runtime_target)):
            raise ValueError('Error semantic/target coordinates cannot contradict registry scope.')

    @classmethod
    def from_execution(cls, context: ExecutionContext) -> 'RuntimeErrorContext':
        if type(context) is not ExecutionContext:
            raise TypeError('Only an explicit actual existing execution context may supply error coordinates.')
        return cls(context.semantic_context, context.registry_scope.runtime_target, context.registry_scope,
            context.invocation_identity, context.correlation_identity, context.causation)


@dataclass(frozen=True, slots=True)
class RuntimeErrorTarget:
    artifact_key: CompilationArtifactKey | None = None
    artifact_kind: CompilationArtifactKind | None = None
    manifest_identity: str | None = None
    definitions: tuple[ElementVersionRef, ...] = ()
    instance_identity: RuntimeInstanceIdentityAssociation | None = field(default=None, repr=False)
    field_id: FieldId | None = None
    constraint_kind: ConstraintKind | None = None
    revision: RuntimeInstanceRevision | None = None

    def __post_init__(self) -> None:
        for value, expected in ((self.artifact_key, CompilationArtifactKey), (self.artifact_kind, CompilationArtifactKind), (self.instance_identity, RuntimeInstanceIdentityAssociation), (self.field_id, FieldId), (self.constraint_kind, ConstraintKind), (self.revision, RuntimeInstanceRevision)):
            if value is not None and type(value) is not expected:
                raise TypeError('Runtime targets preserve actual stable field/instance/artifact/version coordinates.')
        if not _typed_tuple(self.definitions, ElementVersionRef) or len(self.definitions) > 128 or any(type(r.element_id) is not SemanticElementId or type(r.version) is not SemanticVersion for r in self.definitions):
            raise TypeError('Definition associations must be a bounded immutable exact-reference tuple.')
        if self.manifest_identity is not None and (type(self.manifest_identity) is not str or len(self.manifest_identity) > 160 or re.fullmatch(r'manifest-[a-z][a-z0-9]*(?:[.-][a-z0-9]+)*', self.manifest_identity) is None):
            raise TypeError('Manifest identity is a bounded original operational token, never an inferred semantic ID.')


_ERROR_DIAGNOSTIC_TYPES = (RuntimeArtifactLoadDiagnostic, RuntimeArtifactReaderDiagnostic,
    RuntimeInstanceDiagnostic, RuntimeValidationDiagnostic, ExecutionContextDiagnostic)


@dataclass(frozen=True, slots=True)
class RuntimeErrorDiagnosticAssociation:
    """Actual existing typed diagnostic reference, not another Diagnostic model."""
    source: RuntimeArtifactLoadDiagnostic | RuntimeArtifactReaderDiagnostic | RuntimeInstanceDiagnostic | RuntimeValidationDiagnostic | ExecutionContextDiagnostic = field(repr=False)
    source_index: int

    def __post_init__(self) -> None:
        if type(self.source) not in _ERROR_DIAGNOSTIC_TYPES or type(self.source_index) is not int or self.source_index < 0:
            raise TypeError('Association retains original immutable diagnostic occurrence and explicit source ordering.')

    @property
    def code(self) -> str:
        return self.source.code if type(self.source) is RuntimeArtifactReaderDiagnostic else self.source.code.value


class RuntimeErrorCauseKind(Enum):
    DIRECT_UNDERLYING = 'direct-underlying'
    RELATED_DIAGNOSTIC = 'related-diagnostic'


@dataclass(frozen=True, slots=True)
class RuntimeErrorCause:
    """Flat immutable snapshot. No exception, parent error pointer or recursive cause field."""
    kind: RuntimeErrorCauseKind
    code: RuntimeErrorCode | None
    category: RuntimeErrorCategory
    operation: RuntimeErrorOperation
    context: RuntimeErrorContext
    target: RuntimeErrorTarget
    diagnostic: RuntimeErrorDiagnosticAssociation | None = field(default=None, repr=False)
    depth: int = 1

    def __post_init__(self) -> None:
        if type(self.kind) is not RuntimeErrorCauseKind or self.code is not None and type(self.code) is not RuntimeErrorCode or type(self.category) is not RuntimeErrorCategory or type(self.operation) is not RuntimeErrorOperation or type(self.context) is not RuntimeErrorContext or type(self.target) is not RuntimeErrorTarget or self.diagnostic is not None and type(self.diagnostic) is not RuntimeErrorDiagnosticAssociation or type(self.depth) is not int or not 1 <= self.depth <= 32:
            raise TypeError('Cause is a bounded typed actual failure snapshot; correlation alone is not cause evidence.')
        if self.code is None and self.diagnostic is None:
            raise ValueError('Unknown code cause must retain the actual original diagnostic, never invented evidence.')
        if self.code is not None and self.category is not _runtime_error_category(self.code, (self.diagnostic,) if self.diagnostic is not None else ()):
            raise ValueError('Cause code/category must retain actual known lower diagnostic classification.')


def _runtime_error_category(code: RuntimeErrorCode, diagnostics: tuple[RuntimeErrorDiagnosticAssociation, ...]) -> RuntimeErrorCategory:
    if code.value == 'RUN-006':
        readers = []
        overflow = False
        for ref in diagnostics[:1024]:
            if type(ref.source) is RuntimeArtifactLoadDiagnostic:
                inventory = ref.source.reader_diagnostics
                remaining = 1024 - len(readers)
                readers.extend(inventory[:remaining])
                overflow = overflow or len(inventory) > remaining
            elif type(ref.source) is RuntimeArtifactReaderDiagnostic and len(readers) < 1024:
                readers.append(ref.source)
        categories = {_RUNTIME_ERROR_CATEGORIES.get(d.code, RuntimeErrorCategory.UNKNOWN)
            for d in readers if d.severity is RuntimeLoadSeverity.ERROR}
        if RuntimeErrorCategory.INTEGRITY in categories:
            return RuntimeErrorCategory.INTEGRITY
        if overflow:
            return RuntimeErrorCategory.UNKNOWN
        for category in (RuntimeErrorCategory.RESOURCE_LIMIT, RuntimeErrorCategory.COMPATIBILITY,
                         RuntimeErrorCategory.INFRASTRUCTURE, RuntimeErrorCategory.INVALID_REQUEST):
            if category in categories:
                return category
        return RuntimeErrorCategory.UNKNOWN
    return _RUNTIME_ERROR_CATEGORIES[code.value]


def _runtime_safe_error_message(code: RuntimeErrorCode, category: RuntimeErrorCategory) -> str:
    return 'The request could not be completed.' if code.value == 'RUN-505' else _RUNTIME_ERROR_MESSAGES[category]


@dataclass(frozen=True, slots=True)
class RuntimeErrorDetail:
    code: RuntimeErrorCode
    category: RuntimeErrorCategory
    severity: RuntimeLoadSeverity
    operation: RuntimeErrorOperation
    context: RuntimeErrorContext
    target: RuntimeErrorTarget
    safe_message: str
    diagnostics: tuple[RuntimeErrorDiagnosticAssociation, ...] = field(default=(), repr=False)
    causes: tuple[RuntimeErrorCause, ...] = field(default=(), repr=False)
    omitted_diagnostics: int = 0
    omitted_causes: int = 0
    omitted_targets: int = 0

    def __post_init__(self) -> None:
        if type(self.code) is not RuntimeErrorCode or type(self.category) is not RuntimeErrorCategory or type(self.severity) is not RuntimeLoadSeverity or type(self.operation) is not RuntimeErrorOperation or type(self.context) is not RuntimeErrorContext or type(self.target) is not RuntimeErrorTarget:
            raise TypeError('Runtime error is an immutable value, not a Python exception or operation result.')
        if not _typed_tuple(self.diagnostics, RuntimeErrorDiagnosticAssociation) or len(self.diagnostics) > 1024 or not _typed_tuple(self.causes, RuntimeErrorCause) or len(self.causes) > 128:
            raise TypeError('Error details have hard bounded immutable diagnostic/cause membership.')
        if self.category is not _runtime_error_category(self.code, self.diagnostics) or type(self.safe_message) is not str or self.safe_message != _runtime_safe_error_message(self.code, self.category):
            raise ValueError('Code/category/message must use the actual controlled mapping, never raw exception text.')
        if any(type(v) is not int or v < 0 for v in (self.omitted_diagnostics, self.omitted_causes, self.omitted_targets)):
            raise ValueError('Every dropped detail has explicit nonnegative omission evidence.')

    @property
    def detail_complete(self) -> bool:
        return self.category is not RuntimeErrorCategory.UNKNOWN and self.omitted_diagnostics == self.omitted_causes == self.omitted_targets == 0 and all(c.code is not None and c.category is not RuntimeErrorCategory.UNKNOWN for c in self.causes)


@dataclass(frozen=True, slots=True)
class RuntimeErrorCollection:
    errors: tuple[RuntimeErrorDetail, ...] = ()
    omitted_errors: int = 0

    def __post_init__(self) -> None:
        if not _typed_tuple(self.errors, RuntimeErrorDetail) or len(self.errors) > 1024 or type(self.omitted_errors) is not int or self.omitted_errors < 0:
            raise TypeError('Collection preserves ordered occurrences/duplicates and explicit capacity omissions.')

    @property
    def detail_complete(self) -> bool:
        return self.omitted_errors == 0 and all(e.detail_complete for e in self.errors)


@dataclass(frozen=True, slots=True)
class RuntimeErrorResultAssociation:
    operation: RuntimeErrorOperation
    source_status: RuntimeArtifactLoadStatus | RuntimeModelLookupStatus | RuntimeInstanceInspectionStatus | RuntimeValidationStatus
    errors: RuntimeErrorCollection
    diagnostics: tuple[RuntimeErrorDiagnosticAssociation, ...] = field(default=(), repr=False)
    omitted_diagnostics: int = 0
    validation_complete: bool | None = None

    def __post_init__(self) -> None:
        if type(self.operation) is not RuntimeErrorOperation or type(self.source_status) not in (RuntimeArtifactLoadStatus, RuntimeModelLookupStatus, RuntimeInstanceInspectionStatus, RuntimeValidationStatus) or type(self.errors) is not RuntimeErrorCollection or not _typed_tuple(self.diagnostics, RuntimeErrorDiagnosticAssociation) or len(self.diagnostics) > 1024:
            raise TypeError('Association retains authoritative original status, without a replacement generic result.')
        if type(self.omitted_diagnostics) is not int or self.omitted_diagnostics < 0 or self.validation_complete is not None and type(self.validation_complete) is not bool:
            raise TypeError('Detail omissions and validation completeness remain separate from status.')
        if self.operation is RuntimeErrorOperation.INSTANCE_VALIDATE:
            if type(self.source_status) is not RuntimeValidationStatus or self.validation_complete is None:
                raise ValueError('Validation interoperability preserves VALID/INVALID/INCOMPLETE and completeness.')
        elif self.validation_complete is not None:
            raise ValueError('Only actual validation result supplies validation completeness.')
        expected_status = RuntimeModelLookupStatus if self.operation in (RuntimeErrorOperation.MODEL_LOOKUP, RuntimeErrorOperation.MODEL_INSPECT_NAME, RuntimeErrorOperation.MODEL_MEMBERSHIP, RuntimeErrorOperation.MODEL_ENUMERATE_VERSIONS) else RuntimeInstanceInspectionStatus if self.operation is RuntimeErrorOperation.INSTANCE_INSPECT else RuntimeValidationStatus if self.operation is RuntimeErrorOperation.INSTANCE_VALIDATE else RuntimeArtifactLoadStatus
        if type(self.source_status) is not expected_status:
            raise ValueError('Source status family must match the original operation-specific result.')
        if self.source_status in (RuntimeArtifactLoadStatus.SUCCEEDED, RuntimeModelLookupStatus.FOUND, RuntimeInstanceInspectionStatus.FOUND, RuntimeInstanceInspectionStatus.MISSING, RuntimeValidationStatus.VALID) and (self.errors.errors or self.errors.omitted_errors):
            raise ValueError('Successful authoritative result cannot acquire fabricated failure evidence.')
        if self.source_status in (RuntimeArtifactLoadStatus.SUCCEEDED, RuntimeModelLookupStatus.FOUND, RuntimeInstanceInspectionStatus.FOUND, RuntimeInstanceInspectionStatus.MISSING, RuntimeValidationStatus.VALID) and any(d.source.severity is RuntimeLoadSeverity.ERROR for d in self.diagnostics):
            raise ValueError('Successful result association cannot retain contradictory fatal diagnostics.')
        if self.source_status not in (RuntimeArtifactLoadStatus.SUCCEEDED, RuntimeModelLookupStatus.FOUND, RuntimeModelLookupStatus.NOT_FOUND, RuntimeModelLookupStatus.AMBIGUOUS, RuntimeInstanceInspectionStatus.FOUND, RuntimeInstanceInspectionStatus.MISSING, RuntimeValidationStatus.VALID) and not self.errors.errors and self.errors.omitted_errors == 0:
            raise ValueError('Failure/incomplete association needs known errors or explicit unavailable-detail fallback.')

    @property
    def detail_complete(self) -> bool:
        return self.omitted_diagnostics == 0 and self.errors.detail_complete


@dataclass(frozen=True, slots=True)
class RuntimeErrorPolicy:
    maximum_errors: int = 128
    maximum_diagnostics: int = 256
    maximum_causes: int = 32
    maximum_cause_depth: int = 8
    maximum_targets: int = 128
    maximum_message_length: int = 256

    def __post_init__(self) -> None:
        ceilings = (1024, 1024, 128, 32, 128, 1024)
        if any(type(getattr(self, f.name)) is not int or not 1 <= getattr(self, f.name) <= ceiling for f, ceiling in zip(fields(self), ceilings)):
            raise ValueError('Owner error-detail ceilings are positive actual bounded integers.')
        if self.maximum_message_length < max(len(m) for m in _RUNTIME_ERROR_MESSAGES.values()):
            raise ValueError('Message budget must admit every controlled template; never truncate machine meaning.')


class RuntimeErrorFactory:
    """Pure mapping/composition. No validators, registry/instance actions or IO."""
    __slots__ = ('_policy',)

    def __init__(self, policy: RuntimeErrorPolicy | None = None):
        if policy is not None and type(policy) is not RuntimeErrorPolicy:
            raise TypeError('Owner supplies an immutable typed error construction policy.')
        self._policy = RuntimeErrorPolicy() if policy is None else policy

    @staticmethod
    def _context(source, supplied=None):
        if supplied is not None and type(supplied) is not RuntimeErrorContext:
            raise TypeError('Explicit supplied error context must contain actual trusted typed coordinates.')
        scope = source.registry_scope if type(source) is RuntimeArtifactLoadDiagnostic else source.scope if type(source) in (RuntimeInstanceDiagnostic, RuntimeValidationDiagnostic) else source.registry_scope if type(source) is ExecutionContextDiagnostic else None
        semantic = source.semantic_context if type(source) in (RuntimeArtifactLoadDiagnostic, ExecutionContextDiagnostic) else scope.semantic_context if scope is not None else None
        target = source.runtime_target if type(source) is RuntimeArtifactLoadDiagnostic else scope.runtime_target if scope is not None else None
        invocation = source.invocation_identity if type(source) is ExecutionContextDiagnostic else None
        correlation = source.correlation_identity if type(source) is ExecutionContextDiagnostic else None
        cause = source.causation if type(source) is ExecutionContextDiagnostic else None
        values = (semantic, target, scope, invocation, correlation, cause)
        if supplied is not None:
            original = tuple(getattr(supplied, f.name) for f in fields(supplied))
            if any(a is not None and b is not None and a != b for a, b in zip(values, original)):
                raise ValueError('Supplied context cannot overwrite contradictory original diagnostic associations.')
            values = tuple(a if a is not None else b for a, b in zip(values, original))
        return RuntimeErrorContext(*values)

    def _target(self, source):
        refs = source.semantic_origins if type(source) is RuntimeArtifactLoadDiagnostic else ()
        exact = source.definition_identity if type(source) in (RuntimeArtifactLoadDiagnostic, RuntimeInstanceDiagnostic, RuntimeValidationDiagnostic, ExecutionContextDiagnostic) else None
        if exact is not None and exact not in refs:
            refs = (exact, *refs)
        maximum = self._policy.maximum_targets
        manifest = source.manifest_identity if type(source) in (RuntimeArtifactLoadDiagnostic, RuntimeArtifactReaderDiagnostic) else None
        manifest_safe = manifest is not None and len(manifest) <= 160 and re.fullmatch(r'manifest-[a-z][a-z0-9]*(?:[.-][a-z0-9]+)*', manifest) is not None
        return RuntimeErrorTarget(
            source.artifact_key if type(source) in (RuntimeArtifactLoadDiagnostic, RuntimeArtifactReaderDiagnostic) else None,
            source.artifact_kind if type(source) in (RuntimeArtifactLoadDiagnostic, RuntimeArtifactReaderDiagnostic) else None,
            manifest if manifest_safe else None,
            refs[:maximum], source.instance_identity if type(source) in (RuntimeInstanceDiagnostic, RuntimeValidationDiagnostic) else None,
            source.field_id if type(source) in (RuntimeInstanceDiagnostic, RuntimeValidationDiagnostic) else None,
            source.constraint_kind if type(source) in (RuntimeInstanceDiagnostic, RuntimeValidationDiagnostic) else None,
            source.expected_revision if type(source) is RuntimeInstanceDiagnostic else source.revision if type(source) is RuntimeValidationDiagnostic else None), max(0, len(refs) - maximum) + int(manifest is not None and not manifest_safe)

    def create(self, code: RuntimeErrorCode, operation: RuntimeErrorOperation, *, context: RuntimeErrorContext | None = None,
               target: RuntimeErrorTarget | None = None, severity: RuntimeLoadSeverity = RuntimeLoadSeverity.ERROR,
               diagnostics: tuple[RuntimeErrorDiagnosticAssociation, ...] = (), causes: tuple[RuntimeErrorCause, ...] = (),
               omitted_diagnostics: int = 0, omitted_causes: int = 0, omitted_targets: int = 0) -> RuntimeErrorDetail:
        if type(code) is not RuntimeErrorCode or type(operation) is not RuntimeErrorOperation or not _typed_tuple(diagnostics, RuntimeErrorDiagnosticAssociation) or not _typed_tuple(causes, RuntimeErrorCause):
            raise TypeError('Factory constructs from typed explicit codes/operations/known evidence only.')
        if any(type(v) is not int or v < 0 for v in (omitted_diagnostics, omitted_causes, omitted_targets)):
            raise ValueError('Omission counts must be actual nonnegative integers, not Boolean counters.')
        kept = diagnostics[:self._policy.maximum_diagnostics]
        kept_causes = tuple(c for c in causes[:self._policy.maximum_causes] if c.depth <= self._policy.maximum_cause_depth)
        category = _runtime_error_category(code, kept)
        actual_target = RuntimeErrorTarget() if target is None else target
        if type(actual_target) is not RuntimeErrorTarget:
            raise TypeError('Target must preserve actual immutable owned coordinates.')
        omitted_targets += max(0, len(actual_target.definitions) - self._policy.maximum_targets)
        actual_target = replace(actual_target, definitions=actual_target.definitions[:self._policy.maximum_targets])
        return RuntimeErrorDetail(code, category, severity, operation,
            RuntimeErrorContext() if context is None else context, actual_target,
            _runtime_safe_error_message(code, category), kept, kept_causes,
            omitted_diagnostics + len(diagnostics) - len(kept), omitted_causes + len(causes) - len(kept_causes), omitted_targets)

    @staticmethod
    def _source_operation(source, fallback):
        if type(source) is RuntimeArtifactLoadDiagnostic and source.registry_operation is not None:
            return {RuntimeModelRegistryOperation.REGISTER: RuntimeErrorOperation.MODEL_REGISTER,
                RuntimeModelRegistryOperation.LOOKUP: RuntimeErrorOperation.MODEL_LOOKUP,
                RuntimeModelRegistryOperation.INSPECT_NAME: RuntimeErrorOperation.MODEL_INSPECT_NAME,
                RuntimeModelRegistryOperation.ENUMERATE_VERSIONS: RuntimeErrorOperation.MODEL_ENUMERATE_VERSIONS,
                RuntimeModelRegistryOperation.SNAPSHOT: RuntimeErrorOperation.MODEL_SNAPSHOT}[source.registry_operation]
        return fallback

    def _diagnostic_error(self, source, operation, index, supplied=None):
        association = RuntimeErrorDiagnosticAssociation(source, index)
        known = association.code in _RUNTIME_ERROR_CATEGORIES
        code = RuntimeErrorCode(association.code if known else 'RUN-503')
        target, omitted = self._target(source)
        lower = source.reader_diagnostics if type(source) is RuntimeArtifactLoadDiagnostic else source.registry_causes if type(source) is RuntimeInstanceDiagnostic else ()
        related, causes, lower_omitted_targets = [association], [], 0
        for i, diagnostic in enumerate(lower[:self._policy.maximum_causes]):
            ref = RuntimeErrorDiagnosticAssociation(diagnostic, i)
            related.append(ref)
            raw = ref.code
            cause_code = RuntimeErrorCode(raw) if raw in _RUNTIME_ERROR_CATEGORIES else None
            cause_target, dropped = self._target(diagnostic)
            lower_omitted_targets += dropped
            causes.append(RuntimeErrorCause(RuntimeErrorCauseKind.DIRECT_UNDERLYING if diagnostic.severity is RuntimeLoadSeverity.ERROR else RuntimeErrorCauseKind.RELATED_DIAGNOSTIC, cause_code,
                _RUNTIME_ERROR_CATEGORIES[raw] if cause_code is not None else RuntimeErrorCategory.UNKNOWN,
                RuntimeErrorOperation.ARTIFACT_READ if type(source) is RuntimeArtifactLoadDiagnostic else self._source_operation(diagnostic, RuntimeErrorOperation.MODEL_LOOKUP),
                self._context(diagnostic), cause_target, ref))
        return self.create(code, operation, context=self._context(source, supplied), target=target,
            severity=source.severity, diagnostics=tuple(related), causes=tuple(causes),
            omitted_causes=max(0, len(lower) - len(causes)), omitted_targets=omitted + lower_omitted_targets)

    def wrap(self, lower: RuntimeErrorDetail, code: RuntimeErrorCode, operation: RuntimeErrorOperation, *, context: RuntimeErrorContext | None = None, target: RuntimeErrorTarget | None = None) -> RuntimeErrorDetail:
        if type(lower) is not RuntimeErrorDetail:
            raise TypeError('Wrapping needs an actual lower failure, never shared correlation or an exception guess.')
        direct = RuntimeErrorCause(RuntimeErrorCauseKind.DIRECT_UNDERLYING, lower.code, lower.category,
            lower.operation, lower.context, lower.target, lower.diagnostics[0] if lower.diagnostics else None)
        deeper = tuple(replace(c, depth=c.depth + 1) for c in lower.causes if c.depth < 32)
        return self.create(code, operation, context=lower.context if context is None else context,
            target=lower.target if target is None else target, severity=lower.severity,
            diagnostics=lower.diagnostics, causes=(direct, *deeper), omitted_diagnostics=lower.omitted_diagnostics,
            omitted_causes=lower.omitted_causes + len(lower.causes) - len(deeper), omitted_targets=lower.omitted_targets)

    def aggregate(self, collections: tuple[RuntimeErrorCollection, ...]) -> RuntimeErrorCollection:
        if not _typed_tuple(collections, RuntimeErrorCollection) or len(collections) > 128:
            raise TypeError('Aggregation uses finite ordered source collections, preserving every duplicate occurrence.')
        items, omitted = [], sum(c.omitted_errors for c in collections)
        for collection in collections:
            available = self._policy.maximum_errors - len(items)
            items.extend(collection.errors[:available])
            omitted += max(0, len(collection.errors) - available)
        return RuntimeErrorCollection(tuple(items), omitted)

    def map_result(self, result, operation: RuntimeErrorOperation, *, context: RuntimeErrorContext | None = None, include_not_found: bool = False) -> RuntimeErrorResultAssociation:
        allowed = {
            RuntimeArtifactLoadResult: (RuntimeErrorOperation.ARTIFACT_LOAD,),
            RuntimeModelRegistrationResult: (RuntimeErrorOperation.MODEL_REGISTER,),
            RuntimeModelLookupResult: (RuntimeErrorOperation.MODEL_LOOKUP, RuntimeErrorOperation.MODEL_INSPECT_NAME),
            RuntimeModelMembershipResult: (RuntimeErrorOperation.MODEL_MEMBERSHIP,),
            RuntimeModelVersionInspectionResult: (RuntimeErrorOperation.MODEL_ENUMERATE_VERSIONS,),
            RuntimeModelRegistrySnapshotResult: (RuntimeErrorOperation.MODEL_SNAPSHOT,),
            RuntimeInstanceOperationResult: (RuntimeErrorOperation.INSTANCE_CREATE, RuntimeErrorOperation.INSTANCE_UPDATE),
            RuntimeInstanceInspectionResult: (RuntimeErrorOperation.INSTANCE_INSPECT,),
            RuntimeValidationResult: (RuntimeErrorOperation.INSTANCE_VALIDATE,),
            ExecutionContextCreationResult: (RuntimeErrorOperation.CONTEXT_CREATE, RuntimeErrorOperation.CONTEXT_DERIVE),
        }
        if type(result) not in allowed or type(operation) is not RuntimeErrorOperation or operation not in allowed[type(result)] or type(include_not_found) is not bool or context is not None and type(context) is not RuntimeErrorContext:
            raise TypeError('Map only existing operation-specific results with explicit compatible operation/context.')
        status, originals = result.status, result.diagnostics
        success = status in (RuntimeArtifactLoadStatus.SUCCEEDED, RuntimeModelLookupStatus.FOUND,
            RuntimeInstanceInspectionStatus.FOUND, RuntimeInstanceInspectionStatus.MISSING, RuntimeValidationStatus.VALID)
        routine = status in (RuntimeModelLookupStatus.NOT_FOUND, RuntimeModelLookupStatus.AMBIGUOUS)
        project_routine = status is RuntimeModelLookupStatus.NOT_FOUND and include_not_found
        related = tuple(RuntimeErrorDiagnosticAssociation(d, i) for i, d in enumerate(originals[:self._policy.maximum_diagnostics]))
        error_items, omitted_errors = [], 0
        for i, d in enumerate(originals):
            if success or routine and not project_routine or d.severity is not RuntimeLoadSeverity.ERROR and not project_routine:
                continue
            if len(error_items) >= self._policy.maximum_errors:
                omitted_errors += 1
                continue
            if type(d) is RuntimeInstanceDiagnostic:
                actual_operation = {RuntimeInstanceOperation.CREATE: RuntimeErrorOperation.INSTANCE_CREATE,
                    RuntimeInstanceOperation.UPDATE: RuntimeErrorOperation.INSTANCE_UPDATE,
                    RuntimeInstanceOperation.INSPECT: RuntimeErrorOperation.INSTANCE_INSPECT}[d.operation]
                if actual_operation is not operation:
                    raise ValueError('Explicit error operation cannot contradict original instance diagnostic.')
            if self._source_operation(d, operation) is not operation:
                raise ValueError('Explicit operation cannot contradict original registry diagnostic.')
            error_items.append(self._diagnostic_error(d, operation, i, context))
        if not success and not routine and not error_items and omitted_errors == 0:
            # Cause UNKNOWN is honest lack-of-detail evidence, not a new diagnosis.
            error_items.append(self.create(RuntimeErrorCode('RUN-503'), operation, context=context))
        # RUN-03 actually retained the authoritative RUN-04 report. Preserve the
        # known lower report as RELATED evidence, not guessed one-field causality.
        if type(result) is RuntimeInstanceOperationResult and not success and result.validation_result is not None and error_items:
            lower = self.map_result(result.validation_result, RuntimeErrorOperation.INSTANCE_VALIDATE)
            first = error_items[0]
            extra = tuple(RuntimeErrorCause(RuntimeErrorCauseKind.RELATED_DIAGNOSTIC, e.code, e.category,
                e.operation, e.context, e.target, e.diagnostics[0] if e.diagnostics else None) for e in lower.errors.errors[:self._policy.maximum_causes])
            error_items[0] = self.create(first.code, first.operation, context=first.context, target=first.target,
                severity=first.severity, diagnostics=first.diagnostics, causes=first.causes + extra,
                omitted_diagnostics=first.omitted_diagnostics + lower.omitted_diagnostics, omitted_causes=first.omitted_causes + lower.errors.omitted_errors + max(0, len(lower.errors.errors) - len(extra)), omitted_targets=first.omitted_targets)
        return RuntimeErrorResultAssociation(operation, status, RuntimeErrorCollection(tuple(error_items), omitted_errors),
            related, max(0, len(originals) - len(related)), result.complete if type(result) is RuntimeValidationResult else None)

    def map_expected(self, exception: RuntimeArtifactLoadError | RuntimeInstanceError, operation: RuntimeErrorOperation, *, context: RuntimeErrorContext | None = None) -> RuntimeErrorResultAssociation:
        if type(exception) is RuntimeInstanceError and operation in (RuntimeErrorOperation.INSTANCE_CREATE, RuntimeErrorOperation.INSTANCE_UPDATE):
            result = RuntimeInstanceOperationResult(exception.status, diagnostics=exception.diagnostics, validation_result=exception.validation_result)
        elif type(exception) is RuntimeArtifactLoadError and operation in (RuntimeErrorOperation.ARTIFACT_LOAD, RuntimeErrorOperation.MODEL_REGISTER, RuntimeErrorOperation.MODEL_SNAPSHOT):
            result_type = {RuntimeErrorOperation.ARTIFACT_LOAD: RuntimeArtifactLoadResult,
                RuntimeErrorOperation.MODEL_REGISTER: RuntimeModelRegistrationResult,
                RuntimeErrorOperation.MODEL_SNAPSHOT: RuntimeModelRegistrySnapshotResult}[operation]
            result = result_type(exception.status, diagnostics=exception.diagnostics)
        else:
            raise TypeError('Expected exception mapping requires compatible existing narrow runtime exception/operation.')
        return self.map_result(result, operation, context=context)

    def from_unexpected(self, exception: BaseException, operation: RuntimeErrorOperation, *, context: RuntimeErrorContext | None = None) -> RuntimeErrorDetail:
        """Explicit outer boundary only; never wrap a domain method in broad catch.

        No exception object/type/message/traceback survives into the value; caller
        retains standard approved logging/rethrow policy outside this transform.
        """
        if not isinstance(exception, BaseException):
            raise TypeError('Unexpected boundary needs an actual exception, not an arbitrary client claim.')
        if not isinstance(exception, Exception) or isinstance(exception, (FutureCancelledError, BaseExceptionGroup)):
            raise exception  # preserve cancellation/process termination signals
        if isinstance(exception, (RuntimeArtifactLoadError, RuntimeInstanceError)):
            raise TypeError('Expected runtime rejection must use its diagnostic-preserving adapter.')
        code = RuntimeErrorCode('RUN-502' if isinstance(exception, OSError) else 'RUN-501')
        return self.create(code, operation, context=context)


@dataclass(frozen=True, slots=True)
class RuntimeErrorPresentationPolicy:
    """Trusted server presentation choice, not client permission or a tenant policy."""
    exposed_codes: tuple[RuntimeErrorCode, ...] = ()
    maximum_items: int = 1
    correlation_identity: ExecutionCorrelationId | None = None

    def __post_init__(self) -> None:
        if not _typed_tuple(self.exposed_codes, RuntimeErrorCode) or len(self.exposed_codes) > 256 or len(set(self.exposed_codes)) != len(self.exposed_codes) or type(self.maximum_items) is not int or not 1 <= self.maximum_items <= 1024 or self.correlation_identity is not None and type(self.correlation_identity) is not ExecutionCorrelationId:
            raise TypeError('Presentation allowlist/size/correlation are explicit immutable owner choices.')


@dataclass(frozen=True, slots=True)
class RuntimeErrorPublicItem:
    code: RuntimeErrorCode
    category: RuntimeErrorCategory
    safe_message: str
    correlation_identity: ExecutionCorrelationId | None = None

    def __post_init__(self) -> None:
        if type(self.code) is not RuntimeErrorCode or type(self.category) is not RuntimeErrorCategory or self.code.value != 'RUN-006' and self.category is not _RUNTIME_ERROR_CATEGORIES[self.code.value] or type(self.safe_message) is not str or self.safe_message != _runtime_safe_error_message(self.code, self.category) or self.correlation_identity is not None and type(self.correlation_identity) is not ExecutionCorrelationId:
            raise TypeError('Public view carries only controlled code/category/message and explicitly approved correlation.')


@dataclass(frozen=True, slots=True)
class RuntimeErrorPublicView:
    items: tuple[RuntimeErrorPublicItem, ...]
    limited: bool

    def __post_init__(self) -> None:
        if not _typed_tuple(self.items, RuntimeErrorPublicItem) or len(self.items) > 1024 or type(self.limited) is not bool:
            raise TypeError('Public projection is immutable bounded presentation, not authoritative failure evidence.')


def present_runtime_errors(collection: RuntimeErrorCollection, policy: RuntimeErrorPresentationPolicy | None = None) -> RuntimeErrorPublicView:
    if type(collection) is not RuntimeErrorCollection or policy is not None and type(policy) is not RuntimeErrorPresentationPolicy:
        raise TypeError('Projection accepts only actual internal collection and trusted server presentation policy.')
    config = RuntimeErrorPresentationPolicy() if policy is None else policy
    items = []
    for error in collection.errors[:config.maximum_items]:
        disclose = error.code in config.exposed_codes
        code = error.code if disclose else RuntimeErrorCode('RUN-505')
        category = error.category if disclose else RuntimeErrorCategory.UNKNOWN
        correlation = config.correlation_identity if config.correlation_identity == error.context.correlation_identity else None
        items.append(RuntimeErrorPublicItem(code, category, _runtime_safe_error_message(code, category), correlation))
    return RuntimeErrorPublicView(tuple(items), not collection.detail_complete or len(collection.errors) > len(items)
        or any(e.diagnostics or e.causes or e.target != RuntimeErrorTarget() or e.code not in config.exposed_codes for e in collection.errors))


__all__ += ['RuntimeErrorCategory', 'RuntimeErrorOperation', 'RuntimeErrorCode', 'RuntimeErrorContext',
    'RuntimeErrorTarget', 'RuntimeErrorDiagnosticAssociation', 'RuntimeErrorCauseKind', 'RuntimeErrorCause',
    'RuntimeErrorDetail', 'RuntimeErrorCollection', 'RuntimeErrorResultAssociation', 'RuntimeErrorPolicy',
    'RuntimeErrorFactory', 'RuntimeErrorPresentationPolicy', 'RuntimeErrorPublicItem',
    'RuntimeErrorPublicView', 'present_runtime_errors']
