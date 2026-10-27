<a id="s50"></a>
## 50. Menemora illustration and Open Engineering Decisions — non-normative

This section preserves the owner's organizational example and explicitly unfinished decisions. It is not an implemented filesystem, universal feature list, approved saving algorithm, or additional normative rule set. The obligations governing applicable applications are in sections 45–49 and the retained foundation.

<a id="menemora-blueprint"></a>
### 50.1. Approved illustrative Menemora workspace

Menemora, a voice recording and transcription application, supplied the owner's concrete design context. The following is the exact illustrative hierarchy from the mission. Domain folder names do not become mandatory in unrelated applications.

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

<a id="menemora-records"></a>
#### 50.1.1. Recording-local information and identity

The recording folder demonstrates the WORKSPACE-3/INFO-3 relationship contract: its original audio, applicable transcript, notes, metadata and history are discoverable together. The owner's Menemora design keeps each recording's associated information discoverable from that recording's folder, rather than placing every recording's notes in an unrelated global Notes folder. `Interview_A7F2` illustrates a readable label with an identity cue; it does not prescribe a universal identifier algorithm. `recording.json` supplies full scoped recovery data under JSON-1, not merely paths to the audio and text beside it.

<a id="menemora-settings"></a>
#### 50.1.2. Settings and support responsibilities

In this illustration Settings contains settings, file-path configuration, exports, system support, search indexes, integrity, logs and recovery information. Under WORKSPACE-3/JSON-2 each receives its own purpose, authority and retention/rebuild classification. A search index is disposable only when its declared dependencies support rebuilding; retained settings, histories, relationships and meaningful logs remain recoverable. An integrity manifest is evidence for a defined trust model, not missing-file payload. Transactions and Verified-History require JSON-3's finite packaging boundaries and REV-2's independent protection: placing history in this folder alone supplies no access isolation or independent failure domain. An export's intended scope/lifecycle is explicit; its filename does not make it authoritative. Ordinary readable settings JSON is not an acceptable insecure credential store.

<a id="menemora-collections"></a>
#### 50.1.3. Optional Collections and feature scope

The owner leaves Collections optional and enableable/disableable through Settings. Disabling the feature does not itself authorize erasing existing collection information; deletion follows the existing authority/retention contract. A permanent root Collections folder is not required. The future App Plan selects metadata, references or justified folders, without unnecessarily duplicating original media for organizational views. This is distinct from required full JSON recovery duplication.

Transcription, transcript correction, AI summaries, audio processing, notes and other capabilities remain subject to Menemora's future App Plan. The example does not automatically authorize or require every suggested capability, implementation or access to a Menemora repository. A primary trusted Skill under WORKSPACE-AI-1 is separately discoverable; its omission from this exact illustrative tree does not waive that applicable contract or make editable workspace instructions authoritative.

<a id="open-engineering"></a>
### 50.2. Open Engineering Decisions

**Historical RC4 engineering context (superseded in the newer candidate only):** Topic 1's physical transaction protocol remains unfinished. The historical ratified RC4 revision must be read at its original commit, not inferred from this updated working document. The owner's newer locked candidate requires always-active complete per-file Current JSON and verified per-folder Folder JSON, while global Master JSON and external complete backup remain optional under [section 53](#s53). Other goals remain Git-inspired revision evidence, safe coordination, truthful acknowledgement, no silent data diminution and no hidden fallback. The following questions have no universal approved answer in this candidate. Entries are decision prompts, not selected requirements or permissions to deploy unfinished mechanisms.

| Open choice | Evidence and decision still needed |
|---|---|
| Acknowledgement timing | How edits can be durably acknowledged independently of completion of a large mandatory Current JSON, asynchronous Folder JSON, and optional Master JSON; define actual recovery point, caller-visible status and safe close boundary. Exact physical protocol is not yet selected. |
| Durable staging and commit format | Format, publication ordering, reader visibility, interruption handling and retained operation evidence across originals, mandatory Current JSON, verified Folder JSON, optional global Master JSON, catalog and history. A successful rename or database commit alone does not settle cross-artifact durability. |
| Write coordination protocol | Writer authority, stale-writer exclusion, concurrent/offline changes, conflict handling and evidence of valid committed revisions on actual supported backends. |
| Efficient enormous global updates | A complete-payload generation/update approach with measured lifetime I/O, memory, CPU, latency, temporary space and failure behavior. No references-only substitution is approved. |
| Universally required storage optimization | Whether any specific streaming, compression, snapshot, reflink, sparse or copy-on-write optimization should become mandatory; actual platform availability and recovery behavior remain to be established. |
| Device/NAS/cloud authoritative-copy topology | Placement and write authority for the one logical workspace, complete global representation, local working copies and protected history. Existing enabled-NAS hub and ordinary local-operation policies stay active; neither settles final universal write authority or requires every device to retain all content. |
| Rebuild, batching, compaction and capacity thresholds | Workload-specific thresholds, trigger behavior, retention preservation, resource accounting, incomplete-generation treatment and acceptance criteria. No numeric defaults are invented. |
| Universal timeout/retry budgets | Backend/workload timing, cancellation, uncertain outcomes, safe retries and measurable limits. The same-operation/replay safeguards remain active without a newly invented universal budget. |
| Exact history retention across apps | Domain-specific duration, protected generations, privacy/erasure, history growth, recovery points, independent access and finite reconstruction boundaries. No perpetual retention or universal generation count is selected. |

Material decisions return to the future research and authorized App Plan decision process under DEV-5/DEV-8/GOV-3 before affected implementation. Engineering choices already within delegated authority need no repeated request; unresolved owner policy cannot be inferred from an example. These open questions do not weaken mandatory per-file literal payload obligations or enabled optional global payload obligations. Research, prototypes and estimates remain evidence with stated limits, not approval or demonstrated production guarantees.

