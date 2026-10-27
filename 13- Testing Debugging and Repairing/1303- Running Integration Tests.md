<a id="test-2"></a>
### 27.2. TEST-2 — Practical verification patterns

**Type:** RECOMMENDATION | **Origin:** DERIVED ENGINEERING RULE | **Applies:** development/release verification choices

Automation SHOULD cover critical transitions, interfaces, interruption points, authority boundaries, and representative workflows. Examples: concurrent edits, stale lease holders, disconnect after commit before acknowledgement, audit/outbox recovery, deletion then restore, incompatible schemas, and revoked queued authority. Use actual targets where needed; an emulator cannot certify every NAS appliance.

A shared conformance harness MAY help inspect declared applicability, links, schemas, and selected guarantees. It SHOULD measure behavior rather than prescribed filenames. Destructive tests need isolated fixtures and scope; a documentation rule does not authorize inspection or mutation of unrelated applications.

