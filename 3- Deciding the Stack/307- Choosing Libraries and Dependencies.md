<a id="sec-3"></a>
### 25.3. SEC-3 — Dependency and build discipline

**Type:** ECOSYSTEM POLICY | **Origin:** ARCHITECTURAL DECISION | **Applies:** released application builds and third-party dependencies

Released builds MUST record a reproducible dependency-resolution strategy appropriate to their toolchains, preserving integrity/trust checks. Library version ranges may coexist with reproducible test/release environments. Assess dependencies by function, provenance, maintenance, vulnerabilities, license, transitive cost, and replacement feasibility. Short handwritten security/parsing code is not inherently preferable.

Use supported lock/resolution mechanisms and review updates. `go.sum` records checksums; it alone is not an exact Go dependency lock model, which also involves `go.mod` and resolution semantics. Rust ownership checks and `Cargo.lock` do not establish trust. Vulnerability review SHOULD be proportionate and recurring; CVE scans cannot prove absence of defects.

Protect software delivery proportionately through dependency provenance, controlled resolution, source/release integrity verification, appropriately verifiable packages/updates, restricted build/release authority, vulnerability response, and review of critical third-party changes. No one signing system, SBOM format, package manager, or scanner is mandated. Automated updates MUST verify authorization and integrity before execution using an appropriate platform mechanism; arriving through the update path is not trust evidence by itself. Update failure MUST NOT silently authorize destructive data migration; [MIGRATE-1](#migrate-1) and [MIGRATE-2](#migrate-2) still apply. Reconstruction and material dependency-disappearance dispositions follow [SEC-5](#sec-5).

