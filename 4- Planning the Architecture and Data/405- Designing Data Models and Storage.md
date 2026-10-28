<a id="life-2"></a>
### 7.2. LIFE-2 — Long-term accessibility

**Type:** ECOSYSTEM POLICY | **Origin:** USER POLICY | **Applies:** information designated for long-term user retention

Applications MUST provide a practicable preservation and exit path beyond a particular runtime or vendor's lifetime, using documented formats, exports, readers, and recovery dependencies as appropriate. This does not require indefinite retention of expiring tokens or deleted content. Host bindings and secrets need an explicit portability/recovery strategy.

Where durable user information is retained, its lifecycle MUST be distinguished from replaceable application binaries, UI, AI/model providers, indexes, runtime state, and machines. Loss or replacement of one of those components MUST NOT automatically destroy or unnecessarily trap the retained information within disposable implementation state. Planning MUST ask: **Could the application implementation be replaced without unnecessarily destroying or trapping the user's retained information?** Recovery remains bounded by declared retention, portability, and dependency contracts, including [BACKUP-1](../16-%20Maintaining%20Updating%20and%20Recovering/1606-%20Testing%20Backup%20and%20Restoration.md#backup-1); this does not promise that every binary artifact is readable without software or that every failure is recoverable.

The goal is **maintenance-minimal**, not maintenance-zero: documented schemas, portable data, replaceable components, the shared Rust core, stable identities, migration discipline, explicit dependencies, tests, reproducible builds where applicable, rebuildable derived state, and durable planning context reduce future work. Applications MUST NOT promise that they work forever without maintenance without supportable evidence.

