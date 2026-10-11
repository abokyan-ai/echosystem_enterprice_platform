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

    def __post_init__(self) -> None:
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
