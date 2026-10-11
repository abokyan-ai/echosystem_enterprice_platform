# CMP-09 — Artifact Reader

Date: 2026-10-11. Implementation status: **DEFERRED / NOT VERIFIED**. Tests implemented/executed **0**. [173 deferred scenarios](../../test-archive/CMP-09/CMP-09-deferred-tests.md).

## Actual contracts and ownership

`compiler_core.public` owns pure Python ArtifactReader, ArtifactReadRequest, ArtifactReadSelection/Mode, ArtifactReadPolicy/Integrity, ArtifactReadPlanner/Plan, ArtifactReadVerification, RetrievedArtifact, ArtifactReadResult and ArtifactReadDiagnostics/Stage/SourceType. Domain/application code contains no filesystem/framework imports. Original CompilationResult and ArtifactWriteResult are unchanged.

ArtifactReadSource is an explicit alias of CMP-08 ArtifactWriteDestination: the same logical approved root reference plus committed output-set token, not a new storage/path model. Existing ArtifactRelativeLocation, MaterializedArtifact, ArtifactContentDigest and ArtifactMaterializationReceipt are reused. No bare paths or independent reader layout are accepted.

`artifact_writer.public.LocalFilesystemArtifactReader` is the read-only infrastructure adapter in the existing tooling-owned `tools/artifact-writer` package. It reuses ApprovedLocalArtifactRoot and root traversal/directory binding helpers already owned there. Read-specific code never calls the writer, staging, rename, cleanup or synchronization operations. Distinct reader/writer classes preserve capabilities; no combined storage manager is introduced. Existing constrained artifact-materialization profile and compiler public edge suffice; no new module, policy exception, neutral filesystem capability, compiler-to-tool or runtime edge.

Trusted application code explicitly wires roots and server limits. Django/DRF remains the selected API stack, but package metadata reports both absent and no compilation HTTP adapter exists. No endpoint/serializer/permission change/ORM/migration is added. Any future applicable API must perform established authorization, resolve server root config and bound response size; an ID/manifest/receipt is not access authority.

## Manifest and original receipt prerequisite

Require actual immutable CMP-07 manifest and original CMP-08 receipt. There is no supported receipt-free locator path. Revalidate manifest V0/schema/identity/full descriptor inventory/internal dependencies, original canonical scope/target, original accepted VALID/READY evidence and exact model object, invocation output origin/request/compiler, and captured completed/executed final artifact phase evidence. No compilation/semantic validation/type lowering executes. Existing manifests represent accepted past compilation: the reader does **not** rerun a current compiler configuration audit to read historical bytes.

Receipt identity/schema/scope/target/full descriptors/kinds must match the supplied manifest, and its compilation_association must be the **same original object**. Equivalent metadata from another invocation is insufficient. The receipt destination must equal the requested logical source. All receipt entries are checked for complete ordered membership, unique validated flat locations, actual nonnegative byte lengths and optional supported declared digest, even for a subset read. No missing/extra/duplicate entry reconciliation, receipt reconstruction from disk or guessed locations.

These are trusted in-process associations, not portable signed/authenticated provenance or protection against malicious Python forging frozen values. No reader claim upgrades receipt existence into proof of current physical presence or publisher authority.

## Explicit selection, ordering and bounded policy

ONE_ARTIFACT requires exactly one existing CompilationArtifactKey. EXPLICIT_ARTIFACT_SET requires distinct nonempty keys. ALL_DECLARED_ARTIFACTS permits no key overrides. Unknown identities fail before filesystem access; no filename/QName/semantic-ID/IR-ID fallback and no dependency closure. Selected entries retain manifest artifact-key order, regardless of caller key order or filename.

ArtifactReadPlan retains actual request, effective policy, selected receipt entries and selected_keys. `complete_set` is true only for ALL mode. Explicit subset success verifies only its selected scope; even an explicit set containing every key retains explicit-set mode. Read result carries the plan rather than implying full verification from count.

Default caller/server policy: **32 MiB per artifact, 128 MiB aggregate, 128 artifacts**, all finite positive actual ints (not bool/float). Required integrity is SIZE_VERIFIED or DIGEST_VERIFIED. Effective maxima are the minima of caller/server limits; effective integrity is the stricter requirement. Caller options cannot raise ceilings or weaken a mandatory server digest. Trusted server config may explicitly select other finite limits. Count and receipt lengths are checked before filesystem access; actual file length and each read chunk are also bounded.

Payload limits bound retained byte content, not an exact process RSS/interpreter overhead or storage latency. Reads use at most 1 MiB chunks and at most one extra byte as a growth/EOF probe; a bounded bytearray is converted to immutable bytes, which may transiently duplicate one individually bounded buffer. Already retrieved selected payloads remain within aggregate limits. No unbounded streams/global caches/timeouts/remote streaming framework.

## Safe read-only Linux adapter

Supported environment is the existing trusted Linux local-filesystem model: explicit canonical root configuration, administrator-controlled ancestry/mounts, root/writer-reader UID ownership, no group/world-writable ancestors or output directory, no symlink components. Root is opened component by component with O_DIRECTORY|O_NOFOLLOW directory handles, and the committed output token is opened relative to that root. Output must have same device as root, expected UID and safe permissions. No inferred cwd/home/MEDIA_ROOT/source/query root or resolve-then-open.

Only existing CMP-08 flat lowercase portable ASCII relative filenames are supported (1..240 characters, no traversal/separators/NUL/encoding aliases/reserved stems/trailing dot). The reader uses actual receipt locations and never repeats writer layout mapping.

