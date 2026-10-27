<a id="arch-2"></a>
### 6.2. ARCH-2 — Modular monolith by default

**Type:** DEFAULT | **Origin:** USER POLICY | **Applies:** ordinary feature-rich application deployment

A modular monolith SHOULD be preferred when it is the simplest design satisfying isolation, reliability, privilege boundaries, scaling, deployment, lifecycle, maintainability, and performance. Multiple processes/services may be justified by fault containment, plugin isolation, runtime incompatibility, independent lifecycle, hardware placement, operational economics, reliability, or scaling. Record the rationale; literal single-process impossibility is not required. Distribution adds network, transaction, deployment, and recovery responsibilities.

<a id="workspace-3"></a>
### 45.3. WORKSPACE-3 — Three architectures and meaningful folder contracts

**Type:** ECOSYSTEM POLICY | **Origin:** USER POLICY | **Applies:** substantial application planning, with workspace detail required for persistent-data applications

<a id="workspace-three-architectures"></a>
#### 45.3.1. Workspace, planning, and implementation responsibilities

Planning MUST separately assess and validate **A: User Data Workspace**, **B: Master Plan**, and **C: Codebase**, including cross-references and distinct ownership/responsibilities. If no user information is retained, document A as inapplicable. Master Plan retains [BLUEPRINT-1](#blueprint-1)'s Languages and Data, complete specification, Research and Decisions, Design, Reviews, Project State and sequential phases/subphases. Codebase retains feature-first frontend, backend, database and genuine shared responsibilities. `Codebase/Database/` schemas/migrations are development artifacts, not actual user data by default.

<a id="workspace-folder-contract"></a>
#### 45.3.2. Per-folder and per-file design contract

For substantial persistent-data applications, the data hierarchy MUST be explicitly designed, explained, challenged and validated before plan approval. An attractive tree alone is insufficient. Use extensive meaningful headings/subheadings without arbitrary heading limits. Each meaningful folder/file or documented homogeneous class MUST establish purpose, ownership, contents, format, naming, relationships, dependencies, authority/replica/projection/historical-evidence role, rebuildability, discovery, human reading, AI reading, permitted modification, change detection, corruption detection, recovery, relocation behavior, access controls, and retention. Class-level contracts must resolve every actual member's role; they cannot hide exceptional authoritative content.

Do not create customary or empty folders without a demonstrated responsibility. Validate the hierarchy through [WORKSPACE-TEST-1](#workspace-test-1), and keep the complete intended specification and its technical records consistent under [BLUEPRINT-2](#blueprint-2).

