<a id="blueprint-3"></a>
### 39.3. BLUEPRINT-3 — Feature-first code with real shared boundaries

**Type:** ECOSYSTEM POLICY | **Origin:** USER POLICY | **Applies:** substantial application codebases

Organize code primarily by meaningful feature/domain responsibility under [ARCH-1](#arch-1)–[ARCH-3](#arch-3), with discoverable frontend and backend feature areas where their responsibilities exist. Examples such as Search, Collections, Import, and Settings illustrate feature names, not compulsory features. Shared areas MUST represent actual shared responsibilities; possible examples include motion/components/accessibility/design-system mechanisms and backend authorization/validation/error contracts.

Do not duplicate frontend/backend areas merely for visual symmetry, create a giant universal backend, or add unnecessary layers. The shared Rust core under [CORE-1](#core-1) may be composed of cohesive feature modules; feature-first organization does not authorize parallel product truths. Each boundary MUST have deliberate contracts and effective permissions. A feature MUST NOT bypass another feature's canonical-state, validation, or authorization invariants. Database schemas/migrations/storage implementation remain discoverable, independently of actual private data locations under [SURVIVE-2](#survive-2).

