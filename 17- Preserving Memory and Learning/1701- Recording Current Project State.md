<a id="dev-9"></a>
### 31.9. DEV-9 — Project State as the current execution entry point

**Type:** ECOSYSTEM POLICY | **Origin:** USER POLICY | **Applies:** every active application

Each active application MUST maintain a concise machine-readable and human-readable Project State record, discoverable from the repository entry point. One record or consistently generated views MAY satisfy both forms; no exact format is mandated. Its sole governing responsibility is current execution status and navigation, not duplication of the full Master Plan or completed history.

Without prior conversation, it MUST reveal the current phase, last completed phase, completed capabilities, work in progress, work not started, known blockers, current branch/revision where applicable, next authoritative action, and the active phase specification's location. Identify the revision actually observed rather than inventing a self-referential commit identifier. Update status when work, blockers, phase completion, or next action changes; distinguish verified completion from claims awaiting verification. State/implementation contradictions MUST be reconciled before relying on that state to proceed.

Current and last verified completed subphases, unresolved errors, actual implementation status, exact next authorized action, and bare “Continue” behavior additionally follow [EXEC-4](../0-%20Start%20Here%20and%20Universal%20Rules/008-%20Continuing%20Previous%20Work.md#exec-4). A structured Markdown record with a documented stable field schema may satisfy both machine-readable and human-readable requirements; a prose-only status narrative without reliably identifiable fields does not satisfy the machine-readable duty.

