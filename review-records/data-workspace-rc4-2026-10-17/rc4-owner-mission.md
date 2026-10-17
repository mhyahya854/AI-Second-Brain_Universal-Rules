# GPT-6 ASTRA — UNIVERSAL RULES RC4: DATA WORKSPACE, DUAL-JSON RECOVERY, AND FOLDER ARCHITECTURE INTEGRATION

## 0. YOUR ROLE AND AUTHORITY

You are GPT-6 Astra, acting as principal constitutional engineer, software architect, data-integrity specialist, filesystem architect, technical researcher, and integration coordinator.

Use the highest reasonably available reasoning capability.

Where supported, delegate independent technical investigations and adversarial reviews to separately tasked agents.

Your mission is to update the owner's existing Universal Rules constitution by incorporating the **new decisions provided below**.

These decisions were developed after the previous rc3 integration.

This is an **authorized repository-editing mission**, not a request for theoretical recommendations.

You must inspect the repository, reconcile requirements, implement the approved constitutional changes, validate them, commit and push the resulting candidate, and report the exact outcome.

However:

- Do not implement an application.
- Do not build Menemora.
- Do not install or execute untrusted Skills.
- Do not invent unresolved architectural decisions.
- Do not rewrite the original constitution unnecessarily.
- Do not remove existing security, reliability, or recovery protections.
- Do not claim technical guarantees without evidence.
- Do not ratify the constitution on the owner's behalf.

**The owner has not yet authorized ratification.**

## 1. CURRENT GITHUB BASELINE — INDEPENDENTLY REVERIFY

Repository:

https://github.com/mhyahya854/Universal-Rules

At the time this mission was prepared, the actual GitHub state was independently checked.

Default branch: `main`

Exact HEAD:

`73b2e8adb0236af7d4e503e67f9d507148cc95b7`

Current designation:

`1.0.0-rc3 — Single-file integration candidate — NOT RATIFIED`

The entire active tracked tree consists of:

```text
MASTER_PLAN.md
```

The document contains:

- 137 unique normative rules.
- All 113 original rule IDs.
- 24 additional rules introduced during rc3.
- 44 substantive numbered sections, plus navigation.
- 201 unique explicit anchors.
- 709 resolving internal links.

The current document was previously reviewed by two procedurally independent fresh-context Red Team rounds.

Both reported zero BLOCKER, MATERIAL, and NON-BLOCKING defects.

**Those reviews apply only to rc3. They cannot certify your new rc4 changes.**

Preserve historical refs:

- `constitution/pre-ratification-working`
- `constitution/single-file-integration-2026-10-14`
- `review-history/universal-rules-convergence`
- `review-history/single-file-integration-2026-10-14`

The `work` branch was observed to be behind `main`, not ahead of it.

Before editing, reverify every relevant branch and file.

If the remote state differs from this checkpoint, investigate the difference before proceeding.

## 2. PRESERVE THE SINGLE-FILE CONSTITUTION

This remains a non-negotiable requirement.

The final active Universal Rules repository must contain exactly:

```text
Universal-Rules/
└── MASTER_PLAN.md
```

No additional tracked README, policy files, review folders, or other files on the final active branch.

The document must remain self-contained.

Preserve historical governance and review artifacts through Git history and separate historical evidence branches.

Do not rewrite, force-push, or delete historical evidence.

**The one-file restriction applies to the Universal Rules repository only.**

Future application repositories will contain the extensive folders and files prescribed inside that document.

Create a new revision/integration branch from the verified current `main`.

Do not alter the original rc3 review target.

After successful integration and required checks, publish the new candidate through an authorized non-destructive update. Do not assume permission to bypass branch protection or rewrite history.

If safe promotion is blocked, publish the integration branch and accurately report the blocker.

## 3. PRESERVE ALL EXISTING CONSTITUTIONAL RULES

The current constitution is the normative foundation.

Do not replace it with a simplified document.

Retain the existing protections concerning:

- Authorization and permissions.
- Data integrity.
- User ownership.
- Local-first functionality.
- NAS and synchronization.
- Transaction consistency.
- Recovery and backup.
- Security and privacy.
- Import/export.
- Migration and schema evolution.
- Audit and provenance.
- AI authority and trusted Skills.
- GitHub research and source reuse.
- Feature-first codebases.
- Master Plan organization.
- Strict execution phases.
- Small-model continuity.
- No fallback implementations.
- Rust/Tauri/SQLite preferences.
- Testing and verification.
- Design and accessibility.
- Review, freeze, and ratification governance.

