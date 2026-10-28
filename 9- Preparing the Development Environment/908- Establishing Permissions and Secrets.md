<a id="sec-2"></a>
### 25.2. SEC-2 — No accidental secret disclosure

**Type:** PROHIBITION | **Origin:** DERIVED ENGINEERING RULE | **Applies:** secrets and security credentials

Applications MUST NOT disclose usable secrets through unintended source control, logs, prompts, exports, or interfaces. Storage/delivery MUST match threats and permit appropriate revocation/rotation. Credential stores, managed services, protected configuration, and environment injection are options. Restricted plaintext local files may suit a bounded threat model; they do not isolate all same-account processes. Environment variables also have exposure paths.

Ignore rules and permissions are not complete access or history-erasure controls. Disclosures need appropriate containment, including revocation where needed. Removing a file from a current tree does not remove every historical copy.

