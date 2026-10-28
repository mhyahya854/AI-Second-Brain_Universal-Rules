<a id="doc-2"></a>
### 40.2. DOC-2 — Real relationship maps and synchronized documentation

**Type:** ECOSYSTEM POLICY | **Origin:** USER POLICY | **Applies:** implementation relationships, shared components, and changes affecting documented behavior

Maintain accurate `code-map.md`, `feature-map.md`, and `dependency-map.md` or mapped equivalents under `Codebase/Documentation/`, alongside relevant headers, function documentation, and precise source links. A shared motion module used by actual Search, Collections, Import, and Settings implementations MUST identify those verified consumers. Do not invent these consumers when the features do not exist.

Distinguish direct imports/calls, interface contracts, event paths, data dependencies, and indirect semantic effects. A backend operation that changes UI state does not by itself establish a direct dependency between a frontend animation module and that backend module; document the actual connection path. Use automated extraction/link checks where practical and explicitly record dynamic or semantic relationships that static analysis cannot prove. Relevant documentation MUST be updated during the same verified work that changes its truth. Phase verification MUST detect material documentation drift rather than accepting stale maps silently.

