<a id="s21"></a>
## 21. Reversal and recovery

<a id="recover-1"></a>
### 21.1. RECOVER-1 — Honest recovery semantics

**Type:** UNIVERSAL INVARIANT | **Origin:** DERIVED ENGINEERING RULE | **Applies:** undo, restoration, reversal, or compensation claims and recovery of important retained user state

Applications MUST describe actual recovery/compensation honestly and provide recovery where technically and operationally appropriate. Distinguish inverse mutation, transaction rollback, restoration, compensation, cancellation, reconciliation, and irreversible actions. Reversal MUST use current authority and constraints, not historical permission alone.

Communications cannot be recalled from recipients' knowledge. Refunds are separate effects; physical actions may be irreversible; APIs may need reconciliation. Restoring old global state MUST NOT be presented as safe undo without accounting for newer valid work. Expired/erased information may not be recoverable. Required reversal audit links to the original under [AUDIT-1](#audit-1).

For applications owning important retained user state, successful normal application startup MUST NOT be the only route to inspect, verify, extract, or recover otherwise recoverable information. Define an appropriate recovery route and its dependencies/limits in the App Plan, supported by proportionate evidence under [BACKUP-2](#backup-2) and [TEST-1](#test-1). A read-only recovery mode, independent reader, doctor tool, recovery executable, or documented portable inspection/export procedure may suffice. Neither a CLI nor a separate rescue application is required where the durable format already provides an adequate route. Recovery MUST preserve applicable authorization, privacy, and key-access constraints under [AUTH-1](#auth-1), [PRIV-1](#priv-1), and [BACKUP-1](#backup-1).

Recovery MUST distinguish corruption detection/diagnosis, derived-state rebuilding, verified canonical restoration, and canonical repair. It MUST NOT fabricate missing facts to claim a healthy state. When facts cannot be established, preserve uncertainty under [EVID-1](#evid-1), surface the problem, quarantine where appropriate, and stop destructive repair; [SAFE-1](#safe-1), [DATA-2](#data-2), and [EDIT-1](#edit-1) remain governing constraints.

Malware/ransomware recovery SHOULD, where applicable, contain affected clients/services, stop unsafe propagation, identify the best evidenced known-good canonical state/recovery points, validate backup integrity, restore or reconstruct canonical information, rebuild disposable derived state, reconcile legitimate newer information where safe, and rotate/revoke compromised credentials before validated sync resumption. Recovery MUST NOT overwrite the best surviving clean evidence merely for convenience. Recovery copies may themselves be corrupted, malicious, or already compromised; age or immutability does not establish cleanliness. Evidence and uncertainty follow [BACKUP-2](#backup-2) and [EVID-1](#evid-1), with privacy/deletion duties intact.

<a id="recover-2"></a>
### 21.2. RECOVER-2 — Prefer bounded reversibility

**Type:** DEFAULT | **Origin:** ARCHITECTURAL DECISION | **Applies:** mutations and consequential automation

Operations SHOULD offer scoped undo, reversible preparation, cancellation, or compensation where benefit justifies cost. Soft deletion may help; retention/privacy may require erasure. Communicate irreversible boundaries where relevant. Delegation can authorize automatic execution under [AUTH-2](#auth-2) and [AI-3](#ai-3) without repeated confirmation.

For retained user-owned data, destructive deletion SHOULD normally include a reversible stage where practical before permanent purge. Trash or pending-deletion state is one pattern, not a required directory. Explicit secure deletion, privacy/legal erasure, ephemeral/cache/temp data, safety/security needs, and other justified cases may require a different lifecycle. No indefinite retention is implied; [PRIV-1](#priv-1) and [SAFE-2](#safe-2) govern conflicting obligations.

