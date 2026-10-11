"""Stable artifact output seams, separate from models/compiler/runtime behavior."""
from dataclasses import dataclass
from typing import Protocol
import re
from semantic_kernel.public import SemanticContextRef, ElementVersionRef, SemanticElementId, SemanticVersion

MODULE_NAME = 'compiled-contracts'


@dataclass(frozen=True, slots=True, order=True)
class CompilationArtifactKey:
    """Caller-owned deterministic artifact membership key, never a file/semantic ID."""
    value: str

    def __post_init__(self) -> None:
        if type(self.value) is not str or re.fullmatch(r'[a-z][a-z0-9]*(?:[.-][a-z0-9]+)*', self.value) is None or len(self.value) > 160:
            raise ValueError('Artifact key requires a bounded explicit logical token, not a filename/UUID service.')


@dataclass(frozen=True, slots=True)
class CompilationArtifactKind:
    value: str

    def __post_init__(self) -> None:
        if type(self.value) is not str or re.fullmatch(r'[a-z][a-z0-9]*(?:-[a-z0-9]+)*', self.value) is None or len(self.value) > 80:
            raise ValueError('Artifact kind requires an explicit bounded contract token.')


class CompilationArtifact(Protocol):
    """Read-only metadata of a future owned typed artifact implementation.

    CMP-01 has no concrete payload/generator. Later formats must implement this
    seam with immutable typed payloads; arbitrary dictionaries/blobs are not IR.
    No canonical serialization, content hash, storage or publication implied.
    """
    @property
    def key(self) -> CompilationArtifactKey:
        ...

    @property
    def kind(self) -> CompilationArtifactKind:
        ...

    @property
    def scope(self) -> SemanticContextRef:
        ...

    @property
    def target(self) -> str:
        ...

    @property
    def semantic_dependencies(self) -> tuple[ElementVersionRef, ...]:
        ...


__all__ = ['MODULE_NAME', 'CompilationArtifactKey', 'CompilationArtifactKind', 'CompilationArtifact']


@dataclass(frozen=True, slots=True, order=True)
class RuntimeArtifactFormatId:
    """Explicit content encoding contract; no formats are approved by RUN-01."""
    value: str

    def __post_init__(self) -> None:
        if type(self.value) is not str or len(self.value) > 80 or re.fullmatch(r'[a-z][a-z0-9]*(?:-[a-z0-9]+)*', self.value) is None:
            raise ValueError('Content format requires a bounded explicit logical token.')


@dataclass(frozen=True, slots=True, order=True)
class RuntimeArtifactFormatVersion:
    """Exact encoding version, independent of semantic/manifest/IR versions."""
    value: str

    def __post_init__(self) -> None:
        if type(self.value) is not str or len(self.value) > 40 or re.fullmatch(r'(?:0|[1-9][0-9]*)(?:\.(?:0|[1-9][0-9]*))*', self.value) is None:
            raise ValueError('Format version requires an exact bounded numeric version token.')


@dataclass(frozen=True, slots=True, order=True)
class RuntimeTargetId:
    """Runtime objective, never the compiler artifact-build target."""
    value: str

    def __post_init__(self) -> None:
        RuntimeArtifactFormatId(self.value)


@dataclass(frozen=True, slots=True, order=True)
class RuntimeCapabilityId:
    value: str

    def __post_init__(self) -> None:
        RuntimeArtifactFormatId(self.value)


@dataclass(frozen=True, slots=True, order=True)
class RuntimeCompatibilityVersion:
    """Exact runtime compatibility declaration; no range/latest resolution."""
    value: str

    def __post_init__(self) -> None:
        RuntimeArtifactFormatVersion(self.value)