Retain existing stable normative rule IDs where appropriate.

Add new IDs or carefully amend existing rules when genuinely necessary.

Provide an explicit coverage map showing how every requirement in this mission was integrated.

**Do not silently weaken or retire a previous obligation.**

## 4. NEW CORE POLICY — UNIVERSAL DATA WORKSPACE ARCHITECTURE

The owner has established a stronger vision of persistent application information.

The fundamental principle is:

**The information is the durable product. The application is a replaceable interface for accessing, interpreting, editing, and managing that information.**

For applications retaining user-owned information, define a discoverable, documented, independently accessible data workspace.

The owner strongly prefers a real, user-accessible folder structure.

The user must be able to understand the workspace without the original application.

A sufficiently capable small AI must be able to navigate it through bounded, well-documented interfaces.

The workspace must remain separate from disposable application installation state.

The planning AI must prioritize:

1. Human comprehension.
2. Information preservation.
3. Independent recovery.
4. Clear folder relationships.
5. Deterministic machine navigation.
6. Safe AI operations.
7. Scalability.
8. Long-term compatibility.

The AI must not substitute a hidden opaque storage system for the owner's independently accessible data-workspace requirement.

Existing technology choices such as SQLite may still be used for appropriate operational responsibilities, but they do not replace the newly required JSON recovery representations.

Apply these requirements to relevant persistent-data applications, not stateless utilities that retain no user information.

## 5. USER-SELECTED DATA LOCATION

Every applicable App Plan must define where the user's actual data lives.

The default user experience should be:

1. On first setup, the application asks the user to select or approve a persistent data-workspace location.
2. The user may select a suitable local folder, or another supported storage arrangement.
3. The application remembers the approved workspace location and stable workspace identity.
4. The application accesses that approved workspace unless the user deliberately changes it.
5. Important user information must not exist only inside disposable application installation state.

### 5.1 Missing workspace

If a configured location becomes unavailable, the application must not silently create a replacement empty workspace.

Report:

**Data location not found.**

Offer the user an understandable procedure for reconnecting the original workspace.

Verify its stable identity and contents before adoption.

### 5.2 Moving a workspace

A user may move the workspace to another folder, drive, device, NAS, or supported cloud arrangement.

The system must document and verify migration or reconnection.

Prefer relative paths within a workspace.

Maintain stable record identities independently of physical folder names.

Do not silently change the authoritative storage location.

### 5.3 Corrupted workspace

If a workspace is damaged, the application should report:

**Data integrity issue detected.**

Offer a verified recovery procedure.

The user should be able to choose an appropriate recovery destination, including the original location where safe or a separate folder.

The system must preserve recoverable damaged originals before any potentially destructive restoration.

### 5.4 Platform limitations

Research and document real operating-system behavior.

Mobile app-private storage may disappear during uninstall.

A supported preservation location must genuinely survive the relevant application-disappearance scenario, or an independently maintained recovery representation must do so.

Do not claim that every phone or cloud provider supports arbitrary permanent filesystem access.

## 6. MANDATORY DATA FOLDER ARCHITECTURE PLANNING

The owner places exceptionally high importance on folder organization.

**Folder structure is a major product-design responsibility, not an incidental coding choice.**

Every substantial persistent-data App Plan must explicitly design, explain, challenge, and validate the user-data workspace hierarchy.

A folder tree must not be approved merely because it looks organized.

For every meaningful folder/file, planning should establish:

- Purpose.
- Ownership.
- Contents.
- Format.
- Naming convention.
- Relationships.
- Dependencies.
- Whether it is authoritative, a replica, a projection, or historical evidence.
- Whether it can be rebuilt.
- How it is located.
- How a human reads it.
- How an AI reads it.
- How it is modified.
- How modifications are detected.
- How corruption is identified.
- How recovery works.
- What happens when the folder is moved.
- Applicable access controls.
- Long-term retention.

Use extensive meaningful headings and subheadings.

Do not impose arbitrary heading-count limits.

Do not create customary folders without demonstrating their need.

### 6.1 Three folder architectures

Every substantial application planning process must explicitly assess:

**A. User Data Workspace**

The durable, user-owned information structure.

**B. Master Plan**

