"""CMP-08/09 Linux artifact storage adapters: isolated writing and bounded reading.

Supported roots must be trusted application-controlled local filesystems. This
adapter does not protect against privileged actors or hostile same-UID code.
No artifact bytes are executed, encoded or generated here.
"""
from __future__ import annotations
from dataclasses import dataclass, field
import ctypes
import errno
import hashlib
import os
from pathlib import PurePosixPath
import secrets
import stat
import sys

from compiler_core.public import (
    ArtifactWriteRequest, ArtifactWritePlanner, ArtifactWriteDestination, ArtifactWriteDiagnostics,
    ArtifactWritePlan, ArtifactWriteResult,
    ArtifactMaterializationReceipt, MaterializedArtifact, CompilationStatus,
    CompilationFailure, ArtifactDurabilityPolicy, ArtifactWriteStage,
    ArtifactWriteError,
)

MODULE_NAME = 'artifact-writer'
_write_diagnostic = ArtifactWriteDiagnostics.create
_write_reject = ArtifactWriteDiagnostics.reject


_CHUNK = 1024 * 1024
_UNSUPPORTED = {errno.ENOSYS, errno.EINVAL, errno.EOPNOTSUPP, errno.ENOTSUP}


def _rename_capability(plan: ArtifactWritePlan):
    required = (os.open, os.mkdir, os.stat, os.unlink, os.rmdir)
    if sys.platform != 'linux' or any(not hasattr(os, flag) for flag in ('O_DIRECTORY', 'O_NOFOLLOW', 'O_CLOEXEC')) or any(f not in os.supports_dir_fd for f in required) or os.listdir not in os.supports_fd or os.stat not in os.supports_follow_symlinks:
        _write_reject(CompilationFailure.WRITE_UNSUPPORTED_ATOMICITY, 'Secure Linux directory handles and no-follow/exclusive operations are unavailable.', manifest=plan.request.manifest_assembly.manifest, stage=ArtifactWriteStage.DESTINATION, incomplete=True)
    try:
        library = ctypes.CDLL(None, use_errno=True)
        rename = library.renameat2
    except (AttributeError, OSError):
        _write_reject(CompilationFailure.WRITE_UNSUPPORTED_ATOMICITY, 'Linux renameat2 NOREPLACE capability is unavailable; no unsafe fallback.', manifest=plan.request.manifest_assembly.manifest, stage=ArtifactWriteStage.DESTINATION, incomplete=True)
    rename.argtypes = (ctypes.c_int, ctypes.c_char_p, ctypes.c_int, ctypes.c_char_p, ctypes.c_uint)
    rename.restype = ctypes.c_int
    return rename


def _open_root(root: ApprovedLocalArtifactRoot) -> int:
    """Walk every absolute component with no-follow; never use resolve+open."""
    flags = os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW | os.O_CLOEXEC
    descriptor = os.open('/', flags)
    try:
        for component in PurePosixPath(root.absolute_path).parts[1:]:
            previous = descriptor
            descriptor = os.open(component, flags, dir_fd=previous)
            os.close(previous)
            info = os.fstat(descriptor)
            if not stat.S_ISDIR(info.st_mode) or info.st_mode & 0o022 or info.st_uid not in (0, os.geteuid()):
                raise PermissionError('Approved-root ancestry must be controlled.')
        info = os.fstat(descriptor)
        if info.st_uid != os.geteuid():
            raise PermissionError('Approved root must belong to the writer account.')
        return descriptor
    except BaseException:
        os.close(descriptor)
        raise


def _same_directory(parent: int, name: str, descriptor: int) -> bool:
    named = os.stat(name, dir_fd=parent, follow_symlinks=False)
    opened = os.fstat(descriptor)
    return stat.S_ISDIR(named.st_mode) and (named.st_dev, named.st_ino) == (opened.st_dev, opened.st_ino)


def _synchronize(descriptor: int, manifest, output=None) -> None:
    try:
        os.fsync(descriptor)
    except OSError as error:
        incomplete = error.errno in _UNSUPPORTED
        _write_reject(CompilationFailure.WRITE_UNSUPPORTED_DURABILITY if incomplete else CompilationFailure.WRITE_IO_FAILED, 'Mandatory local synchronization did not complete.', manifest=manifest, stage=ArtifactWriteStage.SYNC, descriptor=None if output is None else output.descriptor, location=None if output is None else output.location, incomplete=incomplete)


