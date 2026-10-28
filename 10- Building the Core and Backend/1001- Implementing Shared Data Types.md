<a id="s08"></a>
## 8. Authority, derivation, and reproducibility

<a id="data-1"></a>
### 8.1. DATA-1 — Independent state dimensions

**Type:** UNIVERSAL INVARIANT | **Origin:** DERIVED ENGINEERING RULE | **Applies:** state whose authority or lifecycle matters

Applications MUST identify authoritative state and when other representations may be relied on or discarded. Authority, factual verification, provenance, ownership, reproducibility, retention value, recovery cost, sensitivity, and lifecycle MUST NOT be automatically treated as equivalent or inferred from one another without an explicit justified rule. Valid policy relationships between these dimensions are permitted; for example, sensitivity can inform retention and access policy. A generated document may be authoritative and valuable; canonical temporary state may expire. Distributed authority is permitted with defined semantics.

Storage technology does not determine authority: a vector database can hold authoritative originals and embeddings. An expendable cache must not hold the only copy of information promised preservation. Human edits or confirmation do not establish factual correctness of a whole record. Verification claims MUST identify the actual reviewed scope.

<a id="data-2"></a>
### 8.2. DATA-2 — Honest regeneration claims

**Type:** CONDITIONAL | **Origin:** DERIVED ENGINEERING RULE | **Applies:** artifacts claimed to be rebuildable through generation

Recovery MUST specify its target: identical bytes, semantic equivalence, equivalent functionality or quality, or an acceptable replacement. Exact reproduction claims require preserved dependencies and evidence. If exact artifact identity matters, preserve the artifact for its required lifecycle rather than relying on unproven regeneration.

Account for models, versions, seeds, external inputs, licenses, hardware behavior, cost, and availability where relevant. Non-reproducible outputs and expensive embeddings are not automatically disposable. Derived-state backup is permitted. Synchronous indexes/materialized views are permitted; derivation does not grant authority to mutate canonical records outside [AUTH-1](1007-%20Implementing%20Security%20and%20Authorization.md#auth-1).

Indexes, search/vector databases, embeddings, caches, previews, thumbnails, OCR indexes, materialized views, and generated reports/workbooks are often derived; their actual authority and retention follow [DATA-1](#data-1), not their names. Deleting a store declared rebuildable MUST NOT destroy the canonical information or retained dependencies needed for its declared rebuild contract. A derived artifact MUST NOT silently become the sole copy of irreplaceable information.

Editing a derived report, spreadsheet, index, dashboard, projection, cache, or generated view MUST NOT silently mutate canonical state. Supported bidirectional editing requires deliberately designed, validated adoption/import semantics under [EDIT-1](../12-%20Connecting%20and%20Completing%20the%20Application/1205-%20Connecting%20Complete%20Data%20Workflows.md#edit-1), [IO-1](1008-%20Implementing%20Required%20Core%20Capabilities.md#io-1), and [AUTH-1](1007-%20Implementing%20Security%20and%20Authorization.md#auth-1); a projection is not automatically a write authority.

