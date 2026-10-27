<a id="core-1"></a>
### 6.4. CORE-1 — One shared Rust product core

**Type:** ECOSYSTEM POLICY | **Origin:** USER POLICY | **Applies:** products with multiple clients sharing domain or durable application behavior

Where technically practical, all clients of the same product MUST share the same Rust core for domain logic, canonical-state rules, data models, validation, synchronization, conflict semantics, migrations where applicable, authorization rules, AI capability enforcement, and durable application behavior. The goal is **one product truth, multiple clients**. Platform code may call into the core through suitable interfaces. Business logic MUST NOT be independently rewritten in Kotlin, Swift, TypeScript, or desktop frontend code merely because clients use different UI technologies.

This spans applicable Windows, macOS, Linux, Android, iOS, iPadOS, tablet, and web-associated native clients within the declared product scope. Neither UI strategy may independently alter canonical behavior; product behavior remains governed by the shared core and its documented technical exceptions.

Supported AI, native UI, web, CLI, and headless interfaces MUST operate on the same logical application state through shared core/domain contracts. They MUST NOT unknowingly maintain separate incompatible truths merely because the interface differs. Declared replicas and interface-specific presentation/preferences are allowed; canonical state and synchronization remain explicit under [DATA-1](#data-1) and [SYNC-1](#sync-1). Planning MUST ask whether a supported interface could disappear for years and return without conversion from a separate hidden interface-only truth. Legitimate version/schema migration may still be required.

Technical departures MUST document the affected component, concrete constraint, scope, and consistency implications under [LANG-1](#lang-1) and [GOV-3](#gov-3). A shared core may consist of cohesive feature modules and target-specific builds; it does not require one giant module, identical binaries, or one process. [ARCH-3](#arch-3)'s general duplication discretion does not override this product-core policy. Shared code does not establish trusted execution: enforce authority at the effective boundary under [AUTH-1](#auth-1), including service-side enforcement where clients are untrusted.

