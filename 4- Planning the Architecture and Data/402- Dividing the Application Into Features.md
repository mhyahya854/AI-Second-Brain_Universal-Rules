<a id="s06"></a>
## 6. Feature-first architecture, shared core, and UI

*Section 6 rules across lifecycle files: [ARCH-1](#arch-1), [ARCH-2](401-%20Designing%20the%20Application%20Architecture.md#arch-2), [ARCH-3](404-%20Defining%20APIs%20and%20Interfaces.md#arch-3), [CORE-1](403-%20Designing%20the%20Shared%20Core.md#core-1), [UI-1](../3-%20Deciding%20the%20Stack/305-%20Choosing%20Frontend%20Technologies.md#ui-1), [UI-2](../5-%20Designing%20the%20UI%20and%20UX/507-%20Designing%20Screens%20and%20Responsive%20Layouts.md#ui-2), [UI-3](../5-%20Designing%20the%20UI%20and%20UX/509-%20Applying%20Accessibility%20and%20Localization.md#ui-3), [UI-4](../5-%20Designing%20the%20UI%20and%20UX/501-%20Understanding%20the%20Desired%20Experience.md#ui-4), [UI-5](../5-%20Designing%20the%20UI%20and%20UX/506-%20Building%20the%20Design%20System.md#ui-5), [UI-6](../11-%20Building%20the%20Frontend/1106-%20Implementing%20Loading%20Empty%20and%20Error%20States.md#ui-6), [UI-7](../5-%20Designing%20the%20UI%20and%20UX/510-%20Reviewing%20and%20Approving%20the%20Design.md#ui-7).*

<a id="arch-1"></a>
### 6.1. ARCH-1 — Feature-first organization

**Type:** ECOSYSTEM POLICY | **Origin:** USER POLICY | **Applies:** applications with multiple meaningful user or domain capabilities

Feature-first organization is presumptive. Responsibility ownership, domain/capability boundaries, authoritative-state ownership, shared concepts, dependencies, and cross-boundary effects MUST be understandable and deliberate. A feature MUST NOT silently bypass another feature's applicable invariants. Policy departures require a scoped rationale and approval under [GOV-3](../0-%20Start%20Here%20and%20Universal%20Rules/003-%20Rule%20Priority%20and%20Authority.md#gov-3).

The detailed substantial-application default in [BLUEPRINT-1](../6-%20Writing%20the%20Complete%20Master%20Plan/608-%20Finalizing%20the%20Project%20Folder%20Structure.md#blueprint-1) prescribes discoverable planning/code responsibilities and a preferred physical layout, with justified engineering/framework adaptations. It does not impose one runtime user-data hierarchy. A tiny cohesive utility is outside the multi-capability trigger and may use the proportionate blueprint representation. Compiler passes, signal-processing pipelines, rendering engines, mathematical kernels, framework layers, hardware-oriented structures, and justified process boundaries are valid where appropriate. Mapped folder-name adaptations and justified fewer layers under that blueprint are not departures from feature-first policy.