def _write_file(stage: int, output, synchronize: bool, created: dict[str, tuple[int, int]], manifest) -> None:
    descriptor = os.open(output.location.value, os.O_WRONLY | os.O_CREAT | os.O_EXCL | os.O_NOFOLLOW | os.O_CLOEXEC, 0o600, dir_fd=stage)
    try:
        info = os.fstat(descriptor)
        created[output.location.value] = (info.st_dev, info.st_ino)
        position = 0
        content = memoryview(output.content)
        while position < len(content):
            count = os.write(descriptor, content[position:position + _CHUNK])
            if count <= 0:
                raise OSError(errno.EIO, 'File write made no progress.')
            position += count
        if synchronize:
            _synchronize(descriptor, manifest, output)
    finally:
        os.close(descriptor)


def _verify_file(stage: int, output, inode: tuple[int, int], manifest) -> MaterializedArtifact:
    descriptor = os.open(output.location.value, os.O_RDONLY | os.O_NOFOLLOW | os.O_CLOEXEC, dir_fd=stage)
    try:
        info = os.fstat(descriptor)
        valid = stat.S_ISREG(info.st_mode) and info.st_nlink == 1 and (info.st_dev, info.st_ino) == inode and info.st_size == output.expected_byte_length
        digest = hashlib.sha256() if output.declared_digest is not None else None
        position = 0
        while valid:
            data = os.read(descriptor, _CHUNK)
            if not data:
                break
            if data != output.content[position:position + len(data)]:
                valid = False
                break
            position += len(data)
            if digest is not None:
                digest.update(data)
        after = os.fstat(descriptor)
        valid = valid and position == output.expected_byte_length and (after.st_dev, after.st_ino, after.st_size, after.st_mtime_ns, after.st_ctime_ns) == (info.st_dev, info.st_ino, info.st_size, info.st_mtime_ns, info.st_ctime_ns)
        if not valid or digest is not None and digest.hexdigest() != output.declared_digest.value:
            _write_reject(CompilationFailure.WRITE_INTEGRITY_MISMATCH, 'Staged file does not match approved exact byte content, length or declared digest.', manifest=manifest, descriptor=output.descriptor, location=output.location, stage=ArtifactWriteStage.VERIFY)
        return MaterializedArtifact(output.descriptor, output.location, position, output.declared_digest)
    finally:
        os.close(descriptor)


def _cleanup(root: int, name: str, stage: int, created: dict[str, tuple[int, int]]) -> None:
    """Never recursively remove arbitrary contents or redirect through symlinks."""
    if not _same_directory(root, name, stage):
        raise OSError(errno.EPERM, 'Owned staging binding changed.')
    if set(os.listdir(stage)) != set(created):
        raise OSError(errno.EPERM, 'Owned staging inventory changed.')
    for location, inode in sorted(created.items()):
        info = os.stat(location, dir_fd=stage, follow_symlinks=False)
        if not stat.S_ISREG(info.st_mode) or (info.st_dev, info.st_ino) != inode:
            raise OSError(errno.EPERM, 'Owned staging file binding changed.')
        os.unlink(location, dir_fd=stage)
    os.rmdir(name, dir_fd=root)


