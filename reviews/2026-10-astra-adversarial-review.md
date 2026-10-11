# Pre-Ratification Adversarial Review

Historical review supplied in this Codex conversation on 2026-10-11. Preserved below without revising its findings to match the integration. The filename follows the requested repository convention; it does not independently attest a reviewer model identity. Section numbers refer to the original constitution at `c2fd9e3d8ac8c41a2ec1e336d2ec097314ef80a5`, not the candidate. This record is non-normative.

---

## VERDICT

**MATERIAL ARCHITECTURAL FLAWS**

The draft contains defensible goals, but several mandatory mechanisms undermine those goals. The most serious problems concern crash-consistent auditing, NAS concurrency, migration recovery, irreversible actions, privacy, and the distinction between authoritative data and factual truth.

This is more than a classification problem. An implementation could comply with the draft and still lose concurrent updates, acknowledge changes without durable audit records, erase newer data during migration recovery, or retain sensitive information indefinitely.

The supplied **Rust-first policy is defensible as an ecosystem policy**. It is not a universal engineering truth, and it conflicts with §43’s unrestricted language choice. Its documented, component-specific exceptions make it substantially more defensible than many absolute rules in the constitution.

This review used only the named constitution and your supplied policy. No project implementations were inspected, no files were changed, and no empirical storage or platform tests were performed. Technical findings below distinguish conceptual failures from claims requiring platform-specific verification.

## CONSTITUTIONAL INVARIANTS THAT SURVIVED ATTACK

These are the defensible cores of existing rules. Several survive only after removing the draft’s absolute guarantees or prescribed mechanisms.

| Principle | Strongest attempted counterexample | Why it survives |
|---|---|---|
| **Do not silently misrepresent data loss, corruption, or operation results** — §§4, 18, 28, 30 | An application intentionally discards temporary data or uses lossy compression. | Intentional, disclosed loss can be part of the contract. Undisclosed loss contrary to that contract cannot. The invariant concerns promised semantics, not preservation of every byte forever. |
| **Enforce applicable authorization and integrity constraints at an effective execution boundary** — §§4.1, 12–14 | A 100-line CLI or browser-only application has no separate domain-service layer. | The boundary can be a function, transaction, sandbox, or operating-system capability. Separate architectural layers are unnecessary; effective enforcement remains necessary. |
| **An AI must not silently obtain authority beyond its delegation** — §§12.3, 13, 23 | A coding agent legitimately needs filesystem access, shell commands, and patches. | Those capabilities can be explicitly delegated and scoped. Their breadth does not justify silent escalation or bypassing applicable protections. |
| **Do not make prompt obedience the sole enforcement of critical constraints** — §§13.1, 39.2 | An AI classifier necessarily makes probabilistic judgments. | Probabilistic judgments may be authorized inputs. Permissions, resource limits, allowed effects, and acceptance criteria still need enforcement outside the model where enforceable. |
| **Identify which state is authoritative and which copies may be discarded** — §§7, 39.5 | A distributed collaborative system has no single master node. | Authority can be distributed according to a defined protocol. The invariant requires explicit semantics, not one database or one writer. |
| **Protect retained user data across supported application replacement operations** — §§4.2, 6 | A mobile user explicitly requests “uninstall and delete all data.” | Explicit deletion is compatible with sovereignty. Accidental deletion during an operation represented as preserving data is not. |
| **Validate externally supplied state before relying on its integrity** — §§17, 21 | A text editor treats externally edited documents as normal inputs. | It need not quarantine every edit. It must still handle malformed, stale, or incompatible inputs safely under its documented format contract. |
| **Represent conflicts according to explicit domain semantics** — §§18, 22, 29 | A collaborative preference uses a last-writer-wins register. | That is defensible when overwriting is the intended semantics. Silent destruction of independently meaningful content is different. |
| **Recovery claims require recovery evidence** — §§20, 34 | A utility delegates backups to an operating-system service. | It need not implement a backup engine. Any claim that its data is recoverable must account for the actual restore path and dependencies. |
| **Preserve a practicable exit path for retained user data** — §§4.2, 21 | A huge media archive cannot be converted into human-readable text. | Documented binary formats, compatible readers, export tools, and preserved keys can provide an exit path. Human readability is not necessary. |
| **Match exposure and privilege to authorized purpose** — §§25–27 | A backup daemon needs broad read access; a public server needs external network access. | Those privileges can be necessary. Unexplained or accidental authority remains unjustified. |
| **Verify the guarantees the application actually promises** — §§34–35 | A tiny stateless formatter has no database, AI, or backup subsystem. | Its verification should cover formatting and failure behavior. It need not manufacture nonexistent subsystems to satisfy a checklist. |

**What did not survive:** “100% deterministic,” “permanent audit,” “all files use atomic replacement,” “every entity has a version number,” and “every application supports all deployment targets” are not equivalent to these principles.

## RULES THAT SHOULD BE DOWNGRADED

`E` below means the draft labels the provision `[ESTABLISHED]`; `P` means `[PROPOSED / DERIVED]`. Those labels assert provenance, not technical validity. The document supplies no decision records sufficient to independently establish most claimed prior agreements.

