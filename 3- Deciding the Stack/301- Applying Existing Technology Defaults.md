<a id="s35"></a>
## 35. Technology preferences after requirements

<a id="tech-1"></a>
### 35.1. TECH-1 — Requirements justify the selected stack

**Type:** ECOSYSTEM POLICY | **Origin:** USER POLICY | **Applies:** application and component technology selection

After requirements analysis, evaluate **Rust first for implementation, Tauri 2 first as an application framework, SQLite first when a database is appropriate, and open-source or public-domain solutions first across the relevant stack**. Prefer a feature-first modular monolith where suitable and practical resource efficiency. These preferences are strong starting points, not evidence of suitability. [LANG-1](303-%20Choosing%20Programming%20Languages.md#lang-1)'s Rust policy and [CORE-1](../4-%20Planning%20the%20Architecture%20and%20Data/403-%20Designing%20the%20Shared%20Core.md#core-1)'s shared product core remain controlling.

Concrete evidence of a substantial improvement in required functionality, reliability, platform compatibility, accessibility, maintainability, or user experience may justify another choice. Record affected components, alternatives, requirements, evidence, tradeoffs, and applicable approval under [GOV-3](../0-%20Start%20Here%20and%20Universal%20Rules/003-%20Rule%20Priority%20and%20Authority.md#gov-3). Popularity or fashion alone is insufficient. Avoid heavyweight technology without demonstrated benefit, and avoid lightweight choices that demonstrably harm essential usability or functionality. A database MUST NOT be introduced merely to satisfy a database preference when documented files meet the requirements better.