def _materialize(plan: ArtifactWritePlan, root: ApprovedLocalArtifactRoot) -> ArtifactWriteResult:
    """Only called by the public facade after complete pure preflight."""
    request = plan.request
    manifest = request.manifest_assembly.manifest
    root_fd = stage_fd = None
    stage_name = None
    created = {}
    diagnostics = []
    entries = None
    committed = False
    status = CompilationStatus.FAILED
    stage = ArtifactWriteStage.DESTINATION
    current = None
    synchronize = request.durability is ArtifactDurabilityPolicy.SYNCHRONIZED_COMMIT
    try:
        rename = _rename_capability(plan)
        root_fd = _open_root(root)
        try:
            os.stat(request.destination.output_directory, dir_fd=root_fd, follow_symlinks=False)
        except FileNotFoundError:
            pass
        else:
            _write_reject(CompilationFailure.WRITE_DESTINATION_EXISTS, 'Committed destination already exists; it is preserved.', manifest=manifest, stage=stage)
        # Detect unavailable synchronization before staging/commit where possible.
        if synchronize:
            stage = ArtifactWriteStage.SYNC
            _synchronize(root_fd, manifest)
        stage = ArtifactWriteStage.STAGING
        for attempt in range(32):
            candidate = '.artifact-stage-' + secrets.token_hex(16)
            try:
                os.mkdir(candidate, 0o700, dir_fd=root_fd)
            except FileExistsError:
                continue
            stage_name = candidate
            break
        else:
            _write_reject(CompilationFailure.WRITE_STAGING_FAILED, 'Exclusive private staging allocation exhausted its bounded attempts.', manifest=manifest, stage=stage)
        stage_fd = os.open(stage_name, os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW | os.O_CLOEXEC, dir_fd=root_fd)
        info = os.fstat(stage_fd)
        if info.st_dev != os.fstat(root_fd).st_dev or info.st_uid != os.geteuid() or info.st_mode & 0o077 or not _same_directory(root_fd, stage_name, stage_fd):
            _write_reject(CompilationFailure.WRITE_STAGING_FAILED, 'Private staging does not meet same-filesystem ownership/isolation requirements.', manifest=manifest, stage=stage)
        for output in plan.outputs:
            current = output
            stage = ArtifactWriteStage.WRITE
            # Ownership is captured from the exclusive open handle before any
            # writes. A failed exclusive open never adopts an existing file.
            _write_file(stage_fd, output, synchronize, created, manifest)
        stage = ArtifactWriteStage.VERIFY
        if set(os.listdir(stage_fd)) != {o.location.value for o in plan.outputs}:
            _write_reject(CompilationFailure.WRITE_INTEGRITY_MISMATCH, 'Staged inventory differs from the complete output plan.', manifest=manifest, stage=stage)
        checked = []
        for output in plan.outputs:
            current = output
            checked.append(_verify_file(stage_fd, output, created[output.location.value], manifest))
        entries = tuple(checked)
        current = None
        if synchronize:
            stage = ArtifactWriteStage.SYNC
            _synchronize(stage_fd, manifest)
        stage = ArtifactWriteStage.COMMIT
        if not _same_directory(root_fd, stage_name, stage_fd):
            _write_reject(CompilationFailure.WRITE_COMMIT_FAILED, 'Owned staging directory binding changed before commit.', manifest=manifest, stage=stage)
        # Linux RENAME_NOREPLACE = 1. A pre-check alone is never the commit lock.
        if rename(root_fd, os.fsencode(stage_name), root_fd, os.fsencode(request.destination.output_directory), 1) != 0:
            code = ctypes.get_errno()
            if code in (errno.EEXIST, errno.ENOTEMPTY):
                _write_reject(CompilationFailure.WRITE_DESTINATION_EXISTS, 'Another committed destination won the exclusive commit race; existing content is preserved.', manifest=manifest, stage=stage)
            if code in _UNSUPPORTED or code == errno.EXDEV:
                _write_reject(CompilationFailure.WRITE_UNSUPPORTED_ATOMICITY, 'Filesystem cannot provide same-filesystem NOREPLACE complete-directory commit.', manifest=manifest, stage=stage, incomplete=True)
            raise OSError(code, 'Exclusive commit failed.')
        committed = True
        if not _same_directory(root_fd, request.destination.output_directory, stage_fd):
            _write_reject(CompilationFailure.WRITE_COMMIT_FAILED, 'Visible destination binding changed after commit.', manifest=manifest, stage=stage)
        if synchronize:
            stage = ArtifactWriteStage.SYNC
            _synchronize(root_fd, manifest)
        status = CompilationStatus.SUCCEEDED
    except ArtifactWriteError as error:
        status = error.status
        diagnostics.extend(error.diagnostics)
    except OSError as error:
        incomplete = stage is ArtifactWriteStage.SYNC and error.errno in _UNSUPPORTED
        category = CompilationFailure.WRITE_UNSUPPORTED_DURABILITY if incomplete else {
            ArtifactWriteStage.DESTINATION: CompilationFailure.WRITE_INVALID_DESTINATION,
            ArtifactWriteStage.STAGING: CompilationFailure.WRITE_STAGING_FAILED,
            ArtifactWriteStage.COMMIT: CompilationFailure.WRITE_COMMIT_FAILED,
            ArtifactWriteStage.VERIFY: CompilationFailure.WRITE_INTEGRITY_MISMATCH,
        }.get(stage, CompilationFailure.WRITE_IO_FAILED)
        status = CompilationStatus.INCOMPLETE if incomplete else CompilationStatus.FAILED
        diagnostics.append(_write_diagnostic(category, 'A mandatory local filesystem operation failed; no successful receipt is issued.', manifest=manifest, stage=stage, descriptor=None if current is None else current.descriptor, location=None if current is None else current.location, incomplete=incomplete))
    finally:
        if stage_name is not None and not committed:
            try:
                if stage_fd is None:
                    # Open failure means ownership cannot be re-established safely.
                    raise OSError(errno.EPERM, 'Staging handle unavailable for safe cleanup.')
                _cleanup(root_fd, stage_name, stage_fd, created)
                if synchronize:
                    os.fsync(root_fd)
            except OSError:
                diagnostics.append(_write_diagnostic(CompilationFailure.WRITE_CLEANUP_FAILED, 'Owned staging cleanup could not be completed safely; original failure is retained.', manifest=manifest, stage=ArtifactWriteStage.CLEANUP))
                status = CompilationStatus.FAILED
        for descriptor in (stage_fd, root_fd):
            if descriptor is not None:
                try:
                    os.close(descriptor)
                except OSError:
                    diagnostics.append(_write_diagnostic(CompilationFailure.WRITE_IO_FAILED, 'A local resource close failed; committed visibility is reported separately.', manifest=manifest, stage=stage))
                    status = CompilationStatus.FAILED
    destination = request.destination if committed else None
    if status is CompilationStatus.SUCCEEDED:
        receipt = ArtifactMaterializationReceipt(manifest, request.destination, entries, request.durability)
        original = request.compilation_result.diagnostics
        additional = tuple(d for d in request.manifest_assembly.diagnostics if not any(d is existing for existing in original))
        return ArtifactWriteResult(status, receipt, (*original, *additional), destination)
    return ArtifactWriteResult(status, diagnostics=tuple(diagnostics), committed_destination=destination)