The planning documentation structure already governed by rc3, including Languages and Data, Master Plan, Research and Decisions, Design, Reviews, Project State, and sequential phases/subphases.

**C. Codebase**

The feature-first frontend, backend, database, and shared-component structure already governed by rc3.

The planning system must validate these three distinct responsibilities and their cross-references.

Do not confuse actual user data with source-code database schemas or development artifacts.

### 6.2 Mandatory navigation and recovery simulations

For applicable data workspaces, plan and eventually verify representative scenarios:

- A human locating a specific record.
- A small AI locating a specific record.
- Understanding a folder without the application.
- Moving the entire workspace.
- Restoring a deleted original file.
- Corrupting a record-level JSON.
- Corrupting the global JSON.
- Detecting a modification made outside the application.
- Recovering after application disappearance.
- Navigating large datasets.
- NAS/cloud interruption and conflicting changes.
- Restoring to another selected location.

Distinguish design-time simulation from actual implementation testing.

## 7. SELF-DOCUMENTING WORKSPACE ENTRY POINT

The owner has approved four primary root information documents:

```text
00-START-HERE.md
01-FOLDER-GUIDE.md
02-DATA-DICTIONARY.md
catalog.json
```

These constitute the preferred entry-point pattern for a substantial filesystem-backed user workspace.

Also introduce:

```text
master-data.json
```

as the complete global JSON recovery representation.

Define each responsibility.

### 7.1 00-START-HERE.md

Plain-English explanation of the workspace.

It must explain where to begin, what the major folders mean, how to find information, and what to do if the original application no longer exists.

Accessible to a non-programmer.

### 7.2 01-FOLDER-GUIDE.md

Complete documented directory architecture.

Describe folder purposes, relationships, identity, navigation, and examples.

### 7.3 02-DATA-DICTIONARY.md

Explain actual data formats, fields, relationships, identifiers, provenance, timestamps, versioning, and recovery concepts.

### 7.4 catalog.json

A validated, navigable catalog of workspace records and their current logical locations.

It should help bounded machine retrieval and avoid unnecessary full filesystem scans.

Its authority, update process, and reconstruction procedure must be explicit.

### 7.5 master-data.json

The required complete global JSON recovery representation.

Its full reconstruction contract is defined below.

Do not collapse it into a list of hashes or pointers.

These names are the preferred human-facing blueprint. Any technically necessary physical adaptation must be explicitly mapped and must preserve the same user-facing discovery and recovery outcome.

## 8. MENEMORA — APPROVED ILLUSTRATIVE WORKSPACE BLUEPRINT

The owner used Menemora, a voice recording and transcription application, to refine the design.

Preserve this example to illustrate the architecture without forcing Menemora's specific features onto unrelated applications.

```text
Menemora/
│
├── 00-START-HERE.md
├── 01-FOLDER-GUIDE.md
├── 02-DATA-DICTIONARY.md
├── catalog.json
├── master-data.json
│
├── Recordings/
│   └── 2026/
│       └── October/
│           └── Interview_A7F2/
│               ├── recording.json
│               ├── recording.m4a
│               ├── transcript.md
│               ├── Notes/
│               │   └── notes.md
│               └── History/
│                   └── changes.json
│
└── Settings/
    ├── settings.json
    │
    ├── File-Paths/
    │   └── file-paths.json
    │
    ├── Exports/
    │
    └── System/
        ├── system.json
        │
        ├── Search-Index/
        │   └── search-index.json
        │
        ├── Integrity/
        │   └── integrity-manifest.json
        │
        ├── Logs/
        │   └── operations-001.json
        │
        └── Recovery/
            ├── recovery-state.json
            ├── Transactions/
            └── Verified-History/
```

This is an organizational blueprint, not an implemented filesystem.

### 8.1 Individual recording integrity

Every recording's associated information must be discoverable from that recording's folder.

Do not place all recording notes into an unrelated global Notes folder.

Original recordings, transcripts where applicable, notes, metadata, and history should have clearly documented relationships.

### 8.2 Settings hierarchy

The owner wants Settings to contain settings, file-path configuration, exports, system support, logs, indexes, integrity, and recovery-related information.

Distinguish the data-preservation responsibilities of these objects.

Do not store credentials insecurely in ordinary readable JSON.

### 8.3 Optional Collections

Collections are an optional Menemora feature.

They may be enabled or disabled through Settings.

Disabling Collections must not automatically erase the user's existing collection information.

