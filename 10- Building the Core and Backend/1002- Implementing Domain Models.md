<a id="data-3"></a>
### 8.3. DATA-3 — Originals, derivative lineage, and annotations

**Type:** ECOSYSTEM POLICY | **Origin:** USER POLICY | **Applies:** applications ingesting or preserving source artifacts and meaningful derivatives

Applications MUST distinguish preserved originals from extraction, normalization, transformation, interpretation, annotation, AI-generated derivatives, and canonical decisions where those roles exist. A searchable derivative MUST NOT silently replace a preserved original merely for convenience. Preservation follows the declared retention/privacy contract, not indefinite storage of every source.

Meaningful derivatives SHOULD retain proportionate lineage sufficient to identify their parent/source and relevant source version/hash, tool/version, model/version where applicable, creation time, method, and review/verification status. Not every field is needed for trivial artifacts, and uncertain model identity must remain uncertain. Material source changes MUST support invalidation, stale marking, regeneration, or review as appropriate rather than silently representing outdated derivatives as current. Lineage and its retention follow [EVID-1](../0-%20Start%20Here%20and%20Universal%20Rules/009-%20Evidence%20and%20Truthful%20Completion.md#evid-1) and [PRIV-1](../6-%20Writing%20the%20Complete%20Master%20Plan/606-%20Documenting%20Data%20Security%20and%20Recovery.md#priv-1).

Where originals are to be preserved, notes, highlights, comments, tags, review decisions, and AI annotations SHOULD normally be related overlays anchored to the original, rather than destructive alteration. Ordinary editable documents remain valid. Anchors and their source-context validity follow [INFO-4](#info-4).

<a id="info-3"></a>
### 32.3. INFO-3 — Durable identity, organization, and relationships

**Type:** ECOSYSTEM POLICY | **Origin:** USER POLICY | **Applies:** important durable logical objects whose identity must survive organization changes

Such objects MUST have durable product-owned logical identity or an equivalent documented identity contract independent of mutable filenames, display names, paths, categories, statuses, or UI locations. The product SHOULD resolve **stable identity → current location** where location applies. Ordinary renaming or movement between folders, collections, statuses, categories, and views MUST NOT unnecessarily create a new identity or destroy relationships, provenance, or retained history. Explicit copy/new-object and migration operations may have distinct documented identity semantics.

When an object participates in multiple views or relationships, prefer explicit references/relationships over uncontrolled canonical duplication. Canonical information SHOULD NOT be duplicated merely to appear in multiple organizational views when references preserve the same meaning safely. Deliberate replicas, snapshots, backups, and derivatives remain valid with declared authority and lifecycle. Mandatory literal per-file Current JSON duplication under [JSON-1](../4-%20Planning%20the%20Architecture%20and%20Data/408-%20Planning%20Backup%20Migration%20and%20Recovery.md#json-1) serves recovery, not organizational views; optional full global JSON adds another complete representation only when enabled. The Folder JSON is a verified manifest and MUST NOT replicate every file's payload. Anti-duplication preferences MUST NOT diminish the mandatory Current JSON or an enabled complete Master JSON. Where byte identity or deduplication matters, content hashes or equivalents may assist integrity, provenance, and tracking; content-addressing is not universally required, and byte equality is not automatically logical identity or authenticated origin.

<a id="info-4"></a>
### 32.4. INFO-4 — Precise sub-object addressing and source context

**Type:** ECOSYSTEM POLICY | **Origin:** USER POLICY | **Applies:** large or heterogeneous content where sub-object addressing materially improves retrieval, citation, annotation, or verification

Applications MUST support appropriate deterministic stable/bounded addressing where technically meaningful so a consumer can resolve **object → precise relevant region** without loading or reasoning over an entire huge object. Pages, sections, paragraphs, records, spreadsheet ranges, timestamps, transcript segments, media frames, image regions, and code symbols are examples, not required features or one universal anchor format.

Anchors to mutable content MUST retain enough source context to determine validity, such as source version/hash, surrounding-text hash, record revision, time/version relationship, or an equivalent mechanism. An old annotation/extraction MUST NOT silently attach to unrelated changed content. Stale, ambiguous, or unresolvable anchors require explicit status, revalidation, or a justified remapping operation. Source and derivative lineage follows [DATA-3](#data-3), while uncertainty follows [EVID-1](../0-%20Start%20Here%20and%20Universal%20Rules/009-%20Evidence%20and%20Truthful%20Completion.md#evid-1).