Each selected named object is inspected no-follow before open; symlinks and nonregular file types are rejected. Then O_RDONLY|O_NOFOLLOW|O_NONBLOCK|O_NOATIME|O_CLOEXEC opens the file relative to the committed directory. NONBLOCK prevents a file-to-FIFO replacement race from hanging; fstat rechecks actual regular type, single link, owner and no group/world-write. O_NOATIME avoids reader-requested file atime updates in this ownership model; no capability fallback silently weakens required open semantics. No artifact file writes, renames, repairs, deletes or decoding occur. Underlying filesystem/access effects are not a universal no-state-change guarantee.

Selected file identity/mode/link/owner/size/mtime/ctime are checked between named stat and opened descriptor, before/after reading, and against the named location after retrieval. Output directory name/inode binding is checked before/after selected retrieval. These detect obvious replacements/mutations, not every hostile concurrent change or a cross-file snapshot. Files read earlier may change while later files are read. Privileged/hostile same-UID actors or administrator root moves remain outside the trusted isolation model. Linux fd flags do not certify arbitrary remote mounts; application must approve actual local storage.

## Exact bytes and actual integrity

Receipt always includes expected byte length; no guessed/missing-size read variant. Initial fstat must match expected length and effective bounds. Read bytes through the opened descriptor without text/line-ending/whitespace normalization, SQL/JSON interpretation, Python import, pickle/eval/exec or runtime loading. Genuine zero-byte artifacts are supported. Growth beyond receipt/limits aborts on a bounded probe, truncated/mismatched lengths fail.

Every available receipt SHA-256 digest is reverified against exact retrieved bytes, including when required_integrity is SIZE_VERIFIED. Explicit algorithm/lowercase digest contract reused; malformed/unknown algorithm fails. Mandatory selected digest absent returns INCOMPLETE before reads, never silent downgrade. No new digest is recorded when absent. SIZE_VERIFIED checks actual equal expected/measured lengths; it cannot detect same-size corruption cryptographically. DIGEST_VERIFIED means actual retrieved bytes matched the declared byte digest, not signature/authenticity/publication/authorization.

ArtifactReadVerification records actual expected/measured lengths and optional reverified declared digest; its integrity property derives the evidence actually present. RetrievedArtifact retains original descriptor (identity/kind/origins/dependencies), safe committed location, immutable bytes and evidence. It is distinct from source CompilationArtifact and does not reconstruct semantic/runtime objects.

## Result atomicity, errors and directory scope

SUCCEEDED requires every selected artifact retrieved/verified in plan order within limits and fulfilled integrity. A failed earlier/later selected file or handle close yields no retrieved-artifact payload collection. FAILED has expected input/storage/path/integrity diagnostics; INCOMPLETE identifies unavailable security/digest capability. Plan metadata may remain for failed selected scope, but artifacts=(). Unexpected programming defects propagate after handle cleanup; no falsely successful result.

Reads are sequential. First failing selected entry defines stable observable failure ordering. Per-file and source handle close errors are separate diagnostics retaining any primary error; close failure blocks success. Handles always close, no repair or writer cleanup executes.

ALL success means every declared artifact was read under the selected checks. The adapter does **not** enumerate/audit the directory: extras are neither read nor deleted, and current directory exclusivity is not certified. Writer commit-time inventory remains a historical fact only. Result atomicity is payload exposure semantics, not filesystem transaction/snapshot/activation.

CMP-062..080 reuse existing compiler diagnostics with RESULT origin, typed read_stage/read_source_type and existing independent manifest/artifact/context/safe relative location associations. Categories cover request/manifest/receipt/unknown selection/source/path/file-type/missing/access/limits/size/digest/missing digest/I/O/incomplete set/concurrent change/unsupported digest/policy. Original CMP-07 rejection diagnostics retained. Raw diagnostics contain new fields; existing model projection unchanged; CMP-06 semantic diagnostic comparison includes them. Public messages never expose unrestricted absolute paths, raw OS error text, stack traces or secrets. Storage availability/corruption is not TYPE-06 semantic blame.

## Mini Sales — conceptual only

Reuse actual Customer `sem_550e8400-e29b-41d4-a716-000000000001@1.0.0` and Employee `sem_550e8400-e29b-41d4-a716-000000000002@1.0.0` from repository Mini Sales sources. Prompt `typ_customer_123` and `typ_employee_123` are illustrative aliases incompatible with actual Kernel grammar.

No approved final byte producer exists currently; TypeCompilerPass produces IR, which cannot fabricate a runtime manifest/receipt/file/read success. No Mini Sales write/read experiment is executed.

A future real producer and successful original CMP-07/CMP-08 materialization receipt may identify `customer.bin`/`employee.bin` under an approved sales output. ALL selects both in manifest order; missing Customer CMP-070, digest-corrupted Employee CMP-074, unknown ID CMP-065, unsafe receipt location CMP-068/underlying CMP-050. If Customer reads then Employee fails, the failed result exposes no partial Customer bytes. ONE(Customer) success reports only that selected scope. No reconstruction, repair, publication, activation or execution follows.

## Deferred verification and limitations

[173 deferred scenarios](../../test-archive/CMP-09/CMP-09-deferred-tests.md) cover all requested categories and added boundaries/resource/race/close/digest cases. Exactly one archive Markdown file per latest task section 45; no README/scaffold/additional archive spec. No automated tests, custom scenario scripts, manual materialization/read experiments or runtime/CLI smoke. Static source/syntax/build/public MODULE_NAME imports/dependency/fitness/document checks are separate and do not verify behavior.

Missing real producer/encoders/portable proof/general SK-11/TYPE-01/HTTP API, optional digest evidence, Linux-only controlled local storage, absent replacement/cloud/streaming/decoder/loader and concurrent snapshot limitations remain explicit. Stop CMP-09; no CMP-10.
