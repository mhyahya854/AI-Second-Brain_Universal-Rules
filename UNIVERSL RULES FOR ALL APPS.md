# UNIVERSAL RULES FOR ALL APPS
## A Comprehensive Architectural, Safety, Data, AI, Portability, and Governance Constitution

> **Status:** Working Master Constitution — Exhaustive Baseline Draft  
> **Document Identifier:** `ECOSYSTEM-CONST-001`  
> **Target Scope:** All applications, services, tools, and background processes developed or maintained within this ecosystem.  
> **Applicability:** Universal invariant baseline. Any deviation requires formal, documented exception approval under Section 38.

---

## TABLE OF CONTENTS

1. [Purpose & Scope of the Constitution](#1-purpose--scope-of-the-constitution)
2. [Definitions & Domain Terminology](#2-definitions--domain-terminology)
3. [Rule Classification & Tagging Schema](#3-rule-classification--tagging-schema)
4. [Fundamental Invariants & Core Philosophy](#4-fundamental-invariants--core-philosophy)
5. [Mandatory Feature-First Modular-Monolith Architecture](#5-mandatory-feature-first-modular-monolith-architecture)
6. [Structural Separation of Application Code & User Data](#6-structural-separation-of-application-code--user-data)
7. [Canonical vs. Derived State Architecture](#7-canonical-vs-derived-state-architecture)
8. [Local-First & Offline-First Core Design](#8-local-first--offline-first-core-design)
9. [Cross-Platform Portability (Windows, macOS, Linux, BSD)](#9-cross-platform-portability-windows-macos-linux-bsd)
10. [NAS & Private Network Storage as a First-Class Requirement](#10-nas--private-network-storage-as-a-first-class-requirement)
11. [Storage Architecture & Filesystem Semantics](#11-storage-architecture--filesystem-semantics)
12. [Authorized Mutation Model](#12-authorized-mutation-model)
13. [AI Tools & Skills as Capability Boundaries](#13-ai-tools--skills-as-capability-boundaries)
14. [Human Authorization & Operational Permissions](#14-human-authorization--operational-permissions)
15. [Complete Change Auditing & Event History](#15-complete-change-auditing--event-history)
16. [Provenance Tracking & Data Lineage](#16-provenance-tracking--data-lineage)
17. [External & Unauthorized Change Detection (Drift Detection)](#17-external--unauthorized-change-detection-drift-detection)
18. [Reconciliation Workflows & Conflict Resolution](#18-reconciliation-workflows--conflict-resolution)
19. [Rollback, Reversal, & State Recovery](#19-rollback-reversal--state-recovery)
20. [Backup & Restore Architecture](#20-backup--restore-architecture)
21. [Import & Export Protocols](#21-import--export-protocols)
22. [Synchronization & Multi-Client Coherence](#22-synchronization--multi-client-coherence)
23. [AI Architecture & Agent Integration](#23-ai-architecture--agent-integration)
24. [AI Model & Provider Portability / Decoupling](#24-ai-model--provider-portability--decoupling)
25. [Security Architecture & Threat Modeling](#25-security-architecture--threat-modeling)
26. [Privacy & Data Minimization](#26-privacy--data-minimization)
27. [Network Boundaries & Topology Isolation](#27-network-boundaries--topology-isolation)
28. [System Reliability & Resilient Engineering](#28-system-reliability--resilient-engineering)
29. [Concurrency Control & Multi-Worker Safety](#29-concurrency-control--multi-worker-safety)
30. [Crash Safety, Atomicity, & Data Protection](#30-crash-safety-atomicity--data-protection)
31. [Schema & Data Evolution / Migrations](#31-schema--data-evolution--migrations)
32. [Configuration Management & Environment Independence](#32-configuration-management--environment-independence)
33. [Observability, Logging, Diagnostics, & Health Telemetry](#33-observability-logging-diagnostics--health-telemetry)
34. [Comprehensive Testing Strategy](#34-comprehensive-testing-strategy)
35. [Universal Invariant Verification & Test Suites](#35-universal-invariant-verification--test-suites)
36. [Deployment, Service Packaging, & Containerization](#36-deployment-service-packaging--containerization)
37. [Architecture Documentation & Living Contracts](#37-architecture-documentation--living-contracts)
38. [Exception Governance & Deviation Process](#38-exception-governance--deviation-process)
39. [Substantially Expanded Prohibited Patterns & Anti-Patterns Catalog](#39-substantially-expanded-prohibited-patterns--anti-patterns-catalog)
40. [Derived & Proposed Rules Requiring Review](#40-derived--proposed-rules-requiring-review)
41. [Open Questions & Architectural Ambiguities](#41-open-questions--architectural-ambiguities)
42. [Adversarial Review Targets & Vulnerability Probes](#42-adversarial-review-targets--vulnerability-probes)
43. [Non-Universalized Technologies & Implementation Freedom](#43-non-universalized-technologies--implementation-freedom)
44. [Generation Boundary Attestation](#44-generation-boundary-attestation)

---

## 1. PURPOSE & SCOPE OF THE CONSTITUTION

### 1.1 Purpose `[ESTABLISHED]`
This constitution establishes the common architectural, safety, durability, data governance, AI integration, deployment, auditability, recovery, and user sovereignty baseline for all applications built within this ecosystem. Its primary objective is to guarantee that every application respects user sovereignty, protects durable lifetime data, survives runtime or hardware replacement, and operates safely when driven by human users, autonomous AI agents, or background automations.

### 1.2 Non-Brevity Mandate `[ESTABLISHED]`
This document is intentionally constructed to favor **completeness over concision**. In engineering systems operating with high-autonomy AI agents and mission-critical personal or enterprise data, ambiguous guidelines lead directly to architectural decay, silent data corruption, security breaches, and vendor lock-in. Every section provides comprehensive requirements, clear boundaries, and explicit mechanisms.

### 1.3 Scope of Enforcement `[ESTABLISHED]`
This constitution applies to:
- Every interactive graphical user interface (GUI) application (desktop, local web, mobile).
- Every command-line interface (CLI) and developer tool.
- Every background service, daemon, worker process, and scheduled automation job.
- Every headless API service and local IPC server.
- Every AI skill, agent tool, pipeline, and cognitive workflow integrated into the software.

No project developed within this ecosystem is exempt from these invariants unless a formal, written exception is filed and approved in strict adherence to [Section 38: Exception Governance & Deviation Process](#38-exception-governance--deviation-process).

---

## 2. DEFINITIONS & DOMAIN TERMINOLOGY

### 2.1 Core Actor Definitions `[ESTABLISHED]`
- **The User:** The sovereign owner of the machine, the environment, and the persistent data. The user possesses ultimate moral and operational authority over all canonical records.
- **The Application:** A deterministic software tool designed to execute business logic, enforce domain invariants, manage storage, and render interfaces on behalf of the user. The application serves the user; it does not own the user's data.
- **The AI / Agent:** An external or internal probabilistic cognitive operator equipped with bounded tools and skills. The AI acts exclusively as an unprivileged or selectively privileged operator within constraints strictly enforced by deterministic code.

### 2.2 Storage & State Definitions `[ESTABLISHED]`
- **Canonical State:** The authoritative, irreplaceable, ground-truth record of user data and domain entities. If canonical state is lost, permanent data loss has occurred.
- **Derived State:** Secondary, ephemeral, or cache data computed deterministically or probabilistically from canonical state (e.g., search indexes, vector embeddings, thumbnails, materialized query caches, generated summaries). Derived state may be purged at any time and fully reconstructed from canonical state.
- **External Change (Drift):** Any modification, insertion, or deletion occurring on files, databases, or storage devices hosting canonical state that did not pass through an authorized application mutation pipeline.

### 2.3 Architectural & Operational Definitions `[ESTABLISHED]`
- **Authorized Mutation Pathway:** A strictly defined, deterministic software pipeline through which an authorized actor issues an intent, validates inputs against domain invariants, executes business logic, records an immutable audit log, and mutates canonical state.
- **Modular Monolith:** An architectural design that organizes an entire application within a single unified process or codebase, strictly partitioned into autonomous, domain-bounded feature packages with zero circular dependencies.
- **NAS (Network Attached Storage):** A remote network filesystem share (e.g., SMB, NFS) operating across a private Local Area Network (LAN), subject to variable latency, sudden disconnections, lack of POSIX locking guarantees, and concurrent client access.
- **Local-First:** An architectural paradigm where core read and write capabilities execute against local storage without requiring active internet connectivity, third-party cloud authentication, or external API availability.

---

## 3. RULE CLASSIFICATION & TAGGING SCHEMA

Every directive and rule in this constitution is classified under two orthogonal dimensions: **Epistemic Authority** and **Normative Strength**.

### 3.1 Epistemic Authority Tags `[ESTABLISHED]`
- `[ESTABLISHED]`: Explicitly mandated by core architectural directives, foundational session context, or absolute universal system requirements. These represent immutable pillars.
- `[PROPOSED / DERIVED]`: A logically necessary implication, engineering safeguard, or architectural extension derived systematically from `[ESTABLISHED]` principles to ensure their practical enforceability.
- `[CONDITIONAL]`: An invariant whose technical application depends strictly on whether the specific feature, modality, or capability exists within a given application (e.g., rules governing vector databases apply only if vector search is implemented).

### 3.2 Normative Strength Levels `[ESTABLISHED]`
To eliminate ambiguity, requirements throughout this constitution use standard normative terms:
- **MANDATORY INVARIANT (MUST / SHALL / STRICTLY REQUIRED):** Non-negotiable structural requirements. Violation constitutes an architectural failure.
- **DEFAULT ARCHITECTURE (SHOULD / DEFAULT):** The mandatory default pattern. Divergence is permitted only through documented architectural rationale or formal exception.
- **RECOMMENDED PRACTICE (RECOMMENDED):** High-value engineering guidance that should be adopted unless specific technical constraints dictate an alternative.
- **CONDITIONAL REQUIREMENT (CONDITIONAL):** Mandatory if and only if the corresponding architectural component or feature is utilized.
- **STRICTLY PROHIBITED (MUST NOT / FORBIDDEN):** Architectural anti-patterns, dangerous practices, or security hazards that are completely banned.
- **EXCEPTION PROCESS (DEVIATION PROTOCOL):** The formal governance mechanism required to bypass any mandatory rule.

---

## 4. FUNDAMENTAL INVARIANTS & CORE PHILOSOPHY

### 4.1 The Core Philosophy of User Sovereignty `[ESTABLISHED]`
All applications built under this ecosystem are governed by a single philosophical foundation:
1. **The user owns the data.** The user's lifetime data belongs exclusively to the user, not to an application vendor, cloud provider, database engine, or AI model.
2. **The application is an ephemeral tool operating on that data.** The application exists to read, modify, visualize, and analyze the user's data according to deterministic rules. If the application disappears, is rewritten, or is replaced, the user's underlying canonical data must remain accessible, intact, and durable.
3. **The AI is an untrusted operator using granted capabilities.** An AI model is an assistive cognitive worker. It must never possess unmediated authority over canonical state, it must never bypass domain validation, and it must never silently redefine application truth.
4. **Neither UI nor AI is the authority.** Domain invariants and data integrity rules must reside in deterministic core code below all user interfaces and agent layers.

```
+-------------------------------------------------------------------------+
|                              THE USER                                   |
|               (Sovereign Owner of Lifetime Canonical Data)              |
+-------------------------------------------------------------------------+
                                     |
               +---------------------+---------------------+
               |                                           |
               v                                           v
    +----------------------+                   +----------------------+
    |    HUMAN OPERATOR    |                   |       AI AGENT       |
    | (Interacting via UI) |                   | (Interacting via API)|
    +----------------------+                   +----------------------+
               |                                           |
               | [Requests Intent]                         | [Invokes Tool]
               v                                           v
+-------------------------------------------------------------------------+
|                       AUTHORIZED CAPABILITY BOUNDARY                    |
|    - Schema Validation        - Rate & Scope Limits                     |
|    - Role & Permission Checks - Explicit Previews & Dry-Runs            |
+-------------------------------------------------------------------------+
                                     |
                                     v
+-------------------------------------------------------------------------+
|                       DETERMINISTIC DOMAIN CORE                         |
|    - Invariant Enforcement    - Business Rule Logic                     |
|    - State Transitions        - Transaction Boundaries                  |
+-------------------------------------------------------------------------+
                                     |
               +---------------------+---------------------+
               |                                           |
               v                                           v
+-----------------------------+             +-----------------------------+
|    CANONICAL MUTATION       |             |     APPEND-ONLY AUDIT       |
| (Durable, Crash-Safe Store) |             | (Immutable Provenance Log)  |
+-----------------------------+             +-----------------------------+
               |
               v
+-------------------------------------------------------------------------+
|                       DERIVED STATE PIPELINES                           |
| (Search Indexes, Vector Embeddings, Previews, Cache Materialization)    |
+-------------------------------------------------------------------------+
```

### 4.2 Lifetime Data Preservation Guarantee `[ESTABLISHED]`
An application MUST be designed under the assumption that the user will want to access, read, and preserve their data 30 years into the future, long after the original programming language version, framework, operating system, and hardware architecture have become obsolete. Data must not be trapped in opaque, proprietary, undocumented binary blobs when standardized, inspectable, or openly documented formats are viable.

### 4.3 Determinism vs. Probability Doctrine `[ESTABLISHED]`
- Critical operations—including identity resolution, validation, mathematical calculations, permissions, state transitions, migrations, storage operations, and reconciliation—MUST be 100% deterministic.
- Probabilistic AI models may propose actions, summarize text, draft content, or extract semantic parameters, but deterministic application code SHALL make all authoritative mutation and validation decisions.

### 4.4 Rule Priority Hierarchy `[ESTABLISHED]`
When architectural requirements, performance goals, or design ideals conflict during development, the conflict MUST be resolved using the following strict priority ordering:
1. **Prevention of Data Loss and Silent Corruption:** No performance optimization, UX convenience, or feature velocity may risk canonical integrity.
2. **User Safety, Security, and Privacy:** Defense against unauthorized access, credential leakage, and malicious execution.
3. **User Ownership, Portability, and Recoverability:** Ensuring the user can inspect, extract, back up, and restore their information anywhere.
4. **Correctness and Deterministic Domain Invariants:** Absolute compliance with business rules and relational constraints.
5. **Auditability and Provenance Tracking:** Complete transparency into how, when, and by whom data was altered.
6. **Platform Portability and Deployability:** Seamless operation across Windows, macOS, Linux, and NAS environments.
7. **Maintainability and Feature Modularity:** Clean, decoupled, feature-first codebase organization.
8. **Performance and Resource Efficiency:** Bounded latency, efficient memory usage, and background processing.
9. **Operational Convenience:** Tooling ergonomics, developer shortcuts, and automated defaults.
10. **Cosmetic and Visual Uniformity:** Superficial styling and design embellishments.

---

## 5. MANDATORY FEATURE-FIRST MODULAR-MONOLITH ARCHITECTURE

### 5.1 Architecture Baseline: Modular Monolith by Default `[ESTABLISHED]`
All applications SHALL be organized as a **feature-first modular monolith** by default. 
- Distributing an application into microservices, separate micro-frontends, or multiple network-coordinated processes simply because an application is complex, feature-rich, or large is **STRICTLY PROHIBITED**.
- In-process module boundaries, strict interface contracts, and clean domain isolation deliver identical architectural decoupling without the operational failures, network latency, distributed transaction complexity, serialization overhead, and deployment fragility inherent in microservices.
- Physical service decomposition is permitted ONLY if an operational requirement (such as independent hardware scaling, distinct security clearance boundaries, or distinct runtime environments) cannot be met within a single process, and must be approved via the Exception Process.

### 5.2 Elimination of Giant Layer Dumping Grounds `[ESTABLISHED]`
Organizing the root or top-level architecture into giant global technical layers is **STRICTLY PROHIBITED**. The following folder structures are explicitly forbidden as primary architectural boundaries:
- `/controllers`
- `/services`
- `/models`
- `/repositories`
- `/views`
- `/utils`
- `/helpers`

When code is organized into horizontal technical layers, domain logic relating to a single business capability is fractured across 7 disparate folders. Unrelated features become tightly coupled, code navigation degrades, and AI coding agents lose localized context, resulting in frequent regressions.

### 5.3 Feature Encapsulation & Self-Contained Domain Modules `[ESTABLISHED]`
Every business capability MUST be housed in its own self-contained feature directory. A feature module owns its entire vertical slice of functionality. Where technically applicable, a feature module SHALL contain:
- **Domain Concepts & Models:** Entities, value objects, domain events, domain exceptions.
- **Business Rules & Invariants:** Validation logic, calculation rules, state machine transitions.
- **Use Cases & Application Services:** Commands, queries, handlers, orchestration workflows.
- **Interfaces & Ports:** Abstract definitions for persistence, external communication, and notifications.
- **Adapters & Persistence Logic:** Database queries, repositories, file serializers, schema mappings.
- **Interface Handlers & Controllers:** Local HTTP/RPC endpoints, CLI commands, IPC message handlers.
- **UI Components:** Views, components, view-models, and presentation state specific to the feature.
- **AI Tools / Skills:** Schemas, tool handlers, and prompt templates exposing feature verbs to agents.
- **Feature Tests:** Unit, integration, invariant, and contract tests for the feature.
- **Documentation:** Architectural notes, invariant specifications, and schema definitions for the feature.

#### Canonical Feature Module Directory Layout `[PROPOSED / DERIVED]`
```
src/features/<feature_name>/
├── domain/                  # Pure deterministic entities, invariants, value objects
│   ├── entities.ts
│   ├── value-objects.ts
│   └── invariants.ts
├── application/             # Use cases, commands, queries, orchestration
│   ├── commands/
│   ├── queries/
│   └── services.ts
├── ports/                   # Abstract interfaces for external dependencies
│   ├── repository.port.ts
│   └── notifier.port.ts
├── adapters/                # Concrete persistence, filesystem, or protocol implementations
│   ├── persistence/
│   └── external/
├── presentation/            # User-facing UI components or CLI handlers
│   ├── components/
│   └── views/
├── ai/                      # AI tools, function-calling schemas, capability boundaries
│   ├── tools.json
│   └── tool-handlers.ts
├── tests/                   # Feature-specific test suite
│   ├── unit/
│   ├── integration/
│   └── invariants/
└── README.md                # Feature domain documentation and invariants
```

### 5.4 Governance of Shared, Common, and Platform Code `[ESTABLISHED]`
- Any folder named `shared`, `common`, `platform`, `core`, or `lib` MUST remain deliberately tiny and strictly governed.
- It is **STRICTLY PROHIBITED** for `shared` or `common` to become an unorganized dumping ground for convenience functions, orphaned helpers, or mixed business logic.
- Code placed in `shared` MUST be completely domain-agnostic (e.g., a generic RFC-4122 UUID generator, an atomic file-renaming utility, a cryptographic hashing helper).
- **Rule of Duplication vs. Coupling `[ESTABLISHED]`:** Prefer the duplication of small, obvious, domain-specific code (e.g., 5 lines of validation logic or a localized DTO) over the introduction of an inappropriate cross-domain coupling through a shared helper.
- If Feature A and Feature B both need a common domain concept, that concept must either:
  1. Belong squarely to one feature, with the other feature accessing it via an explicit, read-only public query contract; or
  2. Be promoted to a dedicated, first-class feature module (e.g., an `Identity` or `Workspace` feature) with its own bounded context.

### 5.5 Inter-Feature Communication Contracts `[PROPOSED / DERIVED]`
1. Direct in-memory manipulation of another feature's internal domain state, private tables, or private filesystem structures is **STRICTLY PROHIBITED**.
2. Features MUST communicate across boundaries using one of three approved mechanisms:
   - **Public Application Services (Facade / Query Ports):** Strongly-typed public functions returning immutable DTOs (Data Transfer Objects).
   - **Domain Events (In-Process Pub/Sub):** Asynchronous or synchronous broadcast of immutable event payloads (e.g., `TaskCompletedEvent`, `DocumentArchivedEvent`).
   - **Command Dispatchers:** Explicit command execution mediated by domain-level authorization.
3. Circular dependencies between feature packages are strictly forbidden. Dependency graphs must remain directed and acyclic (DAG).

---

## 6. STRUCTURAL SEPARATION OF APPLICATION CODE & USER DATA

### 6.1 The Non-Entanglement Mandate `[ESTABLISHED]`
Under no circumstances shall durable user-owned data be co-located or trapped inside the application implementation, source code repository, deployment bundle, or container image. 
- Application code is completely disposable, replaceable, and upgradable.
- User data is permanent, durable, and sovereign.
- A complete wipe and re-installation of the application binary or codebase must leave 100% of user data, user configuration, and audit logs unharmed and immediately re-attachable.

### 6.2 Standardized Storage Topology `[ESTABLISHED]`
Every application MUST organize its physical filesystem footprints into distinct, decoupled storage zones. These zones may be mounted to different physical disks, network shares, or volumes.

```
<Storage Root>/
├── app/          # DISPOSABLE: Application binaries, runtime engines, libraries
├── data/         # CANONICAL: Irreplaceable, user-owned canonical state
│   ├── primary/  # Core relational or structured canonical documents
│   └── blobs/    # Canonical user assets (images, PDFs, media, attachments)
├── config/       # USER/HOST: Environment and preference settings
│   ├── app.json  # Safe defaults and user preferences
│   └── secrets/  # Local-only credentials and cryptographic keys
├── derived/      # DISPOSABLE: Fully regenerable indexes and caches
│   ├── search/   # Search engine index files (e.g., Tantivy, SQLite FTS)
│   ├── vectors/  # Vector databases and embedding caches
│   └── previews/ # Image thumbnails, audio waveforms, cached previews
├── audit/        # PERMANENT: Append-only immutable historical audit trail
│   └── events/   # Sequenced, tamper-evident audit records
├── cache/        # DISPOSABLE: Transient computation caches, temporary files
├── logs/         # ROTATING: Operational diagnostics and error logs
├── backups/      # PROTECTED: Point-in-time snapshots and archive bundles
└── exports/      # STAGING: User-requested data export artifacts
```

### 6.3 Zone Characteristics & Durability Contracts `[PROPOSED / DERIVED]`
Every application SHALL enforce the operational characteristics defined in the following table:

| Storage Zone | Durability Classification | Backup Required? | Auto-Deletable by OS? | Git Tracking Permitted? |
| :--- | :--- | :--- | :--- | :--- |
| `app/` | Disposable / Replaceable | No (Managed by Installer) | No | Yes (Source only) |
| `data/` | **Canonical / Irreplaceable** | **MANDATORY** | **NEVER** | **STRICTLY PROHIBITED** |
| `config/` | Persistent / User-Owned | Yes | Never | Prohibited (Secrets) |
| `derived/` | Ephemeral / Rebuildable | No (Regenerable) | Permitted on disk pressure | Strictly Prohibited |
| `audit/` | **Permanent / Append-Only** | **MANDATORY** | **NEVER** | Strictly Prohibited |
| `cache/` | Ephemeral / Transient | No | Permitted anytime | Strictly Prohibited |
| `logs/` | Rotating / Diagnostic | Optional | Permitted via logrotate | Strictly Prohibited |
| `backups/` | Archival / Historical | Yes (External sync) | Never | Strictly Prohibited |
| `exports/` | Transient / User Artifact | No | Permitted after expiry | Strictly Prohibited |

### 6.4 Git Tracking Anti-Pattern `[ESTABLISHED]`
- Checking user-owned canonical data, secrets, operational logs, or local database files into a Git source code repository is **STRICTLY PROHIBITED**.
- Git is a source code and documentation versioning tool. It is not an enterprise database, an asset store, or a backup engine for user data.
- Every project root MUST maintain an exhaustive `.gitignore` blocking data directories, database files, audit logs, caches, and `.env` files from ever entering source control.

---

## 7. CANONICAL VS. DERIVED STATE ARCHITECTURE

### 7.1 The Boundary of Ground Truth `[ESTABLISHED]`
An application must maintain an absolute, unambiguous division between what constitutes **Canonical State** and what constitutes **Derived State**.
- **Canonical State** is the authoritative master record created or confirmed by the user. If an entity exists only in a search index, vector store, or cache, it does not exist canonically.
- **Derived State** is any projection, index, representation, or accelerated data structure calculated from canonical state.

### 7.2 Derived State Rebuildability Guarantee `[ESTABLISHED]`
- It is a **MANDATORY INVARIANT** that all derived state MUST be 100% regenerable from canonical state.
- If all derived state stores (search indexes, vector embeddings, image thumbnails, summary caches, materialized SQL views) are completely destroyed or corrupted, executing a deterministic command (e.g., `app-cli rebuild-derived-state`) must restore all derived structures to complete parity with canonical data.
- The user's durable information must never depend upon the operational survival of a vector database, an elasticsearch cluster, or an LRU cache.

### 7.3 Canonical Store Mutation Exclusivity `[ESTABLISHED]`
- Derived state generation must be an asynchronous or strictly decoupled downstream subscriber to canonical mutation events.
- Writes to derived state MUST NOT be permitted to alter, inject, or back-propagate mutations into canonical state without executing an independent, fully authorized domain mutation pipeline.

---

## 8. LOCAL-FIRST & OFFLINE-FIRST CORE DESIGN

### 8.1 Offline Autonomy & Zero-Cloud Guarantee `[ESTABLISHED]`
Every application whose core functional domain does not inherently require a live telecommunication counterparty (e.g., live chat, collaborative multiplayer games) MUST function completely without active internet connectivity.
- Core reading, authoring, editing, navigating, searching, and local auditing MUST NOT block on, require, or fail due to external cloud services or network outages.
- An application must never present a blank screen, lock out user access, or abort operations because an external license server, cloud API, or telemetry endpoint is unreachable.

### 8.2 Graceful Network Degradation `[ESTABLISHED]`
Applications that utilize external network APIs or AI cloud providers SHALL implement explicit degradation boundaries:
- When offline, cloud-dependent capabilities (such as remote AI summarization or cloud synchronization) must cleanly disable or queue their operations while notifying the user via unambiguous UI/CLI messaging.
- Queued actions must be locally audited and persisted in a resilient local queue, ready for idempotent execution upon network reconnection.
- Local canonical operations must continue to execute without interruption regardless of network state.

---

## 9. CROSS-PLATFORM PORTABILITY (WINDOWS, MACOS, LINUX, BSD)

### 9.1 Operating System Neutrality `[ESTABLISHED]`
Applications must be architected to operate consistently across:
- **Windows (x64, ARM64)**
- **macOS (Apple Silicon, Intel)**
- **Linux (Debian, Ubuntu, Fedora, Alpine, Arch)**
- **NAS / Private Server Environments (TrueNAS, Synology DSM, Unraid, QNAP)**

### 9.2 Path Portability & Absolute Path Prohibition `[ESTABLISHED]`
Hardcoding developer-specific, machine-specific, or OS-specific absolute paths into application code, database records, configuration files, test fixtures, or documentation is **STRICTLY PROHIBITED**.
- Prohibited patterns include:
  - `C:\Users\username\...`
  - `/home/username/...`
  - `D:\project\...`
  - `/Users/dev/...`
- All filesystem references MUST be dynamically resolved at runtime relative to explicitly discovered or configured environment anchors (e.g., `$APP_DATA_DIR`, `$XDG_DATA_HOME`, `%APPDATA%`, or relative application root).
- Paths stored in canonical databases or serialized documents MUST use normalized, portable relative path descriptors or canonical URI schemes (e.g., `file://attachments/doc1.pdf` or `relative://blobs/img.png`), never platform-locked drive letters or OS roots.

### 9.3 Filesystem Semantics Normalization `[ESTABLISHED]`
Applications must account for critical filesystem differences across operating systems:
- **Path Separators:** Always utilize runtime path-joining abstractions (e.g., `path.join()`, `std::path::PathBuf`, or `os.path.join`). Never assume `/` or `\` in string manipulations.
- **Case Sensitivity:** Windows (NTFS) and macOS (APFS by default) are case-insensitive but case-preserving. Linux (ext4, btrfs, ZFS) is case-sensitive. Code MUST treat filenames as strictly case-sensitive to ensure cross-platform compatibility.
- **Forbidden Characters:** Windows filenames disallow `< > : " / \ | ? *` and reserved names (`CON`, `PRN`, `AUX`, `NUL`, `COM1-9`, `LPT1-9`). Applications MUST sanitize all user-supplied or AI-generated file names against a universal safe-character subset before writing to disk.
- **Line Endings:** Canonical text files and audit records MUST use standard LF (`\n`) line endings. CR-LF (`\r\n`) must be normalized to LF upon ingress.

---

## 10. NAS & PRIVATE NETWORK STORAGE AS A FIRST-CLASS REQUIREMENT

### 10.1 NAS Support is an Architectural Imperative `[ESTABLISHED]`
Designing an application exclusively for high-speed local NVMe solid-state storage and treating Network Attached Storage (NAS) as an unsupported edge case is **STRICTLY PROHIBITED**.
- Private NAS deployments (TrueNAS, Synology, QNAP, Unraid, custom Linux ZFS/Btrfs shares) over SMB or NFS are first-class deployment targets for all applications in this ecosystem.
- NAS support must be baked into the I/O architecture from inception, not patched on as an afterthought.

### 10.2 NAS Architectural Compatibility vs. Mandatory Dockerization `[ESTABLISHED]`
- **Docker / Containerization does NOT equal NAS compatibility.** Running an application inside a Docker container mounted to an SMB share does not magically resolve network latency, filesystem locking failures, or cache incoherence.
- Docker is an optional deployment packaging mechanism, NOT the definition of NAS compatibility.
- An application is NAS-compatible if and only if its core storage and I/O engine natively handles the operational realities of remote network shares.

### 10.3 Network Filesystem Realities & Hazards `[ESTABLISHED]`
When reading from or writing to storage hosted on a NAS share across a private LAN, the application MUST account for:
1. **High and Variable Latency:** Network round-trips over 1GbE/10GbE introduce 0.5ms to 50ms of latency per operation compared to 0.02ms on local NVMe. Sequential small-file operations will cause massive slowdowns unless batched or buffered.
2. **Sudden Physical Disconnections:** WiFi dropouts, switch reboots, NAS sleep states, and IP re-assignments cause immediate network share severing during active I/O.
3. **Flawed Locking Semantics (SMB/NFS Locks):**
   - SQLite, BerkeleyDB, and standard file locking mechanisms (`flock`, `fcntl`, `LockFileEx`) are notoriously unreliable, partially broken, or non-atomic over SMB and NFS shares.
   - Using standard SQLite multi-process write concurrency directly over an SMB share without explicit WAL/VFS mitigations or dedicated server wrappers invites database corruption.
4. **Delayed Write Flushing & Opportunistic Locks (Oplocks):** NAS storage appliances aggressively cache writes. An application must issue explicit synchronous flush calls (`fsync`, `FlushFileBuffers`) when committing canonical data.
5. **Permission Mapping & UID/GID Asymmetry:** The user running the application on a Windows workstation or macOS laptop rarely has identical UID/GID mapping on the remote Linux-based NAS. Storage access MUST accommodate restrictive permissions (`0755`, `0644`) and avoid assuming `chmod`/`chown` control.

### 10.4 Safe NAS I/O Design Patterns `[PROPOSED / DERIVED]`
Applications targeting or supporting NAS storage SHALL implement the following patterns:
- **Client-Server Service Partitioning for Relational DBs:** If an application relies on a heavy relational database (e.g., PostgreSQL, multi-user SQLite), the database engine MUST run as a daemon directly on the NAS server or host machine, with clients connecting via authenticated TCP/IP, rather than mounting raw database files over SMB/NFS.
- **Document / Chunked Store for Direct Filesystem Mode:** If the application operates directly on files across a NAS share, canonical state must be stored as partitioned, immutable or atomically replaceable content-addressed chunks/documents (e.g., JSON, YAML, Markdown, Parquet) rather than a single monolithic binary database file.
- **Heartbeat & Mount Pre-Flight Verification:** Before initiating canonical operations, the storage adapter MUST verify share accessibility, write permissions, and disk space availability via a non-destructive probe.

---

## 11. STORAGE ARCHITECTURE & FILESYSTEM SEMANTICS

### 11.1 Format Selection: Correctness and Integrity Over Ideology `[ESTABLISHED]`
- Plaintext formats (Markdown, JSON, YAML) are highly valued for transparency and lifetime readability. However, **correctness, data integrity, transactional safety, and concurrency control take absolute precedence over format ideology**.
- Applications requiring complex relational queries, high-frequency updates, full-text indexing, or multi-entity transactions MUST use an appropriate robust storage engine (e.g., SQLite with proper VFS/WAL configuration, DuckDB, PostgreSQL, or an ACID-compliant key-value store) rather than fragile homegrown flat-file parsers.
- Where binary or embedded database formats are utilized, the application MUST provide automated, scheduled, and on-demand export pipelines that dump all canonical state into documented, portable, human-readable open formats (JSON, CSV, Markdown, Parquet).

### 11.2 The Atomic Write Protocol (Temp-Write -> Flush -> Atomic Rename) `[ESTABLISHED]`
Overwriting an existing canonical file directly in-place is **STRICTLY PROHIBITED**. Sudden power failure, application crash, or network interruption during an in-place write truncates and destroys the file.
- All file-based canonical mutations MUST follow the **Atomic Replacement Protocol**:
  1. **Write to Temporary File:** Create a unique temporary file in the *same physical directory* (or filesystem mount) as the target file (e.g., `.document.json.tmp.<uuid>`). Writing on the same mount is mandatory to guarantee an atomic rename.
  2. **Serialize and Write Data:** Stream all data into the temporary file.
  3. **Flush and Sync Buffers:** Call explicit OS sync primitives (`fsync` on POSIX, `FlushFileBuffers` on Windows) to force all bytes from OS and network buffers onto persistent media.
  4. **Atomic Rename / Replace:** Atomically rename the temporary file over the destination file using platform-safe atomic rename primitives (`rename` on POSIX, `MoveFileExW` with `MOVEFILE_REPLACE_EXISTING` on Windows).
  5. **Directory Sync (POSIX):** Call `fsync` on the parent directory to guarantee directory entry persistence.

```
+-------------------------------------------------------------------------+
|                    ATOMIC FILE REPLACEMENT PROTOCOL                     |
+-------------------------------------------------------------------------+
|                                                                         |
|  1. Target File Exists:     [ canonical_data.json ]                     |
|                                                                         |
|  2. Create Temp File on     [ canonical_data.json.tmp.8f1a ]            |
|     Same Filesystem Mount:                                              |
|                                                                         |
|  3. Stream & Complete Write: [ Write Bytes 100% ]                       |
|                                                                         |
|  4. Force Media Flush:       fsync() / FlushFileBuffers()               |
|                                                                         |
|  5. Atomic Rename:           MOVEFILE_REPLACE_EXISTING                  |
|                              [ canonical_data.json.tmp.8f1a ]           |
|                                         |                               |
|                                         v                               |
|                              [ canonical_data.json ] (Atomic Swap)      |
|                                                                         |
|  6. Sync Parent Directory:   fsync(parent_directory)                   |
|                                                                         |
+-------------------------------------------------------------------------+
```

### 11.3 File Locking and Concurrency Discipline `[PROPOSED / DERIVED]`
- Any application process writing to shared storage MUST implement explicit concurrency coordination.
- Advisory locks (`flock`, `lockf`) must be combined with timestamp-based or cryptographic optimistic concurrency checks (e.g., `expected_version` or `ETag` match) to detect race conditions across multiple client processes or NAS clients.
- If a lock cannot be acquired within a bounded timeout, the application MUST NOT hang indefinitely. It must abort gracefully, log the contention event, and notify the user with an actionable message.

---

## 12. AUTHORIZED MUTATION MODEL

### 12.1 The Cardinal Invariant of Mutation Authority `[ESTABLISHED]`
Canonical application state MAY ONLY be modified through authorized, deterministic application mutation pathways. 
- Direct, unmediated manipulation of canonical databases, storage files, or configuration stores by users, scripts, or AI models is **STRICTLY PROHIBITED**.
- Every state change must be an expression of intent evaluated against strict domain rules, executing within transactional boundaries, producing an immutable audit record, and propagating to derived state stores.

### 12.2 The Dual Actor Model `[ESTABLISHED]`
The application recognizes exactly two primary external actors capable of initiating mutations:
1. **The Human User:** Initiating changes via approved graphical user interfaces (GUI), command-line interfaces (CLI), or authenticated local APIs.
2. **The Authorized AI Agent:** Initiating changes via approved application tools, skills, or structured function calls.

Neither actor is granted divine authority. Both actors MUST traverse the exact same underlying domain validation and business invariant pipeline. An AI agent is not permitted special backdoors, and a human user is not permitted to bypass relational or data consistency constraints.

```
+---------------------------------------------------------------------------------------------------+
|                                  THE AUTHORIZED MUTATION PIPELINE                                 |
+---------------------------------------------------------------------------------------------------+
|                                                                                                   |
|  [ HUMAN OPERATOR (UI) ]                [ AI AGENT (Tool Call) ]                                  |
|            |                                       |                                              |
|            v                                       v                                              |
|   +------------------------------------------------------------------+                            |
|   | 1. INTENT RECEPTION & SCHEMA VALIDATION                          |                            |
|   |    - Validate input payload syntax, types, ranges, references    |                            |
|   +------------------------------------------------------------------+                            |
|                                    |                                                              |
|                                    v                                                              |
|   +------------------------------------------------------------------+                            |
|   | 2. AUTHORIZATION & CAPABILITY VERIFICATION                       |                            |
|   |    - Check actor permissions, token validity, verb scope         |                            |
|   |    - Evaluate risk tier (Read-Only, Reversible, Destructive)     |                            |
|   +------------------------------------------------------------------+                            |
|                                    |                                                              |
|                                    v                                                              |
|   +------------------------------------------------------------------+                            |
|   | 3. DETERMINISTIC DOMAIN INVARIANT ENFORCEMENT                    |                            |
|   |    - Execute state transition logic, entity rules, constraints   |                            |
|   |    - Reject invalid state transitions deterministically          |                            |
|   +------------------------------------------------------------------+                            |
|                                    |                                                              |
|                                    v                                                              |
|   +------------------------------------------------------------------+                            |
|   | 4. ATOMIC CANONICAL MUTATION                                     |                            |
|   |    - Commit transaction to database / Atomic file replacement    |                            |
|   +------------------------------------------------------------------+                            |
|                                    |                                                              |
|                                    v                                                              |
|   +------------------------------------------------------------------+                            |
|   | 5. IMMUTABLE AUDIT LOG GENERATION                                |                            |
|   |    - Record actor, tool, timestamp, pre/post state, correlation  |                            |
|   +------------------------------------------------------------------+                            |
|                                    |                                                              |
|                                    v                                                              |
|   +------------------------------------------------------------------+                            |
|   | 6. DOWNSTREAM DERIVED STATE PROPAGATION                          |                            |
|   |    - Update search index, trigger vector embedding, clear cache  |                            |
|   +------------------------------------------------------------------+                            |
|                                                                                                   |
+---------------------------------------------------------------------------------------------------+
```

### 12.3 Prohibition of Unrestricted AI Authority `[ESTABLISHED]`
Granting an AI agent raw, unconstrained write authority over the storage layer is **STRICTLY PROHIBITED**.
- An AI model SHALL NOT be provided with tools that allow it to:
  - Execute arbitrary SQL queries (`sqlite3.execute(user_input)`).
  - Write, overwrite, or delete arbitrary files on the filesystem.
  - Directly mutate JSON/YAML/database state stores using unstructured text or patch scripts.
  - Drop tables, alter schemas, or truncate logs.
- Instead, applications MUST expose **bounded, semantic domain verbs** representing discrete, safe application actions:
  - `tasks.create(title, priority, dueDate)`
  - `documents.rename(documentId, newTitle)`
  - `entities.archive(entityId, reason)`
  - `tags.attach(entityId, tagId)`
  - `inventory.adjustQuantity(itemId, delta, justification)`
- The domain verb defines what mutation is permissible. The AI specifies the parameters of its intent. Deterministic application code performs the actual write.

---

## 13. AI TOOLS & SKILLS AS CAPABILITY BOUNDARIES

### 13.1 Tool Contract Architecture `[ESTABLISHED]`
AI tools, plugins, and skills are not mere convenience wrappers; they are **enforced capability boundaries** and security perimeters. Every AI tool MUST adhere to the following architectural requirements:
- **Strict Machine-Readable Schema:** Every tool must define a rigorous JSON Schema or OpenAPI specification detailing all input properties, data types, value constraints, required fields, and return formats.
- **Fail-Fast Boundary Validation:** Tool inputs must be rigorously validated at the ingress boundary before passing to domain services. Malformed inputs must return structured, descriptive errors explaining precisely what parameter failed and why.
- **No Natural-Language Invariant Encoding:** Critical domain invariants MUST NEVER be offloaded to prompt instructions (e.g., instructing the AI in a prompt *"Please ensure the task priority is never set to 0"*). Invariants MUST be enforced deterministically in code.
- **Structured Return Envelopes:** AI tools must return structured payloads containing execution status, affected entity IDs, new version numbers, and audit correlation IDs, enabling deterministic multi-step agent reasoning.

### 13.2 Tool Risk Classification Hierarchy `[ESTABLISHED]`
Every AI-facing tool MUST be explicitly tagged with a risk classification determining its execution protocol:

| Risk Tier | Definition & Scope | Approval Requirement | Execution Protocol |
| :--- | :--- | :--- | :--- |
| **Tier 1: Read-Only** | Queries, data fetching, search, summarization, inspection. No canonical mutation. | Autonomous | Immediate execution. |
| **Tier 2: Low-Risk Reversible** | Non-destructive mutations (e.g., adding a tag, appending a note, adjusting a draft). Easy undo. | Autonomous / Configurable | Execute and log rollback event. |
| **Tier 3: Moderate Mutation** | State transitions, updating canonical records, archiving entities, bulk tagging. | User Confirmation or Policy Rule | Optional dry-run preview before execution. |
| **Tier 4: High-Risk Destructive**| Hard deletions, permanent unlinks, mass updates (>10 records), configuration changes. | **MANDATORY USER CONFIRMATION** | Mandatory preview / dry-run output displayed to user before commitment. |
| **Tier 5: Administrative** | Schema migrations, data imports, system resets, credential rotation. | **MANDATORY EXPLICIT USER OVERRIDE** | High-friction authentication gate; never autonomous. |

### 13.3 Preview and Dry-Run Requirement `[ESTABLISHED]`
Any AI tool operating at Tier 3, Tier 4, or Tier 5 MUST provide a `dry_run=true` execution mode. 
- When invoked in dry-run mode, the tool must compute the exact changes that *would* occur without committing writes to disk.
- The tool must return a structured preview answering:
  1. Exactly which entities and attributes will be altered.
  2. How many total records are affected.
  3. Whether the operation is fully reversible.
  4. What specific audit events will be generated.

---

## 14. HUMAN AUTHORIZATION & OPERATIONAL PERMISSIONS

### 14.1 Authorization Below the User Interface `[ESTABLISHED]`
Authorization, permission checking, and domain invariant enforcement MUST exist at the application and domain boundary, completely independent of the presentation layer.
- Relying exclusively on UI-level controls (e.g., disabling a button, hiding a menu item, hiding an edit field) as a security or validation mechanism is **STRICTLY PROHIBITED**.
- Any action executable via the UI must produce the identical validation, authorization, and audit results if executed via a CLI command, a local IPC socket, an API call, or an automated script.

### 14.2 Deletion Safety & Confirmation Safeguards `[ESTABLISHED]`
- Permanent, irreversible deletion of user data MUST be treated as an exceptional, high-hazard operation.
- **Soft Deletion by Default:** Applications MUST default to soft deletion (e.g., `archived_at = timestamp`, moving items to a recyclable `Trash` state, or marking records as inactive) rather than performing immediate destructive SQL `DELETE` or file `unlink` operations.
- Destructive operations MUST require explicit human confirmation. UI interfaces must clearly convey the gravity of destruction, detailing the items to be destroyed and whether secondary assets (attachments, historical revisions) are included.
- AI tools MUST NOT be granted recursive or bulk hard-deletion capabilities.

---

## 15. COMPLETE CHANGE AUDITING & EVENT HISTORY

### 15.1 Append-Only Audit Trail Mandate `[ESTABLISHED]`
Every authoritative mutation affecting canonical application state MUST generate a permanent, append-only, tamper-evident audit record.
- Silent mutations are an architectural violation.
- Audit records MUST NEVER be updated, overwritten, truncated, or deleted in place under normal operational conditions.
- If an audit record contains erroneous data or reflects an operation that is subsequently reversed, a new, distinct **compensating event** or **reversal event** must be appended to the log referencing the original event ID. Historical reality must not be rewritten.

### 15.2 Mandatory Audit Event Payload Schema `[ESTABLISHED]`
Every audit event MUST capture sufficient telemetry to enable forensic reconstruction of the state transition. The record SHALL contain:

```json
{
  "event_id": "01J9Y5B4E8Z1Q7M3K9P2X4R6T8",
  "correlation_id": "req-98f1c4a2-7b3e-4d1a-8c29-3f0b2a7d6e5c",
  "parent_event_id": null,
  "timestamp": "2026-10-05T20:55:00.124Z",
  "actor": {
    "actor_id": "agent-orchestrator-01",
    "actor_type": "AI_AGENT", 
    "identity": "gemini-3.8-flash-high",
    "authentication_context": "local_session"
  },
  "mechanism": {
    "interface": "TOOL_CALL",
    "tool_name": "tasks.update_status",
    "tool_version": "1.2.0"
  },
  "target": {
    "entity_type": "Task",
    "entity_id": "task-8841",
    "entity_version_before": 3,
    "entity_version_after": 4
  },
  "delta": {
    "field": "status",
    "previous_value": "IN_PROGRESS",
    "new_value": "COMPLETED"
  },
  "reason": "Agent verified all sub-criteria met in user prompt",
  "execution_status": "SUCCESS",
  "reversible": true,
  "rollback_token": "rb-01J9Y5B4E8Z1Q7M3K9P2X4R6T8"
}
```

### 15.3 Classification of Initiator Types `[ESTABLISHED]`
Every audit event must explicitly record its initiating actor category:
- `HUMAN_UI`: Initiated directly by the user via graphical interface controls.
- `HUMAN_CLI`: Initiated by the user via interactive terminal commands.
- `AI_AGENT`: Initiated by an autonomous or semi-autonomous AI model executing a tool.
- `AUTOMATION`: Initiated by a local cron job, scheduled background daemon, or reactive watcher.
- `IMPORT`: Created via bulk data ingestion from external files.
- `SYNCHRONIZATION`: Propagated from a peer client or remote node via sync protocol.
- `MIGRATION`: Created during an automated database schema or format upgrade.
- `SYSTEM_RECOVERY`: Generated by an automated crash-recovery or reconciliation process.

### 15.4 Operational Logs vs. Audit Trails `[ESTABLISHED]`
Operational diagnostics (system logs) and immutable change audit trails are distinct architectural constructs and MUST be separated:
- **Operational Logs (`/logs`):** Ephemeral, high-volume debugging info (e.g., HTTP request traces, thread lifecycles, memory stats). Rotated and purged regularly.
- **Audit Event Logs (`/audit`):** Authoritative, permanent business transaction history. Irreplaceable and critical for user provenance and legal sovereignty. Never rotated into oblivion.

---

## 16. PROVENANCE TRACKING & DATA LINEAGE

### 16.1 Lineage Attribution Standard `[ESTABLISHED]`
Every canonical record and entity MUST maintain traceable lineage metadata answering:
1. **Source of Origin:** Where did this record originate (e.g., user manual creation, PDF import, API ingest, AI generation)?
2. **Author Identity:** Who created or modified the record (human user ID, specific AI model name and version, import script name)?
3. **Creation Context:** Under what session, task prompt, or operational run was the record established?
4. **Transformation History:** If the record was transformed (e.g., OCR scanned, summarized, merged), what prior entities served as inputs?

### 16.2 Distinguishing AI Output from Human Ground Truth `[ESTABLISHED]`
- An application MUST NEVER silently elevate probabilistic AI output to verified canonical fact.
- Any entity, field, or document synthesized by an AI model MUST carry an explicit provenance flag (e.g., `is_generated: true`, `generated_by: "gemini-3.8-flash"`, `verified_by_user: false`).
- Unverified AI-generated content must be clearly styled in UI/CLI outputs to prevent misleading the user into assuming human verification.
- Human user edits or explicit user confirmations clear the unverified tag, converting the record into verified canonical state while recording the transition in the audit log.

---

## 17. EXTERNAL & UNAUTHORIZED CHANGE DETECTION (DRIFT DETECTION)

### 17.1 The Threat Model of Out-of-Band Mutation `[ESTABLISHED]`
Because applications in this ecosystem are local-first, user-sovereign, and deployable on NAS network shares, canonical files and databases CAN and WILL be modified outside the application's runtime. External changes occur when:
- The user directly edits a Markdown, JSON, or YAML file using an external editor (e.g., VS Code, Obsidian, Vim).
- Third-party file synchronization tools (Syncthing, Dropbox, Nextcloud, rsync) replace files on disk.
- NAS snapshots are restored, or network shares are manipulated by another machine.
- Backup utilities or rogue scripts touch canonical directories.

### 17.2 The Non-Trust Invariant `[ESTABLISHED]`
An application MUST NOT silently assume that files on disk are trustworthy or valid simply because they reside in the canonical data directory.
- The application MUST actively detect external drift.
- External drift must not silently bypass domain validation or corrupt internal relational state.

### 17.3 Drift Detection Mechanisms `[ESTABLISHED]`
Applications SHALL maintain independent integrity tracking metadata to detect out-of-band changes:
- **Cryptographic Hashes:** Maintain SHA-256 content hashes of all managed files in an integrity manifest or sidecar index.
- **Entity Generation Tokens / Version Stamps:** Incrementing integer sequence tokens or UUIDs stored inside file frontmatter or database rows.
- **Filesystem Change Watchers:** Inotify / ReadDirectoryChangesW / FSEvents listeners coupled with startup integrity scans.

### 17.4 Drift Processing Pipeline `[ESTABLISHED]`
When an external mutation is detected, the application MUST execute a 5-stage pipeline:
1. **DETECT:** Identify that a file's content hash or timestamp does not match the application's internal integrity manifest.
2. **LOG:** Record an `EXTERNAL_MUTATION_DETECTED` event in the audit log.
3. **FLAG / TAINT:** Mark the affected entity in memory and storage as `TAINTED_UNVERIFIED_EXTERNAL_CHANGE`.
4. **CLASSIFY:** Parse the external change against domain validation rules to determine if it is valid syntax, compliant with business invariants, or corrupted/malformed.
5. **RECONCILE:** Route the change into the formal reconciliation workflow described in Section 18.

---

## 18. RECONCILIATION WORKFLOWS & CONFLICT RESOLUTION

### 18.1 The Prohibition of Silent Last-Write-Wins (LWW) `[ESTABLISHED]`
Silent Last-Write-Wins (overwriting existing data without checking versions or alerting the user) is **STRICTLY PROHIBITED**. LWW is the primary cause of silent data loss in local-first, multi-device, and NAS systems.

### 18.2 Canonical Reconciliation Actions `[ESTABLISHED]`
When external drift or synchronization conflicts occur, the application MUST resolve them through one of five explicit pathways:
1. **Adopt / Accept:** The external change is structurally valid, complies with all domain invariants, and is cleanly incorporated into canonical state. An audit event is generated attributing the change to `ACTOR_EXTERNAL_MUTATION`.
2. **Reject & Restore:** The external change violates critical domain invariants, is corrupted, or represents an illegal state. The application rejects the change, quarantines the corrupted file, and restores the canonical state from the last valid snapshot or audit log.
3. **Merge (Deterministic Field-Level):** If the external change modified Field A while the application modified Field B concurrently, and the domain allows field-level merges, apply a deterministic merge, record the composite state, and update the integrity manifest.
4. **Preserve Both (Fork / Branching):** When an automatic merge is impossible, the application duplicates the conflicting record (e.g., `Document (Conflicted Copy 2026-10-05).md`), preserving both copies without data loss.
5. **Request User Decision:** Present a clear, visual three-way diff to the user (Local Known State vs. External State vs. Common Ancestor) and await sovereign user resolution.

---

## 19. ROLLBACK, REVERSAL, & STATE RECOVERY

### 19.1 The Principle of Reversible Operations `[ESTABLISHED]`
Every authorized application mutation SHOULD be designed to be completely reversible wherever technically feasible. Reversible operations provide safety for human experimentation and autonomous AI workflows.

### 19.2 Reversal Architecture & Compensation Events `[ESTABLISHED]`
- Rolling back a change MUST NOT destroy or erase historical audit events.
- A rollback is itself an authoritative state change. When a user or agent invokes `undo()` or `revert(eventId)`:
  1. The application verifies that the target state is safe to restore.
  2. The application applies the inverse mutation (compensating transaction).
  3. A new audit record of type `COMPENSATING_REVERSAL_EVENT` is appended, explicitly referencing the target `event_id`.
  4. The entity version is incremented.

### 19.3 Limits of Reversal & External Side Effects `[PROPOSED / DERIVED]`
Where an operation involves external, non-reversible side effects (e.g., transmitting an outbound email, executing a financial transaction, writing to a physical hardware port):
- The operation MUST be split into a reversible pre-stage (preparation, drafting, validation) and an irreversible commit stage.
- High-friction warnings and explicit confirmation MUST precede any irreversible commitment.
- Compensating workflows (e.g., sending a cancellation notice) must be explicitly registered if the external system supports them.

---

## 20. BACKUP & RESTORE ARCHITECTURE

### 20.1 The Restore-First Doctrine `[ESTABLISHED]`
A backup that has never been successfully restored is a hallucination. 
- An application's backup strategy is legally and architecturally incomplete until its **restore procedure is fully specified, automated, and tested**.
- Developers MUST NOT declare an application backup-ready simply because it creates a zip archive or copies files to a NAS folder.

### 20.2 Scope of Backup Bundles `[ESTABLISHED]`
Backup operations MUST capture everything required to reconstruct canonical reality, and MUST exclude disposable derived state:
- **INCLUDED IN BACKUP:**
  - Complete canonical data directory (`/data`).
  - Active configuration and user settings (`/config`).
  - Full immutable audit event history (`/audit`).
  - Schema migration history and integrity manifests.
- **EXCLUDED FROM BACKUP:**
  - Search engine index files (`/derived/search`).
  - Vector database embeddings (`/derived/vectors`).
  - Thumbnail, preview, and audio waveform caches (`/derived/previews`).
  - Ephemeral application caches (`/cache`).
  - Operational diagnostic logs (`/logs`).
  - Temporary export staging files (`/exports`).

### 20.3 Verification & Integrity of Backups `[PROPOSED / DERIVED]`
- Every backup archive MUST generate and store an internal cryptographic manifest (SHA-256 checksums of all constituent files, total byte count, application schema version, timestamp).
- The application SHALL provide an automated command (e.g., `app verify-backup <archive>`) that validates archive integrity without writing to active canonical storage.

---

## 21. IMPORT & EXPORT PROTOCOLS

### 21.1 Non-Destructive Imports `[ESTABLISHED]`
- Ingesting data from external files (CSV, JSON, Markdown bundles, external DBs) MUST NEVER blindly overwrite existing canonical entities.
- Importers must validate all incoming records against domain invariants.
- If imported entities conflict with existing records, the importer MUST support explicit conflict policies: `skip`, `overwrite_with_audit`, `fork_as_copy`, or `prompt_user`.
- All imported entities MUST retain provenance indicating their source file, import timestamp, and executing actor.

### 21.2 Non-Destructive Exports `[ESTABLISHED]`
- Executing a data export MUST be a strictly read-only operation. An export operation SHALL NOT mutate canonical records, alter entity versions, or prune historical logs.
- Export formats MUST be documented, open, and platform-neutral.

### 21.3 Export Typology Classification `[ESTABLISHED]`
Applications MUST clearly distinguish between four distinct types of exports:
1. **Full Canonical Snapshot:** Complete raw export of all canonical data, configuration, and audit logs for migration to another system.
2. **Human-Readable Export:** Beautifully structured Markdown, PDF, or HTML bundles designed for human reading and offline archival.
3. **Interoperability Export:** Standardized open interchange formats (e.g., vCard, iCalendar, GeoJSON, Parquet, SQLite dump) designed for ingestion by external software.
4. **Diagnostic / Audit Report:** Chronological reports of system activity, metrics, and audit events for auditing or troubleshooting.

---

## 22. SYNCHRONIZATION & MULTI-CLIENT COHERENCE

### 22.1 Distributed Authority Invariants `[ESTABLISHED]`
In multi-device, local-first, or NAS-shared environments where multiple instances of the application operate on the same logical dataset:
- A clear **Source of Authority** must be established.
- Synchronization engines MUST handle offline operation gracefully. Modifications made while disconnected from the LAN or sync server must be queued locally and merged safely upon reconnection.

### 22.2 Conflict Resolution & State Merging `[ESTABLISHED]`
- Applications utilizing synchronization MUST implement explicit conflict detection mechanisms (e.g., Lamport timestamps, vector clocks, content hashes, or state-based CRDTs).
- Conflicts that cannot be deterministically resolved at the field level MUST be elevated to the user or branched into side-by-side versions.
- Synchronization workers MUST execute mutations through the authorized mutation pipeline, generating audit records with `actor_type: SYNCHRONIZATION`.

---

## 23. AI ARCHITECTURE & AGENT INTEGRATION

### 23.1 The Subservient Agent Paradigm `[ESTABLISHED]`
In this ecosystem, an Artificial Intelligence (AI) model or Autonomous Agent is an **assistive cognitive operator**, not an autonomous owner or divine arbiter of the system.
- The AI operates entirely within capabilities granted to it by deterministic application code.
- The AI possesses zero ambient authority. It cannot read files, write databases, or invoke external APIs unless explicit tools are mounted into its execution context.
- An AI model's internal beliefs, weights, training data, and conversational memory are ephemeral and non-authoritative. The application's canonical store remains the sole source of ground truth.

```
+-------------------------------------------------------------------------+
|                  AI INTEGRATION & SEPARATION OF POWERS                  |
+-------------------------------------------------------------------------+
|                                                                         |
|   +-----------------------------------------------------------------+   |
|   |                       COGNITIVE LAYER (AI)                      |   |
|   |   - Probabilistic Reasoning    - Semantic Extraction            |   |
|   |   - Natural Language Intent    - Tool Selection                 |   |
|   |   - Draft Content Synthesis    - User Prompt Interpretation     |   |
|   +-----------------------------------------------------------------+   |
|                                    |                                    |
|                       Tool Call / Structured Intent                     |
|                                    v                                    |
|   +-----------------------------------------------------------------+   |
|   |                  CAPABILITY BOUNDARY (Tools/Skills)             |   |
|   |   - JSON Schema Validation     - Permission Scope Enforcement   |   |
|   |   - Rate Limiting & Quotas     - Parameter Normalization        |   |
|   +-----------------------------------------------------------------+   |
|                                    |                                    |
|                       Validated Command Execution                       |
|                                    v                                    |
|   +-----------------------------------------------------------------+   |
|   |                 DETERMINISTIC APPLICATION CORE                  |   |
|   |   - Domain Business Rules      - Relational Invariants          |   |
|   |   - ACID Transactions          - Append-Only Auditing           |   |
|   |   - Crash-Safe Storage Commit  - Integrity Verification         |   |
|   +-----------------------------------------------------------------+   |
|                                                                         |
+-------------------------------------------------------------------------+
```

### 23.2 Stateless Cognition vs. Stateful Core `[ESTABLISHED]`
- AI cognition MUST be treated as completely stateless and replaceable.
- The application MUST NOT depend on the internal state, conversational context window, or hidden memory of an AI model to preserve domain consistency.
- Any state that must survive between AI invocations MUST be formalized into explicit, inspectable application entities (e.g., `TaskStep`, `AgentSession`, `ConversationHistoryRecord`) stored in canonical storage with full provenance.

### 23.3 AI Memory Architecture & Governance `[ESTABLISHED]`
Where applications provide "AI Memory" (long-term semantic retrieval, user preference memory, agent scratchpads):
- **Explicit Storage Zone:** AI memory must be stored in a dedicated, inspectable store (`/data/ai_memory/` or dedicated database tables).
- **Inspectable and Mutable by the User:** The human user MUST be able to view, search, edit, export, and delete any memory retained by the AI. Hidden, un-erasable cognitive memory is **STRICTLY PROHIBITED**.
- **Non-Authoritative Status:** AI memory is secondary metadata. It must NEVER override canonical application records, business rules, or user configuration.
- **Independent Lifecycle:** Deleting an entity in canonical storage MUST trigger an automated cascade or prompt to remove corresponding memory traces from AI memory and vector stores.

### 23.4 Search & Embeddings as Derived Ephemeral State `[ESTABLISHED]`
- Vector databases (e.g., Chroma, Qdrant, LanceDB, pgvector, sqlite-vec) and full-text search indexes (e.g., Tantivy, Lucene, SQLite FTS5) MUST be treated as **purely derived, ephemeral state**.
- Vector embeddings are mathematical projections of canonical documents generated by specific model checkpoints (e.g., `text-embedding-3-small`, `bge-large-en`).
- If an embedding model is upgraded, or if the vector index file becomes corrupted, the application MUST be able to delete the entire vector store and rebuild all embeddings directly from the canonical documents.
- A vector database MUST NEVER be the sole repository for user data.

---

## 24. AI MODEL & PROVIDER PORTABILITY / DECOUPLING

### 24.1 The Provider-Agnostic Core Invariant `[ESTABLISHED]`
Applications must be architecturally immune to AI vendor obsolescence, pricing changes, rate limits, API deprecations, and model degradation.
- Embedding vendor-specific SDKs (e.g., OpenAI SDK, Anthropic SDK, Google GenAI SDK) or vendor-specific API payload shapes directly inside feature or domain logic is **STRICTLY PROHIBITED**.
- All AI interactions MUST pass through an abstract, strongly-typed **AI Provider Adapter Port** located in the application architecture.

```
src/features/<feature>/application/
          |
          v
ports/ai/
  ├── language-model.port.ts   # Abstract text generation & tool invocation
  ├── embedding.port.ts        # Abstract vector generation
  ├── vision.port.ts           # Abstract image analysis
  └── transcription.port.ts    # Abstract audio transcription
          ^
          |
adapters/ai/
  ├── local-ollama.adapter.ts  # Concrete Ollama / llama.cpp driver
  ├── gemini.adapter.ts        # Concrete Google Gemini driver
  ├── openai.adapter.ts        # Concrete OpenAI-compatible driver
  └── mock.adapter.ts          # Deterministic test stub driver
```

### 24.2 Resilience to Model Failure, Hallucination, and Degradation `[ESTABLISHED]`
The application MUST continue to function, preserve data, and maintain relational integrity even when:
- The configured AI provider is completely offline, unreachable, or throwing HTTP 5xx errors.
- The AI provider returns invalid JSON, hallucinations, or syntactically broken tool calls.
- The AI model is downgraded to a smaller, less capable local model (e.g., switching from Claude 3.5 Sonnet to Llama-3-8B-Instruct).
- The user chooses to disable AI capabilities entirely.

Under zero circumstances may an AI error cause canonical database corruption or application crash.

---

## 25. SECURITY ARCHITECTURE & THREAT MODELING

### 25.1 Threat Modeling for Local, LAN, and NAS Applications `[ESTABLISHED]`
Local and NAS-hosted applications face distinct threat vectors compared to multi-tenant public SaaS platforms:
- **Local Malicious Processes:** Other programs running on the user's workstation attempting to read canonical databases, steal secrets, or corrupt files.
- **Untrusted Network LAN Exposure:** Other devices on a shared home or office network (smart TVs, IoT devices, compromised guest laptops) scanning for open ports.
- **Prompt Injection & Indirect Injection:** Adversarial data injected into emails, web pages, or documents imported into the application, designed to trick the AI agent into executing unauthorized tool calls.
- **Dependency & Supply Chain Poisoning:** Malicious packages slipped into deep node_modules, Python wheels, or crate dependencies.

### 25.2 Secret Management & Zero Secrets in Version Control `[ESTABLISHED]`
- Storing API keys, encryption keys, tokens, or passwords in Git repositories, source files, or unencrypted canonical documents is **STRICTLY PROHIBITED**.
- Secrets MUST be loaded dynamically from:
  1. Operating system secure credential stores (Windows Credential Manager, macOS Keychain, Linux Secret Service).
  2. Local, uncommitted environment files (`.env.local`) strictly ignored by Git.
  3. Explicitly protected, restricted configuration files (`config/secrets.json` with `0600` permissions).
- Applications MUST provide clear mechanisms for the user to view which keys are set and rotate them at will.

### 25.3 Dependency Discipline & Supply Chain Hygiene `[ESTABLISHED]`
- Third-party dependencies MUST be evaluated ruthlessly. Do not add heavy dependencies for trivial utility functions that can be implemented cleanly in 10 lines of standard library code.
- All dependencies MUST be pinned with exact lockfiles (`package-lock.json`, `poetry.lock`, `Cargo.lock`, `go.sum`).
- Build pipelines and security scans SHOULD regularly audit dependencies against known CVE databases.

### 25.4 The Principle of Least Privilege across All Actors `[ESTABLISHED]`
Every actor (user sessions, AI agents, background workers, sync adapters) SHALL operate with the absolute minimum privilege required to execute their specific task.
- Read operations must use read-only database connections or read-only filesystem handles.
- Background workers must not possess administrative credentials.
- AI agents must be scoped exclusively to tools relevant to the active user prompt.

---

## 26. PRIVACY & DATA MINIMIZATION

### 26.1 Strict Data Minimization & Local Boundary Confinement `[ESTABLISHED]`
- Applications must collect, process, and retain ONLY the data strictly necessary to fulfill the application's stated functionality.
- Canonical user data MUST remain on the user's local machine or private NAS by default.
- Transmitting user data to third-party cloud servers, telemetry collectors, or external analytics platforms without explicit, informed, opt-in consent from the user is **STRICTLY PROHIBITED**.

### 26.2 AI Prompt Leakage Prevention `[ESTABLISHED]`
When integrating external cloud-hosted AI models (e.g., Google, Anthropic, OpenAI):
- The application MUST transmit ONLY the minimal context window required to execute the specific tool call or prompt.
- Dumping entire databases, unrelated user files, or credentials into prompt context is **STRICTLY PROHIBITED**.
- The application SHOULD allow the user to select local-only AI inference (via Ollama, llama.cpp, LocalAI) for sensitive datasets, ensuring zero bytes of private data leave the local network.

### 26.3 Sanitization and Redaction in Logs and Telemetry `[ESTABLISHED]`
- Operational logs, error traces, crash dumps, and diagnostic bundles MUST be sanitized to scrub:
  - Passwords, API keys, and bearer tokens.
  - Personal Identifiable Information (PII) such as full names, email addresses, and phone numbers where not strictly necessary for local debugging.
  - Raw canonical file contents.
- Diagnostic export tools must present the complete sanitized bundle to the user for review before transmission or export.

---

## 27. NETWORK BOUNDARIES & TOPOLOGY ISOLATION

### 27.1 Default Interface Binding Invariant `[ESTABLISHED]`
Every network-listening daemon, service, or API server built under this ecosystem MUST bind by default to **localhost (`127.0.0.1` or `::1`)**.
- Binding to `0.0.0.0` (all network interfaces) by default is **STRICTLY PROHIBITED**.
- Binding to LAN interfaces (`192.168.x.x`, `10.x.x.x`) or exposing ports to the public network MUST be an explicit, conscious configuration choice made by the user in `config/app.json` or via command-line flags (e.g., `--host 0.0.0.0 --allow-lan`).

### 27.2 LAN Authentication & Boundary Protection `[ESTABLISHED]`
When an application is configured to listen across a private LAN or run on a NAS accessible to multiple network devices:
- The application MUST enforce mandatory authentication (e.g., session tokens, API tokens, mutual TLS, or user password authentication).
- Unauthenticated open network endpoints on a LAN are strictly forbidden unless the service is exclusively a public, read-only static discovery beacon (e.g., mDNS/SSDP).

### 27.3 Network Topology Classification `[PROPOSED / DERIVED]`
Applications SHALL enforce architectural controls corresponding to four explicit network zones:

```
[ ZONE 1: LOCALHOST (Loopback) ]
   └── Default bind: 127.0.0.1. Zero external network exposure. Trusted single-user runtime.

[ ZONE 2: PRIVATE LAN / NAS ]
   └── Explicit user bind. Accessible to household/office devices. Mandatory authentication & rate limits.

[ ZONE 3: VIRTUAL PRIVATE NETWORK (VPN / WireGuard / Tailscale) ]
   └── Authenticated overlay network. Secure encrypted transport. Validated identity tokens.

[ ZONE 4: PUBLIC INTERNET (WAN) ]
   └── Hostile perimeter. Mandatory TLS/HTTPS, reverse proxy isolation, WAF, strict CSRF/CORS.
```

---

## 28. SYSTEM RELIABILITY & RESILIENT ENGINEERING

### 28.1 The Deterministic Core Doctrine `[ESTABLISHED]`
To guarantee system stability, the core business engine of the application must be completely deterministic:
- Business rules, state machine transitions, financial calculations, permission checks, entity validations, data migrations, and reconciliation logic MUST produce identical outputs given identical inputs every single time.
- Randomness, probabilistic AI judgments, and wall-clock time dependencies must be isolated and passed into the deterministic core as explicit, testable parameters.

### 28.2 Idempotency and Retry Safety `[ESTABLISHED]`
Any operation that can be triggered by an autonomous agent, background worker, or network sync worker MUST be **idempotent**:
- Mutations must accept or generate a unique **Idempotency Key** (UUID or cryptographic intent hash).
- If an agent or network retry issues the identical command with the same idempotency key, the application MUST detect the duplication, return the result of the original execution, and refrain from applying duplicate mutations or generating duplicate audit events.
- Retries must never accidentally bill twice, create duplicate tasks, or append duplicate notes.

### 28.3 Actionable Error Handling & No Silent Failures `[ESTABLISHED]`
- Catching exceptions and silently ignoring them (`catch (e) {}` or `except: pass`) is **STRICTLY PROHIBITED**.
- Every failure MUST be:
  1. **Surfaced:** Propagated to the initiating actor (user or agent) with actionable details explaining what failed and how to remediate it.
  2. **Logged:** Recorded in structured operational logs with stack trace and correlation context.
  3. **Attributable:** Linked to the specific request and actor that caused it.
- **Fail-Safe Defaults:** If an error occurs during a multi-step operation, the application must abort cleanly, roll back partial state, and leave canonical storage in a valid, uncorrupted state.

---

## 29. CONCURRENCY CONTROL & MULTI-WORKER SAFETY

### 29.1 Multi-Process and Multi-Agent Concurrency Hazards `[ESTABLISHED]`
Applications must be designed under the assumption that multiple processes, threads, browser tabs, or autonomous agents MAY attempt to access and mutate the same data concurrently:
- Two background workers running simultaneous imports.
- A human user editing an entity in the GUI while an AI agent modifies the same entity via a tool call.
- Two desktop clients mounted to the same NAS network share executing simultaneous writes.

### 29.2 Concurrency Safeguards & Locking Architecture `[ESTABLISHED]`
Applications MUST employ robust concurrency coordination mechanisms:
- **Optimistic Concurrency Control (OCC):** Every canonical entity must maintain a monotonic sequence version number (`version: 4`). When submitting an update, the command must provide `expected_version: 4`. If the storage record has advanced to `version: 5`, the mutation MUST be rejected with a `CONCURRENCY_CONFLICT` error, forcing the caller to re-read and re-evaluate.
- **Advisory and Physical Database Locks:** When using relational engines (SQLite, Postgres), write transactions must obtain exclusive or immediate write locks within bounded timeouts (e.g., `PRAGMA busy_timeout = 5000;`).
- **Distributed NAS Coordination:** For direct file storage on network shares, rely on atomic rename operations and timestamped lockfile leases with automated heartbeat renewal to prevent deadlocks from crashed clients.

---

## 30. CRASH SAFETY, ATOMICITY, & DATA PROTECTION

### 30.1 Sudden Power Loss & Interruption Invariant `[ESTABLISHED]`
An application MUST be architected to withstand sudden, unannounced termination at any millisecond of execution:
- Pulling the power plug from the wall.
- OS kernel panics or blue-screen crashes.
- Sudden network severance to a NAS volume.
- Process termination via `SIGKILL` (`kill -9`).

Under none of these conditions may canonical data on disk be left in a corrupted, half-written, or permanently unreadable state.

### 30.2 Transactional Integrity and Multi-Step Operations `[ESTABLISHED]`
- Operations that modify multiple files, multiple tables, or multiple records MUST execute within an **atomic transaction boundary**.
- Either ALL modifications succeed completely and atomically commit to media, or the entire operation rolls back, leaving canonical storage 100% identical to its pre-operation state.
- Half-mutated systems are an architectural failure.
- When atomic multi-file operations are required without a relational database, the application must utilize a **Write-Ahead Intent Journal** (`/data/.journal`) that records pending operations before execution, allowing recovery on startup.

---

## 31. SCHEMA & DATA EVOLUTION / MIGRATIONS

### 31.1 Non-Destructive Schema Migration Mandate `[ESTABLISHED]`
Application software updates MUST NEVER casually destroy, alter without backup, or corrupt existing user data.
- Migrations MUST be explicit, versioned, strictly sequential, and testable.
- Every migration must have:
  1. A clear `version_number` and descriptive name (e.g., `0014_add_task_priority_index.sql`).
  2. An idempotent `up()` migration routine.
  3. A verified, non-destructive fallback or `down()` routine where technically feasible.
  4. Pre-migration integrity checks.

### 31.2 Pre-Migration Safety Snapshot `[ESTABLISHED]`
Before executing any structural schema migration or major data transformation:
- The application MUST automatically verify that storage media has sufficient free space.
- The application MUST take an immediate, local pre-migration snapshot or backup of the canonical database/files.
- If the migration script encounters an unhandled exception or constraint failure, the transaction must roll back, the pre-migration snapshot must be restored, and the application must refuse to start until the migration is remediated.

### 31.3 Backward and Forward Compatibility Discipline `[PROPOSED / DERIVED]`
- Storage formats SHOULD practice the **Robustness Principle (Postel's Law)**: Be conservative in what you write, liberal in what you accept.
- New application versions reading older data files must migrate smoothly.
- Older application versions reading newer data files should gracefully ignore unknown fields rather than crashing or truncating new data.

---

## 32. CONFIGURATION MANAGEMENT & ENVIRONMENT INDEPENDENCE

### 32.1 Separation of Configuration from Code `[ESTABLISHED]`
Hardcoding runtime configuration settings into application code is **STRICTLY PROHIBITED**.
- Applications must operate identically across development, staging, testing, production, and NAS server environments simply by changing configuration values.

### 32.2 Strict Configuration Precedence Hierarchy `[PROPOSED / DERIVED]`
Applications SHALL resolve configuration parameters using a deterministic precedence hierarchy (highest priority overrides lowest):

```
1. CLI Arguments & Flags (Highest Precedence)      --data-dir=/mnt/nas/data
2. Environment Variables                          APP_DATA_DIR=/mnt/nas/data
3. Host / Deployment Config File                  config/deployment.json
4. User Preference Config File                    config/user.json
5. Built-in Application Defaults (Lowest)         { "dataDir": "./data" }
```

### 32.3 Machine Independence & Dynamic Path Discovery `[ESTABLISHED]`
The application MUST NOT assume that the username, home directory, drive letters, or network paths of the host machine match any hardcoded developer assumptions. All paths must be dynamically constructed via standard OS runtime discovery functions.

---

## 33. OBSERVABILITY, LOGGING, DIAGNOSTICS, & HEALTH TELEMETRY

### 33.1 The Diagnostic Observability Baseline `[ESTABLISHED]`
Every running application, background daemon, and headless service MUST expose sufficient observability to diagnose failures, monitor performance, and verify state without requiring a live debugger:
- **Structured Operational Logs:** Logs must be formatted in structured JSON or clean, machine-parseable key-value lines containing timestamp, log level (`DEBUG`, `INFO`, `WARN`, `ERROR`), module/feature name, message, and error details.
- **Correlation IDs:** Every incoming user request, tool invocation, or background job must be assigned a unique `correlation_id` propagated through all sub-routines and logged across all features.
- **Log Rotation:** Diagnostic logs stored in `/logs` must be automatically rotated by size (e.g., max 10MB per file) and count (e.g., retain 5 files) to prevent exhausting host disk space.

### 33.2 Health Check Probes `[ESTABLISHED]`
Deployable applications and services MUST provide a reliable, lightweight health check endpoint or CLI command (e.g., `app-cli health` or `GET /health`):
- **Health Check Scope:**
  - Verify process execution and responsiveness.
  - Verify canonical storage mount availability and writeability.
  - Verify database connection and schema version match.
  - Verify background worker execution status.
- **Health Check Safety:** Health check probes MUST be lightweight and read-only. They must NEVER perform expensive table scans, execute migrations, or mutate state.

---

## 34. COMPREHENSIVE TESTING STRATEGY

### 34.1 The Pragmatic Testing Pyramid `[ESTABLISHED]`
Applications MUST maintain an automated test suite structured to ensure system correctness, invariant enforcement, and regression prevention:

```
          / \
         /   \         E2E / Workflow Tests (Top - Focused on critical user journeys)
        /-----\
       /       \       AI Tool & Capability Contract Tests (Verify schemas, limits)
      /---------\
     /           \     Integration & Persistence Tests (Real DB, NAS mount, Atomic I/O)
    /-------------\
   /               \   Feature & Domain Invariant Tests (Pure business rules, state logic)
  /-----------------\
```

### 34.2 Critical Mandatory Test Categories `[ESTABLISHED]`
Every application MUST include automated tests covering:
1. **Domain Invariant Tests:** Verifying that entities reject invalid states, forbidden transitions, and malformed inputs.
2. **Persistence & Atomic Write Tests:** Verifying that file replacement is atomic, temporary files are cleaned up, and corrupted writes do not overwrite valid state.
3. **AI Tool Contract Tests:** Verifying that every AI tool schema accurately validates inputs, enforces permissions, produces structured return envelopes, and handles failures gracefully.
4. **Audit Trail Verification Tests:** Verifying that authorized mutations generate complete, compliant audit events and that rollbacks generate compensating events.
5. **Recovery & Backup/Restore Tests:** Verifying that creating a backup and restoring it into a clean environment reconstructs canonical state 100%.
6. **Cross-Platform & NAS Emulation Tests:** Verifying path handling, line endings, and network latency/disconnect behavior.

---

## 35. UNIVERSAL INVARIANT VERIFICATION & TEST SUITES

### 35.1 Automated Universal Invariant Checklist `[ESTABLISHED]`
To guarantee compliance with this constitution across the entire ecosystem, applications SHOULD integrate a standardized **Universal Invariant Test Suite** executed during continuous integration. This suite validates:

- [ ] **Feature Modularity:** Verify that no feature package imports private internal classes from another feature package.
- [ ] **Code/Data Separation:** Verify that the application binary directory contains zero mutable user data files.
- [ ] **No Raw Write Tools:** Verify that no AI tool schema accepts raw SQL strings or raw arbitrary file paths.
- [ ] **Audit Trail Generation:** Verify that invoking any mutating domain command results in an appended audit record.
- [ ] **Drift Detection:** Verify that externally modifying a canonical file causes the drift detection pipeline to flag the change.
- [ ] **Derived State Rebuildability:** Delete the entire `/derived` directory and verify that the rebuild command reconstructs all search and cache indexes successfully.
- [ ] **Zero Hardcoded Paths:** Run static analysis scanning all source files for hardcoded absolute paths (e.g., `C:\`, `/home/`).
- [ ] **Secret Hygiene:** Scan the entire repository for accidentally committed API keys, tokens, or private credentials.

---

## 36. DEPLOYMENT, SERVICE PACKAGING, & CONTAINERIZATION

### 36.1 Deployment Agnosticism `[ESTABLISHED]`
Applications built under this ecosystem must support flexible, zero-friction deployment across multiple environments:
- **Native Host Deployment:** Running directly on the bare operating system as a native binary, background daemon (systemd, launchd, Windows Service), or desktop executable.
- **Containerized Deployment (Docker / Podman / OCI):** Packaged into clean, minimal, non-root OCI container images targeting Linux x86_64 and ARM64.
- **Private NAS Appliance Deployment:** Configured with clean volume mount mappings for Synology Container Manager, TrueNAS Apps, Unraid templates, or Docker Compose.

### 36.2 Startup Safety & Pre-Flight Checks `[ESTABLISHED]`
On startup, every application service MUST execute a deterministic pre-flight safety sequence before opening network ports or accepting user requests:
1. **Verify Canonical Storage Mounts:** Confirm that the configured canonical data directory exists, is mounted, and is writable.
2. **Schema & Version Verification:** Check that the current storage schema version matches the application's compiled version. If un-migrated schemas are detected, initiate the safe migration pipeline or halt with a descriptive error.
3. **Lockfile & Instance Verification:** Detect whether another instance is already running on the same data directory. Abort cleanly if concurrent execution poses a corruption hazard.
4. **Integrity Manifest Verification:** Conduct a fast startup verification of critical manifests and journals.

### 36.3 Graceful Shutdown Handshakes `[ESTABLISHED]`
When receiving a termination signal (`SIGINT`, `SIGTERM`, Windows Service Stop):
- The application MUST NOT abort instantly during active I/O.
- The application MUST initiate a graceful shutdown sequence:
  1. Stop accepting new incoming requests, tool calls, and background jobs.
  2. Complete active write operations and wait for ongoing atomic renames to finalize.
  3. Flush all in-memory buffers and WAL journals to persistent media.
  4. Safely release all advisory file locks and database connections.
  5. Close all network sockets and exit cleanly with status code `0`.

---

## 37. ARCHITECTURE DOCUMENTATION & LIVING CONTRACTS

### 37.1 The Living Documentation Imperative `[ESTABLISHED]`
Every application MUST maintain clear, accurate, and living architectural documentation at the root of its repository (`ARCHITECTURE.md` or within the root `README.md`).
- Documentation MUST describe the system as it actually exists, not as an aspirational, idealized design.
- The documentation must be sufficiently complete, precise, and structured that either a new human maintainer or an autonomous AI coding agent can read it and immediately understand:
  1. Where canonical data lives and how it is structured.
  2. The boundary and responsibilities of every feature module.
  3. All available mutation pathways and authorized AI tools.
  4. The backup, verification, and restoration procedures.
  5. The schema migration and disaster-recovery protocols.

### 37.2 Machine-Readable Interface Contracts `[ESTABLISHED]`
Wherever external interfaces exist (AI tool definitions, local HTTP/RPC endpoints, CLI command flags, data export schemas):
- The application MUST maintain formal, machine-readable contracts (JSON Schema, OpenAPI 3.1, or Protobuf).
- Generating machine-readable schemas directly from strongly-typed code constructs (e.g., Zod, Pydantic, Rust structs) is the **RECOMMENDED PRACTICE** to guarantee synchronization between documentation and runtime behavior.

---

## 38. EXCEPTION GOVERNANCE & DEVIATION PROCESS

### 38.1 The Strict Justification Policy `[ESTABLISHED]`
The universal rules in this constitution represent foundational engineering invariants. However, in rare circumstances, specific domain realities, hardware limitations, or regulatory mandates may make a rule technically impossible or counterproductive.
- A project MAY NOT unilaterally disregard a universal rule.
- A project MAY NOT claim an exception simply because complying with an invariant requires additional development effort, discipline, or architectural refactoring.

### 38.2 The Six Mandatory Criteria for Architectural Exceptions `[ESTABLISHED]`
To obtain a valid exception, the project maintainer MUST file a formal `EXCEPTION_RECORD.md` document at the project root answering all six mandatory criteria:

1. **Exact Rule Identification:** State the exact section, subsection, and invariant title of this constitution being bypassed (e.g., *Section 8.1: Offline Autonomy & Zero-Cloud Guarantee*).
2. **Technical Impossibility Justification:** Provide a rigorous technical explanation of why the rule cannot reasonably apply to this specific domain (e.g., *This application is a live multi-party video conferencing relay whose sole function is real-time cloud packet distribution*).
3. **Hazard & Risk Analysis:** Detail the precise architectural, safety, data loss, security, or portability risks introduced by this deviation.
4. **Compensating Engineering Safeguards:** Document the specific technical mitigations implemented to neutralize the risks identified in Criterion 3.
5. **Scope & Perimeter Confinement:** Explicitly delineate the boundary of the exception. The exception must be strictly confined to the minimal necessary sub-component and must not bleed into unrelated features.
6. **Temporal Lifecycle (Temporary vs. Permanent):** State whether the exception is temporary (with an explicit sunset date and remediation plan) or permanent.

---

## 39. SUBSTANTIALLY EXPANDED PROHIBITED PATTERNS & ANTI-PATTERNS CATALOG

To eliminate ambiguity, this section catalogs prohibited engineering anti-patterns and structural red flags. Any presence of these patterns constitutes an architectural failure.

### 39.1 Data & Storage Anti-Patterns `[ESTABLISHED]`
1. **Direct In-Place File Overwrites:** Overwriting active canonical files without using the atomic temp-write-and-rename protocol.
2. **Git as a User Data Store:** Tracking user-owned canonical documents, personal databases, media assets, or logs in a Git source control repository.
3. **Caches as Canonical State:** Storing user information exclusively in an ephemeral cache (e.g., Redis, in-memory Map, browser LocalStorage) without immediate write-through to durable canonical storage.
4. **Vector Store Monoculture:** Treating vector embeddings or vector databases as the sole persistent copy of user data.
5. **Undocumented Binary Black Boxes:** Storing critical user data in obscure, proprietary, undocumented binary file formats without an automated export mechanism.
6. **Silent Data Loss on Conflict:** Overwriting modified files during sync or concurrent edits without creating conflicted copies or flagging drift.
7. **Disposable Code/Data Entanglement:** Locating user data inside `/src`, `/dist`, `/node_modules`, `/app`, or inside disposable container layers.

### 39.2 AI & Automation Anti-Patterns `[ESTABLISHED]`
8. **Unrestricted SQL / Shell Tools for AI:** Exposing tools to an AI agent that accept arbitrary SQL statements, arbitrary shell commands, or arbitrary file system paths.
9. **Business Rules Living Only in Prompts:** Attempting to enforce core domain validation, permissions, or calculations through system prompts rather than deterministic code.
10. **Silent AI State Escalation:** Treating probabilistic AI outputs, extracted tags, or auto-summaries as verified ground truth without distinct provenance tagging.
11. **Unbounded Recursive AI Destruction:** Equipping an AI agent with unconstrained recursive deletion, bulk purging, or table-dropping capabilities.
12. **AI Provider Lock-In:** Scattering vendor-specific AI client calls (e.g., raw OpenAI SDK methods) throughout UI components or business feature handlers.
13. **Unchecked Agent Retries:** Allowing an automated AI workflow to retry failed mutating actions without idempotency keys, resulting in duplicated real-world operations.

### 39.3 Architectural & Modularity Anti-Patterns `[ESTABLISHED]`
14. **Giant Horizontal Layer Dumping Grounds:** Partitioning an entire application into global `/controllers`, `/services`, `/models`, `/views`, and `/repositories` directories rather than modular feature packages.
15. **The "Utils" Black Hole:** Accumulating orphaned, domain-entangled helper functions inside a sprawling `/utils` or `/common` directory.
16. **Cargo-Cult Microservices:** Fragmenting a local application into multiple distributed microservices, Docker networks, and message brokers without demonstrating an operational necessity.
17. **Circular Feature Couplings:** Creating bidirectional or circular imports between feature modules.
18. **Hidden-Button Security:** Relying on disabled or hidden UI buttons as the sole enforcement mechanism for authorization and validation.

### 39.4 Portability & Deployment Anti-Patterns `[ESTABLISHED]`
19. **Hardcoded Machine Absolute Paths:** Hardcoding developer machine paths (`C:\Users\dev\...`, `/home/dev/...`) into application code, configuration files, or database entries.
20. **Docker Confused with NAS Compatibility:** Assuming that wrapping an application in a Docker container makes it safe for high-latency, imperfectly-locked SMB/NFS network shares.
21. **Single-Process Concurrency Assumption:** Assuming no other process, thread, tab, or client will ever touch the database, ignoring locking and optimistic concurrency.
22. **Unpinned Third-Party Dependencies:** Relying on unpinned, floating package versions (`*` or `latest`) that allow upstream supply chain updates to break production builds.
23. **Plaintext Secrets in Code:** Committing API keys, bearer tokens, or database passwords into source code repositories or unencrypted config files.

### 39.5 Operational & Audit Anti-Patterns `[ESTABLISHED]`
24. **Silent Exception Swallowing:** Writing empty `catch` or `except` blocks that hide underlying I/O, database, or validation failures.
25. **Rewritable Audit Logs:** Storing audit events in mutable database rows or plain files that can be updated, modified, or truncated in-place.
26. **Unverified Backups:** Generating backup archives that have never been subjected to automated or manual restoration testing.
27. **Migrations Without Pre-Snapshots:** Running destructive database migrations without taking an immediate local backup and verifying available disk space.
28. **Hostile Network Default Binds:** Binding web servers, APIs, or RPC daemons to `0.0.0.0` by default instead of `127.0.0.1`.
29. **Unbounded Operational Log Growth:** Allowing log files to accumulate indefinitely without rotation, size caps, or disk pressure monitoring.
30. **Undocumented Data Authority:** Leaving multiple competing data stores in an application without explicitly documenting which store holds canonical truth.

---

## 40. DERIVED & PROPOSED RULES REQUIRING REVIEW

The following rules represent logical extensions, derived safeguards, and formal engineering best practices formulated to fulfill the core established invariants. They are explicitly tagged `[PROPOSED / DERIVED]` for governance board review:

1. **`[PROPOSED / DERIVED]` Standardized Storage Zone Layout (Section 6.2):** Standardizing the physical directory structure into `/app`, `/data`, `/config`, `/derived`, `/audit`, `/cache`, `/logs`, `/backups`, and `/exports`.
2. **`[PROPOSED / DERIVED]` Inter-Feature Communication Constraints (Section 5.5):** Requiring inter-feature communication to traverse strictly typed Public Application Services, In-Process Domain Events, or Command Dispatchers.
3. **`[PROPOSED / DERIVED]` Safe NAS I/O Design Patterns (Section 10.4):** Mandating client-server architecture for heavy relational databases over network shares, or using partitioned content-addressed document chunks.
4. **`[PROPOSED / DERIVED]` Dry-Run Preview Envelope Schema (Section 13.3):** Requiring Tier 3, 4, and 5 AI tools to implement a formal dry-run mode returning affected entities, reversibility flags, and planned audit events.
5. **`[PROPOSED / DERIVED]` Network Zone Classification (Section 27.3):** Classifying network topology into 4 discrete security zones (Loopback, Private LAN, VPN, Public WAN).
6. **`[PROPOSED / DERIVED]` Configuration Precedence Order (Section 32.2):** Formalizing the 5-tier configuration resolution precedence (CLI > Env Vars > Host Config > User Config > Defaults).
7. **`[PROPOSED / DERIVED]` Backward/Forward Compatibility Discipline (Section 31.3):** Enforcing Postel's Law across all schema migrations and serialization models.
8. **`[PROPOSED / DERIVED]` Backup Manifest Cryptographic Checksums (Section 20.3):** Requiring internal SHA-256 manifests and automated restore verification commands for all backup bundles.

---

## 41. OPEN QUESTIONS & ARCHITECTURAL AMBIGUITIES

The following architectural questions remain unresolved as universal requirements and are subject to ongoing deliberation:

1. **Mandatory Encryption-at-Rest for All Local Canonical Data?**
   - *Tension:* Transparent local files (Markdown, JSON) allow straightforward user inspection, scriptability, and recovery via standard OS tools. Enforcing universal encryption-at-rest introduces key management complexity, risk of catastrophic unrecoverable data loss from forgotten passphrases, and hinders third-party editor interoperability.
   - *Status:* Currently classified as `[CONDITIONAL]` based on domain privacy requirements.

2. **Multi-User vs. Single-User Sovereignty Baseline?**
   - *Tension:* Should all apps inherently support multi-user role-based access control (RBAC), or does assuming single-user sovereignty allow significantly simpler, more durable local-first architectures?
   - *Status:* Single-user local sovereignty is the default; multi-user RBAC is `[CONDITIONAL]` upon domain requirements.

3. **Mandatory Event Sourcing for All Canonical State?**
   - *Tension:* Event sourcing guarantees perfect auditability and time-travel debugging. However, it imposes immense structural complexity, snapshot management overhead, and high storage demands on simple local tools.
   - *Status:* Append-only change auditing is MANDATORY; complete event sourcing of state is an optional implementation choice.

4. **Purely Local Apps Requiring Local Authentication?**
   - *Tension:* If an application is strictly a desktop GUI running on a single-user laptop bound to `127.0.0.1`, does forcing a password/login screen add meaningful security or merely useless user friction?
   - *Status:* Localhost-only desktop apps may omit authentication; LAN-exposed services MUST require authentication.

5. **Universal SQLite vs. Universal Flat-File Document Formats?**
   - *Tension:* SQLite delivers rock-solid ACID transactions, crash safety, and relational power, but is binary. Flat files (Markdown/JSON) are human-readable in any text editor, but suffer from race conditions, difficult indexing, and lack of transaction atomicity.
   - *Status:* Both are permitted; SQLite with WAL is recommended for relational data; Atomic temp-write protocols are mandatory for flat files.

---

## 42. ADVERSARIAL REVIEW TARGETS & VULNERABILITY PROBES

This section provides adversarial challenges, edge cases, and stress tests designed to rigorously probe the validity of this constitution. Future architectural reviewers should attack these targets:

### 42.1 Probing Modularity & Feature Architecture
- *Probe:* Does the strict prohibition against horizontal layers (`/controllers`, `/services`) impose unnecessary boilerplate and structural friction on ultra-minimal single-purpose CLI utilities?
- *Probe:* At what exact line-count threshold does a monolithic single-file script need to be refactored into a feature-first modular structure?
- *Probe:* When two features have deeply intertwined entities (e.g., `Billing` and `UserAccount`), does forbidding cross-feature imports force unnecessary artificial abstraction layers?

### 42.2 Probing NAS & Storage Guarantees
- *Probe:* Is it genuinely possible to guarantee atomic file replacement over poorly implemented SMB implementations without kernel-level driver cooperation?
- *Probe:* What happens when a user mounts a NAS share over an unstable WiFi connection with a 5-second latency spike during a multi-file journal write?
- *Probe:* If an application writes to a NAS share mounted concurrently by 10 workstations without a central server process, can optimistic concurrency completely eliminate race conditions?

### 42.3 Probing the Authorized Mutation & Audit Model
- *Probe:* Will an append-only audit trail stored on disk eventually exhaust available storage on resource-constrained devices (e.g., Raspberry Pi, embedded NAS) after millions of micro-mutations?
- *Probe:* Does storing complete pre-state and post-state deltas in audit records inadvertently violate privacy regulations (e.g., GDPR "Right to be Forgotten") when a user requests deletion of sensitive personal data?
- *Probe:* If an external side effect (e.g., an outbound webhook or SMS) has already occurred, does recording a compensating reversal event truly achieve "recovery"?

### 42.4 Probing AI Tools & Autonomy
- *Probe:* Does requiring mandatory human confirmation for Tier 4 destructive tools completely destroy the utility of fully autonomous overnight AI batch workers?
- *Probe:* If an AI model hallucinates a valid, schema-compliant parameter that happens to satisfy all domain invariants but represents an insane user intent, does deterministic validation protect the user?
- *Probe:* Does enforcing rigid tool schemas prevent multi-modal or emerging agentic architectures from leveraging dynamic tool composition?

### 42.5 Probing External Drift Detection
- *Probe:* If a user uses an external editor to edit 50,000 Markdown files simultaneously via a global find-and-replace, will the drift detection pipeline overwhelm CPU and I/O with 50,000 reconciliation workflows?
- *Probe:* How does the system distinguish between a benign external edit made by the sovereign user and a malicious unauthorized file modification by local malware?

---

## 43. NON-UNIVERSALIZED TECHNOLOGIES & IMPLEMENTATION FREEDOM

To prevent harmful over-standardization and dogmatism, this constitution explicitly affirms that the following technology choices **ARE NOT UNIVERSALIZED**:

- **Programming Languages:** Developers are completely free to choose Rust, TypeScript/Node, Go, Python, Swift, C#, C++, or other languages based on performance, ecosystem, and domain fit.
- **UI Frameworks:** React, Vue, Svelte, Qt, SwiftUI, Slint, Flutter, native web standards, or terminal TUIs are equally valid presentation technologies.
- **Database & Persistence Engines:** SQLite, DuckDB, PostgreSQL, SurrealDB, RocksDB, or flat-file document stores may be utilized as appropriate.
- **ORM & Query Libraries:** Prisma, Drizzle, SQLAlchemy, Diesel, sqlx, or raw SQL drivers are implementation choices.
- **Web & RPC Frameworks:** Express, Fastify, Axum, Actix, Gin, FastAPI, gRPC, or tRPC are implementation choices.
- **Package Managers & Toolchains:** Cargo, pnpm, npm, pip, uv, poetry, or go modules are implementation choices.
- **Internal Folder Naming:** While feature-first modular organization is mandatory, the specific sub-folder nomenclature (e.g., `domain/` vs `core/`, `adapters/` vs `infra/`) is flexible.

What is universal is **safety, user data sovereignty, crash resilience, auditability, bounded AI capability, cross-platform portability, and architectural integrity**.

---

## 44. GENERATION BOUNDARY ATTESTATION

### 44.1 Sources of Authority Used
This document was formulated, synthesized, and constructed utilizing strictly:
1. The explicit universal instructions, system invariants, and architectural constraints provided in the root execution directive.
2. Foundational software engineering principles governing user-sovereign systems, local-first computing, distributed consensus, crash safety, and agentic capability security.
3. Logical deductions and engineering safeguards derived systematically from those established directives.

### 44.2 Absolute Directory Boundary Attestation
**I HEREBY ATTEST UNDER COMPLETE SYSTEM INTEGRITY:**
- **Zero project directories were entered, opened, traversed, or inspected during this run.**
- **Zero project files, code manifests, configuration files, Git repositories, databases, or documentation inside any child folder were read or queried.**
- **Zero commands (`cd`, `ls -R`, `dir /s`, `grep`, `find`) were executed against any project container.**
- **Every project directory residing within this root workspace was treated as an inviolable, sealed container.**
- **This constitution represents an authoritative master standard derived entirely without inspecting or biasing against existing project-level implementations.**

---
*End of Master Constitution — File: `UNIVERSL RULES FOR ALL APPS.md`*
