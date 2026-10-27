<a id="s19"></a>
## 19. External editing and drift

<a id="edit-1"></a>
### 19.1. EDIT-1 — User control and safe adoption

**Type:** CONDITIONAL | **Origin:** USER POLICY | **Applies:** managed files/records accessible outside the ordinary runtime

Users may edit their own Markdown, source, configuration, documents, and open formats subject to legitimate shared rights. Applications MUST define supported edits, validation, adoption, conflicts, and rejection. They MUST NOT silently adopt unsafe state merely because it is in an expected directory. Unsupported edits may be rejected/quarantined without claiming ownership over user files. Reconciliation MUST avoid overwriting newer valid work or destroying the only recoverable copy without authority.

<a id="edit-2"></a>
### 19.2. EDIT-2 — Proportionate drift detection

**Type:** CONDITIONAL | **Origin:** DERIVED ENGINEERING RULE | **Applies:** storage models where external change affects claimed integrity

Detection MUST fit threats, dataset size, architecture, and acceptable latency. Hashes, versions, watcher hints, database versioning, service boundaries, snapshots, or reconciliation protocols are options; constant all-file hashing is not required. Watchers can miss changes and need validation/rescan strategies where the contract requires it.

Drift does not prove maliciousness or authorship. Snapshots can roll back data and a local manifest together; detection of that rollback needs evidence outside the boundary. Adoption, restoration, merge, preserved alternatives, and user decisions are possible resolutions subject to current-state coordination under [CON-1](#con-1).

