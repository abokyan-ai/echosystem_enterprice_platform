# CMP-08 — Artifact Writer

Date: 2026-10-11. Implementation status: **DEFERRED / NOT VERIFIED**. Deferred suite executed: **0**. [158 future scenarios](../../test-archive/CMP-08/CMP-08-deferred-tests.md).

## Ownership and actual integration

`compiler_core.public` owns the pure Python ArtifactWriter protocol, immutable ArtifactWriteRequest/Destination/Policy/Durability contracts, explicit ArtifactContentSource/ArtifactByteContentSupport, deterministic ArtifactOutputLayout/WritePlanner/WritePlan, MaterializedArtifact/ArtifactMaterializationReceipt/ArtifactWriteResult and ArtifactWriteDiagnostics. Domain/application planning has no filesystem or framework imports.

`artifact_writer.public` in **tools/artifact-writer** owns ApprovedLocalArtifactRoot and LocalFilesystemArtifactWriter plus Linux filesystem infrastructure. Trusted application code wires root references and the planner explicitly. The constrained `artifact-materialization` tooling profile permits only compiler public contracts. The compiler never imports tooling, and compiler-neutral capabilities remain unchanged. No runtime import/activation change or dependency exception.

Django + DRF remains the selected backend API framework, but neither distribution is installed in this repository workspace and no compilation HTTP adapter exists. No HTTP endpoint, serializer, permission/auth change, ORM model or migration is needed or added. Future API integration must preserve existing authorization and resolve logical destinations through trusted server config.

## Prerequisites and approved content

The write request retains the actual CompilationResult and successful RuntimeArtifactManifestAssemblyResult, original artifact sources, logical destination, explicit policy/durability and layout. The planner uses CMP-01 status directly, requires full successful CMP-07 assembly, rechecks original result/request/configuration/canonical/evidence/context/target and complete phase outcomes, compares output_origin **by identity**, rechecks all descriptor metadata and inventory. No validation, compiler phase, type lowering or encoding executes.

Every source must reference one actual object from the supplied result.artifacts collection, exactly once. Copies, missing/extra/repeated sources fail. Caller-created bytes are not an independent content override. ArtifactByteContentSupport approves an existing CMP-07 frozen concrete artifact kind/class and a separate declared immutable **bytes field**; an optional separate digest field must contain ArtifactContentDigest (`sha256`, lowercase 64 hex). No approved runtime kinds/byte producers/encoders exist by default. Missing capability returns INCOMPLETE, not empty placeholder files. Exact bytes only; text/bytearray/memoryview/implicit OS encoding/repr/pickle are rejected. A genuine producer-defined empty byte payload is valid and distinct from missing content. Digest verification occurs only when explicitly declared; no digest is created as metadata when absent.

This preserves CMP-07's trusted in-process scope association; it is not an authenticated anti-forgery record or portable compiler/output proof. Trusted application/producer code must honor immutable contracts. The writer cannot establish that hostile Python code did not forge or mutate otherwise valid in-process values.

## Complete deterministic plan and destination

ArtifactWriteDestination contains a bounded server root reference and output-set token, never an absolute caller-supplied storage path. Only the adapter's explicit ApprovedLocalArtifactRoot catalog resolves a root; no cwd/home/temp/MEDIA_ROOT/source-directory default. Root config includes an explicit canonical absolute POSIX directory. The adapter checks that it is already present; it does not create an arbitrary root tree.

Before any filesystem mutation, the planner checks status, manifest, exact content membership, kind approval, immutable bytes, layout and conflicts. Configuration resolution and OS/root capability inspection also precede staging. Outputs follow the existing artifact-key order, independent of supplied source order. Default relative filename is `kind__key.bin` using validated logical tokens; `.bin` is a generic byte-file extension, not an encoder/type generation choice. An explicit layout must cover every key/kind once. No timestamps, PID, random final names or automatic collision suffixes.

v0 supports **flat lowercase portable ASCII filenames only**: 1..240 characters, starting with a letter, then lowercase letters/digits/underscore/dot/hyphen, no trailing dot or reserved Windows stem. Absolute/traversal/separators/empty components/NUL/percent-encoding/Unicode/case aliases are rejected. An overlong default kind/key mapping fails before staging; supply an explicit complete shorter mapping. Nested directories are deliberately unsupported. Duplicate normalized locations fail; no file merge.

## Supported Linux security and commit semantics

Actual materialization is restricted to Linux with directory-fd/no-follow primitives, libc `renameat2`, and a **trusted application-approved local filesystem** supporting same-filesystem RENAME_NOREPLACE. Other OS/symbol/kernel/filesystem capabilities fail closed, no fallback to overwriting `os.rename`. A libc symbol does not prove mount support: actual unsupported rename returns INCOMPLETE and triggers owned cleanup.

Absolute roots are walked component by component from `/`, opening O_DIRECTORY|O_NOFOLLOW|O_CLOEXEC handles. Ancestors must have owner root/writer UID and no group/world write; root must belong to the writer UID. Root config/ancestry and mounts must remain administrator-controlled. These protections do not defend against root, privileged actors, hostile same-UID code or an administrator moving root ancestors during an operation. No universal remote filesystem/security/durability claim is made.

