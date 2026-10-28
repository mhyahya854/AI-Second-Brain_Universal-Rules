<a id="s07"></a>
## 7. Data lifecycle and application replacement

*Section 7 rules across lifecycle files: [LIFE-1](#life-1), [LIFE-2](405-%20Designing%20Data%20Models%20and%20Storage.md#life-2), [LIFE-3](405-%20Designing%20Data%20Models%20and%20Storage.md#life-3).*

<a id="life-1"></a>
### 7.1. LIFE-1 — Preservation across supported replacement

**Type:** UNIVERSAL INVARIANT | **Origin:** DERIVED ENGINEERING RULE | **Applies:** installation, update, replacement, or removal with retained state

Lifecycle operations MUST honor declared preservation and deletion semantics. Retained data, user configuration, required keys, and required evidence MUST NOT be accidentally destroyed by an operation represented as preserving them. Reattachment claims MUST account for schemas, keys, permissions, formats, and required software.

<a id="s46"></a>
## 46. Mandatory Current JSON and Folder JSON; optional complete Master JSON

Every qualifying application MUST maintain per-file Current JSONs containing complete literal reconstructible bytes and verified per-folder lightweight Folder JSON manifests. Neither protection may be disabled. Synchronization of a changed Current JSON begins promptly for that file only; Folder JSON is asynchronously verified against a consistent revision boundary. The complete standalone global `master-data.json` remains independently optional under [section 53](#s53). These obligations exclude stateless utilities, do not eliminate original files, do not duplicate file payloads in folder manifests, and do not select a universal operational database.

<a id="json-1"></a>
### 46.1. JSON-1 — Complete Current JSON payloads, verified Folder JSON manifests, and optional global payload

**Type:** ECOSYSTEM POLICY | **Origin:** USER POLICY | **Applies:** mandatory live per-file Current JSON and per-folder Folder JSON for retained-data applications; independently optional global Master JSON

<a id="json-scope"></a>
#### 46.1.1. Complete logical scope and partial replicas

Each applicable retained original file MUST have its own self-contained **Current JSON** containing the actual complete reconstructible original bytes; where physical files are not the relevant unit, an App Plan MAY justify an equivalent independent persistent logical-object scope. Current JSON is mandatory and non-disableable. Each applicable folder MUST have a verified **Folder JSON** manifest of stable file identities, paths, revisions, integrity state and child-folder relationships; it MUST NOT duplicate original-file bytes or claim standalone payload reconstruction. **Only when optional Master JSON is enabled, `master-data.json` MUST independently contain the complete literal reconstructible payload of the retained global workspace at its published verified revision.** Scope inventories MUST account for every retained component without gaps, including workspace-level components outside domain records. Partial device working copies do not redefine the logical workspace or excuse mandatory Current JSON and Folder JSON or an enabled complete global representation. Current, Folder and enabled Master JSON belong **inside the primary workspace**, never only in the external backup location. No layer may claim a newer revision verified before its actual safe publication; placement/coordination follow [JSON-4](#json-4).

<a id="json-literal-payload"></a>
#### 46.1.2. Actual payloads and accessible originals

Literal full duplication is required in every mandatory Current JSON and every enabled global Master JSON: retain actual payloads, including reversible binary-to-text encoding such as Base64 where needed. Paths, hashes, object-store references, diffs, or content-addressed pointers alone MUST NOT substitute for complete payloads. Git-inspired identification supplements full contents. Original audio, images, documents, Markdown and other normal files MUST remain independently available under [WORKSPACE-1](405-%20Designing%20Data%20Models%20and%20Storage.md#workspace-1).

<a id="json-exact-bytes"></a>
#### 46.1.3. Exact original bytes and portable metadata

Current JSON and any enabled Master JSON MUST preserve exact retained original file bytes, including text encoding, line endings and binary content, and required metadata, identifiers, relationships and meaning. For user-created or imported JSON originals, parsing and reserializing can change whitespace, escaping, member order, number spelling/precision, BOM, encoding or line endings. Preserve a reversible original-byte representation separately from any parsed interpretation; canonicalization alone cannot reconstruct arbitrary original JSON bytes. JSON parse equivalence or a successfully opened restored file alone is insufficient. Define byte encoding/decoding, lengths, integrity checks, format/schema versions and safe interpretation, including binary-text alphabet, padding and invalid-input handling. Define parser duplicate-member, numeric-precision, depth, string/token-size and resource-limit behavior without silent truncation of accepted retained content. Required platform metadata not reproducible on a target MUST remain preserved in a documented representation and its restoration limits disclosed; do not claim unsupported exact native metadata restoration.

<a id="json-2"></a>
### 46.2. JSON-2 — Payload schema, coverage, privacy, and no diminution

**Type:** ECOSYSTEM POLICY | **Origin:** USER POLICY | **Applies:** mandatory per-file Current JSON, verified Folder JSON manifests, optional global Master JSON schemas, and retained-content lifecycle

<a id="json-schema"></a>
#### 46.2.1. Payload and application information

Use well-defined versioned schemas conceptually separating **`actual_data`**, retained original content and information necessary for exact reconstruction, from **`app_data`**, application metadata and relationships. Important retained information remains covered even when operational or labeled metadata. Each scope inventory MUST classify original documents/media, transcripts, notes, metadata, settings, file-path records, relationships, IDs, user edits, relevant histories/logs and necessary recovery information. Derived indexes and transient processing artifacts require explicit authority, retention and rebuild contracts; neither filename nor derived origin makes authoritative information disposable.

<a id="json-retention"></a>
#### 46.2.2. No silent loss and legitimate erasure

“No diminution” means no silent loss, omission, truncation, corruption, unapproved replacement or premature deletion of required retained information. It does **not** mean monotonically increasing physical file size. Authorized erasure, lawful retention expiry, compact serialization and deliberate validated migrations remain supported. Coverage applies to information legitimately retained at the declared recovery point; [PRIV-1](../6-%20Writing%20the%20Complete%20Master%20Plan/606-%20Documenting%20Data%20Security%20and%20Recovery.md#priv-1) and [SAFE-2](../0-%20Start%20Here%20and%20Universal%20Rules/002-%20The%20Universal%20Constitution.md#safe-2) govern deletion, minimization and conflicting obligations across originals, mandatory Current JSON and Folder JSON, optional Master JSON, histories, replicas and backups. Restoration MUST reconcile deletion decisions and MUST NOT resurrect erased payloads contrary to policy.

<a id="json-secrets"></a>
#### 46.2.3. Privacy, credentials, and recovery keys

JSON completeness MUST NOT expose credentials or bypass access boundaries. Do not store usable credentials insecurely in ordinary readable JSON. Define protected credential/key storage and independently recoverable key-access paths under [SEC-2](../9-%20Preparing%20the%20Development%20Environment/908-%20Establishing%20Permissions%20and%20Secrets.md#sec-2) and [BACKUP-1](../16-%20Maintaining%20Updating%20and%20Recovering/1606-%20Testing%20Backup%20and%20Restoration.md#backup-1). Where sensitive retained content requires encryption, complete recoverable payloads remain required in protected form; document algorithms/formats and legitimate independent access dependencies without packaging decryption secrets with public copies. A credential reference is not a substitute for retained media/document payloads. Report unrecoverability honestly if required keys are unavailable.

<a id="json-3"></a>
### 46.3. JSON-3 — Finite serialization and reconstruction boundaries

**Type:** ECOSYSTEM POLICY | **Origin:** USER POLICY | **Applies:** JSON self-reference, generated envelopes, and historical recovery packaging

<a id="json-generated-envelopes"></a>
#### 46.3.1. Finite generated-envelope reconstruction

The App Plan MUST define a mathematically finite serialization and reconstruction policy. Mandatory Current JSON and optional global Master JSON representations MUST be reproducible from their defined payload, schema and documented deterministic envelope rules without recursively embedding exact copies of themselves. Folder JSON manifests likewise MUST avoid recursive inclusion of generated envelopes. Define which recovery envelopes are reconstructed, what their byte/semantic reconstruction target is, and preserve any non-derivable retained information they carry. Exact original-file reconstruction under [JSON-1](#json-1) remains mandatory; a serialization boundary cannot discard ordinary retained user content.

<a id="json-finite-history"></a>
#### 46.3.2. Retained history and packaging boundaries

Any enabled current global representation MUST NOT recursively embed itself, unbounded historical snapshots containing themselves, or recursively nested temporary transaction machinery. Folder JSON child relationships use bounded references to separately verified child manifests rather than recursively embedding their contents. Distinguish retained user/domain history and necessary recovery information, which remain covered, from separately protected snapshot generations and reconstructible recovery packaging. Document each exclusion's reconstruction or independent retention/access contract, keys/readers and failure limits; exclude only the recursive/generated or genuinely transient packaging, not user data hidden inside it. All still-retained historical user payloads and history/log information belong in the mandatory per-file/component Current JSON and (when enabled) optional global Master JSON literal coverage inventories; a separate protected generation or history pointer alone does not satisfy that current coverage. A packaging exclusion cannot remove these payloads. Temporary staging is not an ordinary retained original, but any pending user information or operation evidence needed for the declared durable recovery point requires an explicit preservation and reconstruction contract. Historical points themselves MUST have finite, complete declared recovery scopes and accessible dependencies. Reference chains with missing content are not complete recovery payloads.

<a id="json-hash-domain"></a>
#### 46.3.3. Self-hashes and deterministic serialization

Hash domains MUST be explicit and reproducibly verifiable, including how self-generated digest fields and revision identifiers are treated. Do not presume a field can contain the digest of the entire finalized byte string including that same field. Payload-only or explicitly excluded-field domains are examples to evaluate, not a selected universal mechanism. Deterministic envelope serialization must include all necessary version/metadata inputs when exact generated-envelope bytes are promised; semantic reconstruction must be labeled separately.

This rule requires coherent finite boundaries and evidence, not a selected universal serialization, staging, commit or history algorithm. Decisions remain under [section 50.2](410-%20Reviewing%20Architecture%20Decisions.md#open-engineering).

<a id="json-4"></a>
### 46.4. JSON-4 — Current/Folder revision coordination, distributed state, and verified restoration

**Type:** ECOSYSTEM POLICY | **Origin:** USER POLICY | **Applies:** saving, synchronization, conflict resolution, and restoration of retained-data workspaces

<a id="json-commit-evidence"></a>
#### 46.4.1. Committed revision and legitimate authority

The App Plan MUST define valid committed original-data revisions and durable edit protection, how mandatory per-file Current JSONs and their Folder JSON verification evidence relate to those revisions, and—when Master JSON is enabled—how its independent complete global revision relates to the originals, catalog and recovery sources. Current JSON is a first-class recovery source. Folder JSON is a verified inventory, NOT an independent full-content recovery source. Conflicting states MUST NOT independently claim incompatible authority. A newer timestamp, matching hash, syntactically valid JSON or equal copies alone does not establish legitimacy, factual correctness or successful commit. Use enforced authority, current-state coordination and validation under [AUTH-1](../10-%20Building%20the%20Core%20and%20Backend/1007-%20Implementing%20Security%20and%20Authorization.md#auth-1), [CON-1](../10-%20Building%20the%20Core%20and%20Backend/1005-%20Implementing%20Transactions%20and%20Migrations.md#con-1), [STORE-1](../10-%20Building%20the%20Core%20and%20Backend/1004-%20Implementing%20Storage%20and%20Persistence.md#store-1), [AUDIT-2](../10-%20Building%20the%20Core%20and%20Backend/1005-%20Implementing%20Transactions%20and%20Migrations.md#audit-2) and [OUT-1](../0-%20Start%20Here%20and%20Universal%20Rules/009-%20Evidence%20and%20Truthful%20Completion.md#out-1).

<a id="json-reconciliation"></a>
#### 46.4.2. Continuous checking and evidenced reconciliation

Integrity checking and reconciliation MUST have documented schedules and trust/commit boundaries appropriate to the supported workload. Mandatory Current JSON synchronization MUST be triggered immediately for a recognized changed original file or equivalent durable object and MUST NOT routinely rewrite untouched files. An asynchronous, resource-bounded Folder JSON verifier checks the relevant original and Current JSON at a consistent revision boundary and then publishes the affected folder's verified state. An enabled global Master JSON follows its independently configured schedule. Bounded periodic reconciliation and validation at appropriate trust boundaries MUST detect missed watcher events; no constant whole-workspace rescan is required. The authorized, tested reconciliation procedure MUST compare relevant current records/revisions, detect mismatches, determine the last verified common state where establishable, examine durable operation evidence, distinguish committed changes from incomplete updates, preserve disputed versions when necessary and lawful, prevent automatic propagation of unvalidated corruption, verify the resulting representations, and record the actual outcome. If common state or legitimacy cannot be established, report uncertainty and preserve safe evidence; do not invent a winner or perform unrestricted mutual overwriting.

<a id="json-pending"></a>
#### 46.4.3. Pending states and unresolved saving decisions

Saving/acknowledgement timing, staging format, write protocol and universal authoritative-copy topology remain unresolved. An App Plan MUST resolve material choices through research and applicable owner authority before affected production implementation under [DEV-5](../7-%20Attacking%20and%20Freezing%20the%20Master%20Plan/710-%20Freezing%20the%20Approved%20Master%20Plan.md#dev-5). Do not infer permission either for early pending-state acknowledgement or a universal wait-for-both-copies policy. Honest statuses MUST describe the actual durable original-data point and separate per-file Current JSON, Folder JSON, and (when enabled) global Master JSON pending/incomplete/unknown states; no incomplete JSON may masquerade as a complete committed recovery representation. Mandatory Current JSON MUST eventually match a durably committed source revision or visibly remain pending/failed while preserving the last verified representation; it has no OFF switch. Folder JSON MUST retain its last verified published state while a successor is Pending Verification or Conflict Detected, without misrepresenting older verification as covering newer contents. Optional Master JSON must remain fully reconstructible when ON; when OFF the application must not fabricate a fresh global recovery representation.

<a id="json-distribution"></a>
#### 46.4.4. Multi-device and storage-provider boundaries

For supported laptop, phone, desktop/mobile, NAS, selected cloud or multi-device configurations, define write coordination, working copies, revision IDs, synchronization boundaries, offline operations, conflicts, delayed updates, connection/permission failures, recovery and movement between configurations. Preserve the enabled NAS hub policy under [SYNC-3](../12-%20Connecting%20and%20Completing%20the%20Application/1206-%20Integrating%20Offline%20and%20Sync%20Capabilities.md#sync-3) without treating it as final universal copy authority. Do not assume a shared physical writable filesystem works everywhere, ordinary cloud-folder sync atomically publishes huge JSON, or independent devices may edit a live SQLite/WAL database on unsupported network filesystems.

<a id="json-restore"></a>
#### 46.4.5. Failure scenarios and safe restoration

Recovery procedures MUST distinguish missing original files; corrupted individual/global/both current JSONs **where they exist**; valid-but-semantically-wrong copies; disagreement; interrupted writes; disk exhaustion; moved/unavailable storage; external edits; multi-record AI mistakes; app disappearance; and missing decryption keys. Select and validate an evidenced recovery point, preserve recoverable damaged originals before potentially destructive restoration, and never overwrite the only surviving damaged source merely for convenience. Offer supported same-location or separately selected restoration destinations with understandable consequences; use isolated validation where appropriate. Verify restored bytes, metadata, relationships, IDs and declared recovery point before adoption. Restored paths and symlinks MUST NOT escape the selected destination or overwrite unrelated/unapproved files. Detect absolute-path/traversal escapes, reserved names, case/Unicode collisions and target permission differences; preserve original names and required unsupported metadata through documented reversible mappings or report the unsupported restoration, rather than silently merging distinct files. Apply safe path confinement, symlink/traversal handling, collision/name mapping and current authorization under [IO-1](../10-%20Building%20the%20Core%20and%20Backend/1008-%20Implementing%20Required%20Core%20Capabilities.md#io-1), [PORT-2](../3-%20Deciding%20the%20Stack/308-%20Checking%20Compatibility%20and%20Portability.md#port-2) and [RECOVER-1](../12-%20Connecting%20and%20Completing%20the%20Application/1207-%20Integrating%20Error%20and%20Recovery%20Behavior.md#recover-1). If no surviving authorized source/key/dependency supports recovery, report the limitation without invented data or false guarantees.

<a id="s47"></a>
## 47. Revision integrity, external edits, and protected history

<a id="rev-1"></a>
### 47.1. REV-1 — Git-inspired content and revision evidence

**Type:** ECOSYSTEM POLICY | **Origin:** USER POLICY | **Applies:** retained-data workspace change tracking and external modification reconciliation

<a id="revision-records"></a>
#### 47.1.1. Revision and change evidence

Use stable revision identities, cryptographic content hashes, content comparisons, change manifests, structured differences where meaningful, recorded timestamps and previous-version relationships, content provenance and links to protected immutable verified history. Evaluate chunk-level hashing where useful for large content. Relevant change records MUST capture record identity, previous/new revision, affected fields/files, measured change size, recorded time and temporal context, old/new hashes, authorized operation identity where established, outcome, historical-content relationships and validation status where applicable. Unknown actors or times remain unknown; [DATA-5](../11-%20Building%20the%20Frontend/1109-%20Implementing%20Accessibility%20and%20Localization.md#data-5), [AUDIT-1](../10-%20Building%20the%20Core%20and%20Backend/1005-%20Implementing%20Transactions%20and%20Migrations.md#audit-1) and [EVID-1](../0-%20Start%20Here%20and%20Universal%20Rules/009-%20Evidence%20and%20Truthful%20Completion.md#evid-1) govern evidence and retention.

<a id="revision-hash-limits"></a>
#### 47.1.2. What hashes establish

Hashes identify/compare bytes against expected values; they neither store recoverable payloads nor prove authorship, time, legitimacy or factual correctness. Hashes/diffs MUST supplement rather than replace mandatory literal Current JSON or any enabled complete global Master JSON. Folder JSON hashes and inventories are integrity evidence, NOT another copy of file contents. Integrity against malicious rewriting requires the protected references/threat assumptions of [AUDIT-3](../14-%20Reviewing%20the%20Entire%20Application/1405-%20Reviewing%20Security%20and%20Data%20Safety.md#audit-3).

<a id="revision-detection"></a>
#### 47.1.3. External changes and detection latency

External changes by editors, other programs, AI filesystem writes, cloud sync or NAS clients MUST be promptly flagged where supported. Define expected identities/revisions, watcher monitoring where available, hash/version verification, rescan/reconciliation and clear user-visible discrepancies. Watchers may miss events; the application may be stopped; remote changes may not yet have propagated. Mandatory integrity reconciliation at relevant trust/commit boundaries MUST precede destructive overwrite or authoritative adoption, coupled to transitions under [CON-1](../10-%20Building%20the%20Core%20and%20Backend/1005-%20Implementing%20Transactions%20and%20Migrations.md#con-1); do not promise instantaneous detection everywhere.

<a id="revision-adoption"></a>
#### 47.1.4. Legitimate edits and safe adoption

An external edit is not automatically malicious. Preserve its version within legitimate retention/privacy limits, compare with verified state, and provide safe authorized adoption, rejection or preserved alternatives. An older Current JSON or Master JSON MUST NOT silently overwrite the changed original, and unvalidated external bytes MUST NOT blindly propagate into mandatory Current JSONs, published Folder JSONs or optional Master JSON/external backups. Report unresolved conflicts and containment through [EDIT-1](../12-%20Connecting%20and%20Completing%20the%20Application/1205-%20Connecting%20Complete%20Data%20Workflows.md#edit-1), [EDIT-2](../12-%20Connecting%20and%20Completing%20the%20Application/1205-%20Connecting%20Complete%20Data%20Workflows.md#edit-2) and [SYNC-1](../12-%20Connecting%20and%20Completing%20the%20Application/1206-%20Integrating%20Offline%20and%20Sync%20Capabilities.md#sync-1).

<a id="rev-2"></a>
### 47.2. REV-2 — Protected earlier revisions beyond current duplication

**Type:** ECOSYSTEM POLICY | **Origin:** USER POLICY | **Applies:** historical recovery protection for retained-user-data workspaces

<a id="history-failure-domains"></a>
#### 47.2.1. Independent historical recovery points

Every qualifying application MUST support separately protected historical recovery capabilities, including the optional complete external backup facility in [section 53](#s53). Actual independent complete backup retention is an explicit user-selected workspace policy (OFF, Single Backup, or Two Backups); the application MUST NOT claim independent historical recoverability when the user disables it. Equal original and Current JSON bytes cannot undo an incorrect edit propagated to both; Folder JSON supplies manifest evidence, not a third payload copy, and Single Backup may eliminate prior good points after rotation. The design and setup disclosure MUST address AI mistakes, deletion, incorrect transcript/user edits, corrupted JSON, synchronization errors, malicious changes, overwrites and storage failures, with actual declared failure domains, retention, residual risk and platform capabilities. Existing historical evidence is not erased by toggling OFF.

<a id="history-deletion-authority"></a>
#### 47.2.2. Deletion authority and finite retention

Where protected backup/history generations exist, normal application and AI editing credentials SHOULD NOT automatically have unrestricted deletion authority over all generations. Define meaningful separation of normal mutation and historical deletion authority, protected content/revision verification, recovery dependencies and actual residual risk under [BACKUP-1](../16-%20Maintaining%20Updating%20and%20Recovering/1606-%20Testing%20Backup%20and%20Restoration.md#backup-1). Immutable verified history means protected recorded revisions under the declared threat/retention model, not perpetual retention, proof of factual correctness or immunity to root compromise. Authorized erasure/expiry remains enforceable under [PRIV-1](../6-%20Writing%20the%20Complete%20Master%20Plan/606-%20Documenting%20Data%20Security%20and%20Recovery.md#priv-1), including prevention of forbidden resurrection. Finite enabled-JSON snapshot scope follows [JSON-3](#json-3); full external backups have independent finite capture/retention boundaries. No recovery guarantee survives destruction of all independent copies, required keys and dependencies.

<a id="s52"></a>
## 52. Topic 2: Optional Dual-JSON Recovery and Complete On-Site Backup — unratified design record

**Status:** Historical post-RC4 design record; **NOT RATIFIED**. Its original optional Dual-JSON toggle, four-mode table and five-minute individual schedule are **superseded by the later owner-locked per-file Current JSON / Folder JSON architecture in [section 53](#s53)**. This section is preserved only as decision provenance, not as newer design instructions. The separate [section 53](#s53) is the integrated **unratified amendment candidate** that proposes edits to governing rules. This section is not itself a second amendment or adopted policy. It adds no rule to RC4's 151 normative rules, changes no existing rule, and grants no application implementation or data-migration authority. The ratified baseline remains commit `aac66fa5ea1de8579b860f8833725c531317fde2` with `MASTER_PLAN.md` SHA-256 `4796b0f7ba168650cedde615a3382fe475cc64de14784bf6445849ec1a1fb53f`.

This design uses Menemora, a voice-recording and transcription application, as an example. Its folder names illustrate one workspace; they do not authorize moving existing data or impose the same domain folders on other products. Current requirements for the workspace, literal JSON payloads, restoration, history, backup, privacy, and honest outcomes remain in [sections 45–49](405-%20Designing%20Data%20Models%20and%20Storage.md#s45), especially [JSON-1 through JSON-4](#json-1), [REV-1 and REV-2](#rev-1), [BACKUP-1 and BACKUP-2](../16-%20Maintaining%20Updating%20and%20Recovering/1606-%20Testing%20Backup%20and%20Restoration.md#backup-1), [RECOVER-1](../12-%20Connecting%20and%20Completing%20the%20Application/1207-%20Integrating%20Error%20and%20Recovery%20Behavior.md#recover-1), [NOFALL-1 and NOFALL-2](../0-%20Start%20Here%20and%20Universal%20Rules/002-%20The%20Universal%20Constitution.md#nofall-1), [PRIV-1](../6-%20Writing%20the%20Complete%20Master%20Plan/606-%20Documenting%20Data%20Security%20and%20Recovery.md#priv-1), and [AUDIT-2](../10-%20Building%20the%20Core%20and%20Backend/1005-%20Implementing%20Transactions%20and%20Migrations.md#audit-2).

<a id="topic2-status"></a>
### 52.1. What the owner has agreed, and what this record does

The proposed product has two separately controlled workspace protections:

1. **Workspace Dual JSON** keeps a complete individual JSON representation for each applicable record or component and a complete global `master-data.json` inside the primary workspace.
2. **Complete On-Site Backup** creates full, standalone physical copies of the declared retained workspace in a separately selected destination.

The owner controls each setting independently. The proposed future constitutional direction is that qualifying applications support the approved Dual-JSON capability while each user may choose whether active Dual-JSON redundancy is enabled for a workspace. External complete backup remains an independent user choice. This policy has not been integrated into or approved as a replacement for RC4.

<a id="topic2-configurations"></a>
#### 52.1.1. Four independent settings combinations

| Workspace Dual JSON | Complete On-Site Backup | Proposed workspace state |
|---|---|---|
| OFF | OFF | Original workspace data, plus any separate protections still required by the governing constitution and application contract. Do not imply that no protection is required. |
| ON | OFF | Original workspace data and its active individual and global JSON representations. No Complete On-Site Backup is being created by this feature. |
| OFF | ON | Original workspace data and independently versioned complete external backups. Do not generate new complete JSON representations merely because backup runs. |
| ON | ON | Original workspace data, active individual and global JSON representations, and complete external backups. |

Turning either setting OFF does not itself authorize deleting data already produced by that feature. The user must be told what is paused, retained, or unavailable. Deletion and retention follow [PRIV-1](../6-%20Writing%20the%20Complete%20Master%20Plan/606-%20Documenting%20Data%20Security%20and%20Recovery.md#priv-1) and any future approved policy. Pausing, resuming, and separately deleting historical JSON representations remain open decisions.

<a id="topic2-conflict"></a>
#### 52.1.2. Explicit conflict with ratified RC4

RC4 [JSON-1](#json-1), [INFO-1](../5-%20Designing%20the%20UI%20and%20UX/503-%20Designing%20Information%20Architecture%20and%20Flows.md#info-1), and [SURVIVE-1](405-%20Designing%20Data%20Models%20and%20Storage.md#survive-1) currently require accessible retained-workspace data and complete literal individual and global JSON recovery representations for applicable retained-user-data workspaces. Making active Dual JSON optional conflicts with those current requirements. The proposed option cannot silently take effect as current RC4 policy; a future formal amendment must state which clauses change, what protection remains when the option is OFF, and how affected requirements are reconciled.

The term “JSON recovery source” describes a data-recovery representation, not an alternate execution implementation. RC4 [NOFALL-2](../0-%20Start%20Here%20and%20Universal%20Rules/002-%20The%20Universal%20Constitution.md#nofall-2) expressly treats its two JSON layers as complementary recovery representations and permits verified restoration. This proposal does not authorize a hidden secondary database or other substitute to satisfy JSON-1, nor a concealed execution path after failure. Operational databases may retain their separately defined responsibilities under existing workspace rules.

The proposed one- or two-version Complete On-Site Backup retention modes also need reconciliation with RC4 [REV-2](#rev-2)'s independent protected historical recovery points and [BACKUP-1](../16-%20Maintaining%20Updating%20and%20Recovering/1606-%20Testing%20Backup%20and%20Restoration.md#backup-1)'s failure-domain and deletion-authority protections. A single retained copy, or two copies removable through the same ordinary credentials, cannot be presumed to satisfy those requirements. The future amendment must define whether another mechanism continues to meet RC4 when this feature is OFF or in Single Backup mode; the proposed retention count does not waive existing protection.

<a id="topic2-locations"></a>
### 52.2. Primary workspace, JSON locations, and external destination

The primary workspace remains the location of original user data. When Dual JSON is active, its individual and global recovery representations also remain in that workspace. They are not moved into the external backup destination. A complete external backup copies the declared workspace contents, including whichever JSON files exist at the captured recovery point.

An illustrative Menemora layout is:

    Menemora/
    ├── 00-START-HERE.md
    ├── 01-FOLDER-GUIDE.md
    ├── 02-DATA-DICTIONARY.md
    ├── catalog.json
    ├── master-data.json                 (when Dual JSON is active)
    ├── Recordings/
    │   └── 2026/October/Interview_A7F2/
    │       ├── recording.m4a
    │       ├── recording.json            (when Dual JSON is active)
    │       ├── transcript.md
    │       ├── Notes/notes.md
    │       └── History/changes.json
    └── Settings/
        ├── settings.json
        └── System/
            └── Recovery/
                ├── recovery-state.json
                ├── Transactions/
                └── Incidents/

    Selected external destination/
    └── Menemora/
        ├── Backup-Version-<identity>/
        └── Backup-Version-<previous-identity>/    (Two Backups mode)

The paths, filenames, and physical transaction layout are examples, not finalized storage protocol. Settings, retained histories, recovery evidence, credentials, and derived state each need the scope, access, retention, and recovery treatment required by their purpose. Do not expose credentials in ordinary readable JSON. Any backup exclusions—such as transient caches, incomplete staging, or the backup destination itself—must be explicit, justified, and safe from recursive inclusion.

<a id="topic2-first-run"></a>
### 52.3. First-run setup and ongoing controls

Before initial storage configuration, the application is to show the user the primary workspace location and proposed folder structure; where original data, settings, history, recovery information, and individual/global JSON would reside; any storage outside the selected workspace; whether existing data was detected and may be adopted; and relevant capacity and permission information. It should clearly identify which files are originals and which are recovery representations.

The user separately chooses **Workspace Dual JSON: ON or OFF** and **Complete On-Site Backup: ON or OFF**. Neither is silently selected on the user's behalf during first-time setup. If external backup is enabled, the user selects a supported destination, such as an external SSD, external HDD, NAS share, or another validated folder. The application checks the destination and explains whether it is physically independent from the primary workspace and the failure risks that remain. A different path, drive letter, mount, or NAS label alone does not establish independence.

After setup, both controls remain available through **Settings → Data Management**. Recovery approval and urgent integrity notices may appear in context while configuration remains discoverable there. The precise interface may differ by application; the settings and consequences must remain understandable.

If the application detects an existing workspace, it must distinguish adopting and validating that workspace from creating a new one. It must not silently reorganize files or overwrite an existing workspace during setup.

<a id="topic2-json-init"></a>
### 52.4. Enabling Dual JSON for an existing workspace

If the user enables Dual JSON after the workspace already contains data, the initial complete representation is **Workspace JSON Version 1**. Initialization is complete only after the application has:

1. Inventoried the retained data and declared recovery scope.
2. Validated relevant files, relationships, and the selected workspace identity.
3. Established a logically consistent baseline boundary.
4. Constructed all applicable complete individual JSON representations and the complete global `master-data.json`.
5. Verified the representation contents and their ability to reconstruct the declared retained data.
6. Published the verified baseline as Workspace JSON Version 1 and continued under the selected save policies.

Initialization must not assemble a mixed-time baseline while the application or external programs change files. The physical consistency method and the handling of edits during the build are not settled here. A process start, partial set of JSON files, or syntactically valid output is not a verified Version 1. An interrupted attempt must leave original data protected, report incomplete work, and preserve any safely recoverable evidence. Keep the application usable where doing so is safe.

<a id="topic2-json-scheduling"></a>
### 52.5. Edit protection, JSON schedules, and resource reporting

The agreed saving discussion has three layers, whose exact transaction protocol remains open:

1. **Durable edit protection.** Acknowledged edits need durable protection under the applicable data-safety policy without waiting for a potentially large full JSON rebuild. How this minimum durability works when optional Dual JSON is OFF has not been resolved. The future amendment must reconcile the user toggle with the applicable minimum durability and [OUT-1](../0-%20Start%20Here%20and%20Universal%20Rules/009-%20Evidence%20and%20Truthful%20Completion.md#out-1); it must not imply that OFF makes acknowledged edits disposable.
2. **Individual JSON.** When Dual JSON is ON, the discussed user choices are immediate updates, updates every five minutes, or updates when the user becomes idle. These choices apply to individual JSON representations, not automatically to the full global JSON.
3. **Global JSON.** The complete `master-data.json` has its own schedule. Smart/Adaptive is the preferred mode discussed: an eligible update may start when pending changes exist and resource and execution conditions permit. Scheduled and manual updates were also discussed. Each published global JSON must represent a complete verified retained-workspace revision.

Individual JSON and global JSON may have separate resource profiles: **Memory Saver**, **Balanced**, and **Priority**. Values, triggers, fairness, capacity limits, and behavior when resources are unavailable are not selected by this record.

The interface is to distinguish the latest durably recorded edit, individual JSON revision, global JSON revision, pending changes, verification state, resource mode, failures, and recovery requirements. A generic “Saved” indicator must not imply that all layers are current when only an edit or one JSON layer is durable.

No resource-intensive saving or backup job silently continues after the application closes. Any post-close completion worker must be visible and explicitly authorized, then stop when its approved job finishes. No universal post-close execution guarantee is claimed for unsupported operating systems.

<a id="topic2-backup-init"></a>
### 52.6. Complete On-Site Backup and its first verified version

Complete On-Site Backup is separate from Dual JSON. It is user-controlled and has its own destination, schedule, resource policy, version identities, and retention choice. Each completed backup is a full, standalone physical copy of the entire declared retained-workspace scope, browsable as ordinary folders wherever the retained items are ordinary files. It is neither incremental nor a hybrid that requires an earlier backup to reconstruct the declared contents.

The complete scope may include original recordings and other files, transcripts, notes, folder structure, settings, retained histories, relevant manifests and documentation, recovery metadata, individual JSON files if present, the global JSON if present, and every other retained item included in the defined scope. Any exclusions must be documented as described in [section 22](../16-%20Maintaining%20Updating%20and%20Recovering/1606-%20Testing%20Backup%20and%20Restoration.md#s22). A manifest or hash may support inventory and verification, but cannot replace missing payload.

Each backup has an identity in a namespace separate from Workspace JSON versions. If backup is enabled for a workspace that already contains years of data, the first successfully verified complete backup is **External Backup Version 1**. Initialization is not complete until both the copied contents and the published recovery point have been verified. A started, partial, inaccessible, or unverified copy is not a completed backup.

The backup process captures a consistent workspace state under a mechanism to be selected and tested for the target platform. It copies the JSON revisions that actually exist at that state and reports any lag or pending changes. A backup run does not silently trigger full regeneration of `master-data.json`. A disconnected drive, unavailable NAS, access denial, or uncertain copy result cannot be reported as success.

<a id="topic2-backup-schedule"></a>
### 52.7. Complete backup schedule

The five discussed frequency choices are **Daily**, **Weekly**, **Smart / Adaptive**, **Manual**, and **Custom**. Daily and weekly express an aim to create a complete backup each day or week; they do not promise execution when the destination, resources, permission, or authorized execution window is unavailable. Smart/Adaptive may start an eligible complete backup when changes, resources, destination availability, and authorized execution conditions permit. Manual runs only on an explicit request. Custom lets the user choose a supported schedule. All modes expose **Back Up Now**.

Backup frequency is independent of both JSON schedules and of retention mode. A missed run is shown as overdue and follows a transparent execution policy; a failed attempt is not a successful cycle. Execution and resource use remain bounded. The exact time zone, retry limits, catch-up behavior, and custom schedule syntax remain open.

<a id="topic2-backup-retention"></a>
### 52.8. Single Backup and Two Backups retention

The two proposed normal retention choices are:

| Mode | Completed versions retained after a successful safe rotation |
|---|---|
| **Single Backup** | The latest successfully verified complete backup. |
| **Two Backups** | The latest successfully verified complete backup and its immediately preceding successfully verified complete backup. |

For example, Two Backups advances from Current V1; then Current V2 / Previous V1; then Current V3 / Previous V2, with V1 retired after V3 is safely published. A failed attempt does not advance rotation.

The replacement must be fully copied, verified, and durably published before an older protected version is retired. Safe construction may temporarily require space for existing completed versions plus the staged candidate: Single Backup may need two physical copies during construction, and Two Backups may need three. The configured limit applies to completed retained versions after successful cleanup, not every staging instant. If capacity is insufficient, stop and report it; do not delete the only verified copy early to make room.

Pause automatic retirement of potentially valuable versions when corruption, unresolved missing files, or significant integrity conflicts have been detected. Show the hold and temporary extra storage clearly. Disclose that undetected corruption can be copied into a newer full backup. Turning backup OFF does not silently remove existing verified backups. Exact crash-safe publication and retirement mechanisms remain unresolved.

<a id="topic2-everyday-recovery"></a>
### 52.9. JSON-first everyday recovery and complete disaster recovery

For ordinary repair when Dual JSON is active, the proposed investigation order is: examine the relevant individual JSON; durable pending changes and revision relationships; the global `master-data.json` as needed; then other verified retained historical sources. Prepare the best-supported candidate. A newest timestamp alone does not establish the correct revision. An older individual JSON must not cause newer valid durable changes to be ignored. If only one file is damaged, repair only that file unless evidence justifies a wider operation.

Detection, investigation, and preparation may be automatic when safely supported. Replacing an existing original requires explicit user approval under [JSON-4](#json-4), [RECOVER-1](../12-%20Connecting%20and%20Completing%20the%20Application/1207-%20Integrating%20Error%20and%20Recovery%20Behavior.md#recover-1), and the exact-target safeguards in [section 52.12](#topic2-restoration-safety).

Complete On-Site Backup primarily supports disasters such as loss of the primary drive, severe workspace destruction, large-scale unrecoverable loss, or reconstruction on replacement hardware. The proposed flow validates the selected backup and its versions; shows recovery-point information; lets the user choose a safe destination; avoids silently overwriting an existing workspace; restores the complete retained folder structure; verifies files and dependencies; reestablishes appropriate workspace identity and settings; reports unavailable, missing, or incompatible contents; and records the operation. A physically failed source drive whose original bytes cannot be accessed cannot have those bytes preserved by the software. The external destination protects against that failure only if it survives in a genuinely separate failure domain.

<a id="topic2-selective-compare"></a>
### 52.10. User-requested missing-file comparison

The proposed action is discoverable at **Settings → Data Management → Recovery & Restoration → I Think I'm Missing a File**. It is an explicit, read-only comparison and selective-recovery workflow:

1. Identify the active primary workspace and its stable identity.
2. Ask the user to select the external backup drive or folder, optionally suggesting a previously configured destination.
3. Validate the backup and identify available verified versions. In Two Backups mode, allow comparison with both current and previous versions.
4. Compare the current workspace with the selected version or versions and present a clear report.
5. Let the user inspect differences, choose files, and approve any proposed workspace changes.

Scanning and comparison do not change the workspace or external backup. A missing path can reflect intentional deletion, disconnected storage, revoked permission, or a different workspace; it is not automatically corruption, and an inaccessible workspace must not appear as an empty one.

At minimum, classify items as missing from current workspace, different, present only in current workspace, matching, or uncertain/inaccessible. Identify potential moves or renames only when trustworthy evidence supports that conclusion. Prefer a bounded inventory/manifest comparison using trusted relative paths, stable identities when available, sizes, revision metadata, recorded hashes, backup manifests, and current inventory. Investigate bytes more deeply where needed. Do not reread hundreds of gigabytes when a cheaper comparison can answer the question; manifest agreement alone is not a claim of fresh byte-by-byte verification.

Show missing, different, workspace-only, matching where useful, uncertain items, and the backup versions compared. Each item can be inspected by name, original relative path, current and backup locations, size, available hashes, backup version, relevant revision, available history, verification state, and conflicts. Permit individual selection and safe bulk selection. Treat ambiguous or conflicting items separately.

<a id="topic2-selective-restore"></a>
### 52.11. Selective restoration from a complete backup

The owner-approved design direction permits a user to restore one or more explicitly selected files from a complete backup without restoring the entire workspace. This is an intentional, user-requested path alongside ordinary JSON-first repair. For example, a transcript missing from the current workspace may be inspected in Backup V12 and restored from V12, or from V11 if V12 lacks it. The application never silently chooses an older copy or restores every absent file.

The proposed operation validates the selected version and target relative path; treats the external backup as read-only; stages and verifies the selected content; rechecks destination identity and current state; detects a file that appeared or changed since comparison; seeks renewed approval if the proposal's conditions changed; installs only the approved items; verifies the result; records provenance; and updates relevant recovery metadata and JSON status if Dual JSON is active. A genuinely absent target has no existing target bytes to preserve. If a target exists, treat it as a replacement conflict and apply the exact-byte safeguards below. Do not silently overwrite newer work or modify the backup during comparison or restore.

<a id="topic2-restoration-safety"></a>
### 52.12. Exact-byte preservation and explicit replacement approval

Before replacing an existing original, the proposed procedure identifies the trusted workspace and exact target; inspects current contents and revision information; validates the recovery source; reconstructs the candidate in isolated staging; verifies its bytes and required metadata; checks available capacity; and explains the recovery point, consequences, and conflicts. Approval is bound to the exact target, its observed current state, selected source revision, and proposed replacement bytes. Revalidate immediately before mutation. If the target changed after review or approval, stop and present a new proposal; do not silently overwrite it.

Preserve the original's exact existing bytes before replacement and verify that preservation. Then apply the authorized replacement through a recoverable transaction, verify the active result, record the outcome, and update revision/JSON states truthfully. Restoring an earlier point creates a new recovery revision with provenance; it does not rewrite history to imply the incident never occurred. After JSON-based repair, promptly synchronize the affected individual JSON when Dual JSON is ON using recovery-specific durability safeguards. The global JSON retains its separate schedule. Restoration never silently turns Dual JSON ON.

The proposal accounts for traversal, malicious filenames, symlinks, junctions/reparse points, escapes from the chosen workspace, collisions, destination changes, concurrent external edits, insufficient space, interrupted copy, crashes, partial completion, and failed readback. Do not assume one rename makes a multi-file operation atomic or durable. For multi-file repair, maintain durable per-file and batch transaction state. On partial failure, state exactly what was preserved, changed, verified, or left uncertain, and retain safely recoverable evidence.

For bulk restoration, present a closed list, validate each item, and use one understandable batch approval where appropriate. Exclude ambiguous, unsafe, or changed items; never add files after approval; report partial outcomes; and preserve exact damaged bytes before replacing any approved existing file. Incident archives may hold evidence, provenance, verified identities, hashes, decisions, and failure details. Archive naming must not blindly inherit an untrusted source filename. The illustrative Recovery/Incidents layout in [section 50](410-%20Reviewing%20Architecture%20Decisions.md#s50) is not a finalized protocol.

<a id="topic2-states"></a>
### 52.13. Disabled, incomplete, and conflicting states

| State | Proposed truthful behavior |
|---|---|
| Dual JSON OFF | Do not assume complete JSON recovery exists. An available external backup may support user-initiated selective restore. Do not silently enable JSON. |
| External backup OFF | JSON recovery may be available if Dual JSON is ON. Do not imply that JSON on the failed primary drive survives physical loss of that drive. |
| Both OFF | Explain recovery limitations while retaining any other protections required by the applicable constitution and product contract. Do not invent a source. |
| JSON Version 1 incomplete | Do not call it verified. Individually verified artifacts may be considered only under a qualified recovery procedure. |
| Backup creation incomplete | Do not publish it as verified; protect the previous verified backups. |
| Requested historical revision unavailable | Say it is unavailable and offer evidenced alternatives without silently substituting another revision. |
| Evidence inadequate or conflicting | Do not automatically replace originals. Offer investigation, safe export, comparison, or restoration to a separate destination where appropriate. |
| Destination unavailable or inaccessible | Report the actual access/connectivity state; do not label the workspace empty or claim a completed backup. |

<a id="topic2-reporting"></a>
### 52.14. Status, integrity, and security limits

Status distinguishes original edit durability; individual and global JSON revision and verification; pending work; selected resource mode; backup schedule and overdue state; selected destination and access; current and previous backup identities; verification and publication state; retirement hold; recovery requirements; and errors or unknown outcomes. “Saved,” “protected,” “verified,” and “recoverable” must describe the specific evidence and boundary they actually establish.

Hashes support byte comparison and accidental-corruption detection when compared with an appropriate expected value. A hash stored beside a compromised file is not independent proof of authenticity, authorship, factual correctness, or clean history. Distinguish byte integrity, revision consistency, authenticity, physical independence, and disaster recovery. NAS or external storage is not independent merely because it has another path. Stronger defenses may need separately protected trust anchors, access control, or immutable protection; those designs are open.

<a id="topic2-open"></a>
### 52.15. Agreed direction versus unresolved decisions

This paragraph records the historical earlier option as originally discussed. The **later owner-locked requirements in section 53** supersede its optional Dual JSON toggle, four configuration descriptions and individual JSON scheduling decisions: Current JSON and lightweight verified Folder JSON are always-on, whereas only complete global Master JSON and external physical backup remain optional. Other enduring safety decisions here (complete backups, selective restore, exact-byte preservation, truthful failure states) remain applicable as reconciled by section 53.

The following choices remain open; this section does not select mechanisms or defaults on the owner's behalf:

| Open decision | Still to be established |
|---|---|
| Durable transaction protocol | How acknowledged edits, originals, JSONs, backup publication, metadata, and operation evidence reach a truthful durable boundary. |
| Consistent snapshots | Platform-appropriate point-in-time consistency across files and stores, including external writers. |
| Locking and coordination | Local, NAS, removable-storage, cloud-provider, and multi-device writer coordination; stale-writer exclusion and offline changes. |
| Crash recovery and replay | Durable transaction state, recovery ordering, idempotency, uncertain outcomes, and safe cleanup after interruption. |
| Approval persistence and invalidation | What approval survives restart, how it binds to exact state/bytes, expires, and becomes invalid after external change. |
| Incident retention and protected originals | Retention limits, capacity, privacy, access separation, encryption, and deletion authority. |
| Verification and trust anchors | Which checks are freshly performed, independent evidence, tamper assumptions, key handling, and what “verified” means by operation. |
| Backup publication and retirement | Crash-safe promotion, catalog updates, cleanup, and proof the replacement is usable before retirement. |
| Insufficient space and interruption | Preflight limits, cancellation, required staging capacity, partial-state handling, and recovery without premature deletion. |
| Damaged storage | Behavior when reads fail, storage degrades during copy, or the source may be failing physically. |
| First-run validation | Supported destination types, permission/capacity checks, identity and existing-workspace adoption, and accurate independence disclosures. |
| Optional JSON and minimum durability | How the user toggle coexists with mandatory edit durability and the current RC4 JSON-1/INFO-1/SURVIVE-1 requirements. |
| Retention and RC4 protection | How Single/Two Backups satisfies or coexists with REV-2's independently protected history and BACKUP-1's failure-domain/deletion protections, including when this feature is OFF. |
| Constitutional amendment | Exact future wording, affected rule dispositions, transition behavior, and separate owner ratification process. |
| Adversarial validation | Test cases for hostile paths, races, crashes, power loss, tampering, partial batch operations, and supported platform/storage combinations. |

<a id="topic2-amendment"></a>
### 52.16. Future amendment implications

Before any part of this design becomes active constitutional policy, a separately authorized amendment should start from the then-authoritative revision and identify the affected rules. At minimum, it must reconcile the proposed optional active Dual JSON with [JSON-1](#json-1), [INFO-1](../5-%20Designing%20the%20UI%20and%20UX/503-%20Designing%20Information%20Architecture%20and%20Flows.md#info-1), and [SURVIVE-1](405-%20Designing%20Data%20Models%20and%20Storage.md#survive-1); preserve the recovery-source distinction and [NOFALL-2](../0-%20Start%20Here%20and%20Universal%20Rules/002-%20The%20Universal%20Constitution.md#nofall-2); define how minimum edit durability remains protected; and reconcile optional external backup and its Single/Two retention modes with [REV-2](#rev-2), [BACKUP-1](../16-%20Maintaining%20Updating%20and%20Recovering/1606-%20Testing%20Backup%20and%20Restoration.md#backup-1), [BACKUP-2](../16-%20Maintaining%20Updating%20and%20Recovering/1606-%20Testing%20Backup%20and%20Restoration.md#backup-2), [PRIV-1](../6-%20Writing%20the%20Complete%20Master%20Plan/606-%20Documenting%20Data%20Security%20and%20Recovery.md#priv-1), and [RECOVER-1](../12-%20Connecting%20and%20Completing%20the%20Application/1207-%20Integrating%20Error%20and%20Recovery%20Behavior.md#recover-1). It must state retained protections in every setting combination and distinguish proposed policy from platform-specific engineering decisions.

This section records the owner's post-RC4 design direction for future discussion. It does not edit, renumber, replace, or ratify any RC4 rule; change the existing count of ratified rules; authorize implementation against user data; or resolve any open question above. Ratification remains a separate owner decision under [GOV-3 through GOV-5](../0-%20Start%20Here%20and%20Universal%20Rules/003-%20Rule%20Priority%20and%20Authority.md#gov-3).


<a id="s53"></a>
## 53. Universal Current JSON, verified Folder JSON and selective reconciliation — OWNER-LOCKED / UNRATIFIED

**Authority boundary:** The owner has LOCKED the universal mandatory Current JSON, verified Folder JSON (Option B), and highlighted selective-diff reconciliation decisions. This section and its edits to earlier rules constitute an **unratified constitutional amendment candidate**, not separate formal ratification. Ratified RC4 continues to govern until separately approved through [GOV-3](../0-%20Start%20Here%20and%20Universal%20Rules/003-%20Rule%20Priority%20and%20Authority.md#gov-3), [GOV-4](../17-%20Preserving%20Memory%20and%20Learning/1710-%20Improving%20the%20Universal%20Rules%20System.md#gov-4), [GOV-5](../7-%20Attacking%20and%20Freezing%20the%20Master%20Plan/708-%20Performing%20Independent%20Adversarial%20Reviews.md#gov-5). The ratified source is commit \`aac66fa5ea1de8579b860f8833725c531317fde2\` and remains unchanged. [Section 52](#s52) is the owner's design-decision record. If this candidate's explicit controls conflict with preexisting language in this candidate, those clauses must be reconciled before ratification rather than treated as silently overridden. No current application, user-data migration, backup deletion, rollout, or source-code implementation is authorized by this document alone.

### 53.1. Owner-locked universal protection policy

Every qualifying application retaining user-owned original files MUST maintain **Current JSON** (one complete independent recoverable JSON per original file or appropriately justified durable logical data object) and a **Folder JSON** (a verified lightweight manifest of file membership, identity, path, revision and relationships for each applicable folder). **These two capabilities are mandatory, permanently ON and not user-disableable.** Current JSON contains literal original bytes; Folder JSON does not duplicate the file bytes. This applies universally to qualifying apps, with Menemora only an example.

Only a complete global **Master JSON** within the primary workspace and a separately located **Complete On-Site Backup** are user-optional, each controlled independently.

| Current JSON | Folder JSON | Optional Master JSON | Optional Complete On-Site Backup | Recovery representation |
|---|---|---|---|---|
| ON (mandatory) | ON (mandatory) | OFF | OFF | Original + complete per-file Current JSON on the primary workspace drive; verified Folder JSON is a manifest, not another copy. No separate drive-loss copy. |
| ON (mandatory) | ON (mandatory) | ON | OFF | Above plus independently reconstructible global Master JSON inside the primary workspace. |
| ON (mandatory) | ON (mandatory) | OFF | ON | Mandatory per-file recovery and manifests plus separately selected full standalone physical backups. |
| ON (mandatory) | ON (mandatory) | ON | ON | All four layers, with independently declared verification, freshness and failure domains. |

Mandatory Current/Folder JSONs cannot be turned OFF, paused as an optional feature or silently deleted by routine cleanup. Optional Master JSON and Complete Backup may each be switched OFF without silently deleting historical retained artifacts; any later deletion requires explicit, applicable authorization and privacy/retention handling. Original-file saving remains appropriately crash-safe and edit durability reporting honest in all four configurations.

### 53.2. First-run Settings and folder visibility

The setup flow MUST display the approved primary workspace path; original data folders; settings, history, catalogs, recovery files and relevant external locations; proposed directory tree; and how an existing user-owned workspace will be adopted, validated or left untouched. It MUST describe mandatory always-on Current JSON and Folder JSON as built-in architecture and explicitly collect ON/OFF choices only for optional Master JSON and Complete On-Site Backup, neither preselected silently. The workspace location and backup destination are different settings. When backup is ON, the user selects and approves a backup folder (for example, an external drive or NAS). The app checks reachability, permissions, space, identity and whether the destination is actually physically independent; another drive letter is not proof of another failure domain. App-internal and temporary storage outside the chosen workspace must be explained when applicable.

Central controls reside in **Settings → Data Management**, with discoverable overview, storage paths, protection switches, schedules, resource controls, backup versions, recovery and background activity. Contextual integrity notices and necessary restoration approvals may appear elsewhere; this does not move the underlying configuration out of Settings. Never silently create an empty substitute workspace because its configured location disappeared.

### 53.3. Mandatory immediate per-file synchronization and verified Folder JSON

The first-time setup or adoption of an existing workspace MUST inventory retained user files, stable identities and declared recovery scopes, validate source data and construct each file's complete Current JSON. Publish each initial verified per-file baseline only after exact-byte reconstruction checks. Create per-folder manifest baselines at an evidenced consistent revision boundary. Incomplete initialization is pending rather than proof of protection; do not disturb existing original bytes. A newly created original file gets its own mandatory Current JSON and properly verified folder membership.

**Immediate synchronization:** a recognized authorized file change MUST promptly initiate or safely queue an update **only for that changed file's Current JSON**. This is a trigger/eligibility requirement, not a guarantee that multi-gigabyte serialization completes instantly or every five seconds. Coalesce rapid edits safely using durable change evidence; do not indefinitely defer a pending current revision, and report verified source/current divergence. Current JSON remains a *complete literal payload* for its scope, never just a delta, pointer, hash or patch. Publish a verified staged successor without damaging the previous verified version or original; skipped, delayed, failed or interrupted writes remain visibly pending/failed.

**Folder verification:** after a relevant Current JSON change, the app queues resource-bounded, visible asynchronous verification for the relevant Folder JSON and any affected ancestor/old-new folder. The verifier examines the actual original, Current JSON, trusted identity/revision evidence and folder relationships at a consistent snapshot boundary. A newly detected edit during checking must not result in a mismatched mixed-time publication. Preserve the **last verified Folder JSON**, mark the new changes **Pending Verification** or **Conflict Detected**, and publish the new manifest only after its declared scope passes verification. Changed files/folders are prioritized; do not routinely scan or rewrite thousands of unrelated entries. Use bounded periodic/trust-boundary reconciliation to handle missed watcher notifications. Folder JSON never duplicates the original payload and alone cannot restore a lost file.

**Optional complete Master JSON** has a separate ON/OFF setting and independently verified **Global Master JSON Version 1** at first enabled successful initialization. It retains its complete standalone workspace-recovery scope, separate **Smart / Adaptive**, scheduled or manual update options, and verified version/freshness evidence. Master JSON is not regenerated wholesale merely to acknowledge a Current JSON update. External Complete On-Site Backup has its own frequency, verification and version namespace.

The UI MUST separately report original edit durability, per-file Current JSON verification/pending state, per-folder verified vs pending/conflict state, and optional global Master JSON freshness and external-backup completion. A generic green "Saved" indicator cannot equate original-save completion with successful verification of every recovery layer. Resource profiles Memory Saver/Balanced/Priority can govern bounded work but cannot disable mandatory protection. No undisclosed post-close verification or saving process; allow finish-before-close, expressly approved visible worker or safe resume later **only when pending data has appropriate durable protection and the user understands the risk**. Crash-safe original commits, journal protocol, staging, cancellation and cross-file atomicity remain target-platform implementation gates.

### 53.4. Complete On-Site Backup — full copies, schedules and versions

A Complete On-Site Backup is a **complete standalone physical workspace copy** in the user's separately selected destination, preserving ordinary files/folders for direct browsing and independent restoration. It is **not incremental, differential or hybrid**, and it never requires prior backup versions to reconstruct a published version. It covers all declared retained original files and associated settings, metadata, documentation, histories, recovery information, mandatory Current JSONs and Folder JSON manifests, and global Master JSON **when enabled or otherwise retained**. Excluded temporary artifacts and recursive backup containers must be specifically documented with complete retention/reconstruction consequences. Backup copies must have an independently verified consistent source boundary; copying a moving collection of files into an inconsistent mixed-time representation is not a valid complete recovery point. A new backup DOES NOT silently force regeneration of mandatory per-file Current JSON or optional global Master JSON, nor complete pending Folder JSON verifications; it records the actual snapshot's verified revisions and any lag.

The first successfully verified complete backup of existing data is **External Backup Version 1**, distinct from mandatory per-file Current JSON and per-folder manifest revisions and optional Global Master JSON Version 1. No started, staged, interrupted or partially verified candidate may masquerade as a completed backup. Backup frequency is user-configurable independently of JSON schedules and retention: **Daily**, **Weekly**, **Smart / Adaptive**, **Manual**, or **Custom**. All modes expose **Back Up Now**. Schedules are eligibility targets, not guarantees when the NAS, external drive, authorization or resources are unavailable. Report due/overdue/failure/unknown accurately. Reconnection must verify destination identity before a resumed operation; no hidden post-close worker is implied.

The user chooses one of exactly two ordinary completed-version retention policies:

* **Single Backup:** latest successfully verified complete version after safe replacement.
* **Two Backups:** latest and immediately preceding successfully verified complete versions; each is a full standalone copy.

A new version MUST be fully constructed, verified and durably published **before** the old protected version is retired. This may temporarily require two physical full copies for Single mode or three for Two mode (including new staging), while normal completed retention returns to one or two after cleanup. Do not delete a verified backup early to make storage space; stop, disclose capacity shortfall and offer authorized alternatives. Failed attempts do not advance rotation. Suspend automatic retirement when known corruption, unresolved missing files or major integrity disputes make an old version potentially uniquely useful, recording any temporary retention excess. Because unknown corruption may be copied into a new backup, never guarantee that rotating a verified *byte-copy* guarantees a semantically healthy historical source. Every retirement must respect authorized erasure and historical access/security constraints.

### 53.5. JSON-first everyday repair and external disaster recovery

Ordinary local-file repair investigates the corresponding mandatory Current JSON first, then relevant durable pending changes/lineage and Folder JSON evidence, then any verified enabled global \`master-data.json\` or other surviving independently verified historical source. This is a **source-investigation order**, not a rule that the newest timestamp or first matching JSON automatically wins. Prefer file-scoped restoration when only one original is affected. Unexplained file differences may be deliberate external edits; do not silently roll them back. The engine MAY detect, investigate and stage a verified candidate automatically within authorized resources, but MUST obtain approval before replacing an existing original.

The separate complete backup is primarily for catastrophes: failed or lost primary storage, destroyed workspace, or large-scale unrecoverable loss. An explicitly chosen verified full backup can reconstruct the declared workspace in a safely selected location without relying on an earlier backup. A physically inaccessible original device's bytes cannot be promised recoverable or preserved. Avoid automatic destructive restoration into an occupied location; report backup freshness, gaps and key/schema dependencies.

If Complete On-Site Backup is ON, a user MAY initiate a scoped file restore directly from a verified external backup independently of the optional Master JSON setting. Mandatory Current JSON always remains present as an application capability; the external restoration route is neither a hidden fallback implementation nor automatic backup-triggered replacement.

### 53.6. “I Think I'm Missing a File” — read-only comparison and selective restoration

Settings → Data Management → Recovery & Restoration MUST expose **“I Think I'm Missing a File”** or an equally clear localized action. The user chooses the backup folder or drive, optionally aided by the last configured location. Before comparing, validate backup identity, applicable manifest and available verified versions; Two Backup mode allows inspection of both retained versions. Comparison MUST remain read-only for both backup and workspace.

The result MUST distinguish files **missing from workspace**, **different**, **workspace-only**, **matching**, and **uncertain/inaccessible**, plus suspected moves or renames only where supported by evidence. Do not interpret a disconnected workspace as empty or automatically resurrect intentionally deleted files. Use manifest/inventory metadata to narrow comparison efficiently; inspect actual bytes when required to substantiate the proposed repair. A matching manifest alone does not prove a fresh content read.

For each candidate show the trusted relative path, backup version, relevant identity/revision, size, available hashes, current/backup location, verification state and conflicts; offer explicit individual or bounded bulk selection. If the latest backup lacks the desired file but a previous verified backup contains it, let the user inspect and deliberately choose that older version. No automatic bulk restore or unapproved expansion of selected items.

For authorized missing-file recovery: copy only the selected backup bytes into isolated staging, verify them, revalidate the destination and its nonexistence immediately before installing, then place and reread the file at the approved path and record provenance. If a file appeared at the target or its identity changed after comparison, invalidate the earlier approval and treat it as an existing-file replacement instead.

### 53.7. Existing-file replacement — exact-byte preservation

Any operation that would overwrite existing original data MUST provide an intelligible proposal stating the target, observed original identity/hash, source/version, candidate bytes/hash, excluded newer edits, preserved-original destination, storage required and affected related state. Approval MUST bind to those exact material inputs, not merely to a filename or general “fix” request. Immediately before modifying, revalidate target identity, content and authorization; a drifted target invalidates approval.

Candidate reconstruction MUST be isolated and verified. Before replacement, preserve **the original's exact existing bytes** in a protected incident location and verify the preservation. If that cannot be safely done, refuse in-place replacement or offer a separately approved non-destructive recovery destination. Guard against traversal, absolute paths, symlink/junction/reparse escapes, reserved names, case/Unicode collisions, device/special-file paths and unapproved destinations. Recovery metadata must never grant filesystem write authority by presenting a path.

Apply replacements through a documented crash-recoverable transaction with durable per-file and, where applicable, batch states. Do NOT claim an atomic several-file transaction merely because one rename is atomic. After installation, verify active bytes, IDs and relationships; record a new restoration revision linked to the historical source without pretending the prior damage never occurred. Durably protect the recovery event; promptly synchronize the affected mandatory Current JSON, queue affected Folder JSON reverification, and allow enabled Master JSON to follow its separate schedule, while truthfully reporting all outstanding synchronization. A bulk approval is a closed list; items that become unsafe can be skipped but new items may not be silently added. Partial results remain partial, not success.

If source integrity, keys, revision legitimacy, target control or sufficient storage cannot be established, safely refuse destructive repair and show supported comparison/export/investigation alternatives. Restoration respects legitimate deletion decisions and [PRIV-1](../6-%20Writing%20the%20Complete%20Master%20Plan/606-%20Documenting%20Data%20Security%20and%20Recovery.md#priv-1).

### 53.8. State reporting and technical implementation gates

Status MUST independently show durable original revision, mandatory per-file Current JSON freshness and verification, affected Folder JSON's last verified vs pending/conflict revision, enabled Master JSON revision/pending state, configured backup connectivity/versions/schedule, retirement holds, staging, recovery incidents and genuine unknown results. An optional ON toggle means user intent, **not evidence of completed verification**. Current JSON and Folder JSON must never be represented as user-disableable. An optional OFF feature cannot be represented as providing backup/global recovery; an unresolved folder conflict may not appear as a verified healthy latest revision.

Before production implementation or declaring this candidate ready for constitutional adoption, the App Plan and appropriate owner-authorized review MUST still resolve and verify: crash-durable edit protocol and multi-file consistency; physical snapshots and external-writer locking; per-platform paths and supported providers; NAS disconnections and partial writes; approval binding/expiry; exact-byte incident preservation and lawful retention; backup staging/publishing/retirement durability; capacity preflight; failure during cleanup; independent authenticity trust anchors where claimed; malicious filenames/paths and TOCTOU races; key access; deletion/privacy propagation; unattended worker lifecycle; and adversarial tests including power loss and partial recovery. Do not substitute a default implementation or assume these mechanisms have already been technically proven.

### 53.9. Candidate reconciliation ledger

| Existing RC4 rule | Candidate disposition (requires separate ratification) |
|---|---|
| INFO-1, SURVIVE-1, WORKSPACE-1/2/4 | Keep independently accessible originals and discoverability; explicitly expose mandatory Current/Folder JSON paths and independently optional Master JSON/backup; absence of \`master-data.json\` is acceptable when optional Master JSON is OFF. |
| JSON-1 through JSON-4 | Always-active per-file Current JSON literal copies, lightweight verified Folder JSON manifests, immediate affected-file sync initiation, and separately optional full Master JSON; truthful independent per-layer status, preservation of competing versions when review is required, highlighted per-hunk user reconciliation and JSON-first controlled recovery. |
| REV-1/REV-2 | Retain revision evidence and competing old/new contents when needed for conflict review; independent full external backup retained only if selected, with disclosed risks and no silent deletion on OFF. |
| BACKUP-1/BACKUP-2 | When a complete backup is ON or claimed, the full standalone scoped copy, completeness, verification, isolation limits and restoration evidence remain binding; with OFF, no fictional backup. |
| RECOVER-1, PRIV-1, NOFALL-2 | Preserve original bytes before approved replacement, block unsafe repair, respect lawful deletion, and distinguish approved recovery sources from forbidden implementation fallbacks. |
| WORKSPACE-TEST-1 and applicable TEST/DEV/GOV rules | Apply edge-case validation, independent adversarial reviews, evidence and exact-revision owner ratification before adoption or production promises. |

### 53.10. Folder JSON (Option B): verified manifest and status safety

The owner has selected **Option B** universally: Folder JSON is a mandatory verified inventory and consistency witness, **not a third physical copy of the file payloads**. Each applicable folder manifest MUST identify its own stable folder identity, directly retained child files, expected safe relative paths, file identities, declared size/type/hash and current revisions, corresponding per-file Current JSONs and their verified revisions, relevant relationships/deletion/move state and its own verification state. Child folder manifests are related by stable references, not embedded in a recursive envelope; appropriate manifest scopes must avoid recursion and preserve independent discoverability.

Each record/file's original and its complete literal Current JSON are two byte-reconstructible representations **within the same primary workspace failure domain**. If both are lost, a Folder JSON does NOT recover their contents. Enabled Master JSON or independent external backup may provide other actual sources at their disclosed verified revisions.

The verifier MUST preserve its last **Verified at revision R** published manifest while any new **Pending Verification at R+1** candidate is checked. On failure or conflict, do not advance the verified pointer or mislabel current bytes as verified. Source inspection uses actual bytes and trusted revision evidence, not solely a hash supplied by the suspect state; mere hash agreement cannot independently authenticate an adversarial edit. Deletion, rename and move require stable identities and coordinated old/new folder membership so an intentionally removed file is not silently resurrected. Files appearing while verification is running need a consistent revision boundary and fair rescheduling; ordinary edits do not cause whole-workspace rescans.

### 53.11. User-highlighted selective difference review and reconciliation

If old and new versions require **user reconciliation**—for example competing changes, ambiguous external edits, failed verification, conflicting revisions, or user-requested comparison—the application MUST compare available relevant verified *content*, not merely whole-file timestamps or names. **Only the added/new and removed/missing or replaced portions** should be highlighted by default; unchanged context is collapsed with optional expansion. Present accessible red/removed and green/added markings with text/icon labels, per-hunk scope, the old and current source identities/revisions, and a final result preview. This rule does NOT impose conflict popups after every ordinary authorized keystroke or routine save.

Where format semantics permit meaningful merging, the user MAY choose for each independent change **Keep Previous**, **Keep Current**, or **Keep Both**. Mixing choices is permitted: retain an old paragraph while accepting a newly added section elsewhere. Present an accurate merged preview **before** applying. For plain text, Markdown, code and suitable structured documents use bounded line-, word-, field- or block-level diffs appropriate to the format. For PDFs, images or other visual formats use a genuinely supported page/visual/structural comparison where available. Binary or unsupported formats MUST use a truthful file-version/size/hash/metadata comparison or separate-copy review; never invent line-level content or silently combine incompatible binary bytes.

Folder JSON alone never contains prior full-file text. The comparison MUST retrieve its old/new bytes from actual surviving originals, verified Current JSON revisions, appropriately retained historical content or other legitimate verified sources. A manifest/hash without bytes is not a restore point. **When review is required and both contents are available, preserve the competing original and last verified recoverable Current JSON revision during the unresolved decision** rather than immediately replacing the only old recoverable copy with new bytes. If the old content has already legitimately expired or is unavailable, show the limitation and do not fabricate a diff or promise a “Keep Previous” option. Retention follows privacy and authorized erasure duties; no immutable forever copies are implied.

The system MUST distinguish an intentional deletion from accidental loss, and a legitimate new revision from unexpected corruption. It MUST NOT auto-select whichever version is newest or assume a changed original is bad. User choices/approval bind to exact original/current candidate hashes, revision IDs, specific selected changes and approved output. If the file changes during the review, invalidate stale approval and recompare. A chosen result that would replace an existing original MUST be safely staged and validated, preserve that original's exact present bytes beforehand, commit through a crash-recoverable transaction, record provenance/new revision, synchronize **only the affected Current JSON** promptly and queue affected Folder JSON reverification. No unapproved expansion of changes, no silent destructive merge, and no general overwrite of unrelated files. Report partially resolved or uncertain states honestly.

### 53.12. Implementation gates and resource safeguards

“Immediately update Current JSON” means **begin or safely queue the affected-file synchronization promptly**, not promise that a very large original can always be fully re-encoded and published within five seconds. Do not rewrite unchanged Current JSONs, scan all other folders, or continuously re-encode a multi-gigabyte growing recording simply because the clock ticked. A published Current JSON remains a complete reconstructible payload even if construction uses memory-bounded streaming/staging and coalescing internally. Keep a durable honest original-file commit/recovery boundary that remains safe during Current JSON lag. The underlying storage medium can still fail and destroy the original and co-located JSON; optional physical independent backup addresses that separate failure class.

Before production implementation, the App Plan must resolve and actually test per-platform durable original writes, snapshot consistency while files grow, transaction journal semantics, last-verified-version preservation, collision/path/symlink security, long-running verification throttles, record/folder identity on move, external edits, legitimate deletion, privacy retention, missing revisions, binary diff limitations, insufficient staging capacity, interrupted build/replay, user approval staleness, trust anchors and safe background worker lifetime. Exact JSON names and logical object adaptations may vary per application **only** if all required outcomes and independently accessible file identities remain supported. This universal decision applies to all qualifying retained-data apps; Menemora is only an explanatory example. Neither this documentation change nor its publication itself migrates application data or implements runtime features.


**Historical integrity:** Changes in this candidate are proposed changes to RC4's normative text, not retroactive changes to the existing ratified RC4 commit or its independent reviews. The numeric rule-ID inventory remains stable for traceability; changed rule wording and applicability MUST receive fresh independent review. This candidate is explicitly **NOT RATIFIED**.