@dataclass(frozen=True, slots=True)
class ApprovedLocalArtifactRoot:
    """Trusted application config; Linux local filesystem and controlled ancestry."""
    reference: str
    absolute_path: str = field(repr=False)

    def __post_init__(self) -> None:
        from pathlib import PurePosixPath
        ArtifactWriteDestination(self.reference, 'validation')
        path = self.absolute_path
        if type(path) is not str or not path.startswith('/') or path == '/' or '\x00' in path or '\\' in path or str(PurePosixPath(path)) != path or any(p in ('', '.', '..') for p in path.split('/')[1:]):
            _write_reject(CompilationFailure.WRITE_INVALID_DESTINATION, 'Trusted root requires an explicit canonical absolute POSIX directory; no inferred defaults.')


@dataclass(frozen=True, slots=True)
class LocalFilesystemArtifactWriter:
    """Application facade; all filesystem effects reside in the infrastructure adapter."""
    approved_roots: tuple[ApprovedLocalArtifactRoot, ...]
    planner: ArtifactWritePlanner = field(default_factory=ArtifactWritePlanner)

    def __post_init__(self) -> None:
        if type(self.approved_roots) not in (tuple, list) or any(type(r) is not ApprovedLocalArtifactRoot for r in self.approved_roots):
            _write_reject(CompilationFailure.WRITE_INVALID_DESTINATION, 'Approved roots require a finite typed server configuration.')
        roots = tuple(self.approved_roots)
        if len({r.reference for r in roots}) != len(roots) or type(self.planner) is not ArtifactWritePlanner:
            _write_reject(CompilationFailure.WRITE_INVALID_DESTINATION, 'Trusted root references must be unique and planner must be actual typed configuration.')
        object.__setattr__(self, 'approved_roots', tuple(sorted(roots, key=lambda r: r.reference)))

    def write(self, request: ArtifactWriteRequest) -> ArtifactWriteResult:
        try:
            plan = self.planner.plan(request)
            root = next((r for r in self.approved_roots if r.reference == request.destination.root_reference), None)
            if root is None:
                _write_reject(CompilationFailure.WRITE_INVALID_DESTINATION, 'Destination root is not approved by server configuration.', manifest=request.manifest_assembly.manifest, stage=ArtifactWriteStage.DESTINATION)
        except ArtifactWriteError as error:
            return ArtifactWriteResult(error.status, diagnostics=error.diagnostics)
        return _materialize(plan, root)