| Section and current classification | Recommended classification | Strongest counterexample | Corrected principle |
|---|---|---|---|
| **§4.2 — E; 30-year preservation assumption** | **Ecosystem policy**, scoped by retention purpose | A password reset token, temporary voice buffer, or deliberately expiring message should not survive 30 years. | Design retained lifetime data for long-term accessibility; classify transient and expiring information separately. |
| **§§4.3, 28.1 — E; complete determinism** | **Default architecture**, with conditional reproducibility requirements | Cryptographic randomness, hardware sampling, randomized algorithms, and concurrent scheduling are legitimate. | Make authoritative rules explicit and testable; isolate nondeterministic inputs where useful. Determinism alone does not establish correctness. |
| **§5.1 — E; modular monolith by default, decomposition only for necessity** | **Default architecture** | A plugin host isolates untrusted plugins in child processes although a single process is technically possible. | Prefer the simplest deployment meeting isolation, reliability, operational, and organizational needs; justify distribution without requiring impossibility. |
| **§§5.2–5.3 — E; prohibited top-level layers and directory per capability** | **Default architecture / scaling guidance** | A compiler, rendering engine, numerical library, or tiny CLI may be clearer as staged or technical modules. | Require understandable responsibility boundaries; use feature-oriented organization where it reflects the domain. |
| **§5.4 — E; shared code must be tiny and domain-agnostic** | **Recommendation** | A substantial, coherent geometry kernel or accounting shared kernel may appropriately dominate an application. | Govern shared ownership and dependency direction; judge cohesion and change coupling rather than folder size or domain neutrality. |
| **§5.5 — P; exactly three communication mechanisms and dependency DAG** | **Default architecture** | Typed actor messages, callbacks, streams, plugin protocols, or mutually recursive domain structures do not fit the prescribed list cleanly. | Keep interfaces explicit and cycles controlled. Distinguish build dependencies from runtime interaction cycles. |
| **§6.2 — E; mandatory physical zones** | **Recommendation** | Browser-only/PWA storage exposes origin-managed stores rather than an arbitrary root filesystem. | Separate lifecycle and access policies logically; map them onto platform-supported storage. |
| **§6.3 — P; fixed backup, deletion, and Git rules** | **Conditional policy** | An expensive reproducible index may deserve backup; an exported archive may be the user’s only retained copy. | Assign retention and backup policy by value, recovery cost, sensitivity, and role. |
| **§6.4 — E; no canonical user data in Git** | **Conditional prohibition** | A Git-backed note application or source-code editor intentionally stores user-owned canonical work in Git. | Prohibit accidental inclusion in an unrelated application source repository; allow deliberate, documented versioned data stores. |
| **§7.3 — E; asynchronous or strictly decoupled derivation** | **Default architecture** | A transactional database index or synchronously maintained materialized view can be necessary for immediate consistency. | Derived representations must not acquire unauthorized authority; synchronous maintenance is permitted. |
| **§8.1 — E; complete offline function except live counterparties** | **Ecosystem policy with capability-level conditions** | A web search client, market terminal, streaming client, or third-party API administration tool inherently needs remote resources without necessarily having a live human counterparty. | Preserve useful independent local capabilities and clearly identify inherently remote functions. |
| **§§8.2, 22.1 — E; durable offline queues** | **Conditional** | A market order or door-unlock command becomes dangerous when replayed hours later. | Queue only operations whose freshness, authorization, duplication, and cancellation semantics support delayed execution. |
| **§9.1 — E; broad platform operation** | **Ecosystem portability policy; conditional support matrix** | A mobile application or native hardware driver cannot meaningfully support every desktop and NAS environment. | Avoid unnecessary lock-in; separately declare portable architecture, buildable targets, tested targets, and supported targets. |
| **§9.3 — E; universal filename sanitation and LF conversion** | **Conditional interoperability policy** | A forensic tool, source editor, or signed-document archive must preserve original names and bytes. | Apply format-specific normalization only where semantically permitted; preserve originals or reversible mappings. |
| **§10.4 — P; prescribed server/chunked-file designs and preflights** | **Default patterns**, conditional on storage contracts | A NAS-hosted service uses a local transactional engine; a desktop media client reads ordinary files over SMB. | Select an access mode with demonstrated semantics; do not impose chunking or a per-operation probe universally. |
| **§11.1 — E; scheduled human-readable exports** | **Ecosystem exit policy; export scheduling conditional** | A huge media library or encrypted archive cannot usefully dump all state into text on a schedule. | Provide a usable, documented preservation and migration path with appropriate formats and cadence. |
| **§11.3 — P; locks combined with timestamp/hash checks** | **Conditional implementation guidance** | A database serializable transaction or enforced single writer already coordinates writes. | Use a sufficient coordination protocol for the actual storage model; additional checks are not automatically beneficial. |
| **§13.1 — E; JSON Schema/OpenAPI and fixed return fields** | **Conditional tool-contract requirement; format recommendation** | A typed in-process tool or streaming media tool needs different contracts and outputs. | Define machine-enforceable inputs, effects, errors, and outcomes in a suitable representation. |
| **§§13.2, 14.2 — E; fixed approval tiers and soft deletion** | **Risk-based ecosystem policy / default** | An authorized retention daemon must delete expired records; repeated human prompts would defeat its purpose. | Approval depends on delegated scope, impact, reversibility, sensitivity, and cumulative effects. |
| **§13.3 — E; exact dry-run for all higher tiers** | **Conditional preview requirement** | A remote API allocates an identifier or changes state between preview and execution. | Provide an honest preview with assumptions and preconditions; distinguish estimates from guaranteed effects. |
| **§§15–16 — E; permanent full audit and per-record lineage** | **Conditional accountability requirements** | High-frequency hardware telemetry or millions of imported records can make full per-field history more costly and sensitive than the data itself. | Record sufficient accountable evidence at meaningful operation granularity, subject to retention and minimization. |
| **§§17.3–17.4 — E; hash everything and fixed reconciliation pipeline** | **Conditional implementation guidance** | A huge media library cannot hash every byte at startup; a database service may prevent ordinary out-of-band file edits. | Detect relevant changes using mechanisms proportionate to the threat, access model, and detection-time contract. |
| **§§20.2–20.3 — E/P; fixed backup contents and internal SHA-256 manifests** | **Conditional recovery specification / recommended mechanism** | A storage-native snapshot has its own integrity model; expensive embeddings may be essential to timely recovery. | Back up the complete recovery dependency set and verify it using suitable mechanisms. |
| **§21.3 — E; four export categories** | **Recommendation** | A small contact conversion CLI needs one documented interchange format. | Distinguish different export purposes where they exist; do not require all four. |
| **§§23.2–23.4 — E; stateless cognition, canonical session state, ephemeral vector stores** | **Conditional AI architecture guidance** | Temporary agent scratch work should expire; a vector database may also durably store authoritative original documents. | Classify each artifact by authority and retention needs, independently of storage product and AI origin. |
| **§24.1 — E; mandatory provider abstraction and immunity to change** | **Default architecture** | A tool’s explicit purpose is to administer a particular provider’s unique API. | Isolate provider dependencies where replacement is a real requirement; expose capability differences honestly. |
| **§25.3 — E; exact lockfiles and “10 lines” dependency rule** | **Reproducible application-build policy / recommendation** | A reusable library needs compatible version ranges; handwritten cryptography may be short and unsafe. | Make released builds reproducible and assess dependency risk by function, maintenance, and trust. |
| **§25.4 — E; prescribed privilege mechanisms** | **Conditional security mechanisms** | A credential-rotation worker legitimately needs administrative scope; a read transaction may need storage-engine bookkeeping writes. | Minimize effective authority within the operational model rather than banning actor classes or handle types. |
| **§27.1 — E; universal loopback default** | **Default for local applications** | A NAS service behind an explicitly configured container network must listen beyond its own loopback interface. | Make intended exposure explicit at deployment boundaries and secure that exposure. |
| **§27.3 — P; four zones with fixed controls** | **Threat-model guidance** | A public non-browser protocol has no meaningful CORS policy; a VPN peer may still be hostile. | Derive controls from principals, protocol, reachable surfaces, and deployment trust. |
| **§29.2 — E; versions, locks, and leases prescribed for all** | **Conditional concurrency mechanisms** | A CRDT, append-only log, single-writer service, or MVCC database uses different concurrency semantics. | Prevent invalid interleavings using a protocol appropriate to the domain’s consistency requirements. |
| **§§31.1–31.2 — E; sequential/idempotent migrations and local snapshots** | **Conditional migration safety requirements** | A massive relational deployment needs online expand/contract migration; restoring a local snapshot may destroy newer writes. | Use versioned, recoverable migrations with explicit concurrency, compatibility, and restoration boundaries. |
| **§32.2 — P; universal configuration precedence** | **Default** | A managed deployment must prevent a CLI flag from overriding mandatory security policy. | Define deterministic precedence with explicit non-overridable policy where needed. |
| **§§33–35 — E; universal observability and test categories** | **Conditional, proportional requirements** | A stateless 100-line CLI has no health server, AI tools, audit database, or backup subsystem. | Verify applicable contracts and provide sufficient diagnostics without requiring irrelevant infrastructure. |
| **§36.1 — E; native, container, and NAS appliance deployment** | **Conditional support commitments** | A browser-only application or native desktop UI is not a meaningful headless OCI service. | Support declared deployment modes; keep packaging distinct from storage compatibility. |
| **§§37–38 — E; extensive root documentation and formal exceptions** | **Proportional ecosystem governance policy** | A single-purpose utility can be fully explained in a short README; a default need not require an impossibility argument. | Document relevant contracts and significant decisions; scale governance to risk and scope. |

