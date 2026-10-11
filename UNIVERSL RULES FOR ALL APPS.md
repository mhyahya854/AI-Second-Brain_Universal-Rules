# Universal Rules for All Apps

> Version: 1.0.0-rc1<br>
> Status: V1.0 Ratification Candidate — Not Yet Ratified<br>
> Date: 2026-10-11<br>
> Document identifier: ECOSYSTEM-CONST-001<br>
> Source repository: https://github.com/mhyahya854/Universal-Rules<br>
> Governance authority: repository owner/user, unless explicitly delegated<br>
> Integration baseline: `c2fd9e3d8ac8c41a2ec1e336d2ec097314ef80a5`

This constitution governs ecosystem software through engineering invariants, deliberate ecosystem policies, and capability-specific requirements. It is a candidate for further adversarial verification and owner ratification. Preparing or committing it does not ratify it or establish compliance of any application.

## Contents

1. [Scope and rule classification](#s01)
2. [Foundations and domain hazards](#s02)
3. [Definitions](#s03)
4. [Principals and delegation](#s04)
5. [Rust-first implementation](#s05)
6. [Feature-first architecture and process boundaries](#s06)
7. [Data lifecycle and application replacement](#s07)
8. [Authority, derivation, and reproducibility](#s08)
9. [Local and offline operation](#s09)
10. [Portability, paths, and supported targets](#s10)
11. [NAS support](#s11)
12. [Storage and crash consistency](#s12)
13. [Concurrency and conflict semantics](#s13)
14. [Operation outcomes and acknowledgements](#s14)
15. [Retries and deduplication](#s15)
16. [AI authority, tools, and memory](#s16)
17. [Audit and provenance](#s17)
18. [Privacy, retention, and deletion](#s18)
19. [External editing and drift](#s19)
20. [Synchronization](#s20)
21. [Reversal and recovery](#s21)
22. [Backup and restoration](#s22)
23. [Import and export](#s23)
24. [Schema evolution and migrations](#s24)
25. [Security, secrets, and dependencies](#s25)
26. [Configuration, observability, and runtime lifecycle](#s26)
27. [Verification and evidence](#s27)
28. [Documentation, exceptions, and ratification](#s28)
29. [Anti-pattern index — non-normative](#s29)
30. [Open questions and review probes — non-normative](#s30)

<a id="s01"></a>
## 1. Scope and rule classification

<a id="gov-1"></a>
### GOV-1 — Interpretation and applicability

**Type:** ECOSYSTEM POLICY | **Origin:** USER POLICY | **Applies:** all ecosystem software and constitutional decisions

The scope includes applications, services, background processes, CLI tools, libraries, storage engines, synchronization components, AI tool servers, and development tools. Capability-specific requirements apply when the capability exists or its guarantee is claimed. A stateless formatter does not need a backup engine; an application without AI does not need AI tool tests. A missing capability is not an exception to a conditional rule, but a required ecosystem capability cannot be avoided merely by omitting it.

Each rule has a stable ID, type, origin, and applicability statement. Every rule in this version inherits **Ratification status: CANDIDATE**. A user-directed policy's inclusion does not ratify the entire candidate. Future revisions MUST record status separately from the other dimensions.

| Independent dimension | Values and meaning |
|---|---|
| Ratification status | RATIFIED, CANDIDATE, PROPOSED, DEPRECATED: adoption status, not technical certainty. |
| Rule type | UNIVERSAL INVARIANT, ECOSYSTEM POLICY, DEFAULT, CONDITIONAL, RECOMMENDATION, PROHIBITION. |
| Origin / provenance | USER POLICY, ARCHITECTURAL DECISION, DERIVED ENGINEERING RULE, EXTERNAL STANDARD / REQUIREMENT. An external origin needs an identified source and applicability; none is invented here. |
| Applicability | Relevant capabilities, resources, actors, and assumptions, recorded even when the type is CONDITIONAL. |
| Normative strength | MUST / MUST NOT: mandatory; SHOULD: default or recommendation; MAY: valid option. |

A UNIVERSAL INVARIANT expresses a language- and platform-independent outcome within its stated assumptions. ECOSYSTEM POLICY is an intentional choice, not a law of computer science. DEFAULT is presumptive architecture with a reasoned alternative path. CONDITIONAL is mandatory when its trigger holds. RECOMMENDATION is advice requiring no formal exception when declined. PROHIBITION forbids a sufficiently harmful pattern and requires extraordinary, explicit approval for an exception.

MUST describes candidate conformance, not proof of adoption. Examples, implementation notes, ADR rationale, and historical reviews add no normative obligations. Sections 3, 29, and 30 are interpretive or informative and defer to governing rules. Deviations and conflicts follow [GOV-3](#gov-3); approval cannot make an unsupported technical guarantee true.

<a id="s02"></a>
## 2. Foundations and domain hazards

<a id="safe-1"></a>
### SAFE-1 — Integrity and truthful guarantees

**Type:** UNIVERSAL INVARIANT | **Origin:** DERIVED ENGINEERING RULE | **Applies:** operations and retained information governed by an application contract

Applications MUST protect retained user data according to declared integrity and lifecycle contracts and MUST NOT silently corrupt it or misrepresent known loss. Intentional loss, transformation, or deletion requires applicable authority and accurate semantics. Important operation outcomes MUST be truthful under [OUT-1](#out-1). Guarantees require appropriate evidence under [TEST-1](#test-1), with limits and uncertainty disclosed.

<a id="safe-2"></a>
### SAFE-2 — Domain-aware hazard decisions

**Type:** UNIVERSAL INVARIANT | **Origin:** DERIVED ENGINEERING RULE | **Applies:** conflicts among safety, security, privacy, integrity, and operational obligations

Applications MUST identify material domain hazards and applicable obligations and resolve conflicts on that basis. A global ranking MUST NOT force data preservation when it creates greater human, physical, security, or privacy harm or defeats applicable erasure duties. Emergency shutdown, credential revocation, and containment can require intentional interruption or loss. Record consequential tradeoffs and residual risks proportionately.

Example: a hardware controller may stop an actuator before persisting telemetry; an archive may prioritize retention under a legitimate preservation duty. Neither priority becomes a universal ordering for other domains.

<a id="safe-3"></a>
### SAFE-3 — Explicit, testable core behavior

**Type:** DEFAULT | **Origin:** DERIVED ENGINEERING RULE | **Applies:** domain logic and authoritative decisions

Domain logic SHOULD make inputs, constraints, and transitions explicit and testable. Isolate or record time, randomness, observations, and model outputs where needed for claimed reproducibility. Randomized algorithms and probabilistic domain functions are permitted. Deterministic code is not proof of correctness; total system determinism is not required. Effective enforcement follows [AUTH-1](#auth-1).

<a id="s03"></a>
## 3. Definitions

| Term | Meaning |
|---|---|
| Canonical state | Authoritative state for a defined system purpose. It can be false, disputed, imported, machine-observed, AI-generated, or jointly controlled; authority does not mean factual verification. |
| Derived artifact | An artifact produced from other inputs. Origin does not establish authority, reproducibility, disposability, or retention value. |
| Retained data | Information promised preservation for a defined purpose and lifecycle, which may include finite retention. |
| Principal | An identity or entity under whose authority an operation is permitted: owner, workspace owner, administrator, service account, or delegate. Data-subject rights can constrain authority without granting every operational permission. |
| Actor | The initiator: human UI/CLI, AI, automation, importer, sync worker, migration, recovery process, integration, or device event. |
| Mechanism | The interface, tool, protocol, scheduled path, or other route by which the operation arrives. |
| Delegation | Granted authority bounded by resources, effects, duration, conditions, and revocation semantics. |
| Authoritative mutation pathway | An execution path enforcing applicable authority and integrity constraints, consistency semantics, required evidence, and outcomes. It need not be one service or language. |
| Modular monolith | A cohesive application deployment with explicit internal modules; those modules do not provide the same isolation as protected processes. |
| NAS | A private storage/server environment accessed through one or more modes in [NAS-1](#nas-1), not synonymous with mounting raw database files. |
| Drift | A relevant change outside the expected mutation/synchronization path; detection does not establish authorship or malicious intent. |
| Atomicity | Indivisibility within a stated consistency boundary and observer model, distinct from durability and external completion. |

<a id="s04"></a>
## 4. Principals and delegation

<a id="auth-1"></a>
### AUTH-1 — Effective authorization and integrity enforcement

**Type:** UNIVERSAL INVARIANT | **Origin:** DERIVED ENGINEERING RULE | **Applies:** effects subject to authorization or integrity constraints

Permissions, domain constraints, and effect limits MUST be enforced at a boundary callers cannot silently bypass within the declared threat model. Hidden UI controls and prompts alone are insufficient. Interfaces may differ in authentication, privileges, quotas, rate limits, confirmation, and scope; they MUST NOT introduce an unacknowledged bypass of applicable integrity constraints. Administrative operations need explicitly authorized semantics.

Enforcement can reside in functions, databases, services, sandboxes, operating-system boundaries, or combinations. An in-process convention does not establish protection against a malicious same-account process or host administrator.

<a id="auth-2"></a>
### AUTH-2 — Ownership, delegation, and attribution

**Type:** UNIVERSAL INVARIANT | **Origin:** DERIVED ENGINEERING RULE | **Applies:** operations requiring authority or accountability

Applications MUST distinguish the relevant principal, actor, mechanism, and delegation. Machine ownership MUST NOT imply ownership of all data or unrestricted authority. Shared ownership, data-subject rights, administration, and tenant boundaries require explicit authority and conflict semantics.

Delegations MUST define relevant resources, allowed effects, duration or lifecycle, conditions, and revocation behavior. Accountability-required operations MUST be attributable to the extent supported by evidence; unknown or externally asserted identity MUST NOT be reported as verified. Queued and long-running actions MUST handle authority changes according to their delegation contract.

<a id="s05"></a>
## 5. Rust-first implementation

<a id="lang-1"></a>
### LANG-1 — Rust as the mandatory ecosystem default

**Type:** ECOSYSTEM POLICY | **Origin:** USER POLICY | **Applies:** new software and components developed in this ecosystem

Rust is the presumptive language for applications, services, background processes, CLI tools, core libraries, storage engines, synchronization components, AI tool servers, and other software. A non-Rust selection MUST document why another language materially better meets the component's requirements and obtain applicable approval under [GOV-3](#gov-3). The burden of justification belongs to the deviation.

The question is: **What concrete technical requirement makes another language materially more appropriate for this component?**

Valid reasons include platform-required SDKs/languages; critical capabilities unavailable or impractical in Rust; host/plugin constraints; specialized scientific/ML ecosystems; interoperability/runtime constraints; deployment requirements; materially safer lifecycle or maintenance outcomes; and scripting, configuration, or generated glue where Rust adds disproportionate complexity without meaningful benefit.

Familiarity, habit, popularity, trendiness, tutorials, framework preference, avoiding Rust's learning curve, or faster personal prototyping are insufficient by themselves. Staffing, qualification, certification, expertise, long-term maintenance, and operational support can justify a deviation when tied to material lifecycle or safety risk.

The decision MUST identify the component, selected language, concrete reason Rust was rejected, why the alternative better meets requirements, and whether scope is one component or the whole application. Polyglot systems are permitted with deliberate, maintainable boundaries. Rust is especially preferred for canonical state, filesystem operations, synchronization, concurrency, long-running services, security boundaries, durable infrastructure, performance-sensitive work, AI capability enforcement, and domain operations.

Rust does not establish domain correctness, storage durability, distributed consistency, safe FFI, secure architecture, or correct concurrency semantics. Those remain architectural responsibilities. This policy does not itself mandate rewriting existing applications. Rationale and examples: [ADR-0001](decisions/ADR-0001-rust-first.md).

<a id="s06"></a>
## 6. Feature-first architecture and process boundaries

<a id="arch-1"></a>
### ARCH-1 — Feature-first organization

**Type:** ECOSYSTEM POLICY | **Origin:** USER POLICY | **Applies:** applications with multiple meaningful user or domain capabilities

Feature-first organization is presumptive. Responsibility ownership, domain/capability boundaries, authoritative-state ownership, shared concepts, dependencies, and cross-boundary effects MUST be understandable and deliberate. A feature MUST NOT silently bypass another feature's applicable invariants. Policy departures require a scoped rationale and approval under [GOV-3](#gov-3).

No fixed folders or files are prescribed. A tiny cohesive utility is outside the multi-capability trigger. Compiler passes, signal-processing pipelines, rendering engines, mathematical kernels, framework layers, hardware-oriented structures, and justified process boundaries are valid where appropriate. Different folder names or fewer layers are not policy exceptions.

<a id="arch-2"></a>
### ARCH-2 — Modular monolith by default

**Type:** DEFAULT | **Origin:** USER POLICY | **Applies:** ordinary feature-rich application deployment

A modular monolith SHOULD be preferred when it is the simplest design satisfying isolation, reliability, privilege boundaries, scaling, deployment, lifecycle, maintainability, and performance. Multiple processes/services may be justified by fault containment, plugin isolation, runtime incompatibility, independent lifecycle, hardware placement, operational economics, reliability, or scaling. Record the rationale; literal single-process impossibility is not required. Distribution adds network, transaction, deployment, and recovery responsibilities.

<a id="arch-3"></a>
### ARCH-3 — Contracts and shared code

**Type:** DEFAULT | **Origin:** ARCHITECTURAL DECISION | **Applies:** modular codebases

Modules SHOULD communicate through explicit interfaces and avoid unnecessary dependency cycles. Build-time cycles and runtime conversations differ. Shared code SHOULD have cohesive responsibility and ownership; substantial shared domain kernels may be appropriate. Choose duplication or reuse by consistency needs and change coupling, not line counts or folder names.

Examples: typed application functions, query ports, commands, events, actor messages, callbacks, streams, and plugin protocols. A feature may contain domain logic, adapters, presentation, tests, and documentation without needing every category. An event bus can conceal coupling and does not by itself prove modularity.

<a id="s07"></a>
## 7. Data lifecycle and application replacement

<a id="life-1"></a>
### LIFE-1 — Preservation across supported replacement

**Type:** UNIVERSAL INVARIANT | **Origin:** DERIVED ENGINEERING RULE | **Applies:** installation, update, replacement, or removal with retained state

Lifecycle operations MUST honor declared preservation and deletion semantics. Retained data, user configuration, required keys, and required evidence MUST NOT be accidentally destroyed by an operation represented as preserving them. Reattachment claims MUST account for schemas, keys, permissions, formats, and required software.

<a id="life-2"></a>
### LIFE-2 — Long-term accessibility

**Type:** ECOSYSTEM POLICY | **Origin:** USER POLICY | **Applies:** information designated for long-term user retention

Applications MUST provide a practicable preservation and exit path beyond a particular runtime or vendor's lifetime, using documented formats, exports, readers, and recovery dependencies as appropriate. This does not require indefinite retention of expiring tokens or deleted content. Host bindings and secrets need an explicit portability/recovery strategy.

<a id="life-3"></a>
### LIFE-3 — Logical storage separation

**Type:** RECOMMENDATION | **Origin:** ARCHITECTURAL DECISION | **Applies:** applications with multiple data lifecycles

Applications SHOULD distinguish replaceable code, retained data, configuration, generated artifacts, audit evidence, operational logs, backups, and exports. Directories, tables, object namespaces, or platform-managed stores may implement the distinction. Executables and data may be colocated if lifecycle operations preserve their contracts.

Roles such as `app/`, `data/`, `config/`, `derived/`, `audit/`, `cache/`, `logs/`, `backups/`, and `exports/` are illustrative. An export is not automatically disposable staging. Git may intentionally store canonical documents; it is not automatically a suitable database or independent backup. Prevent unintended inclusion in unrelated source repositories using suitable ignore rules, controls, and review; `.gitignore` is not an enforcement boundary.

<a id="s08"></a>
## 8. Authority, derivation, and reproducibility

<a id="data-1"></a>
### DATA-1 — Independent state dimensions

**Type:** UNIVERSAL INVARIANT | **Origin:** DERIVED ENGINEERING RULE | **Applies:** state whose authority or lifecycle matters

Applications MUST identify authoritative state and when other representations may be relied on or discarded. Authority, factual verification, provenance, ownership, reproducibility, retention value, recovery cost, sensitivity, and lifecycle MUST NOT be inferred from one another. A generated document may be authoritative and valuable; canonical temporary state may expire. Distributed authority is permitted with defined semantics.

Storage technology does not determine authority: a vector database can hold authoritative originals and embeddings. An expendable cache must not hold the only copy of information promised preservation. Human edits or confirmation do not establish factual correctness of a whole record. Verification claims MUST identify the actual reviewed scope.

<a id="data-2"></a>
### DATA-2 — Honest regeneration claims

**Type:** CONDITIONAL | **Origin:** DERIVED ENGINEERING RULE | **Applies:** artifacts claimed to be rebuildable through generation

Recovery MUST specify its target: identical bytes, semantic equivalence, equivalent functionality or quality, or an acceptable replacement. Exact reproduction claims require preserved dependencies and evidence. If exact artifact identity matters, preserve the artifact for its required lifecycle rather than relying on unproven regeneration.

Account for models, versions, seeds, external inputs, licenses, hardware behavior, cost, and availability where relevant. Non-reproducible outputs and expensive embeddings are not automatically disposable. Derived-state backup is permitted. Synchronous indexes/materialized views are permitted; derivation does not grant authority to mutate canonical records outside [AUTH-1](#auth-1).

<a id="s09"></a>
## 9. Local and offline operation

<a id="offline-1"></a>
### OFFLINE-1 — Useful local operation by policy

**Type:** ECOSYSTEM POLICY | **Origin:** USER POLICY | **Applies:** capability design and network dependencies

Applications SHOULD maximize useful local operation where the domain permits it. They MUST define offline behavior per capability and avoid unrelated cloud dependencies disabling otherwise independent local access. Intentional departures need technical justification under [GOV-3](#gov-3).

Search services, email delivery, streaming, live collaboration, market access, and other remote-native capabilities may need connectivity. Intrinsic documented dependence is not a policy exception. Preserve useful drafts, cached content, or inspection where appropriate; do not imply uncached or remotely authoritative information is current or available.

<a id="offline-2"></a>
### OFFLINE-2 — Safe delayed execution

**Type:** CONDITIONAL | **Origin:** DERIVED ENGINEERING RULE | **Applies:** queued or offline operations

Queueing MUST have domain-safe freshness, expiry, cancellation, authorization, replay, and conflict semantics. Time-sensitive orders, physical commands, or door-unlock actions MUST NOT replay automatically merely because connectivity returns. A domain may reject offline writes, allocate rights in advance, or restrict operations to preserve shared invariants. Distinguish queued intent from completed remote action under [OUT-1](#out-1).

<a id="s10"></a>
## 10. Portability, paths, and supported targets

<a id="port-1"></a>
### PORT-1 — Avoid unnecessary platform lock-in

**Type:** ECOSYSTEM POLICY | **Origin:** USER POLICY | **Applies:** platform and deployment choices

Applications SHOULD preserve portable architecture where practical and MUST document architectural portability, source portability, buildability, tested support, and official support separately. Native/specialized applications may support fewer targets with rationale. A build is not runtime evidence. Windows architectures, macOS architectures, Linux distributions, BSD, mobile, browser, and NAS targets are not one universally required matrix. NAS obligations follow [NAS-1](#nas-1).

<a id="port-2"></a>
### PORT-2 — Portable references and faithful content

**Type:** CONDITIONAL | **Origin:** DERIVED ENGINEERING RULE | **Applies:** filesystem references and portable/interchange data

Hardcoded developer-specific paths in portable logic MUST NOT become runtime assumptions. Absolute paths may legitimately be host bindings, user configuration, filesystem-tool inputs, or audit evidence. Where relocation is promised, references MUST have documented identity/resolution semantics and explicit rebinding for host resources.

Use runtime path APIs where appropriate. Claimed targets require consideration of case behavior, Unicode normalization, reserved names, permissions, links, and collisions. Case-sensitive comparison or a universal sanitizer does not solve these differences. Preserve original names, bytes, and line endings when identity, signatures, fidelity, or user intent requires it; transformations need defined semantics and collision handling.

Example: `attachments/doc1.pdf` can be relative when its base and escaping are specified. `file://attachments/doc1.pdf` places `attachments` in the URI authority; it is not an ordinary relative reference. Reversible mappings can avoid lossy sanitation.

<a id="s11"></a>
## 11. NAS support

<a id="nas-1"></a>
### NAS-1 — Mandatory ecosystem support policy

**Type:** ECOSYSTEM POLICY | **Origin:** USER POLICY | **Applies:** relevant hosting, storage, file-access, service-client, and backup roles

NAS support is intentional. Applicable applications MUST identify and support NAS modes needed for their intended workflow, documenting configurations, concurrency assumptions, disconnection semantics, recovery, and tested guarantees. They MUST NOT silently assume only fast local disks. Supporting one mode does not imply the others.

| Mode | Meaning | Scope of support claim |
|---|---|---|
| 1 — NAS/server hosted | Application runs on a NAS/private server using server-local storage. | Runtime, storage, permissions, resources, and lifecycle. |
| 2 — NAS-hosted service client | Client communicates with an application/database/service on NAS. | Protocol, identity, versions, timeouts, cancellation, retries, and outcomes. |
| 3 — User files on a share | Ordinary documents/media/files accessed through network storage. | File operations, identity, caching, concurrency, disconnection, recovery. |
| 4 — Transactional database over a share | Database files opened directly across SMB/NFS or equivalent. | Engine-supported configuration and verified assumptions under [NAS-2](#nas-2). |
| 5 — Backup destination | NAS holds recovery artifacts. | Consistent capture, transfer, restore, keys, access, and failure-domain limits. |

All five modes are not required. Backup-only support MUST NOT be presented as active shared-data support. A service-mediated design can satisfy active NAS use without shared raw database files. Software with no relevant role may document non-applicability; applicable software omitting NAS support needs an approved exception. Docker is neither necessary nor sufficient for NAS compatibility.

<a id="nas-2"></a>
### NAS-2 — Configuration-specific evidence

**Type:** CONDITIONAL | **Origin:** DERIVED ENGINEERING RULE | **Applies:** claimed NAS modes and network storage

Claims MUST identify engine, protocol, client/server, filesystem, and configuration assumptions with proportionate empirical evidence. Mode 4 MUST be supported only where the engine explicitly supports that configuration and the application's assumptions have been verified. Unsupported configurations MUST be rejected or clearly reported as unsupported, rather than silently accepted as safe.

SMB/NFS locking is configuration- and failure-dependent. Standard SQLite WAL relies on shared-memory coordination and is not a general multi-host SMB/NFS solution; custom VFS behavior needs its own supported contract. A NAS-local database service is a different mode.

`fsync` and `FlushFileBuffers` offer the guarantees implemented by the complete storage stack; server acknowledgements, caches, hardware, and error propagation matter. Oplocks do not alone define stable-storage durability. Permissions depend on identities/ACLs; `0755` and `0644` are not universal privacy settings. Latency assumptions MUST be measured or bounded for the claimed workload, not copied from fixed illustrative numbers.

Access, quota, and free-space preflights improve diagnostics but cannot prove a future operation succeeds. Disconnects may leave outcomes unknown under [OUT-1](#out-1). Timestamp leases and heartbeats without stale-writer exclusion cannot establish safe overlapping access; coordination follows [CON-1](#con-1).

Possible patterns include NAS-local database services, supported transactional engines, ordinary files with bounded semantics, or immutable chunks with a publication protocol. Chunking is not mandatory and does not itself create a transaction.

<a id="s12"></a>
## 12. Storage and crash consistency

<a id="store-1"></a>
### STORE-1 — Explicit storage contracts

**Type:** CONDITIONAL | **Origin:** DERIVED ENGINEERING RULE | **Applies:** persistence backends

Each backend MUST document crash-consistency, acknowledgement, concurrency, and recovery contracts and supporting failure assumptions. Protect retained state against the interruptions the application claims to tolerate, and disclose limits instead of promising immunity to arbitrary hardware, software, or adversarial failures.

Visibility, atomicity, durability, replication, and external completion differ. Define consistency units and observers of intermediate state. Larger workflows may expose recoverable intermediate states rather than use one global transaction. Logical rollback need not restore every physical byte to an earlier layout.

Storage MUST fit workload, transaction, concurrency, and recovery needs; a product name is not evidence. Open text and documented binary formats are valid. Parquet is an open binary columnar format, not human-readable text.

<a id="store-2"></a>
### STORE-2 — Mechanisms follow the contract

**Type:** RECOMMENDATION | **Origin:** DERIVED ENGINEERING RULE | **Applies:** storage implementation choices

Implementations SHOULD use proven engine protocols where suitable. ACID transactions, copy-on-write, append logs, journals, transactional object stores, engine-native updates, and atomic replacement are possible mechanisms. No file algorithm is required for every write.

For a replaceable file on a backend with suitable semantics, an illustrative sequence is: create a unique temporary file on the required filesystem; serialize and check writes; synchronize as required; publish through a supported replace/rename operation; synchronize directory metadata where required; recover interrupted work. It also needs safe temporary-file creation, race protection, metadata/permission handling, and failure classification. Same-filesystem placement is not proof of full crash durability. Windows APIs, sharing modes, and filesystems need qualification; a replacement flag is not a universal guarantee.

Append stores and databases may use different protocols, including protected in-place page updates. An intent journal alone does not provide atomic multi-file behavior: durable ordering, commit markers, reader visibility, partial application, and recovery need a complete protocol.

<a id="s13"></a>
## 13. Concurrency and conflict semantics

<a id="con-1"></a>
### CON-1 — Prevent invalid interleavings

**Type:** CONDITIONAL | **Origin:** DERIVED ENGINEERING RULE | **Applies:** state reachable by concurrent actors/processes

Applications MUST prevent invalid interleavings according to declared consistency semantics. Enforced single-writer access is permitted. Exclusive-access assumptions MUST be enforced or explicitly bounded; a convention alone is not exclusion.

MVCC, serialized services, transactions, optimistic concurrency, CRDTs, append protocols, and storage-enforced fencing are possible mechanisms. Version/hash checks MUST be coupled to transitions when used to prevent races; check-then-write is insufficient. Lease designs MUST prevent stale holders violating promised semantics through storage-enforced fencing or an equivalent protocol, not just heartbeats.

Lock scope/deadlines depend on engine and workload; relational writes do not universally need exclusive database locks. Define cancellation, timeout, and starvation behavior where material to correctness or availability.

<a id="con-2"></a>
### CON-2 — Domain-appropriate conflict resolution

**Type:** CONDITIONAL | **Origin:** DERIVED ENGINEERING RULE | **Applies:** conflicting state changes

Resolution MUST preserve declared semantics and MUST NOT silently discard independently meaningful work contrary to them. Reject/retry, semantic merge, preserved alternatives, domain-approved last-writer-wins, or user decisions are options. A deterministic merge can still violate an invariant.

Lamport clocks order events consistently with causality but do not alone identify concurrency. Vector clocks track causal relationships under protocol assumptions. Hashes indicate content equality/difference, not independent causality. CRDTs provide specific convergence semantics, not arbitrary business-invariant preservation. These mechanisms are not interchangeable.

<a id="s14"></a>
## 14. Operation outcomes and acknowledgements

<a id="out-1"></a>
### OUT-1 — Report what is actually known

**Type:** UNIVERSAL INVARIANT | **Origin:** DERIVED ENGINEERING RULE | **Applies:** important local and external operation results

Results MUST distinguish relevant states: rejection, acceptance, queued intent, local application, local durable commit, remote acknowledgement, external completion, failure before execution, partial execution, or unknown outcome. Exact labels are optional. Acceptance MUST NOT imply completion; remote acknowledgement MUST NOT imply stronger durability/finality than its contract provides.

A timeout, crash, or NAS disconnect can leave success indeterminate. Applications MUST report uncertainty, retain suitable recovery correlation, and reconcile or use a demonstrably safe retry policy. Missing acknowledgement alone MUST NOT be reported as proof of failure. Relevant callers, including AI, need the actual durability/completion boundary.

Example result fields: operation ID, known phase, affected resources, durability scope, external correlation, uncertainty, and allowed next actions. A small utility may convey these semantics through exit status and a concise message.

<a id="s15"></a>
## 15. Retries and deduplication

<a id="retry-1"></a>
### RETRY-1 — Replay safety is a protocol

**Type:** CONDITIONAL | **Origin:** DERIVED ENGINEERING RULE | **Applies:** retried, replayed, or redelivered operations

Contracts MUST distinguish idempotent transitions, request deduplication, replay-safe execution, ambiguous outcomes, and irreversible effects. A new retry identifier does not deduplicate an earlier request.

Key-based protocols MUST define principal/operation scope, persistence, concurrent requests, payload matching, retention, expiry, and result recovery. One key reused for a different intent MUST NOT silently apply a different action. Deduplication state and local effects need sufficient commit consistency for the replay claim. Expiration limits MUST be accounted for.

External duplicate prevention depends on the remote contract; a client key alone cannot provide it. An uncertain external action MUST NOT be retried merely because of a timeout. Status queries, reconciliation, durable intent/outboxes, remote idempotency, cancellation, or human intervention may be appropriate. Attempts may be observable without falsely recording repeated business effects.

<a id="s16"></a>
## 16. AI authority, tools, and memory

<a id="ai-1"></a>
### AI-1 — Explicitly delegated capability

**Type:** UNIVERSAL INVARIANT | **Origin:** USER POLICY | **Applies:** AI actors exercising capabilities

An AI MUST exercise only explicitly delegated capabilities through enforcement it cannot silently bypass within the declared threat model. Effects MUST satisfy applicable authorization, integrity, privacy, safety, and operational constraints. Human/AI interfaces normally share domain-integrity rules under [AUTH-1](#auth-1), without identical privileges or approval policy.

Scoped reads/writes, patches, SQL, shell execution, scratch space, import staging, coding, and bulk operations can be legitimate when intentionally delegated and effectively bounded. Validate scope/effects at execution; a broad tool name or path supplies no authority. Untrusted content and model output MUST NOT grant authority by claiming to be principal instructions.

<a id="ai-2"></a>
### AI-2 — Enforced tool contracts

**Type:** CONDITIONAL | **Origin:** DERIVED ENGINEERING RULE | **Applies:** AI tools, skills, plugins, and capability adapters

A natural-language skill or tool description is not a security boundary. Enforced boundaries MUST provide appropriate validation, authorization, scope restrictions, resource limits, effect constraints, output handling, and relevant accountability. Critical enforceable permissions/integrity rules MUST NOT depend solely on prompt obedience.

Machine-readable contracts SHOULD be used where useful for enforcement or interoperability; JSON Schema/OpenAPI are options, not universal requirements. Structured returns SHOULD expose actionable results and uncertainty; they do not make AI deterministic. Schema-valid intent can still be harmful, requiring semantic policy and effect limits.

<a id="ai-3"></a>
### AI-3 — Risk, delegation, and approval

**Type:** CONDITIONAL | **Origin:** USER POLICY | **Applies:** AI capability exposure and execution policy

Risk MUST consider relevant confidentiality, disclosure, financial/physical effects, irreversibility, sensitivity, scope, cumulative volume, cost, uncertainty, destination, delegation, cancellation, and recovery. A read may reveal secrets, export medical data, upload private files, or fetch attacker-controlled URLs. Mutation status or a record-count threshold does not establish risk.

Approval MUST reflect consequences and actual delegation. Explicitly authorized autonomous consequential or high-volume work is permitted within enforced limits. Interactive confirmation is one control, not a universal prerequisite. Material scope expansion needs new authority, not inferred consent.

When approval relies on a preview, bind it to relevant parameters, resources, versions, scope, expiry, and budgets; revalidate before execution where necessary. Disclose estimates, external dependencies, and stale assumptions. A dry-run does not prove future external effects. Changes invalidating approved scope MUST be rejected, reconciled, or reauthorized according to policy.

<a id="ai-4"></a>
### AI-4 — Memory and provider boundaries

**Type:** CONDITIONAL | **Origin:** DERIVED ENGINEERING RULE | **Applies:** AI state, retained memory, and integrations

Domain consistency MUST NOT depend solely on hidden model memory or ephemeral context. Explicit state follows [DATA-1](#data-1); scratch work need not become permanent history. Retained AI memory MUST have defined inspection, correction, export, access, deletion, and derived-copy lifecycle controls consistent with principals' rights. It MUST NOT silently override authoritative records or policy.

Provider integrations SHOULD isolate replaceable dependencies where useful and declare capabilities. Abstraction reduces coupling, not differences in model quality, interfaces, cost, licensing, or availability. Provider-specific tools may intentionally use unique capabilities. Optional AI failure SHOULD preserve independent functions; AI-native functions may become unavailable with truthful results. Protect retained data and contain failure within stated assumptions rather than promising immunity to all crashes or resource exhaustion.

<a id="s17"></a>
## 17. Audit and provenance

<a id="audit-1"></a>
### AUDIT-1 — Proportionate accountable evidence

**Type:** CONDITIONAL | **Origin:** DERIVED ENGINEERING RULE | **Applies:** operations requiring accountability under domain, policy, or applicable obligations

Applications MUST define required events and an audit contract covering granularity, principal/actor/mechanism, outcome, resources, necessary before/after information, retention, access, redaction, archival, deletion, integrity, and recovery. Evidence MUST support the claim without indiscriminate payload capture. Relevant failures/unknown outcomes MUST be distinguishable from successful effects.

Bulk events may reference an affected set; micro-events may be aggregated if accountability is retained. Model identities may be unknown/provider-reported. Human review records its actual scope. Prompts and free-text reasons need privacy treatment and are not mandatory permanent payloads. Rollback identifiers SHOULD be references rather than enduring bearer authority.

Diagnostics and audit evidence have distinct purposes/lifecycles, without mandatory separate directories. Ordinary correction/reversal should retain its relation to earlier events. Authorized expiry/redaction follows [PRIV-1](#priv-1); append-only semantics do not forbid it.

<a id="audit-2"></a>
### AUDIT-2 — Mutation and evidence commit consistency

**Type:** CONDITIONAL | **Origin:** DERIVED ENGINEERING RULE | **Applies:** evidence required for a committed mutation

Required evidence MUST be atomic, transactionally coupled, or recoverably linked with its committed effect. A crash window between unrelated writes MUST NOT be accepted as fulfilling that contract. Define recovery and how evidence-storage failure affects execution, including safety obligations under [SAFE-2](#safe-2).

Non-normative local example:

```text
validate authority and preconditions
begin transaction
    apply canonical transition
    persist required audit event or recoverable outbox evidence
commit that consistency unit
report the outcome supported by the commit contract
deliver outbox evidence with retry-safe processing where applicable
```

An outbox does not atomically execute a physical or remote API effect. Durable intent, correlation, observed outcome, and reconciliation remain necessary, and outcomes can remain unknown. Recoverable evidence needs sufficient information for the actual obligation; a lossy queue marker is not sufficient by definition.

<a id="audit-3"></a>
### AUDIT-3 — Integrity claims and trust anchors

**Type:** CONDITIONAL | **Origin:** DERIVED ENGINEERING RULE | **Applies:** claims of tamper evidence

Claims MUST identify adversaries, protected references, verification, and recovery limits. Hashes detect changes relative to trusted references; attackers able to replace data and manifests can defeat comparison. Hash chains need protected anchors or independent evidence against wholesale rewriting. Encryption does not itself establish authorization or audit completeness. Authorized redaction/expiry MUST be distinguishable from unexplained alteration within the stated integrity model.

<a id="s18"></a>
## 18. Privacy, retention, and deletion

<a id="priv-1"></a>
### PRIV-1 — Purpose-limited processing and retention

**Type:** UNIVERSAL INVARIANT | **Origin:** DERIVED ENGINEERING RULE | **Applies:** sensitive/personal information collection, processing, disclosure, retention

Processing and retention MUST be limited to authorized purposes and applicable obligations. Audit, provenance, prompts, diagnostics, before/after state, model metadata, backups, and derived copies are included. Full prompts, secrets, personal information, and deleted payloads MUST NOT be retained merely because available.

Deletion/retention policies MUST define scope, timing, protected obligations, replicas, indexes, backups, and known limitations. Logical append-only history may coexist with authorized redaction, expiry, archival, key destruction, and cryptographic erasure. Preserve necessary evidence of lifecycle actions without recreating erased payloads. Restore MUST account for applicable deletion decisions rather than silently reinstating information contrary to policy.

Cryptographic erasure depends on effective key destruction and copies; it cannot recall disclosed plaintext. Soft deletion is not a universal substitute for erasure. Resolve conflicting rights and retention obligations through [SAFE-2](#safe-2) with a documented legitimate basis.

<a id="priv-2"></a>
### PRIV-2 — Local data and deliberate disclosure

**Type:** ECOSYSTEM POLICY | **Origin:** USER POLICY | **Applies:** user-data storage and external transmission

Local machine/private NAS storage is the default. External disclosure MUST have informed authorization appropriate to purpose, destination, data scope, and principal. Standing delegation is permitted without per-request prompts. Remote-native functions follow [OFFLINE-1](#offline-1). Cloud AI requests SHOULD include only necessary relevant context. Local inference MAY help but does not prove other components transmit nothing. Diagnostic exports need sanitization and user control without mandatory manual inspection of every byte.

<a id="s19"></a>
## 19. External editing and drift

<a id="edit-1"></a>
### EDIT-1 — User control and safe adoption

**Type:** CONDITIONAL | **Origin:** USER POLICY | **Applies:** managed files/records accessible outside the ordinary runtime

Users may edit their own Markdown, source, configuration, documents, and open formats subject to legitimate shared rights. Applications MUST define supported edits, validation, adoption, conflicts, and rejection. They MUST NOT silently adopt unsafe state merely because it is in an expected directory. Unsupported edits may be rejected/quarantined without claiming ownership over user files. Reconciliation MUST avoid overwriting newer valid work or destroying the only recoverable copy without authority.

<a id="edit-2"></a>
### EDIT-2 — Proportionate drift detection

**Type:** CONDITIONAL | **Origin:** DERIVED ENGINEERING RULE | **Applies:** storage models where external change affects claimed integrity

Detection MUST fit threats, dataset size, architecture, and acceptable latency. Hashes, versions, watcher hints, database versioning, service boundaries, snapshots, or reconciliation protocols are options; constant all-file hashing is not required. Watchers can miss changes and need validation/rescan strategies where the contract requires it.

Drift does not prove maliciousness or authorship. Snapshots can roll back data and a local manifest together; detection of that rollback needs evidence outside the boundary. Adoption, restoration, merge, preserved alternatives, and user decisions are possible resolutions subject to current-state coordination under [CON-1](#con-1).

<a id="s20"></a>
## 20. Synchronization

<a id="sync-1"></a>
### SYNC-1 — Explicit distributed authority

**Type:** CONDITIONAL | **Origin:** DERIVED ENGINEERING RULE | **Applies:** synchronization or replicas of a logical dataset

Protocols MUST define authority, identity, causal/conflict semantics, disconnected changes, duplicate handling, deletion propagation, and recovery. Peer data MUST pass applicable authority/integrity controls; sync is not a bypass. Preserve origin and propagation identity where needed for accountability.

Offline availability is constrained by invariants: scarce resources may need online coordination or preallocated rights. Convergence is not proof of correctness. Tombstone retention, long-offline replicas, and reintroduction of erased information need explicit lifecycle semantics. Conflicts follow [CON-2](#con-2); delay follows [OFFLINE-2](#offline-2).

<a id="s21"></a>
## 21. Reversal and recovery

<a id="recover-1"></a>
### RECOVER-1 — Honest recovery semantics

**Type:** UNIVERSAL INVARIANT | **Origin:** DERIVED ENGINEERING RULE | **Applies:** undo, restoration, reversal, or compensation claims

Applications MUST describe actual recovery/compensation honestly and provide recovery where technically and operationally appropriate. Distinguish inverse mutation, transaction rollback, restoration, compensation, cancellation, reconciliation, and irreversible actions. Reversal MUST use current authority and constraints, not historical permission alone.

Communications cannot be recalled from recipients' knowledge. Refunds are separate effects; physical actions may be irreversible; APIs may need reconciliation. Restoring old global state MUST NOT be presented as safe undo without accounting for newer valid work. Expired/erased information may not be recoverable. Required reversal audit links to the original under [AUDIT-1](#audit-1).

<a id="recover-2"></a>
### RECOVER-2 — Prefer bounded reversibility

**Type:** DEFAULT | **Origin:** ARCHITECTURAL DECISION | **Applies:** mutations and consequential automation

Operations SHOULD offer scoped undo, reversible preparation, cancellation, or compensation where benefit justifies cost. Soft deletion may help; retention/privacy may require erasure. Communicate irreversible boundaries where relevant. Delegation can authorize automatic execution under [AUTH-2](#auth-2) and [AI-3](#ai-3) without repeated confirmation.

<a id="s22"></a>
## 22. Backup and restoration

<a id="backup-1"></a>
### BACKUP-1 — Complete recovery dependency set

**Type:** CONDITIONAL | **Origin:** DERIVED ENGINEERING RULE | **Applies:** retained state with provided/claimed backup or recovery

Strategies MUST identify a consistent recovery point and complete dependency set for the promised result: potentially data, configuration, keys/key-recovery paths, audit evidence, schemas, readers, migration metadata, expensive derived artifacts, and external dependencies. Secrets need protection and recoverability, not indiscriminate packaging with public exports.

No directory inclusion list or derived-data exclusion applies universally. NAS/filesystem snapshots, OS backup, database-native, or application-native backup may be used. Understand snapshot scope and cross-store consistency. A copy in the same failure domain does not establish independent recovery.

<a id="backup-2"></a>
### BACKUP-2 — Recovery evidence

**Type:** CONDITIONAL | **Origin:** DERIVED ENGINEERING RULE | **Applies:** backup-readiness and recoverability claims

Claims MUST have documented, testable restoration and supporting evidence. Verify intended results, keys/dependencies, compatibility, and meaningful failure cases. Untested backups are unverified, not necessarily empty or legally nonexistent. State recovery-point/time expectations and untested limits.

Manifests/checksums can detect accidental corruption; adversaries may require protected evidence under [AUDIT-3](#audit-3). Verification SHOULD avoid active-data changes and restore tests SHOULD use safe destinations. Actual restore requires authority and accounting for later work/deletion policy.

<a id="s23"></a>
## 23. Import and export

<a id="io-1"></a>
### IO-1 — Controlled ingestion and faithful export

**Type:** CONDITIONAL | **Origin:** DERIVED ENGINEERING RULE | **Applies:** import/export capabilities

Imports MUST validate format/domain constraints, define identity/conflicts, and prevent blind overwrite contrary to intent. Staging, skip, audited replacement, merge, or alternatives may be used. Track needed provenance without unrelated sensitive content.

Exports presented as copies MUST NOT silently mutate/delete sources. An intentional move or export-and-delete needs separate effect semantics and authority. Exports MUST document scope, omissions, transformations, consistency point, and format, distinguishing archival fidelity from presentation. Apply [PRIV-1](#priv-1).

Canonical snapshots, human-readable reports, interchange formats, and diagnostics are useful categories, not four required features. JSON, Markdown, CSV, documented databases, and open binary formats serve different purposes. Scheduled export is optional unless the selected preservation contract relies on it.

<a id="s24"></a>
## 24. Schema evolution and migrations

<a id="migrate-1"></a>
### MIGRATE-1 — Versioned, recoverable evolution

**Type:** CONDITIONAL | **Origin:** DERIVED ENGINEERING RULE | **Applies:** persistent format/schema evolution

Migrations MUST be explicit, versioned, and testable with defined dependencies/order, preconditions, interruption, and recovery. Define exclusive versus online execution, compatibility windows, concurrent writers, rollback/roll-forward, snapshot role, restoration boundary, and failure classification. Resource preflights cannot prove future allocation succeeds.

Consistent snapshots/backups are useful safeguards; a local full copy is not required for every migration. Failure MUST NOT cause unconditional snapshot restoration. Determine whether rollback succeeded, work remains partial, newer writes exist, or forward recovery is needed. Restoration requires authority over the real loss boundary. Restricted/read-only operation may be appropriate during recovery.

Retry safety may come from idempotent steps or a correctly recorded execution protocol. Safe downgrade may be unavailable; do not invent a non-destructive `down()` when information has been lost.

<a id="migrate-2"></a>
### MIGRATE-2 — Semantic compatibility

**Type:** CONDITIONAL | **Origin:** DERIVED ENGINEERING RULE | **Applies:** evolving persistent formats and protocols

Compatibility MUST be explicit. Unknown fields/new semantics MUST NOT be silently accepted then destroyed or misinterpreted. Define readable, preservable, transformable, and writable versions; reject unsafe writes or require supported migration. Liberal acceptance is not a blanket persistence rule. Tolerant reading may work when content is preserved safely and constraints remain understood.

<a id="s25"></a>
## 25. Security, secrets, and dependencies

<a id="sec-1"></a>
### SEC-1 — Threat-based boundaries and exposure

**Type:** CONDITIONAL | **Origin:** DERIVED ENGINEERING RULE | **Applies:** resources exposed to actors or networks

Controls MUST reflect principals, reachable surfaces, protocols, deployment, and threats, including relevant local processes, supply-chain inputs, network devices, and prompt injection. Localhost, LAN, or VPN membership alone does not establish application identity/authority. Least privilege means minimum effective authority for the role; backup/credential workers can need broad controlled access.

Local apps SHOULD bind local services to loopback by default. Network services may use intended interfaces, including containers, with explicit secure deployment. Authentication, authorization, transport protection, browser-origin defenses, and rate limits MUST match exposed operations/data. Deliberately public data may have public access semantics; private LAN location does not justify sensitive unauthenticated access. CORS/WAFs are not universal protocol controls; CORS is not general authorization.

<a id="sec-2"></a>
### SEC-2 — No accidental secret disclosure

**Type:** PROHIBITION | **Origin:** DERIVED ENGINEERING RULE | **Applies:** secrets and security credentials

Applications MUST NOT disclose usable secrets through unintended source control, logs, prompts, exports, or interfaces. Storage/delivery MUST match threats and permit appropriate revocation/rotation. Credential stores, managed services, protected configuration, and environment injection are options. Restricted plaintext local files may suit a bounded threat model; they do not isolate all same-account processes. Environment variables also have exposure paths.

Ignore rules and permissions are not complete access or history-erasure controls. Disclosures need appropriate containment, including revocation where needed. Removing a file from a current tree does not remove every historical copy.

<a id="sec-3"></a>
### SEC-3 — Dependency and build discipline

**Type:** ECOSYSTEM POLICY | **Origin:** ARCHITECTURAL DECISION | **Applies:** released application builds and third-party dependencies

Released builds MUST record a reproducible dependency-resolution strategy appropriate to their toolchains, preserving integrity/trust checks. Library version ranges may coexist with reproducible test/release environments. Assess dependencies by function, provenance, maintenance, vulnerabilities, license, transitive cost, and replacement feasibility. Short handwritten security/parsing code is not inherently preferable.

Use supported lock/resolution mechanisms and review updates. `go.sum` records checksums; it alone is not an exact Go dependency lock model, which also involves `go.mod` and resolution semantics. Rust ownership checks and `Cargo.lock` do not establish trust. Vulnerability review SHOULD be proportionate and recurring; CVE scans cannot prove absence of defects.

<a id="s26"></a>
## 26. Configuration, observability, and runtime lifecycle

<a id="run-1"></a>
### RUN-1 — Explicit configuration and defaults

**Type:** DEFAULT | **Origin:** ARCHITECTURAL DECISION | **Applies:** configurable applications

Applications SHOULD separate environment-specific settings from portable logic and define deterministic resolution/validation. Built-in defaults are legitimate. CLI, environment, deployment file, user preferences, defaults is an illustrative order; managed policy may be non-overridable. Surface relevant effective non-secret settings and use supported host discovery or explicit configuration. Changing configuration does not imply environments have equivalent capabilities.

<a id="run-2"></a>
### RUN-2 — Proportionate diagnostics

**Type:** CONDITIONAL | **Origin:** DERIVED ENGINEERING RULE | **Applies:** failure reporting and operations

Applications MUST provide sufficient outcome/failure information without unnecessary sensitive exposure. Expected conditions differ from faults; a best-effort cleanup failure may need no stack trace, but material loss or a failed commit MUST NOT be hidden. Logs need bounded resources and appropriate retention.

Structured logging, correlation IDs, metrics, and health endpoints SHOULD be used where helpful; short-lived tools may need only exit status and diagnostics. Separate liveness, readiness, and deeper checks. Ordinary probes SHOULD be lightweight/non-destructive. Read-only probes cannot guarantee future writes; deliberate synthetic writes need explicit scope and cleanup.

<a id="run-3"></a>
### RUN-3 — Declared deployment and bounded lifecycle

**Type:** CONDITIONAL | **Origin:** DERIVED ENGINEERING RULE | **Applies:** supported deployment modes and persistent services

Applications MUST document supported runtime modes. Native binaries, desktops, mobile/browser runtimes, services, and OCI images are options, not universal simultaneous requirements. Container identities, mounts, permissions, and isolation must fit their role; packaging does not establish NAS semantics.

Startup MUST verify prerequisites for safe operation, including relevant schema compatibility/exclusivity. Read-only software need not demand writable canonical storage. Preflight success does not replace runtime handling. Shutdown SHOULD stop new work, complete or safely interrupt work, and flush/close according to contract within appropriate bounds. Crash safety cannot depend solely on graceful shutdown. Exit status and diagnostics MUST reflect material failures; process exit alone does not prove effects completed.

<a id="s27"></a>
## 27. Verification and evidence

<a id="test-1"></a>
### TEST-1 — Evidence appropriate to the claim

**Type:** UNIVERSAL INVARIANT | **Origin:** DERIVED ENGINEERING RULE | **Applies:** claimed application guarantees

Applications MUST verify claims with evidence appropriate to scope, risk, and failure model. Important claims require relevant failure, recovery, concurrency, migration, portability, security-boundary, AI-capability, and NAS-mode checks where those capabilities exist. Record tested configurations and distinguish passed, failed, skipped, unrun, and unsupported outcomes. A syntactic checklist does not prove semantics.

Non-AI apps need no AI tests; stateless formatters need no backup tests; NAS backup does not imply raw network-database support. Reuse engine/platform evidence only within its assumptions and verify integration. Tests reduce uncertainty rather than establish absence of all defects.

<a id="test-2"></a>
### TEST-2 — Practical verification patterns

**Type:** RECOMMENDATION | **Origin:** DERIVED ENGINEERING RULE | **Applies:** development/release verification choices

Automation SHOULD cover critical transitions, interfaces, interruption points, authority boundaries, and representative workflows. Examples: concurrent edits, stale lease holders, disconnect after commit before acknowledgement, audit/outbox recovery, deletion then restore, incompatible schemas, and revoked queued authority. Use actual targets where needed; an emulator cannot certify every NAS appliance.

A shared conformance harness MAY help inspect declared applicability, links, schemas, and selected guarantees. It SHOULD measure behavior rather than prescribed filenames. Destructive tests need isolated fixtures and scope; a documentation rule does not authorize inspection or mutation of unrelated applications.

<a id="s28"></a>
## 28. Documentation, exceptions, and ratification

<a id="gov-2"></a>
### GOV-2 — Proportional living contracts

**Type:** ECOSYSTEM POLICY | **Origin:** USER POLICY | **Applies:** ecosystem repositories

Documentation MUST describe actual behavior, guarantees, assumptions, support, and limits. A concise README can cover a tiny tool; larger systems need relevant ownership maps, storage/authority contracts, AI capabilities, NAS configurations, recovery/migration, deployment, and evidence. Unimplemented aspirations MUST NOT be presented as existing behavior.

Machine-readable contracts SHOULD be maintained where they improve interoperability/enforcement. Schema generation reduces drift but does not prove runtime semantic or authorization agreement. Record significant tradeoffs and governing clauses. This constitution is primary; ADRs, reviews, and examples cannot silently strengthen it.

<a id="gov-3"></a>
### GOV-3 — Policy authority and exceptions

**Type:** ECOSYSTEM POLICY | **Origin:** USER POLICY | **Applies:** policy decisions, deviations, and ratification

The repository owner/user is ultimate policy and ratification authority unless explicitly delegated. AI reviewers may recommend, challenge, draft, and verify, but cannot independently ratify. No governance board is presumed.

Formal exceptions to ecosystem policies, prohibitions, explicitly mandatory defaults, or genuine exceptional conflicts involving invariants MUST record rule ID, component/scope, technical reason, risk, mitigation, relevant duration/permanence or review trigger, and actual approving authority with approval evidence. Proposed exceptions are not approved. Scoped prior delegation can authorize decisions without repeated prompts.

Ordinary DEFAULT alternatives need a proportionate rationale, not impossibility proof or formal exception unless their clause expressly requires one. RECOMMENDATION alternatives need no exception. Material CONDITIONAL non-applicability should be documented without requiring approval. Rust-first and applicable NAS/feature-first departures follow formal policy governance; folder-name variation within feature-first does not.

An exception MUST NOT present an unmet engineering guarantee as satisfied. A real domain conflict needs revised scope, affected claims, residual risk, and authority under [SAFE-2](#safe-2). Approval cannot waive physical constraints or applicable legal obligations by declaration.

<a id="gov-4"></a>
### GOV-4 — Reviewable evolution

**Type:** ECOSYSTEM POLICY | **Origin:** USER POLICY | **Applies:** constitutional changes and adoption

Changes MUST preserve reviewability through recorded versions, rationale, affected rule IDs, and evidence. Candidate status MUST remain explicit until owner ratification. Adoption should identify exact revision and applicability date. Preserve historical reviews rather than rewriting findings to fit the result. Substantive changes need appropriate adversarial review and disposition. Changes here do not authorize automatic migration or assessment of governed repositories.

Supporting records: [Rust ADR](decisions/ADR-0001-rust-first.md), [historical review](reviews/2026-10-astra-adversarial-review.md), [integration disposition](reviews/2026-10-rc1-integration-disposition.md), [changelog](CHANGELOG.md), [historical attestation](provenance/initial-generation-boundary.md). Historical section numbers refer to their baseline, not this candidate.

<a id="s29"></a>
## 29. Anti-pattern index — non-normative

This navigation index adds no requirements. Applicability, strength, and exceptions remain those of the governing clauses.

| Warning sign | Governing clause |
|---|---|
| Accepted/uncertain operation reported as known final completion | [OUT-1](#out-1) |
| UI controls or prompts treated as effective permission enforcement | [AUTH-1](#auth-1), [AI-2](#ai-2) |
| Untrusted content grants AI new authority | [AI-1](#ai-1) |
| Read-only label or record count used as complete risk model | [AI-3](#ai-3) |
| Expendable cache holds the only copy promised preservation | [DATA-1](#data-1) |
| Generated artifact assumed disposable or exactly reproducible | [DATA-2](#data-2) |
| Application replacement accidentally deletes retained data | [LIFE-1](#life-1) |
| One write algorithm prescribed without backend failure semantics | [STORE-1](#store-1) |
| WAL, hashes, or unfenced leases treated as sufficient NAS safety | [NAS-2](#nas-2), [CON-1](#con-1) |
| Docker or backup-only support presented as all NAS modes | [NAS-1](#nas-1) |
| Required evidence written independently after mutation commit | [AUDIT-2](#audit-2) |
| Attacker-rewritable manifest presented as protected anchor | [AUDIT-3](#audit-3) |
| Permanent sensitive retention justified only by auditability | [PRIV-1](#priv-1) |
| Migration failure blindly restores over newer work | [MIGRATE-1](#migrate-1) |
| Unknown persistent semantics accepted then destroyed | [MIGRATE-2](#migrate-2) |
| Recovery claimed without restoration evidence | [BACKUP-2](#backup-2) |
| Loopback or VPN treated as complete authorization | [SEC-1](#sec-1) |
| Invariants bypassed or distribution introduced without rationale | [ARCH-1](#arch-1), [ARCH-2](#arch-2) |
| Unjustified non-Rust implementation | [LANG-1](#lang-1) |
| Unsupported or untested targets presented as verified | [TEST-1](#test-1), [PORT-1](#port-1) |

<a id="s30"></a>
## 30. Open questions and review probes — non-normative

Rust-first, feature-first preference, mandatory applicable NAS support, local/offline-first preference, and owner governance are decided policies for this integration. Universal event sourcing, one database, per-action confirmation, and a fixed platform matrix are not pending requirements: scoped rules above replace them.

Remaining ratification work is further adversarial verification of this candidate and the owner's adoption decision on its exact revision. No unapproved global encryption-at-rest mandate or fixed audit retention period is introduced. Application-specific threat models, legal obligations, support matrices, NAS configurations, and recovery targets remain application decisions, not unresolved universal-policy placeholders.

Useful illustrative review probes:

- Can required audit evidence recover after failure at each commit boundary?
- Can stale writers, previews, revoked delegations, or expired deduplication keys violate effect limits?
- Can restore reintroduce erased information or hide loss of newer work?
- Does NAS support distinguish hosting, service access, files, raw database access, and backups?
- Can tiny tools avoid irrelevant subsystems while large collaborative systems retain meaningful guarantees?
- Are examples or recommendations being used as hidden prohibitions?

These probes do not replace claim-specific evidence under [TEST-1](#test-1).
