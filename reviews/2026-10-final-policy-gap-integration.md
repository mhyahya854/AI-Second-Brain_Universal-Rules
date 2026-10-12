# Final policy-gap integration and follow-up owner decisions

- Date: 2026-10-12 (owner/client date).
- Branch: `constitution/pre-ratification-working`.
- Verified starting HEAD: `cd06a629fb370b4c08684ec9470151c4d4ca88f8`.
- Starting working tree: clean; matched the owner's expected state.
- Candidate remains `1.0.0-working.1 — Pre-Ratification Working Candidate`, unratified and not frozen.
- Authority: the owner's “FINAL POLICY-GAP INTEGRATION BEFORE OWNER FREEZE REVIEW” and subsequent “FOLLOW-UP OWNER POLICY — UNIVERSAL TIMEZONE SEMANTICS AND MALWARE/DATA PROTECTION” instructions, supplied in this conversation and uploaded text.

Before editing, the complete constitution, README, CHANGELOG, latest development-governance report, and four-app integration report were read. All 94 starting normative rule IDs were confirmed present; the four-app Hermes/information-architecture blueprint was already integrated as candidate policy. No state discrepancy was found.

The preceding **read-only owner policy-completion gap review** in the conversation assessed A–V and recommended seven additions: reconstruction/dependency continuity, recovery without normal startup, lifetime growth, emergency maintenance, accessibility, locale semantics, and temporal semantics. That review did not create a repository report. This record summarizes its accepted dispositions and the owner's follow-up; it does not invent a historical review artifact or repeat that review. Historical reports remain unchanged and non-normative. Links below point to the constitution, which remains the normative source.

## Seven accepted decisions and necessity

