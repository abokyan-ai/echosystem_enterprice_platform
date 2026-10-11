"""MOD-01 schema, MOD-05 canonicalization and MOD-06/07 resolution and MOD-08 validation.

Input is a decoded JSON-compatible abstract tree, never JSON/YAML source text.
Schema projection returns authoring snapshots; canonicalization is a separate
operation requiring typed resolution bindings. Namespace resolution is a
separate explicit-environment operation; reference requirements and complete
binding readiness are another boundary. Validation delegates to existing validators
without executing those transformations. No registry mutation, compiler,
runtime or parser dependency.
"""
from dataclasses import dataclass as _dataclass, field as _dataclass_field, is_dataclass as _is_dataclass
import re as _re
from enum import Enum as _Enum
from types import MappingProxyType as _MappingProxyType
from typing import Mapping as _Mapping, Protocol as _Protocol
from semantic_kernel.public import (
    SemanticElementId, SemanticElementIdError, SemanticContextRef,
    SemanticContextRefError, Namespace, NamespaceError, QualifiedName,
    QualifiedNameError, SemanticVersion, SemanticVersionError, PrimitiveType,
    PrimitiveTypeError, ElementRef, ElementVersionRef, SemanticElementKind,
    SemanticElementKinds,
)
from model_core.public import (
    FieldId, FieldIdError, FieldName, FieldNameError, FieldConstraintError,
    FieldPresence, FieldNullability, ConstraintKind, ConstraintKinds,
    FieldConstraintSet, MinLengthConstraint, MaxLengthConstraint,
    MinimumConstraint, MaximumConstraint, PatternConstraint, PrecisionConstraint,
    ScaleConstraint, TypeValidationSeverity, FieldDefinition, FieldDefinitionError,
    DataFacet, DataFacetError, PrimitiveTypeRef, SemanticTypeRef, TypeRefError,
    CanonicalModel, CanonicalDefinition, CanonicalModelFactory, CanonicalConstructionDiagnostic,
    create_type_data_definition,
    TypeLookup, TypeRegistryAmbiguityError, TypeValidator, TypeValidationContext,
    TypeValidationDiagnostic, TypeValidationResult, CanonicalModelConstructionResult,
)

MODULE_NAME = 'model-authoring'
AUTHORING_SCHEMA_VERSION = '1.0'  # Authoring format v0, not SemanticVersion.
__all__ = [
    'MODULE_NAME', 'AUTHORING_SCHEMA_VERSION', 'AuthoringModelDocument',
    'AuthoringTypeDeclaration', 'AuthoringDataFacetDeclaration',
    'AuthoringFieldDeclaration', 'AuthoringConstraintDeclaration',
    'AuthoringValueConstraintDeclaration', 'AuthoringTypeExpression',
    'AuthoringPrimitiveExpression', 'AuthoringNameExpression',
    'AuthoringIdentityExpression', 'AuthoringVersionExpression',
    'AuthoringSchemaValidator', 'AuthoringSchemaValidationResult',
    'AuthoringSchemaDiagnostic', 'AuthoringSchemaPath',
]


def _ordered(values: tuple, expected: type) -> tuple:
    if type(values) not in (list, tuple) or any(type(value) is not expected for value in values):
        raise TypeError('Authoring members require an ordered collection of canonical declaration snapshots.')
    return tuple(values)


@_dataclass(frozen=True, slots=True)
class AuthoringPrimitiveExpression:
    primitive: PrimitiveType

    def __post_init__(self):
        if type(self.primitive) is not PrimitiveType:
            raise TypeError('Primitive expression requires the existing Kernel primitive vocabulary.')

    @property
    def kind(self) -> str:
        return 'primitive'


@_dataclass(frozen=True, slots=True)
class AuthoringNameExpression:
    """Syntactically valid local/qualified name; target existence is unresolved."""
    name: str

    def __post_init__(self):
        if type(self.name) is not str:
            raise TypeError('Named expression requires exact authoring text.')
        if '.' in self.name:
            QualifiedName.parse(self.name)  # Syntax check only; no binding retained.
        else:
            FieldName.parse(self.name)  # Same established ASCII local-name grammar.

    @property
    def kind(self) -> str:
        return 'semantic-name'


@_dataclass(frozen=True, slots=True)
class AuthoringIdentityExpression:
    """Author supplied identity, not proof of target existence or a chosen version."""
    reference: ElementRef

    def __post_init__(self):
        if type(self.reference) is not ElementRef or type(self.reference.element_id) is not SemanticElementId:
            raise TypeError('Identity expression requires a canonical Kernel ElementRef.')

    @property
    def kind(self) -> str:
        return 'semantic-id'


@_dataclass(frozen=True, slots=True)
class AuthoringVersionExpression:
    """Exact authored coordinate; later stages must not discard its version pin."""
    reference: ElementVersionRef

    def __post_init__(self):
        if type(self.reference) is not ElementVersionRef or type(self.reference.element_id) is not SemanticElementId or type(self.reference.version) is not SemanticVersion:
            raise TypeError('Version expression requires a canonical Kernel ElementVersionRef.')

    @property
    def kind(self) -> str:
        return 'semantic-version'


AuthoringTypeExpression = AuthoringPrimitiveExpression | AuthoringNameExpression | AuthoringIdentityExpression | AuthoringVersionExpression
_EXPRESSION_TYPES = (AuthoringPrimitiveExpression, AuthoringNameExpression, AuthoringIdentityExpression, AuthoringVersionExpression)


@_dataclass(frozen=True, slots=True)
class AuthoringValueConstraintDeclaration:
    """Supported typed kind and original integer/text literal, not normalized text."""
    kind: ConstraintKind
    value: int | str

    def __post_init__(self):
        if type(self.kind) is not ConstraintKind or self.kind not in _CONSTRAINT_FACTORIES:
            raise TypeError('Only the seven established value constraint kinds are supported.')
        if type(self.value) not in (int, str):
            raise TypeError('Constraint authoring payload requires a plain integer or exact text.')
        _CONSTRAINT_FACTORIES[self.kind](self.value)  # Existing payload rules, no matrix.


@_dataclass(frozen=True, slots=True)
class AuthoringConstraintDeclaration:
    presence: FieldPresence
    nullability: FieldNullability
    values: tuple[AuthoringValueConstraintDeclaration, ...]

    def __post_init__(self):
        if type(self.presence) is not FieldPresence or type(self.nullability) is not FieldNullability:
            raise TypeError('Presence and nullability are separate explicit declarations.')
        values = _ordered(self.values, AuthoringValueConstraintDeclaration)
        # Reuse TYPE-04 consistency; keep original declaration/literal order.
        FieldConstraintSet(self.presence, self.nullability, tuple(_CONSTRAINT_FACTORIES[v.kind](v.value) for v in values))
        object.__setattr__(self, 'values', values)


@_dataclass(frozen=True, slots=True)
class AuthoringFieldDeclaration:
    id: str
    name: str
    type: AuthoringTypeExpression
    constraints: AuthoringConstraintDeclaration

    def __post_init__(self):
        if type(self.id) is not str or type(self.name) is not str:
            raise TypeError('Field ID and name require separate authoring text.')
        FieldId.parse(self.id)
        FieldName.parse(self.name)
        if type(self.type) not in _EXPRESSION_TYPES or type(self.constraints) is not AuthoringConstraintDeclaration:
            raise TypeError('Field requires explicit authoring type expression and constraints.')


@_dataclass(frozen=True, slots=True)
class AuthoringDataFacetDeclaration:
    fields: tuple[AuthoringFieldDeclaration, ...]

    def __post_init__(self):
        object.__setattr__(self, 'fields', _ordered(self.fields, AuthoringFieldDeclaration))

    @property
    def kind(self) -> str:
        return 'data'


@_dataclass(frozen=True, slots=True)
class AuthoringTypeDeclaration:
    """Root identity text plus facet declarations; no direct field ownership."""
    id: str
    name: str
    version: str
    facets: tuple[AuthoringDataFacetDeclaration, ...]

    def __post_init__(self):
        if any(type(value) is not str for value in (self.id, self.name, self.version)):
            raise TypeError('Definition identity/name/version require separate authoring text.')
        SemanticElementId.parse(self.id)
        FieldName.parse(self.name)
        SemanticVersion.parse(self.version)
        object.__setattr__(self, 'facets', _ordered(self.facets, AuthoringDataFacetDeclaration))

    @property
    def kind(self) -> str:
        return 'type'


@_dataclass(frozen=True, slots=True)
class AuthoringModelDocument:
    """Source container: format version and scope, never a SemanticElement.

    Declarations retain authored ID/version/name/literal text and ordering.
    Context is an explicit typed reference, not a namespace/tenant or lookup.
    Direct construction is representation, not a schema-validation certificate.
    """
    schema_version: str
    context: SemanticContextRef
    namespace: str
    definitions: tuple[AuthoringTypeDeclaration, ...]

    def __post_init__(self):
        if type(self.schema_version) is not str or type(self.namespace) is not str:
            raise TypeError('Schema version and namespace require explicit authoring text.')
        if type(self.context) is not SemanticContextRef or type(self.context.context_id) is not SemanticElementId:
            raise TypeError('Authoring document requires an explicit Kernel context reference.')
        Namespace.parse(self.namespace)
        object.__setattr__(self, 'definitions', _ordered(self.definitions, AuthoringTypeDeclaration))


@_dataclass(frozen=True, slots=True)
class AuthoringSchemaPath:
    """Provisional source-tree coordinate pending SK-11; indices are not identities."""
    segments: tuple[str | int, ...] = ()

    def __post_init__(self):
        if type(self.segments) not in (list, tuple) or any(type(s) not in (str, int) or type(s) is int and s < 0 for s in self.segments):
            raise TypeError('Schema path requires property text or non-negative array indices.')
        object.__setattr__(self, 'segments', tuple(self.segments))

    def __str__(self) -> str:
        result = '$'
        for segment in self.segments:
            result += '[' + str(segment) + ']' if type(segment) is int else '[' + repr(segment) + ']'
        return result


@_dataclass(frozen=True, slots=True)
class AuthoringSchemaDiagnostic:
    """Narrow provisional MOD diagnostic, not a replacement for absent SK-11."""
    code: str
    message: str
    path: AuthoringSchemaPath
    cause_code: str | None = None
    related_path: AuthoringSchemaPath | None = None

    def __post_init__(self):
        if type(self.code) is not str or self.code not in _SCHEMA_CODES or type(self.message) is not str or not self.message:
            raise TypeError('Expected a supported stable MOD schema diagnostic and message.')
        if type(self.path) is not AuthoringSchemaPath or self.related_path is not None and type(self.related_path) is not AuthoringSchemaPath:
            raise TypeError('Schema diagnostics require typed source-tree paths.')
        if self.cause_code is not None and type(self.cause_code) is not str:
            raise TypeError('Delegated diagnostic code must be text.')

    @property
    def severity(self) -> TypeValidationSeverity:
        return TypeValidationSeverity.ERROR


@_dataclass(frozen=True, slots=True)
class AuthoringSchemaValidationResult:
    document: AuthoringModelDocument | None
    diagnostics: tuple[AuthoringSchemaDiagnostic, ...]

    def __post_init__(self):
        if self.document is not None and type(self.document) is not AuthoringModelDocument:
            raise TypeError('Result document must be a canonical authoring snapshot or None.')
        diagnostics = _ordered(self.diagnostics, AuthoringSchemaDiagnostic)
        if (self.document is None) != bool(diagnostics):
            raise ValueError('A successful schema projection has a document and no error diagnostics.')
        object.__setattr__(self, 'diagnostics', diagnostics)

    @property
    def is_valid(self) -> bool:
        return self.document is not None


_SCHEMA_CODES = frozenset('MOD-SCHEMA-' + f'{n:03d}' for n in range(1, 15))
_CONSTRAINT_FACTORIES = _MappingProxyType({
    ConstraintKinds.MIN_LENGTH: MinLengthConstraint,
    ConstraintKinds.MAX_LENGTH: MaxLengthConstraint,
    ConstraintKinds.MINIMUM: MinimumConstraint,
    ConstraintKinds.MAXIMUM: MaximumConstraint,
    ConstraintKinds.PATTERN: PatternConstraint,
    ConstraintKinds.PRECISION: PrecisionConstraint,
    ConstraintKinds.SCALE: ScaleConstraint,
})
_EXPECTED_VALUE_ERRORS = (SemanticElementIdError, SemanticContextRefError, NamespaceError, QualifiedNameError, SemanticVersionError, PrimitiveTypeError, FieldIdError, FieldNameError, FieldConstraintError)


def _error(diagnostics: list, code: str, message: str, path: tuple, cause_code: str | None = None, previous: tuple | None = None):
    diagnostics.append(AuthoringSchemaDiagnostic(code, message, AuthoringSchemaPath(path), cause_code, None if previous is None else AuthoringSchemaPath(previous)))


def _object(value: object, required: tuple[str, ...], allowed: tuple[str, ...], path: tuple, diagnostics: list) -> dict | None:
    if type(value) is not dict:
        _error(diagnostics, 'MOD-SCHEMA-001', 'Expected a decoded authoring object.', path)
        return None
    if any(type(key) is not str for key in value):
        _error(diagnostics, 'MOD-SCHEMA-001', 'Authoring object keys must be plain strings.', path)
    for name in required:
        if name not in value:
            _error(diagnostics, 'MOD-SCHEMA-002', 'Required authoring property is missing.', (*path, name))
    for name in sorted(key for key in value if type(key) is str and key not in allowed):
        _error(diagnostics, 'MOD-SCHEMA-003', 'Unsupported authoring property; extensions require a future explicit schema contract.', (*path, name))
    return value


def _collection(value: object, path: tuple, diagnostics: list) -> list | None:
    if type(value) is not list:
        _error(diagnostics, 'MOD-SCHEMA-001', 'Expected an ordered decoded authoring array.', path)
        return None
    return value


def _scalar(obj: dict, name: str, factory, code: str, path: tuple, diagnostics: list):
    if name not in obj:
        return None  # Missing property already diagnosed by _object.
    value = obj[name]
    if type(value) is not str:
        _error(diagnostics, code, 'Expected explicit authoring text without coercion.', (*path, name))
        return None
    try:
        return factory(value)
    except _EXPECTED_VALUE_ERRORS as error:
        _error(diagnostics, code, 'Invalid authoring value syntax.', (*path, name), error.code)
        return None


def _expression(value: object, path: tuple, diagnostics: list) -> AuthoringTypeExpression | None:
    obj = _object(value, ('kind',), ('kind', 'primitive', 'name', 'id', 'version'), path, diagnostics)
    if obj is None or 'kind' not in obj:
        return None
    kind = obj['kind']
    if type(kind) is not str or kind not in ('primitive', 'semantic-name', 'semantic-id', 'semantic-version'):
        _error(diagnostics, 'MOD-SCHEMA-008', 'Unsupported or ambiguous type-expression discriminator.', (*path, 'kind'))
        return None
    keys = {'primitive': ('kind', 'primitive'), 'semantic-name': ('kind', 'name'), 'semantic-id': ('kind', 'id'), 'semantic-version': ('kind', 'id', 'version')}[kind]
    # Broad initial shape detects completely unknown properties; this pass checks
    # only supported keys belonging to a different variant, without duplicate errors.
    for key in keys[1:]:
        if key not in obj:
            _error(diagnostics, 'MOD-SCHEMA-002', 'Required type-expression property is missing.', (*path, key))
    for key in sorted(set(obj).intersection({'primitive', 'name', 'id', 'version'}) - set(keys)):
        _error(diagnostics, 'MOD-SCHEMA-003', 'Property belongs to another type-expression variant.', (*path, key))
    if kind == 'primitive':
        primitive = _scalar(obj, 'primitive', PrimitiveType.parse, 'MOD-SCHEMA-009', path, diagnostics)
        return None if primitive is None else AuthoringPrimitiveExpression(primitive)
    if kind == 'semantic-name':
        name = _scalar(obj, 'name', AuthoringNameExpression, 'MOD-SCHEMA-010', path, diagnostics)
        return name
    identity = _scalar(obj, 'id', SemanticElementId.parse, 'MOD-SCHEMA-010', path, diagnostics)
    if kind == 'semantic-id':
        return None if identity is None else AuthoringIdentityExpression(ElementRef(identity))
    version = _scalar(obj, 'version', SemanticVersion.parse, 'MOD-SCHEMA-010', path, diagnostics)
    return None if identity is None or version is None else AuthoringVersionExpression(ElementVersionRef(identity, version))


