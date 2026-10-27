<a id="s18"></a>
## 18. Privacy, retention, and deletion

<a id="priv-1"></a>
### 18.1. PRIV-1 — Purpose-limited processing and retention

**Type:** UNIVERSAL INVARIANT | **Origin:** DERIVED ENGINEERING RULE | **Applies:** sensitive/personal information collection, processing, disclosure, retention

Processing and retention MUST be limited to authorized purposes and applicable obligations. Audit, provenance, prompts, diagnostics, before/after state, model metadata, backups, and derived copies are included. Full prompts, secrets, personal information, and deleted payloads MUST NOT be retained merely because available.

Deletion/retention policies MUST define scope, timing, protected obligations, replicas, indexes, backups, and known limitations. Logical append-only history may coexist with authorized redaction, expiry, archival, key destruction, and cryptographic erasure. Preserve necessary evidence of lifecycle actions without recreating erased payloads. Restore MUST account for applicable deletion decisions rather than silently reinstating information contrary to policy.

Cryptographic erasure depends on effective key destruction and copies; it cannot recall disclosed plaintext. Soft deletion is not a universal substitute for erasure. Resolve conflicting rights and retention obligations through [SAFE-2](#safe-2) with a documented legitimate basis.

<a id="priv-2"></a>
### 18.2. PRIV-2 — Local data and deliberate disclosure

**Type:** ECOSYSTEM POLICY | **Origin:** USER POLICY | **Applies:** user-data storage and external transmission

Local machine/private NAS storage is the default. External disclosure MUST have informed authorization appropriate to purpose, destination, data scope, and principal. Standing delegation is permitted without per-request prompts. Remote-native functions follow [OFFLINE-1](#offline-1). Cloud AI requests SHOULD include only necessary relevant context. Local inference MAY help but does not prove other components transmit nothing. Diagnostic exports need sanitization and user control without mandatory manual inspection of every byte.

