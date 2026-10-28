<a id="sec-4"></a>
### 25.4. SEC-4 — Vendored or forked foundation provenance

**Type:** ECOSYSTEM POLICY | **Origin:** USER POLICY | **Applies:** third-party source snapshots vendored or forked as meaningful application foundations

Projects MUST preserve durable provenance appropriate to the foundation: upstream project/repository, version/tag where applicable, exact commit/revision, source digest where appropriate, license/notices, import date, acquisition method, local modification boundary, and maintenance/update strategy. When source identifiers differ, record an equivalent exact snapshot identity rather than inventing a commit.

Explicitly decide whether the project tracks upstream, selectively merges changes, or owns a fixed independent fork/snapshot. Do not leave that maintenance responsibility ambiguous. This does not require vendoring dependencies; foundation evaluation follows [DEV-3](203-%20Researching%20Existing%20GitHub%20Projects.md#dev-3) and dependency safety follows [SEC-3](../3-%20Deciding%20the%20Stack/307-%20Choosing%20Libraries%20and%20Dependencies.md#sec-3).

