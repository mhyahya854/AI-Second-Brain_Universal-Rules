<a id="audit-3"></a>
### 17.3. AUDIT-3 — Integrity claims and trust anchors

**Type:** CONDITIONAL | **Origin:** DERIVED ENGINEERING RULE | **Applies:** claims of tamper evidence

Claims MUST identify adversaries, protected references, verification, and recovery limits. Hashes detect changes relative to trusted references; attackers able to replace data and manifests can defeat comparison. Hash chains need protected anchors or independent evidence against wholesale rewriting. Encryption does not itself establish authorization or audit completeness. Authorized redaction/expiry MUST be distinguishable from unexplained alteration within the stated integrity model.

