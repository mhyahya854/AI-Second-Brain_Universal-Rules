<a id="s12"></a>
## 12. Storage and crash consistency

<a id="store-1"></a>
### 12.1. STORE-1 — Explicit storage contracts

**Type:** CONDITIONAL | **Origin:** DERIVED ENGINEERING RULE | **Applies:** persistence backends

Each backend MUST document crash-consistency, acknowledgement, concurrency, and recovery contracts and supporting failure assumptions. Protect retained state against the interruptions the application claims to tolerate, and disclose limits instead of promising immunity to arbitrary hardware, software, or adversarial failures.

Visibility, atomicity, durability, replication, and external completion differ. Define consistency units and observers of intermediate state. Larger workflows may expose recoverable intermediate states rather than use one global transaction. Logical rollback need not restore every physical byte to an earlier layout.

Storage MUST fit workload, transaction, concurrency, and recovery needs; a product name is not evidence. Open text and documented binary formats are valid. Parquet is an open binary columnar format, not human-readable text.

<a id="store-2"></a>
### 12.2. STORE-2 — Mechanisms follow the contract

**Type:** RECOMMENDATION | **Origin:** DERIVED ENGINEERING RULE | **Applies:** storage implementation choices

Implementations SHOULD use proven engine protocols where suitable. ACID transactions, copy-on-write, append logs, journals, transactional object stores, engine-native updates, and atomic replacement are possible mechanisms. No file algorithm is required for every write.

For a replaceable file on a backend with suitable semantics, an illustrative sequence is: create a unique temporary file on the required filesystem; serialize and check writes; synchronize as required; publish through a supported replace/rename operation; synchronize directory metadata where required; recover interrupted work. It also needs safe temporary-file creation, race protection, metadata/permission handling, and failure classification. Same-filesystem placement is not proof of full crash durability. Windows APIs, sharing modes, and filesystems need qualification; a replacement flag is not a universal guarantee.

Append stores and databases may use different protocols, including protected in-place page updates. An intent journal alone does not provide atomic multi-file behavior: durable ordering, commit markers, reader visibility, partial application, and recovery need a complete protocol.