def _constraints(value: object, path: tuple, diagnostics: list) -> AuthoringConstraintDeclaration | None:
    start = len(diagnostics)
    obj = _object(value, ('presence', 'nullability', 'values'), ('presence', 'nullability', 'values'), path, diagnostics)
    if obj is None:
        return None
    presence = None
    nullability = None
    for name, factory in (('presence', FieldPresence), ('nullability', FieldNullability)):
        if name not in obj:
            continue
        try:
            if type(obj[name]) is not str:
                raise ValueError('Explicit token required')
            parsed = factory(obj[name])
            if name == 'presence':
                presence = parsed
            else:
                nullability = parsed
        except ValueError:
            _error(diagnostics, 'MOD-SCHEMA-011', 'Unsupported explicit presence/nullability token.', (*path, name))
    entries = _collection(obj['values'], (*path, 'values'), diagnostics) if 'values' in obj else None
    authored = []
    typed = []
    kinds = {}
    for index, raw in enumerate(entries or []):
        location = (*path, 'values', index)
        item_start = len(diagnostics)
        item = _object(raw, ('kind', 'value'), ('kind', 'value'), location, diagnostics)
        if item is None:
            continue
        kind = _scalar(item, 'kind', ConstraintKind.parse, 'MOD-SCHEMA-011', location, diagnostics)
        if kind is None:
            continue
        if kind not in _CONSTRAINT_FACTORIES:
            _error(diagnostics, 'MOD-SCHEMA-011', 'Unsupported value constraint kind.', (*location, 'kind'))
            continue
        if kind in kinds:
            _error(diagnostics, 'MOD-SCHEMA-011', 'Duplicate value constraint kind.', (*location, 'kind'), 'TYPE-CONSTRAINT-008', kinds[kind])
        else:
            kinds[kind] = (*location, 'kind')
        if 'value' not in item:
            continue
        literal = item['value']
        integer_kind = kind in (ConstraintKinds.MIN_LENGTH, ConstraintKinds.MAX_LENGTH, ConstraintKinds.PRECISION, ConstraintKinds.SCALE)
        if type(literal) is not (int if integer_kind else str):
            _error(diagnostics, 'MOD-SCHEMA-011', 'Constraint requires a plain integer or exact text according to its kind; no numeric coercion.', (*location, 'value'))
            continue
        try:
            parsed = _CONSTRAINT_FACTORIES[kind](literal)
        except FieldConstraintError as error:
            _error(diagnostics, 'MOD-SCHEMA-011', 'Invalid constraint literal.', (*location, 'value'), error.code)
            continue
        if len(diagnostics) == item_start:
            typed.append(parsed)
            authored.append(AuthoringValueConstraintDeclaration(kind, literal))
    if len(diagnostics) == start and presence is not None and nullability is not None:
        try:
            FieldConstraintSet(presence, nullability, typed)
        except FieldConstraintError as error:
            _error(diagnostics, 'MOD-SCHEMA-011', 'Locally inconsistent value constraints.', path, error.code)
            return None
        return AuthoringConstraintDeclaration(presence, nullability, authored)
    return None


def _field(value: object, path: tuple, diagnostics: list) -> AuthoringFieldDeclaration | None:
    start = len(diagnostics)
    obj = _object(value, ('id', 'name', 'type', 'constraints'), ('id', 'name', 'type', 'constraints'), path, diagnostics)
    if obj is None:
        return None
    identity = _scalar(obj, 'id', FieldId.parse, 'MOD-SCHEMA-007', path, diagnostics)
    name = _scalar(obj, 'name', FieldName.parse, 'MOD-SCHEMA-007', path, diagnostics)
    expression = _expression(obj['type'], (*path, 'type'), diagnostics) if 'type' in obj else None
    constraints = _constraints(obj['constraints'], (*path, 'constraints'), diagnostics) if 'constraints' in obj else None
    if len(diagnostics) == start and identity is not None and name is not None and expression is not None and constraints is not None:
        return AuthoringFieldDeclaration(obj['id'], obj['name'], expression, constraints)
    return None


def _duplicates(obj: dict, path: tuple, diagnostics: list, ids: dict, names: dict, folded: dict):
    # Independent of other field errors: valid coordinates still participate in
    # duplicate detection. Reuse value parsing, never position-derived identity.
    id = None
    name = None
    try:
        if type(obj.get('id')) is str:
            id = FieldId.parse(obj['id'])
    except FieldIdError:
        pass  # The field reader owns the original syntax diagnostic.
    try:
        if type(obj.get('name')) is str:
            name = FieldName.parse(obj['name'])
    except FieldNameError:
        pass
    if id is not None:
        if id in ids:
            _error(diagnostics, 'MOD-SCHEMA-013', 'Duplicate FieldId in this DataFacet.', (*path, 'id'), previous=ids[id])
        else:
            ids[id] = (*path, 'id')
    if name is not None:
        if name in names:
            _error(diagnostics, 'MOD-SCHEMA-013', 'Duplicate FieldName in this DataFacet.', (*path, 'name'), previous=names[name])
        else:
            names[name] = (*path, 'name')
            key = str(name).lower()  # Existing ASCII local-name portability rule.
            if key in folded:
                _error(diagnostics, 'MOD-SCHEMA-013', 'Field-name case portability collision.', (*path, 'name'), previous=folded[key])
            else:
                folded[key] = (*path, 'name')


def _facets(value: object, path: tuple, diagnostics: list) -> tuple[AuthoringDataFacetDeclaration, ...]:
    entries = _collection(value, path, diagnostics)
    result = []
    first_data = None
    for index, raw in enumerate(entries or []):
        location = (*path, index)
        start = len(diagnostics)
        obj = _object(raw, ('kind', 'fields'), ('kind', 'fields'), location, diagnostics)
        if obj is None:
            continue
        if 'kind' not in obj:
            continue
        if type(obj['kind']) is not str or obj['kind'] != 'data':
            _error(diagnostics, 'MOD-SCHEMA-006', 'Unsupported facet kind in format v0.', (*location, 'kind'))
            continue
        if first_data is not None:
            _error(diagnostics, 'MOD-SCHEMA-014', 'Only one data facet may be declared on a type.', (*location, 'kind'), previous=first_data)
        else:
            first_data = (*location, 'kind')
        fields = _collection(obj['fields'], (*location, 'fields'), diagnostics) if 'fields' in obj else None
        members = []
        ids, names, folded = {}, {}, {}
        for ordinal, raw_field in enumerate(fields or []):
            field_path = (*location, 'fields', ordinal)
            field = _field(raw_field, field_path, diagnostics)
            if type(raw_field) is dict:
                _duplicates(raw_field, field_path, diagnostics, ids, names, folded)
            if field is not None:
                members.append(field)
        if len(diagnostics) == start:
            result.append(AuthoringDataFacetDeclaration(members))
    return tuple(result)


def _definition(value: object, path: tuple, diagnostics: list) -> AuthoringTypeDeclaration | None:
    start = len(diagnostics)
    obj = _object(value, ('kind', 'id', 'name', 'version'), ('kind', 'id', 'name', 'version', 'facets'), path, diagnostics)
    if obj is None:
        return None
    if 'kind' not in obj:
        return None
    if type(obj['kind']) is not str or obj['kind'] != 'type':
        _error(diagnostics, 'MOD-SCHEMA-005', 'Unsupported definition kind in format v0.', (*path, 'kind'))
        return None
    id = _scalar(obj, 'id', SemanticElementId.parse, 'MOD-SCHEMA-007', path, diagnostics)
    name = _scalar(obj, 'name', FieldName.parse, 'MOD-SCHEMA-007', path, diagnostics)
    version = _scalar(obj, 'version', SemanticVersion.parse, 'MOD-SCHEMA-007', path, diagnostics)
    facets = _facets(obj['facets'], (*path, 'facets'), diagnostics) if 'facets' in obj else ()
    if len(diagnostics) == start and id is not None and name is not None and version is not None:
        return AuthoringTypeDeclaration(obj['id'], obj['name'], obj['version'], facets)
    return None


def _definition_duplicates(obj: dict, path: tuple, diagnostics: list, identities: dict, names: dict):
    if obj.get('kind') != 'type':
        return
    try:
        if type(obj.get('id')) is not str or type(obj.get('version')) is not str:
            return
        id = SemanticElementId.parse(obj['id'])
        version = SemanticVersion.parse(obj['version'])
    except (SemanticElementIdError, SemanticVersionError):
        return  # Original value errors already belong to the declaration reader.
    key = (id, version)
    if key in identities:
        _error(diagnostics, 'MOD-SCHEMA-012', 'Duplicate exact type declaration in this document.', (*path, 'id'), previous=identities[key])
    else:
        identities[key] = (*path, 'id')
    try:
        if type(obj.get('name')) is not str:
            return
        name = FieldName.parse(obj['name'])
    except FieldNameError:
        return
    if name in names and names[name][0] != id:
        _error(diagnostics, 'MOD-SCHEMA-012', 'Local type name is declared by different identities in this document scope.', (*path, 'name'), previous=names[name][1])
    elif name not in names:
        names[name] = (id, (*path, 'name'))


@_dataclass(frozen=True, slots=True)
class AuthoringSchemaValidator:
    """Stateless diagnostic-first projection of a decoded tree into schema v0.

    Expected malformed source produces diagnostics, never repair or identity
    generation. Direct declaration constructors enforce representation contracts,
    not complete schema validity. No source text parser or schema extension bag.
    """
    def validate(self, source: object) -> AuthoringSchemaValidationResult:
        diagnostics = []
        root = _object(source, ('schemaVersion', 'context', 'namespace', 'definitions'), ('schemaVersion', 'context', 'namespace', 'definitions'), (), diagnostics)
        if root is None:
            return AuthoringSchemaValidationResult(None, diagnostics)
        if 'schemaVersion' in root and (type(root['schemaVersion']) is not str or root['schemaVersion'] != AUTHORING_SCHEMA_VERSION):
            _error(diagnostics, 'MOD-SCHEMA-004', 'Unsupported authoring format version; only 1.0 is supported.', ('schemaVersion',))
        context = _scalar(root, 'context', SemanticContextRef.parse, 'MOD-SCHEMA-007', (), diagnostics)
        namespace = _scalar(root, 'namespace', Namespace.parse, 'MOD-SCHEMA-007', (), diagnostics)
        definitions = _collection(root['definitions'], ('definitions',), diagnostics) if 'definitions' in root else None
        declarations = []
        identities, names = {}, {}
        for index, raw in enumerate(definitions or []):
            path = ('definitions', index)
            declaration = _definition(raw, path, diagnostics)
            if type(raw) is dict:
                _definition_duplicates(raw, path, diagnostics, identities, names)
            if declaration is not None:
                declarations.append(declaration)
        if diagnostics:
            return AuthoringSchemaValidationResult(None, diagnostics)
        document = AuthoringModelDocument(AUTHORING_SCHEMA_VERSION, context, root['namespace'], declarations)
        return AuthoringSchemaValidationResult(document, ())


# MOD-05: explicit resolution bindings and pure canonical transformation.
class CanonicalizationFailure(_Enum):
    INVALID_INPUT = 'MOD-TRANSFORM-001'
    INVALID_BINDING = 'MOD-TRANSFORM-002'
    MISSING_BINDING = 'MOD-TRANSFORM-003'
    UNRESOLVED_REFERENCE = 'MOD-TRANSFORM-004'
    SCOPE_CONFLICT = 'MOD-TRANSFORM-005'
    UNSUPPORTED_FACET = 'MOD-TRANSFORM-006'
    UNREPRESENTABLE_VERSION = 'MOD-TRANSFORM-007'
    INVALID_TYPE_EXPRESSION = 'MOD-TRANSFORM-008'
    CONSTRAINT_CONSTRUCTION = 'MOD-TRANSFORM-009'
    FIELD_CONSTRUCTION = 'MOD-TRANSFORM-010'
    DEFINITION_CONSTRUCTION = 'MOD-TRANSFORM-011'
    MEMBERSHIP_CONFLICT = 'MOD-TRANSFORM-012'


def _coordinate(value: int) -> None:
    if type(value) is not int or value < 0:
        raise TypeError('Binding coordinates require nonnegative plain integers.')


@_dataclass(frozen=True, slots=True)
class ResolvedFieldBinding:
    """Source coordinate selects a declaration; FieldId owns semantic identity.

    target=None is correct for primitives, an unresolved failure for semantic
    expressions. Exact targets remain representable here so they can be rejected
    explicitly rather than silently weakened by the identity-only TYPE-05 seam.
    """
    facet_index: int
    field_index: int
    field_id: FieldId
    target: ElementRef | ElementVersionRef | None = None

    def __post_init__(self) -> None:
        _coordinate(self.facet_index)
        _coordinate(self.field_index)
        if type(self.field_id) is not FieldId:
            raise TypeError('Field binding requires an existing FieldId.')
        if self.target is not None:
            if type(self.target) not in (ElementRef, ElementVersionRef) or type(self.target.element_id) is not SemanticElementId:
                raise TypeError('Resolved targets require existing canonical Kernel references.')
            if type(self.target) is ElementVersionRef and type(self.target.version) is not SemanticVersion:
                raise TypeError('Exact target requires the existing SemanticVersion.')


@_dataclass(frozen=True, slots=True)
class ResolvedTypeBinding:
    declaration_index: int
    id: SemanticElementId
    qualified_name: QualifiedName
    context: SemanticContextRef
    version: SemanticVersion
    fields: tuple[ResolvedFieldBinding, ...] = ()

    def __post_init__(self) -> None:
        _coordinate(self.declaration_index)
        if type(self.id) is not SemanticElementId or type(self.qualified_name) is not QualifiedName or type(self.qualified_name.namespace) is not Namespace:
            raise TypeError('Definition binding requires existing canonical identity and name values.')
        if type(self.context) is not SemanticContextRef or type(self.context.context_id) is not SemanticElementId or type(self.version) is not SemanticVersion:
            raise TypeError('Definition binding requires canonical context and exact version values.')
        object.__setattr__(self, 'fields', _ordered(self.fields, ResolvedFieldBinding))


@_dataclass(frozen=True, slots=True)
class ResolvedAuthoringModel:
    """Immutable single-document binding boundary, not a resolution certificate.

    Constructors enforce payload types; canonicalize checks coverage, duplicate
    coordinates and agreement with authored IDs/names/versions. Caller owns target
    existence/authority and upstream resolution; no dictionary or lookup is used.
    """
    document: AuthoringModelDocument
    declarations: tuple[ResolvedTypeBinding, ...]
    retain_source_associations: bool = True

    def __post_init__(self) -> None:
        if type(self.document) is not AuthoringModelDocument:
            raise TypeError('Resolved input requires an existing authoring document.')
        object.__setattr__(self, 'declarations', _ordered(self.declarations, ResolvedTypeBinding))
        if type(self.retain_source_associations) is not bool:
            raise TypeError('Source association retention must be explicit boolean intent.')


@_dataclass(frozen=True, slots=True)
class CanonicalSourceTarget:
    """Exact semantic owner, optionally an owned FieldId; never an array index."""
    definition: ElementVersionRef
    field_id: FieldId | None = None

    def __post_init__(self) -> None:
        if type(self.definition) is not ElementVersionRef or type(self.definition.element_id) is not SemanticElementId or type(self.definition.version) is not SemanticVersion:
            raise TypeError('Source target requires an exact canonical owner reference.')
        if self.field_id is not None and type(self.field_id) is not FieldId:
            raise TypeError('Field source target requires a stable FieldId.')


@_dataclass(frozen=True, slots=True)
class CanonicalSourceAssociation:
    target: CanonicalSourceTarget
    path: AuthoringSchemaPath

    def __post_init__(self) -> None:
        if type(self.target) is not CanonicalSourceTarget or type(self.path) is not AuthoringSchemaPath:
            raise TypeError('Source associations require typed semantic targets and source coordinates.')


@_dataclass(frozen=True, slots=True)
class CanonicalizationDiagnostic:
    """Narrow MOD-05 diagnostic pending general SK-11; delegated codes retained."""
    code: CanonicalizationFailure
    message: str
    path: AuthoringSchemaPath
    cause_code: str | None = None
    related_path: AuthoringSchemaPath | None = None
    membership_diagnostic: CanonicalConstructionDiagnostic | None = None

    def __post_init__(self) -> None:
        if type(self.code) is not CanonicalizationFailure or type(self.message) is not str or not self.message:
            raise TypeError('Transformation diagnostics require a known code and message.')
        if type(self.path) is not AuthoringSchemaPath or self.related_path is not None and type(self.related_path) is not AuthoringSchemaPath:
            raise TypeError('Transformation diagnostic coordinates must be typed.')
        if self.cause_code is not None and type(self.cause_code) is not str:
            raise TypeError('Delegated diagnostic codes require text.')
        if self.membership_diagnostic is not None and type(self.membership_diagnostic) is not CanonicalConstructionDiagnostic:
            raise TypeError('Membership failures preserve the exact MOD-04 diagnostic.')

    @property
    def severity(self) -> TypeValidationSeverity:
        return TypeValidationSeverity.ERROR


@_dataclass(frozen=True, slots=True)
class CanonicalizationResult:
    model: CanonicalModel | None
    diagnostics: tuple[CanonicalizationDiagnostic, ...] = ()
    source_associations: tuple[CanonicalSourceAssociation, ...] = ()

    def __post_init__(self) -> None:
        object.__setattr__(self, 'diagnostics', _ordered(self.diagnostics, CanonicalizationDiagnostic))
        object.__setattr__(self, 'source_associations', _ordered(self.source_associations, CanonicalSourceAssociation))
        if (self.model is None) != bool(self.diagnostics) or self.model is not None and type(self.model) is not CanonicalModel:
            raise ValueError('Transformation returns one complete model or nonempty failure diagnostics.')
        if self.model is None and self.source_associations:
            raise ValueError('Failed transformations cannot advertise successful canonical targets.')
        if self.model is not None:
            field_ids = {ElementVersionRef(d.type_definition.id, d.type_definition.version): frozenset(f.id for f in d.data.fields) if d.data is not None else frozenset() for d in self.model.definitions}
            for association in self.source_associations:
                members = field_ids.get(association.target.definition)
                if members is None or association.target.field_id is not None and association.target.field_id not in members:
                    raise ValueError('Every source association must identify actual canonical membership.')

    @property
    def is_success(self) -> bool:
        return self.model is not None


