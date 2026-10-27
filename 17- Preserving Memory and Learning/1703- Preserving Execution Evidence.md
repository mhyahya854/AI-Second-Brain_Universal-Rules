<a id="dev-12"></a>
### 31.12. DEV-12 — Evidence-bearing Done Phases

**Type:** ECOSYSTEM POLICY | **Origin:** USER POLICY | **Applies:** phases that have passed the completion gate

A completed phase MUST be moved or recorded in discoverable Done Phases history, preserving the original specification or its immutable reference, actual implementation, deviations, relevant decisions, tests executed, outcomes, completion evidence, relevant commit/revision references, and remaining follow-ups. Update Project State with the result and next permitted action. A failed or unverified phase MUST NOT be represented as done.

Done Phases complements Git and other version history with understandable evidence; it neither replaces version control nor requires reconstructing completed work solely from commits. References may avoid duplicating large artifacts, provided the promised evidence remains accessible under its retention contract. Follow-ups MUST NOT conceal unresolved required acceptance criteria; approved exceptions are explicit.

For substantial tasks/phases, preserve execution evidence during work as well as at completion: what was attempted, what actually changed, validation performed, passed/failed outcomes, remaining uncertainty, and the containing revision/commit where relevant. Interrupted or failed work needs an accurate continuation record rather than a false Done entry. Project State points to this evidence; completion incorporates or references it in Done Phases without unnecessary duplication or a mandatory `Operations/` directory.

Evidence MAY include tests, builds, static checks, runtime validation, relevant screenshots, schemas, hashes, migration comparisons, commit IDs, and operation receipts as appropriate. Evidence supports the actual claim and the [Three-Layer Conformance Gate](#dev-13); its mere existence or a screenshot cannot establish unrelated guarantees.

Subphase evidence, verified ✅ heading markers, and parent phase completion additionally follow [EXEC-5](#exec-5); no marker precedes actual acceptance verification.

