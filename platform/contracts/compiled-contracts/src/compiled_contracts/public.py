"""Stable artifact output seams, separate from models/compiler/runtime behavior."""
from dataclasses import dataclass
from typing import Protocol
import re
from semantic_kernel.public import SemanticContextRef, ElementVersionRef

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