def _transform_error(diagnostics: list[CanonicalizationDiagnostic], code: CanonicalizationFailure, message: str, path: tuple = (), *, cause: str | None = None, related: tuple | None = None) -> None:
    diagnostics.append(CanonicalizationDiagnostic(code, message, AuthoringSchemaPath(path), cause, None if related is None else AuthoringSchemaPath(related)))


def _resolved_type_ref(expression: AuthoringTypeExpression, binding: ResolvedFieldBinding, path: tuple, diagnostics: list[CanonicalizationDiagnostic]) -> PrimitiveTypeRef | SemanticTypeRef | None:
    if type(expression) is AuthoringPrimitiveExpression:
        if binding.target is not None:
            _transform_error(diagnostics, CanonicalizationFailure.INVALID_BINDING, 'Primitive fields must not carry a semantic target.', path)
            return None
        return PrimitiveTypeRef(expression.primitive)
    if type(expression) not in (AuthoringNameExpression, AuthoringIdentityExpression, AuthoringVersionExpression):
        _transform_error(diagnostics, CanonicalizationFailure.INVALID_TYPE_EXPRESSION, 'Unsupported authoring type expression.', path)
        return None
    if binding.target is None:
        _transform_error(diagnostics, CanonicalizationFailure.UNRESOLVED_REFERENCE, 'Semantic expression requires an explicitly resolved target.', path)
        return None
    if type(expression) is AuthoringVersionExpression or type(binding.target) is ElementVersionRef:
        _transform_error(diagnostics, CanonicalizationFailure.UNREPRESENTABLE_VERSION, 'TYPE-05 currently permits only ElementRef; an exact target pin cannot be weakened or discarded.', path, cause='TYPE-REF-003')
        return None
    if type(expression) is AuthoringIdentityExpression and expression.reference != binding.target:
        _transform_error(diagnostics, CanonicalizationFailure.INVALID_BINDING, 'Resolved target disagrees with the authored stable identity.', path)
        return None
    return SemanticTypeRef(binding.target)


@_dataclass(frozen=True, slots=True)
class Canonicalizer:
    """Stateless transformation only. No parser, resolver, registry or validator."""
    def canonicalize(self, resolved_model: ResolvedAuthoringModel) -> CanonicalizationResult:
        diagnostics: list[CanonicalizationDiagnostic] = []
        if type(resolved_model) is not ResolvedAuthoringModel:
            _transform_error(diagnostics, CanonicalizationFailure.INVALID_INPUT, 'Supply the explicit immutable resolved authoring input contract.')
            return CanonicalizationResult(None, diagnostics)
        document = resolved_model.document
        if document.schema_version != AUTHORING_SCHEMA_VERSION:
            _transform_error(diagnostics, CanonicalizationFailure.INVALID_INPUT, 'Unsupported authoring schema version.', ('schemaVersion',))
            return CanonicalizationResult(None, diagnostics)
        bindings: dict[int, ResolvedTypeBinding] = {}
        duplicate_bindings: set[int] = set()
        for binding in resolved_model.declarations:
            index = binding.declaration_index
            path = ('definitions', index)
            if index >= len(document.definitions):
                _transform_error(diagnostics, CanonicalizationFailure.INVALID_BINDING, 'Binding selects no authored declaration.', path)
            elif index in bindings:
                duplicate_bindings.add(index)
                _transform_error(diagnostics, CanonicalizationFailure.INVALID_BINDING, 'Duplicate definition binding coordinate.', path, related=path)
            else:
                bindings[index] = binding
        definitions: list[CanonicalDefinition] = []
        candidate_paths: list[tuple] = []
        associations: list[CanonicalSourceAssociation] = []
        namespace = Namespace.parse(document.namespace)
        for index, declaration in enumerate(document.definitions):
            path = ('definitions', index)
            binding = bindings.get(index)
            if binding is None:
                _transform_error(diagnostics, CanonicalizationFailure.MISSING_BINDING, 'Every definition requires an explicit identity/name/context/version binding.', path)
                continue
            if index in duplicate_bindings:
                continue
            start = len(diagnostics)
            if binding.context != document.context:
                _transform_error(diagnostics, CanonicalizationFailure.SCOPE_CONFLICT, 'Bound context disagrees with the explicit model scope.', path)
            if binding.id != SemanticElementId.parse(declaration.id) or binding.version != SemanticVersion.parse(declaration.version) or binding.qualified_name != QualifiedName.create(namespace, declaration.name):
                _transform_error(diagnostics, CanonicalizationFailure.INVALID_BINDING, 'Binding must preserve the authored identity, exact version and declared qualified name.', path)
            if len(declaration.facets) > 1:
                _transform_error(diagnostics, CanonicalizationFailure.UNSUPPORTED_FACET, 'DataFacet v0 permits at most one facet; no merge is performed.', (*path, 'facets'), cause='TYPE-DATA-005')
            field_bindings: dict[tuple[int, int], ResolvedFieldBinding] = {}
            duplicated_fields: set[tuple[int, int]] = set()
            for field_binding in binding.fields:
                key = (field_binding.facet_index, field_binding.field_index)
                field_path = (*path, 'facets', key[0], 'fields', key[1])
                if key[0] >= len(declaration.facets) or key[1] >= len(declaration.facets[key[0]].fields):
                    _transform_error(diagnostics, CanonicalizationFailure.INVALID_BINDING, 'Field binding selects no authored field.', field_path)
                elif key in field_bindings:
                    duplicated_fields.add(key)
                    _transform_error(diagnostics, CanonicalizationFailure.INVALID_BINDING, 'Duplicate field binding coordinate.', field_path, related=field_path)
                else:
                    field_bindings[key] = field_binding
            fields: list[FieldDefinition] = []
            field_paths: list[tuple] = []
            for facet_index, facet in enumerate(declaration.facets):
                for field_index, field in enumerate(facet.fields):
                    field_path = (*path, 'facets', facet_index, 'fields', field_index)
                    field_binding = field_bindings.get((facet_index, field_index))
                    if field_binding is None:
                        _transform_error(diagnostics, CanonicalizationFailure.MISSING_BINDING, 'Every field requires an explicit stable FieldId binding.', field_path)
                        continue
                    if (facet_index, field_index) in duplicated_fields:
                        continue
                    if field_binding.field_id != FieldId.parse(field.id):
                        _transform_error(diagnostics, CanonicalizationFailure.INVALID_BINDING, 'Field binding must preserve the authored FieldId.', (*field_path, 'id'))
                        continue
                    type_ref = _resolved_type_ref(field.type, field_binding, (*field_path, 'type'), diagnostics)
                    if type_ref is None:
                        continue
                    try:
                        constraints = FieldConstraintSet.create(field.constraints.presence, field.constraints.nullability, tuple(_CONSTRAINT_FACTORIES[v.kind](v.value) for v in field.constraints.values))
                    except FieldConstraintError as error:
                        value_path = (*field_path, 'constraints')
                        if error.constraint_index is not None:
                            value_path = (*value_path, 'values', error.constraint_index)
                        related = None if error.previous_index is None else (*field_path, 'constraints', 'values', error.previous_index)
                        _transform_error(diagnostics, CanonicalizationFailure.CONSTRAINT_CONSTRUCTION, error.message, value_path, cause=error.code, related=related)
                        continue
                    try:
                        canonical_field = FieldDefinition.create(field_binding.field_id, FieldName.parse(field.name), type_ref, constraints)
                    except (FieldDefinitionError, FieldNameError, TypeRefError) as error:
                        _transform_error(diagnostics, CanonicalizationFailure.FIELD_CONSTRUCTION, error.message, field_path, cause=error.code)
                        continue
                    fields.append(canonical_field)
                    field_paths.append(field_path)
            if len(diagnostics) != start:
                continue
            try:
                data = None if not declaration.facets else DataFacet.create(fields)
                definition = create_type_data_definition(binding.id, binding.qualified_name, binding.context, binding.version, data)
            except DataFacetError as error:
                error_path = (*path, 'facets') if error.field_index is None else field_paths[error.field_index]
                related = None if error.previous_index is None else field_paths[error.previous_index]
                _transform_error(diagnostics, CanonicalizationFailure.DEFINITION_CONSTRUCTION, error.message, error_path, cause=error.code, related=related)
                continue
            definitions.append(definition)
            candidate_paths.append(path)
            if resolved_model.retain_source_associations:
                reference = ElementVersionRef(binding.id, binding.version)
                associations.append(CanonicalSourceAssociation(CanonicalSourceTarget(reference), AuthoringSchemaPath(path)))
                associations.extend(CanonicalSourceAssociation(CanonicalSourceTarget(reference, field.id), AuthoringSchemaPath(field_path)) for field, field_path in zip(fields, field_paths))
        assembled = CanonicalModelFactory().create(document.context, definitions)
        for diagnostic in assembled.diagnostics:
            primary = () if diagnostic.input_index is None else candidate_paths[diagnostic.input_index]
            related = None if diagnostic.related_input_index is None else AuthoringSchemaPath(candidate_paths[diagnostic.related_input_index])
            diagnostics.append(CanonicalizationDiagnostic(CanonicalizationFailure.MEMBERSHIP_CONFLICT, diagnostic.message, AuthoringSchemaPath(primary), diagnostic.code.value, related, diagnostic))
        if diagnostics:
            return CanonicalizationResult(None, diagnostics)
        return CanonicalizationResult(assembled.model, (), associations)


__all__ += [
    'ResolvedAuthoringModel', 'ResolvedTypeBinding', 'ResolvedFieldBinding',
    'Canonicalizer', 'CanonicalizationResult', 'CanonicalizationDiagnostic',
    'CanonicalizationFailure', 'CanonicalSourceTarget', 'CanonicalSourceAssociation',
]


# MOD-06: name-to-identity resolution in explicit immutable visibility snapshots.
class NamespaceResolutionFailure(_Enum):
    INVALID_EXPRESSION = 'MOD-NAMESPACE-001'
    INVALID_ENVIRONMENT = 'MOD-NAMESPACE-002'
    NAME_NOT_FOUND = 'MOD-NAMESPACE-003'
    AMBIGUOUS_NAME = 'MOD-NAMESPACE-004'
    ALIAS_NOT_FOUND = 'MOD-NAMESPACE-005'
    ALIAS_COLLISION = 'MOD-NAMESPACE-006'
    CONTEXT_MISMATCH = 'MOD-NAMESPACE-007'
    KIND_MISMATCH = 'MOD-NAMESPACE-008'
    VERSION_NOT_FOUND = 'MOD-NAMESPACE-009'
    SYMBOL_COLLISION = 'MOD-NAMESPACE-010'
    UNBOUND_LOOKUP_VERSION = 'MOD-NAMESPACE-011'
    INVALID_BINDING = 'MOD-NAMESPACE-012'


def _resolution_reference(reference: ElementRef | ElementVersionRef) -> None:
    if type(reference) not in (ElementRef, ElementVersionRef) or type(reference.element_id) is not SemanticElementId:
        raise TypeError('Resolution requires canonical Kernel reference values.')
    if type(reference) is ElementVersionRef and type(reference.version) is not SemanticVersion:
        raise TypeError('Exact resolution requires a canonical SemanticVersion.')


def _resolution_path(path: AuthoringSchemaPath | None) -> None:
    if path is not None and type(path) is not AuthoringSchemaPath:
        raise TypeError('Optional source coordinates require the existing authoring path.')


@_dataclass(frozen=True, slots=True)
class SemanticSymbol:
    """Minimal declared coordinate; no semantic definition/facet is duplicated."""
    context: SemanticContextRef
    qualified_name: QualifiedName
    reference: ElementVersionRef
    kind: SemanticElementKind
    path: AuthoringSchemaPath | None = None

    def __post_init__(self) -> None:
        if type(self.context) is not SemanticContextRef or type(self.context.context_id) is not SemanticElementId:
            raise TypeError('Symbol requires an explicit canonical context.')
        if type(self.qualified_name) is not QualifiedName or type(self.qualified_name.namespace) is not Namespace or type(self.kind) is not SemanticElementKind:
            raise TypeError('Symbol name/kind must use existing Kernel values.')
        _resolution_reference(self.reference)
        if type(self.reference) is not ElementVersionRef:
            raise TypeError('Each declared symbol records its explicit definition version.')
        _resolution_path(self.path)


@_dataclass(frozen=True, slots=True)
class NamespaceAlias:
    """Environment-scoped alias to a concrete Namespace, never another alias."""
    alias: Namespace
    target: Namespace
    path: AuthoringSchemaPath | None = None

    def __post_init__(self) -> None:
        if type(self.alias) is not Namespace or len(self.alias.segments) != 1 or type(self.target) is not Namespace:
            raise TypeError('Alias requires a single canonical namespace segment and concrete Namespace target.')
        _resolution_path(self.path)


@_dataclass(frozen=True, slots=True)
class AliasQualifiedNameExpression:
    """Explicit resolver-only capability; not an extension of MOD-01 syntax."""
    alias: Namespace
    local_name: str

    def __post_init__(self) -> None:
        if type(self.alias) is not Namespace or len(self.alias.segments) != 1 or type(self.local_name) is not str:
            raise TypeError('Alias-qualified expression requires an explicit single alias and local name.')
        QualifiedName.create(self.alias, self.local_name)


NamespaceNameExpression = AuthoringNameExpression | AuthoringIdentityExpression | AuthoringVersionExpression | AliasQualifiedNameExpression
_NAMESPACE_EXPRESSION_TYPES = (AuthoringNameExpression, AuthoringIdentityExpression, AuthoringVersionExpression, AliasQualifiedNameExpression)


@_dataclass(frozen=True, slots=True)
class NamespaceResolutionRequest:
    expression: NamespaceNameExpression
    context: SemanticContextRef
    expected_kind: SemanticElementKind | None = None
    exact_version: SemanticVersion | None = None
    path: AuthoringSchemaPath | None = None

    def __post_init__(self) -> None:
        if type(self.expression) not in _NAMESPACE_EXPRESSION_TYPES:
            raise TypeError('Name resolution requires a supported explicit expression variant.')
        if type(self.context) is not SemanticContextRef or type(self.context.context_id) is not SemanticElementId:
            raise TypeError('Resolution request requires an explicit canonical context.')
        if self.expected_kind is not None and type(self.expected_kind) is not SemanticElementKind or self.exact_version is not None and type(self.exact_version) is not SemanticVersion:
            raise TypeError('Optional kind/version requirements must use existing Kernel values.')
        _resolution_path(self.path)


@_dataclass(frozen=True, slots=True)
class NamespaceResolutionDiagnostic:
    """Narrow actual MOD diagnostic seam pending missing general SK-11."""
    code: NamespaceResolutionFailure
    message: str
    context: SemanticContextRef | None = None
    expression: NamespaceNameExpression | None = None
    exact_version: SemanticVersion | None = None
    candidates: tuple[SemanticSymbol, ...] = ()
    path: AuthoringSchemaPath | None = None
    related_paths: tuple[AuthoringSchemaPath, ...] = ()
    cause_code: str | None = None

    def __post_init__(self) -> None:
        if type(self.code) is not NamespaceResolutionFailure or type(self.message) is not str or not self.message:
            raise TypeError('Namespace diagnostics require a known code and nonempty message.')
        if self.context is not None and (type(self.context) is not SemanticContextRef or type(self.context.context_id) is not SemanticElementId):
            raise TypeError('Diagnostic context must be a canonical context or absent.')
        if self.expression is not None and type(self.expression) not in _NAMESPACE_EXPRESSION_TYPES or self.exact_version is not None and type(self.exact_version) is not SemanticVersion:
            raise TypeError('Diagnostic expression/version must be typed or absent.')
        object.__setattr__(self, 'candidates', _ordered(self.candidates, SemanticSymbol))
        object.__setattr__(self, 'related_paths', _ordered(self.related_paths, AuthoringSchemaPath))
        _resolution_path(self.path)
        if self.cause_code is not None and type(self.cause_code) is not str:
            raise TypeError('Delegated lookup codes require text.')

    @property
    def severity(self) -> TypeValidationSeverity:
        return TypeValidationSeverity.ERROR


def _symbol_order(symbol: SemanticSymbol) -> tuple:
    return (symbol.reference.element_id.value, symbol.reference.version, str(symbol.qualified_name), symbol.kind.value, '' if symbol.path is None else str(symbol.path))


def _symbol_diagnostic(code: NamespaceResolutionFailure, message: str, context: SemanticContextRef, candidates: tuple[SemanticSymbol, ...]) -> NamespaceResolutionDiagnostic:
    candidates = tuple(sorted(set(candidates), key=_symbol_order))
    paths = tuple(sorted({s.path for s in candidates if s.path is not None}, key=str))
    return NamespaceResolutionDiagnostic(code, message, context, candidates=candidates, path=None if not paths else paths[0], related_paths=paths[1:])