__all__ = ['MODULE_NAME', 'ApprovedLocalArtifactRoot', 'LocalFilesystemArtifactWriter']


# CMP-09 reuses the storage configuration boundary, not writer operations.
from compiler_core.public import (
    ArtifactReadRequest, ArtifactReadPolicy, ArtifactReadPlanner, ArtifactReadPlan,
    ArtifactReadResult, ArtifactReadError, ArtifactReadDiagnostics, ArtifactReadStage,
    ArtifactReadVerification, RetrievedArtifact,
)


def _read_capability(plan: ArtifactReadPlan) -> None:
    if sys.platform != 'linux' or any(not hasattr(os, flag) for flag in ('O_DIRECTORY', 'O_NOFOLLOW', 'O_CLOEXEC', 'O_NONBLOCK', 'O_NOATIME')) or os.open not in os.supports_dir_fd or os.stat not in os.supports_dir_fd or os.stat not in os.supports_follow_symlinks:
        ArtifactReadDiagnostics.reject(CompilationFailure.READ_UNSUPPORTED_SOURCE, 'Secure Linux directory-relative no-follow/nonblocking read capabilities are unavailable.', manifest=plan.request.manifest, stage=ArtifactReadStage.SOURCE, incomplete=True)


def _read_metadata(info) -> tuple[int, ...]:
    return (info.st_dev, info.st_ino, info.st_mode, info.st_nlink, info.st_uid, info.st_size, info.st_mtime_ns, info.st_ctime_ns)


def _read_directory_current(root: int, name: str, descriptor: int) -> bool:
    try:
        return _same_directory(root, name, descriptor)
    except FileNotFoundError:
        return False