Do not force a permanent root-level Collections folder merely because collections can exist.

The actual App Plan should determine whether collections use metadata, references, or justified folders.

Do not duplicate original media unnecessarily for organizational views.

### 8.4 Other Menemora capabilities

Transcription, transcript correction, AI summaries, audio processing, notes, and other features remain subject to Menemora's future App Plan.

This example does not automatically authorize or require every suggested feature.

## 9. UNIVERSAL LITERAL DUAL-JSON RECOVERY ARCHITECTURE

This is the most significant new policy.

The owner explicitly selected **literal full duplication**, rather than a system where the JSON documents merely refer to separately stored binary objects.

Respect that choice.

The architecture has two first-class recovery representations:

**Individual JSON records**

Each retained logical record or appropriately scoped data component has a self-contained JSON recovery representation.

**One global JSON record**

`master-data.json` contains the complete recoverable contents of the entire retained workspace.

These are complementary, first-class recovery representations.

Neither may silently diminish its required information.

### 9.1 The original files remain available

Human-readable Markdown, original audio, images, documents, and other normal files remain present and independently accessible.

The JSON system does not replace the human-readable workspace with a database-only representation.

### 9.2 Literal reconstruction

The individual JSON must contain the actual recoverable data necessary to reconstruct every retained original file within its defined scope.

The global JSON must contain the actual recoverable data necessary to reconstruct the retained workspace.

For binary objects, this may require reversible binary-to-text encoding such as Base64.

A path plus a hash is not sufficient for literal reconstruction.

A pointer to an object store is not literal full duplication.

Do not replace complete payloads with only references to content-addressed objects.

### 9.3 Two portions inside relevant JSON records

Use a well-defined JSON schema that conceptually separates:

**actual_data**

The retained original content and information needed for exact reconstruction.

**app_data**

The operational metadata and relationships needed by the application.

Define the status of information that is itself important user data even if operational in nature.

No important retained information should disappear merely because it is labeled metadata.

### 9.4 Scope of coverage

Account for applicable retained:

- Original documents and media.
- Transcripts.
- Notes.
- Metadata.
- Settings.
- File-path records.
- Relationships.
- Record identifiers.
- User edits.
- Relevant histories and logs.
- Necessary recovery information.

Derived indexes and transient processing artifacts require explicit retention and recovery contracts.

Do not silently treat an authoritative artifact as disposable.

### 9.5 JSON self-reference

Ordinary finite JSON cannot recursively include a complete exact copy of itself indefinitely.

Document a mathematically coherent serialization and reconstruction policy.

An individual JSON must be reproducible from its defined payload and schema without requiring literal recursive self-inclusion.

The global JSON must likewise be reconstructible without recursively embedding infinite copies of itself.

Historical snapshots and temporary transaction files must not recursively inflate the current global representation.

Do not use this necessary self-reference boundary as an excuse to omit ordinary retained user content.

### 9.6 No silent data diminution

The owner says the JSON must never diminish.

Interpret this as a protection against silent loss, omission, truncation, corruption, unapproved replacement, or premature deletion of information required by the retention contract.

Do not interpret it as a mathematical requirement that physical file byte counts can never decrease.

Authorized erasure, lawful retention policies, compact serialization, and deliberate migrations must remain possible.

Explain this distinction clearly.

## 10. GIT-INSPIRED CONTENT IDENTIFICATION AND VERSION HISTORY

The owner wants the microscopic actual content stored in JSON, while Git-inspired mechanisms describe:

- What changed.
- How much changed.
- When it changed.
- Which revision came before.
- Which content is unchanged.
- How to locate retained historical versions.
- Whether compared bytes match.

Incorporate Git-inspired:

- Stable revision identities.
- Cryptographic content hashes.
- Content comparisons.
- Change manifests.
- Structured differences where applicable.
- Recorded timestamps.
- Previous-version relationships.
- Immutable verified history.
- Potential chunk-level hashing for large content.
- Content identity and provenance.

### 10.1 Hashes are not backups

A cryptographic hash identifies or verifies bytes relative to an expected value.

It does not contain the information needed to reconstruct those bytes.

It does not establish when a change occurred without an associated revision record.

It does not inherently establish authorship or factual correctness.

Git stores content objects as well as identifying them through hashes.

Apply these distinctions accurately.

### 10.2 The JSON remains complete

Git-inspired revision tracking must not silently transform `master-data.json` into a references-only manifest.

