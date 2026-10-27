<a id="hermes-1"></a>
### 16.5. HERMES-1 — Optional, bounded intelligence

**Type:** ECOSYSTEM POLICY | **Origin:** USER POLICY | **Applies:** applications integrating Hermes

Hermes MUST remain an optional intelligence layer rather than the sole means of using the application. Core application behavior MUST work without Hermes. Hermes MUST NOT receive unrestricted raw authority over canonical state; canonical writes MUST pass through validated, authorized application operations under [AUTH-1](#auth-1) and [AI-1](#ai-1). Hermes SHOULD be able to operate locally where the relevant data and model are available. Optional Hermes capabilities do not redefine unrelated AI-native functions in [AI-4](#ai-4) as ordinary core functionality.

Approved application/core operations MUST enforce applicable deterministic validation and bounded authority; model-generated intent supplies neither approval nor validation. Retrieval MUST respect access scope and privacy; provenance and audit follow [AUDIT-1](#audit-1), [AUDIT-2](#audit-2), and [PRIV-1](#priv-1).

Hermes import/processing of untrusted file content MUST use the same deterministic intake/security gates as native UI operations under [IO-2](#io-2) and [IO-3](#io-3). Model size or provider grants no bypass of required malware checks, quarantine, or core validation.

Canonical data MUST NOT exist solely inside an opaque AI memory/vector database with no independent application access and preservation path. This concerns opacity and sole dependence on the intelligence layer, not a blanket ban on vector storage technology: authoritative originals may use such a backend under [DATA-1](#data-1), [LIFE-2](#life-2), and applicable storage/export contracts.

Hermes embeddings, vector stores, semantic indexes, generated summaries, and retrieval caches are normally navigation aids. They SHOULD be reconstructable from retained sources and appropriate deterministic metadata under the actual [DATA-2](#data-2) reproduction contract, without assuming bit-for-bit regeneration of nondeterministic summaries. They MUST NOT silently become the sole repository of irreplaceable information. An explicit, justified authoritative classification is permitted under [DATA-1](#data-1), with independent access, retention, and recovery obligations; it does not excuse opaque model-only preservation.

<a id="s23"></a>
## 23. Import and export

<a id="io-1"></a>
### 23.1. IO-1 — Controlled ingestion and faithful export

**Type:** CONDITIONAL | **Origin:** DERIVED ENGINEERING RULE | **Applies:** import/export capabilities

Imports MUST validate format/domain constraints, define identity/conflicts, and prevent blind overwrite contrary to intent. Staging, skip, audited replacement, merge, or alternatives may be used. Track needed provenance without unrelated sensitive content.

Externally supplied data MUST be treated as untrusted until processed according to the application's risk model. This includes applicable downloads, email attachments, documents/media, archives, office files, plugin packages, NAS content, sync peers, APIs, and removable media. Controls may include format/type/magic validation, safe-path/traversal checks, archive-depth/expansion and decompression-bomb limits, size/resource limits, active-content restrictions, staging/quarantine, scanning, and restricted parsing under [SEC-1](#sec-1). Harmless bounded values need no expensive scanning without meaningful benefit. Parsing success or location in a data tree does not grant execution trust. Locale/time interpretation follows [DATA-4](#data-4) and [DATA-5](#data-5).

Controlled intake SHOULD provide risk-appropriate inspection/staging, validation using the relevant controls above, duplicate/identity/provenance resolution, commit, and operation receipts where needed. These are applicable safeguards, not mandatory heavyweight quarantine or a fixed physical pipeline for every tiny input.

For externally supplied files, [IO-2](#io-2) defines the preferred logical Raw/Intake boundary; [IO-3](#io-3) governs applicable malware-verification state and [SEC-6](#sec-6) the replaceable local scanning capability.

Exports presented as copies MUST NOT silently mutate/delete sources. An intentional move or export-and-delete needs separate effect semantics and authority. Exports MUST document scope, omissions, transformations, consistency point, and format, distinguishing archival fidelity from presentation. Apply [PRIV-1](#priv-1).

A portable-exit claim MUST preserve the declared meaning, not merely copy bytes: applicable stable IDs, relationships, metadata, provenance, originals, annotations, history, and schema definitions may be needed. Disclose what the target format cannot represent; silently dropping meaning MUST NOT be called lossless export. An ordinary export is an output snapshot, not a new write authority. Editing it does not mutate canonical state without an explicit validated re-import/adoption operation under [EDIT-1](#edit-1).

Canonical snapshots, human-readable reports, interchange formats, and diagnostics are useful categories, not four required features. JSON, Markdown, CSV, documented databases, and open binary formats serve different purposes. Scheduled export is optional unless the selected preservation contract relies on it.

<a id="io-2"></a>
### 23.2. IO-2 — Untrusted Raw intake, promotion, and quarantine

**Type:** ECOSYSTEM POLICY | **Origin:** USER POLICY | **Applies:** applications ingesting, receiving, downloading, synchronizing, or otherwise accepting externally supplied file-like content

Such applications SHOULD expose a dedicated logical Raw/Intake/Staging area; `Raw/` is the preferred human-readable name where it fits the design. The boundary may be a directory, managed store, or equivalent logical state; no universal physical name or hierarchy is required. Content entering it MUST initially be untrusted regardless of location inside application-owned data. File-ingesting applications SHOULD prefer this boundary together with the local malware-intake pipeline in [IO-3](#io-3) and [SEC-6](#sec-6), proportionate to actual protection benefit. Applications without relevant file intake need no empty Raw directory, scanner, quarantine UI, or signature infrastructure.

Before promotion to ordinary managed/canonical content or risky normal processing, the required configured intake policy MUST succeed. Define relevant gates explicitly: malware verification, format/security validation, identity/provenance resolution, core validation, and authorized adoption under [IO-1](#io-1) and [AUTH-1](#auth-1). Not every input needs every step; isolated intake analysis is distinct from ordinary trusted processing. Pending, failed, stale, or unavailable verification MUST NOT silently satisfy a required gate. Bind promotion to the actual verified content/version and current applicable policy; intervening changes invalidate unsupported verdict reuse under [CON-1](#con-1).

A scanner detection alone MUST NOT automatically destroy retained source content. Quarantine/isolation SHOULD be the default response. Quarantined objects MUST NOT execute, receive ordinary trusted parsing, be automatically promoted, or be represented as clean canonical content. Authorized inspection/recovery may remain available through appropriate restricted mechanisms. Permanent deletion requires explicit policy/user authority or applicable security/privacy obligations under [PRIV-1](#priv-1) and [SAFE-2](#safe-2). A folder named `Quarantine/` is not sufficient isolation: the App Plan MUST choose risk-appropriate controls such as restricted access, non-executable storage, exclusion from normal import paths, renamed/encapsulated representation, or isolated storage.

Promotion need not delete the Raw original. Retained originals may support evidence, provenance, reproduction, or recovery under [DATA-3](#data-3), but remain subject to untrusted-content handling and retention/privacy policy. A derived canonical record does not authorize executing or reinterpreting its original, and canonical authority does not mean malware safety under [DATA-1](#data-1).

<a id="io-3"></a>
### 23.3. IO-3 — Incremental malware verification and visible scan state

**Type:** ECOSYSTEM POLICY | **Origin:** USER POLICY | **Applies:** applications with Raw/Intake malware-verification workflows

At each application start/open, every Raw/Intake object's malware-verification validity MUST be evaluated. Applications SHOULD automatically initiate this as a non-blocking background check, keeping normal UI startup responsive rather than waiting for full historical scans. Incremental inventory, trustworthy content/version evidence, bounded queues, backpressure, resumable work, and priority for new/unverified content SHOULD keep the workflow within [DEV-16](#dev-16)'s lifetime envelope. Evaluation may proceed incrementally in the background; objects whose required validity has not been established remain gated under [IO-2](#io-2).

Unchanged content need not be byte-rescanned on every launch. The App Plan MUST define verdict reuse, staleness, and rescan policy using relevant object identity, content hash or equivalent version evidence, size/version, scanner implementation/engine, signature database, policy version, scan time, and result. Do not rely on untrusted mutable metadata beyond its evidence contract. New or materially changed Raw objects SHOULD be queued promptly while running, without waiting for restart. Required scanning MUST precede risky normal processing; scanner work itself remains restricted under [SEC-1](#sec-1).

Use explicit states equivalent to **UNSCANNED, QUEUED, SCANNING, CLEAN, DETECTED, SUSPICIOUS, SCAN_FAILED, UNSUPPORTED, SIGNATURES_STALE, SCANNER_UNAVAILABLE, and QUARANTINED**, as relevant; exact labels and whether these are separate state dimensions may vary. Failure to scan MUST NOT equal clean. CLEAN means no threat detected under the recorded scanner/engine/signature/policy state, not guaranteed safety. Format validation, sandboxing, least privilege, resource limits, and active-content restrictions still apply. Scanner failure MUST NOT corrupt canonical state; expose failure/unavailability truthfully and support retry/recovery through the core's existing mutation contracts.

Unavailable scanning or signature updates MUST NOT unnecessarily disable independent local capabilities under [OFFLINE-3](#offline-3). Required intake gates remain enforced for affected content; degraded offline protection must be reported honestly rather than silently bypassed or represented as current.

Where a verdict controls processing/promotion, retain proportionate scan evidence bound to the relevant object/content: ID, hash/version, scanner/engine, signature/policy versions, timestamp, verdict, threat/signature name where detected, and failure reason where applicable. Receipts may reuse [OPS-1](#ops-1) and applicable audit records. Classify authority/retention under [DATA-1](#data-1) and [PRIV-1](#priv-1); transient progress is not automatically canonical, while evidence required for promotion must remain available for its declared lifecycle.

Signature-based scanning MUST distinguish current, stale, unavailable, and failed-update conditions, without presenting degraded state as full current protection. Support appropriate local database maintenance; for ClamAV, `freshclam` or an equivalent managed mechanism SHOULD update signatures without unnecessarily blocking normal startup. The App Plan MUST define freshness and risk-based rescanning after relevant changes, considering object risk, scan age, content changes, engine/signature/policy changes, threat intelligence, and performance. New signatures may invalidate prior confidence but do not universally require full-library rescans after every minor update. Signature delivery remains subject to [SEC-3](#sec-3)'s integrity/trust discipline.

Background scanning MUST expose appropriate non-blocking status in the relevant interface: progress/pending items, degraded protection, detection/quarantine, scanner unavailability, and completion. Desktop/mobile UI or headless structured health/progress may satisfy this; no literal bottom bar is prescribed. Routine success SHOULD stay unobtrusive, with proportionate prominence for detections, scan failures, unavailable scanners, materially stale signatures, and blocked/unverified content. Applicable accessibility follows [UI-3](#ui-3).

The App Plan MUST specify whether unscanned Raw content, quarantine state, and scan verdicts synchronize, whether receiving devices rescan, and how scanner/version differences affect trust. A remote CLEAN verdict MUST NOT become permanent universal trust without deliberate receiving-device policy; receivers may require local rescanning. [SYNC-1](#sync-1), [NAS-1](#nas-1), privacy, and containment rules still apply. Synchronization or preservation of untrusted bytes does not itself authorize promotion or ordinary processing.

