"""MOD-01: immutable authoring schema and pure structural validation.

Input is a decoded JSON-compatible abstract tree, never JSON/YAML source text.
Output is an authoring snapshot, not TypeDefinition/FieldDefinition/TypeRef.
No resolution, registry, canonicalizer, compiler, runtime or parser dependency.
"""
from dataclasses import dataclass as _dataclass
from types import MappingProxyType as _MappingProxyType
from semantic_kernel.public import (
    SemanticElementId, SemanticElementIdError, SemanticContextRef,
    SemanticContextRefError, Namespace, NamespaceError, QualifiedName,
    QualifiedNameError, SemanticVersion, SemanticVersionError, PrimitiveType,
    PrimitiveTypeError, ElementRef, ElementVersionRef,
)
from model_core.public import (
    FieldId, FieldIdError, FieldName, FieldNameError, FieldConstraintError,
    FieldPresence, FieldNullability, ConstraintKind, ConstraintKinds,
    FieldConstraintSet, MinLengthConstraint, MaxLengthConstraint,
    MinimumConstraint, MaximumConstraint, PatternConstraint, PrecisionConstraint,
    ScaleConstraint, TypeValidationSeverity,
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