[SURVIVE-1](#survive-1)–[SURVIVE-2](../16-%20Maintaining%20Updating%20and%20Recovering/1606-%20Testing%20Backup%20and%20Restoration.md#survive-2) require an actually preserved independent representation and app-disappearance evidence, including mobile uninstall/container/key risks.

<a id="life-3"></a>
### 7.3. LIFE-3 — Logical storage separation

**Type:** RECOMMENDATION | **Origin:** ARCHITECTURAL DECISION | **Applies:** applications with multiple data lifecycles

Applications SHOULD distinguish replaceable code, retained data, configuration, generated artifacts, audit evidence, operational logs, backups, and exports. Directories, tables, object namespaces, or platform-managed stores may implement the distinction. Executables and data may be colocated if lifecycle operations preserve their contracts; for retained user-owned information, [WORKSPACE-1](#workspace-1) requires separation from disposable installation state and independently accessible preservation. Colocation cannot make that disposable state the only retained copy.

Roles such as `app/`, `data/`, `config/`, `derived/`, `audit/`, `cache/`, `logs/`, `backups/`, and `exports/` are illustrative. An export is not automatically disposable staging. Git may intentionally store canonical documents; it is not automatically a suitable database or independent backup. Prevent unintended inclusion in unrelated source repositories using suitable ignore rules, controls, and review; `.gitignore` is not an enforcement boundary.

<a id="info-2"></a>
### 32.2. INFO-2 — Discoverable workspace entry contract

**Type:** ECOSYSTEM POLICY | **Origin:** USER POLICY | **Applies:** substantial durable workspaces, including equivalent database/service-managed datasets

A workspace MUST expose a predictable logical entry point through which authorized deterministic software and suitably constrained AI can discover applicable workspace identity, schema/format version, major domains/collections, registered data roots, important catalogs/indexes, supported operations, migration/version state, relevant policy/configuration, and lineage where required.

A root manifest, workspace catalog, typed API, database schema plus discovery endpoint, or equivalent deterministic mechanism may implement this capability. The preferred physical entry pattern and technically necessary mapped adaptations for retained-data workspaces follow [WORKSPACE-4](#workspace-4). No public disclosure of private metadata/secrets is required. Discovery is subject to authorization; version handling follows [MIGRATE-2](../16-%20Maintaining%20Updating%20and%20Recovering/1605-%20Managing%20Data%20and%20Schema%20Migrations.md#migrate-2). Supported offline discovery and synchronization follow the existing local-first and sync contracts.

<a id="s36"></a>
## 36. Data that survives the application

<a id="survive-1"></a>
### 36.1. SURVIVE-1 — Independent retained information

**Type:** ECOSYSTEM POLICY | **Origin:** USER POLICY | **Applies:** retained user-owned information

Retained user-owned information **MUST NOT depend for its existence on the continued installation, availability, or development of the original application**. Provide an independently preserved, documented, practically recoverable representation outside disposable installation state. A format being open or a database being SQLite does not alone satisfy this requirement. The representation MUST be obtainable and recoverable without the original app within the declared retention and recovery contract, including relationships, identifiers, required originals, and interpretation dependencies.

The App Plan MUST document authoritative locations; ownership; actual engine and file formats; appropriate human-readable and machine-readable representations; schemas, identifiers, and relationships; export/import; access without the original app; uninstall behavior; mobile container deletion; encryption/key recovery; backup/restore; replacement/migration; retention/legitimate deletion; and offline, NAS, and synchronization responsibilities. SQL is a language, not a storage engine. SQLite, PostgreSQL, Markdown, HTML, original documents/media, and justified combinations may serve appropriate responsibilities. For retained user-owned information, the accessible workspace under [WORKSPACE-1](#workspace-1) remains required even when both optional protections are OFF. Every qualifying application MUST continuously support mandatory per-file complete Current JSON and verified per-folder Folder JSON manifests under [JSON-1](408-%20Planning%20Backup%20Migration%20and%20Recovery.md#json-1), with global Master JSON and external complete backup separately optional. Independently accessible originals, documentation, identity and access without the app remain required regardless of those optional settings; no format choice waives them. Stateless utilities retaining no user information need no such machinery.

A recoverable representation may be an independently accessible authoritative dataset or an independent recoverable copy. Declare when it becomes durable, what information it covers, its freshness and permitted recovery-point loss, and the dependencies and failure domains. Required preservation MUST be established and verified before claiming retained data is protected; an export button that has never produced an independent copy is insufficient. Recovery claims MUST disclose limits rather than promise immunity to all loss. Data preservation does not override authorized erasure, privacy obligations, or expiration under [PRIV-1](../6-%20Writing%20the%20Complete%20Master%20Plan/606-%20Documenting%20Data%20Security%20and%20Recovery.md#priv-1).

<a id="s45"></a>
## 45. User-owned data workspace and folder architecture

The information is the durable product; the application is a replaceable interface for accessing, interpreting, editing, and managing it. The following are owner policies for applicable retained-data applications, not requirements for stateless utilities retaining no user information. All new rules inherit CANDIDATE status under GOV-1.

<a id="workspace-1"></a>
### 45.1. WORKSPACE-1 — Independently accessible durable workspace

**Type:** ECOSYSTEM POLICY | **Origin:** USER POLICY | **Applies:** applications retaining user-owned information

<a id="workspace-access"></a>
#### 45.1.1. Independent access and physical adaptation

The App Plan MUST define one logical, discoverable, documented, independently accessible user-owned data workspace, separate from disposable application installation state. It SHOULD use a real user-accessible folder structure wherever the supported platform permits it. A technically necessary physical adaptation MUST document its mapping and preserve independent discovery, access and recovery outcomes; hidden opaque storage is not an equivalent substitute. Ordinary original documents/media and human-readable files MUST remain present and independently accessible within the supported storage/security contract. SQLite and other operational stores MAY serve appropriate responsibilities but MUST NOT replace the original independently accessible workspace, mandatory per-file Current JSON, verified Folder JSON or enabled optional full global Master JSON under [JSON-1](408-%20Planning%20Backup%20Migration%20and%20Recovery.md#json-1).

<a id="workspace-survival"></a>
#### 45.1.2. Planning priorities and platform survival

Planning MUST prioritize human comprehension, information preservation, independent recovery, clear folder relationships, deterministic machine navigation, safe AI operations, scalability, and long-term compatibility. Document access without the original application, schemas/readers, retention and key dependencies under [SURVIVE-1](#survive-1)–[SURVIVE-2](../16-%20Maintaining%20Updating%20and%20Recovering/1606-%20Testing%20Backup%20and%20Restoration.md#survive-2). An independently preserved recovery representation must actually survive the declared application-disappearance scenario; exposing app-private files through a picker or calling them external does not establish survival. Supported phone/provider access, permission persistence, offline availability and uninstall behavior MUST be researched and validated; arbitrary permanent filesystem access MUST NOT be promised for every phone or cloud service.

<a id="workspace-2"></a>
### 45.2. WORKSPACE-2 — Selected location, identity, movement, and reconnection

**Type:** ECOSYSTEM POLICY | **Origin:** USER POLICY | **Applies:** setup and lifecycle of retained-user-data workspaces

<a id="workspace-selection"></a>
#### 45.2.1. Setup and stable identity

Every applicable App Plan MUST identify where actual data lives. First setup MUST present the proposed persistent workspace location, major folder paths, settings, history, JSON and recovery locations, any data outside the workspace, and adoption of existing data for explicit user inspection and approval. The user MUST select or approve a suitable local folder or other supported storage arrangement and understand that Current JSON and Folder JSON are always-on parts of the app, then explicitly choose ON or OFF independently for optional Master JSON and Complete On-Site Backup; neither optional choice may be silently preselected. When backup is ON, the user MUST choose a separate validated backup destination, such as an external drive, NAS or other supported folder. These choices remain adjustable in Settings → Data Management under the safeguards of [section 53](408-%20Planning%20Backup%20Migration%20and%20Recovery.md#s53). Remember the approved location and stable workspace identity, and use it until a deliberate authorized change. The application MUST NOT silently change authoritative location or create a replacement empty workspace when the configured location is unavailable.

<a id="workspace-missing"></a>
#### 45.2.2. Missing location and damaged information

For an unavailable configured location, report **“Data location not found.”** Provide understandable reconnection steps and verify the candidate workspace's stable identity and contents before adoption. Distinguish missing/unreachable location, revoked permission, and damaged information; diagnostics must not claim corruption merely because access failed. For detected damage, report **“Data integrity issue detected.”** and investigate the mandatory Current JSON recovery source under [JSON-4](408-%20Planning%20Backup%20Migration%20and%20Recovery.md#json-4), checking its verified revision and genuine availability. Consider optional verified Master JSON and external backup only when actually present; never assume a stale, incomplete or absent representation can restore the requested bytes.

<a id="workspace-movement"></a>
#### 45.2.3. Verified movement and rebinding

Movement between folders, drives, devices, NAS, and supported cloud arrangements MUST have documented and verified migration/reconnection procedures. Prefer relative internal references with an explicit base; stable record identities MUST survive physical folder/name changes. Rebind host-specific paths deliberately, verify permissions/schema/identity/contents and reconcile pending/concurrent changes before adopting a relocated workspace. Document rollback and incomplete movement without silently declaring success. Respect [PORT-2](../3-%20Deciding%20the%20Stack/308-%20Checking%20Compatibility%20and%20Portability.md#port-2), [MIGRATE-1](../16-%20Maintaining%20Updating%20and%20Recovering/1605-%20Managing%20Data%20and%20Schema%20Migrations.md#migrate-1), and [SYNC-4](../12-%20Connecting%20and%20Completing%20the%20Application/1206-%20Integrating%20Offline%20and%20Sync%20Capabilities.md#sync-4).

<a id="workspace-4"></a>
### 45.4. WORKSPACE-4 — Human and machine entry documents

**Type:** ECOSYSTEM POLICY | **Origin:** USER POLICY | **Applies:** substantial retained-data workspaces and their independent discovery/recovery interfaces

<a id="workspace-entry-pattern"></a>
#### 45.4.1. Five discoverable entry responsibilities

The preferred human-facing filesystem entry pattern is the following four primary information documents, mandatory per-file Current JSON recovery files and verified per-folder Folder JSON manifests, plus a complete global recovery representation **only when Master JSON is enabled**. Physical adaptations MUST map all applicable responsibilities. Disabling Master JSON does not disable originals, per-file recovery or folder verification.

| Entry | Required responsibility |
|---|---|
| `00-START-HERE.md` | Plain-English, non-programmer guidance: what this workspace contains, where to begin, major folders, finding information, and recovery when the original application no longer exists. |
| `01-FOLDER-GUIDE.md` | Complete directory architecture, purposes, relationships, identity/navigation conventions and concrete examples; link each meaningful folder/file contract. |
| `02-DATA-DICTIONARY.md` | Actual formats, fields, relationships, IDs, provenance, timestamp meaning, schema/revision versions, encodings and recovery concepts/dependencies. |
| `catalog.json` | Validated navigable catalog resolving stable records to current logical locations through bounded machine retrieval; explicit authority, update/consistency policy, validation and reconstruction procedure. |
| `*.current.json` | **Mandatory** separate complete literal reconstructible payload per retained original file or justified equivalent persistent logical object. Actual names are App Plan-defined. |
| `folder.json` | **Mandatory** verified folder inventory, location, identity, expected revision/hash, relationships and verification state; no original-file payload duplication. |
| `master-data.json` | **Optional Master JSON ON:** one complete independent literal global recovery payload. OFF does not silently delete a previously verified representation. |

<a id="workspace-bootstrap"></a>
#### 45.4.2. Independent bootstrap and protected discovery

Documentation and recovery schemas MUST remain obtainable and usable without the original application or AI Skill. Catalog reconstruction and recovery discovery MUST not depend circularly on an intact catalog or global JSON: document bootstrap procedures using surviving individual records, protected history or independent recovery dependencies as appropriate. Routine AI retrieval uses bounded catalog/index interfaces, not full scans; authorized deterministic reconstruction may scan with declared costs. Private metadata and credentials remain protected under [AUTH-1](../10-%20Building%20the%20Core%20and%20Backend/1007-%20Implementing%20Security%20and%20Authorization.md#auth-1), [PRIV-1](../6-%20Writing%20the%20Complete%20Master%20Plan/606-%20Documenting%20Data%20Security%20and%20Recovery.md#priv-1) and [SEC-2](../9-%20Preparing%20the%20Development%20Environment/908-%20Establishing%20Permissions%20and%20Secrets.md#sec-2).