def _read_selected_file(directory: int, entry: MaterializedArtifact, plan: ArtifactReadPlan, aggregate: int) -> RetrievedArtifact:
    manifest, policy = plan.request.manifest, plan.effective_policy
    reject = ArtifactReadDiagnostics.reject
    descriptor = None
    outcome = None
    failure = None
    stage = ArtifactReadStage.OPEN
    try:
        named = os.stat(entry.location.value, dir_fd=directory, follow_symlinks=False)
        if stat.S_ISLNK(named.st_mode):
            reject(CompilationFailure.READ_UNSAFE_PATH, 'Selected committed artifact is a symbolic link.', manifest=manifest, entry=entry, stage=stage)
        if not stat.S_ISREG(named.st_mode):
            reject(CompilationFailure.READ_UNSUPPORTED_FILE_TYPE, 'Selected committed artifact is not a regular file.', manifest=manifest, entry=entry, stage=stage)
        # Nonblocking open prevents a regular-file-to-FIFO race from blocking.
        descriptor = os.open(entry.location.value, os.O_RDONLY | os.O_NOFOLLOW | os.O_NONBLOCK | os.O_NOATIME | os.O_CLOEXEC, dir_fd=directory)
        before = os.fstat(descriptor)
        if not stat.S_ISREG(before.st_mode) or before.st_nlink != 1:
            reject(CompilationFailure.READ_UNSUPPORTED_FILE_TYPE, 'Opened artifact must be a regular single-link committed file.', manifest=manifest, entry=entry, stage=stage)
        if before.st_uid != os.geteuid() or before.st_mode & 0o022:
            reject(CompilationFailure.READ_ACCESS_DENIED, 'Opened artifact ownership or write permissions violate approved isolation.', manifest=manifest, entry=entry, stage=stage)
        if _read_metadata(named) != _read_metadata(before):
            reject(CompilationFailure.READ_CONCURRENT_MODIFICATION, 'Selected file binding or metadata changed during safe open.', manifest=manifest, entry=entry, stage=stage)
        stage = ArtifactReadStage.VERIFY
        if before.st_size > policy.maximum_artifact_bytes or aggregate + before.st_size > policy.maximum_aggregate_bytes:
            reject(CompilationFailure.READ_SIZE_LIMIT_EXCEEDED, 'Actual stored bytes exceed effective read limits.', manifest=manifest, entry=entry, stage=stage)
        if before.st_size != entry.byte_length:
            reject(CompilationFailure.READ_SIZE_MISMATCH, 'Stored byte length differs from the materialization receipt.', manifest=manifest, entry=entry, stage=stage)
        buffer = bytearray()
        digest = hashlib.sha256() if entry.verified_digest is not None else None
        stage = ArtifactReadStage.READ
        while True:
            # At most one extra byte probes growth beyond the approved length.
            allowance = min(entry.byte_length - len(buffer), policy.maximum_artifact_bytes - len(buffer), policy.maximum_aggregate_bytes - aggregate - len(buffer))
            data = os.read(descriptor, min(_CHUNK, allowance + 1))
            if not data:
                break
            actual = len(buffer) + len(data)
            if actual > policy.maximum_artifact_bytes or aggregate + actual > policy.maximum_aggregate_bytes:
                reject(CompilationFailure.READ_SIZE_LIMIT_EXCEEDED, 'Stored content grew beyond effective limits during bounded read.', manifest=manifest, entry=entry, stage=stage)
            if actual > entry.byte_length:
                reject(CompilationFailure.READ_SIZE_MISMATCH, 'Stored content grew beyond its committed expected byte length.', manifest=manifest, entry=entry, stage=stage)
            buffer.extend(data)
            if digest is not None:
                digest.update(data)
        stage = ArtifactReadStage.VERIFY
        after = os.fstat(descriptor)
        if _read_metadata(before) != _read_metadata(after):
            reject(CompilationFailure.READ_CONCURRENT_MODIFICATION, 'Opened file metadata changed while retrieving selected bytes.', manifest=manifest, entry=entry, stage=stage)
        try:
            current = os.stat(entry.location.value, dir_fd=directory, follow_symlinks=False)
        except FileNotFoundError:
            reject(CompilationFailure.READ_CONCURRENT_MODIFICATION, 'Committed location disappeared after its file was opened.', manifest=manifest, entry=entry, stage=stage)
        if _read_metadata(current) != _read_metadata(after):
            reject(CompilationFailure.READ_CONCURRENT_MODIFICATION, 'Committed location no longer identifies the unchanged opened file.', manifest=manifest, entry=entry, stage=stage)
        if len(buffer) != entry.byte_length:
            reject(CompilationFailure.READ_SIZE_MISMATCH, 'Retrieved byte length differs from the materialization receipt.', manifest=manifest, entry=entry, stage=stage)
        if digest is not None and digest.hexdigest() != entry.verified_digest.value:
            reject(CompilationFailure.READ_DIGEST_MISMATCH, 'Retrieved bytes do not match the explicitly declared receipt digest.', manifest=manifest, entry=entry, stage=stage)
        outcome = RetrievedArtifact(entry.descriptor, entry.location, bytes(buffer), ArtifactReadVerification(entry.byte_length, len(buffer), entry.verified_digest))
    except ArtifactReadError as error:
        failure = error
    except OSError as error:
        category = CompilationFailure.READ_MISSING_FILE if error.errno == errno.ENOENT else CompilationFailure.READ_ACCESS_DENIED if isinstance(error, PermissionError) or error.errno in (errno.EACCES, errno.EPERM) else CompilationFailure.READ_UNSAFE_PATH if error.errno in (errno.ELOOP, errno.ENOTDIR) else CompilationFailure.READ_IO_FAILED
        failure = ArtifactReadError((ArtifactReadDiagnostics.create(category, 'A mandatory safe file read operation failed.', manifest=manifest, entry=entry, stage=stage),))
    finally:
        if descriptor is not None:
            try:
                os.close(descriptor)
            except OSError:
                diagnostic = ArtifactReadDiagnostics.create(CompilationFailure.READ_IO_FAILED, 'A selected read handle could not be closed normally.', manifest=manifest, entry=entry, stage=ArtifactReadStage.CLOSE)
                failure = ArtifactReadError((diagnostic,) if failure is None else (*failure.diagnostics, diagnostic))
    if failure is not None:
        raise failure
    return outcome