Both JSON recovery layers must preserve the literal reconstruction requirements.

Hashes and diffs supplement the complete data representation.

### 10.3 Revision information

Each relevant change record should capture, where appropriate:

- Record identity.
- Previous revision.
- New revision.
- Changed fields or files.
- Measured change size.
- Recorded time and temporal context.
- Old and new hashes.
- Authorized operation identity.
- Outcome.
- Relationships to protected historical content.
- Validation status.

Do not claim that a timestamp proves who performed a change.

Do not assume a newer timestamp automatically identifies the correct version.

## 11. DUAL-JSON RECONCILIATION AND CONFLICT PROTECTION

The owner wants the global and individual JSONs continuously checked and reconciled.

Do not implement that as unrestricted mutual overwriting.

The approved high-level principles are:

1. Compare the relevant current records and revisions.
2. Detect mismatches.
3. Determine the last verified common state.
4. Examine durable operation evidence.
5. Distinguish a committed change from an incomplete update.
6. Preserve disputed versions when necessary.
7. Prevent automatic propagation of unvalidated corruption.
8. Reconcile only through an authorized, tested procedure.
9. Verify the resulting representations.
10. Record the actual outcome.

Both JSON layers are first-class recovery sources.

However, **being first-class does not mean two conflicting copies can independently declare incompatible states authoritative**.

The App Plan must define how a valid committed revision is determined.

Neither a newer timestamp nor a matching hash alone establishes legitimacy.

## 12. PROTECTED HISTORY AND BACKUPS

Two identical current copies are not enough to recover from a bad edit that has already propagated into both.

The owner explicitly wants protection from:

- AI mistakes.
- Accidental deletion.
- Incorrect transcript edits.
- Corrupted JSON.
- Synchronization errors.
- Malicious changes.
- Accidental overwrites.
- Storage failures.

The architecture therefore needs independently protected historical recovery points.

Normal application and AI editing credentials should not automatically have unrestricted deletion authority over every backup generation.

The protection design must account for failure domains, privacy, authorized erasure, and actual platform capabilities.

Historical snapshots must not recursively contain infinite historical copies of themselves.

Do not claim recovery is guaranteed if every independent copy, required key, and recovery dependency has been destroyed.

## 13. EXTERNAL MODIFICATIONS

The owner wants changes made outside the application or outside its trusted AI operations to be promptly flagged.

Examples:

- The user edits `transcript.md` using a text editor.
- Another program changes `notes.md`.
- A small AI writes directly to a data file.
- Cloud synchronization modifies a file.
- A NAS client changes a record.

Define:

- Expected content identities and revisions.
- File-change monitoring where supported.
- Hash/version verification.
- Reconciliation and rescanning.
- Detection before destructive overwrite or authoritative adoption.
- Clear user-visible discrepancy reporting.
- Safe adoption, rejection, or preservation of externally modified content.

### 13.1 Important truthfulness limitations

Not all external changes can be detected instantly.

Watchers may miss events.

The application may be stopped.

A remote cloud/NAS modification may not yet have propagated.

Hashes can identify differences but cannot prove the author of a change.

Therefore, require prompt detection where supported and mandatory integrity reconciliation at the relevant trust/commit boundaries.

### 13.2 Legitimate external edits

An external edit is not automatically malicious.

The user may deliberately edit their own files.

Preserve the external version, compare it against verified state, and provide a safe adoption procedure.

Do not silently overwrite the user's modified file simply because an older JSON exists.

Do not blindly synchronize unvalidated external changes into both JSON copies.

## 14. ONE TRUSTED ENTRY-POINT AI SKILL PER APPLICATION

Every applicable AI-accessible application should expose **one clearly named, discoverable primary Skill** that guides AI models through the application's information and supported operations.

Example:

`Menemora/SKILL.md`

The Skill should explain:

- What the application does.
- Where the workspace is located.
- Where AI should begin.
- How folders are organized.
- How to discover records.
- How to retrieve bounded information.
- How to interpret schemas and revisions.
- How to request edits.
- How to distinguish source information from instructions.
- Which operations require approval.
- How permissions are enforced.
- How to handle errors and ambiguity.
- How to verify changes.
- What must never be directly modified.
- How to report uncertain or blocked outcomes.

The primary Skill may reference other bounded internal Skills or documentation where justified.

Do not confuse one primary application entry point with a prohibition on useful subordinate expertise.