| Decision / original prompt sections | Prior coverage and reason for the addition | Integrated disposition |
|---|---|---|
| Reconstruction and critical dependencies / 3–5 | SEC-3 addressed dependency discipline and LIFE-2/DEV-15 longevity, but not a complete supported-release reconstruction procedure or material disappearance-risk disposition. | New [SEC-5](../UNIVERSL%20RULES%20FOR%20ALL%20APPS.md#sec-5) covers supported/equivalent builds, applicable inputs/steps, dependency continuity, honest limits, and proportionate evidence; SEC-3 links to it. |
| Recovery without normal startup / 6–7 | Recovery, backup, and uncertainty rules existed, but a broken normal runtime could remain the sole information-access path. | Strengthened [RECOVER-1](../UNIVERSL%20RULES%20FOR%20ALL%20APPS.md#recover-1): appropriate independent recovery route, current authority, no forced CLI/separate executable, no fabricated validity. Existing EVID-1/DATA-2/SAFE-1 obligations are referenced. |
| Lifetime growth / 8–10 | General verification and workload contracts did not explicitly require planning decades of accumulated information or maintenance at that scale. | New [DEV-16](../UNIVERSL%20RULES%20FOR%20ALL%20APPS.md#dev-16): relevant growth dimensions, explicit assumptions, app-specific budgets, ordinary and lifecycle operation validation. |
| Emergency maintenance / 11–14 | SAFE-2 allowed containment, but planning/phase gates needed a concrete temporary procedure and reconciliation path. | New [DEV-17](../UNIVERSL%20RULES%20FOR%20ALL%20APPS.md#dev-17); DEV-5/10/13 cross-reference bounded repair, durable evidence, and reconciliation/conformance before features resume. |
| Accessible interaction / 15–17 | Platform/adaptive UI rules did not establish accessible workflow correctness or acceptance criteria. | New [UI-3](../UNIVERSL%20RULES%20FOR%20ALL%20APPS.md#ui-3), applicable across native/shared/web strategies and relevant administration/tooling. |
| Locale-independent meaning / 18–21 | PORT-2 covered filesystem/text differences and IO-1 fidelity, but interpretation could still depend on the reading device's locale. | New [DATA-4](../UNIVERSL%20RULES%20FOR%20ALL%20APPS.md#data-4): unambiguous values, parsing assumptions, source context, relevant text identity and matching semantics; IO-1 cross-reference. |
| Temporal meaning / 22–25 | Existing time-dependent contracts did not establish a coherent planning policy for materially distinct temporal concepts. | New [DATA-5](../UNIVERSL%20RULES%20FOR%20ALL%20APPS.md#data-5), strengthened by the follow-up to require timezone planning in every App Plan while retaining domain-specific, sometimes timezone-free representations. |

Original sections 26–27 feed these contracts into [DEV-7](../UNIVERSL%20RULES%20FOR%20ALL%20APPS.md#dev-7) for discoverable procedures, risks, criteria, and assumptions without hidden conversation or code inference. Sections 28–30 are implemented through existing families, cross-references, stable IDs, and no duplicate lifecycle systems. Sections 31–35 are addressed by the proportionality, reconciliation, validation, history, and status records below.

## Follow-Up Owner Decisions Integrated

| Follow-up sections | Disposition |
|---|---|
| 1–5 — Universal timezone planning | DATA-5 and DEV-7 require an explicit policy for every application, including logs, receipts, backups, security events, imports, sync, and diagnostics without scheduling. Define applicable representation/conversion/persistence/comparison/display/import/export/sync/migration semantics; preserve date-only/duration/monotonic meanings. Device/NAS/locale changes cannot reinterpret history. Offsets and zone-rule identities differ; rule changes, clock trust/skew, source time, and uncertainty are addressed proportionately. |
| 6–9 — Hostile inputs and parser isolation | [SEC-1](../UNIVERSL%20RULES%20FOR%20ALL%20APPS.md#sec-1) and [IO-1](../UNIVERSL%20RULES%20FOR%20ALL%20APPS.md#io-1) add defense in depth, untrusted-source treatment, risk-based parsing/path/archive/resource/active-content controls, minimum parser authority, and executable installation/activation trust distinct from data location. Antivirus is only a possible component. |
| 10–11 — Least privilege and blast radius | SEC-1 uses AUTH-1's existing capability boundary to constrain unnecessary archive/backup/secret/NAS/network access and assess compromise propagation across clients, plugins, parsers, optional subsystems, and AI tools. It disclaims perfect protection against a compromised OS/admin. |
| 12, 17 — Suspicious sync and containment | [SYNC-1](../UNIVERSL%20RULES%20FOR%20ALL%20APPS.md#sync-1) requires risk-based destructive/anomalous bulk-change policy for large retained datasets and an appropriate compromise-containment route. Signals need interpretation; no fixed thresholds or universal prompts. Validation/reconciliation precedes resumption. |
| 13–16 — Backup isolation, authority, and validation | [BACKUP-1](../UNIVERSL%20RULES%20FOR%20ALL%20APPS.md#backup-1) distinguishes replicas/hubs/history/backups, considers recovery copies outside ordinary-client/failure destruction, and separates deletion authority where meaningful. [BACKUP-2](../UNIVERSL%20RULES%20FOR%20ALL%20APPS.md#backup-2) requires an app-defined recoverability validation cadence for important retained data and evidence for recovery points; successful writes, checksums alone, age, or immutability are not proof of usable clean recovery. |
| 18 — Safe malware recovery | RECOVER-1 covers containment, propagation stop, evidenced recovery points, backup validation, canonical recovery, derived rebuild, safe reconciliation of newer information, necessary credential revocation/rotation, and validated resumption without overwriting best surviving clean evidence for convenience. |
| 19–20 — Supply chain and update integrity | [SEC-3](../UNIVERSL%20RULES%20FOR%20ALL%20APPS.md#sec-3) connects source/release integrity, controlled resolution, provenance, build/release authority, vulnerability response, and critical-change review to SEC-5. Automated updates verify authorization and integrity before execution; failed updates do not authorize destructive migration. |
| 21, 25 — Encryption and honest security limits | SEC-1 distinguishes storage protection from equivalent-authority malware in an unlocked session. Encryption and malware defenses complement rather than replace each other. No virus-proof, sandbox-proof, hash-proof, or clean-immutable-backup guarantee. |
| 22 — NAS recovery separation | [NAS-1](../UNIVERSL%20RULES%20FOR%20ALL%20APPS.md#nas-1) explicitly assesses hub compromise and independent/protected history or recovery; ordinary sync does not require unrestricted NAS administration. NAS modes remain distinct. |
| 23 — Hermes and malicious content | [AI-1](../UNIVERSL%20RULES%20FOR%20ALL%20APPS.md#ai-1) explicitly treats retrieved content as data, unable to override governing instructions, core validation, capabilities, authority, or data protection. Hermes stays a bounded client. |
| 24, 26–28 — Planning, proportionality, validation/report | DEV-7 references the security/recovery contracts rather than creating another parallel governance system. This report records combined coverage and verification. No final adversarial attack was initiated. |

## Rule governance and scope

New IDs: **UI-3, DATA-4, DATA-5, SEC-5, DEV-16, DEV-17**. Each is **ECOSYSTEM POLICY / USER POLICY / CANDIDATE**, with explicit applicability. Universal timezone planning is an intentional owner policy, not a claim that every temporal value has a timezone.

Existing rule bodies strengthened: **NAS-1, AI-1, SYNC-1, RECOVER-1, BACKUP-1, BACKUP-2, IO-1, SEC-1, SEC-3, DEV-5, DEV-7, DEV-10, DEV-13**. Existing IDs and type/origin classifications remain unchanged. This report records owner provenance for these amendments while retaining each existing rule family's classification. RECOVER-1's applicability now expressly includes recovery of important retained user state. The document date and section 30's current integration/next-action record are also updated.

## Proportionality and direct conflicts resolved

| Concern | Resolution |
|---|---|
| Rebuildability versus impossible forever guarantees | Supported/equivalent builds and explicit limits; no all-release archive, SBOM format, universal vendoring, permanent toolchains, or cloud build requirement. Preservation does not require executing obsolete vulnerable components. |
| Recovery versus extra infrastructure or authority bypass | Important retained state triggers the route; a documented format/reader can suffice. Authorization, keys, privacy, deletion, and actual restoration evidence remain required. Stateless tools need no rescue program. |
| Growth versus global benchmark bureaucracy | Material growth gets explicit app-specific envelopes/budgets and relevant lifecycle evidence; bounded tiny apps may state a concise bound. |
| Emergency work versus Plan Freeze/phase completion | Only necessary planning/approval steps may be deferred under actual emergency authority/prior delegation. Evidence, Project State, repair contract, and post-emergency three-layer reconciliation prevent permanent bypass. Ordinary bugfixes/features do not inherit emergency authority; weak models still cannot guess. |
| Accessibility versus identical/native-only UI | Outcome and acceptance criteria span native/shared/web implementations, with platform-appropriate mechanisms. No graphical controls for headless components unless a user-facing interface exists. |
| Locale safety versus mandatory translation/metadata | Only interpretation-relevant values require deliberate semantics; no every-language support, metadata on every string, or global normalization algorithm. |
| Original conditional time policy versus follow-up universal planning | The later owner decision governs: every App Plan states a timezone policy. Actual temporal structures depend on domain; absent operations may be stated concisely, without inventing scheduling or timezone-bearing dates/durations. |
| Hostile inputs versus enterprise scanning for tiny tools | Defenses follow retained-data value, attack surface, platform, and architecture. Scanning harmless bounded values without meaningful benefit is not required. No prescribed sandbox, scanner, thresholds, or enterprise ransomware subsystem. |
| Sync containment versus authorized bulk work/deletion | Anomalous patterns are signals, not proof; scoped authorization and legitimate erasure remain supported. Containment does not authorize indefinite retention or a universal fresh prompt. |
| NAS/backup protection versus one mandatory topology | Existing NAS modes, local operation, opt-in hub, and sync contracts remain. Document justified recovery isolation/residual risk; no global hosting or backup topology. |
| Security/recovery evidence versus privacy | Existing PRIV-1 and SEC-2 constrain retention, secrets, erasure, restored data, and diagnostics. Neither preserving clean evidence nor isolated backups grants indefinite payload retention. |
| New policies versus existing product architecture | Rust-first, shared core, feature-first, platform scopes/four Linux baselines, local/offline operation, storage/concurrency, canonical/derived meanings, portability, exceptions, and information architecture remain controlling. No new AI authority or hidden cloud dependency. |

The preceding review's already-covered topics were not turned into separate new rules: activation independence, feature-removal obligations, retained configuration migration, general plan drift, application self-description, migration-chain mechanism, binary/data rollback, optional-component degradation, plugin authority, general diagnostics/privacy, and hardware relocation. Existing uncertainty/corruption rules are reinforced through recovery cross-references, not a second repair system.

## Validation

Executed documentation checks:

- **PASS:** 493 local Markdown links across 12 Markdown files resolve, including fragments.
- **PASS:** 100 unique normative rule IDs, each with an anchor and type/origin/applicability metadata; 32 numbered sections and their explicit anchors remain intact.
- **PASS:** all 94 starting IDs and type/origin classifications remain; six new rules have ECOSYSTEM POLICY / USER POLICY classification and inherit CANDIDATE status.
- **PASS:** baseline rule-body comparison identifies exactly the 13 existing rules listed above as changed; other existing rule bodies remain unchanged. Leading/trailing separator whitespace is ignored in this comparison.
- **PASS:** all eight pre-existing review, ADR, and provenance files are byte-identical to starting HEAD. The rc1 branch remains at its reviewed revision, and the local origin/main tracking reference is unchanged.
- **PASS:** working version/status and the explicit owner-confirmation gate remain; current constitution/README retain integrated Hermes status. Pending-design mentions are confined to clearly historical records/entries. No new release candidate or ratification instruction was introduced.
- **PASS:** whitespace checks using `git diff --check` and `git diff --cached --check`, including the new report.

Direct integration checks, supported by targeted searches and comparison with the unchanged governing rules:

| Area | Result |
|---|---|
| Reconstruction/dependencies | PASS — supported/equivalent-build instructions, critical-risk dispositions, limits, and security constraints; no permanent cloud build or vulnerable-runtime retention requirement. |
| Recovery/growth | PASS — recovery without normal startup remains authorized and uncertainty-preserving; relevant lifetime maintenance operations have app-specific assumptions and evidence. No forced rescue executable or universal benchmark budget. |
| Emergency/conformance | PASS — scoped temporary repair, actual authority, durable record, Project State, and post-emergency three-layer gate; no ordinary feature or weak-model guessing bypass. |
| Accessibility/locale | PASS — applicable user workflow correctness across UI strategies; no identical UI or translation mandate; unambiguous durable/import/export semantics and deliberate text identity where material. |
| Time | PASS — every App Plan states timezone policy; date-only/duration/monotonic concepts are not falsely converted; device/NAS/locale changes cannot reinterpret history; offsets and zone-rule identities remain distinct; clock/rule uncertainty is explicit. |
| Hostile input/AI | PASS — defense in depth rather than antivirus alone; data location and retrieved instructions confer no executable or policy authority; parser privilege/isolation and compromise propagation are risk-scoped. |
| Sync/NAS/backup | PASS — suspicious bulk changes require an applicable policy; compromise containment precedes validated resumption; NAS sync is not independent backup; protected recovery copies and deletion authority are considered; restore validation is required at app-defined cadence. |
| Software delivery/security claims | PASS — automated update authorization/integrity precedes execution; failure does not authorize destructive migration; encryption and malware defenses address distinct threats; no perfect-containment claim. |
| Preserved governing contracts | PASS — additions align with Rust-first, cross-platform/four Linux baselines, local/offline operation, NAS roles, sync, privacy/erasure, AI authority, weak-model boundaries, exceptions, information architecture, canonical/derived distinctions, and portability. |
| Small-project scope | PASS — concise combined records remain valid; no mandatory SBOM, scanner, rescue program, scale benchmark, emergency process for every bugfix, headless GUI, per-string locale metadata, or complex temporal schema for every app. Universal timezone planning remains explicit even when concise. |

The repository defines no application build/runtime test suite. These structural checks and direct integration consistency checks do not certify application behavior, malware resistance, supported platforms, or every constitutional guarantee; this is not a hostile ratification review. The next owner policy-completion review was not performed.

## Repository changes and remaining action

- Modified: `UNIVERSL RULES FOR ALL APPS.md`, `README.md`, `CHANGELOG.md`.
- Created: this report.
- Existing historical reviews, ADR, and provenance remain byte-identical to the starting revision. Earlier pending-Hermes markers remain historical; the current blueprint stays integrated as candidate policy.
- Resulting local commit/HEAD and clean/dirty state are reported in the conversation; this avoids embedding a self-referential commit hash.
- No unrelated application was inspected. No push, merge, tag, ratification, freeze, release candidate, final adversarial attack, or next owner policy-completion review is part of this pass.

No specific unresolved universal-policy item identified. One final owner policy-completion review remains before Plan Freeze. The owner's explicit **“There is nothing else left to add.”** confirmation remains necessary before final candidate freeze and attack; ratification is a separate decision.

**SEVEN FINAL POLICY-GAP DECISIONS INTEGRATED AS CANDIDATE POLICY. NOT YET FROZEN. ONE FINAL OWNER POLICY-COMPLETION REVIEW REMAINS BEFORE THE FINAL ADVERSARIAL ATTACK.**