class NamespaceEnvironmentError(ValueError):
    def __init__(self, diagnostics: tuple[NamespaceResolutionDiagnostic, ...]) -> None:
        if type(diagnostics) is not tuple or not diagnostics or any(type(d) is not NamespaceResolutionDiagnostic for d in diagnostics):
            raise TypeError('Environment construction errors require nonempty typed diagnostics.')
        self.diagnostics = diagnostics
        super().__init__('Namespace visibility snapshot violates intrinsic invariants.')


@_dataclass(frozen=True, slots=True)
class NamespaceResolutionEnvironment:
    """Single-context explicit visibility; no live lookup, authorization or globals.

    Local/visible symbols have equal standing. Unqualified names search current
    namespace plus explicit search_namespaces; none shadows another. Qualified
    names search exactly their namespace among supplied symbols.
    """
    context: SemanticContextRef
    current_namespace: Namespace
    local_symbols: tuple[SemanticSymbol, ...] = ()
    visible_symbols: tuple[SemanticSymbol, ...] = ()
    aliases: tuple[NamespaceAlias, ...] = ()
    search_namespaces: tuple[Namespace, ...] = ()
    _names: _Mapping[QualifiedName, tuple[SemanticSymbol, ...]] = _dataclass_field(init=False, repr=False, compare=False, hash=False)
    _identities: _Mapping[SemanticElementId, tuple[SemanticSymbol, ...]] = _dataclass_field(init=False, repr=False, compare=False, hash=False)
    _aliases: _Mapping[Namespace, NamespaceAlias] = _dataclass_field(init=False, repr=False, compare=False, hash=False)

    def __post_init__(self) -> None:
        if type(self.context) is not SemanticContextRef or type(self.context.context_id) is not SemanticElementId or type(self.current_namespace) is not Namespace:
            raise TypeError('Environment requires explicit canonical context and current namespace.')
        local = _ordered(self.local_symbols, SemanticSymbol)
        visible = _ordered(self.visible_symbols, SemanticSymbol)
        aliases = tuple(sorted(_ordered(self.aliases, NamespaceAlias), key=lambda a: (a.alias.value, a.target.value, '' if a.path is None else str(a.path))))
        search = tuple(sorted(set((self.current_namespace, *_ordered(self.search_namespaces, Namespace))), key=str))
        symbols = tuple(sorted(set((*local, *visible)), key=_symbol_order))
        diagnostics: list[NamespaceResolutionDiagnostic] = []
        exact: dict[ElementVersionRef, SemanticSymbol] = {}
        kinds: dict[SemanticElementId, SemanticSymbol] = {}
        ownership: dict[QualifiedName, SemanticSymbol] = {}
        names: dict[QualifiedName, list[SemanticSymbol]] = {}
        identities: dict[SemanticElementId, list[SemanticSymbol]] = {}
        for symbol in symbols:
            if symbol.context != self.context:
                diagnostics.append(_symbol_diagnostic(NamespaceResolutionFailure.CONTEXT_MISMATCH, 'Visible symbol belongs to a different semantic context; cross-context lookup is not supported in v0.', self.context, (symbol,)))
                continue
            previous = exact.get(symbol.reference)
            if previous is not None and (previous.qualified_name != symbol.qualified_name or previous.kind != symbol.kind):
                diagnostics.append(_symbol_diagnostic(NamespaceResolutionFailure.SYMBOL_COLLISION, 'One exact identity/version has conflicting symbol name or kind.', self.context, (previous, symbol)))
            first_kind = kinds.get(symbol.reference.element_id)
            if first_kind is not None and first_kind.kind != symbol.kind:
                diagnostics.append(_symbol_diagnostic(NamespaceResolutionFailure.SYMBOL_COLLISION, 'A stable identity cannot designate conflicting semantic kinds in this visibility snapshot.', self.context, (first_kind, symbol)))
            owner = ownership.get(symbol.qualified_name)
            if owner is not None and owner.reference.element_id != symbol.reference.element_id:
                diagnostics.append(_symbol_diagnostic(NamespaceResolutionFailure.SYMBOL_COLLISION, 'Qualified-name ownership conflicts across explicitly visible identities/versions.', self.context, (owner, symbol)))
            exact.setdefault(symbol.reference, symbol)
            kinds.setdefault(symbol.reference.element_id, symbol)
            ownership.setdefault(symbol.qualified_name, symbol)
            names.setdefault(symbol.qualified_name, []).append(symbol)
            identities.setdefault(symbol.reference.element_id, []).append(symbol)
        alias_index: dict[Namespace, NamespaceAlias] = {}
        for alias in aliases:
            previous = alias_index.get(alias.alias)
            if previous is not None and previous.target != alias.target:
                paths = tuple(sorted({a.path for a in (previous, alias) if a.path is not None}, key=str))
                diagnostics.append(NamespaceResolutionDiagnostic(NamespaceResolutionFailure.ALIAS_COLLISION, f'Alias {alias.alias} has conflicting concrete targets {previous.target} and {alias.target}.', self.context, path=None if not paths else paths[0], related_paths=paths[1:]))
            alias_index.setdefault(alias.alias, alias)
        if diagnostics:
            raise NamespaceEnvironmentError(tuple(diagnostics))
        object.__setattr__(self, 'local_symbols', tuple(sorted(set(local), key=_symbol_order)))
        object.__setattr__(self, 'visible_symbols', tuple(sorted(set(visible), key=_symbol_order)))
        object.__setattr__(self, 'aliases', tuple(alias_index.values()))
        object.__setattr__(self, 'search_namespaces', search)
        object.__setattr__(self, '_names', _MappingProxyType({k: tuple(v) for k, v in names.items()}))
        object.__setattr__(self, '_identities', _MappingProxyType({k: tuple(v) for k, v in identities.items()}))
        object.__setattr__(self, '_aliases', _MappingProxyType(alias_index))


@_dataclass(frozen=True, slots=True)
class NamespaceEnvironmentResult:
    environment: NamespaceResolutionEnvironment | None
    diagnostics: tuple[NamespaceResolutionDiagnostic, ...] = ()

    def __post_init__(self) -> None:
        object.__setattr__(self, 'diagnostics', _ordered(self.diagnostics, NamespaceResolutionDiagnostic))
        if (self.environment is None) != bool(self.diagnostics) or self.environment is not None and type(self.environment) is not NamespaceResolutionEnvironment:
            raise ValueError('Environment result must contain a complete snapshot or nonempty failure diagnostics.')

    @property
    def is_success(self) -> bool:
        return self.environment is not None


@_dataclass(frozen=True, slots=True)
class NamespaceEnvironmentFactory:
    def create(self, context: SemanticContextRef, current_namespace: Namespace, local_symbols: tuple[SemanticSymbol, ...] = (), visible_symbols: tuple[SemanticSymbol, ...] = (), aliases: tuple[NamespaceAlias, ...] = (), search_namespaces: tuple[Namespace, ...] = ()) -> NamespaceEnvironmentResult:
        try:
            return NamespaceEnvironmentResult(NamespaceResolutionEnvironment(context, current_namespace, local_symbols, visible_symbols, aliases, search_namespaces))
        except NamespaceEnvironmentError as error:
            return NamespaceEnvironmentResult(None, error.diagnostics)


@_dataclass(frozen=True, slots=True)
class ResolvedSemanticTarget:
    """Identity or explicit exact coordinate, never an implicitly chosen version.

    Identity lookups can have several explicitly recorded names over versions.
    Returning all matching names avoids choosing a historical/current name.
    """
    reference: ElementRef | ElementVersionRef
    context: SemanticContextRef
    kind: SemanticElementKind
    qualified_names: tuple[QualifiedName, ...]

    def __post_init__(self) -> None:
        _resolution_reference(self.reference)
        if type(self.context) is not SemanticContextRef or type(self.context.context_id) is not SemanticElementId or type(self.kind) is not SemanticElementKind:
            raise TypeError('Resolved target requires existing context and kind values.')
        names = _ordered(self.qualified_names, QualifiedName)
        if not names or any(type(n.namespace) is not Namespace for n in names):
            raise TypeError('Resolved target must retain nonempty canonical matching qualified names.')
        object.__setattr__(self, 'qualified_names', tuple(sorted(set(names), key=str)))


@_dataclass(frozen=True, slots=True)
class NamespaceResolutionResult:
    target: ResolvedSemanticTarget | None
    diagnostics: tuple[NamespaceResolutionDiagnostic, ...] = ()
    path: AuthoringSchemaPath | None = None

    def __post_init__(self) -> None:
        object.__setattr__(self, 'diagnostics', _ordered(self.diagnostics, NamespaceResolutionDiagnostic))
        if (self.target is None) != bool(self.diagnostics) or self.target is not None and type(self.target) is not ResolvedSemanticTarget:
            raise ValueError('Resolution requires one complete target or nonempty failure diagnostics.')
        _resolution_path(self.path)

    @property
    def is_success(self) -> bool:
        return self.target is not None


def _resolution_failure(request: NamespaceResolutionRequest, code: NamespaceResolutionFailure, message: str, candidates: tuple[SemanticSymbol, ...] = (), exact_version: SemanticVersion | None = None) -> NamespaceResolutionResult:
    ordered = tuple(sorted(set(candidates), key=_symbol_order))
    related = tuple(sorted({s.path for s in ordered if s.path is not None and s.path != request.path}, key=str))
    diagnostic = NamespaceResolutionDiagnostic(code, message, request.context, request.expression, exact_version if exact_version is not None else request.exact_version, ordered, request.path, related)
    return NamespaceResolutionResult(None, (diagnostic,), request.path)


@_dataclass(frozen=True, slots=True)
class NamespaceResolver:
    """Stateless scoped name resolution. No semantic construction or traversal."""
    def resolve(self, request: NamespaceResolutionRequest, environment: NamespaceResolutionEnvironment) -> NamespaceResolutionResult:
        if type(request) is not NamespaceResolutionRequest:
            return NamespaceResolutionResult(None, (NamespaceResolutionDiagnostic(NamespaceResolutionFailure.INVALID_EXPRESSION, 'Supply a typed resolution request.'),))
        if type(environment) is not NamespaceResolutionEnvironment:
            return _resolution_failure(request, NamespaceResolutionFailure.INVALID_ENVIRONMENT, 'Supply an immutable explicit namespace environment.')
        if request.context != environment.context:
            return _resolution_failure(request, NamespaceResolutionFailure.CONTEXT_MISMATCH, 'Request context differs from the explicit visibility context.')
        expression = request.expression
        exact = request.exact_version
        if type(expression) is AuthoringVersionExpression:
            if exact is not None and exact != expression.reference.version:
                return _resolution_failure(request, NamespaceResolutionFailure.INVALID_EXPRESSION, 'The authored exact coordinate conflicts with the requested exact version.')
            exact = expression.reference.version
        if type(expression) in (AuthoringIdentityExpression, AuthoringVersionExpression):
            # No qualified-name re-resolution. Visibility/kind/version safeguards
            # still apply to the identity explicitly supplied by the author.
            candidates = environment._identities.get(expression.reference.element_id, ())
        elif type(expression) is AliasQualifiedNameExpression:
            alias = environment._aliases.get(expression.alias)
            if alias is None:
                return _resolution_failure(request, NamespaceResolutionFailure.ALIAS_NOT_FOUND, 'Alias is not declared in this explicit environment.')
            name = QualifiedName.create(alias.target, expression.local_name)
            candidates = environment._names.get(name, ())
        elif '.' in expression.name:
            candidates = environment._names.get(QualifiedName.parse(expression.name), ())
        else:
            candidates = tuple(symbol for namespace in environment.search_namespaces for symbol in environment._names.get(QualifiedName.create(namespace, expression.name), ()))
        candidates = tuple(sorted(set(candidates), key=_symbol_order))
        if not candidates:
            return _resolution_failure(request, NamespaceResolutionFailure.NAME_NOT_FOUND, 'No explicitly visible symbol designates the requested name or identity.', exact_version=exact)
        identities = {s.reference.element_id for s in candidates}
        if len(identities) != 1:
            return _resolution_failure(request, NamespaceResolutionFailure.AMBIGUOUS_NAME, 'The permitted name scope designates multiple stable semantic identities; neither kind nor version requirements choose an identity.', candidates, exact)
        if request.expected_kind is not None and candidates[0].kind != request.expected_kind:
            return _resolution_failure(request, NamespaceResolutionFailure.KIND_MISMATCH, 'Resolved identity has a different declared semantic kind.', candidates, exact)
        if exact is not None:
            selected = tuple(s for s in candidates if s.reference.version == exact)
            if not selected:
                return _resolution_failure(request, NamespaceResolutionFailure.VERSION_NOT_FOUND, 'The explicitly requested exact version is not visible under this expression.', candidates, exact)
            candidates = selected
        identity = candidates[0].reference.element_id
        reference = ElementRef(identity) if exact is None else ElementVersionRef(identity, exact)
        target = ResolvedSemanticTarget(reference, request.context, candidates[0].kind, tuple(s.qualified_name for s in candidates))
        return NamespaceResolutionResult(target, (), request.path)


@_dataclass(frozen=True, slots=True)
class NamespaceSymbolSnapshotResult:
    symbols: tuple[SemanticSymbol, ...] = ()
    diagnostics: tuple[NamespaceResolutionDiagnostic, ...] = ()

    def __post_init__(self) -> None:
        object.__setattr__(self, 'symbols', _ordered(self.symbols, SemanticSymbol))
        object.__setattr__(self, 'diagnostics', _ordered(self.diagnostics, NamespaceResolutionDiagnostic))
        if self.diagnostics and self.symbols:
            raise ValueError('Failed symbol capture cannot expose a partial successful snapshot.')

    @property
    def is_success(self) -> bool:
        return not self.diagnostics


@_dataclass(frozen=True, slots=True)
class TypeLookupSymbolAdapter:
    """Snapshot only explicitly selected identities from actual TYPE-07 TypeLookup.

    Use a caller-bound exact view for multi-version registries; this adapter does
    not enumerate a global registry or bind/select versions itself. Environment
    stores copied symbols, never the live port. Non-type hosts are rejected.
    """
    lookup: TypeLookup

    def __post_init__(self) -> None:
        if not callable(getattr(self.lookup, 'find', None)):
            raise TypeError('Symbol adapter requires the existing read-only TypeLookup port.')

    def capture(self, context: SemanticContextRef, references: tuple[ElementRef, ...]) -> NamespaceSymbolSnapshotResult:
        if type(context) is not SemanticContextRef or type(context.context_id) is not SemanticElementId:
            raise TypeError('Symbol capture requires an explicit canonical context.')
        references = _ordered(references, ElementRef)
        for reference in references:
            _resolution_reference(reference)
        symbols: list[SemanticSymbol] = []
        diagnostics: list[NamespaceResolutionDiagnostic] = []
        for reference in sorted(set(references), key=lambda r: r.element_id.value):
            try:
                host = self.lookup.find(reference)
            except TypeRegistryAmbiguityError:
                diagnostics.append(NamespaceResolutionDiagnostic(NamespaceResolutionFailure.UNBOUND_LOOKUP_VERSION, 'TYPE-07 lookup has multiple versions; the caller must supply an explicitly bound view.', context, AuthoringIdentityExpression(reference), cause_code='TYPE-REG-006'))
                continue
            if host is None:
                diagnostics.append(NamespaceResolutionDiagnostic(NamespaceResolutionFailure.NAME_NOT_FOUND, 'Explicitly selected lookup identity is absent.', context, AuthoringIdentityExpression(reference)))
                continue
            values = tuple(getattr(host, name, None) for name in ('id', 'qualified_name', 'context', 'kind', 'version'))
            expected = (SemanticElementId, QualifiedName, SemanticContextRef, SemanticElementKind, SemanticVersion)
            if any(type(v) is not t for v, t in zip(values, expected)) or type(values[1].namespace) is not Namespace or type(values[2].context_id) is not SemanticElementId or values[0] != reference.element_id:
                diagnostics.append(NamespaceResolutionDiagnostic(NamespaceResolutionFailure.INVALID_ENVIRONMENT, 'TypeLookup returned an invalid or mismatched semantic identity snapshot.', context, AuthoringIdentityExpression(reference)))
                continue
            symbol = SemanticSymbol(values[2], values[1], ElementVersionRef(values[0], values[4]), values[3])
            if symbol.context != context:
                diagnostics.append(_symbol_diagnostic(NamespaceResolutionFailure.CONTEXT_MISMATCH, 'Selected lookup symbol belongs to another context.', context, (symbol,)))
            elif symbol.kind != SemanticElementKinds.TYPE_DEFINITION:
                diagnostics.append(_symbol_diagnostic(NamespaceResolutionFailure.KIND_MISMATCH, 'TYPE-07 adapter contributes only type-definition symbols.', context, (symbol,)))
            else:
                symbols.append(symbol)
        return NamespaceSymbolSnapshotResult((), diagnostics) if diagnostics else NamespaceSymbolSnapshotResult(tuple(sorted(symbols, key=_symbol_order)))