**Rust-first policy:** Keep as **ECOSYSTEM POLICY — MANDATORY DEFAULT**. A native SDK, deployment limitation, mature domain ecosystem, or demonstrably safer maintenance arrangement can justify a component exception. Familiarity alone does not. However, evidence that staffing, toolchain qualification, or long-term support materially affects safety is a technical lifecycle argument and should not be dismissed merely because people are involved.

## RULES THAT SHOULD BE REMOVED

These removals target harmful assertions or redundant normative machinery, not the underlying goals.

1. **The non-brevity mandate as an architectural rule — §1.2.**  
   Length is not evidence of completeness. Repetition already creates contradictory obligations. Require precision and coverage instead.

2. **“Identical architectural decoupling” from in-process modules — §5.1.**  
   In-process interfaces do not provide identical failure containment, memory isolation, privilege separation, deployment independence, or runtime independence.

3. **“Exactly two” mutation initiator types — §12.2.**  
   This excludes timers, external systems, devices, recovery processes, and the automation categories explicitly listed in §15.3.

4. **The `>10 records` destructive-risk threshold — §13.2.**  
   Eleven harmless tags and one irreversible payment demonstrate its invalidity.

5. **Automatic verification of an entire AI-generated record after any human edit — §16.2.**  
   Editing punctuation does not verify factual content. This rule launders uncertainty into false assurance.

6. **Unconditional exclusion of derived artifacts from backup — §20.2.**  
   This can make recovery operationally impossible or economically unacceptable even when recomputation is theoretically possible.

7. **Blanket Postel’s Law for stored data — §31.3.**  
   Liberal acceptance can silently misinterpret new semantics, bypass validation, or destroy unknown fields on writeback.

8. **Unconditional successful exit status on shutdown — §36.3.**  
   A flush failure or unrecovered operation must not be reported as success.

9. **The claim that event sourcing “guarantees perfect auditability and time-travel debugging” — §41.3.**  
   Event completeness, schema evolution, deterministic replay, external inputs, retention, and integrity remain separate requirements.

10. **§39 as an independent source of absolute prohibitions.**  
    Keep it only as a non-normative index to authoritative clauses. Its present wording converts qualified guidance into unconditional architectural failures and duplicates contradictions.

11. **The generation-boundary attestation as constitutional law — §44.**  
    It is a claim about an earlier drafting session, not an enduring application requirement. Preserve it, if useful, in provenance records; this review cannot authenticate it.

## RULES THAT REQUIRE REWORDING

These are conceptual corrections, not a replacement constitution.

### 1. Authority, ownership, and truth — §§2.1–2.2, 4.1, 7.1, 16.2, 23.1

The draft conflates:

- ownership;
- permission to perform an operation;
- authority of a record within a system;
- factual correctness;
- human review.

A canonical record may be false, disputed, automatically observed, jointly owned, or lawfully subject to another person’s rights.

**Correction:** Canonical means authoritative for a defined system purpose. It does not mean objectively true or necessarily created or confirmed by a human. Identify owners, subjects, administrators, delegates, and conflicting rights separately.

### 2. Safety priorities — §4.4

The absolute ordering puts data preservation above human safety, security, and privacy.

**Counterexample:** A hardware controller must stop a dangerous actuator even if abrupt shutdown loses recent telemetry. A compromised credential may require immediate revocation. A lawful erasure may intentionally destroy retained information.

**Correction:** Resolve conflicts using explicit domain hazards and obligations. No global ordering should require preservation of data at the expense of greater physical or security harm.

### 3. Code/data separation — §6.1

A portable desktop application may intentionally carry its data beside its executable. Source code itself is canonical user data for an editor.

**Correction:** Application replacement must respect declared data lifecycles. Logical ownership and destructive-operation boundaries matter more than directory adjacency. “Immediately re-attachable” also depends on schema compatibility, keys, permissions, and available readers.

### 4. Canonical versus derived — §§2.2, 7, 23.4

Three different properties are collapsed into one:

- produced from other information;
- authoritative;
- safely disposable.

An AI-generated artifact can be derived by origin and nevertheless require preservation. Conversely, some canonical information is intentionally ephemeral.

**Correction:** Classify authority, provenance, reproducibility, retention, and recovery cost independently. Derived origin does not imply disposability.

### 5. Regeneration guarantees — §7.2

Bit-for-bit reconstruction may require retained model weights, exact software, seeds, hardware behavior, licensed dependencies, and historical external inputs.

**Correction:** Specify whether recovery means identical bytes, equivalent functionality, equivalent quality, or an acceptable replacement. If an artifact’s exact identity matters, preserve it regardless of whether it was generated.

### 6. Offline behavior — §§8, 22

§8.1 already contains an exception for live counterparties; it is not literally an unqualified offline mandate. Its exception is nevertheless too narrow.

**Correction:** Define offline guarantees per capability. Email can preserve local drafts and cached messages without promising delivery; streaming can expose downloaded media without inventing access to uncached content. Shared scarce resources may require online authorization or previously allocated rights.

### 7. Filesystem paths and names — §§9.2–9.3

Absolute paths can be legitimate user configuration, audit evidence, or the very objects managed by a filesystem tool. Sanitization can collapse distinct names or change meaning.

**Correction:** Distinguish portable references from host bindings. Preserve identity through explicit mapping, collision handling, and reversible encoding. Do not rewrite user content merely to make it portable.

### 8. File mutation safety — §11.2

Atomic replacement is one useful algorithm. It is not appropriate for every database page, append-only archive, huge media edit, or log.

**Correction:** Require a specified crash-consistency and acknowledgement contract for each storage backend. Permit transactional engines, append protocols, copy-on-write, journals, or replacement algorithms when their assumptions are satisfied.

### 9. Mutation/audit atomicity — §§12.2, 15.1

The diagram commits state and then generates an audit event. A crash between those steps violates the audit mandate.

**Correction:** When an event is required evidence of a committed mutation, make their durable relationship atomic or recoverably coupled. A transaction containing both records, or a transactionally recorded outbox, can achieve this; two ordinary sequential writes cannot.

### 10. Read authority — §§13.2, 23.1, 25.4

“No canonical mutation” is not equivalent to low risk.

**Counterexamples:** Reading secrets, exporting medical records, sending documents to a summarization provider, executing costly queries, or following attacker-controlled URLs.

**Correction:** Authorize reads by confidentiality, destination, cost, and side effects as well as mutation status. A read tool may still need strict restrictions.

### 11. Previews and approvals — §13.3

An exact preview becomes stale when state changes. A displayed record count does not bind execution to that same set.

**Correction:** Bind approval to operation identity, scope, parameters, relevant versions, expiry, and budgets. Revalidate at execution. Describe uncertain effects explicitly.

### 12. Direct user editing — §§12.1, 17–18

The owner may legitimately edit their own Markdown, configuration, or source files outside the application.