The Skill must remain separate from actual permission enforcement.

An editable file inside the user-data workspace must not grant elevated authority merely by containing instructions.

AI operations must use the approved, permission-enforced application interfaces.

The entry-point Skill does not automatically authorize direct filesystem mutation, credential access, data deletion, or production operations.

The workspace's human-readable documentation must remain usable without the Skill.

## 15. VERY SMALL AI MODEL NAVIGATION

The owner wants the workspace to be organized so clearly that even a model around **one billion parameters** can navigate it and answer appropriately scoped questions.

Treat this as a measurable engineering target, not a guarantee for every model or task.

The intended navigation path is:

```text
AI
 ↓
Trusted application Skill
 ↓
00-START-HERE.md
 ↓
Folder guide and catalog
 ↓
Bounded retrieval operation
 ↓
Relevant record and precise content
```

A small model should not need to read the entire global JSON, a massive database, or thousands of files just to retrieve one recording.

Require:

- Clear entry points.
- Stable IDs.
- Human-readable names.
- Bounded indexes and catalogs.
- Precise sub-object addressing.
- Deterministic lookup.
- Limited retrieval outputs.
- Explicit ambiguity reporting.
- Safe authorization.
- Task-specific examples.
- Documented error handling.

Define real evaluation procedures for 1B-class models where material capability claims are made.

Measure retrieval accuracy, errors, hallucinated paths, unauthorized mutations, context budget, and correct escalation.

A model's parameter count alone is not evidence of capability.

Preserve the separate existing 4B-class target for implementing applications from detailed phase contracts.

**Data navigation by a 1B model and code execution by a 4B model are distinct evaluation goals.**

## 16. NAS, CLOUD, AND MULTI-DEVICE WORKSPACES

The owner wants the data-workspace architecture to accommodate appropriate:

- Laptop-only applications.
- Phone-only applications.
- Desktop and mobile applications.
- NAS-based workspaces.
- User-selected cloud storage.
- Multiple synchronized devices.

The logical workspace should remain understandable regardless of location.

The actual storage and coordination topology must follow the App Plan.

Do not presume one physical writable filesystem works on all platforms.

Do not let multiple devices independently edit one live SQLite/WAL database on unsupported network filesystems.

Do not presume ordinary cloud-folder synchronization provides atomic updates or safe conflict resolution for enormous JSON files.

The planning process must define:

- Authoritative write coordination.
- Working copies.
- Revision identifiers.
- Synchronization boundaries.
- Offline operations.
- Conflict detection.
- Delayed updates.
- Connectivity failures.
- Permission loss.
- Verified recovery.
- Movement between storage configurations.

The user has **not yet finalized the preferred universal authoritative-copy topology**.

Do not invent that decision.

Preserve the requirement for one logical, user-owned workspace and an explicit approved synchronization architecture.

## 17. CORRUPTION AND RESTORATION BEHAVIOR

The App Plan must define recovery from:

- Original file deleted.
- Individual JSON corrupted.
- Global JSON corrupted.
- Both current JSONs corrupted.
- Current JSONs internally valid but semantically incorrect.
- Current copies disagree.
- Interrupted write.
- Insufficient disk space.
- Storage moved.
- NAS or cloud unavailable.
- External edit detected.
- AI mistakenly changes multiple records.
- Application uninstalled or abandoned.
- Required decryption key unavailable.

Distinguish:

**Missing location** from **damaged information**.

Do not silently manufacture a replacement empty library.

Do not overwrite the only surviving damaged source during recovery.

Where appropriate, preserve damaged originals and restore into an isolated location for validation.

A user should be able to choose a supported same-folder or different-folder restoration procedure with honest explanation of its consequences.

Verify restored file bytes, metadata, relationships, identifiers, and declared recovery point.

A restored file merely opening successfully is insufficient evidence of exact recovery.

## 18. AGGRESSIVE BREAK-TESTING

The owner explicitly wants applications tested aggressively until defects are found, repaired, and retested against demanding, documented acceptance standards.

The AI should not treat a successful compilation or a happy-path demonstration as sufficient proof of quality.

Require appropriate:

