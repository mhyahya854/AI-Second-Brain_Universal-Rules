<a id="s02"></a>
## 2. Foundations and domain hazards

<a id="safe-1"></a>
### 2.1. SAFE-1 — Integrity and truthful guarantees

**Type:** UNIVERSAL INVARIANT | **Origin:** DERIVED ENGINEERING RULE | **Applies:** operations and retained information governed by an application contract

Applications MUST protect retained user data according to declared integrity and lifecycle contracts and MUST NOT silently corrupt it or misrepresent known loss. Intentional loss, transformation, or deletion requires applicable authority and accurate semantics. Important operation outcomes MUST be truthful under [OUT-1](#out-1). Guarantees require appropriate evidence under [TEST-1](#test-1), with limits and uncertainty disclosed.

<a id="safe-2"></a>
### 2.2. SAFE-2 — Domain-aware hazard decisions

**Type:** UNIVERSAL INVARIANT | **Origin:** DERIVED ENGINEERING RULE | **Applies:** conflicts among safety, security, privacy, integrity, and operational obligations

Applications MUST identify material domain hazards and applicable obligations and resolve conflicts on that basis. A global ranking MUST NOT force data preservation when it creates greater human, physical, security, or privacy harm or defeats applicable erasure duties. Emergency shutdown, credential revocation, and containment can require intentional interruption or loss. Record consequential tradeoffs and residual risks proportionately.

Example: a hardware controller may stop an actuator before persisting telemetry; an archive may prioritize retention under a legitimate preservation duty. Neither priority becomes a universal ordering for other domains.

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
| Universal Rules repository | This constitutional repository, whose active tree contains only `MASTER_PLAN.md`; historical Git refs preserve earlier supporting files. |
| App Master Plan / App Plan / historical APP Plan | The authoritative intended product specification and its planning responsibility in a future application; the complete specification follows BLUEPRINT-2. “Master Plan” folder names do not refer to this constitution's one-file tree. |
| Phase / subphase | Ordered bounded implementation contract and its smaller executable contracts, with validation gates, evidence, and numerical order under EXEC-1–EXEC-5. |
| Frozen candidate | Exact committed document bytes bound to recorded owner freeze authority; its identifier/digest is recorded outside those bytes to avoid self-reference. Freeze is not ratification. |
| Review convergence | Revision-bound satisfaction of GOV-5's findings, validation, regression, and two consecutive independent clean-round conditions; not a guarantee of correctness. |
| Approved implementation | Deliberately selected capability implementation and declared platform/configuration contract; failure never silently authorizes an alternative under NOFALL-1. |

<a id="s37"></a>
## 37. NO FALLBACKS in the App Plan or Codebase

<a id="nofall-1"></a>
### 37.1. NOFALL-1 — One approved implementation and honest failure

**Type:** PROHIBITION | **Origin:** USER POLICY | **Applies:** planned and implemented application capabilities after implementation selection

**NO FALLBACKS IN THE APP PLAN OR CODEBASE.** Once a capability's implementation is selected and approved, an executor MUST NOT introduce an alternative execution implementation to conceal or work around that implementation's failure. Prohibited behavior includes silent alternate algorithms or providers, hidden secondary databases, replacement execution paths triggered by primary failure, dummy implementations or mock results presented as functioning behavior, disabling required functionality or tests to claim success, fabricated success, silent error swallowing, and undocumented degraded substitutes. Merely naming a substitute an “adapter,” “resilience mode,” “recovery,” or “approved fallback” does not make it compliant.

Define the capability's selected implementation, configuration/platform scope, success criteria, and failure contract in the authoritative App Plan. On failure, report what is known, unknown, blocked, and safely recoverable under [OUT-1](#out-1), [RUN-2](#run-2), and [OPS-1](#ops-1). Implement error paths without falsifying effects or acknowledgements. Test fixtures, mocks, and simulations MAY be used in explicitly identified isolated tests/research; their outputs MUST NOT satisfy claims that real production behavior ran successfully.

<a id="nofall-2"></a>
### 37.2. NOFALL-2 — Safety, offline operation, and platform boundaries

**Type:** ECOSYSTEM POLICY | **Origin:** USER POLICY | **Applies:** interpretation and verification of NOFALL-1 across recovery, platform, offline, security, and synchronization contracts

The following distinctions MUST govern implementation and review:

| Existing responsibility | Compliant meaning under the prohibition |
|---|---|
| Errors, interruption, and rollback | Explicit failure, safe interruption, transaction rollback, security containment, and bounded crash recovery preserve the approved operation/state contract; they do not report substitute success. |
| Retry | A validated retry of the **same approved operation** remains subject to [RETRY-1](#retry-1), effect identity, uncertainty, authorization, and retry bounds. Switching providers/algorithms after failure is not a retry. |
| Backup and restoration | Independent backups and authorized restoration recover retained state under the declared recovery contract. Recovery MUST disclose restored points, losses, conflicts, and unknowns; it does not silently execute the failed capability through a second implementation. |
| Platforms and adapters | Deliberately selected platform adapters may differ by supported target while enforcing the same shared core contract. Their selection is based on the declared platform/configuration, not failure-triggered substitution. No requirement for identical binaries or one physical module is introduced. |
| Local/offline operation | Approved local capabilities are normal capabilities with their own contracts, available independently of online services. A network-dependent action that cannot complete stays failed, pending, or unknown as appropriate. Showing a cached view is permitted only as an explicitly designed view with disclosed freshness; it cannot masquerade as fresh remote success. |
| Synchronization and topology | Declared replicas, authorized topology transitions, and delayed operation queues preserve the same approved sync/authority semantics under [SYNC-1](#sync-1)–[SYNC-4](#sync-4). NAS loss MUST NOT silently create a new canonical database, weaken conflict rules, or acknowledge undelivered remote effects. |
| Optional AI/Hermes | Independent ordinary functionality remains available without optional AI. An AI-native operation remains unavailable/failed/unknown when its approved model cannot perform it; silently switching model/provider or inventing a result is prohibited. HERMES-1 and AI-4 retain their distinct scope. |
| Malware verification | Required gates under [IO-2](#io-2)–[IO-3](#io-3) remain enforced on scanner/signature failure. Independent local capabilities may continue; affected intake stays gated and protection state stays visible. A missing scanner MUST NOT activate an alternate engine or clean-result stub. An explicitly designed multi-engine scan pipeline, if justified, must require its specified stages/results and cannot treat one failed stage as success supplied by another. |
| Replacement and migration | An alternative may be researched, selected, and deliberately adopted as a future version/configuration through the normal planning, authority, migration, and verification gates. This is an explicit change to the approved implementation, not a dormant runtime rescue path. |

These distinctions preserve availability where honestly supported, recovery, privacy, malware containment, the shared core, and data integrity. They do not weaken existing gates. No fallback design is approved merely by listing two implementations in a plan; the plan MUST specify the independent legitimate responsibility of each or select one. Any genuine unresolved conflict MUST stop affected design/implementation and receive an explicit scoped decision under [GOV-3](#gov-3), without silent weakening of either rule.

Mandatory Current JSON and optional complete Master JSON are separate declared recovery representations, not alternate execution implementations. Folder JSON is their integrity and inventory manifest, not a fallback recovery engine. Verified restoration under [JSON-1](#json-1)–[JSON-4](#json-4) remains permitted; stale or incomplete representations MUST NOT silently count as successful saving. Explicit backup-file restoration is likewise an approved recovery operation, not a hidden implementation substitution.