**Correction:** The application may define which external changes it can safely adopt and may refuse incompatible input. It must not claim sovereignty over the user’s ability to alter their own files. Supported editing workflows should have explicit ingestion and reconciliation semantics.

### 13. Audit content and retention — §§6.2–6.3, 15–16, 26

Append-only logical history does not require permanent retention of original sensitive payloads.

**Correction:** Define retention windows, field minimization, access controls, redaction, lawful erasure, archival, and integrity verification. Record that authorized deletion or redaction occurred without automatically preserving the deleted secret.

A rollback identifier should not become an enduring bearer credential merely because it appears in an audit event.

### 14. Human and AI provenance — §§15.2, 16

A model identifier is useful only if known and meaningful. Provider aliases may change, and a prompt may contain unrelated personal information.

**Correction:** Capture attribution necessary for accountability, permit unknown or provider-reported identities, and separate sensitive explanatory material from durable event metadata. Human review should identify its actual scope.

### 15. Drift and restoration — §§17–18

A restored NAS snapshot may roll back both data and its local integrity manifest, leaving no mismatch. A detected change does not identify its author.

**Correction:** Specify which drift classes can be detected and what independent evidence is required. Avoid automatically restoring an older copy over a newer valid external change. Reconciliation itself needs concurrency protection.

### 16. Retries and external effects — §28.2

A client-generated key cannot guarantee that a remote service applies an effect only once.

**Correction:** Distinguish idempotent state transitions, deduplicated requests, replay-safe commands, and non-repeatable effects. Specify key scope, persistence, payload matching, retention, and ambiguous-result handling. After a timeout, an operation may have succeeded remotely.

### 17. Atomicity and recovery — §§28.3, 30.2

“All modifications” is too broad for distributed services, large imports, physical operations, and external APIs.

**Correction:** Define atomic consistency units. Larger workflows may expose explicit, recoverable intermediate states. An interrupted operation need not restore every physical byte to its earlier value; it must preserve promised logical consistency.

### 18. Migration recovery — §31

Automatic restoration after a failed migration may discard concurrent valid writes. A transactional rollback can also make snapshot restoration unnecessary.

**Correction:** Establish exclusive access or coordinated online migration semantics; classify failure before choosing rollback, roll-forward, restore, or restricted service. Never restore a stale snapshot blindly.

### 19. Network trust — §§27, 41.4

Loopback is not automatically a trusted single-user environment. Other local users, compromised processes, browser-origin attacks, and proxy configurations matter.

**Correction:** Treat interface binding as exposure reduction. Authentication, request-origin protections, transport security, and authorization depend on the actual threat model. VPN membership is not universal application authorization.

### 20. Error handling and shutdown — §§28.3, 36.3

Logging every expected failure with a stack trace creates noise and leakage. Waiting indefinitely for an unavailable NAS can prevent shutdown.

**Correction:** Distinguish expected conditions from faults; report material failure truthfully. Use bounded shutdown and rely on crash recovery when orderly completion is impossible.

### 21. Rust-first implementation — supplied policy and §43

The supplied policy changes an ecosystem decision, not a fact about all software.

**Correction:** Retain the presumption of Rust and component-scoped documented exceptions. Recognize that Rust does not itself guarantee domain correctness, durable storage, secure FFI, distributed consistency, or suitable real-time behavior. Minimize language boundaries where doing so improves the system, rather than treating fewer languages as an independent safety guarantee.

## INTERNAL CONTRADICTIONS

The following are meaningful contradictions or unresolved cross-rule tensions. Where a generous interpretation could reconcile them, that interpretation needs to be written explicitly.

| Sections | Conflict | Consequence |
|---|---|---|
| **§§3.1, 38, 41–42** | “Established” rules are called immutable pillars, while the draft itself lists unresolved questions and adversarial challenges to them. | Provenance, ratification status, and technical certainty are conflated. |
| **§§3.1–3.2** | `[CONDITIONAL]` appears as an epistemic category, although it expresses applicability; `[PROPOSED / DERIVED]` combines proposal status with logical derivation. | The advertised independent classification axes are not independent. |
| **§5.1 internally** | Modular monolith is a “default,” but alternatives require an operational need that cannot be met in one process. | A defeasible default becomes an almost absolute requirement. |
| **§§5.5, 39.3** | Proposed inter-feature constraints reappear as unconditional architectural-failure prohibitions. | Unratified mechanisms acquire mandatory force elsewhere. |
| **§§6.2, 40.1** | The physical storage layout is `[ESTABLISHED]` in §6.2 and `[PROPOSED / DERIVED]` in §40.1. | Direct classification contradiction. |
| **§§13.3, 40.4** | Mandatory dry-run requirements are established in §13.3 and proposed in §40.4. | Direct classification contradiction. |
| **§§13.2–13.3** | Tier 3 execution calls preview optional, while §13.3 requires support for dry-run. | Potentially reconcilable: providing the capability can be mandatory while invocation is optional. The text must distinguish those obligations. |
| **§§4.1, 12.1, 17–18** | The user is sovereign, direct editing is prohibited, and later sections recognize and adopt direct user edits. | Supported external editing is left simultaneously normal and forbidden. |
| **§§12.2, 15.3** | Exactly two initiating actors versus automation, import, sync, migration, and recovery initiators. | Actor model is internally incomplete. |
| **§§12.2, 15.1, 30.2** | State commit precedes audit creation despite mandatory audit and atomicity claims. | Crash window for committed, unaudited changes. |
| **§§6.2–6.3, 15, 26.1** | Permanent full history versus retention minimization. | No resolution for lawful erasure, sensitive corrections, or expired data. |
| **§§15–16, 23.3** | Deletion of AI memory traces versus permanent history containing previous values or creation context. | “Deleted” memory can remain reconstructable from logs. |
| **§§16.2, 4.3** | Any human edit makes AI output “verified,” despite the emphasis on deterministic correctness. | Human interaction is falsely treated as evidence of truth. |
| **§§7.2, 20.2, 23.4** | Exact rebuildability and mandatory backup exclusion despite externally dependent AI generation. | Recovery promises lack retained dependencies or preserved outputs. |
| **§§23.2–23.3** | All state surviving invocations becomes canonical; AI memory is described as secondary; scratchpads share that memory category. | Authority and lifecycle of agent state are inconsistent. |
| **§§8, 22.1, 30.2** | Offline writes and later merging versus unconditional global invariants and atomicity. | Some domains cannot accept arbitrary partitioned writes without restricting operations or weakening guarantees. |
| **§§10.2, 10.4** | NAS compatibility exists “if and only if” the core handles remote shares, yet a NAS-local database service is prescribed. | A valid NAS-local deployment fails the draft’s own definition. |
| **§§10.2, 36.1** | Containerization is optional versus required support for container deployment. | Direct mandatory/optional conflict. |
| **§§11.1, 20.2–20.3** | Strong recovery requirements versus backups specified mainly as directory inclusion. | A live multi-store directory copy need not be a consistent recoverable snapshot. |
| **§§19.1, 19.3** | Not a contradiction: §19.1 already says “SHOULD” and “where technically feasible”; §19.3 acknowledges irreversible effects. | The actual defect is universal high-friction confirmation and overprescribed staging, not a literal promise that everything is reversible. |
| **§§25.2, 39.4 item 23** | Restricted plaintext `.env.local`/secret files are allowed; unencrypted config secrets are prohibited. | Conflicting secret-storage rules. |
| **§§32.1–32.2** | Hardcoded runtime settings are prohibited while built-in defaults are explicitly part of precedence. | Defaults need a clear exception from prohibited environment assumptions. |
| **§§33.2, 36.2** | Read-only probes are expected to verify writeability. | They can inspect conditions but cannot establish that a future write will succeed. |
| **§§34.2, 43** | Every app requires AI tool tests while technology and feature choices remain application-dependent. | Non-AI applications inherit irrelevant requirements. |
| **§§35.1, 38** | The universal verification suite is optional while compliance is described as strict and universal. | The document does not distinguish mandatory evidence from a recommended test harness. |
| **Supplied Rust policy, §43** | Rust is presumptive with justified deviations versus complete freedom of language choice. | §43 must reflect the new policy before ratification. |

