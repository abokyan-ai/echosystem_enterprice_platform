# ADR-0042 — Runtime artifact loading without compiler coupling or fabricated capabilities

Date: 2026-10-11. Status: accepted for implementation; behavioral verification deferred.

CMP-07/08/09 are actually compiler-owned in this repository. Runtime currently imports only Kernel/compiled-contracts; there is no authenticated loading API, approved runtime payload format/decoder or publisher. Moving compiler structures into Runtime or granting Runtime a compiler dependency would violate existing dependency direction.

Keep existing compiler manifest/receipt/reader contracts and filesystem implementation unchanged. Introduce a constrained tooling composition module that retains their original association, reuses CMP-09 planning/reading and projects only bound artifact coordinates/evidence into pure runtime contracts. Add a trailing optional shared producer content declaration to distinguish kind, encoding/version and runtime compatibility; approve no actual format automatically.

Runtime v0 requires complete ALL selection and verified SHA-256 receipt evidence. Inject authenticated authorization through a trusted application port, default unavailable. Bind decisions to the exact source invocation/context/runtime target/full artifact scope, before any byte retrieval. Checksums and manifest availability grant no authority. Preserve independent internal dependencies in manifest order, including permitted reference cycles; do not solve semantic graphs or activate services.

Explicit immutable decoder approvals require concrete frozen representation graph types and bounded parsing before allocation. An empty default catalog fails closed; there is no guessed JSON/IR decoder. Coordination validates approved representation graphs and all identity/context/origin/resource requirements, then emits only a complete immutable inactive loaded set. Structured runtime diagnostics retain ordered original reader causes; tooling also retains exact original CMP diagnostic objects. Expected load failures are structured; unexpected programming faults propagate.

Django/DRF remain the selected backend boundary; neither is installed and no existing authenticated HTTP workflow applies. Introduce no speculative endpoint, ORM model, database/migration or framework import in Runtime. Future adapter composition must supply real authentication/authorization and owned decoder capabilities before production loading can succeed.

Consequences: one explicitly registered tooling module, no runtime zone relaxation or exception; existing manifest identity and source ownership remain in process. SHA-256 is integrity evidence, not authenticity. Decoder safety approval is trusted configuration, not a sandbox; structural budgets do not prove exact memory/latency. Cross-source result equivalence and domain-specific decoder schemas remain unsupported until their actual contracts exist. No producer, encoder, activation, execution, publication or RUN-02 work.

[Contract and Mini Sales](../../runtime/runtime-artifact-loader.md); [deferred archive](../../../test-archive/RUN-01/RUN-01-deferred-tests.md). Tests created/executed: 0; **DEFERRED / NOT VERIFIED**.