def _retrieve_selected(plan: ArtifactReadPlan, root: ApprovedLocalArtifactRoot) -> ArtifactReadResult:
    root_fd = directory_fd = None
    manifest = plan.request.manifest
    stage = ArtifactReadStage.SOURCE
    diagnostics = []
    status = CompilationStatus.FAILED
    retrieved = []
    try:
        _read_capability(plan)
        root_fd = _open_root(root)
        directory_fd = os.open(plan.request.source.output_directory, os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW | os.O_CLOEXEC, dir_fd=root_fd)
        directory = os.fstat(directory_fd)
        if directory.st_dev != os.fstat(root_fd).st_dev or directory.st_uid != os.geteuid() or directory.st_mode & 0o022:
            ArtifactReadDiagnostics.reject(CompilationFailure.READ_UNSUPPORTED_SOURCE, 'Committed directory does not meet approved same-filesystem ownership/isolation requirements.', manifest=manifest, stage=stage)
        if not _read_directory_current(root_fd, plan.request.source.output_directory, directory_fd):
            ArtifactReadDiagnostics.reject(CompilationFailure.READ_CONCURRENT_MODIFICATION, 'Committed directory binding changed during source open.', manifest=manifest, stage=stage)
        aggregate = 0
        for entry in plan.entries:
            artifact = _read_selected_file(directory_fd, entry, plan, aggregate)
            retrieved.append(artifact)
            aggregate += len(artifact.content)
        stage = ArtifactReadStage.VERIFY
        if not _read_directory_current(root_fd, plan.request.source.output_directory, directory_fd):
            ArtifactReadDiagnostics.reject(CompilationFailure.READ_CONCURRENT_MODIFICATION, 'Committed directory binding changed during selected retrieval.', manifest=manifest, stage=stage)
        status = CompilationStatus.SUCCEEDED
    except ArtifactReadError as error:
        status = error.status
        diagnostics.extend(error.diagnostics)
    except OSError as error:
        category = CompilationFailure.READ_MISSING_FILE if error.errno == errno.ENOENT else CompilationFailure.READ_ACCESS_DENIED if isinstance(error, PermissionError) or error.errno in (errno.EACCES, errno.EPERM) else CompilationFailure.READ_UNSAFE_PATH if error.errno in (errno.ELOOP, errno.ENOTDIR) else CompilationFailure.READ_IO_FAILED
        diagnostics.append(ArtifactReadDiagnostics.create(category, 'Approved committed source could not be accessed safely.', manifest=manifest, stage=stage))
    finally:
        for descriptor in (directory_fd, root_fd):
            if descriptor is not None:
                try:
                    os.close(descriptor)
                except OSError:
                    diagnostics.append(ArtifactReadDiagnostics.create(CompilationFailure.READ_IO_FAILED, 'A source read handle could not be closed normally.', manifest=manifest, stage=ArtifactReadStage.CLOSE))
                    status = CompilationStatus.FAILED
    # Atomicity concerns exposed result payloads, not a filesystem transaction.
    return ArtifactReadResult(status, plan, tuple(retrieved) if status is CompilationStatus.SUCCEEDED else (), tuple(diagnostics))


@dataclass(frozen=True, slots=True)
class LocalFilesystemArtifactReader:
    """Read-only adapter; shares trusted root configuration with CMP-08."""
    approved_roots: tuple[ApprovedLocalArtifactRoot, ...]
    planner: ArtifactReadPlanner = field(default_factory=ArtifactReadPlanner)

    def __post_init__(self) -> None:
        if type(self.approved_roots) not in (tuple, list) or any(type(r) is not ApprovedLocalArtifactRoot for r in self.approved_roots) or type(self.planner) is not ArtifactReadPlanner:
            ArtifactReadDiagnostics.reject(CompilationFailure.READ_UNSUPPORTED_SOURCE, 'Reader requires finite typed server-approved roots and planner.')
        roots = tuple(self.approved_roots)
        if len({r.reference for r in roots}) != len(roots):
            ArtifactReadDiagnostics.reject(CompilationFailure.READ_UNSUPPORTED_SOURCE, 'Approved read root references must be unique.')
        object.__setattr__(self, 'approved_roots', tuple(sorted(roots, key=lambda r: r.reference)))

    def read(self, request: ArtifactReadRequest) -> ArtifactReadResult:
        try:
            plan = self.planner.plan(request)
            root = next((r for r in self.approved_roots if r.reference == request.source.root_reference), None)
            if root is None:
                ArtifactReadDiagnostics.reject(CompilationFailure.READ_UNSUPPORTED_SOURCE, 'Read source is not in the trusted application root catalog.', manifest=request.manifest, stage=ArtifactReadStage.SOURCE)
        except ArtifactReadError as error:
            return ArtifactReadResult(error.status, diagnostics=error.diagnostics)
        return _retrieve_selected(plan, root)


__all__ += ['LocalFilesystemArtifactReader']