The title of §9 includes BSD, but §9.1 does not enumerate it. This is an unresolved support-scope omission, not evidence that BSD has been operationally specified.

## TECHNICALLY QUESTIONABLE CLAIMS

### Storage, concurrency, and distributed systems

1. **§9.3: Treating all filenames as case-sensitive ensures portability.**  
   False. Two names differing only by case can coexist on one filesystem and collide on another. Case behavior can vary by filesystem and configuration. Unicode normalization and reserved-name behavior create additional identity problems.

2. **§9.2: `file://attachments/doc1.pdf` represents a portable relative file reference.**  
   Misleading. In a file URI, `attachments` occupies the authority position. Relative references need defined semantics; the example is not an ordinary relative path.

3. **§10.3: SMB/NFS locking is generally broken or non-atomic.**  
   Overgeneralized. Behavior depends on protocol version, server, client, mount configuration, failure mode, and application protocol. Neither universal safety nor universal brokenness follows from the acronym.

4. **§10.3: SQLite network-share risks can be handled with “WAL/VFS mitigations.”**  
   Dangerous phrasing. Standard SQLite WAL relies on shared-memory coordination and is not a general multi-host network-filesystem solution. A specialized VFS requires its own documented guarantees. A server process accessing local storage is a different architecture.

5. **§10.3: `fsync` forces network-buffered data onto durable media.**  
   Only within the storage stack’s implemented contract. Server acknowledgements, stable storage, hardware caches, power protection, and error propagation matter.

6. **§10.3: Oplocks describe the whole delayed-write hazard.**  
   Incomplete. Cache-coherence mechanisms and stable-storage guarantees are related but distinct. Disabling an oplock is not a durability proof.

7. **§10.3: `0755` and `0644` are appropriately “restrictive.”**  
   Not for all private data: they commonly permit other users to read files or traverse directories. Network ACLs and identity mapping also need separate treatment.

8. **§10.4: Preflight accessibility, permission, and free-space checks establish safety.**  
   False. They race with the actual operation, may miss quotas or allocation effects, and cannot promise future connectivity. Correct handling of operation failures remains essential.

9. **§11.1: Parquet is human-readable.**  
   Incorrect. It is an openly specified binary columnar format. Open documentation and human readability are different properties.

10. **§11.1: Listed storage engines are interchangeable evidence of transactional suitability.**  
    Unsupported. SQLite, DuckDB, PostgreSQL, and key-value engines have different concurrency, workload, durability, and deployment contracts.

11. **§11.2: In-place updates inherently truncate and destroy canonical files.**  
    False. Transactional page updates and properly designed append protocols are counterexamples. Unsafe unsynchronized overwrite is the problem.

12. **§11.2: Same-filesystem rename plus flush guarantees universal crash safety.**  
    Too strong. Atomic visibility, durability, metadata preservation, concurrency control, and post-failure outcome determination are separate properties.

13. **§11.2: `MoveFileExW(...MOVEFILE_REPLACE_EXISTING...)` is a universal atomic replacement guarantee.**  
    Requires Windows filesystem, API, sharing-mode, and failure-model qualification. The flag alone does not establish every promised property.

14. **§11.3: A timestamp or hash check prevents concurrent write races.**  
    Only if validation and state transition are coordinated atomically. “Check, then write” leaves a race.

15. **§18.1: LWW is the primary cause of silent data loss.**  
    An unsupported empirical superlative. LWW is also a legitimate resolution policy for some registers and preferences.

16. **§22.2: Lamport timestamps, hashes, vector clocks, and CRDTs are equivalent conflict-detection mechanisms.**  
    Incorrect. Lamport timestamps do not, by themselves, establish concurrency; hashes indicate content difference; vector clocks track causal relationships under assumptions; CRDTs encode convergence semantics.

17. **§29.2: Relational writes must obtain exclusive or immediate write locks.**  
    Overbroad and potentially harmful. PostgreSQL’s MVCC and lock modes cannot be reduced to SQLite-style immediate writer acquisition. Unnecessarily broad locking destroys useful concurrency.

18. **§29.2: Timestamped leases and heartbeats prevent unsafe NAS concurrency.**  
    Insufficient. A paused or partitioned old holder may resume after a new holder acquires the lease. Safe exclusion needs a protocol that prevents stale writes, often through storage-enforced fencing or an equivalent mechanism.

19. **§30.2: A write-ahead intent journal provides atomic multi-file operations.**  
    Not by itself. Recovery idempotence, ordering, durable commit markers, concurrent reader behavior, and partial application all require design.

20. **§30.1: No interruption can ever leave unreadable canonical data.**  
    Unachievable without bounded assumptions. Hardware faults, storage-stack defects, torn sectors, malicious interference, and lost keys exceed what application code can categorically prevent.

### Security, AI, and operational claims

21. **§13.1: Tools and skills are inherently security perimeters.**  
    False for descriptive schemas or natural-language skills alone. A perimeter exists only where authority is enforced and bypass paths are controlled.

22. **§13.1: Structured return envelopes enable deterministic agent reasoning.**  
    They improve machine interpretability. They do not make a probabilistic model deterministic or correct.

23. **§§15, 17, 20: Hashing establishes tamper evidence.**  
    Only relative to trusted evidence. An attacker able to rewrite both data and a local manifest can recompute hashes. A hash chain also needs a protected checkpoint or trust anchor to detect complete rewriting.

24. **§16.2: Human confirmation establishes factual ground truth.**  
    It establishes that a person approved something, possibly only a limited aspect. It does not prove its content.

25. **§24.1: Provider abstraction creates immunity to pricing, capability, or model changes.**  
    False. An adapter can reduce code changes; it cannot manufacture equivalent model quality, licensing, latency, or availability.

26. **§24.2: AI failure can never crash an application.**  
    A useful containment objective, not an absolute guarantee. Resource exhaustion, native dependencies, implementation defects, and process-wide failures still require bounded claims and recovery design.

27. **§25.3: `go.sum` is an exact dependency lockfile.**  
    Incorrect. It records module checksums; dependency selection also involves `go.mod` and Go’s module-resolution rules.

28. **§25.2: `0600` protects secrets from all local malicious processes.**  
    It generally does not isolate other processes running as the same account. Threat-specific isolation or credential services may be needed.

29. **§27.3: Localhost means a trusted single-user runtime; VPN means validated application identity.**  
    Neither follows automatically. Network location is not a complete identity or authorization model.