def local_authoring_symbols(document: AuthoringModelDocument) -> NamespaceSymbolSnapshotResult:
    """Project declared identities before field binding; no definitions constructed."""
    if type(document) is not AuthoringModelDocument or document.schema_version != AUTHORING_SCHEMA_VERSION:
        return NamespaceSymbolSnapshotResult((), (NamespaceResolutionDiagnostic(NamespaceResolutionFailure.INVALID_ENVIRONMENT, 'Supply an existing supported authoring document for local declaration visibility.'),))
    namespace = Namespace.parse(document.namespace)
    symbols = tuple(SemanticSymbol(document.context, QualifiedName.create(namespace, d.name), ElementVersionRef(SemanticElementId.parse(d.id), SemanticVersion.parse(d.version)), SemanticElementKinds.TYPE_DEFINITION, AuthoringSchemaPath(('definitions', i))) for i, d in enumerate(document.definitions))
    return NamespaceSymbolSnapshotResult(tuple(sorted(symbols, key=_symbol_order)))


@_dataclass(frozen=True, slots=True)
class NamespaceFieldBindingResult:
    binding: ResolvedFieldBinding | None
    diagnostics: tuple[NamespaceResolutionDiagnostic, ...] = ()

    def __post_init__(self) -> None:
        object.__setattr__(self, 'diagnostics', _ordered(self.diagnostics, NamespaceResolutionDiagnostic))
        if (self.binding is None) != bool(self.diagnostics) or self.binding is not None and type(self.binding) is not ResolvedFieldBinding:
            raise ValueError('Field binding result contains an existing binding or failure diagnostics.')

    @property
    def is_success(self) -> bool:
        return self.binding is not None


def bind_namespace_target(result: NamespaceResolutionResult, facet_index: int, field_index: int, field_id: FieldId) -> NamespaceFieldBindingResult:
    """Minimal MOD-05 bridge, not complete model/reference binding orchestration.

    Exact pins stay exact. Current Canonicalizer will reject them until TYPE-05
    supports that representation; this bridge must not silently downgrade them.
    """
    if type(result) is not NamespaceResolutionResult:
        raise TypeError('Binding requires an actual namespace-resolution result.')
    _coordinate(facet_index)
    _coordinate(field_index)
    if type(field_id) is not FieldId:
        raise TypeError('Binding requires a supplied stable FieldId.')
    if result.target is None:
        return NamespaceFieldBindingResult(None, result.diagnostics)
    if result.target.kind != SemanticElementKinds.TYPE_DEFINITION:
        diagnostic = NamespaceResolutionDiagnostic(NamespaceResolutionFailure.KIND_MISMATCH, 'MOD-05 semantic field binding requires a declared type-definition target.', result.target.context, path=result.path)
        return NamespaceFieldBindingResult(None, (diagnostic,))
    return NamespaceFieldBindingResult(ResolvedFieldBinding(facet_index, field_index, field_id, result.target.reference))


__all__ += [
    'SemanticSymbol', 'NamespaceAlias', 'AliasQualifiedNameExpression',
    'NamespaceNameExpression', 'NamespaceResolutionRequest',
    'NamespaceResolutionEnvironment', 'NamespaceEnvironmentFactory',
    'NamespaceEnvironmentResult', 'NamespaceEnvironmentError',
    'NamespaceResolver', 'ResolvedSemanticTarget', 'NamespaceResolutionResult',
    'NamespaceResolutionFailure', 'NamespaceResolutionDiagnostic',
    'NamespaceSymbolSnapshotResult', 'TypeLookupSymbolAdapter',
    'local_authoring_symbols', 'NamespaceFieldBindingResult', 'bind_namespace_target',
]


# MOD-07: reference requirements, verified bindings and complete authoring input.
class ReferenceVersionRequirement(_Enum):
    IDENTITY_ONLY = 'identity-only'
    EXACT_VERSION = 'exact-version'


class ReferenceConsumer(_Enum):
    SEMANTIC_DEFINITION = 'semantic-definition'
    SEMANTIC_TYPE_FIELD = 'semantic-type-field'


@_dataclass(frozen=True, slots=True)
class SemanticReferenceRequirement:
    expected_kind: SemanticElementKind
    version_requirement: ReferenceVersionRequirement
    consumer: ReferenceConsumer = ReferenceConsumer.SEMANTIC_DEFINITION

    def __post_init__(self) -> None:
        if type(self.expected_kind) is not SemanticElementKind or type(self.version_requirement) is not ReferenceVersionRequirement or type(self.consumer) is not ReferenceConsumer:
            raise TypeError('Reference requirements need explicit typed kind/version/consumer values.')
        if self.consumer is ReferenceConsumer.SEMANTIC_TYPE_FIELD and self.expected_kind != SemanticElementKinds.TYPE_DEFINITION:
            raise TypeError('TYPE-05 semantic fields explicitly require type-definition kind.')


@_dataclass(frozen=True, slots=True)
class SemanticReferenceResolutionRequest:
    expression: NamespaceNameExpression
    context: SemanticContextRef
    requirement: SemanticReferenceRequirement
    exact_version: SemanticVersion | None = None
    path: AuthoringSchemaPath | None = None

    def __post_init__(self) -> None:
        if type(self.expression) not in _NAMESPACE_EXPRESSION_TYPES or type(self.requirement) is not SemanticReferenceRequirement:
            raise TypeError('Semantic reference requests require supported expressions and explicit requirements.')
        if type(self.context) is not SemanticContextRef or type(self.context.context_id) is not SemanticElementId:
            raise TypeError('Reference requests require canonical semantic context.')
        if self.exact_version is not None and type(self.exact_version) is not SemanticVersion:
            raise TypeError('An explicit reference pin must use SemanticVersion.')
        _resolution_path(self.path)


class ReferenceEvidenceOrigin(_Enum):
    LOCAL_DECLARATION = 'local-declaration'
    VISIBLE_SYMBOL = 'visible-symbol'


@_dataclass(frozen=True, slots=True)
class ReferenceTargetEvidence:
    symbol: SemanticSymbol
    origin: ReferenceEvidenceOrigin

    def __post_init__(self) -> None:
        if type(self.symbol) is not SemanticSymbol or type(self.origin) is not ReferenceEvidenceOrigin:
            raise TypeError('Reference evidence requires an existing declared symbol and explicit source category.')


def _evidence_order(evidence: ReferenceTargetEvidence) -> tuple:
    return (*_symbol_order(evidence.symbol), evidence.origin.value)


@_dataclass(frozen=True, slots=True)
class ResolvedReferenceBinding:
    reference: ElementRef | ElementVersionRef
    context: SemanticContextRef
    requirement: SemanticReferenceRequirement
    evidence: tuple[ReferenceTargetEvidence, ...]
    path: AuthoringSchemaPath | None = None

    def __post_init__(self) -> None:
        _resolution_reference(self.reference)
        if type(self.context) is not SemanticContextRef or type(self.context.context_id) is not SemanticElementId or type(self.requirement) is not SemanticReferenceRequirement:
            raise TypeError('Verified reference binding requires explicit typed context and requirements.')
        evidence = tuple(sorted(set(_ordered(self.evidence, ReferenceTargetEvidence)), key=_evidence_order))
        if not evidence:
            raise ValueError('A structurally valid reference alone is not target existence evidence.')
        expected_form = ElementRef if self.requirement.version_requirement is ReferenceVersionRequirement.IDENTITY_ONLY else ElementVersionRef
        if type(self.reference) is not expected_form:
            raise ValueError('Reference shape must preserve the declared version requirement.')
        if self.requirement.consumer is ReferenceConsumer.SEMANTIC_TYPE_FIELD and type(self.reference) is not ElementRef:
            raise ValueError('Current TYPE-05 cannot represent exact semantic field pins.')
        for item in evidence:
            symbol = item.symbol
            if symbol.reference.element_id != self.reference.element_id or symbol.context != self.context or symbol.kind != self.requirement.expected_kind or type(self.reference) is ElementVersionRef and symbol.reference.version != self.reference.version:
                raise ValueError('Every retained evidence coordinate must agree with the verified target.')
        object.__setattr__(self, 'evidence', evidence)
        _resolution_path(self.path)


class SemanticReferenceFailure(_Enum):
    INVALID_REQUEST = 'MOD-REFERENCE-001'
    INVALID_ENVIRONMENT = 'MOD-REFERENCE-002'
    TARGET_NOT_FOUND = 'MOD-REFERENCE-003'
    AMBIGUOUS_TARGET = 'MOD-REFERENCE-004'
    CONTEXT_MISMATCH = 'MOD-REFERENCE-005'
    KIND_MISMATCH = 'MOD-REFERENCE-006'
    EXACT_VERSION_NOT_FOUND = 'MOD-REFERENCE-007'
    UNSUPPORTED_REFERENCE_FORM = 'MOD-REFERENCE-008'
    REQUIRED_VERSION_MISSING = 'MOD-REFERENCE-009'
    INVALID_LOCAL_BINDING = 'MOD-REFERENCE-010'
    CONFLICTING_TARGET_EVIDENCE = 'MOD-REFERENCE-011'
    REQUIRED_BINDING_MISSING = 'MOD-REFERENCE-012'


@_dataclass(frozen=True, slots=True)
class SemanticReferenceDiagnostic:
    """Narrow actual diagnostic seam pending missing general SK-11."""
    code: SemanticReferenceFailure
    message: str
    request: SemanticReferenceResolutionRequest | None = None
    target_reference: ElementRef | ElementVersionRef | None = None
    namespace_diagnostic: NamespaceResolutionDiagnostic | None = None
    path: AuthoringSchemaPath | None = None

    def __post_init__(self) -> None:
        if type(self.code) is not SemanticReferenceFailure or type(self.message) is not str or not self.message:
            raise TypeError('Reference diagnostics require a known code and message.')
        if self.request is not None and type(self.request) is not SemanticReferenceResolutionRequest or self.namespace_diagnostic is not None and type(self.namespace_diagnostic) is not NamespaceResolutionDiagnostic:
            raise TypeError('Diagnostic request/delegated namespace failure must be typed.')
        if self.target_reference is not None:
            _resolution_reference(self.target_reference)
        _resolution_path(self.path)

    @property
    def severity(self) -> TypeValidationSeverity:
        return TypeValidationSeverity.ERROR

    @property
    def related_paths(self) -> tuple[AuthoringSchemaPath, ...]:
        return () if self.namespace_diagnostic is None else self.namespace_diagnostic.related_paths


@_dataclass(frozen=True, slots=True)
class SemanticReferenceResolutionResult:
    binding: ResolvedReferenceBinding | None
    diagnostics: tuple[SemanticReferenceDiagnostic, ...] = ()

    def __post_init__(self) -> None:
        object.__setattr__(self, 'diagnostics', _ordered(self.diagnostics, SemanticReferenceDiagnostic))
        if (self.binding is None) != bool(self.diagnostics) or self.binding is not None and type(self.binding) is not ResolvedReferenceBinding:
            raise ValueError('Reference result requires a verified binding or nonempty failure diagnostics.')

    @property
    def is_success(self) -> bool:
        return self.binding is not None


class ReferenceBatchStatus(_Enum):
    ALL_RESOLVED = 'all-resolved'
    PARTIALLY_RESOLVED = 'partially-resolved'
    NONE_RESOLVED = 'none-resolved'


@_dataclass(frozen=True, slots=True)
class SemanticReferenceBatchResult:
    results: tuple[SemanticReferenceResolutionResult, ...]

    def __post_init__(self) -> None:
        object.__setattr__(self, 'results', _ordered(self.results, SemanticReferenceResolutionResult))

    @property
    def status(self) -> ReferenceBatchStatus:
        successes = sum(r.is_success for r in self.results)
        if successes == len(self.results):
            return ReferenceBatchStatus.ALL_RESOLVED
        return ReferenceBatchStatus.PARTIALLY_RESOLVED if successes else ReferenceBatchStatus.NONE_RESOLVED

    @property
    def all_required_bindings_satisfied(self) -> bool:
        return self.status is ReferenceBatchStatus.ALL_RESOLVED

    @property
    def canonicalizer_compatible(self) -> bool:
        return self.all_required_bindings_satisfied and all(r.binding.requirement.consumer is ReferenceConsumer.SEMANTIC_TYPE_FIELD and type(r.binding.reference) is ElementRef for r in self.results)

    @property
    def diagnostics(self) -> tuple[SemanticReferenceDiagnostic, ...]:
        return tuple(d for result in self.results for d in result.diagnostics)


_NAMESPACE_REFERENCE_CODES = _MappingProxyType({
    NamespaceResolutionFailure.INVALID_EXPRESSION: SemanticReferenceFailure.INVALID_REQUEST,
    NamespaceResolutionFailure.INVALID_ENVIRONMENT: SemanticReferenceFailure.INVALID_ENVIRONMENT,
    NamespaceResolutionFailure.NAME_NOT_FOUND: SemanticReferenceFailure.TARGET_NOT_FOUND,
    NamespaceResolutionFailure.AMBIGUOUS_NAME: SemanticReferenceFailure.AMBIGUOUS_TARGET,
    NamespaceResolutionFailure.ALIAS_NOT_FOUND: SemanticReferenceFailure.INVALID_REQUEST,
    NamespaceResolutionFailure.ALIAS_COLLISION: SemanticReferenceFailure.INVALID_ENVIRONMENT,
    NamespaceResolutionFailure.CONTEXT_MISMATCH: SemanticReferenceFailure.CONTEXT_MISMATCH,
    NamespaceResolutionFailure.KIND_MISMATCH: SemanticReferenceFailure.KIND_MISMATCH,
    NamespaceResolutionFailure.VERSION_NOT_FOUND: SemanticReferenceFailure.EXACT_VERSION_NOT_FOUND,
    NamespaceResolutionFailure.SYMBOL_COLLISION: SemanticReferenceFailure.CONFLICTING_TARGET_EVIDENCE,
    NamespaceResolutionFailure.UNBOUND_LOOKUP_VERSION: SemanticReferenceFailure.INVALID_ENVIRONMENT,
    NamespaceResolutionFailure.INVALID_BINDING: SemanticReferenceFailure.INVALID_LOCAL_BINDING,
})


def _reference_failure(code: SemanticReferenceFailure, message: str, request: SemanticReferenceResolutionRequest | None = None, target: ElementRef | ElementVersionRef | None = None, path: AuthoringSchemaPath | None = None) -> SemanticReferenceResolutionResult:
    return SemanticReferenceResolutionResult(None, (SemanticReferenceDiagnostic(code, message, request, target, path=request.path if request is not None else path),))


def _reference_evidence_index(environment: NamespaceResolutionEnvironment) -> dict[SemanticElementId, tuple[ReferenceTargetEvidence, ...]]:
    groups: dict[SemanticElementId, list[ReferenceTargetEvidence]] = {}
    for symbols, origin in ((environment.local_symbols, ReferenceEvidenceOrigin.LOCAL_DECLARATION), (environment.visible_symbols, ReferenceEvidenceOrigin.VISIBLE_SYMBOL)):
        for symbol in symbols:
            groups.setdefault(symbol.reference.element_id, []).append(ReferenceTargetEvidence(symbol, origin))
    return {identity: tuple(sorted(set(items), key=_evidence_order)) for identity, items in groups.items()}


@_dataclass(frozen=True, slots=True)
class ResolvedAuthoringInputResult:
    resolved_model: ResolvedAuthoringModel | None
    references: SemanticReferenceBatchResult
    diagnostics: tuple[SemanticReferenceDiagnostic, ...] = ()

    def __post_init__(self) -> None:
        if type(self.references) is not SemanticReferenceBatchResult:
            raise TypeError('Authoring readiness requires the actual finite reference batch result.')
        object.__setattr__(self, 'diagnostics', _ordered(self.diagnostics, SemanticReferenceDiagnostic))
        if (self.resolved_model is None) != bool(self.diagnostics) or self.resolved_model is not None and type(self.resolved_model) is not ResolvedAuthoringModel:
            raise ValueError('Authoring input is complete or has failure diagnostics; no partial successful input.')
        if self.resolved_model is not None and not self.references.canonicalizer_compatible:
            raise ValueError('A complete authoring input cannot advertise unresolved/incompatible reference bindings.')
        reported = frozenset(self.diagnostics)
        if any(d not in reported for d in self.references.diagnostics):
            raise ValueError('Authoring readiness must preserve every batch failure diagnostic.')
        if self.resolved_model is not None:
            document = self.resolved_model.document
            declarations = {b.declaration_index: b for b in self.resolved_model.declarations}
            if len(declarations) != len(self.resolved_model.declarations) or set(declarations) != set(range(len(document.definitions))):
                raise ValueError('Ready authoring input must cover every declaration exactly once.')
            reference_index = 0
            for index, declaration in enumerate(document.definitions):
                bound = declarations[index]
                if bound.id != SemanticElementId.parse(declaration.id) or bound.version != SemanticVersion.parse(declaration.version) or bound.context != document.context or bound.qualified_name != QualifiedName.create(Namespace.parse(document.namespace), declaration.name):
                    raise ValueError('Ready authoring declaration bindings must preserve their authored coordinates.')
                fields = {(f.facet_index, f.field_index): f for f in bound.fields}
                required = {(a, b) for a, facet in enumerate(declaration.facets) for b in range(len(facet.fields))}
                if len(fields) != len(bound.fields) or set(fields) != required:
                    raise ValueError('Ready authoring input must cover every field exactly once.')
                for facet_index, facet in enumerate(declaration.facets):
                    for field_index, field in enumerate(facet.fields):
                        supplied = fields[(facet_index, field_index)]
                        if supplied.field_id != FieldId.parse(field.id):
                            raise ValueError('Ready authoring fields must retain their stable FieldIds.')
                        if type(field.type) is AuthoringPrimitiveExpression:
                            if supplied.target is not None:
                                raise ValueError('Primitive field bindings must bypass semantic target resolution.')
                            continue
                        if reference_index >= len(self.references.results):
                            raise ValueError('A required semantic occurrence is missing from the reference batch.')
                        verified = self.references.results[reference_index].binding
                        reference_index += 1
                        path = AuthoringSchemaPath(('definitions', index, 'facets', facet_index, 'fields', field_index, 'type'))
                        if verified.path != path or supplied.target != verified.reference or verified.context != document.context:
                            raise ValueError('Each ready semantic field must match its exact verified source occurrence.')
                        if type(field.type) is AuthoringVersionExpression or type(field.type) is AuthoringIdentityExpression and field.type.reference != verified.reference:
                            raise ValueError('Ready semantic fields cannot discard an authored identity or exact version pin.')
            if reference_index != len(self.references.results):
                raise ValueError('Ready authoring input cannot contain unrelated extra reference results.')

    @property
    def ready_for_canonicalization(self) -> bool:
        return self.resolved_model is not None