- Fault injection.
- Crash simulations.
- Disk-full simulations.
- Corrupted inputs.
- Truncated JSON.
- Missing original files.
- Concurrent writes.
- Interrupted commits.
- Power-loss assumptions.
- Cloud/NAS disconnection.
- Conflicting remote edits.
- AI-induced destructive mistakes.
- Large media payloads.
- Lifetime-scale datasets.
- Migration failures.
- Application-disappearance recovery.
- Small-model navigation trials.
- Memory and CPU measurements.
- Startup and search performance measurements.
- Backup and restore verification.

Use isolated fixtures and authorized test environments.

Never deliberately damage live user data for testing.

Test, repair, retest, and repeat until the documented quality baseline is met or a material unresolved limitation is accurately reported.

Do not require physically impossible infinite testing.

No theoretical recovery guarantee may be represented as demonstrated merely because a specification exists.

## 19. LITERAL DUAL-JSON SCALABILITY AND FACTUALITY

The owner deliberately retained the more demanding architecture.

Do not weaken it silently because an alternative would be easier to implement.

But evaluate its real costs honestly.

For example, 100 GB of binary originals encoded through Base64 would occupy approximately:

- 100 GB in original files.
- 133 GB in individual JSON payloads.
- 133 GB in the complete global JSON.

Approximately 366 GB total before other overhead and history.

A small content change may require producing a new complete global JSON representation.

Content hashing cannot eliminate that requirement on its own.

Git avoids full-repository rewrites by using separate immutable content objects and references. This is different from a single literal complete JSON payload.

Copy-on-write filesystems, snapshots, compression, sparse files, reflinks, streaming serialization, and other techniques may change actual storage costs under specific conditions, but must not be assumed portable or reliable without evidence.

The planning AI must evaluate:

- Capacity.
- Storage amplification.
- Temporary write space.
- Write frequency.
- Serialization time.
- Crash consistency.
- Memory usage.
- Backup growth.
- Cloud upload and transfer costs.
- NAS bandwidth.
- Mobile storage constraints.
- Concurrent access.
- Lifetime growth.

If the chosen literal architecture cannot satisfy an application's agreed workload, the AI must present the material conflict honestly to the owner.

It may not silently replace the complete JSON payloads with hashes or pointers.

## 20. DO NOT PREMATURELY DECIDE THE SAVING ALGORITHM

This is critical.

**The owner and assistant have not finished Topic 1: Saving and Version Control.**

We have agreed on:

- Complete individual JSON representations.
- One complete global JSON representation.
- Git-inspired change tracking.
- Cryptographic hashes.
- Version history.
- Protected earlier revisions.
- Safe coordination.
- Honest acknowledgement.
- No silent data diminution.
- No hidden fallback implementation.

We have NOT yet finalized:

- Whether edits are acknowledged only after both full JSON copies are committed or whether an earlier independently durable pending state is permitted.
- Exact durable staging and commit format.
- Exact write coordination protocol.
- How to update an enormous complete global JSON efficiently.
- Whether specific storage-level optimizations are universally required.
- Final device-to-NAS/cloud authority topology.
- Exact thresholds for rebuild, batching, compaction, and storage capacity.
- Universal timeout or retry budgets.
- Exact history retention policy for all apps.

Do not invent approval for these choices.

Incorporate the agreed invariants and expressly delegate the remaining technical mechanisms to the future engineering decision process, subject to user authority where required.

Where an unresolved question would materially affect the proposed universal requirements, identify it in a clearly labeled **non-normative Open Engineering Decisions** section.

Do not pretend that a future design question has already been fully resolved.

Do not use deferred engineering choices to weaken the decided literal dual-JSON obligation.

## 21. CONSTITUTIONAL RECONCILIATION

Pay special attention to existing rc3 rules including:

- `INFO-1` through `INFO-4`.
- `LIFE-1` and `LIFE-2`.
- `SURVIVE-1` and `SURVIVE-2`.
- `DATA-1` through `DATA-5`.
- `STORE-1` and `STORE-2`.
- `CON-1` and `CON-2`.
- `EDIT-1` and `EDIT-2`.
- `SYNC-1` through `SYNC-4`.
- `RECOVER-1` and `RECOVER-2`.
- `BACKUP-1` and `BACKUP-2`.
- `AUTH-1` and `AUTH-2`.
- `AI-1` through `AI-4`.
- `HERMES-1` through `HERMES-3`.
- `NOFALL-1` and `NOFALL-2`.
- `PLAN-1` and `PLAN-2`.
- `BLUEPRINT-1` through `BLUEPRINT-3`.
- `DOC-1` and `DOC-2`.
- `EXEC-1` through `EXEC-6`.
- `GOV-3` through `GOV-5`.