The adapter allocates a fresh exclusive 0700 random staging directory under the opened root (up to 32 bounded name attempts), verifies same filesystem/ownership/inode binding, then creates each flat 0600 file using O_CREAT|O_EXCL|O_NOFOLLOW. Random staging names never affect committed layout. Exclusive file handle inode tracking occurs **before** writes; a failed exclusive open never adopts another file for cleanup.

Short writes are looped in bounded chunks; zero progress is I/O failure. Every file is reopened no-follow and compared to approved bytes, measured length and inode, regular type, nlink=1, stable metadata and optional declared SHA-256. Staging inventory must be exactly the complete plan. Staged verification cannot authorize runtime execution.

A single directory `renameat2(..., RENAME_NOREPLACE)` commits the entire set in the same opened root. The early existence check is only preflight; **NOREPLACE** supplies the cross-process commit conflict guarantee. An existing directory (including empty), file or symlink is preserved. Racing writers use independent staging; only one may win. FAIL_IF_EXISTS repeated requests are explicit conflicts, never successful idempotent replays. Safe replacement is unsupported; no remove-then-rename, per-file commit, in-process lock or distributed transaction.

## Durability and failure facts

VISIBLE_COMMIT means verified complete directory visible at final destination. It does not claim crash durability. SYNCHRONIZED_COMMIT requires initial root fsync capability inspection, every file fsync, staging-directory fsync, then rename and final root fsync. These are actual requested synchronization steps, not a universal hardware/power-loss/remote/replication guarantee.

Before commit, any failed mandatory stage prevents final directory/receipt. Expected OS failures yield FAILED; missing content/platform/policy/durability capability yields INCOMPLETE. Unexpected programming defects propagate after narrowly scoped cleanup.

A failure **after successful rename** cannot safely roll back a visible committed directory. The result has no success receipt and explicitly retains `committed_destination`; it may be FAILED or INCOMPLETE if final synchronization is unavailable. Callers must inspect this field before retrying. The adapter never removes the committed final output.

Cleanup validates the original staging-directory inode and exact tracked file inventory/inodes. It removes only owned files and the owned empty staging directory, never recursively adopts unknown entries or follows links. Cleanup failure adds CMP-058 while retaining the primary diagnostic, and may leave owned staging for explicit operator action. Failure to open the staging handle also fails cleanup closed. Process termination/crash may leave staging; there is no background sweeper. Diagnostic messages omit staging names, unrestricted absolute roots, secrets and raw OS exception text.

## Results, diagnostics and compatibility

SUCCEEDED requires full committed receipt with accepted manifest, original compilation association, logical destination, exact ordered descriptor membership/kinds, actual safe relative locations/byte lengths, optional verified declared digest and fulfilled durability policy. Receipt retains no byte payload or temporary location. FAILED/INCOMPLETE retain diagnostics and no receipt; an explicitly visible post-commit destination is distinct from success. Original compiler diagnostics retain object identity and are not re-added when already present in assembly evidence.

Existing CompilationResult remains unchanged in CMP-08. Compiler diagnostics add stable CMP-044..061 and trailing optional typed write_stage/output_location associations, RESULT origin, artifact/manifest/context binding. Existing model projection stays compatible; full raw diagnostic carries writer associations, and CMP-06 diagnostic semantic comparison includes them. No fabricated physical source association or semantic-validation blame.

## Mini Sales — conceptual, not executed

Reuse actual `examples/authoring/mini-sales.json` Customer `sem_550e8400-e29b-41d4-a716-000000000001@1.0.0` and `mini-sales-references.json` Employee `sem_550e8400-e29b-41d4-a716-000000000002@1.0.0`, under the actual sales scope. Prompt `typ_customer_123`/`typ_employee_123` are illustrative aliases and fail current Kernel ID grammar.

Current TypeCompilerPass emits CompiledTypeIR envelopes, not final runtime byte artifacts. Artifact-build without a real approved final producer remains INCOMPLETE. No writer success/file/digest is demonstrated or fabricated.

A future approved target can produce original Customer/Employee artifacts with existing kind metadata, immutable defined bytes and a matching complete original CMP-07 assembly. Explicit mappings `customer.bin`/`employee.bin` plus a trusted sales root then yield a planned complete set. Missing Employee source rejects CMP-047 before staging; `../../outside/customer.bin` rejects CMP-050; shared location CMP-051; later Employee I/O prevents partial commit; an existing destination CMP-053 preserves old output. Only real complete verified commit produces a receipt. This neither publishes, activates, deploys nor executes the artifacts.

## Deferred verification

[The sole detailed archive](../../test-archive/CMP-08/CMP-08-deferred-tests.md) has **158** scenarios covering all requested positive/negative/collision/security/failure/concurrency/integrity/durability/edge/framework/Mini Sales/boundary cases. Tests implemented/executed **0**. No producer fixture, automated test, scenario script, smoke materialization or CLI/runtime execution is introduced. Syntax/build/architecture/import checks are separate and cannot establish behavioral correctness.