@_dataclass(frozen=True, slots=True)
class SemanticReferenceResolver:
    namespace_resolver: NamespaceResolver = _dataclass_field(default_factory=NamespaceResolver)

    def __post_init__(self) -> None:
        if type(self.namespace_resolver) is not NamespaceResolver:
            raise TypeError('Reference resolution delegates to the actual stateless MOD-06 service.')

    def resolve(self, request: SemanticReferenceResolutionRequest, environment: NamespaceResolutionEnvironment) -> SemanticReferenceResolutionResult:
        evidence = _reference_evidence_index(environment) if type(environment) is NamespaceResolutionEnvironment else {}
        return self._resolve(request, environment, evidence)

    def _resolve(self, request: SemanticReferenceResolutionRequest, environment: NamespaceResolutionEnvironment, evidence_index: _Mapping[SemanticElementId, tuple[ReferenceTargetEvidence, ...]]) -> SemanticReferenceResolutionResult:
        if type(request) is not SemanticReferenceResolutionRequest:
            return _reference_failure(SemanticReferenceFailure.INVALID_REQUEST, 'Supply a typed semantic reference request; primitive and instance references are outside this operation.')
        if type(environment) is not NamespaceResolutionEnvironment:
            return _reference_failure(SemanticReferenceFailure.INVALID_ENVIRONMENT, 'Supply the existing immutable MOD-06 visibility environment.', request)
        requirement = request.requirement
        has_pin = request.exact_version is not None or type(request.expression) is AuthoringVersionExpression
        if requirement.version_requirement is ReferenceVersionRequirement.IDENTITY_ONLY and has_pin:
            return _reference_failure(SemanticReferenceFailure.UNSUPPORTED_REFERENCE_FORM, 'An authored/requested exact pin cannot be represented by an identity-only requirement.', request)
        if requirement.version_requirement is ReferenceVersionRequirement.EXACT_VERSION and not has_pin:
            return _reference_failure(SemanticReferenceFailure.REQUIRED_VERSION_MISSING, 'Exact reference requirement needs an explicit request or authored version.', request)
        named = self.namespace_resolver.resolve(NamespaceResolutionRequest(request.expression, request.context, requirement.expected_kind, request.exact_version, request.path), environment)
        if not named.is_success:
            diagnostics = tuple(SemanticReferenceDiagnostic(_NAMESPACE_REFERENCE_CODES[d.code], d.message, request, namespace_diagnostic=d, path=d.path) for d in named.diagnostics)
            return SemanticReferenceResolutionResult(None, diagnostics)
        target = named.target
        matched_names = frozenset(target.qualified_names)
        items = tuple(item for item in evidence_index.get(target.reference.element_id, ()) if item.symbol.context == target.context and item.symbol.kind == requirement.expected_kind and item.symbol.qualified_name in matched_names and (type(target.reference) is ElementRef or item.symbol.reference.version == target.reference.version))
        if not items:
            return _reference_failure(SemanticReferenceFailure.CONFLICTING_TARGET_EVIDENCE, 'Namespace target has no matching declared/visible evidence under this snapshot.', request, target.reference)
        if requirement.consumer is ReferenceConsumer.SEMANTIC_TYPE_FIELD and type(target.reference) is ElementVersionRef:
            return _reference_failure(SemanticReferenceFailure.UNSUPPORTED_REFERENCE_FORM, 'Current TYPE-05 SemanticTypeRef accepts only ElementRef; the verified exact pin cannot be downgraded.', request, target.reference)
        return SemanticReferenceResolutionResult(ResolvedReferenceBinding(target.reference, target.context, requirement, items, request.path))

    def resolve_many(self, requests: tuple[SemanticReferenceResolutionRequest, ...], environment: NamespaceResolutionEnvironment) -> SemanticReferenceBatchResult:
        requests = _ordered(requests, SemanticReferenceResolutionRequest)
        evidence = _reference_evidence_index(environment) if type(environment) is NamespaceResolutionEnvironment else {}
        return SemanticReferenceBatchResult(tuple(self._resolve(request, environment, evidence) for request in requests))

    def resolve_document(self, document: AuthoringModelDocument, environment: NamespaceResolutionEnvironment, *, retain_source_associations: bool = True) -> ResolvedAuthoringInputResult:
        """Complete existing MOD-05 input, never a canonical model.

        Environment must explicitly predeclare this document's local coordinates.
        Primitive fields bypass resolution. Required semantic fields are collected
        in source order; any failure blocks complete authoring-input readiness.
        """
        empty = SemanticReferenceBatchResult(())
        if type(retain_source_associations) is not bool:
            raise TypeError('Source association intent must be an explicit boolean.')
        if type(document) is not AuthoringModelDocument or document.schema_version != AUTHORING_SCHEMA_VERSION:
            failure = _reference_failure(SemanticReferenceFailure.INVALID_REQUEST, 'Supply one existing supported immutable authoring document.')
            return ResolvedAuthoringInputResult(None, empty, failure.diagnostics)
        if type(environment) is not NamespaceResolutionEnvironment:
            failure = _reference_failure(SemanticReferenceFailure.INVALID_ENVIRONMENT, 'Document reference binding requires an explicit namespace environment.')
            return ResolvedAuthoringInputResult(None, empty, failure.diagnostics)
        if document.context != environment.context or Namespace.parse(document.namespace) != environment.current_namespace:
            failure = _reference_failure(SemanticReferenceFailure.CONTEXT_MISMATCH, 'Document context/current namespace must agree with the explicit environment.', path=AuthoringSchemaPath(()))
            return ResolvedAuthoringInputResult(None, empty, failure.diagnostics)
        local_coordinates = {(s.reference, s.qualified_name, s.kind) for s in environment.local_symbols}
        namespace = Namespace.parse(document.namespace)
        declarations = []
        diagnostics: list[SemanticReferenceDiagnostic] = []
        requests: list[SemanticReferenceResolutionRequest] = []
        occurrences: list[tuple[int, int, int, FieldId]] = []
        fields: dict[tuple[int, int, int], ResolvedFieldBinding] = {}
        for index, declaration in enumerate(document.definitions):
            identity = SemanticElementId.parse(declaration.id)
            version = SemanticVersion.parse(declaration.version)
            name = QualifiedName.create(namespace, declaration.name)
            reference = ElementVersionRef(identity, version)
            if (reference, name, SemanticElementKinds.TYPE_DEFINITION) not in local_coordinates:
                diagnostics.append(SemanticReferenceDiagnostic(SemanticReferenceFailure.INVALID_LOCAL_BINDING, 'Document declaration lacks matching explicit local identity/name/kind/version evidence.', target_reference=reference, path=AuthoringSchemaPath(('definitions', index))))
            declarations.append((identity, version, name))
            for facet_index, facet in enumerate(declaration.facets):
                for field_index, field in enumerate(facet.fields):
                    key = (index, facet_index, field_index)
                    field_id = FieldId.parse(field.id)
                    if type(field.type) is AuthoringPrimitiveExpression:
                        fields[key] = ResolvedFieldBinding(facet_index, field_index, field_id)
                        continue
                    mode = ReferenceVersionRequirement.EXACT_VERSION if type(field.type) is AuthoringVersionExpression else ReferenceVersionRequirement.IDENTITY_ONLY
                    requirement = SemanticReferenceRequirement(SemanticElementKinds.TYPE_DEFINITION, mode, ReferenceConsumer.SEMANTIC_TYPE_FIELD)
                    requests.append(SemanticReferenceResolutionRequest(field.type, document.context, requirement, path=AuthoringSchemaPath(('definitions', index, 'facets', facet_index, 'fields', field_index, 'type'))))
                    occurrences.append((*key, field_id))
        batch = self.resolve_many(requests, environment)
        diagnostics.extend(batch.diagnostics)
        for occurrence, result in zip(occurrences, batch.results):
            if result.is_success:
                declaration_index, facet_index, field_index, field_id = occurrence
                fields[(declaration_index, facet_index, field_index)] = ResolvedFieldBinding(facet_index, field_index, field_id, result.binding.reference)
        if diagnostics:
            return ResolvedAuthoringInputResult(None, batch, diagnostics)
        bindings: list[ResolvedTypeBinding] = []
        for index, (identity, version, name) in enumerate(declarations):
            members = tuple(fields[(index, facet_index, field_index)] for facet_index, facet in enumerate(document.definitions[index].facets) for field_index in range(len(facet.fields)))
            bindings.append(ResolvedTypeBinding(index, identity, name, document.context, version, members))
        return ResolvedAuthoringInputResult(ResolvedAuthoringModel(document, bindings, retain_source_associations), batch)


__all__ += [
    'ReferenceVersionRequirement', 'ReferenceConsumer', 'SemanticReferenceRequirement',
    'SemanticReferenceResolutionRequest', 'ReferenceEvidenceOrigin',
    'ReferenceTargetEvidence', 'ResolvedReferenceBinding', 'SemanticReferenceFailure',
    'SemanticReferenceDiagnostic', 'SemanticReferenceResolutionResult',
    'ReferenceBatchStatus', 'SemanticReferenceBatchResult', 'ResolvedAuthoringInputResult',
    'SemanticReferenceResolver',
]


# MOD-08: orchestration only. Original validator diagnostics remain unchanged.
class ModelValidationStatus(_Enum):
    VALID = 'valid'
    INVALID = 'invalid'
    INCOMPLETE = 'incomplete'


class CompilationReadiness(_Enum):
    READY = 'ready'
    NOT_READY = 'not-ready'


class ValidationStageStatus(_Enum):
    COMPLETED = 'completed'
    BLOCKED = 'blocked'
    INCOMPLETE = 'incomplete'
    SKIPPED = 'skipped'


class ValidationWarningPolicy(_Enum):
    ALLOW = 'allow'
    BLOCK = 'block'


class ModelValidationFailure(_Enum):
    CONTEXT_MISMATCH = 'MOD-VALIDATION-001'
    LOOKUP_UNAVAILABLE = 'MOD-VALIDATION-002'
    LOOKUP_AMBIGUOUS = 'MOD-VALIDATION-003'
    LOOKUP_SNAPSHOT_MISMATCH = 'MOD-VALIDATION-004'
    LOOKUP_CONTEXT_MISMATCH = 'MOD-VALIDATION-005'


@_dataclass(frozen=True, slots=True)
class ModelValidationDiagnostic:
    """Only orchestration failures, pending SK-11; TYPE-06 is never translated."""
    code: ModelValidationFailure
    message: str
    reference: ElementRef | ElementVersionRef | None = None
    cause_code: str | None = None

    def __post_init__(self) -> None:
        if type(self.code) is not ModelValidationFailure or type(self.message) is not str or not self.message:
            raise TypeError('Pipeline failures require a supported orchestration code and message.')
        if self.reference is not None:
            _resolution_reference(self.reference)
        if self.cause_code is not None and type(self.cause_code) is not str:
            raise TypeError('Delegated failure code must be text.')

    @property
    def severity(self) -> TypeValidationSeverity:
        return TypeValidationSeverity.WARNING if self.code in (ModelValidationFailure.LOOKUP_UNAVAILABLE, ModelValidationFailure.LOOKUP_AMBIGUOUS) else TypeValidationSeverity.ERROR


@_dataclass(frozen=True, slots=True)
class ModelValidationContext:
    scope: SemanticContextRef
    type_lookup: TypeLookup | None
    warning_policy: ValidationWarningPolicy = ValidationWarningPolicy.ALLOW

    def __post_init__(self) -> None:
        if type(self.scope) is not SemanticContextRef or type(self.scope.context_id) is not SemanticElementId:
            raise TypeError('Validation scope requires an explicit canonical semantic context.')
        if self.type_lookup is not None and not callable(getattr(self.type_lookup, 'find', None)):
            raise TypeError('Validation lookup must implement the existing read-only TypeLookup port.')
        if type(self.warning_policy) is not ValidationWarningPolicy:
            raise TypeError('Warning readiness policy must be explicit and typed.')


@_dataclass(frozen=True, slots=True)
class ModelValidationRequest:
    model: CanonicalModel
    context: ModelValidationContext
    source_associations: tuple[CanonicalSourceAssociation, ...] = ()
    _source_paths: _Mapping[CanonicalSourceTarget, AuthoringSchemaPath] = _dataclass_field(init=False, repr=False, compare=False, hash=False)

    def __post_init__(self) -> None:
        if type(self.model) is not CanonicalModel or type(self.context) is not ModelValidationContext:
            raise TypeError('Canonical validation requires MOD-04 model and explicit validation context.')
        associations = _ordered(self.source_associations, CanonicalSourceAssociation)
        paths = {}
        owned_fields = {ElementVersionRef(d.type_definition.id, d.type_definition.version): frozenset(f.id for f in d.data.fields) if d.data is not None else frozenset() for d in self.model.definitions}
        for association in associations:
            member = self.model.find(association.target.definition)
            if member is None or association.target.field_id is not None and association.target.field_id not in owned_fields[association.target.definition]:
                raise ValueError('Source association must identify an actual exact model member/owned field.')
            if association.target in paths:
                raise ValueError('Each semantic source target must have one explicit association.')
            paths[association.target] = association.path
        object.__setattr__(self, 'source_associations', associations)
        object.__setattr__(self, '_source_paths', _MappingProxyType(paths))

    def source_path(self, definition: ElementVersionRef | None, field_id: FieldId | None = None) -> AuthoringSchemaPath | None:
        if definition is None:
            return None
        path = self._source_paths.get(CanonicalSourceTarget(definition, field_id))
        return path if path is not None else self._source_paths.get(CanonicalSourceTarget(definition))


@_dataclass(frozen=True, slots=True)
class ModelValidationReport:
    """Provenance envelope; retain the whole original diagnostic, not a new code."""
    stage_id: str
    diagnostic: TypeValidationDiagnostic | ModelValidationDiagnostic
    definition: ElementVersionRef | None = None
    source_path: AuthoringSchemaPath | None = None

    def __post_init__(self) -> None:
        _validation_stage_id(self.stage_id)
        if type(self.diagnostic) not in (TypeValidationDiagnostic, ModelValidationDiagnostic):
            raise TypeError('Reports retain actual validator or narrow orchestration diagnostics.')
        if self.definition is not None and type(self.definition) is not ElementVersionRef:
            raise TypeError('Diagnostic owner requires an exact member reference.')
        if self.source_path is not None and type(self.source_path) is not AuthoringSchemaPath:
            raise TypeError('Source report coordinate must be an actual supplied association path.')

    @property
    def severity(self) -> TypeValidationSeverity:
        return self.diagnostic.severity


