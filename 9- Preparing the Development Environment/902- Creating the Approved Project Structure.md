<a id="blueprint-3"></a>
### 39.3. BLUEPRINT-3 — Feature-first code with real shared boundaries

**Type:** ECOSYSTEM POLICY | **Origin:** USER POLICY | **Applies:** substantial application codebases

Organize code primarily by meaningful feature/domain responsibility under [ARCH-1](../4-%20Planning%20the%20Architecture%20and%20Data/402-%20Dividing%20the%20Application%20Into%20Features.md#arch-1)–[ARCH-3](../4-%20Planning%20the%20Architecture%20and%20Data/404-%20Defining%20APIs%20and%20Interfaces.md#arch-3), with discoverable frontend and backend feature areas where their responsibilities exist. Examples such as Search, Collections, Import, and Settings illustrate feature names, not compulsory features. Shared areas MUST represent actual shared responsibilities; possible examples include motion/components/accessibility/design-system mechanisms and backend authorization/validation/error contracts.

Do not duplicate frontend/backend areas merely for visual symmetry, create a giant universal backend, or add unnecessary layers. The shared Rust core under [CORE-1](../4-%20Planning%20the%20Architecture%20and%20Data/403-%20Designing%20the%20Shared%20Core.md#core-1) may be composed of cohesive feature modules; feature-first organization does not authorize parallel product truths. Each boundary MUST have deliberate contracts and effective permissions. A feature MUST NOT bypass another feature's canonical-state, validation, or authorization invariants. Database schemas/migrations/storage implementation remain discoverable, independently of actual private data locations under [SURVIVE-2](../16-%20Maintaining%20Updating%20and%20Recovering/1606-%20Testing%20Backup%20and%20Restoration.md#survive-2).