30. **§27.3: Every public service needs a WAF and CORS.**  
    These controls are protocol- and deployment-specific. CORS is not general network authorization and does not protect non-browser clients.

31. **§28.2: Idempotency keys eliminate duplicate effects universally.**  
    They do so only within a correct deduplication protocol and its retention and trust boundaries. They do not automatically solve external side effects.

32. **§33.2: A lightweight read-only health check verifies writeability.**  
    At best it reports evidence or prerequisites. A future write can still fail from quota, permissions changes, disconnection, or storage faults.

33. **§37.2: Generating schemas guarantees runtime/documentation synchronization.**  
    It reduces drift, but custom validators, deployment configuration, authorization, and semantic behavior may remain outside the generated schema.

34. **§20.1: An untested backup is a “hallucination” and legally incomplete.**  
    It may contain valid recoverable data; its recoverability is unproven. Legal adequacy depends on the applicable obligation, not this metaphor.

### Arbitrary constants and unjustified fixed schemes

| Item | Assessment |
|---|---|
| **30 years — §4.2** | Defensible planning horizon for an ecosystem preservation policy; not a universal retention requirement or guarantee. |
| **Seven disparate folders — §5.2** | Rhetorical illustration, not evidence that horizontal organization inevitably causes regressions. |
| **Five lines of duplication — §5.4** | Example, not a meaningful coupling threshold. |
| **Ten lines instead of a dependency — §25.3** | Particularly dangerous for security, parsing, Unicode, and protocol code. Line count does not measure implementation risk. |
| **More than ten records — §13.2** | Invalid normative risk threshold; remove. |
| **Five risk tiers — §13.2** | A policy taxonomy, not a discovered engineering law. It misses confidentiality, cost, physical effects, and cumulative scope. |
| **0.5–50 ms versus 0.02 ms — §10.3** | Workload- and hardware-dependent illustrative measurements presented too generally. Benchmark relevant access patterns. |
| **5,000 ms lock timeout — §29.2** | Explicit example, not a universal requirement. A suitable deadline depends on workload and user expectations. |
| **10 MB × 5 log files — §33.1** | Explicit example; retention should depend on event volume, diagnostic needs, sensitivity, and available storage. |
| **Four network zones and five configuration levels — §§27.3, 32.2** | Useful models in some deployments, but neither is exhaustive or universally ordered. |
| **SHA-256 — §§17.3, 20.3** | A reasonable current mechanism, not a timeless constitutional invariant. Requirements should describe needed integrity properties and algorithm evolution. |
| **Five-second latency, ten workstations, 50,000 files — §42** | Adversarial test scenarios rather than mandatory thresholds. Retain as examples, not acceptance criteria. |

Claims about specific filesystem durability, locking, latency, model reproducibility, and supported platform combinations require empirical qualification against declared configurations. Conceptual review cannot certify them.

## MISSING UNIVERSAL PRINCIPLES

Most apparent omissions are actually defects in existing provisions. Authentication, backup testing, least privilege, bounded capabilities, dependency discipline, and privacy already appear and should be corrected rather than duplicated.

Two missing concepts deserve explicit constitutional treatment:

1. **An acknowledgement must state what is known to have happened.**  
   The draft lacks a first-class distinction among rejected, accepted, locally committed, durably committed, remotely completed, and outcome-unknown operations.

   A NAS disconnection or API timeout can leave success uncertain. The application must preserve and communicate that uncertainty rather than report failure and blindly retry. Neither generic error handling nor idempotency alone defines this contract.

2. **Authority requires an explicit principal and delegation model.**  
   The singular sovereign “user” does not resolve conflicts among device owners, data subjects, workspace owners, administrators, service accounts, and delegates.

   The constitution needs a way to identify whose authority permits an operation, over which data, for what scope and duration. Actor labels and permission checks do not supply the missing ownership and delegation semantics.

## NAS VERDICT

**NAS support should remain mandatory ecosystem policy, expressed as an applicable, declared, tested support contract. It must not mean that every application opens transactional files over SMB/NFS or runs on every NAS appliance.**

| NAS mode | What support should mean | Principal failure to avoid |
|---|---|---|
| **1. Application runs on a NAS/server** | Support a declared server/runtime and local storage arrangement, including lifecycle, permissions, resource limits, and recovery. | Assuming that “NAS-hosted” means database files are accessed over a remote share. |
| **2. Client connects to a NAS-hosted service** | Define authentication, protocol compatibility, timeouts, cancellation, retries, stale reads, and unknown outcomes. | Treating a network API timeout as proof that no write occurred. |
| **3. Ordinary user files reside on a NAS share** | Support declared file access patterns and preserve file identity, concurrent-change semantics, and failure handling. | Assuming rename or a successful preflight establishes a complete transaction. |
| **4. Transactional database files are opened across SMB/NFS** | Permit only configurations explicitly supported by the engine and demonstrated for the intended failure and concurrency model; otherwise reject this mode clearly. | Treating WAL, a lockfile, or “SQLite support” as a general safety certificate. |
| **5. NAS is a backup destination** | Produce consistent recovery artifacts, verify transfer and restoration, and account for credentials, keys, corruption, and failure-domain independence. | Calling a copy on the same vulnerable storage system an independent recovery strategy. |

Every application should document which modes are relevant and how the intended NAS use is satisfied. A client may satisfy the requirement through mode 2 without supporting mode 4. A tiny utility may support NAS input/output paths or a documented service-mediated workflow without shipping a NAS daemon.

A backup-only mode must not be used to claim active NAS data support when the application’s intended workflow requires shared active data. Conversely, software with no persistent data or filesystem role should document that fact rather than invent storage features.

The constitutional requirement should demand:

- no accidental local-disk-only assumptions in applicable I/O;
- explicit supported access modes and configurations;
- truthful acknowledgement and recovery semantics;
- safe handling of disconnection and concurrent access;
- tested behavior for the modes actually claimed.

No application can guarantee stronger durability or coordination than its storage and network substrate provides.

## AI AUTHORITY VERDICT

**An AI may exercise only explicitly delegated capabilities, through enforcement that it cannot silently bypass; every resulting effect must satisfy the applicable authorization, integrity, privacy, and operational constraints.**

That rule survives the strongest counterexamples:

- **Direct file reads:** Legitimate when authorized, but confidentiality and exfiltration matter.
- **Coding agents:** Scoped file writes, patches, and shell execution are legitimate capabilities. They are not intrinsically an architectural violation.
- **Scratch space:** Broad temporary writes may be safe under bounded resource and access policies.
- **Import staging:** Raw writes can be allowed before controlled validation and incorporation into authoritative state.
- **Patch tools:** A patch can be safely accepted when scope, preconditions, resulting content, and authorization are checked.
- **High-volume automation:** Prior delegation can authorize large operations with budgets, constraints, monitoring, cancellation, and recovery.
- **Schema-valid harmful intent:** Schema validation cannot establish that an action serves the user’s actual goal. Scope limits, semantic policy, previews where useful, and outcome monitoring remain necessary.

Humans and AI should face the same applicable integrity constraints. They need not receive identical privileges, authentication methods, rate limits, or approval requirements.

Approval should depend on consequences, scope, uncertainty, and delegation—not actor identity alone. Reversibility is important but insufficient: reading and publishing a secret is irreversible even if no database mutation occurs.

