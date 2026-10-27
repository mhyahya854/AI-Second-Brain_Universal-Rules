<a id="dev-16"></a>
### 31.16. DEV-16 — Lifetime growth envelope and maintenance validation

**Type:** ECOSYSTEM POLICY | **Origin:** USER POLICY | **Applies:** planning and verification where retained data, history, media, logs, indexes, or relationships may materially grow

The App Plan MUST define a reasonable expected lifetime growth envelope and its validation assumptions where scale affects architecture. Relevant dimensions may include records/files, storage/media volume, relationships, history/audit growth, devices, archive age, and users/accounts/tenants. State assumptions and limits so future humans or AI need not infer the intended workload. This is a planning envelope, not an indefinite capacity guarantee or universal numerical threshold.

Validation under [TEST-1](#test-1) MUST consider applicable ordinary and lifecycle operations at expected scale: startup, query/search, index rebuilding, backup, restore, migration, sync, recovery, export, integrity scans, and compaction/retention. The App Plan defines suitable resource/time budgets and supporting evidence, including limitations of estimates or representative samples. Tiny or inherently bounded applications may state that bound and its rationale without special scaling architecture or meaningless benchmarks.