@dataclass(frozen=True, slots=True)
class RuntimeArtifactContentDeclaration:
    """Optional producer-declared runtime format metadata, preserved by manifests."""
    format: RuntimeArtifactFormatId
    version: RuntimeArtifactFormatVersion
    runtime_target: RuntimeTargetId
    compatibility_version: RuntimeCompatibilityVersion
    required_capabilities: tuple[RuntimeCapabilityId, ...] = ()

    def __post_init__(self) -> None:
        if any(type(v) is not t for v, t in ((self.format, RuntimeArtifactFormatId), (self.version, RuntimeArtifactFormatVersion), (self.runtime_target, RuntimeTargetId), (self.compatibility_version, RuntimeCompatibilityVersion))):
            raise TypeError('Content declaration requires distinct typed format/runtime coordinates.')
        values = self.required_capabilities
        if type(values) is not tuple or len(values) > 128 or any(type(v) is not RuntimeCapabilityId for v in values) or len(set(values)) != len(values):
            raise ValueError('Required capabilities are a bounded distinct immutable explicit inventory.')
        object.__setattr__(self, 'required_capabilities', tuple(sorted(values)))


@dataclass(frozen=True, slots=True)
class RuntimeArtifactDependencyRef:
    """Explicit identity in the same manifest; no inferred/external dependency."""
    key: CompilationArtifactKey

    def __post_init__(self) -> None:
        if type(self.key) is not CompilationArtifactKey:
            raise TypeError('Internal artifact dependency requires its existing artifact key.')


@dataclass(frozen=True, slots=True)
class RuntimeArtifactMetadata:
    """Optional producer-owned metadata, separate from semantic dependencies/payload."""
    semantic_origins: tuple[ElementVersionRef, ...]
    model_wide: bool
    dependencies: tuple[RuntimeArtifactDependencyRef, ...] = ()
    content_declaration: RuntimeArtifactContentDeclaration | None = None

    def __post_init__(self) -> None:
        if self.content_declaration is not None and type(self.content_declaration) is not RuntimeArtifactContentDeclaration:
            raise TypeError('Optional runtime content declaration must be an actual immutable contract.')
        if type(self.semantic_origins) not in (tuple, list) or any(type(r) is not ElementVersionRef or type(r.element_id) is not SemanticElementId or type(r.version) is not SemanticVersion for r in self.semantic_origins):
            raise TypeError('Runtime artifact origins require exact immutable semantic references.')
        origins = tuple(self.semantic_origins)
        if type(self.model_wide) is not bool or self.model_wide and origins or not self.model_wide and not origins or len(set(origins)) != len(origins):
            raise ValueError('Declare either distinct exact origins or explicit model-wide origin.')
        if type(self.dependencies) not in (tuple, list) or any(type(d) is not RuntimeArtifactDependencyRef for d in self.dependencies):
            raise TypeError('Artifact dependencies are explicit typed internal references.')
        dependencies = tuple(self.dependencies)
        if len({d.key for d in dependencies}) != len(dependencies):
            raise ValueError('Dependency membership cannot repeat an artifact key.')
        object.__setattr__(self, 'semantic_origins', tuple(sorted(origins, key=lambda r: (r.element_id.value, r.version.major, r.version.minor, r.version.patch))))
        object.__setattr__(self, 'dependencies', tuple(sorted(dependencies, key=lambda d: d.key.value)))


@dataclass(frozen=True, slots=True)
class RuntimeArtifactDescriptor:
    key: CompilationArtifactKey
    kind: CompilationArtifactKind
    metadata: RuntimeArtifactMetadata

    def __post_init__(self) -> None:
        if type(self.key) is not CompilationArtifactKey or type(self.kind) is not CompilationArtifactKind or type(self.metadata) is not RuntimeArtifactMetadata:
            raise TypeError('Descriptor uses existing artifact identity/kind and closed immutable metadata, never a payload.')


__all__ += ['RuntimeArtifactDependencyRef', 'RuntimeArtifactMetadata', 'RuntimeArtifactDescriptor']
__all__ += ['RuntimeArtifactFormatId', 'RuntimeArtifactFormatVersion', 'RuntimeTargetId',
            'RuntimeCapabilityId', 'RuntimeCompatibilityVersion', 'RuntimeArtifactContentDeclaration']