A natural-language “skill” is guidance unless executable controls enforce its limits. Tool descriptions are not a security boundary by themselves.

## AUDIT & ROLLBACK VERDICT

**Auditability should mean sufficient, protected, proportionate evidence of accountable operations—not permanent retention of every original payload.**

A defensible audit contract specifies:

- which events matter and at what granularity;
- what identity and outcome can actually be established;
- how required evidence is coupled to committed effects;
- how unauthorized alteration is detected within the stated threat model;
- retention, access, redaction, deletion, and recovery policies.

A bulk operation may have one operation record plus a durable affected-set representation rather than millions of repeated prompts and actor fields. A hardware controller may aggregate routine telemetry while recording safety-significant transitions individually.

Append-only event semantics can coexist with authorized payload expiration, key destruction, redaction, and archival. Cryptographic erasure has limits: it cannot recall plaintext already exported or copied, and remaining metadata may still be sensitive.

**Rollback must state its actual scope and limits.**

| Effect | Defensible promise |
|---|---|
| Local state change | Restore or compensate where feasible, subject to subsequent changes and current authorization. |
| Concurrent collaborative update | Undo the intended contribution without blindly restoring an old global snapshot. |
| Remote API operation | Reconcile status; use cancellation or compensation if supported. |
| Sent email or published message | A follow-up or deletion request may mitigate; it cannot guarantee recipients forget it. |
| Financial transaction | Refund or reversal may be a separate transaction with different legal and economic effects. |
| Physical action | Often impossible to reverse; safety must operate before and during execution. |
| Expired or securely erased data | Recovery may intentionally be impossible. |
| Backup restoration | Restore a declared recovery point; disclose lost later work and external effects that are not undone. |

§19.1’s “where technically feasible” is already the right direction. Its supporting rules should distinguish inverse operations, compensations, restoration, cancellation, and irreversible commitment.

Mandatory interactive confirmation for every irreversible effect would make legitimate automation daemons, retention services, hardware controllers, and communication systems unusable. Explicit bounded delegation can provide authorization without a fresh prompt for each action.

## FEATURE-FIRST VERDICT

**No particular directory structure survives as a universal invariant. The defensible mandatory portion is responsibility clarity and protection of applicable invariants across boundaries.**

For an application with multiple capabilities:

- responsibilities and authoritative data ownership should be identifiable;
- cross-boundary effects should use explicit contracts;
- callers should not silently bypass another component’s integrity rules;
- shared concepts should have deliberate ownership;
- dependencies should remain understandable and maintainable.

Feature-first organization is a strong **ecosystem default** for feature-rich applications. It should not prohibit:

- one cohesive file for a tiny CLI;
- compiler passes or signal-processing pipelines;
- a shared mathematical or storage kernel;
- framework-required platform layers;
- separate UI, privileged helper, and untrusted plugin processes;
- performance-oriented data layouts;
- narrowly justified shared domain models.

A package dependency DAG is useful default discipline. A ban on every runtime cycle would prohibit ordinary request/response relationships, callbacks, and mutually interacting state machines. Event buses can also hide coupling while satisfying a superficial import-DAG check.

The modular monolith remains a strong default where deployment simplicity and transactional locality dominate. Process separation may be justified by fault containment, privilege boundaries, runtime incompatibility, independent lifecycle, or operational economics—not solely by proving that a single-process implementation is impossible.

Documentation should scale from a few sentences describing a tiny utility to explicit feature contracts, ownership maps, recovery procedures, and compatibility decisions for a large application.

## FINAL RATIFICATION TABLE

Cost estimates describe the draft’s current obligations for a typical small-to-medium application. They are qualitative engineering costs, not schedule estimates. Each verdict identifies the dominant disposition; mixed families require the clause-level corrections above.