The existing `INFO-1` rule permits various storage representations and does not require JSON.

The new owner policy deliberately strengthens that position for retained-user-data applications.

Make the change explicitly, with correct scope and provenance.

Avoid accidental contradictions or dual interpretations.

Do not mandate meaningless data-storage machinery for stateless tools.

Do not let JSON completeness override authorized deletion, privacy obligations, or established security boundaries.

## 22. IMPLEMENTATION AND REVIEW PROCESS

### Stage 1 — Verify

Retrieve and read the actual rc3 file and historical review evidence.

Record exact refs, checksum, and initial rule inventory.

### Stage 2 — Build a requirement coverage matrix

Map every numbered requirement above against current normative rules.

Classify as:

- Already satisfied.
- Requires clarification.
- Requires refinement.
- Requires new rule.
- Contains a material conflict.
- Deferred engineering choice.

### Stage 3 — Technical research

Research material storage, Git-object, JSON, hashing, crash-consistency, filesystem, mobile-storage, NAS, and cloud facts through appropriate authoritative sources.

Do not rely on memory where exact guarantees matter.

### Stage 4 — Integrate

Edit only the appropriate parts of `MASTER_PLAN.md`.

Add necessary new sections, rules, definitions, cross-references, and examples.

Preserve original policy intent, identities, and working protections.

Use very extensive, navigable headings.

### Stage 5 — Structural validation

Check:

- One-file active tree.
- All original rule IDs.
- New rule IDs and metadata.
- Rule origin and applicability.
- Unique anchors.
- Valid internal links.
- No deleted-file dependency.
- Heading structure.
- Correct Markdown fences.
- Numbering.
- Requirement completeness.
- Absence of duplicate competing rules.
- Accurate provenance.
- Historical recovery.
- Git integrity.

### Stage 6 — Adversarial review

Run fresh Red Team review of the exact new candidate.

Include existing A–P lenses and additional attacks specifically against:

- Literal complete JSON reconstruction.
- Infinite recursive self-inclusion.
- Global JSON scalability.
- Simultaneous updates.
- Valid but incorrect JSON contents.
- Propagated AI errors.
- Protected history deletion.
- External changes.
- Cloud/NAS conflict propagation.
- Mobile uninstall.
- Unauthorized AI Skill writes.
- False corruption-recovery guarantees.
- Hash misuse.
- Personal-data retention and authorized erasure.
- No-fallback policy interactions.
- Weak-model navigation.
- User-selected storage locations.
- Partial commits and recovery after power failure.

Keep Red reviewers read-only.

Repair valid findings through the authorized Green Fix procedure and re-review changed normative bytes.

Do not claim convergence merely because previous rc3 reviews were clean.

### Stage 7 — Publish

Commit and push the result to GitHub.

Keep historical candidate refs intact.

Ensure the final active repository still has precisely one tracked file.

Verify actual remote refs and the exact final content.

If applicable review/freeze authority is insufficient for a particular step, report that boundary rather than inventing authorization.

### Stage 8 — Final report

Return one detailed final report containing:

1. Executive outcome.
2. Repository/branch status.
3. Exact final commit.
4. New document SHA-256.
5. Final file-tree confirmation.
6. Original rule preservation counts.
7. Added and modified normative rules.
8. Full requirement coverage matrix.
9. Technical research findings.
10. Contradictions reconciled.
11. Explicit deferred engineering choices.
12. Structural validation results.
13. Red Team review results.
14. Historical preservation verification.
15. Residual risks.
16. Ratification status.
17. Next action for the owner.

## 23. FINAL REQUIREMENTS

You must implement all **settled owner decisions** in this mission.

Do not broaden Menemora-specific examples into unrelated mandatory features.

Do not substitute a references-only content-addressed store for the owner's literal dual-JSON architecture.

Do not invent a finalized Topic 1 saving algorithm.

Do not discard existing rc3 protections.

Do not introduce a second constitutional file.

Do not leave accepted work only in an ephemeral environment.

Do not claim unrun tests succeeded.

Do not ratify the constitution.

**The target outcome is an updated, deeply structured, technically honest single-file Universal Rules candidate, preserving the 137-rule rc3 foundation while integrating the owner's new data-workspace and recovery architecture.**

Proceed with the authorized repository integration and return the verified GitHub result.