def _validation_stage_id(value: str) -> None:
    if type(value) is not str or not value.startswith('MOD-STAGE-') or not value[10:] or any(c not in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-' for c in value[10:]):
        raise ValueError('Validation stages require stable MOD-STAGE identifiers.')


@_dataclass(frozen=True, slots=True)
class ModelValidationStageResult:
    stage_id: str
    status: ValidationStageStatus
    diagnostics: tuple[ModelValidationReport, ...] = ()
    reason: str | None = None

    def __post_init__(self) -> None:
        _validation_stage_id(self.stage_id)
        if type(self.status) is not ValidationStageStatus:
            raise TypeError('Stage status must be explicit.')
        object.__setattr__(self, 'diagnostics', _ordered(self.diagnostics, ModelValidationReport))
        if any(d.stage_id != self.stage_id for d in self.diagnostics):
            raise ValueError('Stage results cannot relabel another stage diagnostic.')
        if self.status is not ValidationStageStatus.COMPLETED and (type(self.reason) is not str or not self.reason):
            raise ValueError('Blocked/incomplete/skipped stages require an explicit reason.')
        if self.status is ValidationStageStatus.SKIPPED and self.diagnostics:
            raise ValueError('Skipped stages cannot claim executed validator diagnostics.')
        if self.reason is not None and (type(self.reason) is not str or not self.reason):
            raise TypeError('Stage reason must be nonempty text when supplied.')


class ModelValidationStage(_Protocol):
    @property
    def id(self) -> str:
        ...

    def validate(self, request: ModelValidationRequest) -> ModelValidationStageResult:
        ...


@_dataclass(frozen=True, slots=True)
class CanonicalIntegrityValidationStage:
    id: str = _dataclass_field(default='MOD-STAGE-CANONICAL-INTEGRITY', init=False)

    def validate(self, request: ModelValidationRequest) -> ModelValidationStageResult:
        if type(request) is not ModelValidationRequest:
            raise TypeError('Integrity stage requires the actual canonical validation request.')
        # MOD-04 already proves immutable membership/kind/exact/scope invariants.
        if request.model.scope != request.context.scope:
            diagnostic = ModelValidationDiagnostic(ModelValidationFailure.CONTEXT_MISMATCH, 'Explicit validation scope differs from the canonical model scope.')
            return ModelValidationStageResult(self.id, ValidationStageStatus.BLOCKED, (ModelValidationReport(self.id, diagnostic),), 'Invalid stage scope prevents safe semantic validation.')
        return ModelValidationStageResult(self.id, ValidationStageStatus.COMPLETED)


@_dataclass(frozen=True, slots=True)
class _ValidationLookupTarget:
    id: SemanticElementId
    qualified_name: QualifiedName
    context: SemanticContextRef
    kind: SemanticElementKind
    version: SemanticVersion


@_dataclass(frozen=True, slots=True)
class _ValidationLookupSnapshot:
    targets: _Mapping[SemanticElementId, _ValidationLookupTarget | None]

    def __post_init__(self) -> None:
        object.__setattr__(self, 'targets', _MappingProxyType(dict(self.targets)))

    def find(self, reference: ElementRef) -> _ValidationLookupTarget | None:
        if type(reference) is not ElementRef:
            raise TypeError('Validation snapshot accepts actual identity-only TypeLookup references.')
        if reference.element_id not in self.targets:
            raise ValueError('Validator requested an identity outside the finite declared validation snapshot.')
        return self.targets[reference.element_id]


@_dataclass(frozen=True, slots=True)
class TypeSemanticValidationStage:
    """TYPE-06 full validation includes approved references, exactly once/member."""
    validator: TypeValidator = _dataclass_field(default_factory=TypeValidator)
    id: str = _dataclass_field(default='MOD-STAGE-TYPE-SEMANTIC', init=False)

    def __post_init__(self) -> None:
        if type(self.validator) is not TypeValidator:
            raise TypeError('Type semantic stage requires the existing full TYPE-06 validator.')

    def validate(self, request: ModelValidationRequest) -> ModelValidationStageResult:
        if type(request) is not ModelValidationRequest:
            raise TypeError('Semantic stage requires the actual canonical validation request.')
        if request.model.scope != request.context.scope:
            d = ModelValidationDiagnostic(ModelValidationFailure.CONTEXT_MISMATCH, 'Canonical and validation scopes disagree; semantic prerequisites are invalid.')
            return ModelValidationStageResult(self.id, ValidationStageStatus.BLOCKED, (ModelValidationReport(self.id, d),), 'Explicit scope must match before lookup or TYPE-06 validation.')
        lookup = request.context.type_lookup
        if lookup is None:
            d = ModelValidationDiagnostic(ModelValidationFailure.LOOKUP_UNAVAILABLE, 'Required stable TypeLookup is unavailable; missing infrastructure does not establish missing targets.')
            return ModelValidationStageResult(self.id, ValidationStageStatus.INCOMPLETE, (ModelValidationReport(self.id, d),), 'TYPE-06 requires an explicit lookup even for primitive-only models.')
        identities = {d.type_definition.id for d in request.model.definitions}
        for definition in request.model.definitions:
            if definition.data is not None:
                identities.update(f.type.target.element_id for f in definition.data.fields if type(f.type) is SemanticTypeRef)
        targets: dict[SemanticElementId, _ValidationLookupTarget | None] = {}
        reports = []
        for identity in sorted(identities, key=lambda i: i.value):
            reference = ElementRef(identity)
            try:
                host = lookup.find(reference)
            except TypeRegistryAmbiguityError as error:
                d = ModelValidationDiagnostic(ModelValidationFailure.LOOKUP_AMBIGUOUS, 'Lookup has no explicit version binding; validation never selects latest.', reference, error.code)
                reports.append(ModelValidationReport(self.id, d))
                continue
            if host is None:
                targets[identity] = None
                continue
            values = tuple(getattr(host, name, None) for name in ('id', 'qualified_name', 'context', 'kind', 'version'))
            expected = (SemanticElementId, QualifiedName, SemanticContextRef, SemanticElementKind, SemanticVersion)
            if any(type(v) is not t for v, t in zip(values, expected)) or type(values[1].namespace) is not Namespace or type(values[2].context_id) is not SemanticElementId:
                raise TypeError('TypeLookup violated its typed SemanticElement contract; this is an infrastructure/programming defect.')
            target = _ValidationLookupTarget(*values)
            targets[identity] = target
            if target.id != identity or target.context != request.context.scope:
                code = ModelValidationFailure.LOOKUP_SNAPSHOT_MISMATCH if target.id != identity else ModelValidationFailure.LOOKUP_CONTEXT_MISMATCH
                d = ModelValidationDiagnostic(code, 'Lookup target identity/context disagrees with the requested semantic scope.', reference)
                reports.append(ModelValidationReport(self.id, d))
        # Compare selected five-value metadata, not absent facet content on TypeLookup.
        checked = set()
        for definition in request.model.definitions:
            owner = definition.type_definition
            if owner.id in checked or owner.id not in targets:
                continue
            checked.add(owner.id)
            target = targets[owner.id]
            exact = None if target is None else ElementVersionRef(target.id, target.version)
            member = None if exact is None else request.model.find(exact)
            if member is None or target != _ValidationLookupTarget(member.type_definition.id, member.type_definition.qualified_name, member.type_definition.context, member.type_definition.kind, member.type_definition.version):
                subject = ElementVersionRef(owner.id, owner.version)
                d = ModelValidationDiagnostic(ModelValidationFailure.LOOKUP_SNAPSHOT_MISMATCH, 'Canonical identity must be explicitly visible at a matching selected version/name/kind/context; no local fallback or implicit selection.', ElementRef(owner.id))
                reports.append(ModelValidationReport(self.id, d, subject, request.source_path(subject)))
        if reports:
            status = ValidationStageStatus.BLOCKED if any(r.severity is TypeValidationSeverity.ERROR for r in reports) else ValidationStageStatus.INCOMPLETE
            return ModelValidationStageResult(self.id, status, reports, 'Lookup evidence is inconsistent or unavailable; TYPE-06 prerequisites are unsafe.')
        context = TypeValidationContext(_ValidationLookupSnapshot(targets))
        for definition in request.model.definitions:
            owner = definition.type_definition
            subject = ElementVersionRef(owner.id, owner.version)
            result = self.validator.validate(definition, context)
            reports.extend(ModelValidationReport(self.id, d, subject, request.source_path(subject, d.field_id)) for d in result.diagnostics)
        return ModelValidationStageResult(self.id, ValidationStageStatus.COMPLETED, reports)


_MANDATORY_VALIDATION_STAGES = ('MOD-STAGE-CANONICAL-INTEGRITY', 'MOD-STAGE-TYPE-SEMANTIC')


@_dataclass(frozen=True, slots=True)
class ModelValidationResult:
    stage_outcomes: tuple[ModelValidationStageResult, ...]
    warning_policy: ValidationWarningPolicy = ValidationWarningPolicy.ALLOW
    validated_model: CanonicalModel | None = _dataclass_field(default=None, repr=False, compare=False, hash=False)

    def __post_init__(self) -> None:
        if self.validated_model is not None and type(self.validated_model) is not CanonicalModel:
            raise TypeError('Validation binding must retain the exact canonical input object.')
        object.__setattr__(self, 'stage_outcomes', _ordered(self.stage_outcomes, ModelValidationStageResult))
        ids = tuple(s.stage_id for s in self.stage_outcomes)
        if ids[:2] != _MANDATORY_VALIDATION_STAGES or len(set(ids)) != len(ids):
            raise ValueError('Results must report every mandatory core stage in order, without duplicates.')
        if type(self.warning_policy) is not ValidationWarningPolicy:
            raise TypeError('Result warning policy must be explicit.')

    @property
    def diagnostics(self) -> tuple[ModelValidationReport, ...]:
        return tuple(d for stage in self.stage_outcomes for d in stage.diagnostics)

    @property
    def status(self) -> ModelValidationStatus:
        if any(d.severity is TypeValidationSeverity.ERROR for d in self.diagnostics):
            return ModelValidationStatus.INVALID
        if any(s.status is not ValidationStageStatus.COMPLETED for s in self.stage_outcomes):
            return ModelValidationStatus.INCOMPLETE
        if self.warning_policy is ValidationWarningPolicy.BLOCK and any(d.severity is TypeValidationSeverity.WARNING for d in self.diagnostics):
            return ModelValidationStatus.INVALID
        return ModelValidationStatus.VALID

    @property
    def readiness(self) -> CompilationReadiness:
        return CompilationReadiness.READY if self.status is ModelValidationStatus.VALID else CompilationReadiness.NOT_READY


@_dataclass(frozen=True, slots=True)
class ModelValidationPipeline:
    type_stage: TypeSemanticValidationStage = _dataclass_field(default_factory=TypeSemanticValidationStage)
    additional_stages: tuple[ModelValidationStage, ...] = ()

    def __post_init__(self) -> None:
        if type(self.type_stage) is not TypeSemanticValidationStage:
            raise TypeError('Pipeline requires its mandatory full type stage.')
        if type(self.additional_stages) not in (tuple, list):
            raise TypeError('Extra stages require an explicit finite ordered sequence.')
        stages = tuple(self.additional_stages)
        ids = set(_MANDATORY_VALIDATION_STAGES)
        for stage in stages:
            _validation_stage_id(getattr(stage, 'id', None))
            if not callable(getattr(stage, 'validate', None)):
                raise TypeError('Stage must implement the explicit validate protocol.')
            if stage.id in ids:
                raise ValueError('Stage IDs cannot duplicate/replace mandatory stages.')
            ids.add(stage.id)
        object.__setattr__(self, 'additional_stages', stages)

    @property
    def stages(self) -> tuple[ModelValidationStage, ...]:
        return (CanonicalIntegrityValidationStage(), self.type_stage, *self.additional_stages)

    def validate(self, request: ModelValidationRequest) -> ModelValidationResult:
        if type(request) is not ModelValidationRequest:
            raise TypeError('Pipeline consumes only the explicit canonical validation request.')
        outcomes = []
        blocker = None
        for stage in self.stages:
            if blocker is not None:
                outcomes.append(ModelValidationStageResult(stage.id, ValidationStageStatus.SKIPPED, reason='Prerequisite stage ' + blocker + ' could not safely complete.'))
                continue
            outcome = stage.validate(request)
            if type(outcome) is not ModelValidationStageResult or outcome.stage_id != stage.id:
                raise TypeError('Stage implementation violated its declared result contract.')
            outcomes.append(outcome)
            if outcome.status is not ValidationStageStatus.COMPLETED:
                blocker = stage.id
        return ModelValidationResult(outcomes, request.context.warning_policy, request.model)


__all__ += [
    'ModelValidationStatus', 'CompilationReadiness', 'ValidationStageStatus',
    'ValidationWarningPolicy', 'ModelValidationFailure', 'ModelValidationDiagnostic',
    'ModelValidationContext', 'ModelValidationRequest', 'ModelValidationReport',
    'ModelValidationStage', 'ModelValidationStageResult', 'ModelValidationResult',
    'CanonicalIntegrityValidationStage', 'TypeSemanticValidationStage', 'ModelValidationPipeline',
]


# MOD-09 associates existing judgments; no validator or source tooling execution.
class ModelDiagnosticOrigin(_Enum):
    AUTHORING_SCHEMA = 'authoring-schema'
    MODEL_LOADER = 'model-loader'
    NAMESPACE_RESOLVER = 'namespace-resolver'
    REFERENCE_RESOLVER = 'reference-resolver'
    CANONICALIZER = 'canonicalizer'
    CANONICAL_CONSTRUCTION = 'canonical-construction'
    TYPE_VALIDATOR = 'type-validator'
    MODEL_VALIDATION_PIPELINE = 'model-validation-pipeline'
    COMPILER = 'compiler'


class ModelDiagnosticTargetKind(_Enum):
    DEFINITION = 'definition'
    FIELD = 'field'
    REFERENCE = 'reference'


@_dataclass(frozen=True, slots=True)
class ModelDiagnosticTarget:
    kind: ModelDiagnosticTargetKind
    reference: ElementRef | ElementVersionRef
    field_id: FieldId | None = None

    def __post_init__(self) -> None:
        if type(self.kind) is not ModelDiagnosticTargetKind:
            raise TypeError('Diagnostic target kind must be explicit.')
        _resolution_reference(self.reference)
        if (self.kind is ModelDiagnosticTargetKind.FIELD) != (self.field_id is not None):
            raise ValueError('Only field targets carry an existing owned FieldId.')
        if self.field_id is not None and type(self.field_id) is not FieldId:
            raise TypeError('Field identity is FieldId, never SemanticElementId.')

    @property
    def exact_version(self) -> str | None:
        return str(self.reference.version) if type(self.reference) is ElementVersionRef else None


class ModelDiagnosticExtension(_Protocol):
    """Explicit compiler diagnostic presentation seam; no producer discovery.

    Implementations are immutable pure values. This is not full missing SK-11.
    """
    @property
    def code(self) -> str | _Enum:
        ...

    @property
    def message(self) -> str:
        ...

    @property
    def severity(self) -> TypeValidationSeverity:
        ...

    @property
    def phase_id(self) -> str | None:
        ...

    @property
    def cause_code(self) -> str | None:
        ...


ModelDiagnosticPayload = ModelDiagnosticExtension | AuthoringSchemaDiagnostic | CanonicalConstructionDiagnostic | CanonicalizationDiagnostic | NamespaceResolutionDiagnostic | SemanticReferenceDiagnostic | TypeValidationDiagnostic | ModelValidationDiagnostic
_DIAGNOSTIC_ORIGINS = _MappingProxyType({
    AuthoringSchemaDiagnostic: ModelDiagnosticOrigin.AUTHORING_SCHEMA,
    CanonicalConstructionDiagnostic: ModelDiagnosticOrigin.CANONICAL_CONSTRUCTION,
    CanonicalizationDiagnostic: ModelDiagnosticOrigin.CANONICALIZER,
    NamespaceResolutionDiagnostic: ModelDiagnosticOrigin.NAMESPACE_RESOLVER,
    SemanticReferenceDiagnostic: ModelDiagnosticOrigin.REFERENCE_RESOLVER,
    TypeValidationDiagnostic: ModelDiagnosticOrigin.TYPE_VALIDATOR,
    ModelValidationDiagnostic: ModelDiagnosticOrigin.MODEL_VALIDATION_PIPELINE,
})


@_dataclass(frozen=True, slots=True)
class ModelDiagnosticContext:
    semantic_context: SemanticContextRef | None = None
    source_associations: tuple[CanonicalSourceAssociation, ...] = ()
    _paths: _Mapping[CanonicalSourceTarget, tuple[AuthoringSchemaPath, ...]] = _dataclass_field(init=False, repr=False, compare=False, hash=False)

    def __post_init__(self) -> None:
        if self.semantic_context is not None and (type(self.semantic_context) is not SemanticContextRef or type(self.semantic_context.context_id) is not SemanticElementId):
            raise TypeError('Optional diagnostic scope must be an actual semantic context.')
        associations = _ordered(self.source_associations, CanonicalSourceAssociation)
        groups = {}
        for association in associations:
            groups.setdefault(association.target, []).append(association.path)
        object.__setattr__(self, 'source_associations', associations)
        object.__setattr__(self, '_paths', _MappingProxyType({target: tuple(dict.fromkeys(paths)) for target, paths in groups.items()}))

    def source_path(self, target: ModelDiagnosticTarget | None) -> AuthoringSchemaPath | None:
        if target is None or type(target.reference) is not ElementVersionRef or target.kind is ModelDiagnosticTargetKind.REFERENCE:
            return None
        key = CanonicalSourceTarget(target.reference, target.field_id)
        paths = self._paths.get(key)
        if paths is None and target.field_id is not None:
            paths = self._paths.get(CanonicalSourceTarget(target.reference))
        # Multiple explicit distinct associations are unavailable, never first-match.
        return paths[0] if paths is not None and len(paths) == 1 else None


class CompilationDiagnosticOrigin(_Enum):
    PREREQUISITE = 'compilation-prerequisite'
    ORCHESTRATOR = 'compiler-orchestrator'
    PHASE = 'compiler-phase'
    ARTIFACT_CONSTRUCTION = 'artifact-construction'
    ARTIFACT_COLLECTION = 'artifact-collection'
    RESULT = 'compilation-result'


@_dataclass(frozen=True, slots=True)
class CompilationArtifactDiagnosticView:
    """Transport projection of existing artifact tokens, not an artifact identity type."""
    key: str | None = None
    kind: str | None = None
    target: str | None = None

    def __post_init__(self) -> None:
        for value, pattern, limit in ((self.key, r'[a-z][a-z0-9]*(?:[.-][a-z0-9]+)*', 160), (self.kind, r'[a-z][a-z0-9]*(?:-[a-z0-9]+)*', 80), (self.target, r'[a-z][a-z0-9]*(?:-[a-z0-9]+)*', 80)):
            if value is not None and (type(value) is not str or len(value) > limit or _re.fullmatch(pattern, value) is None):
                raise ValueError('Artifact diagnostic projection requires original bounded logical tokens.')
        if self.key is None and self.kind is None and self.target is None:
            raise ValueError('Artifact association needs a key, kind or explicit intended target.')


@_dataclass(frozen=True, slots=True)
class CompilationDiagnosticDetails:
    """MOD-09 presentation seam; compiler owns association and result semantics."""
    origin: CompilationDiagnosticOrigin
    phase_id: str | None = None
    artifact: CompilationArtifactDiagnosticView | None = None
    semantic_context: SemanticContextRef | None = None
    ir_identity: str | None = None

    def __post_init__(self) -> None:
        if self.ir_identity is not None and (type(self.ir_identity) is not str or len(self.ir_identity) > 160 or _re.fullmatch(r'ir-[a-z][a-z0-9]*(?:[.-][a-z0-9]+)*', self.ir_identity) is None):
            raise ValueError('IR presentation retains an actual bounded representation token.')
        if type(self.origin) is not CompilationDiagnosticOrigin:
            raise TypeError('Compiler responsibility must be explicit.')
        if self.phase_id is not None and (type(self.phase_id) is not str or _re.fullmatch(r'CMP-PHASE-[A-Z0-9]+(?:-[A-Z0-9]+)*', self.phase_id) is None):
            raise ValueError('Use the existing compiler phase identifier.')
        if self.origin in (CompilationDiagnosticOrigin.PHASE, CompilationDiagnosticOrigin.ARTIFACT_CONSTRUCTION) and self.phase_id is None:
            raise ValueError('Executed phase responsibility requires a phase association.')
        if self.origin is CompilationDiagnosticOrigin.PREREQUISITE and self.phase_id is not None:
            raise ValueError('Prerequisite gate is not an executed phase.')
        if self.artifact is not None and type(self.artifact) is not CompilationArtifactDiagnosticView:
            raise TypeError('Artifact presentation is a typed projection.')
        if self.semantic_context is not None and (type(self.semantic_context) is not SemanticContextRef or type(self.semantic_context.context_id) is not SemanticElementId):
            raise TypeError('Scope association requires an existing semantic context.')


@_dataclass(frozen=True, slots=True)
class ModelDiagnosticEntry:
    diagnostic: ModelDiagnosticPayload
    target: ModelDiagnosticTarget | None = None
    related_targets: tuple[ModelDiagnosticTarget, ...] = ()
    source_path: AuthoringSchemaPath | None = None
    related_paths: tuple[AuthoringSchemaPath, ...] = ()
    validation_report: ModelValidationReport | None = None
    extension_origin: ModelDiagnosticOrigin | None = None
    compilation_details: CompilationDiagnosticDetails | None = None

    def __post_init__(self) -> None:
        if type(self.diagnostic) not in _DIAGNOSTIC_ORIGINS:
            if self.extension_origin is not ModelDiagnosticOrigin.COMPILER:
                raise TypeError('Unknown diagnostic requires the explicit compiler presentation extension, not origin guessing.')
            d = self.diagnostic
            if not _is_dataclass(d) or isinstance(d, type) or not d.__dataclass_params__.frozen:
                raise TypeError('Compiler diagnostic extension must be an immutable value implementation.')
            if not isinstance(d.code, (str, _Enum)) or type(d.message) is not str or not d.message or type(d.severity) is not TypeValidationSeverity:
                raise TypeError('Compiler presentation must expose the existing typed diagnostic scalar contract.')
            if d.phase_id is not None and (type(d.phase_id) is not str or not d.phase_id.startswith('CMP-PHASE-')) or d.cause_code is not None and (type(d.cause_code) is not str or not d.cause_code):
                raise TypeError('Compiler presentation must retain explicit optional phase/cause identifiers.')
        elif self.extension_origin is not None:
            raise ValueError('Existing diagnostic origins cannot be relabeled by an extension.')
        if self.compilation_details is not None and (type(self.compilation_details) is not CompilationDiagnosticDetails or self.extension_origin is not ModelDiagnosticOrigin.COMPILER):
            raise TypeError('Compiler details cannot relabel validation diagnostics.')
        if self.target is not None and type(self.target) is not ModelDiagnosticTarget:
            raise TypeError('Semantic target association must be typed or absent.')
        object.__setattr__(self, 'related_targets', _ordered(self.related_targets, ModelDiagnosticTarget))
        object.__setattr__(self, 'related_paths', _ordered(self.related_paths, AuthoringSchemaPath))
        _resolution_path(self.source_path)
        if self.validation_report is not None and (type(self.validation_report) is not ModelValidationReport or self.validation_report.diagnostic != self.diagnostic):
            raise ValueError('Stage association must preserve the original MOD-08 report and diagnostic.')

    @property
    def origin(self) -> ModelDiagnosticOrigin:
        return self.extension_origin if self.extension_origin is not None else _DIAGNOSTIC_ORIGINS[type(self.diagnostic)]

    @property
    def stage_id(self) -> str | None:
        return None if self.validation_report is None else self.validation_report.stage_id

    @property
    def cause_codes(self) -> tuple[str, ...]:
        d = self.diagnostic
        codes = []
        if type(d) in (AuthoringSchemaDiagnostic, CanonicalizationDiagnostic, NamespaceResolutionDiagnostic, ModelValidationDiagnostic) and d.cause_code is not None:
            codes.append(d.cause_code)
        if type(d) is CanonicalizationDiagnostic and d.membership_diagnostic is not None:
            codes.append(d.membership_diagnostic.code.value)
        if type(d) is SemanticReferenceDiagnostic and d.namespace_diagnostic is not None:
            codes.append(d.namespace_diagnostic.code.value)
            if d.namespace_diagnostic.cause_code is not None:
                codes.append(d.namespace_diagnostic.cause_code)
        return tuple(codes)


def associate_model_diagnostic(diagnostic: ModelDiagnosticPayload | ModelValidationReport, context: ModelDiagnosticContext) -> ModelDiagnosticEntry:
    """Explicit bounded adapters; no message/QName identity inference or lookup."""
    if type(context) is not ModelDiagnosticContext:
        raise TypeError('Association requires the actual immutable diagnostic context.')
    report = diagnostic if type(diagnostic) is ModelValidationReport else None
    d = diagnostic.diagnostic if report is not None else diagnostic
    if type(d) not in _DIAGNOSTIC_ORIGINS:
        raise TypeError('Unsupported diagnostic producer; no origin guessing.')
    target = None
    related = ()
    path = None
    related_paths = ()
    if report is not None and report.definition is not None:
        field_id = d.field_id if type(d) is TypeValidationDiagnostic else None
        target = ModelDiagnosticTarget(ModelDiagnosticTargetKind.DEFINITION if field_id is None else ModelDiagnosticTargetKind.FIELD, report.definition, field_id)
    if type(d) is TypeValidationDiagnostic:
        if d.target is not None:
            related = (ModelDiagnosticTarget(ModelDiagnosticTargetKind.REFERENCE, d.target),)
    elif type(d) is CanonicalConstructionDiagnostic:
        if target is None and d.reference is not None:
            target = ModelDiagnosticTarget(ModelDiagnosticTargetKind.DEFINITION, d.reference)
        if d.related_reference is not None:
            related = (ModelDiagnosticTarget(ModelDiagnosticTargetKind.DEFINITION, d.related_reference),)
    elif type(d) is CanonicalizationDiagnostic:
        path = d.path
        related_paths = () if d.related_path is None else (d.related_path,)
        if d.membership_diagnostic is not None and d.membership_diagnostic.reference is not None:
            target = ModelDiagnosticTarget(ModelDiagnosticTargetKind.DEFINITION, d.membership_diagnostic.reference)
        if d.membership_diagnostic is not None and d.membership_diagnostic.related_reference is not None:
            related = (ModelDiagnosticTarget(ModelDiagnosticTargetKind.DEFINITION, d.membership_diagnostic.related_reference),)
    elif type(d) is AuthoringSchemaDiagnostic:
        path = d.path
        related_paths = () if d.related_path is None else (d.related_path,)
    elif type(d) is NamespaceResolutionDiagnostic:
        path, related_paths = d.path, d.related_paths
        # Candidates are alternatives, never select a target from ambiguity.
        if type(d.expression) in (AuthoringIdentityExpression, AuthoringVersionExpression):
            target = ModelDiagnosticTarget(ModelDiagnosticTargetKind.REFERENCE, d.expression.reference)
    elif type(d) is SemanticReferenceDiagnostic:
        path, related_paths = d.path, d.related_paths
        if d.target_reference is not None:
            target = ModelDiagnosticTarget(ModelDiagnosticTargetKind.REFERENCE, d.target_reference)
        elif d.request is not None and type(d.request.expression) in (AuthoringIdentityExpression, AuthoringVersionExpression):
            target = ModelDiagnosticTarget(ModelDiagnosticTargetKind.REFERENCE, d.request.expression.reference)
    elif type(d) is ModelValidationDiagnostic and d.reference is not None:
        reference_target = ModelDiagnosticTarget(ModelDiagnosticTargetKind.REFERENCE, d.reference)
        if target is None:
            target = reference_target
        else:
            related = (reference_target,)
    if report is not None and report.source_path is not None:
        path = report.source_path
    if path is None:
        path = context.source_path(target)
    return ModelDiagnosticEntry(d, target, related, path, related_paths, report)


__all__ += ['ModelDiagnosticOrigin', 'ModelDiagnosticTargetKind', 'ModelDiagnosticTarget',
            'ModelDiagnosticPayload', 'ModelDiagnosticContext', 'ModelDiagnosticEntry',
            'associate_model_diagnostic', 'ModelDiagnosticExtension']


# CMP-01 narrow diagnostic presentation projection; no compiler implementation edge.
@_dataclass(frozen=True, slots=True)
class CompilerPhaseDiagnosticView:
    phase_id: str
    status: str
    reason: str | None = None
    prerequisites: tuple[str, ...] = ()
    executed: bool | None = None

    def __post_init__(self) -> None:
        if type(self.prerequisites) not in (tuple, list) or any(type(p) is not str or _re.fullmatch(r'CMP-PHASE-[A-Z0-9]+(?:-[A-Z0-9]+)*', p) is None for p in self.prerequisites):
            raise TypeError('Prerequisite projection retains explicit ordered phase identifiers.')
        object.__setattr__(self, 'prerequisites', tuple(self.prerequisites))
        if self.executed is not None and type(self.executed) is not bool or self.status == 'skipped' and self.executed is True:
            raise ValueError('Execution evidence cannot claim a skipped phase ran.')
        if type(self.phase_id) is not str or not self.phase_id.startswith('CMP-PHASE-') or not self.phase_id[10:]:
            raise TypeError('Compiler phase presentation requires the producer phase identifier.')
        if self.status not in ('completed', 'failed', 'incomplete', 'skipped') or type(self.status) is not str:
            raise TypeError('Compiler phase presentation preserves an actual supported status scalar.')
        if self.reason is not None and (type(self.reason) is not str or not self.reason):
            raise TypeError('Optional producer reason must be nonempty text.')


@_dataclass(frozen=True, slots=True)
class CompilationDiagnosticReport:
    """Immutable explicit MOD-09 projection, not a compiler output/artifact model."""
    status: str
    target: str | None
    entries: tuple[ModelDiagnosticEntry, ...]
    phase_outcomes: tuple[CompilerPhaseDiagnosticView, ...]
    validation_evidence: ModelValidationResult | None = None
    artifact_count: int | None = None

    def __post_init__(self) -> None:
        if self.artifact_count is not None and (type(self.artifact_count) is not int or self.artifact_count < 0):
            raise ValueError('Artifact count is original output membership, never a publication claim.')
        if self.status != 'succeeded' and self.artifact_count not in (None, 0):
            raise ValueError('Unsuccessful compilation projection cannot claim successful output artifacts.')
        if type(self.status) is not str or self.status not in ('succeeded', 'failed', 'incomplete'):
            raise TypeError('Compiler presentation preserves the original status scalar.')
        if self.target is not None and (type(self.target) is not str or not self.target):
            raise TypeError('Optional target presentation must be an explicit producer token.')
        object.__setattr__(self, 'entries', _ordered(self.entries, ModelDiagnosticEntry))
        object.__setattr__(self, 'phase_outcomes', _ordered(self.phase_outcomes, CompilerPhaseDiagnosticView))
        if self.validation_evidence is not None and type(self.validation_evidence) is not ModelValidationResult:
            raise TypeError('Compiler presentation retains original MOD-08 evidence.')


    @property
    def compiler_entries(self) -> tuple[ModelDiagnosticEntry, ...]:
        return tuple(e for e in self.entries if e.origin is ModelDiagnosticOrigin.COMPILER)

    @property
    def summary(self) -> 'CompilationDiagnosticSummary':
        entries = self.compiler_entries
        return CompilationDiagnosticSummary(len(entries), *(sum(e.diagnostic.severity is s for e in entries) for s in (TypeValidationSeverity.ERROR, TypeValidationSeverity.WARNING, TypeValidationSeverity.INFO)))

    def by_severity(self, severity: TypeValidationSeverity) -> tuple[ModelDiagnosticEntry, ...]:
        if type(severity) is not TypeValidationSeverity:
            raise TypeError('Reuse the current diagnostic severity.')
        return tuple(e for e in self.compiler_entries if e.diagnostic.severity is severity)

    def by_origin(self, origin: CompilationDiagnosticOrigin | None) -> tuple[ModelDiagnosticEntry, ...]:
        if origin is not None and type(origin) is not CompilationDiagnosticOrigin:
            raise TypeError('Use the explicit compiler responsibility.')
        return tuple(e for e in self.compiler_entries if (None if e.compilation_details is None else e.compilation_details.origin) is origin)

    def by_phase(self, phase_id: str | None) -> tuple[ModelDiagnosticEntry, ...]:
        if phase_id is not None and (type(phase_id) is not str or _re.fullmatch(r'CMP-PHASE-[A-Z0-9]+(?:-[A-Z0-9]+)*', phase_id) is None):
            raise ValueError('Use existing phase IDs or explicit absence.')
        return tuple(e for e in self.compiler_entries if (e.diagnostic.phase_id if e.compilation_details is None else e.compilation_details.phase_id) == phase_id)

    def by_semantic_target(self, target: ModelDiagnosticTarget) -> tuple[ModelDiagnosticEntry, ...]:
        if type(target) is not ModelDiagnosticTarget:
            raise TypeError('Semantic filtering requires a stable typed target.')
        return tuple(e for e in self.compiler_entries if target in (e.target, *e.related_targets))

    def by_artifact_target(self, artifact: CompilationArtifactDiagnosticView) -> tuple[ModelDiagnosticEntry, ...]:
        if type(artifact) is not CompilationArtifactDiagnosticView:
            raise TypeError('Use the explicit artifact projection.')
        return tuple(e for e in self.compiler_entries if e.compilation_details is not None and e.compilation_details.artifact == artifact)

    def group_by_origin(self) -> _Mapping[CompilationDiagnosticOrigin | None, tuple[ModelDiagnosticEntry, ...]]:
        return _MappingProxyType({origin: entries for origin in (None, *CompilationDiagnosticOrigin) if (entries := self.by_origin(origin))})

    def group_by_phase(self) -> _Mapping[str | None, tuple[ModelDiagnosticEntry, ...]]:
        declared = tuple(p.phase_id for p in self.phase_outcomes)
        entry_phases = tuple(e.diagnostic.phase_id if e.compilation_details is None else e.compilation_details.phase_id for e in self.compiler_entries)
        extra = sorted({p for p in entry_phases if p is not None} - set(declared))
        phases = (None, *declared, *extra)
        return _MappingProxyType({phase: entries for phase in phases if (entries := self.by_phase(phase))})

    def group_by_severity(self) -> _Mapping[TypeValidationSeverity, tuple[ModelDiagnosticEntry, ...]]:
        return _MappingProxyType({severity: entries for severity in TypeValidationSeverity if (entries := self.by_severity(severity))})


__all__ += ['CompilerPhaseDiagnosticView', 'CompilationDiagnosticReport']


@_dataclass(frozen=True, slots=True)
class CompilationDiagnosticSummary:
    total: int
    errors: int
    warnings: int
    info: int

    def __post_init__(self) -> None:
        if any(type(v) is not int or v < 0 for v in (self.total, self.errors, self.warnings, self.info)) or self.total != self.errors + self.warnings + self.info:
            raise ValueError('Summary counts must be nonnegative integers covering the existing severities.')


__all__ += ['CompilationDiagnosticOrigin', 'CompilationArtifactDiagnosticView',
            'CompilationDiagnosticDetails', 'CompilationDiagnosticSummary']
