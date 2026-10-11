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

from semantic_kernel.public import (SemanticContextRef, SemanticElementId,
    SemanticVersion, ElementVersionRef, ElementRef, PrimitiveTypes)
from model_core.public import (FieldId, FieldName, FieldDefinition, FieldConstraintSet,
    FieldPresence, FieldNullability, PrimitiveTypeRef, SemanticTypeRef,
    ConstraintKind, ConstraintKinds, MinimumConstraint, MaximumConstraint,
    MinLengthConstraint, MaxLengthConstraint, PatternConstraint, PrecisionConstraint,
    ScaleConstraint, NumericConstraintValue, primitive_constraint_kinds)
from compiled_contracts.public import RuntimeCapabilityId
from runtime_core.public import (RuntimeArtifactLoadStatus, RuntimeLoadSeverity,
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
    def __init__(self, diagnostics: tuple[RuntimeInstanceDiagnostic, ...], status: RuntimeArtifactLoadStatus = RuntimeArtifactLoadStatus.FAILED):
        if not _typed_tuple(diagnostics, RuntimeInstanceDiagnostic) or not diagnostics or status not in (RuntimeArtifactLoadStatus.FAILED, RuntimeArtifactLoadStatus.INCOMPLETE):
            raise TypeError('Expected instance rejection has actual diagnostics and non-success status.')
        self.diagnostics, self.status = diagnostics, status
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

    def __post_init__(self) -> None:
        if type(self.status) is not RuntimeArtifactLoadStatus or not _typed_tuple(self.diagnostics, RuntimeInstanceDiagnostic):
            raise TypeError('Operation result uses existing runtime status and typed diagnostics.')
        if self.status is RuntimeArtifactLoadStatus.SUCCEEDED:
            if type(self.state) is not RuntimeInstanceState or any(d.severity is RuntimeLoadSeverity.ERROR for d in self.diagnostics):
                raise ValueError('Success requires a complete canonical instance and no errors.')
        elif self.state is not None or not self.diagnostics:
            raise ValueError('Failure/incomplete returns diagnostics without a partial state.')

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


class DefaultSemanticInstanceRuntime:
    """Pure immutable transformation service with no stored instance membership.

    Composition belongs to the application zone: it may reuse model FieldId and
    constraint contracts without adding a forbidden model edge to runtime-core.
    """
    __slots__ = ('_binding', '_registry', '_authorizer', '_contract', '_schemas',
                 '_constraints', '_capabilities', '_policy')

    def __init__(self, scopes: tuple[RuntimeModelRegistryScope, ...], registry: RuntimeModelRegistry,
                 *, authorizer: RuntimeInstanceAuthorizer | None = None,
                 contract_support: RuntimeSemanticInstanceContractSupport | None = None,
                 definition_support: tuple[RuntimeInstanceDefinitionSupport, ...] = (),
                 constraint_support: RuntimeInstanceConstraintSupport | None = None,
                 supported_capabilities: tuple[RuntimeCapabilityId, ...] = (),
                 policy: RuntimeInstancePolicy | None = None):
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
        support = next((s for s in self._schemas if s.decoder_registration is definition.loaded_artifact.decoder_registration and s.definition_type is type(definition.representation) and s.definition_kind == definition.definition_kind), None)
        if support is None or not support.instance_schema_complete:
            self._reject(RuntimeInstanceFailure.VALIDATION_UNAVAILABLE, 'Loaded definition has no explicitly approved complete instance-schema projection.', operation, request, incomplete=True)
        schema = support.projector.project(definition, self._policy.maximum_fields)
        if type(schema) is not RuntimeInstanceDefinitionSchema or schema.definition is not definition:
            self._reject(RuntimeInstanceFailure.INTEGRITY_FAILURE, 'Schema projection does not retain the actual selected runtime definition.', operation, request)
        if len(schema.fields) > self._policy.maximum_fields:
            self._reject(RuntimeInstanceFailure.RESOURCE_LIMIT_EXCEEDED, 'Declared field inventory exceeds the service budget.', operation, request)
        if any(c not in self._capabilities for c in schema.required_capabilities):
            self._reject(RuntimeInstanceFailure.VALIDATION_UNAVAILABLE, 'An explicit required instance-schema capability is unavailable.', operation, request, incomplete=True)
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
                self._reject(RuntimeInstanceFailure.RESOURCE_LIMIT_EXCEEDED, 'Original schema association traversal exceeds the load budget.', operation, request)
            if type(node) is tuple:
                stack.extend(node)
            elif is_dataclass(node):
                stack.extend(getattr(node, f.name) for f in fields(type(node)))
        if not found:
            self._reject(RuntimeInstanceFailure.INTEGRITY_FAILURE, 'Projected field order is not the original encoded field tuple.', operation, request)
        ids = tuple(f.id for f in schema.fields)
        if not _typed_tuple(ids, FieldId) or len(set(ids)) != len(ids):
            self._reject(RuntimeInstanceFailure.INTEGRITY_FAILURE, 'Declared fields have invalid or duplicate stable identities.', operation, request)
        for member in schema.fields:
            if type(member.constraints) is not FieldConstraintSet or type(member.type) not in (PrimitiveTypeRef, SemanticTypeRef) or type(member.constraints.presence) is not FieldPresence or type(member.constraints.nullability) is not FieldNullability:
                self._reject(RuntimeInstanceFailure.INTEGRITY_FAILURE, 'Declared field representation is not the supported immutable model contract.', operation, request, field_id=member.id)
            for constraint in member.constraints.value_constraints:
                if type(constraint) not in (MinimumConstraint, MaximumConstraint, MinLengthConstraint, MaxLengthConstraint, PatternConstraint, PrecisionConstraint, ScaleConstraint):
                    self._reject(RuntimeInstanceFailure.VALIDATION_UNAVAILABLE, 'Required field constraint has no supported runtime evaluator.', operation, request, field_id=member.id, incomplete=True)
                if type(member.type) is SemanticTypeRef or constraint.kind not in primitive_constraint_kinds(member.type.primitive):
                    self._reject(RuntimeInstanceFailure.INTEGRITY_FAILURE, 'Registered constraint is incompatible with the declared primitive/reference kind.', operation, request, field_id=member.id, constraint=constraint.kind)
                if type(constraint) in (MinimumConstraint, MaximumConstraint) and (type(constraint.value) is not NumericConstraintValue or member.type.primitive == PrimitiveTypes.INTEGER and '.' in constraint.value.value):
                    self._reject(RuntimeInstanceFailure.INTEGRITY_FAILURE, 'Numeric bound does not preserve TYPE-04/06 exact integral applicability.', operation, request, field_id=member.id, constraint=constraint.kind)
                if type(constraint) in (PatternConstraint, PrecisionConstraint, ScaleConstraint) and (self._constraints is None or constraint.kind not in self._constraints.kinds):
                    self._reject(RuntimeInstanceFailure.VALIDATION_UNAVAILABLE, 'Pattern dialect or decimal precision/scale execution requires an explicit approved evaluator.', operation, request, field_id=member.id, constraint=constraint.kind, incomplete=True)
        return schema

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

    def _value(self, member: FieldDefinition, value: SemanticFieldValue, definition: RuntimeModelDefinition, request: object, operation: RuntimeInstanceOperation, identity: RuntimeInstanceIdentityAssociation) -> RuntimeInstanceValueKind:
        projected = self._contract.adapter.inspect_value(value)
        if projected is None:
            self._reject(RuntimeInstanceFailure.UNSUPPORTED_FIELD_VALUE, 'Canonical value has no approved primitive/instance-reference projection.', operation, request, identity=identity, field_id=member.id, incomplete=type(member.type) is SemanticTypeRef)
        expected = {self._contract.missing_type: RuntimeInstanceValueKind.MISSING, self._contract.null_type: RuntimeInstanceValueKind.NULL, self._contract.value_type: RuntimeInstanceValueKind.VALUE}[type(value)]
        if type(projected) is not RuntimeInstanceValueView or projected.kind is not expected or not _immutable(projected.primitive, (), self._policy.maximum_value_nodes, self._policy.maximum_value_depth, self._policy.maximum_scalar_units):
            self._reject(RuntimeInstanceFailure.INTEGRITY_FAILURE, 'Canonical value projection violates approved variant or immutable primitive representation.', operation, request, identity=identity, field_id=member.id)
        if projected.kind is RuntimeInstanceValueKind.MISSING:
            if member.constraints.presence is FieldPresence.REQUIRED:
                self._reject(RuntimeInstanceFailure.REQUIRED_FIELD_MISSING, 'Required field must be present independently of nullability.', operation, request, identity=identity, field_id=member.id)
            return projected.kind
        if projected.kind is RuntimeInstanceValueKind.NULL:
            if member.constraints.nullability is FieldNullability.NON_NULL:
                self._reject(RuntimeInstanceFailure.NULL_NOT_ALLOWED, 'Explicit Null is forbidden by field nullability.', operation, request, identity=identity, field_id=member.id)
            return projected.kind
        if type(member.type) is SemanticTypeRef:
            self._reject(RuntimeInstanceFailure.UNSUPPORTED_FIELD_VALUE, 'Canonical semantic instance-reference values are not established; no recursion or relationship inference.', operation, request, identity=identity, field_id=member.id, incomplete=True)
        primitive_types = ((PrimitiveTypes.STRING, str), (PrimitiveTypes.BOOLEAN, bool), (PrimitiveTypes.INTEGER, int), (PrimitiveTypes.DECIMAL, Decimal), (PrimitiveTypes.DATE, date), (PrimitiveTypes.DATETIME, datetime), (PrimitiveTypes.UUID, UUID))
        actual_type = next((t for p, t in primitive_types if p == member.type.primitive), None)
        if actual_type is None:
            self._reject(RuntimeInstanceFailure.UNSUPPORTED_FIELD_VALUE, 'Declared primitive representation is unsupported.', operation, request, identity=identity, field_id=member.id, incomplete=True)
        primitive = projected.primitive
        if type(primitive) is not actual_type:
            self._reject(RuntimeInstanceFailure.PRIMITIVE_TYPE_MISMATCH, 'Canonical Value primitive does not match the exact declared primitive; no coercion.', operation, request, identity=identity, field_id=member.id)
        for constraint in member.constraints.value_constraints:
            t = type(constraint)
            violated = False
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
                result = self._constraints.evaluator.evaluate(invocation)
                if type(result) is not RuntimeInstanceConstraintResult or result.request is not invocation:
                    self._reject(RuntimeInstanceFailure.INTEGRITY_FAILURE, 'Constraint evaluator result does not match the exact original invocation.', operation, request, identity=identity, field_id=member.id, constraint=constraint.kind)
                if result.decision is RuntimeInstanceConstraintDecision.UNAVAILABLE:
                    self._reject(RuntimeInstanceFailure.VALIDATION_UNAVAILABLE, 'Approved evaluator cannot judge this required constraint.', operation, request, identity=identity, field_id=member.id, constraint=constraint.kind, incomplete=True)
                violated = result.decision is RuntimeInstanceConstraintDecision.VIOLATED
            if violated:
                self._reject(RuntimeInstanceFailure.CONSTRAINT_VIOLATION, 'Value violates an explicit supported runtime field constraint.', operation, request, identity=identity, field_id=member.id, constraint=constraint.kind)
        return projected.kind

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
            self._value(member, value, schema.definition, request, operation, identity)
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
        return self._canonical_view(state.instance, schema, request, operation)

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
            return RuntimeInstanceOperationResult(RuntimeArtifactLoadStatus.SUCCEEDED, state)
        except RuntimeInstanceError as error:
            return RuntimeInstanceOperationResult(error.status, diagnostics=tuple(replace(d, instance_identity=d.instance_identity or identity) for d in error.diagnostics))

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
            return RuntimeInstanceOperationResult(RuntimeArtifactLoadStatus.SUCCEEDED, state)
        except RuntimeInstanceError as error:
            return RuntimeInstanceOperationResult(error.status, diagnostics=tuple(replace(d, instance_identity=d.instance_identity or identity) for d in error.diagnostics))

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


__all__ = [name for name in globals() if name.startswith(('RuntimeInstance', 'RuntimeSemanticInstance', 'SemanticInstance'))] + ['MODULE_NAME', 'SemanticFieldValue', 'RuntimePrimitiveValue', 'DefaultSemanticInstanceRuntime']