| Constitutional family | Classification | Cost | Does universal benefit justify current cost? |
|---|---|---:|---|
| **§1 — Purpose, scope, completeness** | **REWRITE** | LOW–MODERATE | Broad scope is useful; mandatory verbosity and universal subsystem obligations are not. |
| **§2 — Definitions** | **REWRITE** | LOW initially; HIGH downstream | Essential, but current definitions distort authority, derivation, NAS, and actor models. |
| **§3 — Classification scheme** | **REWRITE** | LOW | Separate provenance, ratification, normative strength, and applicability. |
| **§4.1 — User sovereignty and bounded authority** | **KEEP AS UNIVERSAL INVARIANT** | MODERATE | Yes, with explicit rights and delegation scope. |
| **§4.2 — Lifetime preservation** | **KEEP AS ECOSYSTEM POLICY** | HIGH | Appropriate for designated lifetime data, not every artifact. |
| **§4.3 — Complete determinism** | **DOWNGRADE TO DEFAULT** | MODERATE–HIGH | Testability helps broadly; absolute determinism is unnecessary. |
| **§4.4 — Fixed priority ordering** | **REWRITE** | HIGH | Can produce unsafe decisions; requires domain hazard analysis. |
| **§5 — Feature-first modular monolith** | **DOWNGRADE TO DEFAULT** | MODERATE–HIGH | Valuable for many applications; excessive for tiny or non-feature-oriented systems. |
| **§6.1 — Replacement-safe data lifecycle** | **KEEP AS UNIVERSAL INVARIANT** | LOW–MODERATE | Yes, relative to declared preservation semantics. |
| **§§6.2–6.4 — Physical zones and Git bans** | **REWRITE** | MODERATE | Logical lifecycle separation survives; fixed topology and blanket bans do not. |
| **§7 — Canonical/derived architecture** | **REWRITE** | HIGH | Explicit authority survives; exact rebuildability and technology-based classification fail. |
| **§8 — Local/offline-first** | **KEEP AS ECOSYSTEM POLICY** | HIGH–VERY HIGH | Strong preference, with capability-specific remote dependencies. |
| **§9 — Cross-platform portability** | **KEEP AS ECOSYSTEM POLICY** | VERY HIGH | Avoiding lock-in is justified; simultaneous support for every target is not. |
| **§10 — NAS support** | **KEEP AS ECOSYSTEM POLICY** | HIGH–VERY HIGH | Intentional requirement; must distinguish access and deployment modes. |
| **§11 — Storage mechanisms** | **REWRITE** | HIGH | Safety outcomes justify effort; one universal algorithm does not. |
| **§12 — Authorized mutation** | **REWRITE** | MODERATE–HIGH | Enforcement survives; actor exclusions and prohibition of owner editing fail. |
| **§13 — AI tool contracts and risk tiers** | **MAKE CONDITIONAL** | MODERATE–HIGH | Applies to AI capabilities; fixed thresholds and universal previews fail. |
| **§14 — Authorization and deletion** | **REWRITE** | MODERATE | Effective enforcement survives; identical actor privileges and per-action confirmation do not. |
| **§15 — Permanent comprehensive auditing** | **REWRITE** | HIGH–VERY HIGH | Proportionate accountability is justified; unlimited sensitive history is not. |
| **§16 — Per-record lineage and verification** | **MAKE CONDITIONAL** | HIGH | Valuable for some domains; exact model/prompt lineage and blanket human verification are excessive. |
| **§17 — Drift detection** | **MAKE CONDITIONAL** | HIGH–VERY HIGH | Needed for supported out-of-band mutation models; all-file hashing is not universal. |
| **§18 — Reconciliation** | **REWRITE** | HIGH | Explicit conflict semantics survive; fixed workflows and blanket LWW prohibition fail. |
| **§19 — Reversal and compensation** | **REWRITE** | HIGH | Honest recoverability is broadly valuable; universal staging and prompts are not. |
| **§20 — Backup and restore** | **MAKE CONDITIONAL** | HIGH | Required for applicable retained state; recovery may be delegated and artifact policy must vary. |
| **§21 — Import/export** | **MAKE CONDITIONAL** | MODERATE–HIGH | Safe interchange is necessary where provided; all four export types are not. |
| **§22 — Synchronization** | **MAKE CONDITIONAL** | VERY HIGH | Justified where synchronization exists; not every app needs offline multi-writer behavior. |
| **§23 — AI state and memory** | **MAKE CONDITIONAL** | HIGH | Applies to AI systems; retention and authority need separate classification. |
| **§24 — Provider independence** | **DOWNGRADE TO DEFAULT** | MODERATE–HIGH | Useful isolation; universal substitutability is impossible. |
| **§25 — Security and dependencies** | **REWRITE** | MODERATE–HIGH | Threat-based protection survives; prescribed mechanisms contain errors and contradictions. |
| **§26 — Privacy and minimization** | **KEEP AS UNIVERSAL INVARIANT** | MODERATE–HIGH | Purpose-limited processing survives; per-action UI review and local-only defaults are policy mechanisms. |
| **§27 — Network exposure and zones** | **REWRITE** | MODERATE | Explicit secure exposure survives; topology does not establish trust. |
| **§28 — Reliability, retries, errors** | **REWRITE** | HIGH | Truthful outcomes and retry safety survive; absolute idempotency does not. |
| **§29 — Concurrency** | **REWRITE** | HIGH–VERY HIGH | Coordination is necessary when concurrency is possible; one protocol is not universal. |
| **§30 — Crash safety and atomicity** | **REWRITE** | HIGH–VERY HIGH | Requires bounded failure assumptions and declared transaction units. |
| **§31 — Migration** | **REWRITE** | HIGH–VERY HIGH | Recoverable evolution survives; liberal parsing and blind snapshot restore do not. |
| **§32 — Configuration** | **DOWNGRADE TO DEFAULT** | LOW–MODERATE | Explicit resolution is useful; fixed precedence and identical environments are not universal. |
| **§33 — Observability** | **MAKE CONDITIONAL** | MODERATE | Diagnostics should scale; health endpoints and full correlation machinery are not universal. |
| **§34 — Testing** | **REWRITE** | HIGH–VERY HIGH | Applicable guarantees require evidence; absent subsystems need no tests. |
| **§35 — Shared compliance harness** | **DOWNGRADE TO RECOMMENDATION** | HIGH | Useful automation, but syntax checks cannot certify semantics or safety. |
| **§36 — Deployment and lifecycle** | **MAKE CONDITIONAL** | HIGH–VERY HIGH | Support declared runtime modes with bounded startup/shutdown behavior. |
| **§37 — Documentation and contracts** | **KEEP AS ECOSYSTEM POLICY** | LOW–HIGH | Proportional living documentation is justified. |
| **§38 — Exceptions** | **REWRITE** | MODERATE, recurring | Necessary for policy governance; defaults need rationale, not impossibility proofs. |
| **§39 — Duplicated prohibitions** | **REMOVE** | LOW initially; HIGH drift cost | Retain only a non-normative index. |
| **§40 — Proposed-rule inventory** | **REWRITE** | LOW | Useful ratification metadata, but must match actual clause status. |
| **§41 — Open questions** | **REWRITE** | LOW | Preserve as decision records; correct unsupported factual claims. |
| **§42 — Adversarial probes** | **DOWNGRADE TO RECOMMENDATION** | MODERATE | Useful examples, not an exhaustive acceptance suite. |
| **§43 — Implementation freedom** | **REWRITE** | LOW–MODERATE | Preserve technology choice subject to explicit Rust-first and other ecosystem policies. |
| **§44 — Historical attestation** | **REMOVE** | LOW | Not an application governance rule. |
| **Supplied Rust-first policy** | **KEEP AS ECOSYSTEM POLICY** | MODERATE; domain-dependent | Defensible with technically justified, component-scoped exceptions. |

The most severe complexity mismatch affects tiny utilities, applications without AI, low-resource Raspberry Pi deployments, and browser/mobile environments. At the opposite extreme, the prescribed mechanisms become inadequate for millions of records, huge media collections, multi-user collaboration, and high-volume automation. The draft simultaneously overbuilds small systems and underspecifies difficult large-system guarantees.

## TOP 20 CHANGES BEFORE RATIFICATION

1. **Replace the global safety priority ordering.** Data preservation must not categorically outrank physical safety, security response, or required erasure.
2. **Repair mutation/audit commit semantics.** Eliminate the committed-but-unaudited crash window.
3. **Define NAS modes and correct unsafe coordination advice.** Address SQLite WAL limitations, stale lease holders, fencing, and uncertain write outcomes.
4. **Replace absolute crash and atomicity guarantees with explicit contracts.** State failure assumptions, acknowledgement meaning, and consistency boundaries.
5. **Fix migration recovery.** Remove liberal-acceptance guidance and prevent automatic restoration from destroying concurrent valid work.
6. **Resolve permanent auditing versus privacy and deletion.** Separate event integrity from indefinite sensitive-payload retention.
7. **Separate canonical authority from factual truth.** Remove automatic verification through human editing and account for machine-originated authoritative records.
8. **Make operation uncertainty first-class.** Specify what happens after timeouts, disconnections, and ambiguous external commits.
9. **Replace universal idempotency claims with actual retry protocols.** Include remote-system limits and duplicate-effect reconciliation.
10. **Repair AI risk classification.** Cover sensitive reads, external disclosure, cumulative scope, cost, physical effects, and delegated autonomy.
11. **Bind previews and approvals to execution conditions.** Remove unsupported promises of exact future effects.
12. **Separate derivation, disposability, authority, and preservation value.** Permit backup of expensive artifacts and preservation of non-reproducible outputs.
13. **Reconcile sovereignty with external editing.** Define supported adoption and rejection behavior without forbidding owners from controlling their own files.
14. **Distinguish actors from principals and delegation.** Remove the two-actor fiction and address shared ownership and administration.
15. **Rewrite storage prescriptions as outcome requirements.** Permit appropriate transaction, append, journal, and replacement mechanisms.
16. **Retain offline-first as a scoped ecosystem policy.** Do not queue stale or dangerous remote operations automatically.
17. **Scale feature-first architecture to application structure.** Remove folder-name dogma, shared-code size rules, and impossibility tests for process separation.
18. **Separate portability, buildability, testing, support, and packaging.** Remove universal container and platform obligations while preserving intentional NAS support.
19. **Repair the classification and exception system.** Separate provenance, ratification, applicability, and normative strength; eliminate duplicated contradictory rules.
20. **Integrate Rust-first explicitly into §43.** Preserve its justified-exception model and avoid implying that language choice supplies the safety guarantees the architecture must establish.
