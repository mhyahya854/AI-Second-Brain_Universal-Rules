# Universal Rules for All Apps — MASTER PLAN

> Version: **1.2.0-owner-approved-cross-application-candidate (unratified; built on RC4)**<br>
> Status: **OWNER-LOCKED NEW DESIGN — UNRATIFIED CONSTITUTIONAL AMENDMENT CANDIDATE; formal review and ratification remain separate**<br>
> RC4 integration started: 2026-10-17 UTC; resumed: 2026-10-18 UTC; historical rc3 consolidation: 2026-10-15 UTC<br>
> Document identifier: ECOSYSTEM-CONST-001<br>
> Source repository: https://github.com/mhyahya854/Universal-Rules<br>
> Policy and ratification authority: repository owner/user, unless explicitly delegated<br>
> RC4 baseline: `73b2e8adb0236af7d4e503e67f9d507148cc95b7`, MASTER_PLAN.md SHA-256 `07a0976686215cb68e4a0bf63d56aecfb9ec183e7946f84d4855f103fa110460`<br>
> Current integration baseline: `a635045e6561e3e803e6defb207a4bc8eb9a5026`, MASTER_PLAN.md SHA-256 `4aff994600790e48a4ddcacff500e8335f5ca715e2d59a25894c8fefa4e0d4ed`<br>
> Freeze identity and subsequent review results: revision-bound external receipt under section 42; never inferred from historical reviews

This single document contains the current candidate constitution, application planning/execution instructions, Green/Red/Fix procedure, historical preservation map, and technical research evidence. Its purpose is durable, user-owned, understandable, recoverable, portable, maintainable software with truthful evidence and bounded authority. It improves the probability of long-term usefulness without promising indefinite operation or flawless AI execution.

**Two different repository contracts:** the active **Universal Rules** tree contains exactly `MASTER_PLAN.md`. Future **application** repositories use the multi-folder planning and Codebase blueprint in [section 39](#s39). Application folders shown here are instructions for future products, not additional files in this constitutional repository. Git metadata is not a tracked constitutional file.

**NO FALLBACKS IN THE APP PLAN OR CODEBASE:** selected implementations fail honestly; [section 37](#s37) preserves explicit recovery, same-operation retries, independent local functionality, and deliberate platform/migration contracts without hidden substitution.

For the owner: start with [scope/authority](#s01), [ordered planning](#s34), [technology selection](#s35), [data survival](#s36), [visual direction](#s38), and [candidate status](#s30). For execution: use [future project entry points](#blueprint-1), [Project State and Continue](#exec-4), [numbered subphase contracts](#exec-2), and [completion gates](#exec-5). For constitutional review: use [GOV-5](#gov-5) and the complete [operating procedure](#s42). Rule anchors remain stable even when subsection numbers evolve.

<a id="contents"></a>
## 0. Navigation

1. [Scope and rule classification](#s01)
2. [Foundations and domain hazards](#s02)
3. [Definitions](#s03)
4. [Principals and delegation](#s04)
5. [Rust-first implementation](#s05)
6. [Feature-first architecture, shared core, and UI](#s06)
7. [Data lifecycle and application replacement](#s07)
8. [Authority, derivation, and reproducibility](#s08)
9. [Local and offline operation](#s09)
10. [Product platforms, portability, and visual assets](#s10)
11. [NAS support](#s11)
12. [Storage and crash consistency](#s12)
13. [Concurrency and conflict semantics](#s13)
14. [Operation outcomes and acknowledgements](#s14)
15. [Retries and deduplication](#s15)
16. [AI authority, tools, memory, and Hermes](#s16)
17. [Audit and provenance](#s17)
18. [Privacy, retention, and deletion](#s18)
19. [External editing and drift](#s19)
20. [Synchronization](#s20)
21. [Reversal and recovery](#s21)
22. [Backup and restoration](#s22)
23. [Import and export](#s23)
24. [Schema evolution and migrations](#s24)
25. [Security, secrets, and dependencies](#s25)
26. [Configuration, observability, and runtime lifecycle](#s26)
27. [Verification and evidence](#s27)
28. [Documentation, exceptions, and ratification](#s28)
29. [Anti-pattern index — non-normative](#s29)
30. [Candidate status and review continuation — non-normative](#s30)
31. [Application planning, continuity, and conformance](#s31)
32. [Universal Information Architecture Blueprint](#s32)
33. [Reusable Universal Agent Skills governance](#s33)
34. [Requirements-first planning and source reuse](#s34)
35. [Technology preferences after requirements](#s35)
36. [Data that survives the application](#s36)
37. [NO FALLBACKS in the App Plan or Codebase](#s37)
38. [Visual concepts, interaction modes, and named design guidance](#s38)
39. [Future application repository blueprint and feature organization](#s39)
40. [Beginner-readable implementation documentation and simplicity](#s40)
41. [Exact execution, limited repair, and evidence-bearing completion](#s41)
42. [Integrated constitutional operating procedure](#s42)
43. [Authorization provenance and historical preservation — non-normative](#s43)
44. [Technical factuality and source evidence — non-normative](#s44)
45. [User-owned data workspace and folder architecture](#s45)
46. [Mandatory per-file Current JSON, verified Folder JSON, optional global Master JSON](#s46)
47. [Revision integrity, external edits, and protected history](#s47)
48. [Trusted AI entry and bounded navigation](#s48)
49. [Workspace validation and lifetime feasibility](#s49)
50. [Menemora illustration and Open Engineering Decisions — non-normative](#s50)
51. [RC4 authority, reconciliation, and requirement coverage — non-normative](#s51)
52. [Historical Topic 2: Optional Dual-JSON Recovery and Complete On-Site Backup — superseded design record](#s52)
53. [Owner-locked Current/Folder JSON and cross-application candidate — unratified](#s53)

<a id="s01"></a>
## 1. Scope and rule classification

<a id="gov-1"></a>
### 1.1. GOV-1 — Interpretation and applicability

**Type:** ECOSYSTEM POLICY | **Origin:** USER POLICY | **Applies:** all ecosystem software and constitutional decisions

The scope includes applications, services, background processes, CLI tools, libraries, storage engines, synchronization components, AI tool servers, and development tools. Capability-specific requirements apply when the capability exists or its guarantee is claimed. A stateless formatter does not need a backup engine; an application without AI does not need AI tool tests. A missing capability is not an exception to a conditional rule, but a required ecosystem capability cannot be avoided merely by omitting it.

Each rule has a stable ID, type, origin, and applicability statement. Every rule in this version inherits **Ratification status: CANDIDATE**. A user-directed policy's inclusion does not ratify the entire candidate. Future revisions MUST record status separately from the other dimensions.

| Independent dimension | Values and meaning |
|---|---|
| Ratification status | RATIFIED, CANDIDATE, PROPOSED, DEPRECATED: adoption status, not technical certainty. |
| Rule type | UNIVERSAL INVARIANT, ECOSYSTEM POLICY, DEFAULT, CONDITIONAL, RECOMMENDATION, PROHIBITION. |
| Origin / provenance | USER POLICY, ARCHITECTURAL DECISION, DERIVED ENGINEERING RULE, EXTERNAL STANDARD / REQUIREMENT. An external origin needs an identified source and applicability; none is invented here. |
| Applicability | Relevant capabilities, resources, actors, and assumptions, recorded even when the type is CONDITIONAL. |
| Normative strength | MUST / MUST NOT: mandatory; SHOULD: default or recommendation; MAY: valid option. |

A UNIVERSAL INVARIANT expresses a language- and platform-independent outcome within its stated assumptions. ECOSYSTEM POLICY is an intentional choice, not a law of computer science. DEFAULT is presumptive architecture with a reasoned alternative path. CONDITIONAL is mandatory when its trigger holds. RECOMMENDATION is advice requiring no formal exception when declined. PROHIBITION forbids a sufficiently harmful pattern and requires extraordinary, explicit approval for an exception.

MUST describes candidate conformance, not proof of adoption. Examples, implementation notes, ADR rationale, and historical reviews add no normative obligations. Sections 3, 29, and 30 are interpretive or informative and defer to governing rules. Deviations and conflicts follow [GOV-3](#gov-3); approval cannot make an unsupported technical guarantee true.

This file is the single current constitutional source. Sections 34–41 integrate earlier owner decisions; they refine the named clauses rather than leaving superseded wording active. [Section 42](#s42) operationalizes GOV-3–GOV-5 without independent override authority. Sections 45–49 integrate the RC4 workspace candidate within its stated applicability. [Section 52](#s52) is a historical Topic 2 design record superseded by the owner-locked Current/Folder JSON candidate in [section 53](#s53). Section 53 and its explicit edits to earlier clauses are an unratified amendment candidate, not current ratified RC4 policy. Sections 50–51 contain non-normative examples, open decisions and coverage; sections 43–44 preserve historical provenance and research. External references are provenance, not missing operating instructions. When an actual contradiction remains, stop affected decisions and record it for authorized repair under GOV-3; do not silently select convenient wording. The constitution governs conformance; actual owner authority may amend policy or approve recorded scoped exceptions, while approval cannot make an unsupported engineering claim true.

<a id="s02"></a>
## 2. Foundations and domain hazards

<a id="safe-1"></a>
### 2.1. SAFE-1 — Integrity and truthful guarantees

**Type:** UNIVERSAL INVARIANT | **Origin:** DERIVED ENGINEERING RULE | **Applies:** operations and retained information governed by an application contract

Applications MUST protect retained user data according to declared integrity and lifecycle contracts and MUST NOT silently corrupt it or misrepresent known loss. Intentional loss, transformation, or deletion requires applicable authority and accurate semantics. Important operation outcomes MUST be truthful under [OUT-1](#out-1). Guarantees require appropriate evidence under [TEST-1](#test-1), with limits and uncertainty disclosed.

<a id="safe-2"></a>
### 2.2. SAFE-2 — Domain-aware hazard decisions

**Type:** UNIVERSAL INVARIANT | **Origin:** DERIVED ENGINEERING RULE | **Applies:** conflicts among safety, security, privacy, integrity, and operational obligations

Applications MUST identify material domain hazards and applicable obligations and resolve conflicts on that basis. A global ranking MUST NOT force data preservation when it creates greater human, physical, security, or privacy harm or defeats applicable erasure duties. Emergency shutdown, credential revocation, and containment can require intentional interruption or loss. Record consequential tradeoffs and residual risks proportionately.

Example: a hardware controller may stop an actuator before persisting telemetry; an archive may prioritize retention under a legitimate preservation duty. Neither priority becomes a universal ordering for other domains.

<a id="safe-3"></a>
### 2.3. SAFE-3 — Explicit, testable core behavior

**Type:** DEFAULT | **Origin:** DERIVED ENGINEERING RULE | **Applies:** domain logic and authoritative decisions

Domain logic SHOULD make inputs, constraints, and transitions explicit and testable. Isolate or record time, randomness, observations, and model outputs where needed for claimed reproducibility. Randomized algorithms and probabilistic domain functions are permitted. Deterministic code is not proof of correctness; total system determinism is not required. Effective enforcement follows [AUTH-1](#auth-1).

<a id="s03"></a>
## 3. Definitions

| Term | Meaning |
|---|---|
| Canonical state | Authoritative state for a defined system purpose. It can be false, disputed, imported, machine-observed, AI-generated, or jointly controlled; authority does not mean factual verification. |
| Derived artifact | An artifact produced from other inputs. Origin does not establish authority, reproducibility, disposability, or retention value. |
| Retained data | Information promised preservation for a defined purpose and lifecycle, which may include finite retention. |
| Principal | An identity or entity under whose authority an operation is permitted: owner, workspace owner, administrator, service account, or delegate. Data-subject rights can constrain authority without granting every operational permission. |
| Actor | The initiator: human UI/CLI, AI, automation, importer, sync worker, migration, recovery process, integration, or device event. |
| Mechanism | The interface, tool, protocol, scheduled path, or other route by which the operation arrives. |
| Delegation | Granted authority bounded by resources, effects, duration, conditions, and revocation semantics. |
| Authoritative mutation pathway | An execution path enforcing applicable authority and integrity constraints, consistency semantics, required evidence, and outcomes. It need not be one service or language. |
| Modular monolith | A cohesive application deployment with explicit internal modules; those modules do not provide the same isolation as protected processes. |
| NAS | A private storage/server environment accessed through one or more modes in [NAS-1](#nas-1), not synonymous with mounting raw database files. |
| Drift | A relevant change outside the expected mutation/synchronization path; detection does not establish authorship or malicious intent. |
| Atomicity | Indivisibility within a stated consistency boundary and observer model, distinct from durability and external completion. |
| Universal Rules repository | This constitutional repository, whose active tree contains only `MASTER_PLAN.md`; historical Git refs preserve earlier supporting files. |
| App Master Plan / App Plan / historical APP Plan | The authoritative intended product specification and its planning responsibility in a future application; the complete specification follows BLUEPRINT-2. “Master Plan” folder names do not refer to this constitution's one-file tree. |
| Phase / subphase | Ordered bounded implementation contract and its smaller executable contracts, with validation gates, evidence, and numerical order under EXEC-1–EXEC-5. |
| Frozen candidate | Exact committed document bytes bound to recorded owner freeze authority; its identifier/digest is recorded outside those bytes to avoid self-reference. Freeze is not ratification. |
| Review convergence | Revision-bound satisfaction of GOV-5's findings, validation, regression, and two consecutive independent clean-round conditions; not a guarantee of correctness. |
| Approved implementation | Deliberately selected capability implementation and declared platform/configuration contract; failure never silently authorizes an alternative under NOFALL-1. |

<a id="s04"></a>
## 4. Principals and delegation

<a id="auth-1"></a>
### 4.1. AUTH-1 — Effective authorization and integrity enforcement

**Type:** UNIVERSAL INVARIANT | **Origin:** DERIVED ENGINEERING RULE | **Applies:** effects subject to authorization or integrity constraints

Permissions, domain constraints, and effect limits MUST be enforced at a boundary callers cannot silently bypass within the declared threat model. Hidden UI controls and prompts alone are insufficient. Interfaces may differ in authentication, privileges, quotas, rate limits, confirmation, and scope; they MUST NOT introduce an unacknowledged bypass of applicable integrity constraints. Administrative operations need explicitly authorized semantics.

Enforcement can reside in functions, databases, services, sandboxes, operating-system boundaries, or combinations. An in-process convention does not establish protection against a malicious same-account process or host administrator.

<a id="auth-2"></a>
### 4.2. AUTH-2 — Ownership, delegation, and attribution

**Type:** UNIVERSAL INVARIANT | **Origin:** DERIVED ENGINEERING RULE | **Applies:** operations requiring authority or accountability

Applications MUST distinguish the relevant principal, actor, mechanism, and delegation. Machine ownership MUST NOT imply ownership of all data or unrestricted authority. Shared ownership, data-subject rights, administration, and tenant boundaries require explicit authority and conflict semantics.

Delegations MUST define relevant resources, allowed effects, duration or lifecycle, conditions, and revocation behavior. Accountability-required operations MUST be attributable to the extent supported by evidence; unknown or externally asserted identity MUST NOT be reported as verified. Queued and long-running actions MUST handle authority changes according to their delegation contract.

<a id="s05"></a>
## 5. Rust-first implementation

<a id="lang-1"></a>
### 5.1. LANG-1 — Rust as the mandatory ecosystem default

**Type:** ECOSYSTEM POLICY | **Origin:** USER POLICY | **Applies:** new software and components developed in this ecosystem

Rust is the presumptive language for applications, services, background processes, CLI tools, core libraries, storage engines, synchronization components, AI tool servers, and other software. A non-Rust selection MUST document why another language materially better meets the component's requirements and obtain applicable approval under [GOV-3](#gov-3). The burden of justification belongs to the deviation.

The question is: **What concrete technical requirement makes another language materially more appropriate for this component?**

Valid reasons include platform-required SDKs/languages; critical capabilities unavailable or impractical in Rust; host/plugin constraints; specialized scientific/ML ecosystems; interoperability/runtime constraints; deployment requirements; materially safer lifecycle or maintenance outcomes; and scripting, configuration, or generated glue where Rust adds disproportionate complexity without meaningful benefit.

Familiarity, habit, popularity, trendiness, tutorials, framework preference, avoiding Rust's learning curve, or faster personal prototyping are insufficient by themselves. Staffing, qualification, certification, expertise, long-term maintenance, and operational support can justify a deviation when tied to material lifecycle or safety risk.

The decision MUST identify the component, selected language, concrete reason Rust was rejected, why the alternative better meets requirements, and whether scope is one component or the whole application. Polyglot systems are permitted with deliberate, maintainable boundaries. Rust is especially preferred for canonical state, filesystem operations, synchronization, concurrency, long-running services, security boundaries, durable infrastructure, performance-sensitive work, AI capability enforcement, and domain operations.

This language-selection requirement governs authored implementation components. Importing a library or an FFI dependency written in another language does not by itself constitute authoring a new non-Rust application component; dependency and boundary responsibilities still apply. Generated bindings/code, SQL, configuration, shaders, schemas, platform resources, and frontend assets MUST be classified by their role rather than their file extension. They are not automatically separate application components requiring individual exceptions. Authored executable frontend or other implementation logic remains subject to this policy. A documented component-level or standing exception MAY cover related implementation artifacts within its approved scope; generated glue does not exempt independently authored domain logic. The shared product core follows [CORE-1](#core-1).

Rust does not establish domain correctness, storage durability, distributed consistency, safe FFI, secure architecture, or correct concurrency semantics. Those remain architectural responsibilities. This policy does not itself mandate rewriting existing applications. Rationale and examples: [ADR-0001](https://github.com/mhyahya854/Universal-Rules/blob/a9c597c8f14536a4404a64494cf56e9015e1288a/decisions/ADR-0001-rust-first.md).

<a id="s06"></a>
## 6. Feature-first architecture, shared core, and UI

<a id="arch-1"></a>
### 6.1. ARCH-1 — Feature-first organization

**Type:** ECOSYSTEM POLICY | **Origin:** USER POLICY | **Applies:** applications with multiple meaningful user or domain capabilities

Feature-first organization is presumptive. Responsibility ownership, domain/capability boundaries, authoritative-state ownership, shared concepts, dependencies, and cross-boundary effects MUST be understandable and deliberate. A feature MUST NOT silently bypass another feature's applicable invariants. Policy departures require a scoped rationale and approval under [GOV-3](#gov-3).

The detailed substantial-application default in [BLUEPRINT-1](#blueprint-1) prescribes discoverable planning/code responsibilities and a preferred physical layout, with justified engineering/framework adaptations. It does not impose one runtime user-data hierarchy. A tiny cohesive utility is outside the multi-capability trigger and may use the proportionate blueprint representation. Compiler passes, signal-processing pipelines, rendering engines, mathematical kernels, framework layers, hardware-oriented structures, and justified process boundaries are valid where appropriate. Mapped folder-name adaptations and justified fewer layers under that blueprint are not departures from feature-first policy.

<a id="arch-2"></a>
### 6.2. ARCH-2 — Modular monolith by default

**Type:** DEFAULT | **Origin:** USER POLICY | **Applies:** ordinary feature-rich application deployment

A modular monolith SHOULD be preferred when it is the simplest design satisfying isolation, reliability, privilege boundaries, scaling, deployment, lifecycle, maintainability, and performance. Multiple processes/services may be justified by fault containment, plugin isolation, runtime incompatibility, independent lifecycle, hardware placement, operational economics, reliability, or scaling. Record the rationale; literal single-process impossibility is not required. Distribution adds network, transaction, deployment, and recovery responsibilities.

<a id="arch-3"></a>
### 6.3. ARCH-3 — Contracts and shared code

**Type:** DEFAULT | **Origin:** ARCHITECTURAL DECISION | **Applies:** modular codebases

Modules SHOULD communicate through explicit interfaces and avoid unnecessary dependency cycles. Build-time cycles and runtime conversations differ. Shared code SHOULD have cohesive responsibility and ownership; substantial shared domain kernels may be appropriate. Choose duplication or reuse by consistency needs and change coupling, not line counts or folder names.

Examples: typed application functions, query ports, commands, events, actor messages, callbacks, streams, and plugin protocols. A feature may contain domain logic, adapters, presentation, tests, and documentation without needing every category. An event bus can conceal coupling and does not by itself prove modularity.

<a id="core-1"></a>
### 6.4. CORE-1 — One shared Rust product core

**Type:** ECOSYSTEM POLICY | **Origin:** USER POLICY | **Applies:** products with multiple clients sharing domain or durable application behavior

Where technically practical, all clients of the same product MUST share the same Rust core for domain logic, canonical-state rules, data models, validation, synchronization, conflict semantics, migrations where applicable, authorization rules, AI capability enforcement, and durable application behavior. The goal is **one product truth, multiple clients**. Platform code may call into the core through suitable interfaces. Business logic MUST NOT be independently rewritten in Kotlin, Swift, TypeScript, or desktop frontend code merely because clients use different UI technologies.

This spans applicable Windows, macOS, Linux, Android, iOS, iPadOS, tablet, and web-associated native clients within the declared product scope. Neither UI strategy may independently alter canonical behavior; product behavior remains governed by the shared core and its documented technical exceptions.

Supported AI, native UI, web, CLI, and headless interfaces MUST operate on the same logical application state through shared core/domain contracts. They MUST NOT unknowingly maintain separate incompatible truths merely because the interface differs. Declared replicas and interface-specific presentation/preferences are allowed; canonical state and synchronization remain explicit under [DATA-1](#data-1) and [SYNC-1](#sync-1). Planning MUST ask whether a supported interface could disappear for years and return without conversion from a separate hidden interface-only truth. Legitimate version/schema migration may still be required.

Technical departures MUST document the affected component, concrete constraint, scope, and consistency implications under [LANG-1](#lang-1) and [GOV-3](#gov-3). A shared core may consist of cohesive feature modules and target-specific builds; it does not require one giant module, identical binaries, or one process. [ARCH-3](#arch-3)'s general duplication discretion does not override this product-core policy. Shared code does not establish trusted execution: enforce authority at the effective boundary under [AUTH-1](#auth-1), including service-side enforcement where clients are untrusted.

<a id="ui-1"></a>
### 6.5. UI-1 — Platform-appropriate or shared UI

**Type:** ECOSYSTEM POLICY | **Origin:** USER POLICY | **Applies:** products with user interfaces across platform scopes

Products MUST evaluate platform-appropriate native-appearing interfaces and deliberately shared/custom cross-platform interfaces against actual workflow, accessibility, platform integration, design fidelity, performance, and maintenance requirements. Preserve product identity, appropriate visual consistency, and applicable capabilities. Android-native UI technologies, Swift/SwiftUI on Apple platforms, and suitable desktop technologies are valid choices. Non-Rust platform UI components may meet [LANG-1](#lang-1)'s technical exception criteria; record the component or standing exception without treating it as permission to duplicate core behavior.

A shared cross-platform UI is a first-class compliant architecture and needs no exception merely for sharing presentation. Select native, shared/custom, or a justified hybrid through the documented comparison under [TECH-3](#tech-3), rather than imposing one presentation strategy by default. The implementation language still follows [LANG-1](#lang-1), and both strategies preserve the shared Rust core under [CORE-1](#core-1). Platform-specific essential behavior and accessibility remain mandatory.

<a id="ui-2"></a>
### 6.6. UI-2 — Reuse priorities and adaptive presentation

**Type:** ECOSYSTEM POLICY | **Origin:** USER POLICY | **Applies:** products spanning device sizes or platform interaction models

Products MUST share core logic under [CORE-1](#core-1), SHOULD share UI when beneficial, and MUST NOT sacrifice a materially better platform experience merely to maximize UI code reuse. Cross-platform does not mean identical presentation. Navigation, layouts, windowing, gestures, keyboard behavior, menus, share interfaces, and platform integrations may differ while representing the same underlying product and data. Phone and tablet interfaces MUST adapt to their interaction and layout needs rather than simply stretching a phone interface onto a tablet.

<a id="ui-3"></a>
### 6.7. UI-3 — Accessible interaction as product correctness

**Type:** ECOSYSTEM POLICY | **Origin:** USER POLICY | **Applies:** user-facing capabilities, including administration and tooling interfaces where exposed

Important supported workflows MUST provide reasonable accessible interaction appropriate to the target platform and interaction model. The App Plan MUST identify applicable accessibility acceptance criteria and relevant platform/industry standards, considering keyboard or other non-pointer operation, semantic controls, assistive technology, text scaling, visible/readable focus, contrast, reduced motion, and alternative interaction where relevant. Accessibility is part of product correctness, not merely optional visual polish; validate applicable workflows under [TEST-1](#test-1).

Native, shared cross-platform, and web UIs retain this outcome while adapting mechanisms and presentation under [UI-1](#ui-1) and [UI-2](#ui-2). No single accessibility standard or identical UI is universally required. Headless libraries, background daemons, and machine-facing APIs need no graphical accessibility controls; any user-facing administration or tooling is assessed on its own applicable interactions.

Accessibility MUST be considered from relevant wireframe, component, interaction/state, and design-system decisions, not deferred entirely to final polish. Applicable criteria SHOULD address accessible names, focus order/visibility, screen-reader structure, target size, dragging alternatives, and non-color-only meaning. Use current platform/industry guidance and WCAG/APG where applicable without imposing web mechanisms on native/headless software.

<a id="ui-4"></a>
### 6.8. UI-4 — Deliberate design brief, identity, and generic-aesthetic review

**Type:** ECOSYSTEM POLICY | **Origin:** USER POLICY | **Applies:** substantial user-facing interfaces before implementation and at design/completion review

Before substantial UI implementation, the App Plan MUST include or reference an explicit design brief and intentional visual/interaction direction rather than leaving identity to a coding model or framework defaults. Address relevant users, purpose, primary workflows, platform, information density, visual personality, tone, accessibility, interaction model, navigation philosophy, references, anti-references, intended emotional impression, and platform conventions. Tiny utilities with trivial interfaces need no extensive design dossier. UI governance applies to either presentation strategy in [UI-1](#ui-1).

Substantial interfaces MUST demonstrate coherent product-specific decisions about typography, color, spacing/density, geometry/radii/borders, elevation/shadows, iconography/illustrations, motion, layout/imagery/surfaces, navigation, and controls where relevant. The design must explain why this product looks and behaves this way; “the AI generated it” is insufficient. AI-generated work MUST NOT be accepted merely because it functions, looks clean/modern, or responds to viewport changes. **AI convenience must not become visual identity.** Every major dashboard, chart, panel, sidebar, analytics area, or AI interaction MUST have a product purpose; do not manufacture complexity to resemble common generated applications. AI capability requires no permanent chat sidebar, sparkle button, or generic AI aesthetic: contextual, command-based, invoked, workflow-integrated, or external Hermes interaction may fit.

An explicit **AI-Slop / Generic-Aesthetic Review** MUST evaluate the composition as a whole against the brief and product workflows. Review signals include combinations of:

| Signal group | Examples requiring product-specific reasoning when present |
|---|---|
| Color and surfaces | Unexplained purple/blue/cyan or startup-style gradients, gradient text, indiscriminate glassmorphism/backdrop blur, glowing borders, excessive soft shadows. |
| Typography and hierarchy | Unexamined Inter/Roboto/system-sans defaults, oversized centered marketing headlines, interchangeable SaaS heroes, hierarchy dictated by fashion rather than product importance. |
| Layout and geometry | Repetitive three-card layouts, identical rounded-card grids, nested cards, excessive pills/buttons/chips/tags/rounded rectangles or borders, fashionable bento layouts, unnecessary floating cards, domain-independent dashboards, huge empty whitespace reducing useful density. |
| Decorative symbolism | Generic thin-line icons everywhere, decorative blobs, random dot grids, purposeless noise textures, sparkles or generic AI stars/wands. |
| Motion and copy | Arbitrary micro-animation, excessive hover motion or meaningless bouncing/scaling; interchangeable copy such as “Unlock the power of…”, “Transform the way you…”, “Elevate your workflow…”, or “Supercharge your…”. |

These are contextual review signals, not prohibited primitives. Gradients, purple, cards, rounded corners, glass, shadows, familiar fonts, and other techniques remain valid when deliberately chosen, coherent, useful, accessible, and consistent with the design system. Superficially changing a purple gradient to green while leaving an unjustified generic SaaS composition intact MUST NOT count as product-specific design. Review evidence MUST explain relevant decisions and observed workflow/hierarchy suitability rather than merely check off banned-looking features or claim visual uniqueness.

The brief MUST connect relevant differentiation under [DEV-18](#dev-18), use context, and content tone to user flows and information priority before decoration: immediate/secondary information, primary/detail/contextual views, progressive disclosure, and competing attention. Complex interfaces SHOULD reason through low-fidelity sketches, text/ASCII wireframes, navigation maps, mockups, or interaction flows first. One-shot AI output is an exploration prototype, not automatic finished design. Develop appropriate drafts, subtract unnecessary effects/containers/labels/chrome, choose concrete art direction, then establish actual flows, systems, states, accessibility, and real-content behavior. Vague “modern”, “premium”, “sleek”, or “less AI” adjectives are insufficient final specifications.

Every generic-aesthetic review MUST ask what can be removed. Also inspect reflexive badge/H1/dual-CTA heroes, exactly three feature cards, identical icon boxes, thin gray borders or colored left edges everywhere, permanent sidebars/floating AI buttons, arbitrary stagger/fade/hover-scale, and dark mode chosen by reflex. Invented metrics, testimonials, and social proof MUST NOT be presented as genuine evidence under [EVID-1](#evid-1). The logo-swap question SHOULD test whether workflow, information architecture, typography, hierarchy, layout, content, and interaction could belong to many unrelated products; it is a heuristic, not proof or a requirement for novelty that harms usability.

Additional **avoid-by-default review signals**, not prohibited primitives, include decorative colored stripes on cards or panels; gratuitous borders, noise and textures; all-capital eyebrow labels above every heading; meaningless badges, status dots or labels; noun-heavy inflated headings; emojis or generic icons used instead of relevant authentic avatars, logos or photographs; overcrowded screens without clear priority; metaphors needing lengthy labels to explain them; static text-only mockups presented as working software; uniform radii, shadows and card treatments regardless of hierarchy; low-contrast gray text on white; motion without communicative or functional purpose; heavy hero animation or spectacle; default purple gradients, neon glows and dark gridline backgrounds; unverifiable testimonials, metrics, avatars or other fabricated social proof; and generic glass cards or reflexive decorative presentation. An intentional, accessible and product-appropriate use may be justified by the brief and actual workflow.

Demonstrations and completion evidence MUST represent actual implemented behavior honestly. Text-only mockups, static screenshots and nonfunctional prototypes MAY support exploration, but MUST NOT be described as a working demonstration, completed feature or launch-ready application; label placeholders and simulated behavior clearly. Applicable launch-readiness claims require tested representative real workflows and the release/platform evidence in [TEST-1](#test-1), not presentation polish alone.

References from software/screenshots/platforms, design systems, print, architecture, photography, physical products, typography, moodboards, or historical UI MAY inform composition, rhythm, hierarchy, interaction, and density. References do not authorize copying proprietary work. Prefer owner-created, properly licensed/open resources, public standards, and original design, preserving relevant provenance. Art-direction dials such as variance, motion intensity, or density MAY clarify the brief; no third-party numerical default becomes universal policy.

<a id="ui-5"></a>
### 6.9. UI-5 — Coherent design system and purposeful presentation

**Type:** ECOSYSTEM POLICY | **Origin:** USER POLICY | **Applies:** substantial user-facing applications and supported themes/platform presentations

Applications MUST define a reusable design system or equivalent coherent design contract for relevant typography, sizes/weights/line heights, spacing/grid/rhythm, colors/surfaces, borders/radii, elevation/shadows, icons, motion, focus, interaction states, and responsive behavior. Do not improvise these independently per screen. Semantic design tokens SHOULD represent reusable visual constants where practical; names such as `surface.primary`, `text.muted`, `action.primary`, `status.error`, `space.1`, or `motion.quick` are examples, not universal naming. Equivalent controls SHOULD share semantic behavior for primary/destructive actions, modal dismissal, validation, search, selection, navigation, and notifications instead of arbitrary conventions for novelty.

Color balance MUST follow the application's actual hierarchy, content, semantic states, and accessibility needs rather than a prescribed aesthetic ratio or formula. Deliberately identify base/supporting surfaces and emphasis where useful. Semantic error/danger/warning/success/information/focus/selection communication and accessibility MUST take precedence over decorative balance. Primary accent SHOULD retain meaning rather than indiscriminately color every icon, heading, card, border, and control. The product-specific direction and owner preferences follow [DESIGN-1](#design-1).

Supported dark mode MUST be deliberately designed rather than blindly invert light mode: define relevant surfaces, hierarchy, contrast, text tones, borders, shadows/elevation, focus/semantic states, and image treatment. Themes retain product identity without requiring identical visual treatment. Typography SHOULD be deliberately selected for readability, hierarchy, platform, supported languages, weights, performance, licensing, and longevity; Inter, Roboto, or framework defaults are valid when reasoned. Iconography SHOULD use a coherent family/style with deliberate reasons for mixed strokes, filled/outline styles, or generated imagery; vector artwork remains subject to [ASSET-1](#asset-1).

Density SHOULD reflect task frequency, information complexity, expertise, device size, and accessibility, rather than universally impose huge cards, spacing, or typography on finance, developer, media, medical, settings, and other products. Motion SHOULD communicate transition, relationship, hierarchy, continuity, progress, or feedback; respect reduced-motion needs under [UI-3](#ui-3). Visual decoration MUST NOT obscure hierarchy, navigation, actions, application state, errors/warnings, permissions, security/sync state, or progress. Product identity MUST respect applicable navigation, keyboard/windowing/gesture/back/menu/input/selection/system-control conventions; cross-platform consistency means shared identity and semantics, not identical pixels. [UI-2](#ui-2) and [CORE-1](#core-1) still govern adaptation and common product truth.

Establish the core design system before proliferating independently designed screens. Avoid artificial sparsity and chaotic density through grouping/hierarchy. Icon aggregators do not license every underlying asset; verify collection/asset licensing and provenance under [ASSET-2](#asset-2) and [SEC-3](#sec-3). Motion MUST NOT be the only channel of important meaning. Refine hover/pressed/focus/loading/transition/scroll/selection/drag/success/error micro-interactions after the interaction structure is sound; polish does not rescue missing information architecture.

<a id="ui-6"></a>
### 6.10. UI-6 — Complete workflow states and actionable copy

**Type:** ECOSYSTEM POLICY | **Origin:** USER POLICY | **Applies:** user-facing workflows and their materially relevant states

Design MUST cover relevant states beyond the ideal happy path: initial/empty, loading/progressive loading, success/error/partial failure, unavailable service, offline/reconnecting, sync conflict, stale information, permission denied/authentication required, migration/recovery/unsupported version, security scan running/detection/quarantine/scanner unavailable, backup/recovery state, destructive confirmation, and irreversible-action warnings. A state with no applicable capability need not be invented. State presentation MUST accurately reflect outcomes and uncertainty under [OUT-1](#out-1), [RUN-2](#run-2), and [IO-3](#io-3), without changing established authorization or confirmation policy.

User-facing copy MUST be specific, understandable, context-aware, and concise where possible, explaining actual value, state, or action rather than generic AI marketing. Empty states SHOULD explain what belongs there, why it is empty, a useful next action, and whether content is expected automatically where relevant; generic “Nothing here yet!” filler and meaningless illustrations are insufficient when guidance is needed. Errors SHOULD explain what happened/was affected, whether anything changed, whether retry is safe, and the next action to the extent known. Raw implementation failures or “Something went wrong” MUST NOT be the sole explanation when they conceal known material information or uncertainty. Apply [PRIV-1](#priv-1) and [SEC-2](#sec-2) to disclosures.

<a id="ui-7"></a>
### 6.11. UI-7 — Rendered UI evidence and completion gate

**Type:** ECOSYSTEM POLICY | **Origin:** USER POLICY | **Applies:** substantial interface completion and validation of supported sizes/workflows

UI evaluation MUST NOT rely solely on immaculate placeholders or lorem ipsum. Test relevant long/short names, absent optional information, large/small numbers, long/empty lists, unusual Unicode, supported languages, long dates/times/filenames, errors, and realistic content density. Where multiple sizes/form factors are supported, validate actual rendered UI at representative sizes for hierarchy, controls, density, text readability, overflow, navigation, focus, touch targets, and orientation where relevant. A responsive framework alone does not establish good adaptive behavior.

Substantial interface work MUST receive visual review from actual rendered output, using real rendering, screenshots, device previews, human/AI visual review, or equivalent evidence as appropriate; source correctness alone is insufficient. Mature interfaces SHOULD consider visual-regression automation where stability matters; trivial UIs need no screenshot infrastructure. Before declaring substantial UI implementation complete, explicitly review product identity, component/design-system consistency, platform conventions, accessibility, responsive/adaptive behavior, state coverage, realistic content, generic-aesthetic signals, and visual hierarchy. Evidence may be concise but MUST compare rendered behavior with the design brief/contracts and applicable [UI-3](#ui-3) criteria. This review feeds [DEV-13](#dev-13)'s existing Three-Layer Conformance Gate rather than replacing it or creating a second completion authority.

Use a proportionate draft → render → inspect → identify specific issue → modify → render/re-review loop, preferably in coherent flows/screens/components/states rather than giant one-shot whole-product generation. Include representative zoom/text scaling, platform context, and supported localizations/RTL where relevant. Passing code tests MUST NOT alone overrule a coherent owner/designer rejection against intended product direction; preserve actionable evidence and resolve it under project authority/contracts.

Substantial UI SHOULD receive applicable usability heuristic review: system status, real-world match, user control, consistency, error prevention, recognition over memory, flexibility, minimalist focus, error recovery, and useful help. Progressive disclosure SHOULD reduce complexity without hiding necessary primary/frequent functions merely for visual sparsity. Where scale/stakes justify it, validate representative tasks with users, owner walkthroughs for personal products, or equivalent evidence. Tiny personal utilities need no formal research bureaucracy. Subjectivity does not excuse required brief, rendered evidence, accessibility, or workflow review.

For substantial or high-stakes interfaces where resources justify formal heuristic evaluation, multiple independent reviewers SHOULD be preferred over a single self-review, with findings aggregated because different perspectives can uncover different usability failures. No fixed reviewer count or expert panel is required for every interface; this preference neither replaces evidence-based completion nor authorizes a constitutional Red review.

<a id="s07"></a>
## 7. Data lifecycle and application replacement

<a id="life-1"></a>
### 7.1. LIFE-1 — Preservation across supported replacement

**Type:** UNIVERSAL INVARIANT | **Origin:** DERIVED ENGINEERING RULE | **Applies:** installation, update, replacement, or removal with retained state

Lifecycle operations MUST honor declared preservation and deletion semantics. Retained data, user configuration, required keys, and required evidence MUST NOT be accidentally destroyed by an operation represented as preserving them. Reattachment claims MUST account for schemas, keys, permissions, formats, and required software.

<a id="life-2"></a>
### 7.2. LIFE-2 — Long-term accessibility

**Type:** ECOSYSTEM POLICY | **Origin:** USER POLICY | **Applies:** information designated for long-term user retention

Applications MUST provide a practicable preservation and exit path beyond a particular runtime or vendor's lifetime, using documented formats, exports, readers, and recovery dependencies as appropriate. This does not require indefinite retention of expiring tokens or deleted content. Host bindings and secrets need an explicit portability/recovery strategy.

Where durable user information is retained, its lifecycle MUST be distinguished from replaceable application binaries, UI, AI/model providers, indexes, runtime state, and machines. Loss or replacement of one of those components MUST NOT automatically destroy or unnecessarily trap the retained information within disposable implementation state. Planning MUST ask: **Could the application implementation be replaced without unnecessarily destroying or trapping the user's retained information?** Recovery remains bounded by declared retention, portability, and dependency contracts, including [BACKUP-1](#backup-1); this does not promise that every binary artifact is readable without software or that every failure is recoverable.

The goal is **maintenance-minimal**, not maintenance-zero: documented schemas, portable data, replaceable components, the shared Rust core, stable identities, migration discipline, explicit dependencies, tests, reproducible builds where applicable, rebuildable derived state, and durable planning context reduce future work. Applications MUST NOT promise that they work forever without maintenance without supportable evidence.

[SURVIVE-1](#survive-1)–[SURVIVE-2](#survive-2) require an actually preserved independent representation and app-disappearance evidence, including mobile uninstall/container/key risks.

<a id="life-3"></a>
### 7.3. LIFE-3 — Logical storage separation

**Type:** RECOMMENDATION | **Origin:** ARCHITECTURAL DECISION | **Applies:** applications with multiple data lifecycles

Applications SHOULD distinguish replaceable code, retained data, configuration, generated artifacts, audit evidence, operational logs, backups, and exports. Directories, tables, object namespaces, or platform-managed stores may implement the distinction. Executables and data may be colocated if lifecycle operations preserve their contracts; for retained user-owned information, [WORKSPACE-1](#workspace-1) requires separation from disposable installation state and independently accessible preservation. Colocation cannot make that disposable state the only retained copy.

Roles such as `app/`, `data/`, `config/`, `derived/`, `audit/`, `cache/`, `logs/`, `backups/`, and `exports/` are illustrative. An export is not automatically disposable staging. Git may intentionally store canonical documents; it is not automatically a suitable database or independent backup. Prevent unintended inclusion in unrelated source repositories using suitable ignore rules, controls, and review; `.gitignore` is not an enforcement boundary.

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

Account for models, versions, seeds, external inputs, licenses, hardware behavior, cost, and availability where relevant. Non-reproducible outputs and expensive embeddings are not automatically disposable. Derived-state backup is permitted. Synchronous indexes/materialized views are permitted; derivation does not grant authority to mutate canonical records outside [AUTH-1](#auth-1).

Indexes, search/vector databases, embeddings, caches, previews, thumbnails, OCR indexes, materialized views, and generated reports/workbooks are often derived; their actual authority and retention follow [DATA-1](#data-1), not their names. Deleting a store declared rebuildable MUST NOT destroy the canonical information or retained dependencies needed for its declared rebuild contract. A derived artifact MUST NOT silently become the sole copy of irreplaceable information.

Editing a derived report, spreadsheet, index, dashboard, projection, cache, or generated view MUST NOT silently mutate canonical state. Supported bidirectional editing requires deliberately designed, validated adoption/import semantics under [EDIT-1](#edit-1), [IO-1](#io-1), and [AUTH-1](#auth-1); a projection is not automatically a write authority.

<a id="data-3"></a>
### 8.3. DATA-3 — Originals, derivative lineage, and annotations

**Type:** ECOSYSTEM POLICY | **Origin:** USER POLICY | **Applies:** applications ingesting or preserving source artifacts and meaningful derivatives

Applications MUST distinguish preserved originals from extraction, normalization, transformation, interpretation, annotation, AI-generated derivatives, and canonical decisions where those roles exist. A searchable derivative MUST NOT silently replace a preserved original merely for convenience. Preservation follows the declared retention/privacy contract, not indefinite storage of every source.

Meaningful derivatives SHOULD retain proportionate lineage sufficient to identify their parent/source and relevant source version/hash, tool/version, model/version where applicable, creation time, method, and review/verification status. Not every field is needed for trivial artifacts, and uncertain model identity must remain uncertain. Material source changes MUST support invalidation, stale marking, regeneration, or review as appropriate rather than silently representing outdated derivatives as current. Lineage and its retention follow [EVID-1](#evid-1) and [PRIV-1](#priv-1).

Where originals are to be preserved, notes, highlights, comments, tags, review decisions, and AI annotations SHOULD normally be related overlays anchored to the original, rather than destructive alteration. Ordinary editable documents remain valid. Anchors and their source-context validity follow [INFO-4](#info-4).

<a id="data-4"></a>
### 8.4. DATA-4 — Locale-independent durable meaning

**Type:** ECOSYSTEM POLICY | **Origin:** USER POLICY | **Applies:** durable or interchange values whose interpretation or identity can materially depend on locale or text conventions

Persistent/interchange meaning MUST NOT silently depend on the reading device's current display locale. Use typed or otherwise unambiguous representations where needed, separating semantic values from locale-aware presentation. The App Plan MUST declare relevant number, date, currency, percentage, unit, sorting/collation, encoding, Unicode normalization, case, and identifier semantics where these affect durable meaning or identity across supported platforms. [PORT-2](#port-2) governs filesystem differences; no universal normalization algorithm is prescribed.

Human-formatted imports/exports MUST declare parsing/interpretation assumptions, detect ambiguity where practical, and preserve source representation/provenance where meaningful under [IO-1](#io-1), [EVID-1](#evid-1), and [PRIV-1](#priv-1). An ambiguous value such as `1,234` MUST NOT silently be reinterpreted using the current device locale when durable meaning matters. No translation mandate, support for every locale, or locale metadata on every stored string is required.

<a id="data-5"></a>
### 8.5. DATA-5 — Universal timezone policy and explicit temporal meaning

**Type:** ECOSYSTEM POLICY | **Origin:** USER POLICY | **Applies:** every application's timezone planning, with temporal representations and controls determined by actual semantics

Every App Plan MUST explicitly state its timezone policy, regardless of domain or presence of scheduling features. Define how timezone-sensitive values are represented, converted, persisted, compared, displayed, imported, exported, synchronized, and migrated wherever those operations occur. Consider logs, audit events, backups, sync, filesystem observations, migrations, certificates/security events, scheduled jobs, reports, APIs, receipts, provenance, and diagnostics as well as user-visible domain values. A small application may use a concise statement identifying its actual temporal inputs/outputs and absent operations; lack of scheduling MUST NOT be used to omit timezone planning.

Distinguish relevant event/effective time, source observation, ingestion, creation/modification, due time, absolute instants, local civil date/time, timezone-relative schedules, recurring local times, date-only values, elapsed durations, and monotonic runtime intervals. Only relevant concepts need representation. Date-only birthdays, elapsed durations, and monotonic timers MUST NOT acquire arbitrary timezone meaning or conversions. UTC instants are appropriate for many events, not a universal representation for every temporal concept.

Changes to OS timezone, travel location, device, NAS, or locale MUST NOT silently reinterpret persisted historical meaning. Conversions MUST retain enough source context to reconstruct or explain the relevant original meaning where required by the domain/retention contract, distinguishing source timezone, canonical instant, and display timezone where significant. For example, a deadline defined as 23:59 Asia/Bahrain does not become 23:59 Europe/London because a laptop travels; a converted display may differ while preserving declared meaning. Retention remains subject to [PRIV-1](#priv-1).

An observed offset such as UTC+03:00 and a timezone-rule identity such as Asia/Riyadh are not interchangeable concepts. Where future rule changes affect meaning, the App Plan SHOULD use durable timezone semantics rather than relying solely on today's numeric offset, and MUST define how relevant rule changes are handled. No single storage representation or timezone database is prescribed. Where wall-clock correctness matters, account proportionately for skew, unsynchronized devices, source-provided timestamps, device clock changes, uncertain zones, and daylight-saving/rule changes; an OS timestamp is not automatically verified truth under [EVID-1](#evid-1).

Leases, retries, deadlines, expirations, synchronization, idempotency, and ordering MUST use time semantics appropriate to their correctness contracts. Distinguish wall-clock readings from monotonic elapsed-time measurement where conflation could break correctness; document relevant clock, restart, and cross-device assumptions. No one clock mechanism provides distributed ordering or stale-writer exclusion by itself; [CON-1](#con-1), [CON-2](#con-2), and [RETRY-1](#retry-1) continue to apply.

<a id="s09"></a>
## 9. Local and offline operation

<a id="offline-1"></a>
### 9.1. OFFLINE-1 — Useful local operation by policy

**Type:** ECOSYSTEM POLICY | **Origin:** USER POLICY | **Applies:** capability design and network dependencies

Applications SHOULD maximize useful local operation where the domain permits it. They MUST define offline behavior per capability and avoid unrelated cloud dependencies disabling otherwise independent local access. Intentional departures need technical justification under [GOV-3](#gov-3).

Search services, email delivery, streaming, live collaboration, market access, and other remote-native capabilities may need connectivity. Intrinsic documented dependence is not a policy exception. Preserve useful drafts, cached content, or inspection where appropriate; do not imply uncached or remotely authoritative information is current or available.

Independent local capabilities and honest cached/pending states are distinguished from prohibited failure substitutions in [NOFALL-2](#nofall-2).

<a id="offline-2"></a>
### 9.2. OFFLINE-2 — Safe delayed execution

**Type:** CONDITIONAL | **Origin:** DERIVED ENGINEERING RULE | **Applies:** queued or offline operations

Queueing MUST have domain-safe freshness, expiry, cancellation, authorization, replay, and conflict semantics. Time-sensitive orders, physical commands, or door-unlock actions MUST NOT replay automatically merely because connectivity returns. A domain may reject offline writes, allocate rights in advance, or restrict operations to preserve shared invariants. Distinguish queued intent from completed remote action under [OUT-1](#out-1).

<a id="offline-3"></a>
### 9.3. OFFLINE-3 — Device-local personal operation

**Type:** ECOSYSTEM POLICY | **Origin:** USER POLICY | **Applies:** personal applications with ordinary local capabilities

Each applicable personal application MUST remain usable locally on its supported devices. A permanent NAS, cloud service, or Internet connection MUST NOT be required for ordinary local capabilities unless the capability itself is inherently remote. Devices MAY maintain appropriate local working copies; loss of connectivity MUST NOT unnecessarily remove ordinary local functionality or access to locally held user data. Products MUST describe what is retained locally, what is available offline, and which operations require remote coordination. An appropriate working copy need not contain an entire huge media collection. Offline changes and reconnection remain subject to [OFFLINE-2](#offline-2) and [SYNC-1](#sync-1).

<a id="s10"></a>
## 10. Product platforms, portability, and visual assets

<a id="port-1"></a>
### 10.1. PORT-1 — Avoid unnecessary platform lock-in

**Type:** ECOSYSTEM POLICY | **Origin:** USER POLICY | **Applies:** platform and deployment choices

Applications SHOULD preserve portable architecture where practical and MUST document architectural portability, source portability, buildability, tested support, and official support separately. Product targets follow the declared scopes in [PORT-3](#port-3); platform-specific departures use documented exceptions under [GOV-3](#gov-3). A build is not runtime evidence. CPU architectures, OS versions, browser versions, BSD, and NAS platforms are not automatically one support matrix for every product. Declare concrete supported configurations and evidence. NAS obligations follow [NAS-1](#nas-1).

<a id="port-2"></a>
### 10.2. PORT-2 — Portable references and faithful content

**Type:** CONDITIONAL | **Origin:** DERIVED ENGINEERING RULE | **Applies:** filesystem references and portable/interchange data

Hardcoded developer-specific paths in portable logic MUST NOT become runtime assumptions. Absolute paths may legitimately be host bindings, user configuration, filesystem-tool inputs, or audit evidence. Where relocation is promised, references MUST have documented identity/resolution semantics and explicit rebinding for host resources.

Use runtime path APIs where appropriate. Claimed targets require consideration of case behavior, Unicode normalization, reserved names, permissions, links, and collisions. Case-sensitive comparison or a universal sanitizer does not solve these differences. Preserve original names, bytes, and line endings when identity, signatures, fidelity, or user intent requires it; transformations need defined semantics and collision handling.

Example: `attachments/doc1.pdf` can be relative when its base and escaping are specified. `file://attachments/doc1.pdf` places `attachments` in the URI authority; it is not an ordinary relative reference. Reversible mappings can avoid lossy sanitation.

<a id="port-3"></a>
### 10.3. PORT-3 — Declared Product Platform Scope

**Type:** ECOSYSTEM POLICY | **Origin:** USER POLICY | **Applies:** application product scope and supported clients

Each application MUST declare its actual Product Platform Scope or scopes and concrete support matrix under [PORT-1](#port-1), following requirements rather than assuming every product needs every platform. Desktop-only, mobile-only, desktop/mobile/tablet, web, and a justified narrower subset are valid product definitions. Scopes do not require every CLI, library, or service to acquire a graphical or mobile interface. Record technical reasons, intended users, supported configurations and limits; formal departures from an applicable ecosystem policy remain governed by [GOV-3](#gov-3).

| Scope | Product targets and evidence |
|---|---|
| DESKTOP | Consider Windows, macOS, and Linux as the normal desktop/laptop scope; justify a narrower actual product scope. Where Linux is supported, assess Linux Mint's current stable Ubuntu-based release, Ubuntu LTS, Arch Linux, and CachyOS explicitly. |
| MOBILE | Consider Android, iPhone/iOS, iPadOS/iPad, and applicable Android tablets; declare the actual phone/tablet subset and adaptive behavior under [UI-2](#ui-2). |
| UNIVERSAL DEVICE APPLICATION | This claimed scope targets Windows, macOS, Linux, Android, iPhone/iOS, iPadOS, and applicable Android tablets. Name any incomplete targets accurately. Web MAY additionally be included. |
| WEB | Declare supported browsers, versions/capabilities and evidence. Web support is distinct from native application support. |

Linux Mint, Ubuntu LTS, Arch Linux, and CachyOS MUST NOT be casually omitted from desktop-Linux assessment or assumed interchangeable. For each, record first-class supported/tested, planned/unverified, compatibility/best-effort, or unsupported status, the concrete reason, versions or rolling snapshots, material environment assumptions, and the testing commitment. Arch Linux and CachyOS remain important targets; Ubuntu LTS and Linux Mint remain explicit stable-distribution assessment targets. An intentionally narrower support contract is a recorded product decision, not a claim that omitted systems passed.

Every declared first-class supported target MUST receive applicable installation/packaging, launch, updates, filesystem, permissions, core-feature, and native/system-integration validation. State automated/manual coverage and limits under [TEST-1](#test-1). A declared target awaiting implementation/testing MUST remain labeled accordingly. Passing Ubuntu or Mint tests does not validate Arch, CachyOS, or all Linux distributions. Framework support or a successful build is not verified runtime support. Within the declared desktop-Linux scope, other mainstream Linux distributions remain compatibility/best-effort targets where dependencies permit unless explicitly promoted to first-class support or excluded by the justified narrower support contract. Best-effort status is not verified support. [TECH-3](#tech-3) governs platform/frontend investigation.

<a id="asset-1"></a>
### 10.4. ASSET-1 — Genuine vector source artwork

**Type:** ECOSYSTEM POLICY | **Origin:** USER POLICY | **Applies:** application-owned visual assets, including web UI assets

Naturally vector-representable assets SHOULD use genuine SVG as their source format, including icons, logos, interface symbols, badges, simple illustrations, diagrams, and decorative vector artwork. When recreating a raster reference as a UI icon or another vector-representable asset, authors MUST reconstruct genuine vector geometry rather than embed PNG/JPEG content in an SVG wrapper and claim compliance. Appropriate structures include paths, shapes, gradients, masks, and vector text converted appropriately when needed.

Photographs, screenshots, scans, textures, camera images, complex photographic artwork, and other intrinsically raster content MAY remain raster in formats appropriate to the use case. They MUST NOT be converted into meaningless SVG merely to satisfy this policy. Required generated raster icon sizes and platform/store-specific containers are permitted; naturally vector artwork SHOULD retain vector source-of-truth artwork. Generated platform derivatives do not violate this policy.

<a id="asset-2"></a>
### 10.5. ASSET-2 — Third-party brand fidelity

**Type:** ECOSYSTEM POLICY | **Origin:** USER POLICY | **Applies:** third-party trademarks and brand assets

Products MUST NOT inaccurately redraw third-party trademarks from screenshots. Where permitted, use official brand assets and follow applicable brand requirements. The application-owned SVG preference does not authorize inaccurate conversion or disregard of asset licensing or brand constraints.

<a id="asset-3"></a>
### 10.6. ASSET-3 — SVG trust boundaries

**Type:** CONDITIONAL | **Origin:** USER POLICY | **Applies:** SVG acceptance, rendering, and application-owned SVG assets

Untrusted SVG MUST NOT automatically be treated as harmless image data. Applications accepting external SVG MUST handle script execution, remote resource access, and unsafe embedded content according to the actual renderer and trust boundary, using appropriate restrictions, sanitization, isolation, or rejection. Application-owned SVG SHOULD avoid unnecessary executable or external content. File extensions and SVG wrappers do not establish safety.

<a id="s11"></a>
## 11. NAS support

<a id="nas-1"></a>
### 11.1. NAS-1 — Mandatory ecosystem support policy

**Type:** ECOSYSTEM POLICY | **Origin:** USER POLICY | **Applies:** relevant hosting, storage, file-access, service-client, and backup roles

NAS support is intentional. Applicable applications MUST identify and support NAS modes needed for their intended workflow, documenting configurations, concurrency assumptions, disconnection semantics, recovery, and tested guarantees. They MUST NOT silently assume only fast local disks. Supporting one mode does not imply the others.

| Mode | Meaning | Scope of support claim |
|---|---|---|
| 1 — NAS/server hosted | Application runs on a NAS/private server using server-local storage. | Runtime, storage, permissions, resources, and lifecycle. |
| 2 — NAS-hosted service client | Client communicates with an application/database/service on NAS. | Protocol, identity, versions, timeouts, cancellation, retries, and outcomes. |
| 3 — User files on a share | Ordinary documents/media/files accessed through network storage. | File operations, identity, caching, concurrency, disconnection, recovery. |
| 4 — Transactional database over a share | Database files opened directly across SMB/NFS or equivalent. | Engine-supported configuration and verified assumptions under [NAS-2](#nas-2). |
| 5 — Backup destination | NAS holds recovery artifacts. | Consistent capture, transfer, restore, keys, access, and failure-domain limits. |

All five modes are not required. Backup-only support MUST NOT be presented as active shared-data support. A service-mediated design can satisfy active NAS use without shared raw database files. Software with no relevant role may document non-applicability; applicable software omitting NAS support needs an approved exception. Docker is neither necessary nor sufficient for NAS compatibility.

A NAS synchronization hub is a topology role under [SYNC-3](#sync-3), not an assertion of raw database access or a sixth interchangeable storage mode. Products MUST distinguish NAS as sync hub, storage service, backup destination, and application/service host. A deployment may combine these roles, but each role retains its own contract; synchronization alone is not a backup.

For important retained data, NAS-hub compromise MUST be included in the recovery risk assessment under [BACKUP-1](#backup-1). Consider protected snapshots/version history, separately protected backup, or another independent recovery mechanism so the hub does not unnecessarily become a single point whose compromise destroys every historical copy. Ordinary sync clients SHOULD NOT require unrestricted NAS administrator authority; [SEC-1](#sec-1) governs least privilege.

<a id="nas-2"></a>
### 11.2. NAS-2 — Configuration-specific evidence

**Type:** CONDITIONAL | **Origin:** DERIVED ENGINEERING RULE | **Applies:** claimed NAS modes and network storage

Claims MUST identify engine, protocol, client/server, filesystem, and configuration assumptions with proportionate empirical evidence. Mode 4 MUST be supported only where the engine explicitly supports that configuration and the application's assumptions have been verified. Unsupported configurations MUST be rejected or clearly reported as unsupported, rather than silently accepted as safe.

SMB/NFS locking is configuration- and failure-dependent. Ordinary multi-process SQLite WAL coordination commonly relies on shared coordination mechanisms; shared-memory coordination does not describe every possible WAL configuration. This does not establish safe multi-host SQLite database access over SMB/NFS. Specialized configurations, including custom VFS behavior, require their own supported contract and evidence under Mode 4. A NAS-local database service is a different mode.

`fsync` and `FlushFileBuffers` offer the guarantees implemented by the complete storage stack; server acknowledgements, caches, hardware, and error propagation matter. Oplocks do not alone define stable-storage durability. Permissions depend on identities/ACLs; `0755` and `0644` are not universal privacy settings. Latency assumptions MUST be measured or bounded for the claimed workload, not copied from fixed illustrative numbers.

Access, quota, and free-space preflights improve diagnostics but cannot prove a future operation succeeds. Disconnects may leave outcomes unknown under [OUT-1](#out-1). Timestamp leases and heartbeats without stale-writer exclusion cannot establish safe overlapping access; coordination follows [CON-1](#con-1).

Possible patterns include NAS-local database services, supported transactional engines, ordinary files with bounded semantics, or immutable chunks with a publication protocol. Chunking is not mandatory and does not itself create a transaction.

<a id="s12"></a>
## 12. Storage and crash consistency

<a id="store-1"></a>
### 12.1. STORE-1 — Explicit storage contracts

**Type:** CONDITIONAL | **Origin:** DERIVED ENGINEERING RULE | **Applies:** persistence backends

Each backend MUST document crash-consistency, acknowledgement, concurrency, and recovery contracts and supporting failure assumptions. Protect retained state against the interruptions the application claims to tolerate, and disclose limits instead of promising immunity to arbitrary hardware, software, or adversarial failures.

Visibility, atomicity, durability, replication, and external completion differ. Define consistency units and observers of intermediate state. Larger workflows may expose recoverable intermediate states rather than use one global transaction. Logical rollback need not restore every physical byte to an earlier layout.

Storage MUST fit workload, transaction, concurrency, and recovery needs; a product name is not evidence. Open text and documented binary formats are valid. Parquet is an open binary columnar format, not human-readable text.

For applicable retained-user-data applications, the App Plan MUST define a lightweight, cross-platform **Save Transaction & Recovery Protocol** covering the durable original-file boundary, its relation to Current JSON and Folder JSON publication, interruption states, recovery inspection, and user-visible outcomes. The protocol MUST prioritize making the original-file change durable before treating secondary Current JSON synchronization or Folder JSON reverification as complete. Each managed workspace MUST maintain a lightweight, dated, folder-scoped transaction/recovery journal sufficient to identify pending work, affected file/folder identities, durable revision and recovery state. Keep this journal distinct in purpose from diagnostic and security/audit logs; it need not duplicate user payloads or prescribe a universal physical file format. Required journal evidence MUST remain available until its recovery obligation is resolved, subject to applicable privacy, deletion and retention limits. The intended meaning of an earlier “gzip file” status label is unconfirmed; it does not establish a separate required artifact.

Before an operation that needs substantial temporary space, estimate required capacity and a reasonable margin using the selected workspace, source sizes and staging/rollback needs. A successful preflight cannot guarantee later allocation or device health; recheck during the operation, handle actual failures, and do not remove protected recovery data merely to force the operation to continue.

<a id="store-2"></a>
### 12.2. STORE-2 — Mechanisms follow the contract

**Type:** RECOMMENDATION | **Origin:** DERIVED ENGINEERING RULE | **Applies:** storage implementation choices

Implementations SHOULD use proven engine protocols where suitable. ACID transactions, copy-on-write, append logs, journals, transactional object stores, engine-native updates, and atomic replacement are possible mechanisms. No file algorithm is required for every write.

For a replaceable file on a backend with suitable semantics, an illustrative sequence is: create a unique temporary file on the required filesystem; serialize and check writes; synchronize as required; publish through a supported replace/rename operation; synchronize directory metadata where required; recover interrupted work. It also needs safe temporary-file creation, race protection, metadata/permission handling, and failure classification. Same-filesystem placement is not proof of full crash durability. Windows APIs, sharing modes, and filesystems need qualification; a replacement flag is not a universal guarantee.

Append stores and databases may use different protocols, including protected in-place page updates. An intent journal alone does not provide atomic multi-file behavior: durable ordering, commit markers, reader visibility, partial application, and recovery need a complete protocol.

<a id="s13"></a>
## 13. Concurrency and conflict semantics

<a id="con-1"></a>
### 13.1. CON-1 — Prevent invalid interleavings

**Type:** CONDITIONAL | **Origin:** DERIVED ENGINEERING RULE | **Applies:** state reachable by concurrent actors/processes

Applications MUST prevent invalid interleavings according to declared consistency semantics. Enforced single-writer access is permitted. Exclusive-access assumptions MUST be enforced or explicitly bounded; a convention alone is not exclusion.

MVCC, serialized services, transactions, optimistic concurrency, CRDTs, append protocols, and storage-enforced fencing are possible mechanisms. Version/hash checks MUST be coupled to transitions when used to prevent races; check-then-write is insufficient. Lease designs MUST prevent stale holders violating promised semantics through storage-enforced fencing or an equivalent protocol, not just heartbeats.

Lock scope/deadlines depend on engine and workload; relational writes do not universally need exclusive database locks. Define cancellation, timeout, and starvation behavior where material to correctness or availability.

External applications MAY edit supported user files. Prefer coordination that does not hold long-lived exclusive file locks; acquire a brief exclusive scope only when required for correctness, and define its target, expiry/release and failure handling. Do not mistake an unlocked interval or watcher event for proof that no concurrent edit occurred; revalidate at the relevant commit boundary.

<a id="con-2"></a>
### 13.2. CON-2 — Domain-appropriate conflict resolution

**Type:** CONDITIONAL | **Origin:** DERIVED ENGINEERING RULE | **Applies:** conflicting state changes

Resolution MUST preserve declared semantics and MUST NOT silently discard independently meaningful work contrary to them. Reject/retry, semantic merge, preserved alternatives, domain-approved last-writer-wins, or user decisions are options. A deterministic merge can still violate an invariant.

Lamport clocks order events consistently with causality but do not alone identify concurrency. Vector clocks track causal relationships under protocol assumptions. Hashes indicate content equality/difference, not independent causality. CRDTs provide specific convergence semantics, not arbitrary business-invariant preservation. These mechanisms are not interchangeable.

Automatic merges are permitted only when the system can establish that the changed portions are independent and mutually compatible under the domain contract. Otherwise preserve both valid competing versions and present a reviewable conflict; do not silently choose a timestamp winner. Where the format supports meaningful comparison, highlight changed portions and offer scoped **Keep Previous**, **Keep Current**, and **Keep Both** choices with a preview. Binary or unsupported formats require truthful file-level comparison rather than invented text diffs.

<a id="s14"></a>
## 14. Operation outcomes and acknowledgements

<a id="out-1"></a>
### 14.1. OUT-1 — Report what is actually known

**Type:** UNIVERSAL INVARIANT | **Origin:** DERIVED ENGINEERING RULE | **Applies:** important local and external operation results

Results MUST distinguish relevant states: rejection, acceptance, queued intent, local application, local durable commit, remote acknowledgement, external completion, failure before execution, partial execution, or unknown outcome. Exact labels are optional. Acceptance MUST NOT imply completion; remote acknowledgement MUST NOT imply stronger durability/finality than its contract provides.

A timeout, crash, or NAS disconnect can leave success indeterminate. Applications MUST report uncertainty, retain suitable recovery correlation, and reconcile or use a demonstrably safe retry policy. Missing acknowledgement alone MUST NOT be reported as proof of failure. Relevant callers, including AI, need the actual durability/completion boundary.

For workspace saves, report original-file durability separately from the freshness and verification of its mandatory Current JSON and affected Folder JSON. Enabled Master JSON and optional backup progress are separate states. Long-running operations MUST expose truthful progress and phase; provide percentages only when measurable, otherwise use an accurate state label. Progress MUST NOT imply completion, verification, or a fixed amount of work when that amount is unknown.

Example result fields: operation ID, known phase, affected resources, durability scope, external correlation, uncertainty, and allowed next actions. A small utility may convey these semantics through exit status and a concise message.

<a id="ops-1"></a>
### 14.2. OPS-1 — Operation identity and recovery receipts

**Type:** ECOSYSTEM POLICY | **Origin:** USER POLICY | **Applies:** consequential operations whose retry, boundary crossing, crash survival, or uncertainty requires effect correlation

Such operations SHOULD use a stable operation identity or equivalent correlation mechanism to distinguish retrying the same intended operation from a genuinely new operation. Pure local reads with no meaningful side effects do not require idempotency keys. Where identity is used for idempotency, the complete protocol in [RETRY-1](#retry-1) applies; an ID alone does not prevent all duplicates.

When recovery requires knowing what happened, the application MUST maintain durable evidence appropriate to the operation. A receipt may contain operation ID, normalized request identity/hash, result, affected object IDs, commit/reconciliation state, verification evidence, timestamps, and relevant actor/principal. No one format or permanent payload-retention rule is required. Receipts MAY reuse existing audit or execution records rather than duplicate them; required mutation/evidence coupling follows [AUDIT-2](#audit-2) and privacy follows [PRIV-1](#priv-1).

Receipts MUST distinguish observed results from unestablished external completion under [OUT-1](#out-1). Recording intent or a local commit cannot prove that a remote or physical effect occurred. Unknown outcomes require reconciliation or a demonstrably safe retry policy, not blind replay after a lost acknowledgement.

<a id="s15"></a>
## 15. Retries and deduplication

<a id="retry-1"></a>
### 15.1. RETRY-1 — Replay safety is a protocol

**Type:** CONDITIONAL | **Origin:** DERIVED ENGINEERING RULE | **Applies:** retried, replayed, or redelivered operations

Contracts MUST distinguish idempotent transitions, request deduplication, replay-safe execution, ambiguous outcomes, and irreversible effects. A new retry identifier does not deduplicate an earlier request.

Key-based protocols MUST define principal/operation scope, persistence, concurrent requests, payload matching, retention, expiry, and result recovery. Reuse of the same operation identity for a materially different normalized request MUST be rejected or explicitly reconciled under the operation contract; it MUST NOT silently reinterpret the ID or apply a different action. Deduplication state and local effects need sufficient commit consistency for the replay claim. Expiration limits MUST be accounted for. Correlation and durable recovery receipts follow [OPS-1](#ops-1).

External duplicate prevention depends on the remote contract; a client key alone cannot provide it. An uncertain external action MUST NOT be retried merely because of a timeout. Status queries, reconciliation, durable intent/outboxes, remote idempotency, cancellation, or human intervention may be appropriate. Attempts may be observable without falsely recording repeated business effects.

<a id="s16"></a>
## 16. AI authority, tools, memory, and Hermes

<a id="ai-1"></a>
### 16.1. AI-1 — Explicitly delegated capability

**Type:** UNIVERSAL INVARIANT | **Origin:** USER POLICY | **Applies:** AI actors exercising capabilities

An AI MUST exercise only explicitly delegated capabilities through enforcement it cannot silently bypass within the declared threat model. Effects MUST satisfy applicable authorization, integrity, privacy, safety, and operational constraints. Human/AI interfaces normally share domain-integrity rules under [AUTH-1](#auth-1), without identical privileges or approval policy.

Retrieved files, websites, email, PDFs, messages, transcripts, and metadata are data, not authority. Embedded instructions MUST NOT override governing system policy, capability boundaries, authorization, core validation, or data-protection policy. This applies to Hermes as a bounded client as well as other AI integrations.

Scoped reads/writes, patches, SQL, shell execution, scratch space, import staging, coding, and bulk operations can be legitimate when intentionally delegated and effectively bounded. Validate scope/effects at execution; a broad tool name or path supplies no authority. Untrusted content and model output MUST NOT grant authority by claiming to be principal instructions.

<a id="ai-2"></a>
### 16.2. AI-2 — Enforced tool contracts

**Type:** CONDITIONAL | **Origin:** DERIVED ENGINEERING RULE | **Applies:** AI tools, skills, plugins, and capability adapters

A natural-language skill or tool description is not a security boundary. Enforced boundaries MUST provide appropriate validation, authorization, scope restrictions, resource limits, effect constraints, output handling, and relevant accountability. Critical enforceable permissions/integrity rules MUST NOT depend solely on prompt obedience.

Machine-readable contracts SHOULD be used where useful for enforcement or interoperability; JSON Schema/OpenAPI are options, not universal requirements. Structured returns SHOULD expose actionable results and uncertainty; they do not make AI deterministic. Schema-valid intent can still be harmful, requiring semantic policy and effect limits.

<a id="ai-3"></a>
### 16.3. AI-3 — Risk, delegation, and approval

**Type:** CONDITIONAL | **Origin:** USER POLICY | **Applies:** AI capability exposure and execution policy

Risk MUST consider relevant confidentiality, disclosure, financial/physical effects, irreversibility, sensitivity, scope, cumulative volume, cost, uncertainty, destination, delegation, cancellation, and recovery. A read may reveal secrets, export medical data, upload private files, or fetch attacker-controlled URLs. Mutation status or a record-count threshold does not establish risk.

Approval MUST reflect consequences and actual delegation. Explicitly authorized autonomous consequential or high-volume work is permitted within enforced limits. Interactive confirmation is one control, not a universal prerequisite. Material scope expansion needs new authority, not inferred consent.

When approval relies on a preview, bind it to relevant parameters, resources, versions, scope, expiry, and budgets; revalidate before execution where necessary. Disclose estimates, external dependencies, and stale assumptions. A dry-run does not prove future external effects. Changes invalidating approved scope MUST be rejected, reconciled, or reauthorized according to policy.

<a id="ai-4"></a>
### 16.4. AI-4 — Memory and provider boundaries

**Type:** CONDITIONAL | **Origin:** DERIVED ENGINEERING RULE | **Applies:** AI state, retained memory, and integrations

Domain consistency MUST NOT depend solely on hidden model memory or ephemeral context. Explicit state follows [DATA-1](#data-1); scratch work need not become permanent history. Retained AI memory MUST have defined inspection, correction, export, access, deletion, and derived-copy lifecycle controls consistent with principals' rights. It MUST NOT silently override authoritative records or policy.

Provider integrations SHOULD isolate replaceable dependencies where useful and declare capabilities. Abstraction reduces coupling, not differences in model quality, interfaces, cost, licensing, or availability. Provider-specific tools may intentionally use unique capabilities. Optional AI failure SHOULD preserve independent functions; AI-native functions may become unavailable with truthful results. Protect retained data and contain failure within stated assumptions rather than promising immunity to all crashes or resource exhaustion.

Replaceability means deliberate future selection/migration, not runtime provider substitution after failure. Optional AI unavailability and independent non-AI functionality follow [NOFALL-1](#nofall-1)–[NOFALL-2](#nofall-2).

<a id="hermes-1"></a>
### 16.5. HERMES-1 — Optional, bounded intelligence

**Type:** ECOSYSTEM POLICY | **Origin:** USER POLICY | **Applies:** applications integrating Hermes

Hermes MUST remain an optional intelligence layer rather than the sole means of using the application. Core application behavior MUST work without Hermes. Hermes MUST NOT receive unrestricted raw authority over canonical state; canonical writes MUST pass through validated, authorized application operations under [AUTH-1](#auth-1) and [AI-1](#ai-1). Hermes SHOULD be able to operate locally where the relevant data and model are available. Optional Hermes capabilities do not redefine unrelated AI-native functions in [AI-4](#ai-4) as ordinary core functionality.

Approved application/core operations MUST enforce applicable deterministic validation and bounded authority; model-generated intent supplies neither approval nor validation. Retrieval MUST respect access scope and privacy; provenance and audit follow [AUDIT-1](#audit-1), [AUDIT-2](#audit-2), and [PRIV-1](#priv-1).

Hermes import/processing of untrusted file content MUST use the same deterministic intake/security gates as native UI operations under [IO-2](#io-2) and [IO-3](#io-3). Model size or provider grants no bypass of required malware checks, quarantine, or core validation.

Canonical data MUST NOT exist solely inside an opaque AI memory/vector database with no independent application access and preservation path. This concerns opacity and sole dependence on the intelligence layer, not a blanket ban on vector storage technology: authoritative originals may use such a backend under [DATA-1](#data-1), [LIFE-2](#life-2), and applicable storage/export contracts.

Hermes embeddings, vector stores, semantic indexes, generated summaries, and retrieval caches are normally navigation aids. They SHOULD be reconstructable from retained sources and appropriate deterministic metadata under the actual [DATA-2](#data-2) reproduction contract, without assuming bit-for-bit regeneration of nondeterministic summaries. They MUST NOT silently become the sole repository of irreplaceable information. An explicit, justified authoritative classification is permitted under [DATA-1](#data-1), with independent access, retention, and recovery obligations; it does not excuse opaque model-only preservation.

<a id="hermes-2"></a>
### 16.6. HERMES-2 — Structured, bounded small-model retrieval

**Type:** ECOSYSTEM POLICY | **Origin:** USER POLICY | **Applies:** information architecture and retrieval interfaces for Hermes or other AI clients

Information architecture and AI retrieval interfaces MUST provide structured, scoped discovery and bounded context rather than uncontrolled workspace wandering or reliance on loading entire huge workspaces into a model. The logical flow is **user intent → capability discovery → structured query → catalog/index/core → stable ID → exact object → precise anchor where meaningful → bounded context**. Equivalent mechanisms are allowed. The application/core SHOULD perform as much deterministic narrowing as practical through IDs, aliases, catalogs, typed filters, relationships, bounded search, anchors, candidate lists, and structured errors.

Normal retrieval MUST NOT require the language model to recursively scan the entire user-data tree to answer ordinary queries. Authorized deterministic maintenance or index construction may traverse the corpus; that is distinct from the bounded result consumed by the model. Enforce relevant scope, authorization, and privacy during retrieval and context assembly. Rebuild claims follow [DATA-2](#data-2).

Where Hermes/local AI is part of the product, interfaces MUST be designed and tested assuming a suitably capable constrained local model before relying on a powerful cloud model. Approximately 1B-class models are an engineering target where realistic, not a guarantee of flawless behavior or a universal parameter-count threshold. Record tested capabilities and limits under [TEST-1](#test-1). Cloud clients may provide better reasoning but MUST use the same authority model without hidden architectural privileges.

The **Hermes / User-Adaptable File Structure Blueprint is integrated as CANDIDATE policy**, together with [section 32](#s32). It standardizes discoverability and integrity while leaving user-facing organization domain-appropriate and adaptable. This product-use goal is distinct from the full-app development continuity goal in [DEV-11](#dev-11).

<a id="hermes-3"></a>
### 16.7. HERMES-3 — Core resolution, ambiguity, and actionable failures

**Type:** ECOSYSTEM POLICY | **Origin:** USER POLICY | **Applies:** AI-facing lookup and application-operation interfaces

AI MAY express intent using names, aliases, search terms, friendly references, or previously resolved identifiers. The deterministic application/core MUST resolve or validate authoritative identity, exact location/path, and mutation semantics. Model-generated text MUST NOT by itself create authoritative IDs, canonical paths, or hidden persistence structures. Authorized create/import operations may assign or validate identities according to the product contract; this rule does not forbid delegated coding or scratch work under [AI-1](#ai-1).

When a friendly reference has multiple plausible matches and the contract does not uniquely resolve it, tools MUST return scoped candidates and relevant distinguishing information, indicating that clarification is required. They MUST NOT silently choose the first match or require the AI to invent an ID. Candidate disclosure remains subject to access/privacy controls; excessive result sets may be bounded and narrowed.

Failures SHOULD expose deterministic, actionable information where practical: what failed and why, whether anything changed or remains unknown, relevant object/operation IDs, candidates, a safe next action, and whether user input is required. A raw stack trace alone SHOULD NOT be the ordinary continuation contract. Outcomes remain truthful under [OUT-1](#out-1); structured errors do not grant additional authority or guarantee AI obedience.

<a id="s17"></a>
## 17. Audit and provenance

<a id="audit-1"></a>
### 17.1. AUDIT-1 — Proportionate accountable evidence

**Type:** CONDITIONAL | **Origin:** DERIVED ENGINEERING RULE | **Applies:** operations requiring accountability under domain, policy, or applicable obligations

Applications MUST define required events and an audit contract covering granularity, principal/actor/mechanism, outcome, resources, necessary before/after information, retention, access, redaction, archival, deletion, integrity, and recovery. Evidence MUST support the claim without indiscriminate payload capture. Relevant failures/unknown outcomes MUST be distinguishable from successful effects.

Bulk events may reference an affected set; micro-events may be aggregated if accountability is retained. Model identities may be unknown/provider-reported. Human review records its actual scope. Prompts and free-text reasons need privacy treatment and are not mandatory permanent payloads. Rollback identifiers SHOULD be references rather than enduring bearer authority.

Diagnostics and audit evidence have distinct purposes/lifecycles, without mandatory separate directories. Ordinary correction/reversal should retain its relation to earlier events. Authorized expiry/redaction follows [PRIV-1](#priv-1); append-only semantics do not forbid it.

<a id="audit-2"></a>
### 17.2. AUDIT-2 — Mutation and evidence commit consistency

**Type:** CONDITIONAL | **Origin:** DERIVED ENGINEERING RULE | **Applies:** evidence required for a committed mutation

Required evidence MUST be atomic, transactionally coupled, or recoverably linked with its committed effect. A crash window between unrelated writes MUST NOT be accepted as fulfilling that contract. Define recovery and how evidence-storage failure affects execution, including safety obligations under [SAFE-2](#safe-2).

Non-normative local example:

```text
validate authority and preconditions
begin transaction
    apply canonical transition
    persist required audit event or recoverable outbox evidence
commit that consistency unit
report the outcome supported by the commit contract
deliver outbox evidence with retry-safe processing where applicable
```

An outbox does not atomically execute a physical or remote API effect. Durable intent, correlation, observed outcome, and reconciliation remain necessary, and outcomes can remain unknown. Recoverable evidence needs sufficient information for the actual obligation; a lossy queue marker is not sufficient by definition.

<a id="audit-3"></a>
### 17.3. AUDIT-3 — Integrity claims and trust anchors

**Type:** CONDITIONAL | **Origin:** DERIVED ENGINEERING RULE | **Applies:** claims of tamper evidence

Claims MUST identify adversaries, protected references, verification, and recovery limits. Hashes detect changes relative to trusted references; attackers able to replace data and manifests can defeat comparison. Hash chains need protected anchors or independent evidence against wholesale rewriting. Encryption does not itself establish authorization or audit completeness. Authorized redaction/expiry MUST be distinguishable from unexplained alteration within the stated integrity model.

<a id="evid-1"></a>
### 17.4. EVID-1 — Provenance, evidence status, and uncertainty

**Type:** ECOSYSTEM POLICY | **Origin:** USER POLICY | **Applies:** imported/observed information and research whose provenance or evidence strength materially affects decisions or meaning

Relevant provenance MUST be retained proportionately: source/identifier/version, acquisition or import method, observation time, importer/tool, human modification, and verification scope where meaningful. Successful import, a credible source, or canonical designation MUST NOT silently upgrade an observation into verified factual truth; [DATA-1](#data-1) keeps those dimensions distinct.

Applications and planning records MUST represent evidence strength equivalent to **VERIFIED**, **INFERRED / CONDITIONAL**, and **UNKNOWN** where it affects decisions. Verification identifies its actual scope and supporting evidence. Research, compatibility, external integrations, migrations, planning assumptions, and source observations MUST NOT become architectural facts through repetition alone. Meaningful uncertainty MUST remain representable, including known, unknown, unavailable, ambiguous, unverified, stale, conflicting, and pending-review states as applicable; one universal enumeration is not required. This complements operation uncertainty under [OUT-1](#out-1).

When credible sources conflict, preserve sufficient competing evidence, provenance, uncertainty, and review state rather than silently choosing a winner. Automatic resolution requires an explicit deterministic, justified rule; otherwise retain an unresolved interpretation or obtain authorized review. Evidence retention is purpose-limited under [PRIV-1](#priv-1), not a mandate to keep all original sensitive payloads forever.

An upstream source changing or deleting its copy MUST NOT automatically destroy locally retained evidence or user data. Represent removed-upstream, unavailable, superseded/new-version, stale, or tombstone status as appropriate. Actual deletion follows the applicable retention, privacy, authority, and synchronization contract; legitimate erasure and agreed deletion propagation remain enforceable.

<a id="s18"></a>
## 18. Privacy, retention, and deletion

<a id="priv-1"></a>
### 18.1. PRIV-1 — Purpose-limited processing and retention

**Type:** UNIVERSAL INVARIANT | **Origin:** DERIVED ENGINEERING RULE | **Applies:** sensitive/personal information collection, processing, disclosure, retention

Processing and retention MUST be limited to authorized purposes and applicable obligations. Audit, provenance, prompts, diagnostics, before/after state, model metadata, backups, and derived copies are included. Full prompts, secrets, personal information, and deleted payloads MUST NOT be retained merely because available.

Deletion/retention policies MUST define scope, timing, protected obligations, replicas, indexes, backups, and known limitations. Logical append-only history may coexist with authorized redaction, expiry, archival, key destruction, and cryptographic erasure. Preserve necessary evidence of lifecycle actions without recreating erased payloads. Restore MUST account for applicable deletion decisions rather than silently reinstating information contrary to policy.

Cryptographic erasure depends on effective key destruction and copies; it cannot recall disclosed plaintext. Soft deletion is not a universal substitute for erasure. Resolve conflicting rights and retention obligations through [SAFE-2](#safe-2) with a documented legitimate basis.

<a id="priv-2"></a>
### 18.2. PRIV-2 — Local data and deliberate disclosure

**Type:** ECOSYSTEM POLICY | **Origin:** USER POLICY | **Applies:** user-data storage and external transmission

Local machine/private NAS storage is the default. External disclosure MUST have informed authorization appropriate to purpose, destination, data scope, and principal. Standing delegation is permitted without per-request prompts. Remote-native functions follow [OFFLINE-1](#offline-1). Cloud AI requests SHOULD include only necessary relevant context. Local inference MAY help but does not prove other components transmit nothing. Diagnostic exports need sanitization and user control without mandatory manual inspection of every byte.

<a id="s19"></a>
## 19. External editing and drift

<a id="edit-1"></a>
### 19.1. EDIT-1 — User control and safe adoption

**Type:** CONDITIONAL | **Origin:** USER POLICY | **Applies:** managed files/records accessible outside the ordinary runtime

Users may edit their own Markdown, source, configuration, documents, and open formats subject to legitimate shared rights. Applications MUST define supported edits, validation, adoption, conflicts, and rejection. They MUST NOT silently adopt unsafe state merely because it is in an expected directory. Unsupported edits may be rejected/quarantined without claiming ownership over user files. Reconciliation MUST avoid overwriting newer valid work or destroying the only recoverable copy without authority.

<a id="edit-2"></a>
### 19.2. EDIT-2 — Proportionate drift detection

**Type:** CONDITIONAL | **Origin:** DERIVED ENGINEERING RULE | **Applies:** storage models where external change affects claimed integrity

Detection MUST fit threats, dataset size, architecture, and acceptable latency. Hashes, versions, watcher hints, database versioning, service boundaries, snapshots, or reconciliation protocols are options; constant all-file hashing is not required. Watchers can miss changes and need validation/rescan strategies where the contract requires it.

Drift does not prove maliciousness or authorship. Snapshots can roll back data and a local manifest together; detection of that rollback needs evidence outside the boundary. Adoption, restoration, merge, preserved alternatives, and user decisions are possible resolutions subject to current-state coordination under [CON-1](#con-1).

<a id="s20"></a>
## 20. Synchronization

<a id="sync-1"></a>
### 20.1. SYNC-1 — Explicit distributed authority

**Type:** CONDITIONAL | **Origin:** DERIVED ENGINEERING RULE | **Applies:** synchronization or replicas of a logical dataset

Protocols MUST define authority, identity, causal/conflict semantics, disconnected changes, duplicate handling, deletion propagation, and recovery. Peer data MUST pass applicable authority/integrity controls; sync is not a bypass. Preserve origin and propagation identity where needed for accountability.

Offline availability is constrained by invariants: scarce resources may need online coordination or preallocated rights. Convergence is not proof of correctness. Tombstone retention, long-offline replicas, and reintroduction of erased information need explicit lifecycle semantics. Conflicts follow [CON-2](#con-2); delay follows [OFFLINE-2](#offline-2).

Applications synchronizing large retained datasets MUST define a risk-based policy for destructive or anomalous bulk-change propagation; a locally observed change is not automatically legitimate user intent. Consider mass rewrites, renames/deletions, unexpected encrypted/high-entropy replacements, unexplained bursts, and broad schema-invalidating changes where relevant. These signals are not proof of malware. Proportionate responses may pause propagation, stage/quarantine, reconcile, preserve permitted prior versions, or alert; no universal numeric threshold or fresh prompt for every bulk operation is required.

Where suspected compromise could propagate damage, the system MUST provide an appropriate containment route, such as sync pause, device revocation, replica isolation, read-only operation, connector disablement, or staged-import quarantine. Resume automatic propagation only after applicable validation/reconciliation under [RECOVER-1](#recover-1). Authorized bulk work and legitimate deletion/erasure remain supported under [AUTH-2](#auth-2) and [PRIV-1](#priv-1); containment is not indefinite retention authority.

Intentional logical deletion MUST propagate to supported synchronized devices so a reconnecting replica does not resurrect the deleted item. Preserve a minimal non-content tombstone or equivalent only as long as needed to coordinate permitted replicas. If an offline device has a competing unsynchronized edit, preserve it as a conflict version for review rather than silently discarding that work; distinguish this conflict handling from the user's authorized permanent deletion decision. Report remote erasure as pending while a device or backup medium is unreachable, and never claim to have deleted bytes outside the application's actual authority.

<a id="sync-2"></a>
### 20.2. SYNC-2 — Device continuity without a NAS

**Type:** ECOSYSTEM POLICY | **Origin:** USER POLICY | **Applies:** personal products requiring cross-device continuity

Without a NAS, supported laptops, desktops, phones, and tablets MUST retain applicable local operation under [OFFLINE-3](#offline-3). Such products MUST support direct device synchronization or another explicitly selected local-first synchronization mechanism, for example Phone ↔ Laptop or Phone ↔ Laptop ↔ Tablet. A permanent central cloud server MUST NOT be required merely to synchronize the user's own devices. Optional selected intermediaries remain subject to declared dependencies, privacy, and authorization. Conflicts, offline changes, unknown outcomes, integrity, retries, and recovery follow [SYNC-1](#sync-1), [OUT-1](#out-1), and [RETRY-1](#retry-1).

<a id="sync-3"></a>
### 20.3. SYNC-3 — Opt-in NAS synchronization hub

**Type:** ECOSYSTEM POLICY | **Origin:** USER POLICY | **Applies:** applicable personal products with a suitable NAS enabled by the user for shared synchronization

When a suitable NAS is available and the user enables this role, it MUST become the primary shared synchronization hub for application data. All applicable retained/shared data SHOULD synchronize to it according to the declared data scope, permissions, retention, and synchronization contract. Desktop, mobile, and tablet instances act as clients of that shared system while retaining appropriate local working copies. This policy does not silently upload data excluded by user scope, authority, or privacy rules.

The NAS MUST NOT become a hard requirement for ordinary offline work. Temporary disconnection MUST preserve applicable local operation; reconnection MUST synchronize and reconcile according to the declared consistency model and current authority. Primary hub placement does not by itself transfer ownership or make every local write a globally final commit. This enabled-NAS hub policy remains active; it does not finalize a universal authoritative-copy topology or require every device to hold the complete workspace. The App Plan must settle actual write authority and placement under [JSON-4](#json-4), without inferring a decision from the hub role. Distinguish local persistence, hub acknowledgement, and reconciliation under [OUT-1](#out-1). NAS storage/service, backup, and hosting roles remain distinct under [NAS-1](#nas-1).

<a id="sync-4"></a>
### 20.4. SYNC-4 — Safe topology transitions

**Type:** ECOSYSTEM POLICY | **Origin:** USER POLICY | **Applies:** applicable products transitioning between device-local/peer operation and a NAS synchronization hub

Products SHOULD support safe transitions between no-NAS local or peer operation and an enabled NAS hub. Adding a NAS MUST NOT require destructive migration or recreation of all user data. Removing or temporarily losing the NAS MUST NOT make the user's locally held data inaccessible. Appropriate working copies and documented availability still apply; a client cannot promise offline access to content it has never retained.

Authority transitions MUST define identity continuity, reconciliation of concurrent/offline changes, deletion handling, pending or unknown operations, and which participants may accept changes during and after the transition. Removing a hub deliberately MUST provide a preservation/transfer path for retained data needed by the chosen replacement topology; failures MUST report remaining unavailable data truthfully. Existing synchronization, migration, recovery, and authorization contracts apply. These are outcome requirements, not a mandated peer protocol, conflict algorithm, or central-cloud dependency.

<a id="s21"></a>
## 21. Reversal and recovery

<a id="recover-1"></a>
### 21.1. RECOVER-1 — Honest recovery semantics

**Type:** UNIVERSAL INVARIANT | **Origin:** DERIVED ENGINEERING RULE | **Applies:** undo, restoration, reversal, or compensation claims and recovery of important retained user state

Applications MUST describe actual recovery/compensation honestly and provide recovery where technically and operationally appropriate. Distinguish inverse mutation, transaction rollback, restoration, compensation, cancellation, reconciliation, and irreversible actions. Reversal MUST use current authority and constraints, not historical permission alone.

Communications cannot be recalled from recipients' knowledge. Refunds are separate effects; physical actions may be irreversible; APIs may need reconciliation. Restoring old global state MUST NOT be presented as safe undo without accounting for newer valid work. Expired/erased information may not be recoverable. Required reversal audit links to the original under [AUDIT-1](#audit-1).

For applications owning important retained user state, successful normal application startup MUST NOT be the only route to inspect, verify, extract, or recover otherwise recoverable information. Define an appropriate recovery route and its dependencies/limits in the App Plan, supported by proportionate evidence under [BACKUP-2](#backup-2) and [TEST-1](#test-1). A read-only recovery mode, independent reader, doctor tool, recovery executable, or documented portable inspection/export procedure may suffice. Neither a CLI nor a separate rescue application is required where the durable format already provides an adequate route. Recovery MUST preserve applicable authorization, privacy, and key-access constraints under [AUTH-1](#auth-1), [PRIV-1](#priv-1), and [BACKUP-1](#backup-1).

Recovery MUST distinguish corruption detection/diagnosis, derived-state rebuilding, verified canonical restoration, and canonical repair. It MUST NOT fabricate missing facts to claim a healthy state. When facts cannot be established, preserve uncertainty under [EVID-1](#evid-1), surface the problem, quarantine where appropriate, and stop destructive repair; [SAFE-1](#safe-1), [DATA-2](#data-2), and [EDIT-1](#edit-1) remain governing constraints.

Malware/ransomware recovery SHOULD, where applicable, contain affected clients/services, stop unsafe propagation, identify the best evidenced known-good canonical state/recovery points, validate backup integrity, restore or reconstruct canonical information, rebuild disposable derived state, reconcile legitimate newer information where safe, and rotate/revoke compromised credentials before validated sync resumption. Recovery MUST NOT overwrite the best surviving clean evidence merely for convenience. Recovery copies may themselves be corrupted, malicious, or already compromised; age or immutability does not establish cleanliness. Evidence and uncertainty follow [BACKUP-2](#backup-2) and [EVID-1](#evid-1), with privacy/deletion duties intact.

After an abnormal termination, the next application launch MUST promptly inspect pending transaction/recovery journal entries before treating affected files or dependent work as healthy. Prioritize the affected files and dependencies rather than triggering a full-workspace scan for every edit. Automatically complete recovery only when the committed state and proposed action are established as safe and correct; ambiguous, destructive or conflicting restoration requires an informed, current approval. If storage appears to be failing, limit unnecessary writes, preserve readable evidence, avoid compounding damage, and offer safe extraction or a separately chosen recovery destination where supported.

After successful verified recovery, retain the damaged original's exact bytes for at least 24 hours before ordinary cleanup eligibility. This minimum does not override an authorized permanent deletion or applicable privacy/legal erasure duty. Protect unresolved incident evidence, pinned history, and the sole recoverable copy beyond that period as their governing retention and deletion authority requires.

<a id="recover-2"></a>
### 21.2. RECOVER-2 — Prefer bounded reversibility

**Type:** DEFAULT | **Origin:** ARCHITECTURAL DECISION | **Applies:** mutations and consequential automation

Operations SHOULD offer scoped undo, reversible preparation, cancellation, or compensation where benefit justifies cost. Soft deletion may help; retention/privacy may require erasure. Communicate irreversible boundaries where relevant. Delegation can authorize automatic execution under [AUTH-2](#auth-2) and [AI-3](#ai-3) without repeated confirmation.

For retained user-owned data, destructive deletion SHOULD normally include a reversible stage where practical before permanent purge. Trash or pending-deletion state is one pattern, not a required directory. Explicit secure deletion, privacy/legal erasure, ephemeral/cache/temp data, safety/security needs, and other justified cases may require a different lifecycle. No indefinite retention is implied; [PRIV-1](#priv-1) and [SAFE-2](#safe-2) govern conflicting obligations.

For applicable personal workspaces, provide synchronized Trash with a **30-day default retention** that the workspace owner can change. Provide a distinct **Delete Permanently** action with one clear confirmation. It applies only within the application's authority and to app-controlled originals, Current JSON, version history, Trash, conflict copies and managed backup copies that are reachable and legally permitted to delete. Synchronize logical deletion so reconnecting devices do not resurrect deleted records; preserve only the minimum non-content tombstone or equivalent needed to coordinate deletion. Show erasure as pending while offline devices, disconnected media or inaccessible destinations prevent completion, and do not claim deletion from storage the application cannot reach. Permanent erasure follows [PRIV-1](#priv-1), not ordinary Trash expiry.

<a id="s22"></a>
## 22. Backup and restoration

<a id="backup-1"></a>
### 22.1. BACKUP-1 — Complete recovery dependency set

**Type:** CONDITIONAL | **Origin:** DERIVED ENGINEERING RULE | **Applies:** retained state with provided/claimed backup or recovery

Strategies MUST identify a consistent recovery point and complete dependency set for the promised result: potentially data, configuration, keys/key-recovery paths, audit evidence, schemas, readers, migration metadata, expensive derived artifacts, and external dependencies. Secrets need protection and recoverability, not indiscriminate packaging with public exports.

No directory inclusion list or derived-data exclusion applies universally. NAS/filesystem snapshots, OS backup, database-native, or application-native backup may be used. Understand snapshot scope and cross-store consistency. A copy in the same failure domain does not establish independent recovery.

For important retained data, the strategy MUST distinguish active copies, synchronized replicas, NAS hubs, snapshot/version history, and optional independently placed complete backups, and consider recovery copies not simultaneously destroyable through the same ordinary client credentials or failure mechanism. An individual workspace user MAY explicitly disable Complete On-Site Backup under [section 53](#s53); when OFF, document loss-of-drive exposure and never imply an independent backup is present. Document the chosen protection and residual risk proportionately. Immutable/write-protected history, offline/disconnected media, separately credentialed storage, append/versioned backup, or another justified isolation mechanism may fit; no topology is universally required. Ordinary client credentials SHOULD NOT automatically have unrestricted deletion authority over all independent backup generations unless genuinely required; separate retention/deletion authority where meaningful. Isolation does not override authorized erasure under [PRIV-1](#priv-1).

<a id="backup-2"></a>
### 22.2. BACKUP-2 — Recovery evidence

**Type:** CONDITIONAL | **Origin:** DERIVED ENGINEERING RULE | **Applies:** backup-readiness and recoverability claims

Claims MUST have documented, testable restoration and supporting evidence. Verify intended results, keys/dependencies, compatibility, and meaningful failure cases. Untested backups are unverified, not necessarily empty or legally nonexistent. State recovery-point/time expectations and untested limits.

Manifests/checksums can detect accidental corruption; adversaries may require protected evidence under [AUDIT-3](#audit-3). Verification SHOULD avoid active-data changes and restore tests SHOULD use safe destinations. Actual restore requires authority and accounting for later work/deletion policy.

For important retained data, restoration or equivalent recoverability MUST be validated at a proportionate cadence defined in the App Plan. A successful backup write alone is insufficient. Test/sample restores, isolated rehearsals, integrity/dependency verification, or another justified method must support the actual recovery claim; checksums alone do not establish that an application can use the restored state. Assess possible corruption, malicious content, and already-compromised backup state, using evidence to select the best available known-good recovery point and preserving uncertainty when cleanliness cannot be established. Older or immutable does not automatically mean clean; [RECOVER-1](#recover-1) governs safe recovery.

For Complete On-Site Backup, check source health before copying and do not replace the last healthy completed version with a source known to be corrupted. Automatically repair only faults whose safe correction is established by the declared contract; ambiguous repair needs informed approval. If the user requests an emergency readable partial copy, label it **Partial / Unverified**, show omissions and verification state, and do not count it as a completed backup or advance retention. Progress and resume state must reflect verified work actually completed.

<a id="s23"></a>
## 23. Import and export

<a id="io-1"></a>
### 23.1. IO-1 — Controlled ingestion and faithful export

**Type:** CONDITIONAL | **Origin:** DERIVED ENGINEERING RULE | **Applies:** import/export capabilities

Imports MUST validate format/domain constraints, define identity/conflicts, and prevent blind overwrite contrary to intent. Staging, skip, audited replacement, merge, or alternatives may be used. Track needed provenance without unrelated sensitive content.

Externally supplied data MUST be treated as untrusted until processed according to the application's risk model. This includes applicable downloads, email attachments, documents/media, archives, office files, plugin packages, NAS content, sync peers, APIs, and removable media. Controls may include format/type/magic validation, safe-path/traversal checks, archive-depth/expansion and decompression-bomb limits, size/resource limits, active-content restrictions, staging/quarantine, scanning, and restricted parsing under [SEC-1](#sec-1). Harmless bounded values need no expensive scanning without meaningful benefit. Parsing success or location in a data tree does not grant execution trust. Locale/time interpretation follows [DATA-4](#data-4) and [DATA-5](#data-5).

Controlled intake SHOULD provide risk-appropriate inspection/staging, validation using the relevant controls above, duplicate/identity/provenance resolution, commit, and operation receipts where needed. These are applicable safeguards, not mandatory heavyweight quarantine or a fixed physical pipeline for every tiny input.

For externally supplied files, [IO-2](#io-2) defines the preferred logical Raw/Intake boundary; [IO-3](#io-3) governs applicable malware-verification state and [SEC-6](#sec-6) the replaceable local scanning capability.

Exports presented as copies MUST NOT silently mutate/delete sources. An intentional move or export-and-delete needs separate effect semantics and authority. Exports MUST document scope, omissions, transformations, consistency point, and format, distinguishing archival fidelity from presentation. Apply [PRIV-1](#priv-1).

A portable-exit claim MUST preserve the declared meaning, not merely copy bytes: applicable stable IDs, relationships, metadata, provenance, originals, annotations, history, and schema definitions may be needed. Disclose what the target format cannot represent; silently dropping meaning MUST NOT be called lossless export. An ordinary export is an output snapshot, not a new write authority. Editing it does not mutate canonical state without an explicit validated re-import/adoption operation under [EDIT-1](#edit-1).

Canonical snapshots, human-readable reports, interchange formats, and diagnostics are useful categories, not four required features. JSON, Markdown, CSV, documented databases, and open binary formats serve different purposes. Scheduled export is optional unless the selected preservation contract relies on it.

For user-managed imports or externally detected files, offer context-appropriate choices such as **Keep** (adopt or leave in place under the defined ownership contract), **Delete** (only with the applicable deletion authority), **Remove from management** (stop managing the item without implying its bytes were deleted or moved), and **Hibernate** (move or place it in a safe holding location selected by the user). Explain each effect and validate the chosen source/destination before action. A verified Copy or Move import checks identity, contents and required metadata before declaring success; preserve stable logical identity across path changes where the contract permits. Recommend sensible destinations where useful, but do not override the user's selected workspace root.

<a id="io-2"></a>
### 23.2. IO-2 — Untrusted Raw intake, promotion, and quarantine

**Type:** ECOSYSTEM POLICY | **Origin:** USER POLICY | **Applies:** applications ingesting, receiving, downloading, synchronizing, or otherwise accepting externally supplied file-like content

Such applications SHOULD expose a dedicated logical Raw/Intake/Staging area; `Raw/` is the preferred human-readable name where it fits the design. The boundary may be a directory, managed store, or equivalent logical state; no universal physical name or hierarchy is required. Content entering it MUST initially be untrusted regardless of location inside application-owned data. File-ingesting applications SHOULD prefer this boundary together with the local malware-intake pipeline in [IO-3](#io-3) and [SEC-6](#sec-6), proportionate to actual protection benefit. Applications without relevant file intake need no empty Raw directory, scanner, quarantine UI, or signature infrastructure.

Before promotion to ordinary managed/canonical content or risky normal processing, the required configured intake policy MUST succeed. Define relevant gates explicitly: malware verification, format/security validation, identity/provenance resolution, core validation, and authorized adoption under [IO-1](#io-1) and [AUTH-1](#auth-1). Not every input needs every step; isolated intake analysis is distinct from ordinary trusted processing. Pending, failed, stale, or unavailable verification MUST NOT silently satisfy a required gate. Bind promotion to the actual verified content/version and current applicable policy; intervening changes invalidate unsupported verdict reuse under [CON-1](#con-1).

A scanner detection alone MUST NOT automatically destroy retained source content. Quarantine/isolation SHOULD be the default response. Quarantined objects MUST NOT execute, receive ordinary trusted parsing, be automatically promoted, or be represented as clean canonical content. Authorized inspection/recovery may remain available through appropriate restricted mechanisms. Permanent deletion requires explicit policy/user authority or applicable security/privacy obligations under [PRIV-1](#priv-1) and [SAFE-2](#safe-2). A folder named `Quarantine/` is not sufficient isolation: the App Plan MUST choose risk-appropriate controls such as restricted access, non-executable storage, exclusion from normal import paths, renamed/encapsulated representation, or isolated storage.

Promotion need not delete the Raw original. Retained originals may support evidence, provenance, reproduction, or recovery under [DATA-3](#data-3), but remain subject to untrusted-content handling and retention/privacy policy. A derived canonical record does not authorize executing or reinterpreting its original, and canonical authority does not mean malware safety under [DATA-1](#data-1).

<a id="io-3"></a>
### 23.3. IO-3 — Incremental malware verification and visible scan state

**Type:** ECOSYSTEM POLICY | **Origin:** USER POLICY | **Applies:** applications with Raw/Intake malware-verification workflows

At each application start/open, every Raw/Intake object's malware-verification validity MUST be evaluated. Applications SHOULD automatically initiate this as a non-blocking background check, keeping normal UI startup responsive rather than waiting for full historical scans. Incremental inventory, trustworthy content/version evidence, bounded queues, backpressure, resumable work, and priority for new/unverified content SHOULD keep the workflow within [DEV-16](#dev-16)'s lifetime envelope. Evaluation may proceed incrementally in the background; objects whose required validity has not been established remain gated under [IO-2](#io-2).

Unchanged content need not be byte-rescanned on every launch. The App Plan MUST define verdict reuse, staleness, and rescan policy using relevant object identity, content hash or equivalent version evidence, size/version, scanner implementation/engine, signature database, policy version, scan time, and result. Do not rely on untrusted mutable metadata beyond its evidence contract. New or materially changed Raw objects SHOULD be queued promptly while running, without waiting for restart. Required scanning MUST precede risky normal processing; scanner work itself remains restricted under [SEC-1](#sec-1).

Use explicit states equivalent to **UNSCANNED, QUEUED, SCANNING, CLEAN, DETECTED, SUSPICIOUS, SCAN_FAILED, UNSUPPORTED, SIGNATURES_STALE, SCANNER_UNAVAILABLE, and QUARANTINED**, as relevant; exact labels and whether these are separate state dimensions may vary. Failure to scan MUST NOT equal clean. CLEAN means no threat detected under the recorded scanner/engine/signature/policy state, not guaranteed safety. Format validation, sandboxing, least privilege, resource limits, and active-content restrictions still apply. Scanner failure MUST NOT corrupt canonical state; expose failure/unavailability truthfully and support retry/recovery through the core's existing mutation contracts.

Unavailable scanning or signature updates MUST NOT unnecessarily disable independent local capabilities under [OFFLINE-3](#offline-3). Required intake gates remain enforced for affected content; degraded offline protection must be reported honestly rather than silently bypassed or represented as current.

Where a verdict controls processing/promotion, retain proportionate scan evidence bound to the relevant object/content: ID, hash/version, scanner/engine, signature/policy versions, timestamp, verdict, threat/signature name where detected, and failure reason where applicable. Receipts may reuse [OPS-1](#ops-1) and applicable audit records. Classify authority/retention under [DATA-1](#data-1) and [PRIV-1](#priv-1); transient progress is not automatically canonical, while evidence required for promotion must remain available for its declared lifecycle.

Signature-based scanning MUST distinguish current, stale, unavailable, and failed-update conditions, without presenting degraded state as full current protection. Support appropriate local database maintenance; for ClamAV, `freshclam` or an equivalent managed mechanism SHOULD update signatures without unnecessarily blocking normal startup. The App Plan MUST define freshness and risk-based rescanning after relevant changes, considering object risk, scan age, content changes, engine/signature/policy changes, threat intelligence, and performance. New signatures may invalidate prior confidence but do not universally require full-library rescans after every minor update. Signature delivery remains subject to [SEC-3](#sec-3)'s integrity/trust discipline.

Background scanning MUST expose appropriate non-blocking status in the relevant interface: progress/pending items, degraded protection, detection/quarantine, scanner unavailability, and completion. Desktop/mobile UI or headless structured health/progress may satisfy this; no literal bottom bar is prescribed. Routine success SHOULD stay unobtrusive, with proportionate prominence for detections, scan failures, unavailable scanners, materially stale signatures, and blocked/unverified content. Applicable accessibility follows [UI-3](#ui-3).

The App Plan MUST specify whether unscanned Raw content, quarantine state, and scan verdicts synchronize, whether receiving devices rescan, and how scanner/version differences affect trust. A remote CLEAN verdict MUST NOT become permanent universal trust without deliberate receiving-device policy; receivers may require local rescanning. [SYNC-1](#sync-1), [NAS-1](#nas-1), privacy, and containment rules still apply. Synchronization or preservation of untrusted bytes does not itself authorize promotion or ordinary processing.

<a id="s24"></a>
## 24. Schema evolution and migrations

<a id="migrate-1"></a>
### 24.1. MIGRATE-1 — Versioned, recoverable evolution

**Type:** CONDITIONAL | **Origin:** DERIVED ENGINEERING RULE | **Applies:** persistent format/schema evolution

Migrations MUST be explicit, versioned, and testable with defined dependencies/order, preconditions, interruption, and recovery. Define exclusive versus online execution, compatibility windows, concurrent writers, rollback/roll-forward, snapshot role, restoration boundary, and failure classification. Resource preflights cannot prove future allocation succeeds.

Consistent snapshots/backups are useful safeguards; a local full copy is not required for every migration. Failure MUST NOT cause unconditional snapshot restoration. Determine whether rollback succeeded, work remains partial, newer writes exist, or forward recovery is needed. Restoration requires authority over the real loss boundary. Restricted/read-only operation may be appropriate during recovery.

Retry safety may come from idempotent steps or a correctly recorded execution protocol. Safe downgrade may be unavailable; do not invent a non-destructive `down()` when information has been lost.

For a retained-data JSON schema migration such as Current JSON V1 to V2, use three distinct verification gates before adoption: (1) stage and transfer/convert the complete applicable data while preserving V1; (2) independently validate V2 syntax, schema, semantic completeness, data fidelity and recoverability; and (3) separately compare the completed V2 result against preserved V1 and the declared transformation requirements. Adopt V2 only after all gates pass. On failure, preserve V1 and make only a bounded safe retry when it tests a meaningful correction; persistent failure stops migration and reports the issue. Never silently discard unfamiliar fields or historical relationships. This does not prescribe a universal physical migration algorithm.

<a id="migrate-2"></a>
### 24.2. MIGRATE-2 — Semantic compatibility

**Type:** CONDITIONAL | **Origin:** DERIVED ENGINEERING RULE | **Applies:** evolving persistent formats and protocols

Compatibility MUST be explicit. Unknown fields/new semantics MUST NOT be silently accepted then destroyed or misinterpreted. Define readable, preservable, transformable, and writable versions; reject unsafe writes or require supported migration. Liberal acceptance is not a blanket persistence rule. Tolerant reading may work when content is preserved safely and constraints remain understood.

An older application MUST NOT silently write or downgrade a newer data/workspace format it does not understand. If safe compatibility cannot be established, use a supported read-only, export-only, migration-required, or refusal mode as appropriate; do not offer even read/export behavior as faithful unless its contract can be met. Unknown newer fields MUST NOT be silently discarded.

<a id="s25"></a>
## 25. Security, secrets, and dependencies

<a id="sec-1"></a>
### 25.1. SEC-1 — Threat-based boundaries and exposure

**Type:** CONDITIONAL | **Origin:** DERIVED ENGINEERING RULE | **Applies:** resources exposed to actors or networks

Controls MUST reflect principals, reachable surfaces, protocols, deployment, and threats, including relevant local processes, supply-chain inputs, network devices, and prompt injection. Localhost, LAN, or VPN membership alone does not establish application identity/authority. Least privilege means minimum effective authority for the role; backup/credential workers can need broad controlled access.

Local apps SHOULD bind local services to loopback by default. Network services may use intended interfaces, including containers, with explicit secure deployment. Authentication, authorization, transport protection, browser-origin defenses, and rate limits MUST match exposed operations/data. Deliberately public data may have public access semantics; private LAN location does not justify sensitive unauthenticated access. CORS/WAFs are not universal protocol controls; CORS is not general authorization.

Where relevant, the threat model MUST address malware/ransomware, malicious imports/archives/external content, compromised parsers/plugins/updates/dependencies, and unauthorized local processes through defense in depth. Antivirus/endpoint protection may contribute but is not the whole contract. High-risk parsing, previewing, extraction, conversion, transcoding, and rendering SHOULD run with the minimum authority reasonably required, using process isolation, sandboxing, restricted filesystem views, reduced privileges, bounded network access, resource limits, or disposable working space where technically practical. Processing one object SHOULD NOT automatically expose the entire archive, backups, secrets/credentials, NAS administration, arbitrary network services, or unrelated data.

Substantial retained-data applications MUST assess and limit unnecessary compromise propagation from a client, parser, optional subsystem, plugin, or AI tool to all data, replicas, NAS history, backups, and secrets. Use the existing capability model under [AUTH-1](#auth-1): an indexer needs no unrelated remote-write authority, a media parser needs no backup-deletion rights, and ordinary UI/sync need no automatic destructive backup-management or NAS-admin privilege. Presence inside a retained-data tree MUST NOT make content trusted executable code. Distinguish data from executable extensions; scripts/macros/binaries discovered as ordinary data MUST NOT execute merely because of location. Executable extensions require an explicitly trusted installation/activation process or equivalent authority boundary.

Document trust assumptions and residual risk: controls reduce likelihood and blast radius; they do not guarantee virus-proof software, malware-free snapshots, or containment against a fully compromised OS/root/admin. Hashes and sandboxes alone do not establish malware immunity. Encryption at rest primarily addresses access to protected storage without an authorized unlocked session, including lost/stolen media or offline theft; malware with equivalent authority in an unlocked session may still read data. Encryption does not replace least privilege, isolation, safe parsing, integrity verification, independent recovery, or backup protection. Malware controls likewise do not replace appropriate privacy encryption; they address different threats.

<a id="sec-2"></a>
### 25.2. SEC-2 — No accidental secret disclosure

**Type:** PROHIBITION | **Origin:** DERIVED ENGINEERING RULE | **Applies:** secrets and security credentials

Applications MUST NOT disclose usable secrets through unintended source control, logs, prompts, exports, or interfaces. Storage/delivery MUST match threats and permit appropriate revocation/rotation. Credential stores, managed services, protected configuration, and environment injection are options. Restricted plaintext local files may suit a bounded threat model; they do not isolate all same-account processes. Environment variables also have exposure paths.

Ignore rules and permissions are not complete access or history-erasure controls. Disclosures need appropriate containment, including revocation where needed. Removing a file from a current tree does not remove every historical copy.

<a id="sec-3"></a>
### 25.3. SEC-3 — Dependency and build discipline

**Type:** ECOSYSTEM POLICY | **Origin:** ARCHITECTURAL DECISION | **Applies:** released application builds and third-party dependencies

Released builds MUST record a reproducible dependency-resolution strategy appropriate to their toolchains, preserving integrity/trust checks. Library version ranges may coexist with reproducible test/release environments. Assess dependencies by function, provenance, maintenance, vulnerabilities, license, transitive cost, and replacement feasibility. Short handwritten security/parsing code is not inherently preferable.

Use supported lock/resolution mechanisms and review updates. `go.sum` records checksums; it alone is not an exact Go dependency lock model, which also involves `go.mod` and resolution semantics. Rust ownership checks and `Cargo.lock` do not establish trust. Vulnerability review SHOULD be proportionate and recurring; CVE scans cannot prove absence of defects.

Protect software delivery proportionately through dependency provenance, controlled resolution, source/release integrity verification, appropriately verifiable packages/updates, restricted build/release authority, vulnerability response, and review of critical third-party changes. No one signing system, SBOM format, package manager, or scanner is mandated. Automated updates MUST verify authorization and integrity before execution using an appropriate platform mechanism; arriving through the update path is not trust evidence by itself. Update failure MUST NOT silently authorize destructive data migration; [MIGRATE-1](#migrate-1) and [MIGRATE-2](#migrate-2) still apply. Reconstruction and material dependency-disappearance dispositions follow [SEC-5](#sec-5).

<a id="sec-4"></a>
### 25.4. SEC-4 — Vendored or forked foundation provenance

**Type:** ECOSYSTEM POLICY | **Origin:** USER POLICY | **Applies:** third-party source snapshots vendored or forked as meaningful application foundations

Projects MUST preserve durable provenance appropriate to the foundation: upstream project/repository, version/tag where applicable, exact commit/revision, source digest where appropriate, license/notices, import date, acquisition method, local modification boundary, and maintenance/update strategy. When source identifiers differ, record an equivalent exact snapshot identity rather than inventing a commit.

Explicitly decide whether the project tracks upstream, selectively merges changes, or owns a fixed independent fork/snapshot. Do not leave that maintenance responsibility ambiguous. This does not require vendoring dependencies; foundation evaluation follows [DEV-3](#dev-3) and dependency safety follows [SEC-3](#sec-3).

<a id="sec-5"></a>
### 25.5. SEC-5 — Release reconstruction and critical-dependency continuity

**Type:** ECOSYSTEM POLICY | **Origin:** USER POLICY | **Applies:** software built/distributed as executables, and dependencies whose disappearance materially threatens building, operation, migration, recovery, or maintenance

Projects producing executable software MUST preserve durable instructions and inputs sufficient to reconstruct a supported release or equivalent functioning build where reasonably practicable. Record applicable source revision, toolchain/compiler/runtime requirements, build commands, dependency resolution/locks, required build-time assets and generated-code steps, platform prerequisites, packaging/signing procedures, release provenance, and known limits. A future maintainer MUST NOT need undocumented tribal knowledge to determine how a supported release is produced. A tiny utility may satisfy this with concise prerequisites, its source revision, and one deterministic build command; larger distributions need proportionate detail and evidence under [TEST-1](#test-1).

For critical frameworks, runtimes, SDKs, toolchains, package ecosystems, libraries, required local services, model runtimes/providers, APIs, or platform components, the App Plan MUST record a proportionate disappearance-risk disposition where material. Options include replacement paths, interface boundaries, preserved source/vendor snapshots, migration/archive strategies, supported alternatives, or deliberately accepted dependency risk with applicable authority. Match treatment to criticality, replaceability, maintenance burden, license, security, and intended lifetime. Existing selection and foundation provenance follow [SEC-3](#sec-3) and [SEC-4](#sec-4).

State material reconstruction limits honestly, including proprietary SDKs, unavailable signing systems, hardware, closed platforms, discontinued services, and legal restrictions where relevant. No perpetual rebuild guarantee, bit-for-bit reproducibility, mandatory SBOM format, universal vendoring, permanent toolchain-binary retention, or archive of every historical release is required. Preservation does not require continued use of vulnerable obsolete components; distinguish preserved reference material from safe supported execution. No mandatory cloud build infrastructure is introduced. Protect signing secrets and respect access/retention constraints under [SEC-2](#sec-2) and [PRIV-1](#priv-1).

<a id="sec-6"></a>
### 25.6. SEC-6 — Replaceable native malware-scanning capability

**Type:** ECOSYSTEM POLICY | **Origin:** USER POLICY | **Applies:** applications/security components benefiting from file malware detection

Projects SHOULD evaluate and prefer ClamAV as the default open-source malware engine where platform support, licensing, distribution, performance, and threat-model benefit are suitable. ClamAV is replaceable, not canonical architectural authority. Product code MUST depend on a generic malware-scanning capability boundary; engine-specific details belong in the adapter, not core product semantics. A suitable alternative or supplementary engine MAY be deliberately selected with documented rationale without requiring an exception merely for replacing this preferred implementation. Selection, platform adapters, and any explicitly designed multi-engine pipeline MUST comply with [NOFALL-1](#nofall-1)–[NOFALL-2](#nofall-2): engine failure MUST NOT trigger substitute execution or turn an unmet scan gate into success. A future engine replacement follows deliberate planning, migration, and verification; it is not a hidden runtime fallback. Typed operations such as `scan_object`, `scan_stream`, `query_scan_status`, and `quarantine`, or equivalent contracts, preserve core-controlled authorization, outcomes, and promotion.

Scanning SHOULD execute locally on the user's device or authorized local infrastructure. Ordinary scanning MUST NOT require uploading private files to a cloud scanner; cloud scanning may only be an explicitly authorized optional capability under [PRIV-2](#priv-2). Where practical, prefer a constrained scanner process/service behind protected local IPC for crash isolation, resource limits, bounded filesystem/network access, privilege separation, replaceability, and security updates. Direct library integration remains permissible with technical and licensing justification; neither integration mechanism is universal. [SEC-1](#sec-1) and [AUTH-1](#auth-1) still govern effective boundaries.

For `clamd` or equivalent daemons, the scanner interface MUST remain local/protected unless an explicitly secured architecture justifies another deployment. Unauthenticated TCP listeners MUST NOT be exposed to the public Internet or untrusted networks. Prefer protected local sockets/IPC, constrained loopback, or equivalent platform transport; locality alone does not supply authorization. Preserve declared Windows, macOS, Linux, and other product targets under [PORT-3](#port-3); Linux-only ClamAV on-access functionality MUST NOT become a universal dependency. Platform-specific adapters may differ behind the capability contract. Scanning/signature failure follows [IO-3](#io-3) without giving the scanner canonical mutation authority.

When a ClamAV source archive is incorporated into an application or shared security component, record its version, upstream source/repository, exact revision if available, archive/source digest, license/notices, acquisition/import date, local modifications, build configuration, and update strategy under [SEC-4](#sec-4) and [SEC-5](#sec-5). Preserve modification history; do not silently alter vendored security source. Before distribution, verify the actual integration and redistribution model against applicable GPLv2 obligations and relevant bundled-component licenses. This policy does not establish that a particular archive, linking/process arrangement, or distribution is compliant. Importing a foreign-language engine remains governed by [LANG-1](#lang-1)'s dependency/artifact scope; it does not justify independently rewriting the shared Rust product core.

<a id="sec-7"></a>
### 25.7. SEC-7 — Optional workspace encryption and key recovery

**Type:** ECOSYSTEM POLICY | **Origin:** OWNER-APPROVED CANDIDATE | **Applies:** applications offering additional at-rest encryption for retained workspaces

Additional workspace encryption is OPTIONAL; it is not forced on every user. When offered and enabled, use established cryptography and secure random per-workspace cryptographic keys, with documented formats, protected key handling and supported recovery dependencies. A product offering workspace encryption MUST provide an appropriate portable USB/SSD key-file recovery method and a strong generated recovery secret; platform-specific APIs may adapt access, but any target lacking a trustworthy supported method MUST be disclosed and MUST NOT claim portable recovery. A six-digit PIN MAY unlock a trusted device through suitably protected, rate-limited local key storage; it MUST NOT be the sole cryptographic protection for a portable key file. Do not use one global secret whose compromise exposes every workspace.

Preserve cross-device recovery only where it is genuinely supported and tested; do not claim recovery beyond the available key copies and platform access. Do not add a backdoor or claim that ordinary security-question answers can reconstruct a lost strong cryptographic key. Security questions may serve supplemental identity verification only. Their precise role and the complete PIN-loss fallback flow remain **DEFERRED FOR OWNER DISCUSSION** and MUST NOT be represented as adopted key-recovery methods. Encryption remains subject to [SEC-1](#sec-1), [SEC-2](#sec-2), [PRIV-1](#priv-1), and the truthful recovery limits in [BACKUP-1](#backup-1).

<a id="s26"></a>
## 26. Configuration, observability, and runtime lifecycle

<a id="run-1"></a>
### 26.1. RUN-1 — Explicit configuration and defaults

**Type:** DEFAULT | **Origin:** ARCHITECTURAL DECISION | **Applies:** configurable applications

Applications SHOULD separate environment-specific settings from portable logic and define deterministic resolution/validation. Built-in defaults are legitimate. CLI, environment, deployment file, user preferences, defaults is an illustrative order; managed policy may be non-overridable. Surface relevant effective non-secret settings and use supported host discovery or explicit configuration. Changing configuration does not imply environments have equivalent capabilities.

For applicable retained-data applications, keep backup, version-history, verification, recovery and privacy-related controls discoverable under **Settings → Data Management**. Keep the overview and ordinary actions simple; provide optional technical detail for complex mechanisms. Offer appropriate manual verification or repair actions only with truthful status and safe authorization. Surface warnings for material problems rather than flooding users with routine notices.

<a id="run-2"></a>
### 26.2. RUN-2 — Proportionate diagnostics

**Type:** CONDITIONAL | **Origin:** DERIVED ENGINEERING RULE | **Applies:** failure reporting and operations

Applications MUST provide sufficient outcome/failure information without unnecessary sensitive exposure. Expected conditions differ from faults; a best-effort cleanup failure may need no stack trace, but material loss or a failed commit MUST NOT be hidden. Logs need bounded resources and appropriate retention.

Structured logging, correlation IDs, metrics, and health endpoints SHOULD be used where helpful; short-lived tools may need only exit status and diagnostics. Separate liveness, readiness, and deeper checks. Ordinary probes SHOULD be lightweight/non-destructive. Read-only probes cannot guarantee future writes; deliberate synthetic writes need explicit scope and cleanup.

Retained-data applications MUST provide one lightweight cross-platform structured logging gateway, preferably using the shared Rust implementation where technically feasible. Routine diagnostic logs and security/audit events MUST NOT contain plaintext file contents, passwords, PINs, cryptographic keys or recovery secrets. Logs and audit events MUST be metadata-only and private by default. Default diagnostic retention is **14 days**, with resource-conscious platform adaptations; important audit/event records use separate, bounded, purpose-justified retention. Crash-recovery transaction journals have a distinct recovery purpose and MUST NOT be pruned merely because diagnostic retention expired while a transaction remains unresolved. Retain only necessary non-content synchronization/deletion evidence under the applicable privacy lifecycle. Event storage MUST be access-controlled; state its tamper-verification limits honestly. A compatible OpenTelemetry-style event schema is acceptable; no server, cloud collector or heavy telemetry service is required.

Where supported products provide **Settings → Data Management → Recovery History**, show what happened, when, its status/outcome and whether user action is needed. Offer expandable technical detail and a privacy-safe exported report; do not export secrets or unnecessary file content. Allow users to compare selected historical versions and restore selected content with meaningful highlighted differences where supported. Stage and verify a restoration before changing current data, preserve the current version until the replacement is verified, preflight temporary capacity, pause safely when it is insufficient and offer another destination where supported.

<a id="run-3"></a>
### 26.3. RUN-3 — Declared deployment and bounded lifecycle

**Type:** CONDITIONAL | **Origin:** DERIVED ENGINEERING RULE | **Applies:** supported deployment modes and persistent services

Applications MUST document supported runtime modes. Native binaries, desktops, mobile/browser runtimes, services, and OCI images are options, not universal simultaneous requirements. Container identities, mounts, permissions, and isolation must fit their role; packaging does not establish NAS semantics.

Startup MUST verify prerequisites for safe operation, including relevant schema compatibility/exclusivity. Read-only software need not demand writable canonical storage. Preflight success does not replace runtime handling. Shutdown SHOULD stop new work, complete or safely interrupt work, and flush/close according to contract within appropriate bounds. Crash safety cannot depend solely on graceful shutdown. Exit status and diagnostics MUST reflect material failures; process exit alone does not prove effects completed.

When a user closes an application while mandatory Current JSON synchronization or another protected save operation is running, offer a visible **Finish & Close** lifecycle. On desktop, minimize when practical, prevent further edits and lock or optionally obscure only that application's own interface while its approved operation completes, show truthful progress if reopened, and close after safe completion is verified. Never blur or lock the operating system's entire screen. A visible post-close worker requires explicit approval, must stop after its authorized task, and must not run indefinitely without explanation. On Android and iOS, use only permitted background execution: the operating system may suspend or terminate work, so guarantee crash-safe persistence and later inspection/resumption rather than guaranteed completion in the background. If work fails or stalls, preserve safe data, use bounded handling, and show a clear issue on next access; do not leave indefinite UI lockouts.

<a id="run-4"></a>
### 26.4. RUN-4 — Compact, truthful save and synchronization status

**Type:** ECOSYSTEM POLICY | **Origin:** OWNER-APPROVED CANDIDATE | **Applies:** retained-data applications with visible save or synchronization work

Provide a compact bottom status bar, inspired by the functional simplicity of Windows 7-era desktop media applications and adapted to each platform's native interaction conventions, that shows original saving and mandatory JSON synchronization state without creating a bulky permanent dashboard. Clicking or tapping it expands the relevant original-file durability, per-file Current JSON, per-folder Folder JSON, verification, pending work and optional backup details. Use a percentage only when progress is measurable; otherwise show a precise state. Never label the whole workspace “Saved” while required JSON or recovery work remains pending. This supplements [OUT-1](#out-1) and [RUN-2](#run-2); it does not change their outcome contract.

<a id="s27"></a>
## 27. Verification and evidence

<a id="test-1"></a>
### 27.1. TEST-1 — Evidence appropriate to the claim

**Type:** UNIVERSAL INVARIANT | **Origin:** DERIVED ENGINEERING RULE | **Applies:** claimed application guarantees

Applications MUST verify claims with evidence appropriate to scope, risk, and failure model. Important claims require relevant failure, recovery, concurrency, migration, portability, security-boundary, AI-capability, and NAS-mode checks where those capabilities exist. Record tested configurations and distinguish passed, failed, skipped, unrun, and unsupported outcomes. A syntactic checklist does not prove semantics.

Each applicable application MUST provide or adopt a reusable **Universal Rules Test Suite** with shared conformance cases plus platform-specific and application-specific cases. It MUST test real restoration success and resulting data fidelity, not only file existence or valid JSON parsing. Its applicable cases MUST include crashes/interruption before, during and after material transaction stages; hostile paths, traversal, symlinks/reparse points, permissions, stale writers and races; tampered manifests, corrupted JSON and manipulated backups; storage disconnect/reconnect and insufficient space; and representative real supported storage, including HDD, SSD, removable USB and NAS where applicable. Before release, measure representative performance and capacity on the lowest practical supported devices and disclose tested configurations and limits. These cases extend, rather than replace, [WORKSPACE-TEST-1](#workspace-test-1), [WORKSPACE-TEST-2](#workspace-test-2), and platform-specific acceptance criteria.

Non-AI apps need no AI tests; stateless formatters need no backup tests; NAS backup does not imply raw network-database support. Reuse engine/platform evidence only within its assumptions and verify integration. Tests reduce uncertainty rather than establish absence of all defects.

<a id="test-2"></a>
### 27.2. TEST-2 — Practical verification patterns

**Type:** RECOMMENDATION | **Origin:** DERIVED ENGINEERING RULE | **Applies:** development/release verification choices

Automation SHOULD cover critical transitions, interfaces, interruption points, authority boundaries, and representative workflows. Examples: concurrent edits, stale lease holders, disconnect after commit before acknowledgement, audit/outbox recovery, deletion then restore, incompatible schemas, and revoked queued authority. Use actual targets where needed; an emulator cannot certify every NAS appliance.

A shared conformance harness MAY help inspect declared applicability, links, schemas, and selected guarantees. It SHOULD measure behavior rather than prescribed filenames. Destructive tests need isolated fixtures and scope; a documentation rule does not authorize inspection or mutation of unrelated applications.

<a id="s28"></a>
## 28. Documentation, exceptions, and ratification

<a id="gov-2"></a>
### 28.1. GOV-2 — Proportional living contracts

**Type:** ECOSYSTEM POLICY | **Origin:** USER POLICY | **Applies:** ecosystem repositories

Documentation MUST describe actual behavior, guarantees, assumptions, support, and limits. A concise README can cover a tiny tool; larger systems need relevant ownership maps, storage/authority contracts, AI capabilities, NAS configurations, recovery/migration, deployment, and evidence. Unimplemented aspirations MUST NOT be presented as existing behavior.

Machine-readable contracts SHOULD be maintained where they improve interoperability/enforcement. Schema generation reduces drift but does not prove runtime semantic or authorization agreement. Record significant tradeoffs and governing clauses. This constitution is primary; ADRs, reviews, and examples cannot silently strengthen it.

The specific development-governance obligations in [section 31](#s31) apply alongside this proportionality rule. Concise or combined records may satisfy them; proportionality does not waive idea refinement, the Plan Freeze Gate, current Project State, or phase conformance. The required machine-readable and human-readable Project State is governed by [DEV-9](#dev-9), not left optional by the general recommendation above.

<a id="gov-3"></a>
### 28.2. GOV-3 — Policy authority and exceptions

**Type:** ECOSYSTEM POLICY | **Origin:** USER POLICY | **Applies:** policy decisions, deviations, and ratification

The repository owner/user is ultimate policy and ratification authority unless explicitly delegated. AI reviewers may recommend, challenge, draft, and verify, but cannot independently ratify. No governance board is presumed.

Formal exceptions to ecosystem policies, prohibitions, explicitly mandatory defaults, or genuine exceptional conflicts involving invariants MUST record rule ID, component/scope, technical reason, risk, mitigation, relevant duration/permanence or review trigger, and actual approving authority with approval evidence. Proposed exceptions are not approved. Scoped prior delegation can authorize decisions without repeated prompts.

Exceptions MUST be reconsidered when they expire, their assumptions materially change, their technical rationale disappears, or the requested scope changes. They may be renewed, replaced, superseded, or withdrawn by the applicable authority, with the disposition and affected scope recorded. Expiry does not silently renew approval, and changed scope is not automatically covered. When coverage lapses, record the resulting deviation and a proportionate resolution or transition; do not claim conformance or force unsafe immediate changes to deployed systems. Standing or enduring exceptions need no arbitrary periodic review when no expiry or material trigger applies.

Ordinary DEFAULT alternatives need a proportionate rationale, not impossibility proof or formal exception unless their clause expressly requires one. RECOMMENDATION alternatives need no exception. Material CONDITIONAL non-applicability should be documented without requiring approval. Rust-first and applicable NAS/feature-first departures follow formal policy governance; folder-name variation within feature-first does not.

An exception MUST NOT present an unmet engineering guarantee as satisfied. A real domain conflict needs revised scope, affected claims, residual risk, and authority under [SAFE-2](#safe-2). Approval cannot waive physical constraints or applicable legal obligations by declaration.

<a id="gov-4"></a>
### 28.3. GOV-4 — Reviewable evolution

**Type:** ECOSYSTEM POLICY | **Origin:** USER POLICY | **Applies:** constitutional changes and adoption

Changes MUST preserve reviewability through recorded versions, rationale, affected rule IDs, and evidence. Candidate status MUST remain explicit until owner ratification. Adoption should identify exact revision and applicability date. Preserve historical reviews rather than rewriting findings to fit the result. Substantive changes need appropriate adversarial review and disposition. Changes here do not authorize automatic migration or assessment of governed repositories.

Constitutional work MUST use recorded actual authority for integration, freeze, review, scoped repair, publication, and adoption; one authorization may explicitly cover several stages. Do not require repetition of authority already supplied, infer ratification from publication, or treat a historical one-time waiting phrase as a perpetual gate. The 2026-10-17 RC4 owner mission reopens design for its settled workspace decisions and authorizes integration, identifiable candidate review under the existing freeze procedure, substantiated repairs, commit/push, and safe non-destructive publication/promotion within repository protections; [section 51](#s51) records that current scope. The 2026-10-14 mission remains historical authority for rc3. It expressly withholds ratification. [Section 42](#s42) supplies the complete operating procedure and [section 43](#s43) records scope/provenance.

The application Plan Freeze Gate in [DEV-5](#dev-5) remains separate from constitutional freeze. A constitutional candidate MUST have an identifiable frozen revision and owner authority before Red review; current-session or durable prior scoped delegation may supply that authority. Substantive revisions invalidate previous review credit and require the current convergence process under [GOV-5](#gov-5). Changes to this constitution do not authorize inspection, migration, or modification of unrelated application repositories.

Historical ADRs, reviews, freeze/repair receipts, and provenance remain accessible through immutable links in [section 43](#s43). Their former no-push, no-review, or completion-phrase restrictions describe their own authorized task, not a veto over the owner's later explicit authorization. Historical section numbers refer to their own baseline.

<a id="gov-5"></a>
### 28.4. GOV-5 — Green Flag, Red Flag, and review convergence

**Type:** ECOSYSTEM POLICY | **Origin:** USER POLICY | **Applies:** constitutional candidate integration, frozen-candidate attack, repair, and ratification recommendations

**GREEN FLAG** researches, integrates, reconciles, validates, and may repair confirmed findings within authorized scope. **RED FLAG** independently attacks the written owner-frozen candidate and is read-only: no normative edits, repairs, repair commits, or favorable reinterpretation of ambiguity. **GREEN FIX**, when invoked by the owner after Red findings, verifies the exact report/revision, repairs only validated findings, preserves owner policy, records every disposition, validates regressions, creates an exact Git commit locally or, when publication is authorized, through the repository Git-object API, and reports the verified new candidate revision. It does not introduce unrelated policy or ratify. Operational instructions are contained in [section 42](#s42); this rule remains the governing authority for those procedures.

Before RED FLAG, verify branch/HEAD/status, actual normative text, and explicit owner freeze evidence identifying the candidate. Without that evidence, STOP with **RED FLAG REQUIRES OWNER-AUTHORIZED PLAN FREEZE**. Prior completeness recommendations, integration reports, rule counts, historical favorable verdicts, or skill invocation do not authorize freeze/attack. After normative Green Fix, identify the exact repaired revision and verify that the owner freeze/repair authorization covers its review; do not transfer a prior verdict or infer authority for unrelated new policy. Scoped prior delegation may cover repair/review without a fresh prompt under [GOV-3](#gov-3). [GOV-4](#gov-4)'s actual-authority and reviewability requirements, and separate owner ratification authority, remain. The current integration mission supplies freeze/review/repair/publication authority within its stated scope; it does not supply ratification authority.

Red review MUST exercise independent lenses below, using independent reviewers where available or distinct sequential passes with the independence limitation disclosed:

| Lens | Attack scope |
|---|---|
| A — Normative logic | Contradictions/circular definitions, conflicting MUSTs/precedence, terms, absolutes, universality/applicability/exception loopholes. |
| B — Proportionality | Tiny-tool ceremony and lifelong systems evading safety. |
| C — 20–50-year lifecycle | Developer/machine/provider/dependency loss, OS changes, version skew, growth, migration/recovery, exit/reconstruction. |
| D — Data loss/ransomware/sync | Mass deletion/encryption/renames, NAS propagation, backups, stale replicas/conflicts, restore collisions. |
| E — Malware/Raw/ClamAV | False verdicts, stale/unavailable/compromised scanner, parser compromise, quarantine escape, infected Raw sync, platform/license/Rust integration, updates. |
| F — Agent/skill supply chain | Malicious instructions/scripts, injection/exfiltration, mutable remote rules/updates, broad tools, conflicts/context overload, symlinks/path traversal, dependencies/licenses/installers. |
| G — Hermes/AI authority | Content posing as instructions, invented identities/paths, raw writes/traversal, cloud privilege, weak-model guessing, ambiguous matches, approval/version mismatch. |
| H — UI/UX/anti-slop | Blind ratios/new formulas, forced novelty, excessive process, platform/design-system rigidity, inaccessible styling, primitive bans, third-party taste bias, unrendered QA. |
| I — Accessibility | Keyboard traps/focus, color-only meaning, drag-only actions, targets/names, screen readers, scaling/reflow/motion, native/web scope. |
| J — Locale/time | Offset/zone identity, DST/rules, date-only/recurrence, skew/device clocks, parsing/Unicode/RTL, history reinterpretation. |
| K — Platforms/Rust | Windows/macOS/four Linux baselines, mobile/web/native/shared UI, foreign-language dependencies, exception ambiguity, SDKs. |
| L — Local-first/NAS | Absent/added/removed hub, concurrent writers/network storage, backup confusion, raw database shares, outage/stale copies. |
| M — Migration/recovery | Old client/new data, ancient data, interruptions/backup failure, rollback over newer work, corruption/derived rebuild, recovery without startup. |
| N — Build/release/supply chain | Rebuild limits, registries/toolchains/signing loss, updates/unpinned dependencies, vendors, licensing. |
| O — Development governance | Ambiguous phases, APP Plan drift, false Done evidence, emergency abuse, brownfield rewrites, conformance loopholes, hidden context. |
| P — Technical factuality | Hashes/tamper proof, Rust/correctness, scans/immunity, backups/cleanliness, WAL/share safety, keys/exactly-once, schemas/determinism, approval/factual truth. |

Classify every finding **BLOCKER** (unsafe ratification: material data loss/security/fundamental contradiction/unenforceable core/dangerous falsehood), **MATERIAL** (must repair before ratification), **NON-BLOCKING** (recorded improvement), or **NOT AN ISSUE** (rejected hypothesis). Give exact rule/section and wording, scenario, why existing rules do not resolve it, severity/confidence, smallest repair direction, and regression risk. Do not inflate taste into a defect or apply the repair during Red. Trust the frozen text rather than previous author/report claims.

Every normative Green Fix invalidates an earlier Red pass and requires another attack. Recommend ratification only when zero BLOCKER/MATERIAL findings remain, prior findings have explicit dispositions, no old material defect regressed, current structural/factuality/proportionality checks pass, and **two consecutive independent Red rounds after the last normative repair** find no BLOCKER/MATERIAL defect. Disclose unavailable independence; a same-author replay is not independent. A recommendation is not ratification. A mode name alone grants no push, merge, remote-main/tag/release, or ratification authority. Actual owner authorization may already cover publication and promotion, as the current integration mission does; tags/releases and ratification remain separately scoped decisions.

Every Red report MUST disclose that review does not prove absolute correctness, security, completeness, or immunity to future unknown conditions. Only when the review identifies zero BLOCKER and zero MATERIAL findings MUST it state: **No material defect was identified under the defined review battery. This does not prove absolute correctness, security, completeness, or immunity to future unknown conditions.** A report identifying any BLOCKER or MATERIAL finding MUST NOT assert the clean-result sentence as its outcome; it MUST truthfully report the material findings and state that other defects may still exist and the attack does not prove all defects were discovered.

<a id="s29"></a>
## 29. Anti-pattern index — non-normative

This navigation index adds no requirements. Applicability, strength, and exceptions remain those of the governing clauses.

| Warning sign | Governing clause |
|---|---|
| Accepted/uncertain operation reported as known final completion | [OUT-1](#out-1) |
| UI controls or prompts treated as effective permission enforcement | [AUTH-1](#auth-1), [AI-2](#ai-2) |
| Untrusted content grants AI new authority | [AI-1](#ai-1) |
| Read-only label or record count used as complete risk model | [AI-3](#ai-3) |
| Expendable cache holds the only copy promised preservation | [DATA-1](#data-1) |
| Generated artifact assumed disposable or exactly reproducible | [DATA-2](#data-2) |
| Application replacement accidentally deletes retained data | [LIFE-1](#life-1) |
| One write algorithm prescribed without backend failure semantics | [STORE-1](#store-1) |
| WAL, hashes, or unfenced leases treated as sufficient NAS safety | [NAS-2](#nas-2), [CON-1](#con-1) |
| Docker or backup-only support presented as all NAS modes | [NAS-1](#nas-1) |
| Required evidence written independently after mutation commit | [AUDIT-2](#audit-2) |
| Attacker-rewritable manifest presented as protected anchor | [AUDIT-3](#audit-3) |
| Permanent sensitive retention justified only by auditability | [PRIV-1](#priv-1) |
| Migration failure blindly restores over newer work | [MIGRATE-1](#migrate-1) |
| Unknown persistent semantics accepted then destroyed | [MIGRATE-2](#migrate-2) |
| Recovery claimed without restoration evidence | [BACKUP-2](#backup-2) |
| Loopback or VPN treated as complete authorization | [SEC-1](#sec-1) |
| Invariants bypassed or distribution introduced without rationale | [ARCH-1](#arch-1), [ARCH-2](#arch-2) |
| Unjustified non-Rust implementation | [LANG-1](#lang-1) |
| Unsupported or untested targets presented as verified | [TEST-1](#test-1), [PORT-1](#port-1) |

<a id="s30"></a>
## 30. Candidate status and review continuation — non-normative

**1.0.0-rc4 — Single-file data-workspace integration candidate — NOT RATIFIED.** This artifact is prepared for owner-authorized freeze and fresh adversarial review under [section 42](#s42). An external revision receipt identifies the exact committed frozen candidate and its checksum; this document does not invent its own future commit ID. Current review results belong in revision-bound evidence outside the active one-file tree, never silently appended to frozen normative bytes.

The October 14, 2026 clean reviews and convergence audit apply only to `a9c597c8f14536a4404a64494cf56e9015e1288a` and SHA-256 `1c6471ab3ec5291b9cd4ec884912ccec10431d2e35e9e514ad29574b778b082d`. They provide **no convergence credit for rc4**. Their reviewer independence and model-identity limits remain visible in [section 43](#s43). The current candidate requires fresh review of its actual frozen bytes; consult the corresponding external receipt/reports for subsequently completed rounds rather than inferring success from this status page.

All 137 rc3 stable rule IDs and metadata dimensions remain, including the original 113 and the 24 rc3 additions. RC4 adds 14 rules; the resulting inventory is 151. The historical rc3 reviews do not certify these new bytes. The preservation/refinement map in [section 43](#s43) explains the historical rc3 amendments and 137-rule inventory; [section 51](#s51) records RC4 changes. The 33 original Skill families remain a policy catalog, not installed packages. The Hermes/User-Adaptable Information Architecture Blueprint remains integrated candidate policy under [section 32](#s32), separate from the future development repository blueprint under [section 39](#s39).

The current owner mission authorizes integration, review/validated repair, commit/push, and safe normal main promotion of an **unratified** candidate. It does not authorize rewriting history, deleting historical branches, installing the named Skills, or ratifying. No governed application implementation or platform/runtime behavior is certified by this text.

Continuation: verify exact candidate identity and authority, complete fresh independent Red rounds, repair only substantiated issues within scope, restart convergence after normative repairs, preserve all dispositions, validate the published bytes/tree, and present the exact candidate for the owner's separate ratification decision. Publication and default-branch placement do not imply ratification.

<a id="s31"></a>
## 31. Application planning, continuity, and conformance

These are intentional owner development-governance policies, not claims that a particular directory structure is a universal engineering invariant. They inherit CANDIDATE status. Their application to another repository requires the applicable adoption and task authority; this integration does not authorize inspecting or changing other apps.

<a id="dev-1"></a>
### 31.1. DEV-1 — App-specific design and long-lived purpose

**Type:** ECOSYSTEM POLICY | **Origin:** USER POLICY | **Applies:** application design and development lifecycle

The development process MUST pursue maintainability, understandability, recoverability, portability, evolvability, AI continuity, user control, structural coherence, and useful longevity. The constitution governs how designs are discovered, challenged, documented, built, verified, and maintained. It MUST NOT be interpreted as requiring identical application features or identical user-data structures. The design MUST reflect the idea, users, domain, risk, data, target platforms, and intended lifecycle. These goals improve the probability of long-term success; they do not guarantee indefinite usability.

<a id="dev-2"></a>
### 31.2. DEV-2 — Refine the idea before implementation

**Type:** ECOSYSTEM POLICY | **Origin:** USER POLICY | **Applies:** new applications before implementation begins

Implementation MUST NOT begin merely because an initial idea exists. Before implementation code is changed, the idea MUST be interrogated and refined into a coherent product definition addressing the problem, users, long-term role, owned/preserved information, offline capabilities, multi-device needs, NAS behavior, desktop/mobile/web scope, Hermes/AI role, privacy/security expectations, user configuration, expected lifetime, migration/portability needs, and major failure scenarios where applicable. Record non-applicability rather than inventing unnecessary features. Brainstorming MUST NOT silently become implementation. Planning then proceeds through research, specification, and the [Plan Freeze Gate](#dev-5).

Substantial product refinement MUST include actual value/differentiation under [DEV-18](#dev-18) before architecture freeze; private/internal fit does not require a commercial moat.

The mandatory ordered workflow, including initial owner review before dedicated source discovery and final technology selection, is specified in [PLAN-1](#plan-1).

<a id="dev-3"></a>
### 31.3. DEV-3 — Research before architecture freeze

**Type:** ECOSYSTEM POLICY | **Origin:** USER POLICY | **Applies:** new or substantially revised application architecture

After the idea is sufficiently defined and before architecture is frozen, planning MUST research relevant existing solutions: GitHub repositories, mature open-source applications, standards, libraries/frameworks, technical papers or documentation where useful, known architectural failures, and competing approaches. Scope research to the actual problem and authorized sources. Ask whether an existing solution solves a relevant problem better than the proposed design; copying another project is not the goal.

If no better solution is found, refine and retain the design. If a superior pattern is found, understand its advantage, determine applicable parts, and deliberately update the plan. Important comparisons and resulting decisions MUST be preserved under [DEV-8](#dev-8); lack of evidence MUST NOT be reported as completed research.

Before rebuilding a difficult subsystem from scratch, research whether mature existing software solves the relevant problem substantially better. Deliberately evaluate use as a dependency, wrapping, adaptation, vendoring, forking, or rejection, considering architecture fit, security, maintenance, licensing, portability, long-term control, and integration cost. Existence alone does not require adoption. Significant source foundations need provenance under [SEC-4](#sec-4); Rust-first artifact/exception scope remains governed by [LANG-1](#lang-1).

[PLAN-1](#plan-1) orders initial review, mandatory existing-project discovery, and final design/technology selection. Pinned ZIP reuse and actual source assessment follow [PLAN-2](#plan-2).

<a id="dev-4"></a>
### 31.4. DEV-4 — Strongest reasonably available planning capability

**Type:** ECOSYSTEM POLICY | **Origin:** USER POLICY | **Applies:** creation or substantial redesign of an application Master Plan

Planning MUST use the highest-capability model reasonably available for research synthesis, architectural resolution, edge cases, interfaces, storage and synchronization semantics, platform strategy, AI/Hermes design, risks, phases, and acceptance criteria. Record the planning capability selected and material availability constraints proportionately. This requires neither a named provider nor permanent cloud access; relevant data-access and privacy constraints remain in force.

Reasoning, decisions, contracts, and requirements needed for implementation MUST be captured in durable project artifacts. The implementation process MUST NOT depend on continued access to the strongest model or on its hidden conversation history. Model selection does not itself establish correctness or authority.

<a id="dev-5"></a>
### 31.5. DEV-5 — Candidate-plan review and Plan Freeze Gate

**Type:** ECOSYSTEM POLICY | **Origin:** USER POLICY | **Applies:** application plans before implementation and material architectural replanning

Once the full application plan appears complete, freeze an identifiable candidate plan for hostile review before implementing it. Review MUST use the strongest reasonably available AI capability and relevant human/domain expertise and targeted technical research as appropriate to the plan and risk. Attack correctness, architecture, maintainability, longevity, data loss, storage/NAS failures, partitions, sync conflicts, migrations, offline behavior, platform differences, AI failures, security, privacy, performance, recovery, technology/dependency changes, small-model usability, developer replacement, and incomplete requirements where applicable.

Use **Attack → Fix → Attack → Fix**, preserving findings and dispositions, until no known material issue remains unresolved. The **Plan Freeze Gate** is: implementation may begin only when all known material architectural questions, contradictions, blocking risks, and unresolved design decisions have been resolved or explicitly accepted and documented by the applicable authority. Record the gated plan revision, evidence, accepted constraints, and any approved exceptions. Acceptance MUST NOT disguise a missing decision as an implementation task or waive a constitutional obligation without [GOV-3](#gov-3) authority. The gate is an evidence-based decision, not mathematical “100% perfection.”

Authorized, bounded research experiments MAY precede Plan Freeze when needed to resolve a material planning question, including architecture, API/platform compatibility, performance, storage, migration, or crash/recovery behavior. For this gate and [DEV-2](#dev-2), these are evidence-gathering activities, not adopted product implementation. Each experiment MUST define its research question or hypothesis, bound its scope to the evidence needed, and record results and relevant limitations through [DEV-6](#dev-6) and [DEV-8](#dev-8). Experimental code/data MUST be clearly identified as experimental/disposable or otherwise non-authoritative unless deliberately adopted later; the label does not authorize destruction of retained source data or required evidence. Small research scripts need no full production phase merely to gather evidence, but actual authorization, security/privacy controls, safe execution, and truthful evidence remain required.

Incorporation of experimental code or behavior into the product MUST pass the normal Plan Freeze, phase, conformance, security, testing, and evidence requirements. “Prototype” or “research” MUST NOT become a loophole for implementing substantial production scope before planning. Exploratory work MUST NOT silently become canonical architecture merely because it exists. Unresolved questions remain planning questions; this research route does not waive [DEV-11](#dev-11)'s stop-rather-than-guess rule or [DEV-13](#dev-13)'s completion gate.

Material new architectural uncertainty during implementation returns the affected work to planning and this gate; do not silently improvise a different architecture. This application-plan review requirement does not itself authorize a constitutional attack; constitutional review follows the actual owner authorization and identified freeze under [GOV-4](#gov-4), [GOV-5](#gov-5), and [section 42](#s42).

Necessary emergency maintenance may temporarily precede complete planning only under [DEV-17](#dev-17), with bounded authority, evidence, and reconciliation before ordinary feature work resumes. This does not waive the gate for normal implementation.

<a id="dev-6"></a>
### 31.6. DEV-6 — Discoverable planning and implementation responsibilities

**Type:** ECOSYSTEM POLICY | **Origin:** USER POLICY | **Applies:** substantial application repositories, with proportionate representations for smaller applications

Substantial applications SHOULD conceptually separate `Application/Master Plan/` from `Application/Codebase/`, using the complete detailed default in [BLUEPRINT-1](#blueprint-1). The implementation belongs to Codebase; Master Plan holds durable specification, intelligence, state, decisions, and the roadmap. These logical responsibilities MUST remain clear and discoverable. Physical names/layout MAY be adapted when sound engineering or framework compatibility requires it, with an explicit navigation mapping; smaller projects may combine concise records without dropping applicable lifecycle gates. Historical references to “APP Plan” denote this planning responsibility, not a second required folder.

The APP Plan blueprint MUST support these discoverable responsibilities, directly or by clear references:

| Area | Responsibility |
|---|---|
| Master Plan | Current authoritative intended product specification under [DEV-7](#dev-7). |
| Project State | Concise current execution status and authoritative next action under [DEV-9](#dev-9). |
| Research | Important comparative evidence, including adopted/rejected alternatives. |
| Evidence | Supporting benchmark/prototype results, compatibility tests, GitHub comparisons, architecture experiments, migration rehearsals, and citations, directly or by stable references without needless large-artifact duplication. |
| Decisions | Individually discoverable architectural choices and rationale. |
| Phases | Active and planned executable implementation specifications. |
| Done Phases | Completed specifications, actual outcomes, and evidence. |
| Reviews | Candidate-plan attacks, conformance verification, findings, and dispositions. |
| Existing App Assessment | Inherited implementation assessment when adopting the rules for a brownfield app. |
| UI design, where relevant | Product value/flows/information hierarchy, brief, identity/references/design system, platform/accessibility, states, adaptation, anti-slop and rendered QA under [UI-4](#ui-4)–[UI-7](#ui-7). |
| Agent Skill metadata, where relevant | Universal/project workflows, trusted revisions/provenance, modifications/permissions and reliable references under [SKILL-1](#skill-1)–[SKILL-3](#skill-3). |

This is a development-artifact blueprint, distinct from the runtime user-data/workspace contract in [section 32](#s32). Organized APP Plan records do not establish that product data is discoverable, and a navigable runtime hierarchy does not replace a proper APP Plan. Evidence, Research, and completed execution records may share storage/references while retaining their distinct responsibilities. Equivalent domain-appropriate representations are allowed; names do not establish compliance.

<a id="dev-7"></a>
### 31.7. DEV-7 — Authoritative current Master Plan

**Type:** ECOSYSTEM POLICY | **Origin:** USER POLICY | **Applies:** application planning and changes to intended architecture or behavior

The App Master Plan MUST contain the complete current authoritative specification of the intended completed product under [BLUEPRINT-2](#blueprint-2); precise references MAY supply supporting technical detail and evidence but MUST NOT leave material product decisions scattered among competing specifications. It MUST cover applicable product purpose, users, features, architecture, shared Rust core, platform scope, UI strategy, storage architecture, canonical data model, synchronization, NAS and local-only behavior, AI/Hermes, security, privacy, backup/recovery, migrations, testing, deployment, packaging, interfaces, extension points, constraints, and accepted exceptions.

Keep historical brainstorming and superseded rationale in Research, Decisions, Reviews, or provenance; do not make a reader infer current intent from chronology. Changes to intended behavior MUST update the plan deliberately with relevant decision and phase links. The Master Plan specifies intended product truth; it does not claim unbuilt features exist or supersede the constitution without an approved exception.

Every App Plan MUST state the timezone policy under [DATA-5](#data-5). It MUST also specify, where applicable, release reconstruction and dependency-disappearance dispositions ([SEC-5](#sec-5)), recovery without normal startup ([RECOVER-1](#recover-1)), lifetime growth/validation assumptions ([DEV-16](#dev-16)), emergency repair/reconciliation ([DEV-17](#dev-17)), accessibility acceptance criteria ([UI-3](#ui-3)), and locale parsing/identity semantics ([DATA-4](#data-4)). Make procedures, limits, and criteria discoverable without inferring them from code; no separate empty documents are required.

For substantial retained-data applications, security planning MUST address relevant hostile inputs and exposed processors, their access and compromise consequences, destructive sync propagation, NAS-history protection, actual backup copies/deletion authority, restore validation, update integrity, suspected-compromise containment, and evidence for known-good recovery points. Reference the contracts in [SEC-1](#sec-1), [SEC-3](#sec-3), [IO-1](#io-1), [SYNC-1](#sync-1), [NAS-1](#nas-1), [BACKUP-1](#backup-1), [BACKUP-2](#backup-2), and [RECOVER-1](#recover-1) rather than duplicating a parallel security plan. Scope effort to retained-data value, attack surface, and architecture.

Applicable file-intake plans MUST make the [IO-2](#io-2), [IO-3](#io-3), and [SEC-6](#sec-6) contracts discoverable: logical boundary, required promotion gates, scanner selection/transport/authority, verdict reuse and rescan policy, signature maintenance, quarantine controls, status reporting, cross-device trust, lifetime performance, source provenance, and distribution-license verification. Concise references may satisfy this without a separate scanner governance system.

For relevant user-facing work, the plan MUST include or reference the design responsibilities under [UI-4](#ui-4)–[UI-7](#ui-7) and product value under [DEV-18](#dev-18). Development metadata SHOULD identify applicable skill families, trusted versions, local changes/provenance and permissions under [section 33](#s33), without duplicating unchanged central guidance.

<a id="dev-8"></a>
### 31.8. DEV-8 — Comparative research and explicit decisions

**Type:** ECOSYSTEM POLICY | **Origin:** USER POLICY | **Applies:** significant researched alternatives and architectural decisions

Research records MUST identify what was examined, why it was relevant, strengths, weaknesses, what was adopted or rejected, and why. Preserve important source/version references and comparative evidence sufficiently for future humans or AI to understand the decision without repeating major research. Such records do not require copying entire third-party repositories or restricted source material.

Research claims MUST distinguish verified evidence, inference/conditional evidence, and unresolved unknowns under [EVID-1](#evid-1). Supporting evidence belongs in or is referenced through the Evidence responsibility under [DEV-6](#dev-6). Repetition MUST NOT turn an assumption into a frozen architectural fact. Material unverified assumptions and conflicts MUST be resolved or explicitly accepted with their status intact at the [Plan Freeze Gate](#dev-5).

Important architectural decisions MUST be explicit and individually discoverable, including applicable Rust-core, storage-engine, sync-model, NAS-topology, UI, identity, AI/Hermes-boundary, and backup choices. A weaker model must not need to infer them from hundreds of pages of historical text. Decision records MUST identify current versus superseded decisions and link to the Master Plan where needed.

<a id="dev-9"></a>
### 31.9. DEV-9 — Project State as the current execution entry point

**Type:** ECOSYSTEM POLICY | **Origin:** USER POLICY | **Applies:** every active application

Each active application MUST maintain a concise machine-readable and human-readable Project State record, discoverable from the repository entry point. One record or consistently generated views MAY satisfy both forms; no exact format is mandated. Its sole governing responsibility is current execution status and navigation, not duplication of the full Master Plan or completed history.

Without prior conversation, it MUST reveal the current phase, last completed phase, completed capabilities, work in progress, work not started, known blockers, current branch/revision where applicable, next authoritative action, and the active phase specification's location. Identify the revision actually observed rather than inventing a self-referential commit identifier. Update status when work, blockers, phase completion, or next action changes; distinguish verified completion from claims awaiting verification. State/implementation contradictions MUST be reconciled before relying on that state to proceed.

Current and last verified completed subphases, unresolved errors, actual implementation status, exact next authorized action, and bare “Continue” behavior additionally follow [EXEC-4](#exec-4). A structured Markdown record with a documented stable field schema may satisfy both machine-readable and human-readable requirements; a prose-only status narrative without reliably identifiable fields does not satisfy the machine-readable duty.

<a id="dev-10"></a>
### 31.10. DEV-10 — Phases as executable implementation specifications

**Type:** ECOSYSTEM POLICY | **Origin:** USER POLICY | **Applies:** planned implementation and conformance phases

Each phase MUST be sufficiently specified for bounded execution rather than a loose task list. Define as appropriate its objective, rationale, prerequisites, current and expected end states, files/components, interfaces/contracts, data structures, dependencies, tasks and ordering, invariants, files/systems that must not change, error behavior, edge cases, migration impact, security/privacy, tests, validation commands, expected results, completion evidence, stopping conditions, follow-up state, and next phase.

If major architecture must still be invented during execution, the phase is insufficiently specified and affected implementation MUST stop for planning resolution. A phase MUST distinguish delegated implementation choices from unresolved architectural decisions. Acceptance criteria and validation MUST describe outcomes that can actually be checked under [TEST-1](#test-1), not merely the presence of code.

Substantial phases MUST be decomposed into individually numbered, bounded subphases under [EXEC-1](#exec-1), each carrying the concrete 33-field execution contract under [EXEC-2](#exec-2). The parent phase remains the governing specification and conformance boundary. Tiny phases may contain one numbered executable subphase in the same file without artificial folders; proportionate representations do not waive required fields, acceptance evidence, numerical order, or stop conditions.

The temporary emergency path in [DEV-17](#dev-17) may defer only necessary normal planning steps; its durable emergency record and subsequent repair contract do not grant permission to invent unknown architecture.

Phase specifications MAY name relevant process skills for bounded loading, but MUST retain their actual project-specific specification under [SKILL-2](#skill-2). Substantial UI phase acceptance MUST include applicable rendered review under [UI-7](#ui-7); “use frontend-design skill” alone is not a phase contract.

<a id="dev-11"></a>
### 31.11. DEV-11 — Full-build small-model continuity and safe resumption

**Type:** ECOSYSTEM POLICY | **Origin:** USER POLICY | **Applies:** application plans, phase execution, and AI-assisted continuation

Plans and repositories MUST be designed so that a sufficiently capable small local model can build the entire application phase by phase using APP Plan and Codebase, without hidden conversation history or continuous rescue by a stronger model. Shift complexity into specifications, contracts, examples, indexes, tests, acceptance criteria, deterministic tooling, and explicit Project State. Strong planning captures architectural reasoning ahead of time; weaker execution remains bounded. This is a full-build design target, not merely the ability to continue one task and not a claim that any model or parameter count can complete every application.

Every phase MUST support zero-conversation resumption: locate Project State; establish completion and active phase; read the specification; locate implementation; understand the required outcome; make authorized safe changes; run validation; record results; determine completion; and proceed only where permitted by the phase gate. Local execution is the baseline design target; a suitable cloud model may follow the same artifacts, but provider/location alone does not establish capability and continued cloud access is not required.

**A weaker model is allowed to do less, but not to invent more.** If required information is missing, contradictory, or cannot be safely established, the executor MUST stop affected work and record the precise blocker and needed resolution. It MUST NOT invent architecture, silently reinterpret the Master Plan, claim unperformed validation, expand authority, or bypass [AI-1](#ai-1), [AI-3](#ai-3), or [AUTH-1](#auth-1). Full-build continuity does not grant unrestricted autonomous execution; it supplies the information needed to execute authorized work safely.

This **product-development** goal concerns building/continuing software from APP Plan, phases, Project State, tests, and Codebase. The separate **product-use** goal under [HERMES-2](#hermes-2) concerns navigating and using supported application tools through structured, bounded retrieval. Both apply where relevant; satisfying either one does not prove the other.

The owner’s measurable development-execution target includes approximately 4B-class models under [EXEC-6](#exec-6). This is distinct from the approximately 1B product-use retrieval target in HERMES-2, and neither parameter count guarantees success.

<a id="dev-12"></a>
### 31.12. DEV-12 — Evidence-bearing Done Phases

**Type:** ECOSYSTEM POLICY | **Origin:** USER POLICY | **Applies:** phases that have passed the completion gate

A completed phase MUST be moved or recorded in discoverable Done Phases history, preserving the original specification or its immutable reference, actual implementation, deviations, relevant decisions, tests executed, outcomes, completion evidence, relevant commit/revision references, and remaining follow-ups. Update Project State with the result and next permitted action. A failed or unverified phase MUST NOT be represented as done.

Done Phases complements Git and other version history with understandable evidence; it neither replaces version control nor requires reconstructing completed work solely from commits. References may avoid duplicating large artifacts, provided the promised evidence remains accessible under its retention contract. Follow-ups MUST NOT conceal unresolved required acceptance criteria; approved exceptions are explicit.

For substantial tasks/phases, preserve execution evidence during work as well as at completion: what was attempted, what actually changed, validation performed, passed/failed outcomes, remaining uncertainty, and the containing revision/commit where relevant. Interrupted or failed work needs an accurate continuation record rather than a false Done entry. Project State points to this evidence; completion incorporates or references it in Done Phases without unnecessary duplication or a mandatory `Operations/` directory.

Evidence MAY include tests, builds, static checks, runtime validation, relevant screenshots, schemas, hashes, migration comparisons, commit IDs, and operation receipts as appropriate. Evidence supports the actual claim and the [Three-Layer Conformance Gate](#dev-13); its mere existence or a screenshot cannot establish unrelated guarantees.

Subphase evidence, verified ✅ heading markers, and parent phase completion additionally follow [EXEC-5](#exec-5); no marker precedes actual acceptance verification.

<a id="dev-13"></a>
### 31.13. DEV-13 — Three-Layer Conformance Gate after every phase

**Type:** ECOSYSTEM POLICY | **Origin:** USER POLICY | **Applies:** completion of every implementation or conformance phase

Code being written is not completion. Before a phase is marked complete or the next implementation phase proceeds, all applicable layers MUST pass:

1. **Universal Rules:** conformance to the applicable constitutional revision and approved exceptions.
2. **App Master Plan:** conformance to the application's current specified architecture and behavior.
3. **Phase Contract:** satisfaction of that phase's acceptance criteria and required evidence.

Verification MAY be performed by AI, humans, automated validation, or a combination. The verifier MUST compare the actual implementation/artifacts with specifications rather than merely trusting the implementing agent's completion claim. Use deterministic evidence where practical: tests, builds, schemas, static analysis, fixtures, integration validation, and artifact inspection. Record applicable criteria, outcomes, evidence, and exceptions; skipped or unrun required checks are not passes. Separate verifier identity is not universally required, but evidence-based comparison is.

The continuing cycle is **Implement → Verify → Universal Rules → Master Plan → Phase Contract → Pass: continue / Fail: repair**. Do not accumulate known architectural debt for later without an explicit approved exception under [GOV-3](#gov-3). Phase checks cover implemented scope and effects, including regressions in previously conformant work; a planned future capability is not automatically a present violation. Required-but-missing behavior for the current scope remains a failure. Repair phases may address documented failures; ordinary feature progression cannot bypass them.

Emergency containment/repair follows [DEV-17](#dev-17)'s temporary procedure and post-emergency reconciliation gate; it does not count as verified phase completion merely because it was urgent.

<a id="dev-14"></a>
### 31.14. DEV-14 — Brownfield assessment and conformance before features

**Type:** ECOSYSTEM POLICY | **Origin:** USER POLICY | **Applies:** existing or partially built applications when these rules are applied with appropriate authority

Normal feature development MUST pause before extending inherited implementation. First inspect the authorized application, create/update its Master Plan, compare implementation with the applicable Universal Rules, Master Plan, and intended architecture, classify existing work, create Conformance Phases, repair, verify conformance, and only then resume ordinary planned development. Applying this workflow requires actual authority for that repository; this constitutional rule alone grants none.

An Existing App Assessment or equivalent MUST classify inherited implementation as applicable: already compliant, correct and reusable, usable with modification, obsolete, unsafe, architecturally inconsistent, or missing. **Preserve compliant work, repair non-compliant work, replace only where necessary.** Age or predating the current plan does not justify rewriting working compliant code. Record evidence, gaps, retained work, required repairs, and any approved exceptions.

Conformance Phases MUST precede new feature phases and use [DEV-10](#dev-10) and [DEV-13](#dev-13). They bring the inherited implemented scope into alignment with the constitution and current Master Plan; they do not require all future roadmap features to exist before development can resume. A failed gate permits scoped repair, not ordinary feature expansion. Following aggregate conformance verification, every subsequent phase remains subject to the same three-layer gate. Applicable safety/containment actions under [SAFE-2](#safe-2) remain possible; they are not a feature-development bypass.

<a id="dev-15"></a>
### 31.15. DEV-15 — Repository memory and the longevity test

**Type:** ECOSYSTEM POLICY | **Origin:** USER POLICY | **Applies:** application planning, documentation, and long-term continuation

Planning MUST ask: **Could another human or AI understand, maintain, repair, migrate, and continue this application years later using only the repository and documented external dependencies?** If not, planning/documentation is insufficient and the identified gaps MUST be addressed before claiming the relevant plan or phase ready.

The repository MUST carry durable development memory sufficient to establish what the app is, why major decisions were made, what is implemented, what remains, what was rejected, known risks, how to validate, and how to continue. Conversation history may assist planning but MUST NOT be required for continuation. Avoid unnecessary dependence on one developer's memory, one AI conversation, one model provider, one computer, undocumented file locations/decisions, or unsupported proprietary assumptions. Document necessary external dependencies and recovery/access requirements without committing secrets or retaining unnecessary sensitive conversation payloads; [PRIV-1](#priv-1) and [SEC-2](#sec-2) still apply.

<a id="dev-16"></a>
### 31.16. DEV-16 — Lifetime growth envelope and maintenance validation

**Type:** ECOSYSTEM POLICY | **Origin:** USER POLICY | **Applies:** planning and verification where retained data, history, media, logs, indexes, or relationships may materially grow

The App Plan MUST define a reasonable expected lifetime growth envelope and its validation assumptions where scale affects architecture. Relevant dimensions may include records/files, storage/media volume, relationships, history/audit growth, devices, archive age, and users/accounts/tenants. State assumptions and limits so future humans or AI need not infer the intended workload. This is a planning envelope, not an indefinite capacity guarantee or universal numerical threshold.

Validation under [TEST-1](#test-1) MUST consider applicable ordinary and lifecycle operations at expected scale: startup, query/search, index rebuilding, backup, restore, migration, sync, recovery, export, integrity scans, and compaction/retention. The App Plan defines suitable resource/time budgets and supporting evidence, including limitations of estimates or representative samples. Tiny or inherently bounded applications may state that bound and its rationale without special scaling architecture or meaningless benchmarks.

<a id="dev-17"></a>
### 31.17. DEV-17 — Emergency maintenance and reconciliation

**Type:** ECOSYSTEM POLICY | **Origin:** USER POLICY | **Applies:** urgent maintenance where delay materially increases security, data-loss, privacy, safety, or unrecoverable operational risk

Emergency maintenance MAY precede complete normal planning when necessary under [SAFE-2](#safe-2). Bound work to the minimum necessary containment, mitigation, repair, urgency-appropriate validation, and preservation of change evidence. Defer only planning or routine approval steps that cannot practicably precede containment, using actual applicable emergency authority or prior delegation under [AUTH-2](#auth-2) and [GOV-3](#gov-3). Emergency status does not manufacture permission, waive integrity/privacy boundaries, or authorize ordinary feature development. Routine bugfixes do not automatically invoke this procedure.

Maintain a proportionate durable record of trigger, scope, authorization, affected components, actual change, validation, residual risks, and temporarily deferred requirements. Link it from Project State under [DEV-9](#dev-9) so an interrupted session can resume safely. A small urgent patch needs concise evidence, not a parallel paperwork system. [DEV-11](#dev-11) still prohibits guessing missing facts or inventing architecture; choose only safely established, authorized actions and record blockers for the rest.

Before ordinary feature development resumes after a material emergency change, reconcile the applicable Master Plan, Project State, Decisions, phase/execution history, tests, architecture, compatibility expectations, migration implications, and documentation. Establish or update the repair's phase contract and run the applicable [Three-Layer Conformance Gate](#dev-13); deferred required checks are not passes. Outstanding failures require repair or an actually approved scoped exception under [GOV-3](#gov-3), not silent permanent drift. Emergency repair may temporarily precede complete planning; it MUST NOT permanently bypass project truth or mark an unverified phase complete.

<a id="dev-18"></a>
### 31.18. DEV-18 — Product value and differentiation before architecture freeze

**Type:** ECOSYSTEM POLICY | **Origin:** USER POLICY | **Applies:** idea refinement and planning of substantial applications

Before architecture freeze, the product MUST answer: **If someone else can create software performing the same general function, why should someone use this application?** Record actual value such as workflow/usability, privacy/local operation/user ownership, reliability/portability/accessibility, performance/interoperability, specialist fit, low friction, execution quality, longevity/recovery/trust, or precise fit to an individual owner's needs. No fake commercial moat, novelty for its own sake, or market claim is required for private/internal products.

The answer MUST influence relevant workflows, feature priorities, UX/UI, architecture, privacy, platform support, integrations, performance and offline/local behavior; an interchangeable implementation with only a slogan is insufficient. Record what should not be built alongside purpose and alternatives under [DEV-2](#dev-2), [DEV-3](#dev-3), and [DEV-7](#dev-7). Verify the connection in applicable phase/UI review under [DEV-13](#dev-13) and [UI-7](#ui-7).

<a id="s32"></a>
## 32. Universal Information Architecture Blueprint

This candidate blueprint standardizes discoverability and integrity contracts across applicable products, not domain features or one universal folder tree. The owner-supplied four-app analysis provides design provenance, not external normative dependencies. These rules complement existing data, storage, recovery, privacy, synchronization, and AI authority contracts.

<a id="info-1"></a>
### 32.1. INFO-1 — Logical information architecture independent of storage layout

**Type:** ECOSYSTEM POLICY | **Origin:** USER POLICY | **Applies:** applications managing durable user information

The logical information model MUST support deterministic discovery/resolution, identity, provenance where meaningful, relationships, documented access, recovery, continuation, rebuildability where claimed, and portability where required. Human-facing hierarchy MUST remain application/domain-appropriate and MAY be user-configurable. **Standardize the discoverability and integrity contract, not every user's folder names.**

Files, SQLite, PostgreSQL, embedded object stores and services remain available for justified operational responsibilities. For retained user-owned information, an independently accessible durable workspace under [WORKSPACE-1](#workspace-1) remains mandatory. Every qualifying application MUST maintain complete **Current JSON** recovery representations for each retained original file (or a justified equivalent durable logical object), plus a verified **Folder JSON** manifest for each relevant folder under [JSON-1](#json-1) and [section 53](#s53). Neither can be disabled. A complete standalone global `master-data.json` remains user-optional. Operational stores, catalogs, APIs, hashes and manifest pointers cannot replace actual recoverable payloads in mandatory Current JSONs or enabled global Master JSON. The preferred entry filenames and mapped physical adaptations follow [WORKSPACE-4](#workspace-4); no single domain folder tree or operational database is mandated. “Deterministic” here concerns lookup and explicit contracts, not proof that facts, AI outputs, or all application behavior are deterministic.

Where practical, retained information SHOULD support both human comprehension through meaningful names, metadata, documentation, relationships, readers or exports, and machine reliability through structured IDs, schemas, manifests, catalogs, or typed records. Do not sacrifice deterministic interfaces for attractive folders or long-term comprehensibility merely for AI indexing convenience. Documented binary stores are compatible with these outcomes under [LIFE-2](#life-2) and [STORE-1](#store-1).

<a id="info-2"></a>
### 32.2. INFO-2 — Discoverable workspace entry contract

**Type:** ECOSYSTEM POLICY | **Origin:** USER POLICY | **Applies:** substantial durable workspaces, including equivalent database/service-managed datasets

A workspace MUST expose a predictable logical entry point through which authorized deterministic software and suitably constrained AI can discover applicable workspace identity, schema/format version, major domains/collections, registered data roots, important catalogs/indexes, supported operations, migration/version state, relevant policy/configuration, and lineage where required.

A root manifest, workspace catalog, typed API, database schema plus discovery endpoint, or equivalent deterministic mechanism may implement this capability. The preferred physical entry pattern and technically necessary mapped adaptations for retained-data workspaces follow [WORKSPACE-4](#workspace-4). No public disclosure of private metadata/secrets is required. Discovery is subject to authorization; version handling follows [MIGRATE-2](#migrate-2). Supported offline discovery and synchronization follow the existing local-first and sync contracts.

<a id="info-3"></a>
### 32.3. INFO-3 — Durable identity, organization, and relationships

**Type:** ECOSYSTEM POLICY | **Origin:** USER POLICY | **Applies:** important durable logical objects whose identity must survive organization changes

Such objects MUST have durable product-owned logical identity or an equivalent documented identity contract independent of mutable filenames, display names, paths, categories, statuses, or UI locations. The product SHOULD resolve **stable identity → current location** where location applies. Ordinary renaming or movement between folders, collections, statuses, categories, and views MUST NOT unnecessarily create a new identity or destroy relationships, provenance, or retained history. Explicit copy/new-object and migration operations may have distinct documented identity semantics.

When an object participates in multiple views or relationships, prefer explicit references/relationships over uncontrolled canonical duplication. Canonical information SHOULD NOT be duplicated merely to appear in multiple organizational views when references preserve the same meaning safely. Deliberate replicas, snapshots, backups, and derivatives remain valid with declared authority and lifecycle. Mandatory literal per-file Current JSON duplication under [JSON-1](#json-1) serves recovery, not organizational views; optional full global JSON adds another complete representation only when enabled. The Folder JSON is a verified manifest and MUST NOT replicate every file's payload. Anti-duplication preferences MUST NOT diminish the mandatory Current JSON or an enabled complete Master JSON. Where byte identity or deduplication matters, content hashes or equivalents may assist integrity, provenance, and tracking; content-addressing is not universally required, and byte equality is not automatically logical identity or authenticated origin.

<a id="info-4"></a>
### 32.4. INFO-4 — Precise sub-object addressing and source context

**Type:** ECOSYSTEM POLICY | **Origin:** USER POLICY | **Applies:** large or heterogeneous content where sub-object addressing materially improves retrieval, citation, annotation, or verification

Applications MUST support appropriate deterministic stable/bounded addressing where technically meaningful so a consumer can resolve **object → precise relevant region** without loading or reasoning over an entire huge object. Pages, sections, paragraphs, records, spreadsheet ranges, timestamps, transcript segments, media frames, image regions, and code symbols are examples, not required features or one universal anchor format.

Anchors to mutable content MUST retain enough source context to determine validity, such as source version/hash, surrounding-text hash, record revision, time/version relationship, or an equivalent mechanism. An old annotation/extraction MUST NOT silently attach to unrelated changed content. Stale, ambiguous, or unresolvable anchors require explicit status, revalidation, or a justified remapping operation. Source and derivative lineage follows [DATA-3](#data-3), while uncertainty follows [EVID-1](#evid-1).

<a id="s33"></a>
## 33. Reusable Universal Agent Skills governance

These owner policies define a reusable workflow library and its trust/authority contracts. This constitutional catalog is not a claim that operational skill packages have already been authored, installed, reviewed, or tested. An Agent Skill means inspectable workflow guidance and any supporting resources/scripts; calling it a prompt does not remove supply-chain or execution risk.

<a id="skill-1"></a>
### 33.1. SKILL-1 — Modular, discoverable, portable process expertise

**Type:** ECOSYSTEM POLICY | **Origin:** USER POLICY | **Applies:** design and maintenance of ecosystem/project Agent Skill libraries

The ecosystem Agent Skill Library MUST organize reusable engineering process expertise rather than encode each application's product truth. Universal skills and project-specific/domain skills MUST remain distinguishable; project-specific workflows remain under that project's Master Plan and authority. A catalog/manifest or equivalent discovery contract MUST expose skill name/purpose, applicability, needed permissions, source/provenance and current trusted revision/review state where relevant, plus availability and deprecated/superseded status. No universal directory tree, filename, or copy of each unchanged global skill inside every project is required; reliable versioned references may suffice.

Skills SHOULD be cohesive modules loaded progressively for the current task rather than one universal super-prompt containing frontend, security, deployment, databases, planning, UX, tests, and legal disciplines at once. Identify relevant guidance, load only what is needed, execute within the phase, and leave irrelevant material out of active context where tooling permits. Trivial work needs no dozens of skills. Supporting templates, checklists, scripts, examples, schemas, and references MAY be included, while governing instructions and permissions remain understandable.

Complex skills SHOULD use compact root instructions that route to relevant supporting documents or scripts when needed, instead of loading every workflow or repository document for every task. Reusable guidance SHOULD avoid rigid itineraries that add context or constraints without improving correctness, safety, evidence, or reproducibility. This does not weaken the executable Phase Contract under [DEV-10](#dev-10), required validation, or stop conditions; reusable process guidance and project-specific execution specifications have different responsibilities.

Critical workflow instructions MUST remain reviewable text or equivalent inspectable durable process documentation; an opaque proprietary prompt/service MUST NOT be their only representation. Core expertise SHOULD be portable across current/future cloud models, local models, and human developers, with provider-specific wrappers where useful. Skills SHOULD supply explicit procedure, expected inputs/outputs, stop conditions, validation, and evidence for bounded small-model execution under [DEV-11](#dev-11); limited capability does not justify broader authority.

Initial discovery SHOULD expose concise metadata, loading detailed instructions only for relevant tasks. Prefer one primary skill per concern with complementary specialized/project/review layers, rather than competing frontend/color/architecture/testing/writing foundations. Where skills overlap, record priority, why both are needed, and conflict behavior; governing product/design contracts and constitution prevail. Manage context budget for small models; skill/prompt/plugin count is not a quality metric. Centrally maintained references MUST remain revision-resolvable and support future continuation without silent disappearance; dependency continuity follows [SEC-5](#sec-5).

<a id="skill-2"></a>
### 33.2. SKILL-2 — Subordinate guidance and bounded skill execution

**Type:** ECOSYSTEM POLICY | **Origin:** USER POLICY | **Applies:** selection, invocation, and output of Agent Skills during development or application operations

The execution hierarchy is **Universal Rules → owner policy → App Master Plan → Phase/Task Contract → project-specific design/system rules → relevant Agent Skills → implementation**, subject to actual owner authority/approved exceptions under [GOV-3](#gov-3). A skill MUST NOT override governing rules, owner policy, Master Plan, Phase Contract, project design/system contracts, security boundaries, or authorization. External installed skills MUST NOT silently become universal policy. A skill may guide use of existing authorized capabilities; it MUST NOT independently grant filesystem, deployment, credential, canonical-mutation, or production access, nor inherit every capability available to its host AI. Enforce only the permissions required by the workflow through [AUTH-1](#auth-1) and [AI-2](#ai-2). Frontend review normally needs no production DB writes, secrets, or backup deletion; documentation guidance normally needs no deployment authority.

Skill output, including reviews, recommendations, plans, and classifications, MUST remain subject to evidence, relevant core validation/tests, project contracts, and applicable owner approval. Labels or successful skill execution do not establish factual truth or completion under [EVID-1](#evid-1), [TEST-1](#test-1), and [DEV-13](#dev-13). A skill reference MUST NOT replace project-specific phase objectives, files, constraints, target state, tests, evidence, or stopping conditions under [DEV-10](#dev-10). Materially guiding skill choices SHOULD be discoverable in phase/development metadata to support resumption; source/version/local modifications/permissions follow [SKILL-3](#skill-3). Neither a named adversarial skill nor this catalog supplies constitutional attack authority; verify actual owner authorization and the exact frozen candidate under [GOV-4](#gov-4) and [section 42](#s42).

<a id="skill-3"></a>
### 33.3. SKILL-3 — Skill supply-chain review, revisions, and lifecycle

**Type:** ECOSYSTEM POLICY | **Origin:** USER POLICY | **Applies:** third-party skill consideration/trusted use and maintenance of consequential reusable skills

Third-party Agent Skills MUST be treated as supply-chain inputs. Before trusted use, perform the **Skill Security Review** workflow in [SKILL-4](#skill-4): assess provenance/source/repository/author/version, inspect instructions and supporting resources, scripts/dependencies, requested tools, network/filesystem/shell access, credential exposure, prompt-injection behavior, hidden downloads, and update strategy. This may be performed by an authorized human or trusted tooling; it does not require first executing an unreviewed security-review package. Do not install and execute an Internet skill with full shell/credentials merely because it appears helpful or is described as “only a prompt.” Unreviewed resources remain untrusted under [IO-1](#io-1) and [AI-1](#ai-1).

Trusted reusable skills MUST preserve proportionate provenance and review state where consequential: name/purpose, source, version/revision or equivalent identity/digest, license, author/maintainer, local modifications, reviewed scope, and approving authority where required. Projects MUST be able to identify the revision that materially guided work when review/reproducibility matters. A materially changed remote revision MUST NOT silently replace a trusted skill during an active phase; reassess content, permissions, and affected contracts before trusted adoption. Record actual trust/version identity in the discoverable catalog under [SKILL-1](#skill-1); do not claim unperformed review or infer verified provenance.

Important reusable skills SHOULD have workflow-appropriate validation, such as fixtures, expected output structures, policy-compliance cases, permission tests, or adversarial cases; parsing a prose file alone establishes no trust. Review/modification history SHOULD preserve enough evidence to understand significant past work where needed. Obsolete, insecure, superseded, or incompatible skills MUST be marked and have their trusted invocation state reconsidered; old references do not justify continued automatic use. Preserve useful lineage without retaining unnecessary private payloads under [PRIV-1](#priv-1). General dependency/build safety and privilege boundaries in [SEC-1](#sec-1), [SEC-3](#sec-3), and [SEC-4](#sec-4) remain controlling.

Dynamically fetched remote instructions MUST remain untrusted until validated. Pin/verify content where practical, constrain network access, and record the exact retrieved revision or digest before trusted adoption; mutable `main` or `latest` MUST NOT silently change governing instructions mid-phase. Skill Security Review MUST include installer behavior, symlinks/path traversal, license, dynamic remote resources, and overlap/conflicts as well as scripts, dependencies, permissions, and credentials. Trust registration follows source → revision/license → static/content review → scripts/dependencies → permission/network/conflict review → version/digest → approved discoverable registry. Presence in a registry is a recorded trust disposition, not proof of immunity.

<a id="skill-4"></a>
### 33.4. SKILL-4 — Universal workflow capability catalog

**Type:** ECOSYSTEM POLICY | **Origin:** USER POLICY | **Applies:** ecosystem Agent Skill Library scope and design of the listed reusable workflows

The library blueprint MUST support the following logical workflow families, with discoverable purpose, procedure, inputs/outputs, evidence, validation, and stopping conditions appropriate to each. Implementations MAY combine closely related workflows or split large ones while preserving focused responsibilities; neither one file per row nor loading every family for every task is required. Applicable project contracts remain primary under [SKILL-2](#skill-2). Availability, implemented/reviewed status, and limits MUST be reported honestly rather than treating this policy catalog as installed trusted packages.

| Universal skill family | Required process responsibility and relevant governing contracts |
|---|---|
| Idea refinement | Challenge actual problem, users/workflows, assumptions, constraints, non-goals, failure scenarios, unnecessary features, and alternatives before architecture; [DEV-2](#dev-2). |
| Product differentiation/value | Establish why this product/workflow, actual value, what is meaningfully better/different, and what not to build; personal fit needs no commercial moat under [DEV-18](#dev-18). |
| Research and alternatives | Examine relevant open-source projects, mature libraries, standards/platform APIs, known failures, alternatives/tradeoffs; distinguish verified, inferred, and unknown evidence under [DEV-3](#dev-3), [DEV-8](#dev-8), [EVID-1](#evid-1). |
| Architecture and ADR | Identify responsibilities/boundaries, shared core, components, data ownership, interfaces/dependencies/deployment, alternatives and rationale; produce/update required discoverable decisions under [DEV-7](#dev-7), [DEV-8](#dev-8), [CORE-1](#core-1). |
| Phase planning | Turn the Master Plan into bounded executable phases: objective, prerequisites, permitted/forbidden changes, tasks, invariants, tests/validation, evidence, stop conditions, and next phase; [DEV-10](#dev-10), [DEV-11](#dev-11). |
| Frontend design | Execute [UI-4](#ui-4)–[UI-7](#ui-7) from the brief/platform/identity/design system/accessibility/states/realistic content, explicitly resist generic AI defaults, and support holistic generic-aesthetic review. |
| Design system | Define tokens, components, state patterns, typography/spacing, accessibility and responsive/adaptive rules before screen proliferation under [UI-5](#ui-5). |
| UI/anti-slop audit | Review rendered identity, hierarchy/density, generic defaults, unnecessary elements/fake complexity, states and real content; [UI-4](#ui-4), [UI-7](#ui-7). |
| Usability review | Apply heuristics, progressive disclosure, recovery/status visibility, task flows and proportionate user/owner validation; [UI-7](#ui-7). |
| Product copy/writing review | Plain concrete/action-oriented labels, remove empty AI puffery, preserve product voice and localization/accessibility meaning; [UI-6](#ui-6), [DATA-4](#data-4). |
| Accessibility review | Inspect applicable semantics, keyboard/navigation/focus, screen readers, text scaling, contrast, pointer/touch targets, reduced motion, and non-color-only communication; project/platform standards under [UI-3](#ui-3). |
| API/interface design | Define durable deterministic typed input/output/error contracts, versioning/compatibility, relevant idempotency, authorization, validation, and discovery; [ARCH-3](#arch-3), [AUTH-1](#auth-1), [OUT-1](#out-1), [RETRY-1](#retry-1), [MIGRATE-2](#migrate-2), [INFO-2](#info-2). |
| Security threat model | Identify assets, trust boundaries, principals, entry points/hostile input, authorization/secrets, abuse, blast radius, and recovery; connect existing Raw/ClamAV, AI, NAS, sync, backup/privacy contracts in [SEC-1](#sec-1), [SEC-6](#sec-6), and [DEV-7](#dev-7). |
| Hostile input/malware intake review | Apply Raw/Intake, replaceable ClamAV, scan validity/status, parser isolation, quarantine, source/update security and sync safeguards; [IO-1](#io-1)–[IO-3](#io-3), [SEC-1](#sec-1), [SEC-6](#sec-6), [SYNC-1](#sync-1). |
| Privacy/data minimization review | Review necessary collection/retention/disclosure, sensitive logs/backups/AI context and deletion; [PRIV-1](#priv-1), [PRIV-2](#priv-2), [AUDIT-1](#audit-1). |
| Dependency/supply-chain review | Assess dependencies/provenance/licenses, resolution/pinning, maintenance/vulnerabilities, disappearance, vendor/fork choices, updates and replacement; [SEC-3](#sec-3)–[SEC-5](#sec-5). |
| Testing strategy | Select appropriate unit, integration, end-to-end, property, fuzzing, fault-injection, migration, security, UI/visual/accessibility, and performance evidence. No requirement for every test class in every app; [TEST-1](#test-1), [TEST-2](#test-2). |
| Root-cause debugging | Prefer reproduce → observe → isolate → hypothesize → test hypothesis → establish root cause → minimal correction → regression validation. Do not accept repeated random edits without evidence; preserve known limits when reproduction/root cause remains uncertain under [EVID-1](#evid-1). |
| Performance profiling | Measure relevant startup, memory/CPU/disk/network, queries/index/rebuild, migration/sync/rendering; evidence-driven optimization rather than guessing, within [DEV-16](#dev-16) and [TEST-1](#test-1). |
| Data migration/recovery | Identify source/target versions, snapshots/backups, validation, forward safety, rollback limits, partial failure, recovery and retained meaning; [MIGRATE-1](#migrate-1), [MIGRATE-2](#migrate-2), [RECOVER-1](#recover-1), [BACKUP-1](#backup-1), [BACKUP-2](#backup-2). |
| Backup/restore rehearsal | Restore evidence, failure-domain/credential independence, known-good points, ransomware recovery and derived rebuild; [BACKUP-1](#backup-1), [BACKUP-2](#backup-2), [RECOVER-1](#recover-1). |
| Concurrency/crash-safety review | Applicable locking/fencing, atomicity/partial commits, crash recovery, unknown outcomes/retries; [STORE-1](#store-1), [CON-1](#con-1), [OUT-1](#out-1), [AUDIT-2](#audit-2), [RETRY-1](#retry-1). |
| Distributed state/local-first/sync/NAS review | Replica authority, offline work/conflicts, topology/NAS transitions, backup distinction and malicious mass changes; [SYNC-1](#sync-1)–[SYNC-4](#sync-4), [NAS-1](#nas-1), [OFFLINE-3](#offline-3). |
| Observability/diagnostics review | Actionable errors/health, privacy-safe logs/correlation, supportability and visible failures; [RUN-2](#run-2), [OUT-1](#out-1), [PRIV-1](#priv-1), [HERMES-3](#hermes-3). |
| Locale/timezone/internationalization review | Verify relevant locale-independent values, every App Plan's timezone policy, distinct temporal meanings, parsing assumptions, deliberate Unicode/text semantics, and presentation localization without canonical reinterpretation; [DATA-4](#data-4), [DATA-5](#data-5), [PORT-2](#port-2). |
| Code review | Independently inspect actual correctness, maintainability, security, architectural conformance, error handling/tests, unintended complexity, and regressions; do not assume implementer claims are true under [DEV-13](#dev-13). Independent assessment need not require a different actor for every trivial change. |
| Code simplification | After correctness is established, reduce unnecessary duplication, abstraction/indirection, dead code, overengineering, and generated boilerplate while preserving behavior and meaningful tests; [ARCH-3](#arch-3), [TEST-1](#test-1). |
| Documentation continuity | Reconcile applicable Master Plan, Project State, ADR/decisions, API documentation, phases/Done Phases, recovery/build instructions; [GOV-2](#gov-2), [DEV-7](#dev-7), [DEV-9](#dev-9), [DEV-12](#dev-12), [DEV-17](#dev-17). |
| Brownfield assessment | Assess authorized existing code as compliant/reusable/needs modification/unsafe/obsolete/inconsistent/missing, preserve good work, and avoid preference-driven rewrites; [DEV-14](#dev-14). |
| Release readiness | Assess applicable builds/platform packaging/signing, reconstruction/dependencies, updates, migration/rollback boundaries, backup, documentation and known issues; [SEC-3](#sec-3), [SEC-5](#sec-5), [MIGRATE-1](#migrate-1), [PORT-1](#port-1), [TEST-1](#test-1). Passing this workflow supplies evidence, not authority to ship. |
| Build/release reconstruction | Source/toolchain/assets/commands, packaging/signing, dependency resolution and practical limits; [SEC-5](#sec-5). |
| Adversarial review | Independently challenge plans/implementation for contradictions, edge cases, unsafe assumptions/false guarantees, hidden coupling, privilege/data-loss/migration failures, ambiguous authority, and portability. Required formal reviews still follow [DEV-5](#dev-5) and [GOV-4](#gov-4); skill invocation neither substitutes for nor automatically authorizes the constitutional final review. |
| Skill security review | Mandatory workflow before third-party trusted use: provenance → instruction/content review → scripts/dependencies → permissions → version/digest → discoverable trusted registration. Apply [SKILL-3](#skill-3), [AI-1](#ai-1), and [AUTH-1](#auth-1); never infer broad shell/credential authority from a downloaded skill. |

<a id="s34"></a>
## 34. Requirements-first planning and source reuse

This section makes [DEV-2](#dev-2)–[DEV-8](#dev-8) operational. It supplies the owner's ordered application workflow; it does not create a competing product specification or waive the Plan Freeze Gate.

<a id="plan-1"></a>
### 34.1. PLAN-1 — Nine ordered planning and implementation steps

**Type:** ECOSYSTEM POLICY | **Origin:** USER POLICY | **Applies:** new applications and substantial product replanning

Planning MUST establish what the application must do before final technology selection. The following steps MUST occur in order. Research may revisit earlier assumptions; material changes MUST be reconciled with affected decisions before advancing. Bounded research prototypes follow [DEV-5](#dev-5), and emergency maintenance remains limited by [DEV-17](#dev-17).

1. **Receive the idea.** Accept a short, vague, natural-language description. Programming vocabulary is not a prerequisite.
2. **Investigate the problem.** Research relevant direct solutions, adjacent domains, user difficulties, workflows, papers, GitHub projects, standards, failures, and innovations. Breadth MUST follow relevance and material uncertainty; arbitrary caps on repositories, features, or technical alternatives MUST NOT replace adequate investigation. “Search everything” means exhaustive relevant exploration within actual access and practical evidence limits, not a claim to have searched the entire Internet or authority to access restricted material. Record coverage, remaining gaps, and why the evidence is sufficient to proceed.
3. **Connect the evidence.** Identify plausible needs, relationships, gaps, contradictions, opportunities, risks, and hidden dependencies. Distinguish explicit requirements, strongly supported inferences, research-backed recommendations, speculation, and rejected alternatives under [EVID-1](#evid-1). Inference is not owner approval.
4. **Review consequential product decisions.** Present a coherent recommended scope. Resolve material open questions about purpose, values, experience, privacy, risk, or authority with the owner or within already delegated authority. Ordinary technical choices SHOULD be resolved through research and engineering judgment rather than transferring microscopic decisions to a non-programmer.
5. **Discover existing projects and reusable source.** After initial user review and before final design/technology selection, search GitHub and relevant technical sources beyond exact title matches and obvious categories. Consider whole solutions, partial solutions, libraries, algorithms, design/architecture examples, known failures, and neglected functionality. Apply [PLAN-2](#plan-2), assess actual source before planning its modification, and present adoption/reuse recommendations and meaningful alternatives.
6. **Investigate design and technology.** Apply [TECH-1](#tech-1)–[TECH-3](#tech-3) and [DESIGN-1](#design-1)–[DESIGN-3](#design-3) to the understood workflows and requirements. Use bounded prototypes where evidence is needed before freeze.
7. **Write the comprehensive App Master Plan.** Produce the authoritative intended specification, with meaningful numbered headings, technical records, decisions, and executable phases under [BLUEPRINT-1](#blueprint-1), [BLUEPRINT-2](#blueprint-2), and [EXEC-2](#exec-2).
8. **Attack, repair, and freeze the plan.** Use the strongest reasonably available planning/review capability, targeted research, and independent criticism where possible. Resolve substantiated issues and pass the authorized [Plan Freeze Gate](#dev-5). Ordinary production implementation MUST NOT begin before that gate.
9. **Implement through verified phases.** Execute the authorized numerical sequence under [EXEC-1](#exec-1)–[EXEC-6](#exec-6), preserving actual evidence and the Three-Layer Conformance Gate.

<a id="plan-2"></a>
### 34.2. PLAN-2 — Pinned source ZIP reuse and assessment

**Type:** ECOSYSTEM POLICY | **Origin:** USER POLICY | **Applies:** application planning that considers existing projects and adoption of third-party source foundations

Promising projects MUST be assessed for suitability, source history, maintenance, code quality, security, licensing, platforms, portability, and adaptation cost. The preferred reuse mechanism is a **pinned source ZIP**, rather than creating a GitHub fork. Use a different acquisition mechanism only with a recorded concrete reason and applicable authority; source reuse does not require creating a fork.

An adopted source snapshot MUST record repository URL, exact revision/commit, ZIP origin, checksum or equivalent integrity evidence, license and obligations, imported scope, attribution retained, security-review disposition, and local modifications. Record available authentic source/signature evidence separately: a checksum alone does not authenticate an author. A public repository without an applicable license MUST NOT be assumed to grant modification or redistribution rights. Acquisition, dependencies, continuity, and redistribution remain subject to [SEC-3](#sec-3)–[SEC-5](#sec-5), [IO-1](#io-1), and [SKILL-3](#skill-3) where relevant.

Untrusted downloaded scripts/installers MUST NOT be executed before review. Inspect the actual adopted implementation and apply [DEV-14](#dev-14): preserve correct work, assess gaps, and repair deficiencies without indiscriminate rewriting. The App Plan MUST distinguish imported, modified, replaced, and newly implemented responsibilities.

<a id="s35"></a>
## 35. Technology preferences after requirements

<a id="tech-1"></a>
### 35.1. TECH-1 — Requirements justify the selected stack

**Type:** ECOSYSTEM POLICY | **Origin:** USER POLICY | **Applies:** application and component technology selection

After requirements analysis, evaluate **Rust first for implementation, Tauri 2 first as an application framework, SQLite first when a database is appropriate, and open-source or public-domain solutions first across the relevant stack**. Prefer a feature-first modular monolith where suitable and practical resource efficiency. These preferences are strong starting points, not evidence of suitability. [LANG-1](#lang-1)'s Rust policy and [CORE-1](#core-1)'s shared product core remain controlling.

Concrete evidence of a substantial improvement in required functionality, reliability, platform compatibility, accessibility, maintainability, or user experience may justify another choice. Record affected components, alternatives, requirements, evidence, tradeoffs, and applicable approval under [GOV-3](#gov-3). Popularity or fashion alone is insufficient. Avoid heavyweight technology without demonstrated benefit, and avoid lightweight choices that demonstrably harm essential usability or functionality. A database MUST NOT be introduced merely to satisfy a database preference when documented files meet the requirements better.

<a id="tech-2"></a>
### 35.2. TECH-2 — Open-source scope and actual licensing

**Type:** ECOSYSTEM POLICY | **Origin:** USER POLICY | **Applies:** selection and distribution of technology dependencies

The open-source-first evaluation MUST cover relevant languages/toolchains, frameworks, databases, libraries/components, build systems, developer tools, processing infrastructure, local AI tools/runtimes, and other critical dependencies. Record actual licenses, applicable obligations, compatibility with intended use/distribution, and justified departures. Public GitHub visibility, downloadable source, and marketing descriptions do not establish an open-source license.

Dependency licensing MUST be evaluated for the actual integration and distribution model. Using open-source dependencies does not by itself require publishing the owner's application source; some applicable licenses and arrangements may impose source or other obligations. Do not promise either automatic publication requirements or automatic exemption. Preserve attribution, evidence, dependency provenance, and release continuity under [SEC-3](#sec-3)–[SEC-5](#sec-5).

<a id="tech-3"></a>
### 35.3. TECH-3 — Explicit platform commitments and frontend evidence

**Type:** ECOSYSTEM POLICY | **Origin:** USER POLICY | **Applies:** supported-platform definition and frontend selection

Each product MUST choose its actual desktop/mobile/tablet scope under [PORT-3](#port-3), rather than imply universal support. Where desktop Linux is supported, explicitly assess **Linux Mint, Ubuntu LTS, Arch Linux, and CachyOS** and record supported versions/configurations, test commitments, unsupported cases, and reasons. This requires a disposition for these distributions, not an unsupported guarantee that every distribution works identically.

Explain a selected Tauri architecture accurately: it uses a web-rendered interface with native integration; Rust application logic does not make every frontend component Rust. The owner's preference for web-inspired visual design does not require web languages for every app. Select frontend technology through demonstrated design fidelity, performance, accessibility, integration, and platform suitability, using prototypes when necessary. Compare native-appearing, platform-specific UI and deliberately shared/custom appearance on their merits under [UI-1](#ui-1)–[UI-3](#ui-3). Hybrid strategies require explicit reasons rather than becoming an automatic default. Preserve essential platform behavior and accessibility. Relevant future phone/tablet constraints SHOULD inform desktop-first architecture without claiming unimplemented mobile support.

<a id="s36"></a>
## 36. Data that survives the application

<a id="survive-1"></a>
### 36.1. SURVIVE-1 — Independent retained information

**Type:** ECOSYSTEM POLICY | **Origin:** USER POLICY | **Applies:** retained user-owned information

Retained user-owned information **MUST NOT depend for its existence on the continued installation, availability, or development of the original application**. Provide an independently preserved, documented, practically recoverable representation outside disposable installation state. A format being open or a database being SQLite does not alone satisfy this requirement. The representation MUST be obtainable and recoverable without the original app within the declared retention and recovery contract, including relationships, identifiers, required originals, and interpretation dependencies.

The App Plan MUST document authoritative locations; ownership; actual engine and file formats; appropriate human-readable and machine-readable representations; schemas, identifiers, and relationships; export/import; access without the original app; uninstall behavior; mobile container deletion; encryption/key recovery; backup/restore; replacement/migration; retention/legitimate deletion; and offline, NAS, and synchronization responsibilities. SQL is a language, not a storage engine. SQLite, PostgreSQL, Markdown, HTML, original documents/media, and justified combinations may serve appropriate responsibilities. For retained user-owned information, the accessible workspace under [WORKSPACE-1](#workspace-1) remains required even when both optional protections are OFF. Every qualifying application MUST continuously support mandatory per-file complete Current JSON and verified per-folder Folder JSON manifests under [JSON-1](#json-1), with global Master JSON and external complete backup separately optional. Independently accessible originals, documentation, identity and access without the app remain required regardless of those optional settings; no format choice waives them. Stateless utilities retaining no user information need no such machinery.

A recoverable representation may be an independently accessible authoritative dataset or an independent recoverable copy. Declare when it becomes durable, what information it covers, its freshness and permitted recovery-point loss, and the dependencies and failure domains. Required preservation MUST be established and verified before claiming retained data is protected; an export button that has never produced an independent copy is insufficient. Recovery claims MUST disclose limits rather than promise immunity to all loss. Data preservation does not override authorized erasure, privacy obligations, or expiration under [PRIV-1](#priv-1).

<a id="survive-2"></a>
### 36.2. SURVIVE-2 — Mobile uninstall and disappearance rehearsal

**Type:** CONDITIONAL | **Origin:** USER POLICY | **Applies:** applications retaining user information, including platforms with disposable app containers

The App Plan MUST identify which storage and keys the supported operating system may remove on uninstall, reset, account loss, or device failure. App-private mobile storage MUST NOT be the sole claimed independent representation. Select a platform-supported, authorized preservation route outside that disposable state, such as user-controlled files or independently maintained storage/service copies, with documented access and restoration procedures. Do not assume an uninstall hook, shared-folder name, OS backup setting, export format, or removable app key proves survival. If the required route cannot be established, report the unmet preservation requirement and stop claiming the platform configuration satisfies it; resolve the product/storage contract through planning.

Validate an actual app-disappearance scenario using representative retained information: make the original app/runtime unavailable in an isolated test environment, obtain the independent representation and required keys/schema, recover with documented independent means, and verify meaning, relationships, identifiers, and the declared recovery point. Relevant mobile claims require evidence for actual supported uninstall/container behavior rather than desktop extrapolation. Do not delete the owner's live data to run this rehearsal.

[RECOVER-1](#recover-1), [BACKUP-1](#backup-1), and [BACKUP-2](#backup-2) continue to require complete dependencies, independently appropriate failure domains, and restoration evidence. External location or synchronization alone is not backup safety. `Codebase/Database/` contains implementation artifacts such as schemas, migrations, queries, and storage code/configuration; it is not automatically the location of private user data. Keep private data out of source repositories unless specifically authorized and appropriate under privacy policy.

<a id="s37"></a>
## 37. NO FALLBACKS in the App Plan or Codebase

<a id="nofall-1"></a>
### 37.1. NOFALL-1 — One approved implementation and honest failure

**Type:** PROHIBITION | **Origin:** USER POLICY | **Applies:** planned and implemented application capabilities after implementation selection

**NO FALLBACKS IN THE APP PLAN OR CODEBASE.** Once a capability's implementation is selected and approved, an executor MUST NOT introduce an alternative execution implementation to conceal or work around that implementation's failure. Prohibited behavior includes silent alternate algorithms or providers, hidden secondary databases, replacement execution paths triggered by primary failure, dummy implementations or mock results presented as functioning behavior, disabling required functionality or tests to claim success, fabricated success, silent error swallowing, and undocumented degraded substitutes. Merely naming a substitute an “adapter,” “resilience mode,” “recovery,” or “approved fallback” does not make it compliant.

Define the capability's selected implementation, configuration/platform scope, success criteria, and failure contract in the authoritative App Plan. On failure, report what is known, unknown, blocked, and safely recoverable under [OUT-1](#out-1), [RUN-2](#run-2), and [OPS-1](#ops-1). Implement error paths without falsifying effects or acknowledgements. Test fixtures, mocks, and simulations MAY be used in explicitly identified isolated tests/research; their outputs MUST NOT satisfy claims that real production behavior ran successfully.

<a id="nofall-2"></a>
### 37.2. NOFALL-2 — Safety, offline operation, and platform boundaries

**Type:** ECOSYSTEM POLICY | **Origin:** USER POLICY | **Applies:** interpretation and verification of NOFALL-1 across recovery, platform, offline, security, and synchronization contracts

The following distinctions MUST govern implementation and review:

| Existing responsibility | Compliant meaning under the prohibition |
|---|---|
| Errors, interruption, and rollback | Explicit failure, safe interruption, transaction rollback, security containment, and bounded crash recovery preserve the approved operation/state contract; they do not report substitute success. |
| Retry | A validated retry of the **same approved operation** remains subject to [RETRY-1](#retry-1), effect identity, uncertainty, authorization, and retry bounds. Switching providers/algorithms after failure is not a retry. |
| Backup and restoration | Independent backups and authorized restoration recover retained state under the declared recovery contract. Recovery MUST disclose restored points, losses, conflicts, and unknowns; it does not silently execute the failed capability through a second implementation. |
| Platforms and adapters | Deliberately selected platform adapters may differ by supported target while enforcing the same shared core contract. Their selection is based on the declared platform/configuration, not failure-triggered substitution. No requirement for identical binaries or one physical module is introduced. |
| Local/offline operation | Approved local capabilities are normal capabilities with their own contracts, available independently of online services. A network-dependent action that cannot complete stays failed, pending, or unknown as appropriate. Showing a cached view is permitted only as an explicitly designed view with disclosed freshness; it cannot masquerade as fresh remote success. |
| Synchronization and topology | Declared replicas, authorized topology transitions, and delayed operation queues preserve the same approved sync/authority semantics under [SYNC-1](#sync-1)–[SYNC-4](#sync-4). NAS loss MUST NOT silently create a new canonical database, weaken conflict rules, or acknowledge undelivered remote effects. |
| Optional AI/Hermes | Independent ordinary functionality remains available without optional AI. An AI-native operation remains unavailable/failed/unknown when its approved model cannot perform it; silently switching model/provider or inventing a result is prohibited. HERMES-1 and AI-4 retain their distinct scope. |
| Malware verification | Required gates under [IO-2](#io-2)–[IO-3](#io-3) remain enforced on scanner/signature failure. Independent local capabilities may continue; affected intake stays gated and protection state stays visible. A missing scanner MUST NOT activate an alternate engine or clean-result stub. An explicitly designed multi-engine scan pipeline, if justified, must require its specified stages/results and cannot treat one failed stage as success supplied by another. |
| Replacement and migration | An alternative may be researched, selected, and deliberately adopted as a future version/configuration through the normal planning, authority, migration, and verification gates. This is an explicit change to the approved implementation, not a dormant runtime rescue path. |

These distinctions preserve availability where honestly supported, recovery, privacy, malware containment, the shared core, and data integrity. They do not weaken existing gates. No fallback design is approved merely by listing two implementations in a plan; the plan MUST specify the independent legitimate responsibility of each or select one. Any genuine unresolved conflict MUST stop affected design/implementation and receive an explicit scoped decision under [GOV-3](#gov-3), without silent weakening of either rule.

Mandatory Current JSON and optional complete Master JSON are separate declared recovery representations, not alternate execution implementations. Folder JSON is their integrity and inventory manifest, not a fallback recovery engine. Verified restoration under [JSON-1](#json-1)–[JSON-4](#json-4) remains permitted; stale or incomplete representations MUST NOT silently count as successful saving. Explicit backup-file restoration is likewise an approved recovery operation, not a hidden implementation substitution.

<a id="s38"></a>
## 38. Visual concepts, interaction modes, and named design guidance

<a id="design-1"></a>
### 38.1. DESIGN-1 — Three rendered concepts and deliberate direction

**Type:** DEFAULT | **Origin:** USER POLICY | **Applies:** substantial new user interfaces and material visual redesign

After understanding actual features and workflows, the design process SHOULD produce **three genuinely different rendered concepts** for representative real application workflows. Superficial theme variations, empty moodboards, and generic dashboards do not satisfy the concept purpose. Each direction SHOULD make its information hierarchy, typography, layout, identity, interaction assumptions, and meaningful states assessable. The owner may choose, combine, refine, or delegate selection. When selection is delegated, the AI MAY compare alternatives internally and present the strongest justified direction, recording the decision and why it fits.

Prioritize refined typography, intentional negative space, elegant layout, strong hierarchy, purposeful motion, accessible interactions, thoughtful identity, responsive adaptation, and polished real states. Airy, calm design and the full Notion color palette are owner preference references, not compulsory themes or claims of license to copy proprietary work. Applications MUST NOT be forced into identical fonts, colors, cards, navigation, or design language. Aesthetic formulas, generic generated layouts, arbitrary anti-card bans, and compulsory decorative imagery MUST NOT replace product-specific reasoning. Measurable accessibility standards and justified technical budgets remain applicable; “no aesthetic formulas” does not prohibit contrast, target-size, or performance acceptance criteria. Apply [UI-4](#ui-4)–[UI-7](#ui-7), including actual rendered review.

<a id="design-2"></a>
### 38.2. DESIGN-2 — Modes A, B, and C with accessible motion

**Type:** ECOSYSTEM POLICY | **Origin:** USER POLICY | **Applies:** product visual and interaction design

Design plans MUST distinguish these modes when selecting their direction:

| Mode | Meaning and authorization |
|---|---|
| **A — Refined foundation** | Typography, predictable interaction, accessibility, foundational design quality, and shared motion engineering. |
| **B — Distinctive identity** | App-specific visual identity and expressive presentation; unconventional interactions are not required. A and B may coexist. |
| **C — Experimental interaction** | Unconventional interaction models. **Disabled by default; activation requires an owner request for experimentation.** It never overrides core usability, accessibility, authority, or data protections. |

The shared motion foundation supplies reusable mechanisms, while choreography may differ by app. Preserve reduced-motion behavior and meaningful state communication under [UI-3](#ui-3). Relevant desktop, phone, and tablet layouts MUST adapt workflows and controls to their actual constraints; scaling a desktop screenshot is not responsive design.

<a id="design-3"></a>
### 38.3. DESIGN-3 — Named upstream Skills and future ZIP review

**Type:** ECOSYSTEM POLICY | **Origin:** USER POLICY | **Applies:** consideration and later authorized use of the owner's design Skills

The owner's named upstream workflow references are **Taste Skill** (`Leonxlnx/taste-skill`, `skills/taste-skill`), **Image-to-Code Skill** (`Leonxlnx/taste-skill`, `skills/image-to-code-skill`), and **Apple Design Skill** (`dickwu/apple-design-skill`). These names are owner-provided research references; their presence here is not proof of current source identity, revision, license, instructions, capabilities, installation, or trust.

For this constitution-only integration, these Skills MUST NOT be installed, executed, modified, or imported. Future installation/use awaits the owner's supplied local ZIPs at the appropriate authorized stage. Before trusted use, verify source identity, pinned revision/digest, actual instructions/resources, license/obligations, permissions, scripts/dependencies, dynamic fetches, and conflicts using [SKILL-3](#skill-3). Compare supplied archives with verified upstream evidence; a filename is not identity verification.

Preserve original upstream instructions as supplied for personal use, together with provenance and the reviewed revision. Apply authority/security controls externally through the trusted invocation contract rather than silently rewriting upstream instructions. Unsafe or conflicting instructions remain inapplicable and MUST NOT execute; unresolved conflicts block the affected use. Skills remain subordinate to the constitution, owner decisions, App Master Plan, and phase contract under [SKILL-2](#skill-2).

### 38.4. Cross-application design vocabulary — non-normative

The owner's three-category vocabulary is **Design & User Experience**, **Vibe-Coded Application Quality**, and **Production & System Architecture**. These categories organize related concerns already governed by the applicable design, product-quality, security, data, architecture, deployment and verification rules; they do not create a competing constitution or authorize repository restructuring. The second category concerns authentic product behavior, functioning demonstrations, completeness and evidence-based launch readiness. The third concerns deployment, security, databases, distributed-system correctness, performance, reliability and verified testing.

The following design-style names are references for exploration only, not default themes or requirements: Minimalism, Maximalism, Swiss/International Typographic Style, Brutalism, Surrealism, Neo-Brutalism, Neoclassical, Neumorphism, Scrapbook, Glassmorphism, Bento Grid, Pixel Art, Conceptual/Sketch, Editorial, Y2K, Ethereal, Bohemian, Cyberpunk, Anthropomorphic, Victorian, Cybercore, Synthwave, Graffiti, Gothic, Mixed Media and Wabi-Sabi. “Dotmod UI” is an unverified style reference whose intended definition has not been validated. None of these names supplies evidence of suitability, accessibility, licensing or quality; use remains subject to [UI-4](#ui-4), [UI-5](#ui-5), and [ASSET-1](#asset-1).

<a id="s39"></a>
## 39. Future application repository blueprint and feature organization

The one-file Universal Rules repository and a future application's repository have different purposes. This section's folders belong to **future applications**, not the active constitutional repository, whose sole tracked file is `MASTER_PLAN.md`.

<a id="blueprint-1"></a>
### 39.1. BLUEPRINT-1 — Complete substantial-application blueprint

**Type:** DEFAULT | **Origin:** USER POLICY | **Applies:** substantial future application repositories, with proportionate physical simplification for tiny applications

The following is the detailed default conceptual blueprint implementing [DEV-6](#dev-6). Preserve its discoverable responsibilities. Physical names/layout MAY change when sound engineering or framework compatibility requires it, with an explicit mapping in repository entry instructions. Do not create meaningless empty folders, duplicate implementation areas that have no responsibility, or treat folder presence as evidence of implemented behavior. Tiny apps MAY simplify the hierarchy while preserving applicable safety, continuity, specification, and verification obligations.

```text
Application/
│
├── AGENTS.md
├── README.md
│
├── Master Plan/
│   │
│   ├── Languages and Data/
│   │   ├── 1- stack and languages used.md
│   │   └── 2- How the data is stored.md
│   │
│   ├── Master Plan/
│   │   └── master plan.md
│   │
│   ├── Research and Decisions/
│   │   ├── GitHub Research/
│   │   ├── Technical Comparisons/
│   │   ├── Architecture Decisions/
│   │   ├── Rejected Alternatives/
│   │   └── Evidence/
│   │
│   ├── Design/
│   │   ├── Visual Concepts/
│   │   ├── Approved Design/
│   │   ├── Design System/
│   │   ├── Motion/
│   │   └── Accessibility/
│   │
│   ├── Reviews/
│   │   ├── Frontend Reviews/
│   │   ├── Backend Reviews/
│   │   ├── Database Reviews/
│   │   ├── Architecture Reviews/
│   │   ├── Security Reviews/
│   │   ├── Performance Reviews/
│   │   ├── Integration Reviews/
│   │   └── Final Reviews/
│   │
│   ├── Phases/
│   │   ├── To Be Executed Phases/
│   │   │   ├── Phase-001/
│   │   │   │   ├── phase-001.md
│   │   │   │   ├── subphase-001-001.md
│   │   │   │   ├── subphase-001-002.md
│   │   │   │   └── subphase-001-003.md
│   │   │   └── Phase-002/
│   │   │
│   │   └── Done Phases/
│   │
│   └── project-state.md
│
└── Codebase/
    ├── Frontend/
    │   ├── Features/
    │   └── Shared/
    │
    ├── Backend/
    │   ├── Features/
    │   └── Shared/
    │
    ├── Database/
    │   ├── Schemas/
    │   ├── Migrations/
    │   └── Storage/
    │
    └── Documentation/
        ├── code-map.md
        ├── feature-map.md
        └── dependency-map.md
```

`AGENTS.md` MUST route an executor to applicable authority, the current App Master Plan, Project State, and the next authorized phase. `README.md` MUST provide a beginner-readable project entry point. Existing-app assessment under [DEV-14](#dev-14), relevant Skill metadata under [SKILL-1](#skill-1)–[SKILL-3](#skill-3), and additional review disciplines MUST remain discoverable even where the illustrated tree has no dedicated folder. Links or meaningful records may satisfy these responsibilities without empty scaffolding.

<a id="blueprint-2"></a>
### 39.2. BLUEPRINT-2 — One complete authoritative App Master Plan

**Type:** ECOSYSTEM POLICY | **Origin:** USER POLICY | **Applies:** application specification and related technical documentation

`Master Plan/Master Plan/master plan.md`, or its explicitly mapped equivalent, MUST contain the complete authoritative intended application specification, with extensive meaningful hierarchical numbered headings. Supporting documents supply evidence, detailed technical explanations, and execution records; they MUST NOT become competing sources of intended product behavior. Use direct explanations and precise links for detail while ensuring the Master Plan states every material product decision and governing contract. No arbitrary heading cap is permitted, and empty/redundant headings MUST NOT inflate apparent completeness.

Coverage MUST include, where applicable: vision/purpose; users/problems; success criteria; differentiation; research; GitHub comparisons/reuse; requirements/assumptions; complete feature inventory and individual feature specifications; workflows/navigation/interactions; screens and states; platforms/accessibility; identity/design system/motion; architecture/boundaries; technology; structures/storage; import/export; offline/NAS/sync; security/privacy; AI capabilities/permissions; failure/no-fallback behavior; data survival/recovery; performance/testing/integration; deployment/updates/migrations/maintenance; risks/rejected alternatives; development phases; and acceptance/evidence. The additional contracts already required by [DEV-7](#dev-7), including timezone, locale, dependency disappearance, hostile intake, emergency maintenance, and lifetime growth, remain mandatory where applicable.

`Languages and Data/1- stack and languages used.md` MUST explain final languages, frameworks, components, versions, responsibilities, licensing, platform suitability, decisions, and justified deviations. `Languages and Data/2- How the data is stored.md` MUST explain engine choices, actual formats, paths, schemas, ownership, independent lifecycle, backup, recovery, export, migration, and app-disappearance survival. Their first position in the reading order does not authorize selecting technology before requirements. Update affected technical records and the Master Plan together when intended behavior changes; preserve historical decisions as explicitly superseded evidence under [DEV-8](#dev-8).

For substantial persistent-data applications, this specification MUST separately assess the User Data Workspace, Master Plan, and Codebase architectures and their cross-references under [WORKSPACE-3](#workspace-3). Folder planning, dual-JSON reconstruction, location selection, simulations, and deferred decisions belong in the current specification, not only in historical research.

<a id="blueprint-3"></a>
### 39.3. BLUEPRINT-3 — Feature-first code with real shared boundaries

**Type:** ECOSYSTEM POLICY | **Origin:** USER POLICY | **Applies:** substantial application codebases

Organize code primarily by meaningful feature/domain responsibility under [ARCH-1](#arch-1)–[ARCH-3](#arch-3), with discoverable frontend and backend feature areas where their responsibilities exist. Examples such as Search, Collections, Import, and Settings illustrate feature names, not compulsory features. Shared areas MUST represent actual shared responsibilities; possible examples include motion/components/accessibility/design-system mechanisms and backend authorization/validation/error contracts.

Do not duplicate frontend/backend areas merely for visual symmetry, create a giant universal backend, or add unnecessary layers. The shared Rust core under [CORE-1](#core-1) may be composed of cohesive feature modules; feature-first organization does not authorize parallel product truths. Each boundary MUST have deliberate contracts and effective permissions. A feature MUST NOT bypass another feature's canonical-state, validation, or authorization invariants. Database schemas/migrations/storage implementation remain discoverable, independently of actual private data locations under [SURVIVE-2](#survive-2).

<a id="s40"></a>
## 40. Beginner-readable implementation documentation and simplicity

<a id="doc-1"></a>
### 40.1. DOC-1 — File and function explanations for non-programmers

**Type:** ECOSYSTEM POLICY | **Origin:** USER POLICY | **Applies:** meaningful application source files and important functions

Every meaningful source file MUST begin with appropriate language-native file/module documentation, using clear separators and plain language understandable to a reader without programming experience. Explain, as applicable: **(1)** identity/location, **(2)** purpose, **(3)** what it does, **(4)** what it deliberately does not do, **(5)** owning feature/component, **(6)** actual users/callers, **(7)** dependencies/interfaces, **(8)** data read/modified, **(9)** permissions/boundaries, **(10)** invariants, **(11)** errors/failure, **(12)** relevant tests, **(13)** related Master Plan sections, **(14)** maintenance warnings, and **(15)** relevant architectural decisions. Omit inapplicable detail with care; do not replace an explanation with an unexplained acronym or boilerplate slogan.

Important functions MUST document purpose, inputs, outputs, meaningful callers/interfaces, side effects, data mutations, error conditions, assumptions, security/integrity effects, and dependencies. Explain non-obvious internal operations in simple numbered steps. Do not narrate trivial syntax, invent connections, or let comments substitute for types, tests, contracts, or verification. For generated or externally vendored code whose regeneration, upstream preservation, or language syntax prevents safe inline headers, provide a clearly linked adjacent explanation and provenance mapping; the exception is to placement, not to understandability or traceability.

<a id="doc-2"></a>
### 40.2. DOC-2 — Real relationship maps and synchronized documentation

**Type:** ECOSYSTEM POLICY | **Origin:** USER POLICY | **Applies:** implementation relationships, shared components, and changes affecting documented behavior

Maintain accurate `code-map.md`, `feature-map.md`, and `dependency-map.md` or mapped equivalents under `Codebase/Documentation/`, alongside relevant headers, function documentation, and precise source links. A shared motion module used by actual Search, Collections, Import, and Settings implementations MUST identify those verified consumers. Do not invent these consumers when the features do not exist.

Distinguish direct imports/calls, interface contracts, event paths, data dependencies, and indirect semantic effects. A backend operation that changes UI state does not by itself establish a direct dependency between a frontend animation module and that backend module; document the actual connection path. Use automated extraction/link checks where practical and explicitly record dynamic or semantic relationships that static analysis cannot prove. Relevant documentation MUST be updated during the same verified work that changes its truth. Phase verification MUST detect material documentation drift rather than accepting stale maps silently.

<a id="simple-1"></a>
### 40.3. SIMPLE-1 — Simplicity and the identity-verified Ponytail role

**Type:** ECOSYSTEM POLICY | **Origin:** USER POLICY | **Applies:** code simplification and consideration of the owner's named Ponytail aid

Optimize for understandability, simplicity, appropriate reuse, minimal unnecessary abstraction, maintainability, clear responsibilities, and correctness. Necessary tests, error handling, comments, security checks, accessibility behavior, and documented contracts MUST NOT be removed merely to reduce line count. Simplification preserves [ARCH-3](#arch-3), [TEST-1](#test-1), and the current phase's approved behavior.

The owner intends **Ponytail** to assist code simplicity and maintainability. [Section 44](#s44) identifies an actually inspected relevant upstream project and pinned revision; that evidence does not establish which later archive the owner will supply or authorize trusted execution. Before declaring or invoking its capabilities, verify the relevant Skill/project identity, source, revision, license, scope, and actual instructions; record the evidence and approved bounded role through [SKILL-3](#skill-3). Match the future supplied artifact to verified source; if that identity is unresolved, retain an explicit pending reference and do not substitute an unrelated similarly named project. General code-simplification work remains available under the verified contracts above. Ponytail MUST NOT be installed during this constitution-only mission. Later trusted use remains within the approved phase and cannot expand authority, erase safeguards, or change architecture by itself.

<a id="s41"></a>
## 41. Exact execution, limited repair, and evidence-bearing completion

<a id="exec-1"></a>
### 41.1. EXEC-1 — Strict numerical phases and subphases

**Type:** ECOSYSTEM POLICY | **Origin:** USER POLICY | **Applies:** planned application implementation and conformance execution

Phases MUST execute in ascending numerical order; subphases MUST execute in ascending numerical order within their parent phase. An executor MUST NOT skip unfinished required work, jump from `001.002` to `001.005`, or begin a later phase before the current phase passes its completion gate. A substantial phase MUST have a parent Markdown specification, individually numbered subphase specifications, explicit dependencies, evidence references, and completion status in its folder. Keep phases meaningfully verifiable and subphases independently understandable, bounded tasks. Tiny phases may use one numbered executable subphase in the same file rather than artificial folders; the execution contract still applies.

When a newly discovered dependency or necessary repair changes the sequence, stop affected progression and revise the authorized plan through [DEV-5](#dev-5), [DEV-7](#dev-7), and [GOV-3](#gov-3). Preserve old identifiers and evidence through a supersession/mapping record, assign unambiguous numerical execution order to the revised unfinished sequence, and reconcile Project State before resuming. The executor MUST NOT invent a new order. Bounded in-subphase repair is governed by [EXEC-3](#exec-3). [DEV-17](#dev-17)'s urgent containment path is the existing narrowly scoped exception to ordinary scheduling, not a way to mark skipped work done or resume ordinary features before reconciliation.

<a id="exec-2"></a>
### 41.2. EXEC-2 — Mandatory 33-field executable subphase contract

**Type:** ECOSYSTEM POLICY | **Origin:** USER POLICY | **Applies:** every executable application subphase

Each executable subphase MUST contain these numbered headings with concrete task-specific details. Explicitly explain inapplicability where a field has no relevant content; omission, unexplained placeholders, or “implement correctly” do not satisfy the contract. Additional meaningful headings MAY be added.

1. **Objective.** The exact bounded outcome.
2. **Purpose and rationale.** Why the work is needed and its intended value.
3. **Preconditions.** Required authority, environment, prior evidence, tools, and dependencies.
4. **Previous required subphase.** Exact predecessor and verified completion requirement, or explicit first-task status.
5. **Exact repository starting state.** Branch/revision or resolvable baseline, relevant dirty state, and conditions that must be checked before editing.
6. **Exact files to read.** Paths and relevant sections/symbols, with a bounded navigation route.
7. **Exact files to create.** Paths and ownership/responsibility.
8. **Exact files to modify.** Paths and permitted regions or interfaces.
9. **Files forbidden from modification.** Protected files, systems, data, and boundaries.
10. **Related Master Plan sections.** Exact governing numbered sections/anchors.
11. **Relevant existing implementation.** Reusable components, current behavior, and gaps assessed from actual code.
12. **Required inputs.** Types, examples, provenance, and validity constraints.
13. **Required outputs.** Artifacts, values, observable behavior, and persistence expectations.
14. **Exact implementation steps.** Ordered concrete actions and any expressly delegated ordinary choices.
15. **Required interfaces and signatures.** Names, types, contracts, callers, and compatibility constraints.
16. **Relevant data types and schemas.** Structures, identifiers, versioning, and applicable migrations.
17. **State transitions and side effects.** Preconditions, mutations, external effects, atomicity, and acknowledgement boundaries.
18. **Validation.** Input/domain/state validation and required invariants.
19. **Error handling.** Failure classes, truthful reporting, safe interruption, and recovery behavior.
20. **Security and authorization.** Effective principals, permissions, trust boundaries, privacy, and secret handling.
21. **Edge cases.** Applicable empty, invalid, duplicate, large, concurrent, interrupted, and platform cases.
22. **No-fallback restrictions.** Selected implementation and the prohibited substitutions relevant to this task.
23. **Required comments and file headers.** Applicable explanations and exact documentation updates under [DOC-1](#doc-1).
24. **Connected files and dependencies.** Actual connection paths and affected maps under [DOC-2](#doc-2).
25. **Required tests.** Relevant existing/new test cases and their actual claims; justified inapplicability where appropriate.
26. **Exact validation commands.** Working directory, commands, prerequisites, fixtures, and necessary environment details without disclosing secrets.
27. **Expected results.** Checkable outputs, acceptance conditions, and justified tolerances rather than invented future results.
28. **Repair scope.** Permitted correction areas plus finite attempt/time bounds and escalation threshold.
29. **Conditions requiring escalation.** Missing contracts, authority, incompatible evidence, architectural changes, repeated failure, and other specific stop conditions.
30. **Completion checklist.** All acceptance conditions and applicable conformance checks.
31. **Evidence recording.** Where to record actual changes, commands, outcomes, errors, repairs, unresolved issues, and tested revision.
32. **Project State update.** Exact status, paths, evidence pointers, and next-action changes required.
33. **Next subphase.** Exact next authorized identifier/path, or the parent completion gate when this is the last subphase.

The planning capability MUST resolve major architecture beforehand and provide concrete contracts, examples, expected outputs, and verified commands wherever possible. Distinguish a proposed command from one already executed successfully; commands requiring a future environment must identify that prerequisite. If required information is missing, contradictory, or cannot safely be established, the execution model MUST stop affected work and record the precise unresolved issue. A stronger planning/review process must resolve material ambiguity; an executor MUST NOT invent interfaces, widen permissions, silently change requirements, or guess architecture under [DEV-11](#dev-11).

<a id="exec-3"></a>
### 41.3. EXEC-3 — Evidence-based bounded repair

**Type:** ECOSYSTEM POLICY | **Origin:** USER POLICY | **Applies:** compiler failures, test failures, and similar execution defects during a subphase

An executor MAY attempt correction within the current subphase's expressly authorized repair scope. Before execution, that scope MUST establish finite attempt and/or time limits appropriate to the task, with an unambiguous stop condition; a repair loop MUST NOT reset its budget by relabeling the same failure. Use actual compiler/test/runtime evidence to identify or narrow the cause, make a bounded correction, and rerun the affected validation and required regression checks. Record attempts, evidence, changes, results, and remaining uncertainty.

Repair MUST NOT rewrite unrelated components, disable or weaken required tests/acceptance, add dummy code or prohibited fallbacks, alter requirements, or change architecture without applicable authority. Escalate when the limit is reached, cause cannot be safely resolved, or repair exceeds scope. Record the precise blocker and needed planning decision in Project State. Endless error-repair loops are not progress; a failed repair leaves the subphase unfinished.

<a id="exec-4"></a>
### 41.4. EXEC-4 — Project State and a bare “Continue” request

**Type:** ECOSYSTEM POLICY | **Origin:** USER POLICY | **Applies:** every active application and new-session continuation

The concise Project State required by [DEV-9](#dev-9) MUST expose current phase/subphase; last verified completed phase/subphase; completed capabilities; work in progress and not started; actual implementation status; known blockers and important unresolved errors; applicable observed repository revision and relevant dirty state; next authorized action; phase/subphase paths; and continuation instructions. Its human-readable and machine-readable representations MUST agree; one structured Markdown record may serve both. Do not invent the future commit that will contain a state update.

On receiving only **“Continue,”** an executor MUST read repository entry instructions and Project State, reconcile them against actual files/revision/evidence, locate the first unfinished authorized phase and its first unfinished subphase, load its full contract, and inspect existing partial work before acting. A partial subphase MUST NOT automatically restart from scratch. After passing its gate, the executor MAY continue to the next ordered authorized subphase in the same session. Existing delegation persists; “Continue” does not grant new production, destructive, credential, or other ungranted authority. If observed state contradicts recorded state, reconcile evidence and authorization before proceeding; do not select an easier later task.

<a id="exec-5"></a>
### 41.5. EXEC-5 — Verified checkmarks, Done Phases, and technical reviews

**Type:** ECOSYSTEM POLICY | **Origin:** USER POLICY | **Applies:** subphase/phase completion and application reviews

A phase/subphase heading MUST receive **✅ only after actual verification** of its applicable acceptance criteria. Example: `# ✅ SUBPHASE-001.003 — Database Initialization`. A checkmark is evidence-backed status, not decoration or prediction. Record changes, tests/checks actually performed, actual outcomes, errors, repairs, remaining issues, relevant tested commit/revision, and confirmation of passed acceptance criteria. Unrun checks are not passes; unknown results and incomplete work MUST NOT be marked done.

After all subphases and phase-level checks pass the [Three-Layer Conformance Gate](#dev-13)—Universal Rules, current App Master Plan, and current phase/subphase contract—move or record the parent phase in `Done Phases`, preserve original specifications and evidence, and update Project State. Verify actual implementation rather than the executor's confidence. Material regressions require correction or an explicit authorized disposition under [GOV-3](#gov-3) and [DEV-13](#dev-13); an allowed exception MUST be visible and cannot present an unmet engineering guarantee as satisfied. Historical evidence MUST NOT be erased to make progress appear cleaner. A later discovered regression must be recorded with its affected revision and current status, without falsifying what an earlier check established.

Review records MUST be discoverable by applicable technical responsibility: frontend, backend, database, architecture, security, performance, integration, accessibility/rendered UI, recovery/migration, and final application review. Each review MUST state scope, revision, applicable specification, findings, severity, evidence, required repair, disposition, verification result, and remaining uncertainty. Proportional combined records are allowed where responsibilities remain explicit. Reviews supply findings and evidence; intended product behavior remains authoritative in the App Master Plan. Constitutional reviews additionally follow [GOV-5](#gov-5) and its integrated procedure.

<a id="exec-6"></a>
### 41.6. EXEC-6 — Measurable execution target around four billion parameters

**Type:** ECOSYSTEM POLICY | **Origin:** USER POLICY | **Applies:** application planning and evaluation of small-model execution continuity

Use the strongest reasonably available capability for complex planning under [DEV-4](#dev-4). Design execution artifacts for substantially weaker coding models, including a target class around **4 billion parameters**, by shifting architecture and ambiguity resolution into precise plans, examples, interfaces, bounded context, deterministic tooling, and acceptance evidence. This is a measurable full-build engineering target under [DEV-11](#dev-11), not a guarantee that every model of a particular size can build arbitrary software.

An executor should be able, without prior chat, to **(1)** read entry instructions, **(2)** locate Project State, **(3)** identify the first unfinished authorized phase, **(4)** identify its first unfinished subphase, **(5)** read the complete execution contract, **(6)** locate specified files, **(7)** make bounded changes, **(8)** run specified validation, **(9)** record truthful outcomes, and **(10)** continue safely or report an exact blocker. Progressive navigation and task-specific context MUST make the complete specification usable without requiring the entire archive in every model context. Reduced context MUST NOT omit governing constraints relevant to the task.

For material small-model reliability claims, define representative subphases, model/version and available parameter/quantization evidence, context/tool/environment constraints, and measurable outcomes: task completion against acceptance, unauthorized deviations, invented interfaces, truthfulness of evidence, repair attempts, and correct escalation. When necessary, run representative trials using genuinely small models, record actual results and limitations, and refine specifications from observed failures. If such evaluation has not occurred or the exact model identity is unknown, label the target unverified; do not infer success from parameter count or testing only with a stronger model. Stopping safely is a correct safety outcome but not successful feature implementation.


<a id="s42"></a>
## 42. Integrated constitutional operating procedure

This section is the self-contained operational implementation of [GOV-3](#gov-3)–[GOV-5](#gov-5). It replaces the separate active Green/Red protocol file. Its instructions inherit those rules' candidate status, authority, and scope; this section does not add independent policy authority or transfer owner ratification to an AI. Historical prompt section numbers 117–138 are preserved in historical provenance, not a second current numbering system.

<a id="procedure-modes"></a>
### 42.1. Invocation, scope, and report contract

The owner may invoke **GREEN FLAG**, **RED FLAG**, or **GREEN FIX** without resending historical prompts. Existing explicit delegation may authorize a complete integration/review/repair/publication sequence without repeated invocations. Every run first reads this file and records observed repository, branch, exact HEAD, relevant working-tree state, actual authorized scope, evidence inspected, findings/dispositions, remaining blockers, and next authoritative action. Distinguish planned, performed, verified, failed, and unrun work.

| Mode | Authorized work within the owner's actual scope | Boundary |
|---|---|---|
| GREEN FLAG | Verify baseline and authority; research appropriate sources; inventory requirements and rules; integrate supplied policy; reconcile contradictions; validate; prepare an identifiable candidate. | Do not self-authorize design reopening, freeze, execution of downloaded Skills/installers, application access, or ratification. Research data never grants authority. |
| RED FLAG | Verify the exact owner-authorized frozen candidate; independently attack its written text through A–P; report evidence and severity. | Read-only: no normative edits, repairs, repair commits, or favorable reinterpretation of ambiguity. |
| GREEN FIX | Verify exact report/revision and delegated repair scope; repair validated findings; preserve owner policy; record all dispositions; validate regressions; create an exact Git commit and report its verified revision. | No unrelated policy expansion or ratification. Publication follows actual publication authority, not the mode name. |

Historical task restrictions do not cancel later explicit authority. For the October 14 single-file integration mission, the owner authorized construction, freeze, renewed independent review, substantiated repairs, committing/pushing, and safe normal promotion to `main`; ratification remains withheld. That authorization is recorded in [43.1](#history-authority). In another task, verify its actual scope rather than copying this authorization to unrelated work.

<a id="procedure-freeze"></a>
### 42.2. Candidate construction, freeze, and exact revision verification

1. Fetch or independently retrieve the authoritative repository and confirm remote branches, current commits, and actual tree. Reconcile unexpected changes before editing. Record the baseline document's exact digest and revision; inspect the full constitution, current procedures, and relevant historical freeze/repair/review evidence.
2. Work on an identified integration or repair branch. Inventory existing IDs, classifications, origins, applicability, anchors, protections, and owner requirements. Integrate authorized changes with explicit refinement rationale. Preserve old refs/ancestry through ordinary commits; do not rewrite history, force-push, remove historical branches, or manufacture signatures.
3. Before freeze, validate the intended one-file tree, rule/metadata preservation, heading structure, duplicate IDs/anchors, references, deleted-file independence, governance authority, factuality, proportionality, whitespace, and Git integrity. Resolve substantiated contradictions or document exact blockers. A structural check alone is not semantic verification.
4. Verify explicit owner freeze authority identifying the scope/candidate or delegating construction and freeze of the described integration. A prior scoped delegation is sufficient when it actually covers this revision and workflow; neither Green completion nor a self-written freeze label supplies authority. Without the required authority, RED FLAG stops with **RED FLAG REQUIRES OWNER-AUTHORIZED PLAN FREEZE**.
5. Freeze an exact committed candidate. Record repository URL, branch, full commit, tree/blob where available, filename `MASTER_PLAN.md`, SHA-256, clean/known tree state, authorization source/scope, baseline, and permitted review/repair scope in a separate revision receipt or report. Do not invent a self-referential commit ID inside the file being committed. The receipt may live in a separately identified historical Git ref or final report, preserving the active tree's single-file restriction.
6. Before each Red round, independently verify the commit and candidate bytes against the freeze receipt, read the actual full text, and identify any branch movement or dirty changes. A matching filename, branch name, candidate label, or earlier review summary is insufficient. Do not silently switch to a newer HEAD. Record retrieval or verification failures honestly.
7. Keep review outcomes outside frozen candidate bytes. A report commit on a separate historical ref may advance without changing the target. Any normative repair creates a new target and resets the two-round count. Even a purportedly non-normative byte change requires explicit identity/diff verification and a new receipt; do not claim reviewers examined bytes they did not examine.

Freeze closes ordinary policy brainstorming for the specified candidate. Post-freeze normative change requires a traceable validated defect, demonstrated contradiction, technically false claim, unsafe ambiguity, material incompleteness exposed during attack, or explicit owner reopening authority. A defect discovered outside a full Red round first receives a finding record and applicable repair authority; do not invent a completed Red report. Preserve all earlier target identities and findings.

<a id="procedure-red"></a>
### 42.3. Read-only independent Red battery

The source order is **actual frozen normative text → this integrated operating procedure → supporting historical evidence**. Previous assistant explanations, Green reports, rule counts, favorable verdicts, tools, prompts, or outside intent cannot supply missing wording or excuse defects. Attack what is written. Do not infer correctness from Rust, SQLite, ClamAV, source licenses, backups, strong models, Skills, accessible-looking design, or passing syntax checks.

Exercise every **A–P lens in [GOV-5](#gov-5)** and meaningful interactions among them. These 16 named scopes are mandatory battery coverage: A normative logic; B proportionality; C 20–50-year lifecycle; D loss/ransomware/sync; E malware/Raw/ClamAV; F Skill supply chain; G Hermes/AI authority; H UI/UX/anti-slop; I accessibility; J locale/time; K platforms/Rust; L local-first/NAS; M migration/recovery; N build/release/supply chain; O development governance; and P technical factuality. The detailed attack table in GOV-5 is part of this same document and supplies each scope.

Retain the rc3 additional attacks: no-fallback versus independent local/recovery behavior; mobile uninstall and key loss; source ZIP integrity and rights; requirements-first Rust/Tauri/frontend selection; shared-core feature boundaries; complete App Plan versus small-model context; comments and relationship drift; mandatory sequential subphases versus repair/replanning; experimental design versus accessibility; one-file constitution versus future-app folders; and historical convergence wrongly reused for new bytes.

For RC4, additionally attack literal complete JSON reconstruction; recursive self-inclusion; global serialization cost; simultaneous updates; valid-but-incorrect contents; propagated AI errors; deletion of protected history; external edits and cloud/NAS conflicts; mobile uninstall; unauthorized Skill writes; false recovery guarantees; hash misuse; personal-data erasure; no-fallback interactions; weak-model navigation; selected locations; and partial commits/power failure.

Use independently tasked reviewers with fresh contexts where available. A reviewer must not silently repair its own target or serve as an independent reviewer of its own authored/ repaired candidate. Record author/reviewer roles, attributable task/session identities, context separation, material information shared, evidence access, and any configured versus actually observable model identity. Different model labels alone do not prove independent deployed models. Focused helpers contribute coverage; they do not count as separate complete rounds unless they actually perform and report the complete required scope.

If independent reviewers are unavailable, use distinct sequential passes for useful coverage and disclose that independence is unavailable. Same-author or repeated same-reviewer passes do not satisfy two independent-round convergence by relabeling them. Reviews may use targeted primary-source research; distinguish evidence verified from assumptions. Do not execute untrusted source or install Skills merely to review text.

<a id="procedure-findings"></a>
### 42.4. Finding record and truthful residual-risk statement

Every proposed finding receives a stable report-local identifier, target revision/digest, lens/scope, exact rule/section and problematic quotation, concrete failure scenario, why existing clauses do not resolve it, severity and confidence, smallest viable repair direction, and possible regression risk. Preserve rejected hypotheses proportionately as **NOT AN ISSUE** with reasons. Taste or a preferred alternative is not itself a defect.

| Classification | Meaning |
|---|---|
| BLOCKER | Unsafe ratification: material data-loss/security risk, fundamental contradiction, unenforceable core requirement, or dangerous falsehood. |
| MATERIAL | Substantiated defect requiring correction before ratification even when not immediately catastrophic. |
| NON-BLOCKING | Recorded improvement that does not by itself prevent candidate progress. |
| NOT AN ISSUE | Attack hypothesis rejected after examining wording, applicability, and evidence. |

Every Red report gives counts, exact scope/coverage, sources, uncertainty, reviewer independence limits, and whether it is one round or an evidenced convergence assessment. A report with zero BLOCKER and zero MATERIAL findings states exactly:

> No material defect was identified under the defined review battery. This does not prove absolute correctness, security, completeness, or immunity to future unknown conditions.

When either material class is nonzero, do not assert that clean-result sentence as the review outcome. Report the actual material findings and disclose that other defects may remain and the attack does not prove all defects were discovered. No report calls the constitution unbeatable or permanently secure. These residual limitations apply regardless of convergence.

<a id="procedure-fix"></a>
### 42.5. Green Fix and regression validation

1. Verify the exact Red report, target bytes, findings, current branch/tree, and actual owner repair authority. A later current-session delegation may cover repeated repair/review rounds; it does not authorize unrelated policy.
2. Validate each finding against the text/evidence. Record accepted/repaired, rejected with evidence, duplicate, deferred NON-BLOCKING, or unresolved disposition as appropriate. No BLOCKER/MATERIAL item silently disappears or becomes resolved merely by renaming its severity. An accepted residual engineering constraint requires accurate claims and applicable authority; it cannot create a false satisfied guarantee.
3. Repair only substantiated issues within scope. Preserve owner policy, unaffected rule obligations/metadata/IDs, provenance, and historical reports. When materially new policy is genuinely required outside delegation, record the exact missing authority and stop that affected change.
4. Record each finding's severity, affected rules, scenario, repair, regression impact, evidence, remaining uncertainty, and changed candidate identity. A defect established outside a completed Red round is recorded as such.
5. Re-run applicable rule preservation, reference/tree, factuality, proportionality, conflict, regression, whitespace and Git checks. Inspect the actual patch against the reviewed revision. Do not disable validation or fabricate clean outcomes.
6. Create a Git commit for the repaired candidate and return its exact verified revision/digest. This may be a local commit or, under actual publication authority, a repository Git-object API commit followed by a normal non-destructive ref update. Verify parent ancestry, exact tree/blob bytes, and the resulting ref; describe the operation actually performed rather than claiming a local commit when only a remote API commit was created. Bind the new freeze receipt to the repair/review delegation and new bytes. **Every normative repair invalidates all earlier clean-round credit; attack the changed candidate again.** The repairer's own checks are Green verification, not independent Red review.

<a id="procedure-convergence"></a>
### 42.6. Convergence and owner ratification

A ratification recommendation requires all of the following for the exact current candidate: zero remaining BLOCKER; zero remaining MATERIAL; explicit dispositions of earlier findings; no material regression; passing current structural, technical factuality, and proportionality review; and **two consecutive independent complete Red rounds after the last normative repair with no BLOCKER or MATERIAL findings**. A new material finding breaks the clean sequence. Non-blocking issues remain visible even when the candidate is eligible for recommendation.

If this cannot be completed with available resources, report the exact incomplete scope and review count. An authorized accurately labeled unratified candidate may be published without claiming convergence. Historical rounds on other bytes do not count. A clean report is evidence, not proof of permanent correctness or a grant of adoption authority.

Only the owner or an explicitly delegated ratification authority can ratify. Obtain a separate explicit decision identifying the exact revision/digest, status, applicability/effective date, and any approved scope/conditions. Integration authorization, a phrase such as “Continue,” default-branch promotion, a review recommendation, or a push does not ratify. Until that decision, candidate status remains **NOT RATIFIED**. Preserve the actual decision in revision-bound evidence; do not fabricate a signature or externally verified identity. If status metadata is later changed, distinguish the ratified content from the subsequent record commit and accurately bind the decision to the approved bytes.

<a id="procedure-publish"></a>
### 42.7. Publication and independent remote verification

Publication needs actual owner authority, which the current single-file mission provides for the integration branch and normal safe `main` promotion. Verify repository permissions, branch protection, divergence, and ancestry before promotion. Use ordinary non-destructive commits and ref updates; do not force-push, rewrite old history, delete preserved branches, or bypass protections. If main cannot safely advance, publish the completed integration branch, leave main intact, and report the precise blocker. Tags and releases are not implicit in candidate publication.

The final active/default tree contains **only `MASTER_PLAN.md`**, with no tracked supporting files or folders. New review/verification receipts may be committed to separately identified historical refs; such a ref is explicitly evidence storage, not a second active constitution. Verify candidate identity when using evidence refs that also contain an older historical constitution. Former local documents remain recoverable through Git ancestry and immutable links; active operation never requires them to fill a missing rule or procedure.

After persistence, use a fresh checkout or equivalent independent GitHub retrieval to verify repository/branch, exact remote commit, sole tracked file, absent unexpected files/folders/untracked artifacts in the verification checkout, current structural checks, historical candidate/review recoverability, file SHA-256 matching the tested artifact, and NOT RATIFIED status. Report actual commits and outcomes, including failed/unrun checks and limitations. A successful API response alone is not independent verification of final remote contents.

<a id="procedure-amend"></a>
### 42.8. Future amendments and durable continuation

An amendment starts from the current authoritative revision and actual owner authorization. Record the problem/owner decision, impacted IDs, requirement inventory, technical evidence, proposed precise wording, preserved obligations, explicit replacements, compatibility/transition implications, and remaining uncertainty. Preserve stable IDs wherever compatible; an intentionally retired ID retains a historical disposition and replacement mapping rather than silently disappearing. Preserve classifications, origins, applicability, and separate ratification status accurately.

Integrate on an identified branch, keep the active one-file tree, update cross-references and the preservation map, and perform Green validation. Obtain or verify scoped freeze authority, bind exact bytes, and run the same independent Red/Fix/convergence procedure. Substantive amendments cannot inherit old convergence, and ratification of an earlier version does not ratify the amendment. Do not propagate a constitutional change automatically into unrelated application repositories; each application needs applicable adoption/task authority and its own conformance workflow.

A new session reads this document, the exact revision-bound freeze/review/repair receipts, actual Git state, and current delegation. It resumes the next authorized stage supported by evidence. It does not reconstruct missing authority from historical assistant claims or ask the owner to repeat an already documented decision.

<a id="s43"></a>
## 43. Authorization provenance and historical preservation — non-normative

This section records evidence and change dispositions. It does not create additional normative rules, repeat superseded instructions as active policy, ratify the candidate, or certify subsequent publication/review. Current operating obligations are fully stated in this file; historical sources explain their lineage and remain independently recoverable through Git.

<a id="history-authority"></a>
### 43.1. Historical rc3 integration authority and its limits

The owner supplied **“GPT-6 ASTRA — UNIVERSAL RULES: FINAL INTEGRATION AND SINGLE-FILE CONSOLIDATION MISSION”** for the authoritative repository `mhyahya854/Universal-Rules`. The integration began October 14, 2026. This is a recorded user instruction, not an inferred authorization from a tool, previous assistant verdict, or downloaded source. The source mission says:

> You are authorized to perform this repository integration now. Do not stop after producing recommendations or a theoretical plan. Inspect, consolidate, implement, verify, commit, and push the actual work to GitHub.

> The owner authorizes making the final active/default branch conform to the one-file structure, provided this can be accomplished safely through normal, non-destructive Git operations.

> This is authorization to publish a new unratified candidate, not authorization to declare constitutional ratification.

The same mission directs a new integration branch; exact baseline verification; consolidation of all governing information into `MASTER_PLAN.md`; fresh independent A–P review of the materially changed candidate; substantiated repairs and renewed review; and safe normal `main` promotion after applicable validation. Its Stage G permits accurately labeled publication with incomplete convergence if resources prevent completing the review process, with the limitation disclosed. It preserves owner ratification as a separate exact-candidate decision. It forbids history rewriting, force pushes, deletion of historical review branches, manufactured signatures, and installation/execution/modification/import of the named design Skills during this mission; it also forbids Ponytail installation. No tag, release, unrelated application access, or implicit application migration is authorized by this mission.

The complete active policy resulting from that instruction is included in the governing sections here. The source message need not be present as an additional active file to operate these rules. A source attachment digest identifies received evidence without authenticating an external identity or granting broader authority: **SHA-256 `7658f2762fe3b96f7002000c03ec08339c255aaa6bdf083ff4c5daa984978755`**. The authoring process resumed from existing work artifacts after a session interruption on October 15, 2026; the resumed editor remains the same logical Green author role and does not become an independent Red reviewer through that restart.

Old one-time instructions to wait for a completion phrase, keep work local, restrict a particular repair to RF-01/RF-02, or refrain from review described earlier tasks. Their historical records remain intact; the later explicit mission supplies the current scoped authority under [GOV-3](#gov-3)–[GOV-5](#gov-5). General authority, exact-freeze, read-only Red, repair-scope, review-invalidation, and separate-ratification controls remain active in [section 42](#s42).

<a id="history-baseline"></a>
### 43.2. Exact baseline and historical review scope

| Historical item | Identity and interpretation |
|---|---|
| Earlier default-branch draft | `c2fd9e3d8ac8c41a2ec1e336d2ec097314ef80a5`; 112,709-byte original constitution, SHA-256 `21a6c3b807457a910787425af845324e52783f2e48bf00efb55ef6d9b224e459`. It is an ancestor, not a later competing policy. Its obsolete absolutes are not restored into this candidate. |
| Reviewed integration baseline | `constitution/pre-ratification-working` at `a9c597c8f14536a4404a64494cf56e9015e1288a`; 211,799-byte `UNIVERSL RULES FOR ALL APPS.md`, SHA-256 `1c6471ab3ec5291b9cd4ec884912ccec10431d2e35e9e514ad29574b778b082d`; 113 rules, 33 substantive sections, 146 explicit anchors, 33 Skill families, 21 tracked Markdown files. |
| Earlier freeze and repair | The freeze identified `e15191c1509facc3859b46c25cc8a1d1b7eaa12f`; the subsequent RF-01/02 repair produced the a9c597c baseline. DEV-5 preserved bounded planning experiments without production bypass; GOV-5 corrected the residual-risk statement for non-clean reviews. Their exact receipts remain linked below. |
| Historical review evidence | `review-history/universal-rules-convergence` at `b5ac54fb98304515ae394507ae8dbcd0f6fe54d7`, containing six additional review/verification records. Preserve that historical ref and ancestry; do not treat its older constitution as a second current governing source. |
| Historical convergence only | October 14 round 1 and round 2 each reported zero BLOCKER, zero MATERIAL, and zero NON-BLOCKING for the exact a9c597c candidate/digest. The audit concerns only those bytes. These rounds provide no clean-round credit for this materially revised candidate. |

The historical reports document separate reviewer task/context boundaries, a shared model family/environment, limited helper contexts and prior repair-topic exposure, and unverified exact deployed model variants. A scoped A–F helper and targeted ClamAV supplement are not additional complete rounds. One unsuccessful reviewer task was excluded from convergence. The initial-generation provenance record contains an explicitly unverified historical attestation; this appendix preserves its status and does not recertify it. New review outcomes and publication identities belong to exact-revision receipts under [42.2](#procedure-freeze), with actual independence limitations under [42.3](#procedure-red).

<a id="history-rules"></a>
### 43.3. Historical rc3 original-rule preservation and refinement ledger

The following ledger describes the rc3 integration at `73b2e8adb0236af7d4e503e67f9d507148cc95b7`, not a claim that RC4 leaves every listed body unchanged. RC4 changes are separately mapped in [section 51](#s51). At rc3, all **113 original stable IDs, titles, Type, Origin, and Applies fields** remained. The inventory contains **92 original rule bodies preserved without semantic change, 21 original rules explicitly refined, and 24 new rules: 137 total**. No original rule ID is retired or superseded. Numbered subsection prefixes and conversion of former local provenance links to exact historical URLs are editorial changes and do not count as semantic refinement. Additions and clarification within the 21 listed rules count as refinement even when they remove no obligation.

The 92 unchanged bodies preserve their full applicability, qualifiers, tables, examples, and cross-references. Their IDs, grouped for navigation, are:

| Original family | Unchanged rule bodies |
|---|---|
| SAFE | [SAFE-1](#safe-1), [SAFE-2](#safe-2), [SAFE-3](#safe-3) |
| AUTH | [AUTH-1](#auth-1), [AUTH-2](#auth-2) |
| LANG | [LANG-1](#lang-1) |
| ARCH | [ARCH-2](#arch-2), [ARCH-3](#arch-3) |
| CORE | [CORE-1](#core-1) |
| UI | [UI-2](#ui-2), [UI-3](#ui-3), [UI-4](#ui-4), [UI-6](#ui-6), [UI-7](#ui-7) |
| LIFE | [LIFE-1](#life-1), [LIFE-3](#life-3) |
| DATA | [DATA-1](#data-1), [DATA-2](#data-2), [DATA-3](#data-3), [DATA-4](#data-4), [DATA-5](#data-5) |
| OFFLINE | [OFFLINE-2](#offline-2), [OFFLINE-3](#offline-3) |
| PORT | [PORT-1](#port-1), [PORT-2](#port-2) |
| ASSET | [ASSET-1](#asset-1), [ASSET-2](#asset-2), [ASSET-3](#asset-3) |
| NAS | [NAS-1](#nas-1), [NAS-2](#nas-2) |
| STORE | [STORE-1](#store-1), [STORE-2](#store-2) |
| CON | [CON-1](#con-1), [CON-2](#con-2) |
| OUT | [OUT-1](#out-1) |
| OPS | [OPS-1](#ops-1) |
| RETRY | [RETRY-1](#retry-1) |
| AI | [AI-1](#ai-1), [AI-2](#ai-2), [AI-3](#ai-3) |
| HERMES | [HERMES-1](#hermes-1), [HERMES-2](#hermes-2), [HERMES-3](#hermes-3) |
| AUDIT | [AUDIT-1](#audit-1), [AUDIT-2](#audit-2), [AUDIT-3](#audit-3) |
| EVID | [EVID-1](#evid-1) |
| PRIV | [PRIV-1](#priv-1), [PRIV-2](#priv-2) |
| EDIT | [EDIT-1](#edit-1), [EDIT-2](#edit-2) |
| SYNC | [SYNC-1](#sync-1), [SYNC-2](#sync-2), [SYNC-3](#sync-3), [SYNC-4](#sync-4) |
| RECOVER | [RECOVER-1](#recover-1), [RECOVER-2](#recover-2) |
| BACKUP | [BACKUP-1](#backup-1), [BACKUP-2](#backup-2) |
| IO | [IO-1](#io-1), [IO-2](#io-2), [IO-3](#io-3) |
| MIGRATE | [MIGRATE-1](#migrate-1), [MIGRATE-2](#migrate-2) |
| SEC | [SEC-1](#sec-1), [SEC-2](#sec-2), [SEC-3](#sec-3), [SEC-4](#sec-4), [SEC-5](#sec-5) |
| RUN | [RUN-1](#run-1), [RUN-2](#run-2), [RUN-3](#run-3) |
| TEST | [TEST-1](#test-1), [TEST-2](#test-2) |
| GOV | [GOV-2](#gov-2), [GOV-3](#gov-3) |
| DEV | [DEV-1](#dev-1), [DEV-4](#dev-4), [DEV-8](#dev-8), [DEV-13](#dev-13), [DEV-14](#dev-14), [DEV-15](#dev-15), [DEV-16](#dev-16), [DEV-17](#dev-17), [DEV-18](#dev-18) |
| INFO | [INFO-1](#info-1), [INFO-2](#info-2), [INFO-3](#info-3), [INFO-4](#info-4) |
| SKILL | [SKILL-1](#skill-1), [SKILL-3](#skill-3), [SKILL-4](#skill-4) |

The following refinements state their exact integration purpose; unaffected obligations in each rule remain active:

| Refined original rule | Explicit change and retained protection |
|---|---|
| [GOV-1](#gov-1) | Declare the single current file, integrated-procedure precedence, informative history/research, and explicit conflict disposition; retain every original classification, applicability, candidate-status, and exception distinction. |
| [ARCH-1](#arch-1) | Replace the old no-prescribed-folders statement with the detailed substantial-app blueprint and justified mapped adaptations; retain feature ownership, invariants, proportionality and non-folder architecture choices. |
| [UI-1](#ui-1) | Replace automatic native-presentation preference with the owner’s required native versus shared/custom comparison and justified hybrid selection; retain accessibility, platform behavior, Rust selection and shared-core protections. |
| [UI-5](#ui-5) | Replace the numerical 60/30/10 aesthetic default with product-specific color hierarchy because the new owner instruction rejects aesthetic formulas; retain semantic states, accessible communication, design-system coherence, motion and all other safeguards. |
| [LIFE-2](#life-2) | Add the stronger independent representation and app-disappearance evidence requirements; retain bounded retention, portability, dependencies and maintenance-minimal claims. |
| [OFFLINE-1](#offline-1) | Link honest independent local/cached/pending behavior to the no-fallback boundary; retain useful local operation and genuine remote dependence. |
| [PORT-3](#port-3) | Integrate the explicit permission for app-specific narrower platform scope. Preserve named assessment of Mint, Ubuntu LTS, Arch and CachyOS, reasons/status/testing commitments and actual validation for declared supported targets. The prior blanket first-class baseline expectation is expressly refined by this owner decision; unsupported scope is never reported as tested support, and policy departures retain GOV-3 authority. |
| [AI-4](#ai-4) | Clarify deliberate provider migration versus runtime failure substitution; retain independent ordinary functions, AI-native unavailability, memory inspection/privacy and replaceability boundaries. |
| [SEC-6](#sec-6) | Clarify deliberate scanner selection/composition or future migration versus forbidden failure-triggered engine substitution; retain ClamAV preference, generic capability boundary, platform/IPC/security, private local scanning, provenance and actual licensing review. |
| [GOV-4](#gov-4) | Retain version/rationale/ID/evidence, explicit status and no automatic application adoption; replace obsolete one-time completion/waiting gates with actual scoped current authority and exact freeze/review/repair/publication records. |
| [GOV-5](#gov-5) | Inline the operating procedure; reconcile later authorized freeze/review/publication with old task gates; permit exact verified Git commits through local Git or the authorized repository Git-object API. Preserve read-only Red, all A–P lenses, severity/evidence, repair restriction, review reset, two independent clean rounds and owner-only ratification. |
| [DEV-2](#dev-2) | Add the PLAN-1 link to the mandatory ordered workflow; retain complete initial refinement and no premature implementation. |
| [DEV-3](#dev-3) | Add ordered initial review, dedicated project discovery and pinned ZIP/source-assessment links; retain all research/adoption/alternative and provenance obligations. |
| [DEV-5](#dev-5) | Replace the stale statement that constitutional review remains blocked with actual owner-authorized exact-freeze review. Retain all application Plan Freeze requirements, bounded research experiments, stop gates and emergency limits. |
| [DEV-6](#dev-6) | Replace the old broad APP Plan layout example with the owner’s Master Plan/Codebase blueprint and mapped engineering adaptations; retain every discoverable responsibility, including brownfield assessment and Skill metadata. |
| [DEV-7](#dev-7) | Require the complete authoritative intended product specification in the App Master Plan; supporting references cannot hide material decisions. Retain all original product, time, data, security, research and lifecycle coverage. |
| [DEV-9](#dev-9) | Add subphase/error/Continue details and clarify a stable structured Markdown schema can satisfy both machine and human readability; retain all original current-state and revision reconciliation obligations. |
| [DEV-10](#dev-10) | Replace optional decomposition with mandatory numbered bounded subphases and their detailed execution contracts, with proportionate tiny representations; retain parent contracts, stop/escalation gates, authorized choices and emergency limits. |
| [DEV-11](#dev-11) | Add the measurable approximately 4B development target, distinct from the approximately 1B Hermes product-use target; retain full-build continuity, no hidden context, authority and stop-rather-than-guess safeguards. |
| [DEV-12](#dev-12) | Add subphase evidence and verified checkmark/parent completion references; retain original specifications, actual outcome history, acceptance evidence and no false Done status. |
| [SKILL-2](#skill-2) | Replace the historical final-attack block with verification of actual review authority and exact frozen candidate; retain subordinate Skill authority, effective permission boundaries and evidence requirements. |

<a id="history-new-rules"></a>
### 43.4. Historical rc3 new-rule and owner-decision map

| New rules | Integrated owner decision |
|---|---|
| [PLAN-1](#plan-1), [PLAN-2](#plan-2) | Ordered nine-step planning; broad relevant investigation; consequential owner review; post-review existing-project discovery; source ZIP provenance, licensing and actual implementation assessment. |
| [TECH-1](#tech-1)–[TECH-3](#tech-3) | Requirements before technology; Rust/Tauri 2/SQLite/open-source preferences; actual license scope; platform commitments and frontend evidence. |
| [SURVIVE-1](#survive-1), [SURVIVE-2](#survive-2) | Retained information independent of app installation, actual preserved representation, keys/relationships/formats, mobile deletion and app-disappearance recovery. |
| [NOFALL-1](#nofall-1), [NOFALL-2](#nofall-2) | Enforceable prohibition of failure substitution and false success, with precise same-operation retry, recovery, local/offline, platform, sync and scanner boundaries. |
| [DESIGN-1](#design-1)–[DESIGN-3](#design-3) | Three genuinely distinct rendered concepts; owner delegation; intentional visual direction; A/B/C modes; motion/accessibility; named Skills, later ZIP review and unchanged upstream instruction provenance. |
| [BLUEPRINT-1](#blueprint-1)–[BLUEPRINT-3](#blueprint-3) | Complete future-app folder responsibilities, single authoritative App Plan, technical records, feature organization and shared-core boundaries. |
| [DOC-1](#doc-1), [DOC-2](#doc-2), [SIMPLE-1](#simple-1) | Beginner-readable file/function explanations, truthful dependency maps and same-change drift correction; evidenced Ponytail role and protection against destructive shortening. |
| [EXEC-1](#exec-1)–[EXEC-6](#exec-6) | Strict numbered sequence; all 33 subphase fields; finite repair; Project State and bare Continue; verified checkmarks, completion gates and review disciplines; measurable approximately 4B execution target. |

The integrated governance procedure adds no new stable rule IDs: it operationalizes GOV-3–GOV-5. The 33 original Skill families remain intact under SKILL-4. Retained safeguards also cover domain hazards, effective authority, durable storage/consistency/concurrency, original-versus-derived meaning, privacy/erasure, NAS/sync/conflicts, audit/provenance, Hermes independence, untrusted intake, backups/recovery, migrations, release reconstruction, tests, accessibility, emergency/brownfield work, locale and timezone semantics. This ledger supports review; counts and author assertions do not prove semantic correctness or convergence.

<a id="history-files"></a>
### 43.5. Historical rc3 former-file preservation and consolidation map

The baseline’s 21 tracked files are removed only from the new active tree after consolidation. Their bytes remain available at the immutable baseline links below and through ancestry; the six later review records remain at the separately pinned review-history commit. Historical files retain their own wording and section numbers. No former local file supplies a missing active instruction.

| Pinned historical source | Classification and current preservation/consolidation disposition |
|---|---|
| [UNIVERSL RULES FOR ALL APPS.md](https://github.com/mhyahya854/Universal-Rules/blob/a9c597c8f14536a4404a64494cf56e9015e1288a/UNIVERSL%20RULES%20FOR%20ALL%20APPS.md) | Entire original rule foundation consolidated in sections 1–33 with the explicit refinements above; old section 30 status is historical. Original IDs/metadata remain; no duplicate active constitution. |
| [README.md](https://github.com/mhyahya854/Universal-Rules/blob/a9c597c8f14536a4404a64494cf56e9015e1288a/README.md) | Navigation and summaries; no independent stronger authority. Move useful current reader orientation and lifecycle guidance inline; discard stale current checkpoint as current instruction, retain historical link. |
| [CHANGELOG.md](https://github.com/mhyahya854/Universal-Rules/blob/a9c597c8f14536a4404a64494cf56e9015e1288a/CHANGELOG.md) | Chronology and provenance. Summarize important lineage and link exact historical blob; old pending/blocked/no-push statuses are not current obligations. |
| [decisions/ADR-0001-rust-first.md](https://github.com/mhyahya854/Universal-Rules/blob/a9c597c8f14536a4404a64494cf56e9015e1288a/decisions/ADR-0001-rust-first.md) | Rationale/examples subordinate to LANG-1/GOV-3/CORE-1. Existing governing decisions stay in rules. Optionally summarize useful memory-safety limits and exception rationale inline; examples do not create extra obligations. |
| [governance/green-red-protocol.md](https://github.com/mhyahya854/Universal-Rules/blob/a9c597c8f14536a4404a64494cf56e9015e1288a/governance/green-red-protocol.md) | Active operational substance listed above; must be inline. Source prompt section numbers 117–138 are historical identifiers, not constitution section numbering. Old no-push boundary is conditional on absent authorization. |
| [governance/2026-10-plan-freeze.md](https://github.com/mhyahya854/Universal-Rules/blob/a9c597c8f14536a4404a64494cf56e9015e1288a/governance/2026-10-plan-freeze.md) | Original owner authorization, limits and 6a0d89b→e15191c lineage are historical evidence. Preserve general freeze/repair authority procedure inline. Old design complete/next Red status applies only then. |
| [governance/2026-10-plan-freeze-revision.md](https://github.com/mhyahya854/Universal-Rules/blob/a9c597c8f14536a4404a64494cf56e9015e1288a/governance/2026-10-plan-freeze-revision.md) | Historical exact commit/blob/checksum receipt and non-self-referential revision identification example; no current 827-link target or new review credit. |
| [governance/2026-10-green-fix-rf01-rf02.md](https://github.com/mhyahya854/Universal-Rules/blob/a9c597c8f14536a4404a64494cf56e9015e1288a/governance/2026-10-green-fix-rf01-rf02.md) | Historical authorized RF-01/02 dispositions. Preserve resulting DEV-5/GOV-5 requirements; do not carry 'only these two rules may ever change' into reopened mission. |
| [provenance/initial-generation-boundary.md](https://github.com/mhyahya854/Universal-Rules/blob/a9c597c8f14536a4404a64494cf56e9015e1288a/provenance/initial-generation-boundary.md) | Explicitly unverified historical drafting attestation, never an active directory-access prohibition or current agent attestation. Preserve recoverability, don't recertify. |
| [research/2026-10-ui-product-agent-skills.md](https://github.com/mhyahya854/Universal-Rules/blob/a9c597c8f14536a4404a64494cf56e9015e1288a/research/2026-10-ui-product-agent-skills.md) | Historical 18 pinned repository assessments, 109 inspected-file inventory, 23 externally supplied primary summaries, blocked retrievals and reference-only trust dispositions. Preserve evidence distinctions in provenance. No install permission, mandatory vendor style, or current trust certificate follows. Governing source/security/outcome rules already live in SKILL/UI/AI/SEC/EVID. |
| [reviews/2026-10-astra-adversarial-review.md](https://github.com/mhyahya854/Universal-Rules/blob/a9c597c8f14536a4404a64494cf56e9015e1288a/reviews/2026-10-astra-adversarial-review.md) | Original c2fd9e3 attack, findings/tables and 20 priorities. Historical regression leads, not competing current rules or proof of exact model identity. |
| [reviews/2026-10-rc1-integration-disposition.md](https://github.com/mhyahya854/Universal-Rules/blob/a9c597c8f14536a4404a64494cf56e9015e1288a/reviews/2026-10-rc1-integration-disposition.md) | F01–F56 accepted/modified dispositions and 34 factual corrections mapped to rc1. Preserve lineage; don't revive old absolutes or treat old validation as new artifact validation. |
| [reviews/2026-10-rc1-verification-outcome.md](https://github.com/mhyahya854/Universal-Rules/blob/a9c597c8f14536a4404a64494cf56e9015e1288a/reviews/2026-10-rc1-verification-outcome.md) | Historical d9fc392 recommendation and N1–N4, not actual ratification or current review. N1 language artifact scope, N2 exception lifecycle, N3 WAL qualification, N4 independent dimensions remain in normative rules. |
| [reviews/2026-10-pre-attack-integration.md](https://github.com/mhyahya854/Universal-Rules/blob/a9c597c8f14536a4404a64494cf56e9015e1288a/reviews/2026-10-pre-attack-integration.md) | Product platform/shared-core/UI/offline/sync/SVG/Hermes decisions integrated; old pending Hermes marker superseded. |
| [reviews/2026-10-development-governance-integration.md](https://github.com/mhyahya854/Universal-Rules/blob/a9c597c8f14536a4404a64494cf56e9015e1288a/reviews/2026-10-development-governance-integration.md) | DEV-1–15 lineage and matrix, not an instruction to repeat initial planning or wait for already supplied Hermes design. |
| [reviews/2026-10-four-app-blueprint-integration.md](https://github.com/mhyahya854/Universal-Rules/blob/a9c597c8f14536a4404a64494cf56e9015e1288a/reviews/2026-10-four-app-blueprint-integration.md) | Mosaic, LMS/Studies, Accounting & Money, Read & Watch are owner-supplied generalized design provenance only; no app repository dependencies, no imported domain-specific folder rules. All active INFO/HERMES/DATA/EVID/OPS contracts must stay inline. |
| [reviews/2026-10-final-policy-gap-integration.md](https://github.com/mhyahya854/Universal-Rules/blob/a9c597c8f14536a4404a64494cf56e9015e1288a/reviews/2026-10-final-policy-gap-integration.md) | Seven gap decisions and timezone/malware additions already normative. Old unfrozen/owner-completion status superseded; preserve general emergency/growth/locale/accessibility/recovery obligations. |
| [reviews/2026-10-raw-intake-clamav-integration.md](https://github.com/mhyahya854/Universal-Rules/blob/a9c597c8f14536a4404a64494cf56e9015e1288a/reviews/2026-10-raw-intake-clamav-integration.md) | IO-2/3, SEC-6 provenance; owner's then-reported archive was not inspected/certified. Keep actual malware/receipt/platform/license requirements in rules. |
| [reviews/2026-10-green-ui-product-skills-integration.md](https://github.com/mhyahya854/Universal-Rules/blob/a9c597c8f14536a4404a64494cf56e9015e1288a/reviews/2026-10-green-ui-product-skills-integration.md) | Historical earlier research block and broad UI/33-family integration. Block later dispositioned; no current demand to repeat that source research without material need. |
| [reviews/2026-10-ui-design-agent-skills-integration.md](https://github.com/mhyahya854/Universal-Rules/blob/a9c597c8f14536a4404a64494cf56e9015e1288a/reviews/2026-10-ui-design-agent-skills-integration.md) | Second-prompt coverage only, no new normative bodies. 21 original plus 12 later Skill families = current 33; no installed packages implied. |
| [reviews/2026-10-primary-source-reconciliation.md](https://github.com/mhyahya854/Universal-Rules/blob/a9c597c8f14536a4404a64494cf56e9015e1288a/reviews/2026-10-primary-source-reconciliation.md) | Historical owner disposition of proxy block, SKILL-1/UI-7 refinements, source evidence distinctions. Preserve limitations, do not falsely claim direct live-page reads. |
| [review-records/2026-10-14-red-round-1.md](https://github.com/mhyahya854/Universal-Rules/blob/b5ac54fb98304515ae394507ae8dbcd0f6fe54d7/review-records/2026-10-14-red-round-1.md) | One full fresh-context A–P review of a9c597c only, zero B/M/NB. Shared GPT-6 family/environment and helper context limits disclosed. Historical, not new candidate credit. |
| [review-records/2026-10-14-red-round-2.md](https://github.com/mhyahya854/Universal-Rules/blob/b5ac54fb98304515ae394507ae8dbcd0f6fe54d7/review-records/2026-10-14-red-round-2.md) | Second distinct full review of same bytes, zero B/M/NB. Did not read round 1; repair record disclosed two prior topics; deployed model variant unauthenticated. Historical only. |
| [review-records/2026-10-14-scoped-red-a-f.md](https://github.com/mhyahya854/Universal-Rules/blob/b5ac54fb98304515ae394507ae8dbcd0f6fe54d7/review-records/2026-10-14-scoped-red-a-f.md) | Scoped inherited-context subreview, never a full independent convergence round. Historical regression cases. |
| [review-records/2026-10-14-clamav-incomplete-scan-supplement.md](https://github.com/mhyahya854/Universal-Rules/blob/b5ac54fb98304515ae394507ae8dbcd0f6fe54d7/review-records/2026-10-14-clamav-incomplete-scan-supplement.md) | Targeted NOT AN ISSUE adjudication, not a full round. Incomplete/limit-skipped scanning cannot satisfy required CLEAN gate under IO-2/3; no implementation test or exact adapter/exit-code proof. Preserve policy meaning; historical wording need not be made a new universal scanner mechanism. |
| [review-records/2026-10-14-final-convergence-audit.md](https://github.com/mhyahya854/Universal-Rules/blob/b5ac54fb98304515ae394507ae8dbcd0f6fe54d7/review-records/2026-10-14-final-convergence-audit.md) | Historically reports convergence for exact a9c597c and limitations, not permanent correctness. One failed review agent was excluded. Current material revision resets review. |
| [review-records/2026-10-14-remote-verification-receipt.md](https://github.com/mhyahya854/Universal-Rules/blob/b5ac54fb98304515ae394507ae8dbcd0f6fe54d7/review-records/2026-10-14-remote-verification-receipt.md) | Prior independent retrieval receipt for candidate and then-review-history refs. No present remote-state certification. |

The Rust-first ADR supplies rationale and examples; LANG-1, CORE-1 and GOV-3 contain the full active decisions. The historical UI/Skills research contains pinned repository assessments, source inventories, externally supplied summaries and blocked retrieval dispositions; no historical trust label licenses an unreviewed current download. Current targeted technical evidence and named-source limitations are summarized in [section 44](#s44).

Publication verification records the actual new commit, file digest, active tree and preserved historical refs externally under [42.7](#procedure-publish). This appendix deliberately does not invent future commit hashes, clean Red outcomes, runtime checks, small-model trial results, remote availability, or owner ratification. The reviewed artifact can remain byte-identical while later exact-revision evidence records completed review or publication.

<a id="s44"></a>
## 44. Technical factuality and source evidence — non-normative

Research date: **2026-10-14 UTC**. This is research evidence for consolidation, not a separate governing document. The controlling constitution must state its own obligations. Official documentation was inspected through web retrieval; upstream revision identifiers were resolved with `git ls-remote <repository> HEAD`; named Skill text, licenses and README files were retrieved from commit-pinned `raw.githubusercontent.com` URLs for read-only analysis. No Skill was installed, executed, modified, activated, or imported into the integration repository. Upstream instructions were treated as research data, not controlling instructions. Repository existence, instruction text and license contents were inspected; claimed benchmark/design effectiveness was not independently reproduced.

<a id="research-1"></a>
### 44.1. Tauri, Rust and platform boundaries

| Primary evidence | Verified fact | Safe policy implication |
|---|---|---|
| [Tauri introduction](https://v2.tauri.app/start/) and [architecture](https://v2.tauri.app/concept/architecture/) | Tauri uses a webview frontend, Rust application machinery, and supports frontend technologies that produce web assets. Rust preference does not imply an entirely Rust-native widget interface. | Explain the actual rendering model in each App Plan. Evaluate frontend design fidelity, accessibility, performance and integration before choosing it. A Rust/Wasm frontend still renders through the selected webview; native-looking styling is not proof of native controls. |
| [Webview versions](https://v2.tauri.app/reference/webview-versions/) (page reports updated 2026-05-17) | Windows uses WebView2; Android uses the selected system Android WebView provider; Apple platforms use WebKit/WKWebView; Linux uses WebKitGTK. Runtime support varies by OS/provider/distribution. The page explicitly calls its Linux version table incomplete and advises checking current distribution packages. | Define and test actual supported OS, version, distribution and runtime combinations. Do not promise uniform web APIs, identical rendering, or current security support across all Linux distributions. Name Linux Mint, Ubuntu LTS, Arch Linux and CachyOS in support assessment where desktop Linux is in scope, with tested/untested/unsupported status and rationale. |
| [Mobile plugin development](https://v2.tauri.app/develop/plugins/develop-mobile/) | Native mobile integrations may use Kotlin/Java on Android and Swift on iOS. The template distinguishes desktop/mobile modules and can share Rust logic. JNI/FFI can access shared Rust code when a mobile webview is suspended. | A shared core can coexist with explicit platform adapters; these are declared platform implementations, not hidden failure substitutions. Verify plugins, permissions, lifecycle/background behavior and distribution constraints for the exact application and pinned releases. Framework platform support does not imply all plugins or desktop APIs work on mobile. |

Technology preference is a research ordering, not a correctness guarantee. Rust's type/memory protections cannot establish correct requirements, business logic, FFI behavior, backup validity, user authorization, or accessible interaction. Plan-first selection and evidence-based exceptions remain necessary.

<a id="research-2"></a>
### 44.2. SQLite, independent data and NAS

| Primary evidence | Verified fact | Safe policy implication |
|---|---|---|
| [Appropriate uses for SQLite](https://www.sqlite.org/whentouse.html) (page updated 2025-05-31) | SQLite is well suited to device-local application storage and application file formats. It permits one writer at a time per database file. Many concurrent writers or direct remote storage can favor a client/server design. A server can itself use SQLite locally behind its API. | Prefer SQLite when the workload fits; measure concurrency, data scale, durability requirements and operating environment. Do not mandate a database for products better served by files. SQL is a language; SQLite is an engine and database-file format. |
| [SQLite over a network](https://www.sqlite.org/useovernet.html), [WAL](https://www.sqlite.org/wal.html), [database format](https://sqlite.org/fileformat.html) | Network filesystem locking/durability semantics can invalidate assumptions. Standard WAL relies on processes sharing local coordination; it is not a supported way for independent clients on different hosts to concurrently operate a database through a network filesystem. | Do not put an actively shared SQLite/WAL database on a NAS and assume safety. Select and document a validated architecture: local database plus controlled synchronization/consistent backup, or a service that owns local database access, or a justified client/server engine. NAS storage is not itself synchronization or backup. |
| [SQLite backup API](https://www.sqlite.org/backup.html) | SQLite supplies consistent online backup methods, including the backup API and `VACUUM INTO`. A naive file copy during database activity is not equivalent to a validated snapshot. | Specify snapshot creation, successful completion, consistency verification and restore testing. Account for journal/WAL state. Independently preserved data must include schemas, identifiers, relationships, formats and usable encryption/key-recovery information. |
| [SQLite copyright](https://www.sqlite.org/copyright.html), [SQLite warranty/license scope](https://www.sqlite.org/purchase/license) | The SQLite core is public domain. Some extensions are proprietary and have separate rights. | Verify the actual packaged dependency graph and extension licenses; do not project the core's rights onto all wrappers or extensions. |

<a id="research-3"></a>
### 44.3. Mobile uninstall and actual data survival

| Primary evidence | Verified fact | Safe policy implication |
|---|---|---|
| [Android app-specific storage](https://developer.android.com/training/data-storage/app-specific), [storage overview](https://developer.android.com/training/data-storage), [shared storage](https://developer.android.com/training/data-storage/shared) | App-specific internal and external files are removed at uninstall. Shared user data can remain independently of the app. External app-specific storage is still app-specific; the word external does not establish uninstall survival. | Retained user-owned information cannot exist solely in the app's disposable container. Specify a platform-supported independently accessible representation and actual preservation schedule. |
| [Android Storage Access Framework](https://developer.android.com/training/data-storage/shared/documents-files) | The system document picker lets users create/select documents and grant access through document providers. | Use scoped, consented document access where appropriate; document provider availability, ownership, export format and recovery path. Presence in a provider alone does not prove independent backup or indefinite availability. |
| [Apple storage management](https://support.apple.com/en-us/108429), [Apple file system guide](https://developer.apple.com/library/archive/documentation/FileManagement/Conceptual/FileSystemProgrammingGuide/FileSystemOverview/FileSystemOverview.html) | Offloading an app retains its documents/data; deleting an app removes its related local data. App-container Documents/Library locations are not an independent survival guarantee. | Test deletion, not merely offload. Do not equate exposing container documents in Files with preservation outside that container. Use a documented independent document/export/backup destination and test actual survival for the selected destination and OS version. |
| [Apple remove/delete apps](https://support.apple.com/guide/iphone/remove-or-delete-apps-iph248b543ca/ios) | Separately stored iCloud data can survive app deletion; this does not establish indefinite availability or original-app-independent interpretation. | Describe account/service dependence, offline availability, formats and keys. Cloud synchronization, retention and backup are distinct contracts. Respect authorized erasure rather than promising permanent retention. |

Required policy interpretation: independently preserved information must actually exist before app loss, within the declared recovery point and retention contract. Merely providing an unused Export button does not prove the requirement. Prove recovery with the original app unavailable, including installation/container loss as applicable, using documented independent tools and keys. Avoid claims of survival across arbitrary destruction or authorized erasure.

<a id="research-4"></a>
### 44.4. Source ZIP integrity and legal reuse

[GitHub licensing guidance](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/licensing-a-repository) explains that public visibility without a license does not grant general rights to reproduce, redistribute or make derivative works. License identification must cover imported files, dependencies, bundled assets and notices. Dependency use does not automatically require publishing the owner's application: actual obligations depend on the specific licenses and use/distribution model.

[GitHub source archive documentation](https://docs.github.com/en/repositories/working-with-files/using-files/downloading-source-code-archives) distinguishes a commit-pinned snapshot from a movable branch/tag. Archives omit full repository history. Archive compression may change while extracted source remains the same; repository renaming can change the archive's root-directory name.

Safe policy: prefer the owner's pinned ZIP mechanism. Record upstream URL, full commit, exact archive URL/origin, retrieval date, received archive SHA-256, extracted-content manifest or equivalent source verification, license/attribution, imported scope, local modifications, and security assessment. Preserve the reviewed archive when authorized. A self-computed hash identifies received bytes but does not by itself authenticate their author or establish trust. Verify signatures/attestations when available and relevant; do not invent them. Inspect archive paths/symlinks, scripts/installers, submodule and large-file dependencies before controlled extraction/use. A later generated ZIP with different compressed bytes requires investigation against pinned extracted contents, not automatic treatment as identical or malicious. A source ZIP contains no implied permission to execute its contents.

<a id="research-5"></a>
### 44.5. Named Skill references — exact observations

All commit identifiers below were resolved on the research date and are observations, not perpetual recommendations. The owner's later local ZIP may represent a different revision and must be matched and assessed at that time. The constitution should preserve upstream instructions as supplied while applying separate constitutional precedence, applicability and authority controls.

| Reference and exact inspected revision | Verified identity/scope | Licensing and limits |
|---|---|---|
| [Taste Skill](https://github.com/Leonxlnx/taste-skill/blob/f624f37a8c650b9cc550253104925efe4c8de246/skills/taste-skill/SKILL.md), `f624f37a8c650b9cc550253104925efe4c8de246`, path `skills/taste-skill/SKILL.md` | Frontmatter name `design-taste-frontend`. Current v2 scope is public-facing websites; it explicitly excludes dashboard/app screens. Workflow references Node/browser scripts and asset searches. These were not executed. | [MIT LICENSE](https://github.com/Leonxlnx/taste-skill/blob/f624f37a8c650b9cc550253104925efe4c8de246/LICENSE), copyright Leonxlnx 2026, requires preserving copyright/permission notices. Named preference does not automatically authorize its house style, mandatory imagery, fixed iteration counts or fallback directions to replace the approved App Plan. |
| [Image-to-Code](https://github.com/Leonxlnx/taste-skill/blob/f624f37a8c650b9cc550253104925efe4c8de246/skills/image-to-code-skill/SKILL.md), same revision, path `skills/image-to-code-skill/SKILL.md` | Frontmatter name `image-to-code`; instruction workflow generates/analyses website design images then implements matching frontend. Its described focus is website/landing/editorial/product-page work. | Same repository MIT license, subject to scope and third-party asset rights. Image resemblance is not rendered application, accessibility, state or functionality validation. |
| [Apple Design Skill](https://github.com/dickwu/apple-design-skill/blob/904b0eedc7cc778152f545506075d5bb5219ce77/SKILL.md), `904b0eedc7cc778152f545506075d5bb5219ce77`, path `SKILL.md` | Frontmatter name `apple-design`; review instructions reference Apple HIG and cross-platform translation. The README describes 123 HIG pages and a scraper; those are upstream claims, not independently validated content coverage or correctness. | Root tree contains no LICENSE; raw LICENSE returned 404. [README origin/license section](https://github.com/dickwu/apple-design-skill/blob/904b0eedc7cc778152f545506075d5bb5219ce77/README.md#origin-and-license) attributes HIG text to Apple, disclaims affiliation, and says skill/guide/script are provided as-is. An explicit open-source license grant was not verified. Keep reuse/redistribution rights unresolved pending actual rights review; public availability and personal-use intent do not establish a license. Do not copy its HIG collection into this constitution. |
| [Ponytail](https://github.com/DietrichGebert/ponytail/blob/2961b52fc1fe6a5a87c7a959a79512e5c2f3ffe5/skills/ponytail/SKILL.md), `2961b52fc1fe6a5a87c7a959a79512e5c2f3ffe5`, path `skills/ponytail/SKILL.md` | Actual relevant code-simplicity instruction project identified. Frontmatter name `ponytail`; promotes the smallest complete change, existing code/platform/library reuse and comprehensible implementations. It explicitly protects validation, loss-preventing handling, security, accessibility and requested behavior. | [MIT LICENSE](https://github.com/DietrichGebert/ponytail/blob/2961b52fc1fe6a5a87c7a959a79512e5c2f3ffe5/LICENSE), copyright DietrichGebert 2026. Other similarly named repositories exist; this is the evidenced relevant upstream match, not proof of which archive the owner will supply. No benchmark or future weak-model effectiveness guarantee. |

Ponytail's one-line why-comment instruction conflicts with the owner's required beginner-readable documentation; the constitution and App Plan prevail. Its simplification, default/full/ultra modes and smallest-version advice cannot delete approved scope, rewrite architecture without authorization, remove tests/handling/comments, relax acceptance criteria, or override ordered phases. Use it only as reviewed advice within the approved task, and validate the result. Likewise, Taste's use of the word fallback cannot authorize a prohibited alternate execution implementation; approved accessible reduced-motion/static presentation should be specified as normal presentation behavior, not failure substitution.

<a id="research-checksums"></a>
#### 44.5.1. Inspected upstream file checksums

- Taste `skills/taste-skill/SKILL.md`: `ee847084e58f5a81a46120912be9cd15f083570a6ca8f3d1a30372a720633043`.
- Image-to-Code `skills/image-to-code-skill/SKILL.md`: `4c060a8064a8b13380bc2ef3d6e6a1d0b1e316aa093cd9807d0ce9e4eeb037fa`.
- Taste repository `LICENSE`: `4575a543ab88dad12ccea7d97e563d0bce5b448b06072e65d3264497dad326df`.
- Apple `SKILL.md`: `ec7b6e5ebf3477288ce547a1245e5b5234011ac6fa6dd25c2abdad0699dbd30b`.
- Ponytail `skills/ponytail/SKILL.md`: `ba68ff26239c3c3b05b2a9a47ee0d9a6b93a69639a2555ec87a5d44bffaf2f0c`.
- Ponytail `LICENSE`: `fb1bc6909ac3ef82d5c22106e32ef682b0cff66788fa915fb9b53b15c9d2f3ab`.

These are retrieved-file hashes, not ZIP hashes or signature verification. No owner ZIP was supplied or assessed in this research. Full script/dependency security audits and execution tests of these Skills remain for an appropriately authorized application stage.

<a id="s45"></a>
## 45. User-owned data workspace and folder architecture

The information is the durable product; the application is a replaceable interface for accessing, interpreting, editing, and managing it. The following are owner policies for applicable retained-data applications, not requirements for stateless utilities retaining no user information. All new rules inherit CANDIDATE status under GOV-1.

<a id="workspace-1"></a>
### 45.1. WORKSPACE-1 — Independently accessible durable workspace

**Type:** ECOSYSTEM POLICY | **Origin:** USER POLICY | **Applies:** applications retaining user-owned information

<a id="workspace-access"></a>
#### 45.1.1. Independent access and physical adaptation

The App Plan MUST define one logical, discoverable, documented, independently accessible user-owned data workspace, separate from disposable application installation state. It SHOULD use a real user-accessible folder structure wherever the supported platform permits it. A technically necessary physical adaptation MUST document its mapping and preserve independent discovery, access and recovery outcomes; hidden opaque storage is not an equivalent substitute. Ordinary original documents/media and human-readable files MUST remain present and independently accessible within the supported storage/security contract. SQLite and other operational stores MAY serve appropriate responsibilities but MUST NOT replace the original independently accessible workspace, mandatory per-file Current JSON, verified Folder JSON or enabled optional full global Master JSON under [JSON-1](#json-1).

<a id="workspace-survival"></a>
#### 45.1.2. Planning priorities and platform survival

Planning MUST prioritize human comprehension, information preservation, independent recovery, clear folder relationships, deterministic machine navigation, safe AI operations, scalability, and long-term compatibility. Document access without the original application, schemas/readers, retention and key dependencies under [SURVIVE-1](#survive-1)–[SURVIVE-2](#survive-2). An independently preserved recovery representation must actually survive the declared application-disappearance scenario; exposing app-private files through a picker or calling them external does not establish survival. Supported phone/provider access, permission persistence, offline availability and uninstall behavior MUST be researched and validated; arbitrary permanent filesystem access MUST NOT be promised for every phone or cloud service.

<a id="workspace-2"></a>
### 45.2. WORKSPACE-2 — Selected location, identity, movement, and reconnection

**Type:** ECOSYSTEM POLICY | **Origin:** USER POLICY | **Applies:** setup and lifecycle of retained-user-data workspaces

<a id="workspace-selection"></a>
#### 45.2.1. Setup and stable identity

Every applicable App Plan MUST identify where actual data lives. Each managed workspace on each device MUST have one selected physical storage root. A shared logical workspace may synchronize across devices that each have their own validated local root; a common path or raw shared filesystem is not implied. First setup MUST present the proposed persistent workspace location, major folder paths, settings, history, JSON and recovery locations, any data outside the workspace, and adoption of existing data for explicit user inspection and approval. The user MUST select or approve a suitable local folder or other supported storage arrangement and understand that Current JSON and Folder JSON are always-on parts of the app, then explicitly choose ON or OFF independently for optional Master JSON and Complete On-Site Backup; neither optional choice may be silently preselected. When backup is ON, the user MUST choose a separate validated backup destination, such as an external drive, NAS or other supported folder. The application MAY recommend a suitable location but MUST NOT override the selected workspace root. These choices remain adjustable in Settings → Data Management under the safeguards of [section 53](#s53). Remember the approved location and stable workspace identity, and use it until a deliberate authorized change. The application MUST NOT silently change authoritative location or create a replacement empty workspace when the configured location is unavailable.

<a id="workspace-missing"></a>
#### 45.2.2. Missing location and damaged information

For an unavailable configured location, report **“Data location not found.”** Provide understandable reconnection steps and verify the candidate workspace's stable identity and contents before adoption. Distinguish missing/unreachable location, revoked permission, and damaged information; diagnostics must not claim corruption merely because access failed. For detected damage, report **“Data integrity issue detected.”** and investigate the mandatory Current JSON recovery source under [JSON-4](#json-4), checking its verified revision and genuine availability. Consider optional verified Master JSON and external backup only when actually present; never assume a stale, incomplete or absent representation can restore the requested bytes.

<a id="workspace-movement"></a>
#### 45.2.3. Verified movement and rebinding

Movement between folders, drives, devices, NAS, and supported cloud arrangements MUST have documented and verified migration/reconnection procedures. Prefer relative internal references with an explicit base; stable record identities MUST survive physical folder/name changes. A user MAY point the application to a relocated workspace; before adopting it, validate its identity, actual files, mandatory Current JSON and Folder JSON verification states, permissions and schema, then reconcile pending/concurrent changes. Rebuild only a representation or manifest that is demonstrably absent, stale or invalid; do not regenerate everything merely because the path changed. Document rollback and incomplete movement without silently declaring success. Respect [PORT-2](#port-2), [MIGRATE-1](#migrate-1), and [SYNC-4](#sync-4).

<a id="workspace-3"></a>
### 45.3. WORKSPACE-3 — Three architectures and meaningful folder contracts

**Type:** ECOSYSTEM POLICY | **Origin:** USER POLICY | **Applies:** substantial application planning, with workspace detail required for persistent-data applications

<a id="workspace-three-architectures"></a>
#### 45.3.1. Workspace, planning, and implementation responsibilities

Planning MUST separately assess and validate **A: User Data Workspace**, **B: Master Plan**, and **C: Codebase**, including cross-references and distinct ownership/responsibilities. If no user information is retained, document A as inapplicable. Master Plan retains [BLUEPRINT-1](#blueprint-1)'s Languages and Data, complete specification, Research and Decisions, Design, Reviews, Project State and sequential phases/subphases. Codebase retains feature-first frontend, backend, database and genuine shared responsibilities. `Codebase/Database/` schemas/migrations are development artifacts, not actual user data by default.

<a id="workspace-folder-contract"></a>
#### 45.3.2. Per-folder and per-file design contract

For substantial persistent-data applications, the data hierarchy MUST be explicitly designed, explained, challenged and validated before plan approval. An attractive tree alone is insufficient. Use extensive meaningful headings/subheadings without arbitrary heading limits. Each meaningful folder/file or documented homogeneous class MUST establish purpose, ownership, contents, format, naming, relationships, dependencies, authority/replica/projection/historical-evidence role, rebuildability, discovery, human reading, AI reading, permitted modification, change detection, corruption detection, recovery, relocation behavior, access controls, and retention. Class-level contracts must resolve every actual member's role; they cannot hide exceptional authoritative content.

Do not create customary or empty folders without a demonstrated responsibility. Validate the hierarchy through [WORKSPACE-TEST-1](#workspace-test-1), and keep the complete intended specification and its technical records consistent under [BLUEPRINT-2](#blueprint-2).

<a id="workspace-4"></a>
### 45.4. WORKSPACE-4 — Human and machine entry documents

**Type:** ECOSYSTEM POLICY | **Origin:** USER POLICY | **Applies:** substantial retained-data workspaces and their independent discovery/recovery interfaces

<a id="workspace-entry-pattern"></a>
#### 45.4.1. Five discoverable entry responsibilities

The preferred human-facing filesystem entry pattern is the following four primary information documents, mandatory per-file Current JSON recovery files and verified per-folder Folder JSON manifests, plus a complete global recovery representation **only when Master JSON is enabled**. Physical adaptations MUST map all applicable responsibilities. Disabling Master JSON does not disable originals, per-file recovery or folder verification.

| Entry | Required responsibility |
|---|---|
| `00-START-HERE.md` | Plain-English, non-programmer guidance: what this workspace contains, where to begin, major folders, finding information, and recovery when the original application no longer exists. |
| `01-FOLDER-GUIDE.md` | Complete directory architecture, purposes, relationships, identity/navigation conventions and concrete examples; link each meaningful folder/file contract. |
| `02-DATA-DICTIONARY.md` | Actual formats, fields, relationships, IDs, provenance, timestamp meaning, schema/revision versions, encodings and recovery concepts/dependencies. |
| `catalog.json` | Validated navigable catalog resolving stable records to current logical locations through bounded machine retrieval; explicit authority, update/consistency policy, validation and reconstruction procedure. |
| `*.current.json` | **Mandatory** separate complete literal reconstructible payload per retained original file or justified equivalent persistent logical object. Actual names are App Plan-defined. |
| `folder.json` | **Mandatory** verified folder inventory, location, identity, expected revision/hash, relationships and verification state; no original-file payload duplication. |
| `master-data.json` | **Optional Master JSON ON:** one complete independent literal global recovery payload. OFF does not silently delete a previously verified representation. |

<a id="workspace-bootstrap"></a>
#### 45.4.2. Independent bootstrap and protected discovery

Documentation and recovery schemas MUST remain obtainable and usable without the original application or AI Skill. Catalog reconstruction and recovery discovery MUST not depend circularly on an intact catalog or global JSON: document bootstrap procedures using surviving individual records, protected history or independent recovery dependencies as appropriate. Routine AI retrieval uses bounded catalog/index interfaces, not full scans; authorized deterministic reconstruction may scan with declared costs. Private metadata and credentials remain protected under [AUTH-1](#auth-1), [PRIV-1](#priv-1) and [SEC-2](#sec-2).

<a id="s46"></a>
## 46. Mandatory Current JSON and Folder JSON; optional complete Master JSON

Every qualifying application MUST maintain per-file Current JSONs containing complete literal reconstructible bytes and verified per-folder lightweight Folder JSON manifests. Neither protection may be disabled. Synchronization of a changed Current JSON begins promptly for that file only; Folder JSON is asynchronously verified against a consistent revision boundary. The complete standalone global `master-data.json` remains independently optional under [section 53](#s53). These obligations exclude stateless utilities, do not eliminate original files, do not duplicate file payloads in folder manifests, and do not select a universal operational database.

<a id="json-1"></a>
### 46.1. JSON-1 — Complete Current JSON payloads, verified Folder JSON manifests, and optional global payload

**Type:** ECOSYSTEM POLICY | **Origin:** USER POLICY | **Applies:** mandatory live per-file Current JSON and per-folder Folder JSON for retained-data applications; independently optional global Master JSON

<a id="json-scope"></a>
#### 46.1.1. Complete logical scope and partial replicas

Each applicable retained original file MUST have its own self-contained **Current JSON** containing the actual complete reconstructible original bytes; where physical files are not the relevant unit, an App Plan MAY justify an equivalent independent persistent logical-object scope. Current JSON is mandatory and non-disableable. Each applicable folder MUST have a verified **Folder JSON** manifest of stable file identities, paths, revisions, integrity state and child-folder relationships; it MUST NOT duplicate original-file bytes or claim standalone payload reconstruction. **Only when optional Master JSON is enabled, `master-data.json` MUST independently contain the complete literal reconstructible payload of the retained global workspace at its published verified revision.** Scope inventories MUST account for every retained component without gaps, including workspace-level components outside domain records. Partial device working copies do not redefine the logical workspace or excuse mandatory Current JSON and Folder JSON or an enabled complete global representation. Current, Folder and enabled Master JSON belong **inside the primary workspace**, never only in the external backup location. No layer may claim a newer revision verified before its actual safe publication; placement/coordination follow [JSON-4](#json-4).

<a id="json-literal-payload"></a>
#### 46.1.2. Actual payloads and accessible originals

Literal full duplication is required in every mandatory Current JSON and every enabled global Master JSON: retain actual payloads, including reversible binary-to-text encoding such as Base64 where needed. Paths, hashes, object-store references, diffs, or content-addressed pointers alone MUST NOT substitute for complete payloads. Git-inspired identification supplements full contents. Original audio, images, documents, Markdown and other normal files MUST remain independently available under [WORKSPACE-1](#workspace-1).

<a id="json-exact-bytes"></a>
#### 46.1.3. Exact original bytes and portable metadata

Current JSON and any enabled Master JSON MUST preserve exact retained original file bytes, including text encoding, line endings and binary content, and required metadata, identifiers, relationships and meaning. For user-created or imported JSON originals, parsing and reserializing can change whitespace, escaping, member order, number spelling/precision, BOM, encoding or line endings. Preserve a reversible original-byte representation separately from any parsed interpretation; canonicalization alone cannot reconstruct arbitrary original JSON bytes. JSON parse equivalence or a successfully opened restored file alone is insufficient. Define byte encoding/decoding, lengths, integrity checks, format/schema versions and safe interpretation, including binary-text alphabet, padding and invalid-input handling. Define parser duplicate-member, numeric-precision, depth, string/token-size and resource-limit behavior without silent truncation of accepted retained content. Required platform metadata not reproducible on a target MUST remain preserved in a documented representation and its restoration limits disclosed; do not claim unsupported exact native metadata restoration.

<a id="json-stream-compression"></a>
#### 46.1.4. Bounded streaming and optional Current JSON compression

Current JSON generation MUST support bounded streaming for very large retained files where applicable; streaming does not remove the need to publish a complete, independently reconstructible payload. Implementations MAY automatically apply lossless compression inside a Current JSON representation when measured savings justify its resource and recovery costs. Any compression metadata MUST be explicit, versioned and reversibly decoded, and the original source-file bytes MUST remain unchanged and exactly reconstructible. Do not compress or rewrite source files merely to reduce Current JSON size. Compression is optional, never a reason to omit payload bytes. No filesystem-specific clone, reflink or block-copy mechanism is universally required; a platform-specific API MAY be used where justified and verified under the actual platform contract.

<a id="json-2"></a>
### 46.2. JSON-2 — Payload schema, coverage, privacy, and no diminution

**Type:** ECOSYSTEM POLICY | **Origin:** USER POLICY | **Applies:** individual and global JSON schemas and retained-content lifecycle

<a id="json-schema"></a>
#### 46.2.1. Payload and application information

Use well-defined versioned schemas conceptually separating **`actual_data`**, retained original content and information necessary for exact reconstruction, from **`app_data`**, application metadata and relationships. Important retained information remains covered even when operational or labeled metadata. Each scope inventory MUST classify original documents/media, transcripts, notes, metadata, settings, file-path records, relationships, IDs, user edits, relevant histories/logs and necessary recovery information. Derived indexes and transient processing artifacts require explicit authority, retention and rebuild contracts; neither filename nor derived origin makes authoritative information disposable.

<a id="json-retention"></a>
#### 46.2.2. No silent loss and legitimate erasure

“No diminution” means no silent loss, omission, truncation, corruption, unapproved replacement or premature deletion of required retained information. It does **not** mean monotonically increasing physical file size. Authorized erasure, lawful retention expiry, compact serialization and deliberate validated migrations remain supported. Coverage applies to information legitimately retained at the declared recovery point; [PRIV-1](#priv-1) and [SAFE-2](#safe-2) govern deletion, minimization and conflicting obligations across originals, mandatory Current JSON and Folder JSON, optional Master JSON, histories, replicas and backups. Restoration MUST reconcile deletion decisions and MUST NOT resurrect erased payloads contrary to policy.

<a id="json-secrets"></a>
#### 46.2.3. Privacy, credentials, and recovery keys

JSON completeness MUST NOT expose credentials or bypass access boundaries. Do not store usable credentials insecurely in ordinary readable JSON. Define protected credential/key storage and independently recoverable key-access paths under [SEC-2](#sec-2) and [BACKUP-1](#backup-1). Where sensitive retained content requires encryption, complete recoverable payloads remain required in protected form; document algorithms/formats and legitimate independent access dependencies without packaging decryption secrets with public copies. A credential reference is not a substitute for retained media/document payloads. Report unrecoverability honestly if required keys are unavailable.

<a id="json-3"></a>
### 46.3. JSON-3 — Finite serialization and reconstruction boundaries

**Type:** ECOSYSTEM POLICY | **Origin:** USER POLICY | **Applies:** JSON self-reference, generated envelopes, and historical recovery packaging

<a id="json-generated-envelopes"></a>
#### 46.3.1. Finite generated-envelope reconstruction

The App Plan MUST define a mathematically finite serialization and reconstruction policy. Mandatory Current JSON and optional global Master JSON representations MUST be reproducible from their defined payload, schema and documented deterministic envelope rules without recursively embedding exact copies of themselves. Folder JSON manifests likewise MUST avoid recursive inclusion of generated envelopes. Define which recovery envelopes are reconstructed, what their byte/semantic reconstruction target is, and preserve any non-derivable retained information they carry. Exact original-file reconstruction under [JSON-1](#json-1) remains mandatory; a serialization boundary cannot discard ordinary retained user content.

<a id="json-finite-history"></a>
#### 46.3.2. Retained history and packaging boundaries

Any enabled current global representation MUST NOT recursively embed itself, unbounded historical snapshots containing themselves, or recursively nested temporary transaction machinery. Folder JSON child relationships use bounded references to separately verified child manifests rather than recursively embedding their contents. Distinguish retained user/domain history and necessary recovery information, which remain covered, from separately protected snapshot generations and reconstructible recovery packaging. Document each exclusion's reconstruction or independent retention/access contract, keys/readers and failure limits; exclude only the recursive/generated or genuinely transient packaging, not user data hidden inside it. All still-retained historical user payloads and history/log information belong in the individual/component and global literal coverage inventory; a separate protected generation or history pointer alone does not satisfy that current coverage. A packaging exclusion cannot remove these payloads. Temporary staging is not an ordinary retained original, but any pending user information or operation evidence needed for the declared durable recovery point requires an explicit preservation and reconstruction contract. Historical points themselves MUST have finite, complete declared recovery scopes and accessible dependencies. Reference chains with missing content are not complete recovery payloads.

<a id="json-hash-domain"></a>
#### 46.3.3. Self-hashes and deterministic serialization

Hash domains MUST be explicit and reproducibly verifiable, including how self-generated digest fields and revision identifiers are treated. Do not presume a field can contain the digest of the entire finalized byte string including that same field. Payload-only or explicitly excluded-field domains are examples to evaluate, not a selected universal mechanism. Deterministic envelope serialization must include all necessary version/metadata inputs when exact generated-envelope bytes are promised; semantic reconstruction must be labeled separately.

This rule requires coherent finite boundaries and evidence, not a selected universal serialization, staging, commit or history algorithm. Decisions remain under [section 50.2](#open-engineering).

<a id="json-4"></a>
### 46.4. JSON-4 — Current/Folder revision coordination, distributed state, and verified restoration

**Type:** ECOSYSTEM POLICY | **Origin:** USER POLICY | **Applies:** saving, synchronization, conflict resolution, and restoration of retained-data workspaces

<a id="json-commit-evidence"></a>
#### 46.4.1. Committed revision and legitimate authority

The App Plan MUST define valid committed original-data revisions and durable edit protection, how mandatory per-file Current JSONs and their Folder JSON verification evidence relate to those revisions, and—when Master JSON is enabled—how its independent complete global revision relates to the originals, catalog and recovery sources. Current JSON is a first-class recovery source. Folder JSON is a verified inventory, NOT an independent full-content recovery source. Conflicting states MUST NOT independently claim incompatible authority. A newer timestamp, matching hash, syntactically valid JSON or equal copies alone does not establish legitimacy, factual correctness or successful commit. Use enforced authority, current-state coordination and validation under [AUTH-1](#auth-1), [CON-1](#con-1), [STORE-1](#store-1), [AUDIT-2](#audit-2) and [OUT-1](#out-1).

<a id="json-reconciliation"></a>
#### 46.4.2. Continuous checking and evidenced reconciliation

Integrity checking and reconciliation MUST have documented schedules and trust/commit boundaries appropriate to the supported workload. Mandatory Current JSON synchronization MUST be triggered immediately for a recognized changed original file or equivalent durable object and MUST NOT routinely rewrite untouched files. An asynchronous, resource-bounded Folder JSON verifier checks the relevant original and Current JSON at a consistent revision boundary and then publishes the affected folder's verified state. An enabled global Master JSON follows its independently configured schedule. Bounded periodic reconciliation and validation at appropriate trust boundaries MUST detect missed watcher events; no constant whole-workspace rescan is required. The authorized, tested reconciliation procedure MUST compare relevant current records/revisions, detect mismatches, determine the last verified common state where establishable, examine durable operation evidence, distinguish committed changes from incomplete updates, preserve disputed versions when necessary and lawful, prevent automatic propagation of unvalidated corruption, verify the resulting representations, and record the actual outcome. If common state or legitimacy cannot be established, report uncertainty and preserve safe evidence; do not invent a winner or perform unrestricted mutual overwriting.

<a id="json-pending"></a>
#### 46.4.3. Pending states and unresolved saving decisions

Saving/acknowledgement timing, staging format, write protocol and universal authoritative-copy topology remain unresolved. An App Plan MUST resolve material choices through research and applicable owner authority before affected production implementation under [DEV-5](#dev-5). Do not infer permission either for early pending-state acknowledgement or a universal wait-for-both-copies policy. Honest statuses MUST describe the actual durable original-data point and separate individual/global JSON pending/incomplete/unknown states; no incomplete JSON may masquerade as a complete committed recovery representation. Mandatory Current JSON MUST eventually match a durably committed source revision or visibly remain pending/failed while preserving the last verified representation; it has no OFF switch. Folder JSON MUST retain its last verified published state while a successor is Pending Verification or Conflict Detected, without misrepresenting older verification as covering newer contents. Optional Master JSON must remain fully reconstructible when ON; when OFF the application must not fabricate a fresh global recovery representation.

<a id="json-distribution"></a>
#### 46.4.4. Multi-device and storage-provider boundaries

For supported laptop, phone, desktop/mobile, NAS, selected cloud or multi-device configurations, define write coordination, working copies, revision IDs, synchronization boundaries, offline operations, conflicts, delayed updates, connection/permission failures, recovery and movement between configurations. Preserve the enabled NAS hub policy under [SYNC-3](#sync-3) without treating it as final universal copy authority. Do not assume a shared physical writable filesystem works everywhere, ordinary cloud-folder sync atomically publishes huge JSON, or independent devices may edit a live SQLite/WAL database on unsupported network filesystems.

<a id="json-restore"></a>
#### 46.4.5. Failure scenarios and safe restoration

Recovery procedures MUST distinguish missing original files; corrupted individual/global/both current JSONs **where they exist**; valid-but-semantically-wrong copies; disagreement; interrupted writes; disk exhaustion; moved/unavailable storage; external edits; multi-record AI mistakes; app disappearance; and missing decryption keys. Select and validate an evidenced recovery point, preserve recoverable damaged originals before potentially destructive restoration, and never overwrite the only surviving damaged source merely for convenience. Offer supported same-location or separately selected restoration destinations with understandable consequences; use isolated validation where appropriate. Verify restored bytes, metadata, relationships, IDs and declared recovery point before adoption. Restored paths and symlinks MUST NOT escape the selected destination or overwrite unrelated/unapproved files. Detect absolute-path/traversal escapes, reserved names, case/Unicode collisions and target permission differences; preserve original names and required unsupported metadata through documented reversible mappings or report the unsupported restoration, rather than silently merging distinct files. Apply safe path confinement, symlink/traversal handling, collision/name mapping and current authorization under [IO-1](#io-1), [PORT-2](#port-2) and [RECOVER-1](#recover-1). If no surviving authorized source/key/dependency supports recovery, report the limitation without invented data or false guarantees.

<a id="s47"></a>
## 47. Revision integrity, external edits, and protected history

<a id="rev-1"></a>
### 47.1. REV-1 — Git-inspired content and revision evidence

**Type:** ECOSYSTEM POLICY | **Origin:** USER POLICY | **Applies:** retained-data workspace change tracking and external modification reconciliation

<a id="revision-records"></a>
#### 47.1.1. Revision and change evidence

Use stable revision identities, cryptographic content hashes, content comparisons, change manifests, structured differences where meaningful, recorded timestamps and previous-version relationships, content provenance and links to protected immutable verified history. Evaluate chunk-level hashing where useful for large content. Relevant change records MUST capture record identity, previous/new revision, affected fields/files, measured change size, recorded time and temporal context, old/new hashes, authorized operation identity where established, outcome, historical-content relationships and validation status where applicable. Unknown actors or times remain unknown; [DATA-5](#data-5), [AUDIT-1](#audit-1) and [EVID-1](#evid-1) govern evidence and retention.

<a id="revision-hash-limits"></a>
#### 47.1.2. What hashes establish

Hashes identify/compare bytes against expected values; they neither store recoverable payloads nor prove authorship, time, legitimacy or factual correctness. Hashes/diffs MUST supplement rather than replace mandatory literal Current JSON or any enabled complete global Master JSON. Folder JSON hashes and inventories are integrity evidence, NOT another copy of file contents. Integrity against malicious rewriting requires the protected references/threat assumptions of [AUDIT-3](#audit-3).

<a id="revision-detection"></a>
#### 47.1.3. External changes and detection latency

External changes by editors, other programs, AI filesystem writes, cloud sync or NAS clients MUST be promptly flagged where supported. Define expected identities/revisions, watcher monitoring where available, hash/version verification, rescan/reconciliation and clear user-visible discrepancies. Watchers may miss events; the application may be stopped; remote changes may not yet have propagated. Mandatory integrity reconciliation at relevant trust/commit boundaries MUST precede destructive overwrite or authoritative adoption, coupled to transitions under [CON-1](#con-1); do not promise instantaneous detection everywhere.

<a id="revision-adoption"></a>
#### 47.1.4. Legitimate edits and safe adoption

An external edit is not automatically malicious. Preserve its version within legitimate retention/privacy limits, compare with verified state, and provide safe authorized adoption, rejection or preserved alternatives. An older Current JSON or Master JSON MUST NOT silently overwrite the changed original, and unvalidated external bytes MUST NOT blindly propagate into mandatory Current JSONs, published Folder JSONs or optional Master JSON/external backups. Report unresolved conflicts and containment through [EDIT-1](#edit-1), [EDIT-2](#edit-2) and [SYNC-1](#sync-1).

<a id="rev-2"></a>
### 47.2. REV-2 — Protected earlier revisions beyond current duplication

**Type:** ECOSYSTEM POLICY | **Origin:** USER POLICY | **Applies:** historical recovery protection for retained-user-data workspaces

<a id="history-failure-domains"></a>
#### 47.2.1. Independent historical recovery points

Every qualifying application MUST support separately protected historical recovery capabilities, including the optional complete external backup facility in [section 53](#s53). Actual independent complete backup retention is an explicit user-selected workspace policy (OFF, Single Backup, or Two Backups); the application MUST NOT claim independent historical recoverability when the user disables it. Equal original and Current JSON bytes cannot undo an incorrect edit propagated to both; Folder JSON supplies manifest evidence, not a third payload copy, and Single Backup may eliminate prior good points after rotation. The design and setup disclosure MUST address AI mistakes, deletion, incorrect transcript/user edits, corrupted JSON, synchronization errors, malicious changes, overwrites and storage failures, with actual declared failure domains, retention, residual risk and platform capabilities. Existing historical evidence is not erased by toggling OFF.

<a id="history-deletion-authority"></a>
#### 47.2.2. Deletion authority and finite retention

Where protected backup/history generations exist, normal application and AI editing credentials SHOULD NOT automatically have unrestricted deletion authority over all generations. Define meaningful separation of normal mutation and historical deletion authority, protected content/revision verification, recovery dependencies and actual residual risk under [BACKUP-1](#backup-1). Immutable verified history means protected recorded revisions under the declared threat/retention model, not perpetual retention, proof of factual correctness or immunity to root compromise. Authorized erasure/expiry remains enforceable under [PRIV-1](#priv-1), including prevention of forbidden resurrection. Finite enabled-JSON snapshot scope follows [JSON-3](#json-3); full external backups have independent finite capture/retention boundaries. No recovery guarantee survives destruction of all independent copies, required keys and dependencies.

Version history is distinct from the optional Complete On-Site Backup and MUST remain available under its declared contract when external backup is OFF. Each workspace owner selects the history retention period; optional presets are permitted, but no one fixed universal period is imposed. A same-drive history does not protect against total loss of that drive. Under storage pressure, prune the oldest ordinary versions eligible under the selected policy first and warn before pruning earlier than the user's selected retention. Do not prune mandatory Current JSON, Folder JSON's last verified state, pinned/unresolved evidence, or the sole verified recoverable copy merely to save space. Keep pinned evidence and the sole recoverable copy protected beyond ordinary retention as applicable, subject to authorized permanent deletion and lawful erasure.

<a id="s48"></a>
## 48. Trusted AI entry and bounded navigation

<a id="workspace-ai-1"></a>
### 48.1. WORKSPACE-AI-1 — One discoverable primary application Skill

**Type:** ECOSYSTEM POLICY | **Origin:** USER POLICY | **Applies:** AI-accessible applications with retained-user-data workspaces

<a id="ai-entry-contract"></a>
#### 48.1.1. Primary Skill navigation and operation contract

Expose one clearly named discoverable primary trusted application Skill, for example `Menemora/SKILL.md`. It MUST explain application purpose, approved workspace location/discovery, entry point, folders, record discovery, bounded retrieval, schema/revision interpretation, edit requests, source-data versus instruction boundaries, approval requirements, enforced permissions, error/ambiguity handling, change verification, objects never directly modified, and reporting of uncertain/blocked outcomes. It MAY route to justified bounded subordinate Skills/documentation; one primary entry does not prohibit specialized expertise.

<a id="ai-entry-trust"></a>
#### 48.1.2. Trusted registration and enforced permissions

Trust and invocation MUST follow [SKILL-1](#skill-1)–[SKILL-3](#skill-3). An editable workspace file, including a file named SKILL.md, cannot authenticate itself or elevate authority. Trusted registration/revision and enforced permission boundaries remain separate from its text. AI application operations MUST use approved permission-enforced application interfaces; the Skill alone grants no direct filesystem mutation, credential access, deletion, production or other elevated authority. Existing separately delegated coding/scratch capabilities remain scoped under [AI-1](#ai-1) and do not bypass runtime data protections. Human workspace documentation MUST remain usable without the Skill.

<a id="workspace-ai-2"></a>
### 48.2. WORKSPACE-AI-2 — Measurable one-billion-parameter navigation target

**Type:** ECOSYSTEM POLICY | **Origin:** USER POLICY | **Applies:** AI workspace navigation design and material small-model capability claims

<a id="ai-navigation-route"></a>
#### 48.2.1. Bounded retrieval route

Design for appropriately scoped data navigation by a suitably capable model around **1 billion parameters**. The preferred route is **AI → trusted application Skill → 00-START-HERE.md → folder guide and catalog → bounded retrieval operation → relevant record and precise content**. Supply clear entry points, stable IDs, readable names, bounded indexes/catalogs, precise sub-object addresses, deterministic lookup, limited outputs, ambiguity reporting, enforced authorization, task-specific examples and documented errors. A model MUST NOT need to read the complete global JSON, massive database or thousands of files merely to retrieve one ordinary record.

<a id="ai-navigation-evidence"></a>
#### 48.2.2. Actual evaluation and separate development target

Material capability claims MUST identify model/version and available parameter/quantization evidence, environment/tools/context limits, representative tasks and actual evaluation. Measure retrieval accuracy, errors, hallucinated paths, unauthorized mutations, context budget and correct escalation. Record passed/failed/unrun results and limits; parameter count alone proves no capability. Preserve [HERMES-2](#hermes-2)'s local constrained-model testing and [EXEC-6](#exec-6)'s separate approximately 4B code-execution target. Navigating data and implementing an application are distinct evaluations.

<a id="s49"></a>
## 49. Workspace validation and lifetime feasibility

<a id="workspace-test-1"></a>
### 49.1. WORKSPACE-TEST-1 — Navigation, restoration, and aggressive failure trials

**Type:** ECOSYSTEM POLICY | **Origin:** USER POLICY | **Applies:** design and implementation verification of retained-data workspaces

<a id="workspace-design-trials"></a>
#### 49.1.1. Design simulations and implemented scenarios

Plans MUST simulate, then implementations MUST verify representative scenarios: human and small-AI record location; understanding folders without the app; moving the entire workspace; restoring a deleted original; corrupt individual JSON; corrupt global JSON; external modification detection; application-disappearance recovery; large-dataset navigation; interrupted/conflicting NAS/cloud changes; and restoration to another selected location. Mark design-time simulation separately from actual implementation testing; a plan is not demonstrated recovery.

<a id="workspace-fault-trials"></a>
#### 49.1.2. Failure battery and acceptance criteria

Define demanding documented acceptance criteria and appropriate fault injection, crashes, disk-full conditions, malformed/truncated JSON, missing originals, concurrent writes, interrupted commits, power-loss assumptions, NAS/cloud disconnection, remote conflicts, destructive AI mistakes, large media, lifetime-scale datasets, failed migrations, app-disappearance recovery, small-model navigation, memory/CPU, startup/search performance, and backup/restore checks. Include valid-but-wrong JSON and propagated mistakes, not only parse failures. Verify authorization, privacy/deletion, keys, recovery-point truth and no-fallback boundaries alongside successful reconstruction.

<a id="workspace-test-safety"></a>
#### 49.1.3. Isolated fixtures and finite repair

Use isolated fixtures and authorized test environments; never deliberately damage live user data. Test, repair, retest and repeat until the documented quality baseline is met or a material unresolved limitation is accurately reported. A compilation or happy-path demo alone is insufficient. Testing is finite and risk-based, with actual outcomes under [TEST-1](#test-1); it does not prove absence of all future defects or waive [EXEC-3](#exec-3)'s bounded repair/escalation contract.

<a id="workspace-test-2"></a>
### 49.2. WORKSPACE-TEST-2 — Literal JSON capacity and feasible workload

**Type:** ECOSYSTEM POLICY | **Origin:** USER POLICY | **Applies:** workload planning and performance claims for literal dual-JSON storage

<a id="workspace-workload"></a>
#### 49.2.1. Workload and lifetime costs

Evaluate capacity, storage amplification, temporary write space, write frequency, serialization time, crash consistency, memory, backup growth, cloud upload/transfer cost, NAS bandwidth, mobile constraints, concurrent access and lifetime growth under [DEV-16](#dev-16). State assumptions and measured or estimated evidence, including workload and target-platform limits. A small edit may require producing a new complete global JSON representation; hashing alone cannot remove the payload requirement.

<a id="workspace-storage-math"></a>
#### 49.2.2. Logical storage amplification

For illustration, 100 GB of binary originals plus approximately 133 GB of Base64 payloads in individual JSON and 133 GB in global JSON totals about **366 GB** before other overhead, temporary generations and history. This is approximate logical storage accounting, not a measured universal physical requirement. For binary lengths nᵢ, N = Σnᵢ and B = Σ(4 × ceil(nᵢ/3)), originals plus two single-encoded layers require approximately N + 2B; for large inputs this approaches 11N/3, so 100 decimal GB is approximately 366.7 GB. The rounded 366 GB illustration assumes each layer encodes each original payload once. Encoding an already encoded individual JSON envelope again inside the global layer adds expansion; separately encoded chunks add padding/framing. The actual schema must account for these costs rather than assume this estimate universally. Git uses separately stored content objects and references, unlike one literal complete JSON payload.

<a id="workspace-streaming"></a>
#### 49.2.3. Peak resources and streaming limits

Memory estimates MUST include the largest parser/encoder token and buffers: streaming records does not bound memory if an enormous Base64 string is allocated at once. Measure or bound peak disk while prior valid state and staging coexist, total bytes written/transferred, CPU, latency and growth; bounded memory does not remove total serialization, validation or I/O costs.

<a id="workspace-optimization"></a>
#### 49.2.4. Measured optimizations and material conflicts

Bounded streaming for applicable very large Current JSON payloads is required under [JSON-1](#json-1), and lossless compression inside Current JSON is permitted only under the versioning, reversibility and exact-source-byte conditions there. Other optimizations—such as copy-on-write, snapshots, sparse files or reflinks—MAY be evaluated within the eventual approved design, but their portability, actual savings, crash behavior and recovery dependencies require evidence; no filesystem-specific optimization is universally required. None excuses complete payloads. If literal duplication cannot meet the agreed workload, present the material conflict honestly to the owner and resolve affected planning under [GOV-3](#gov-3) and [DEV-5](#dev-5); do not silently replace payloads with pointers, invent capacity, hide loss or implement a fallback.

<a id="s50"></a>
## 50. Menemora illustration and Open Engineering Decisions — non-normative

This section preserves the owner's organizational example and explicitly unfinished decisions. It is not an implemented filesystem, universal feature list, approved saving algorithm, or additional normative rule set. The obligations governing applicable applications are in sections 45–49 and the retained foundation.

<a id="menemora-blueprint"></a>
### 50.1. Approved illustrative Menemora workspace

Menemora, a voice recording and transcription application, supplied the owner's concrete design context. The following is the exact illustrative hierarchy from the mission. Domain folder names do not become mandatory in unrelated applications.

```text
Menemora/
│
├── 00-START-HERE.md
├── 01-FOLDER-GUIDE.md
├── 02-DATA-DICTIONARY.md
├── catalog.json
├── master-data.json
│
├── Recordings/
│   └── 2026/
│       └── October/
│           └── Interview_A7F2/
│               ├── recording.json
│               ├── recording.m4a
│               ├── transcript.md
│               ├── Notes/
│               │   └── notes.md
│               └── History/
│                   └── changes.json
│
└── Settings/
    ├── settings.json
    │
    ├── File-Paths/
    │   └── file-paths.json
    │
    ├── Exports/
    │
    └── System/
        ├── system.json
        │
        ├── Search-Index/
        │   └── search-index.json
        │
        ├── Integrity/
        │   └── integrity-manifest.json
        │
        ├── Logs/
        │   └── operations-001.json
        │
        └── Recovery/
            ├── recovery-state.json
            ├── Transactions/
            └── Verified-History/
```

<a id="menemora-records"></a>
#### 50.1.1. Recording-local information and identity

The recording folder demonstrates the WORKSPACE-3/INFO-3 relationship contract: its original audio, applicable transcript, notes, metadata and history are discoverable together. The owner's Menemora design keeps each recording's associated information discoverable from that recording's folder, rather than placing every recording's notes in an unrelated global Notes folder. `Interview_A7F2` illustrates a readable label with an identity cue; it does not prescribe a universal identifier algorithm. `recording.json` supplies full scoped recovery data under JSON-1, not merely paths to the audio and text beside it.

<a id="menemora-settings"></a>
#### 50.1.2. Settings and support responsibilities

In this illustration Settings contains settings, file-path configuration, exports, system support, search indexes, integrity, logs and recovery information. Under WORKSPACE-3/JSON-2 each receives its own purpose, authority and retention/rebuild classification. A search index is disposable only when its declared dependencies support rebuilding; retained settings, histories, relationships and meaningful logs remain recoverable. An integrity manifest is evidence for a defined trust model, not missing-file payload. Transactions and Verified-History require JSON-3's finite packaging boundaries and REV-2's independent protection: placing history in this folder alone supplies no access isolation or independent failure domain. An export's intended scope/lifecycle is explicit; its filename does not make it authoritative. Ordinary readable settings JSON is not an acceptable insecure credential store.

<a id="menemora-collections"></a>
#### 50.1.3. Optional Collections and feature scope

The owner leaves Collections optional and enableable/disableable through Settings. Disabling the feature does not itself authorize erasing existing collection information; deletion follows the existing authority/retention contract. A permanent root Collections folder is not required. The future App Plan selects metadata, references or justified folders, without unnecessarily duplicating original media for organizational views. This is distinct from required full JSON recovery duplication.

Transcription, transcript correction, AI summaries, audio processing, notes and other capabilities remain subject to Menemora's future App Plan. The example does not automatically authorize or require every suggested capability, implementation or access to a Menemora repository. A primary trusted Skill under WORKSPACE-AI-1 is separately discoverable; its omission from this exact illustrative tree does not waive that applicable contract or make editable workspace instructions authoritative.

<a id="open-engineering"></a>
### 50.2. Open Engineering Decisions

**Historical RC4 engineering context (superseded in the newer candidate only):** Topic 1's physical transaction protocol remains unfinished. The historical ratified RC4 revision must be read at its original commit, not inferred from this updated working document. The owner's newer locked candidate requires always-active complete per-file Current JSON and verified per-folder Folder JSON, while global Master JSON and external complete backup remain optional under [section 53](#s53). Other goals remain Git-inspired revision evidence, safe coordination, truthful acknowledgement, no silent data diminution and no hidden fallback. Some implementation questions remain open below; decisions settled by the newer owner-approved candidate are identified as settled there and must not be reintroduced as unresolved policy choices. This table is non-normative and does not authorize deploying an unfinished mechanism.

| Open choice | Evidence and decision still needed |
|---|---|
| Acknowledgement timing | Priority is settled: make the original-file change durable before treating secondary Current JSON or Folder JSON work as complete, and report each layer separately. Exact physical ordering, acknowledgement boundary, crash-safe transaction and close behavior still require per-platform engineering evidence. |
| Durable staging and commit format | Format, publication ordering, reader visibility, interruption handling and retained operation evidence across originals, mandatory Current JSON, verified Folder JSON, optional global Master JSON, catalog and history. A successful rename or database commit alone does not settle cross-artifact durability. |
| Write coordination protocol | Writer authority, stale-writer exclusion, concurrent/offline changes, conflict handling and evidence of valid committed revisions on actual supported backends. |
| Efficient enormous global updates | A complete-payload generation/update approach with measured lifetime I/O, memory, CPU, latency, temporary space and failure behavior. No references-only substitution is approved. |
| JSON and filesystem optimization | Bounded streaming is required for applicable very large Current JSON payloads. Lossless compression is permitted only inside Current JSON when worthwhile, with versioned reversible metadata and exact source-byte preservation. No filesystem clone/reflink is universally required. Workload thresholds, measured gains, snapshot methods and platform-specific recovery behavior remain to be established. |
| Device/NAS/cloud synchronization authority | One physical root per managed workspace on each device is settled. Cross-device synchronization ordering, write authority, local working-copy topology and NAS/cloud conflict handling still require an App Plan grounded in the supported backend; the candidate does not require every device to retain every logical-workspace byte. |
| Rebuild, batching, compaction and capacity thresholds | Workload-specific thresholds, trigger behavior, retention preservation, resource accounting, incomplete-generation treatment and acceptance criteria. No numeric defaults are invented. |
| Universal timeout/retry budgets | Backend/workload timing, cancellation, uncertain outcomes, safe retries and measurable limits. The same-operation/replay safeguards remain active without a newly invented universal budget. |
| History retention implementation | The workspace owner selects the retention period; no fixed universal period or generation count is required. Physical protection, pruning eligibility, capacity, independent access, lawful erasure and finite recovery boundaries need app-specific design and evidence. |
| PIN-loss and security-question recovery | Optional workspace encryption and per-workspace key design are stated in SEC-7. The precise supplemental role of security questions and complete PIN-loss fallback flow remain deferred for owner discussion; no question-based key reconstruction is approved. |

Material decisions return to the future research and authorized App Plan decision process under DEV-5/DEV-8/GOV-3 before affected implementation. Engineering choices already within delegated authority need no repeated request; unresolved owner policy cannot be inferred from an example. These open questions do not weaken mandatory per-file literal payload obligations or enabled optional global payload obligations. Research, prototypes and estimates remain evidence with stated limits, not approval or demonstrated production guarantees.

<a id="s51"></a>
## 51. RC4 authority, reconciliation, and requirement coverage — non-normative

<a id="rc4-authority"></a>
### 51.1. Current owner mission, dates, and scope

The owner supplied **“GPT-6 ASTRA — UNIVERSAL RULES RC4: DATA WORKSPACE, DUAL-JSON RECOVERY, AND FOLDER ARCHITECTURE INTEGRATION.”** Authoring began 2026-10-17 UTC and resumed 2026-10-18 UTC after interruption. The resumed editor remains the Green author role, with no independent Red credit. Received raw mission SHA-256: `1eceaa424788fe210d7933a2e2b87893ec217b74403d85e9cd958f7e16e51b6b`. This digest identifies received bytes; it is not a signature or independent authentication of a person.

The mission expressly authorizes repository integration, research, structural verification, fresh exact-candidate adversarial review, substantiated repair and re-review, commit/push, and safe non-destructive publication. It directs a new integration branch from verified main and preserving the rc3 target and historical refs. Together with the existing operating procedure, its instruction to review the exact new candidate delegates identifying/freezing that candidate for the requested review sequence; it supplies no authority for unrelated redesign, bypassing repository protections or rewriting history. It forbids application implementation, building Menemora, executing untrusted Skills, inventing unresolved decisions and weakening existing protections. **The owner has not authorized ratification.** Publication remains subject to the actual checks, evidence and limits of section 42.

<a id="rc4-baseline"></a>
### 51.2. Verified baseline and historical preservation

The baseline is `main` at **`73b2e8adb0236af7d4e503e67f9d507148cc95b7`**, designation **1.0.0-rc3 — Single-file integration candidate — NOT RATIFIED**. Its sole tracked file is `MASTER_PLAN.md`, SHA-256 **`07a0976686215cb68e4a0bf63d56aecfb9ec183e7946f84d4855f103fa110460`**, with 137 unique rules, 44 substantive numbered sections, 201 explicit anchors, 709 resolving internal links, all 113 original rule IDs and 33 Skill families. Baseline remote refs were reverified on 2026-10-18 UTC before completing this integration; the `work` branch was behind main, not an unintegrated successor.

Preserved historical refs are `constitution/pre-ratification-working`, `constitution/single-file-integration-2026-10-14`, `review-history/universal-rules-convergence`, and `review-history/single-file-integration-2026-10-14`. Their actual identities and recoverability belong in the external verification receipts; no historical ref is repurposed as the RC4 target. The rc3 clean rounds certify only their stated rc3 bytes and provide no review credit for RC4. Section 43 retains the earlier history and former-file mapping as historical evidence. New review outcomes belong outside frozen normative bytes.

The RC4 integration branch is `constitution/data-workspace-rc4-2026-10-17`. Exact final commit, digest, tree and subsequent review/publication results are recorded externally under section 42, avoiding self-referential commit/digest claims or predicted successful reviews in this candidate.

<a id="rc4-preservation"></a>
### 51.3. Rule preservation and explicit amendment ledger

All **137 rc3 IDs, titles, Type, Origin and Applies metadata fields** are retained. No stable ID is retired. The **14 new USER POLICY rules** bring the inventory to **151**, still CANDIDATE under GOV-1. All 33 Skill families and the complete previous security, data, planning, technology, design, execution and review protections remain governing. The precise baseline diff and structural evidence accompany the candidate receipt; this author ledger is a review aid, not proof of semantic correctness.

| Existing rule refined | Explicit RC4 change and retained boundary |
|---|---|
| [GOV-1](#gov-1) | Route new normative sections 45–49 and informative 50–51; preserve classifications, applicability, conflict handling and owner authority. |
| [LIFE-3](#life-3) | Clarify that executable/data colocation cannot make disposable installation state the only retained copy; retain existing lifecycle freedoms within preservation contracts. |
| [INFO-1](#info-1) | Explicitly replace format-neutral sufficiency for retained-user-data scope with accessible workspace and literal individual/global JSON; retain appropriate operational stores and domain hierarchy choice. |
| [INFO-2](#info-2) | Map logical discovery freedom to preferred human-facing entry documents and physical adaptations; preserve permission and private-metadata boundaries. |
| [INFO-3](#info-3) | Clarify required recovery duplication is distinct from avoidable duplication for organizational views; preserve stable identity and relationship semantics. |
| [SURVIVE-1](#survive-1) | Expressly strengthen former no-universal-format wording within retained-data scope; retain independent preservation, dependencies, recovery-point truth and stateless proportionality. |
| [SYNC-3](#sync-3) | Preserve enabled-NAS primary synchronization hub while distinguishing undecided universal copy authority/placement and partial working copies. |
| [NOFALL-2](#nofall-2) | Identify both JSONs as complementary recovery sources; preserve honest failure, restoration, local operation, retries and prohibition of hidden substitutes. |
| [BLUEPRINT-2](#blueprint-2) | Require three distinct architecture assessments and current specification coverage; retain complete planning, supporting technical records and feature-first code. |
| [GOV-4](#gov-4) | Record current RC4 integration authority separately from historical rc3 authority; preserve exact freeze, read-only review, repair scope, independent rounds, safe publication and owner-only ratification. |

<a id="rc4-new-rules"></a>
#### 51.3.1. Fourteen added rule identities

| Rule family | New stable rules and responsibilities |
|---|---|
| Workspace | [WORKSPACE-1](#workspace-1) independent durable access; [WORKSPACE-2](#workspace-2) selected location/movement; [WORKSPACE-3](#workspace-3) three architectures/folder contracts; [WORKSPACE-4](#workspace-4) entry documents/bootstrap. |
| Literal recovery | [JSON-1](#json-1) complete payloads/exact bytes; [JSON-2](#json-2) schema/retention/privacy; [JSON-3](#json-3) finite envelopes/history/hash domains; [JSON-4](#json-4) committed revisions/reconciliation/topology/restoration. |
| Revisions | [REV-1](#rev-1) content/change evidence and external edits; [REV-2](#rev-2) protected historical recovery. |
| AI workspace access | [WORKSPACE-AI-1](#workspace-ai-1) trusted primary Skill; [WORKSPACE-AI-2](#workspace-ai-2) measurable bounded 1B navigation. |
| Verification and scale | [WORKSPACE-TEST-1](#workspace-test-1) design simulations and actual break-testing; [WORKSPACE-TEST-2](#workspace-test-2) lifetime capacity and honest feasibility. |

<a id="rc4-interactions"></a>
#### 51.3.2. Preserved interaction contracts

| Existing families | Reconciliation with the added policy |
|---|---|
| INFO-1–4, LIFE-1–3, SURVIVE-1–2 | Literal payload/access strengthens format freedom only in stated retained-data scope. Stable identity, precise addressing, lifecycle separation, actual mobile survival and independent interpretation persist. |
| DATA-1–5, STORE-1–2, CON-1–2 | Authority, factual correctness and byte identity remain distinct. Exact original payloads supplement provenance/temporal/locale semantics. Mechanisms still follow supported storage and concurrency contracts; no universal saving algorithm follows from duplication. |
| OUT-1, OPS-1, AUDIT-1–3, RETRY-1 | Honest pending/committed/unknown outcomes, recoverably linked evidence, verified hash domains and safe retries persist without deciding the unfinished acknowledgement policy. |
| EDIT-1–2, SYNC-1–4, NAS-1–2, OFFLINE-1–3 | User edits remain legitimate; adoption remains validated. Continuous checking does not promise instant remote observation. One logical workspace and a complete global representation coexist with declared partial local working copies and existing enabled-NAS hub policy. |
| RECOVER-1–2, BACKUP-1–2 | Both current JSONs supplement protected historical recovery. Preserve damaged sources, verify exact recovery points/dependencies, handle later valid work, and never treat matching current copies or immutable history as proof of correctness. |
| PRIV-1–2, SAFE-2, SEC-1–2, IO-1–3, MIGRATE-1–2 | Complete legitimate retained scope does not demand permanent erased data, leaked credentials or public access. Restoration preserves authorization and safe paths; migration/intake validation, privacy, lawful erasure and key boundaries remain active. |
| AUTH-1–2, AI-1–4, HERMES-1–3, SKILL-1–4 | One primary Skill routes to permitted operations but supplies no extra authority. Workspace content is data until independently trusted; native/core enforcement, bounded retrieval, optional AI and all 33 workflow families remain. |
| NOFALL-1–2 | Dual representations are required recovery responsibilities; stale JSON, pending evidence or recovery mode cannot be presented as substitute successful normal saving. |
| PLAN-1–2, BLUEPRINT-1–3, DOC-1–2, EXEC-1–6, DEV-1–18 | Preserve ordered requirements/research/technology/design planning, feature-first code, complete Master Plan, beginner-readable documentation, 33-field phases, bounded repairs and separate 4B implementation evaluation. 1B navigation is an additional product-use target. |
| GOV-3–5, section 42 | Retain actual authority, one-file active tree, exact-candidate freeze, read-only Red, validated Green Fix, fresh review after repairs, two independent clean rounds for convergence and separate owner ratification. |

<a id="rc4-coverage"></a>
### 51.4. Full owner-requirement coverage map

The source identifiers below refer to the numbered RC4 mission, not competing constitutional sections. Classification describes the baseline disposition; the destination states the implemented policy or applicable operating procedure. Process rows record required work, not a claim that future reviews or publication already succeeded.

| Mission requirement | Baseline disposition | Current destination and coverage |
|---|---|---|
| 0 Role, repository integration, delegation, no application build, no untrusted Skills, no invented guarantees or ratification | Already satisfied / Requires clarification | [51.1](#rc4-authority): Authorized integration scope; no application implementation, untrusted Skill execution, invented approval or ratification. |
| 1 Exact checkpoint, branch/tree/137-rule inventory and historical refs | Already satisfied operationally; reverify | [51.2](#rc4-baseline): Exact rc3 baseline, metadata counts, historical refs and remote verification; unexpected movement is reconciled under 42.2. |
| 2 One-file active constitution; separate immutable historical evidence; new branch; safe publish | Already satisfied | [42.7](#procedure-publish): Only MASTER_PLAN.md on the active tree; new branch, preserved history, non-destructive publication and verified remote outcome. |
| 3 Preserve full foundation and stable IDs, no weakened obligations, coverage | Requires clarification | [51.3](#rc4-preservation): 137 prior IDs/metadata and 33 Skill families preserved;14new rules; explicit amendment and interaction ledger. |
| 4 Durable information is product; discoverable independent workspace, real folders preferred, no opaque substitute; eight priorities; persistent-data scope | Contains a material conflict / Requires refinement | [WORKSPACE-1](#workspace-1): Information as durable product, independently accessible workspace, real-folder preference, eight planning priorities and stateless scope. |
| 5 Setup selection/approval, persistent approved location and stable identity | Requires new rule | [WORKSPACE-2](#workspace-2): Approved setup location, persistent identity and deliberate location changes. |
| 5.1 Missing location | Requires refinement | [45.2.2](#workspace-missing): Data location not found; no empty replacement; verified reconnection. |
| 5.2 Move | Requires clarification | [45.2.3](#workspace-movement): Supported movement/rebinding, relative references, stable identity and verified migration. |
| 5.3 Corruption | Requires refinement | [46.4.5](#json-restore): Data integrity issue detected; preserved damaged source, chosen safe destination and verified restoration. |
| 5.4 Real mobile/provider behavior | Already satisfied / Requires clarification | [45.1.2](#workspace-survival): Real phone/provider access and uninstall survival, with SURVIVE-2 evidence and no arbitrary-filesystem promise. |
| 6 Folder design as product responsibility; every meaningful artifact's 19 listed properties; headings and justified folders | Requires new rule | [45.3.2](#workspace-folder-contract): Per-artifact purpose/ownership/content/format/naming/relationships/dependencies/role/rebuild/discovery/human-AI reading/writes/detection/recovery/movement/access/retention; meaningful headings and justified folders. |
| 6.1 Three architectures and cross-references | Requires refinement | [45.3.1](#workspace-three-architectures): User Data Workspace, Master Plan and Codebase assessed separately with cross-references; existing blueprint retained. |
| 6.2 Twelve design simulations then implementation verification | Requires new rule | [49.1.1](#workspace-design-trials): All twelve navigation, movement, corruption, external-edit, disappearance, scale, NAS/cloud and selected-restore scenarios; simulation distinguished from tests. |
| 7 Five root entry objects and mapped adaptation | Contains a material conflict / Requires refinement | [WORKSPACE-4](#workspace-4): Five preferred entry objects with explicit technically necessary mappings and preserved independent outcomes. |
| 7.1 Start | Requires new rule | [45.4.1](#workspace-entry-pattern): Plain-English non-programmer start and disappearance guidance. |
| 7.2 Folder guide | Requires new rule | [45.4.1](#workspace-entry-pattern): Complete folder purposes, relationships, identity, navigation and examples. |
| 7.3 Data dictionary | Requires new rule | [45.4.1](#workspace-entry-pattern): Actual fields/formats, relationships, IDs, provenance, time, version and recovery dictionary. |
| 7.4 Catalog | Requires new rule | [45.4.2](#workspace-bootstrap): Validated bounded catalog with explicit authority/update/reconstruction and independent bootstrap. |
| 7.5 Global JSON | Requires new rule | [JSON-1](#json-1): Complete global JSON contents, never a hash/pointer catalog. |
| 8 Menemora exact illustrative tree | Requires new example | [50.1](#menemora-blueprint): Exact organizational tree; illustrative Menemora scope only. |
| 8.1 Record-local discoverability | Requires clarification | [50.1.1](#menemora-records): Recording-local discovery of originals, transcript, notes, metadata and history. |
| 8.2 Settings support hierarchy and credentials | Requires clarification | [50.1.2](#menemora-settings): Settings support hierarchy, explicit preservation/rebuild classifications and protected credentials. |
| 8.3 Collections optional | Requires example clarification | [50.1.3](#menemora-collections): Optional Collections, settings switch without implicit erasure, no forced root folder or media duplication for views. |
| 8.4 Future media/AI capabilities | Already satisfied / example clarification | [50.1.3](#menemora-collections): Suggested transcription/AI/processing/notes features await the future App Plan. |
| 9 Both first-class complete JSON layers per retained logical record/scoped component and one entire workspace | Requires new rule / material conflict | [JSON-1](#json-1): Self-contained component records and one entire logical-workspace global JSON; first-class complete payloads. |
| 9.1 Accessible originals persist | Requires refinement | [46.1.2](#json-literal-payload): Ordinary original files remain independently available. |
| 9.2 Exact literal reconstruction incl binary | Requires new rule | [46.1.3](#json-exact-bytes): Exact original bytes, including original JSON, reversible binary encoding and metadata; pointers/hashes insufficient. |
| 9.3 actual_data/app_data | Requires new rule | [46.2.1](#json-schema): Versioned actual_data/app_data schema; important operational metadata remains retained. |
| 9.4 Coverage and derived/transient contracts | Requires refinement | [46.2.1](#json-schema): All specified retained content classes, including settings/path records/history/logs/recovery, with explicit derived/transient classification. |
| 9.5 Finite self-reference and history/staging | Requires new rule / Deferred mechanism | [JSON-3](#json-3): Finite reproducible generated envelopes, explicit selfhash domains, retained historical payload coverage and bounded packaging. |
| 9.6 Never diminish vs physical size/erasure | Requires clarification | [46.2.2](#json-retention): No silent information loss; authorized erasure, lawful expiry, compaction and deliberate migration remain possible. |
| 10 Git-inspired IDs/hashes/diffs/history | Requires refinement | [REV-1](#rev-1): Revision IDs, hashes, comparisons, manifests/diffs, time, previous relationships, protected history and optional chunk hashing. |
| 10.1 Hash truth | Already satisfied / clarify | [47.1.2](#revision-hash-limits): Hashes verify relative byte identity; no payload, authorship/time or factual truth implied. |
| 10.2 Payload completeness despite tracking | Requires new rule | [46.1.2](#json-literal-payload): Hashes/diffs supplement both literal complete recovery layers. |
| 10.3 Change record details | Requires refinement | [47.1.1](#revision-records): Identity, prior/new revision, changed fields/files and measured size, temporal context, hashes, operation/outcome/history links and validation. |
| 11 Ten-stage reconciliation | Requires new rule | [46.4.2](#json-reconciliation): All ten comparison/common-state/durable-evidence/commit/conflict/validation/outcome principles; no unrestricted mutual overwrite. |
| 12 Protected independent history | Requires refinement | [REV-2](#rev-2): Independent protected earlier recovery points, ordinary credential limits, failure domains, finite scope, privacy and no impossible recovery promise. |
| 13 External modification detection and boundaries | Requires refinement | [47.1.3](#revision-detection): Prompt supported detection of external edits, identities/versions/watchers/rescans and mandatory trust/commit reconciliation. |
| 13.1 Prompt not instantaneous detection | Requires clarification | [47.1.3](#revision-detection): No instant detection guarantee; missed events/stopped apps/delayed remote propagation and hash attribution limits. |
| 13.2 Legitimate external edits | Already satisfied / strengthen | [47.1.4](#revision-adoption): Legitimate external edits preserved and compared, safe adoption/rejection, no stale overwrite or blind propagation. |
| 14 One trusted application entry Skill | Requires new rule | [WORKSPACE-AI-1](#workspace-ai-1): One discoverable trusted primary Skill with all navigation/edit/approval/permission/error/verification topics; subordinate Skills allowed and enforced interfaces mandatory. |
| 15 1B navigation path/metrics vs 4B implementation | Requires refinement | [WORKSPACE-AI-2](#workspace-ai-2): 1B route, bounded deterministic lookup/precise addressing, examples/errors and actual measured navigation evidence; separate 4B execution target. |
| 16 Laptop/phone/desktop/mobile/NAS/cloud/multi-device | Requires clarification / Deferred engineering choice | [46.4.4](#json-distribution): Supported laptop/phone/desktop/NAS/cloud/multi-device contracts; explicit working copies/offline/conflicts/failures/moves and undecided universal authority topology. |
| 17 Fourteen recovery scenarios and exact fidelity | Requires new rule | [46.4.5](#json-restore): All fourteen corruption/loss/interruption/movement/AI/key/disappearance scenarios; selected restoration and verified bytes/metadata/relationships/IDs/recovery point. |
| 18 Demanding finite break testing | Requires refinement | [WORKSPACE-TEST-1](#workspace-test-1): Demanding documented failure battery, isolated fixtures, finite repair/retest and truthful outcomes; no live-data damage or specification-as-test. |
| 19 Literal costs and no silent optimization substitution | Requires new rule + research evidence | [WORKSPACE-TEST-2](#workspace-test-2): Literal storage amplification assumptions, whole-global costs, peak resources/lifetime scale, evidence for optimizations and material workload conflicts. |
| 20 Settled invariants and unfinished Topic 1 | Deferred engineering choice | [50.2](#open-engineering): All nine unresolved Topic1 choices explicitly deferred; no selected algorithm/topology/threshold/budget/retention policy. |
| 21 Constitutional reconciliation | Requires refinement | [51.3.2](#rc4-interactions): Every named family reconciled; explicit INFO/SURVIVE strengthening, privacy/security boundaries and stateless proportionality. |
| 22.1 Verify | Already satisfied process; execute | [42.2](#procedure-freeze): Verify baseline refs/bytes/inventory and historical evidence before candidate construction. |
| 22.2 Coverage | Requires current evidence | [51.4](#rc4-coverage): This final map links every numbered policy/process requirement to actual text and records baseline classification. |
| 22.3 Research | Requires current evidence | [51.5](#rc4-research): Primary-source storage/JSON/Git/filesystem/mobile/NAS/cloud research with limitations. |
| 22.4 Integrate | Requires current execution | [51.3](#rc4-preservation): Single-file edits, 14 new rules and explicit existing amendments, navigable headings and examples. |
| 22.5 Structural | Requires current execution | [42.2](#procedure-freeze): Required structural/preservation/link/tree/fence/numbering/coverage/provenance/history/Git checks; exact results in external receipt. |
| 22.6 Adversarial | Requires current execution | [42.3](#procedure-red): Fresh exact-target read-only A–P plus 18 RC4 attack topics; substantiated Green Fix/re-review and convergence reset. |
| 22.7 Publish | Requires current execution | [42.7](#procedure-publish): Authorized commit/push and safe promotion, preserved refs, independent final remote verification; blocked gates reported honestly. |
| 22.8 Final report | Requires current evidence | [51.6](#rc4-evidence-status): Final report covers all 17 requested outcome,identity,coverage,evidence,risks and owner-decision items. |
| 23 Final constraints | Requires end-to-end validation | [51.1](#rc4-authority): All settled policies integrated; no app build, invented decisions, hidden substitution, lost protection, second constitution, ephemeral-only publication claim or ratification. |

<a id="rc4-research"></a>
### 51.5. Technical research and limits — 2026-10-17 UTC

The following primary sources were independently retrieved during the RC4 read-only technical investigation on 2026-10-17 UTC. These are documentation findings and mathematical reasoning, not application implementation, platform durability tests, 1B trials or measured benchmarks. No untrusted Skills were installed or executed. The full research record is preserved with the external integration evidence; all active obligations are stated within this constitution.

| Primary source | Findings and policy implications | Limits |
|---|---|---|
| [RFC 8259, JSON](https://www.rfc-editor.org/rfc/rfc8259), December 2017, §§2,4,6–9 | JSON permits insignificant whitespace and alternative string escapes; object ordering is not portable semantics. Duplicate names have unpredictable interoperability. Numeric precision and parser size/depth/string limits require explicit contracts. Network interchange uses UTF-8. Preserve original bytes separately from parsed interpretations when exact reconstruction is promised. | JSON validity alone establishes neither semantic correctness nor byte identity. A conforming parser can impose resource limits. |
| [RFC 8785, JCS](https://www.rfc-editor.org/rfc/rfc8785), June 2020, §§3.1–3.2 and Appendix D | Canonical serialization can provide deterministic bytes for a defined data model, with constraints on strings and numbers. Its worked example explicitly shows numeric rounding and changed serialized spellings. | Canonicalization does not recover arbitrary original JSON bytes. Do not prescribe JCS universally without deciding numeric/schema requirements. |
| [RFC 4648, Base64](https://www.rfc-editor.org/rfc/rfc4648), October 2006, §§3–4 | Base64 represents octets using four characters per three input bytes with final padding. Define alphabet, padding, line handling and rejection rules. Exact unwrapped padded length is `4*ceil(n/3)`. | Base64 is reversible encoding, not encryption or compression. Encoded text still needs framing, validated length and integrity checks. |
| [Git internals: Git objects](https://git-scm.com/book/en/v2/Git-Internals-Git-Objects), retrieved edition | Git stores actual content objects; names identify those objects. Trees describe names/relationships and commits preserve revision context. A content hash alone cannot regenerate absent content. | The chapter's SHA-1 examples do not require RC4 to adopt SHA-1 or Git's exact storage format. Git-inspired identity/history does not turn references-only JSON into literal recovery. |
| [Linux rename(2)](https://man7.org/linux/man-pages/man2/rename.2.html) | Supported rename replacement changes a destination name atomically; cross-mount rename can fail. | Atomic name replacement is not a complete durable transaction over originals, record JSON, global JSON, catalogs, history and operation evidence. Linux behavior is not a universal mobile/cloud guarantee. |
| [Linux fsync(2)](https://man7.org/linux/man-pages/man2/fsync.2.html) | File flushing does not necessarily flush its containing directory entry; directory synchronization is a separate consideration. Failure returns must be handled. | Flush guarantees depend on the actual storage stack honoring its contract. Do not present a call sequence as proven power-loss safety on every platform. |
| [SQLite atomic commit](https://www.sqlite.org/atomiccommit.html) | Journaling, synchronization ordering and storage assumptions support transaction guarantees; the document explicitly discusses broken flush implementations and crash testing. | SQLite transactions do not automatically atomically include external JSON/media files. SQLite's implementation is evidence for required reasoning, not an approved RC4 saving algorithm. |
| [SQLite WAL](https://www.sqlite.org/wal.html) | Standard WAL requires processes on the same host for shared coordination; direct independent-host access over a network filesystem is unsupported. | A NAS service owning its local SQLite file is a different topology. No universal topology is selected by this evidence. |
| [Android storage overview](https://developer.android.com/training/data-storage), page shows updated 2026-10-16 UTC | App-specific internal and external storage, preferences and local databases are removed on uninstall; shared media/documents have different survival characteristics. | “External” does not mean independent or permanent. Survival of selected provider, access and keys needs actual platform testing. |
| [Android Storage Access Framework](https://developer.android.com/training/data-storage/shared/documents-files) | User-mediated document access can retain URI grants across restarts. Providers expose supported operations. Moving or deleting a document can invalidate access despite a persisted grant. | A URI is not necessarily a POSIX filesystem path; not all provider operations or directories are available. Persisted permission is not indefinite access or backup. |
| [Apple storage management](https://support.apple.com/en-us/108429), [remove/delete apps](https://support.apple.com/guide/iphone/remove-or-delete-apps-iph248b543ca/ios) | Offloading preserves documents/data while deletion removes app-related local data. Separately stored iCloud data can remain when the app is deleted. | Test deletion, not only offload; account/service/key dependence and independently usable formats remain. |
| [Apple File System Basics](https://developer.apple.com/library/archive/documentation/FileManagement/Conceptual/FileSystemProgrammingGuide/FileSystemOverview/FileSystemOverview.html), archived developer guide | App containers and sandbox restrictions distinguish local app storage from independent documents. | This is archived documentation; do not use its old platform/UI wording as an exhaustive current API contract. |
| [Amazon S3 consistency model](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html#ConsistencyModel) | S3 documents strong read-after-write consistency and atomic updates to one key, while stating that atomic updates across keys are not supplied. | This is a provider-specific object API, not ordinary synced folders or all clouds. Even strong single-object consistency does not establish workspace transaction atomicity. |
| [Linux inotify(7)](https://man7.org/linux/man-pages/man7/inotify.7.html), limitations/caveats | Event queues can overflow; directory watches are not recursive; remote network-filesystem changes are not captured; event metadata does not identify the responsible user/process. | Watchers alone cannot prove no external edits occurred. Planned verification/rescans are ordinary supported integrity behavior and need not constitute a prohibited fallback implementation. |

<a id="rc4-research-interpretation"></a>
#### 51.5.1. Consequences supported by the evidence

JSON validity is neither exact original-byte preservation nor semantic correctness. Canonical JSON serialization has a defined data-model scope and cannot recover arbitrary original spellings or bytes. Reversible encoding supplies actual payload; Base64 adds size and supplies no encryption. Finite generated envelopes need explicit serialization inputs and hash domains, while retained user history remains literal content. Hashes verify a comparison against an expected reference and require protected references for adversarial integrity claims; Git retains actual content objects as well as identifiers.

Namespace atomic replacement, durable storage, multi-artifact consistency, distributed coordination and truthful acknowledgement are distinct properties. Filesystem flushing depends on the complete storage stack; SQLite transactions do not automatically encompass external JSON/media; provider-specific one-object consistency does not supply a transaction across a workspace. These facts motivate a full supported contract and tests, without choosing the unfinished saving algorithm.

Mobile app-specific storage and keys may disappear on deletion; a persisted document grant, cloud account or exposed folder name does not guarantee permanent independent recovery. The selected configuration needs app-disappearance evidence. Watchers can miss external changes and cannot establish authorship; mandatory reconciliation at trust boundaries remains necessary. Originals plus two once-encoded payload layers approach 11/3 of original binary volume before metadata/history/staging; actual nested schemas, chunk padding and largest-token memory can materially increase costs. Streaming does not remove total write/transfer work. Optimizations and workload feasibility need platform-specific evidence.

<a id="rc4-evidence-status"></a>
### 51.6. Candidate evidence status and final reporting boundary

This document states policy and provenance. It does not certify an application, prove successful restoration, report unrun tests as passed, or predict an exact future commit. The revision-bound report records actual baseline/remote verification, rule/metadata/33 Skill preservation, additions/modifications, complete coverage, structural/factuality checks, git/history verification, exact Red rounds and dispositions, and independent publication retrieval. RC3 reviews and the Green author's own checks cannot satisfy RC4 independent review.

The final mission report provides all 17 requested items: executive outcome; repository/branch status; exact final commit; document SHA-256; final tree; original rule counts; added/modified rules; full coverage matrix; research findings; reconciled contradictions; explicit deferred decisions; structural results; Red results; historical preservation; residual risks; NOT RATIFIED status; and the owner's next action. Review and publication failures/unrun work remain explicit. Any ratification request is a separate exact-revision decision after the evidence is available, never inferred from this candidate's publication.

<a id="s52"></a>
## 52. Historical Topic 2: Optional Dual-JSON Recovery and Complete On-Site Backup — superseded design record

**Status:** Historical post-RC4 design record; **NOT RATIFIED**. Its optional Dual-JSON toggle, four-mode table, five-minute individual schedule, and amendment analysis are **superseded by the later owner-locked per-file Current JSON / Folder JSON architecture in [section 53](#s53)**. Read this section only as decision provenance, not as current design instructions. Section 53 is the current integrated **unratified amendment candidate** and controls where the two records differ. This section is not a second amendment or adopted policy, adds no rule to RC4's 151 normative rules, and authorizes no application implementation or data migration. The ratified baseline remains commit `aac66fa5ea1de8579b860f8833725c531317fde2` with `MASTER_PLAN.md` SHA-256 `4796b0f7ba168650cedde615a3382fe475cc64de14784bf6445849ec1a1fb53f`.

This design uses Menemora, a voice-recording and transcription application, as an example. Its folder names illustrate one workspace; they do not authorize moving existing data or impose the same domain folders on other products. Current requirements for the workspace, literal JSON payloads, restoration, history, backup, privacy, and honest outcomes remain in [sections 45–49](#s45), especially [JSON-1 through JSON-4](#json-1), [REV-1 and REV-2](#rev-1), [BACKUP-1 and BACKUP-2](#backup-1), [RECOVER-1](#recover-1), [NOFALL-1 and NOFALL-2](#nofall-1), [PRIV-1](#priv-1), and [AUDIT-2](#audit-2).

<a id="topic2-status"></a>
### 52.1. What the owner has agreed, and what this record does

The proposed product has two separately controlled workspace protections:

1. **Workspace Dual JSON** keeps a complete individual JSON representation for each applicable record or component and a complete global `master-data.json` inside the primary workspace.
2. **Complete On-Site Backup** creates full, standalone physical copies of the declared retained workspace in a separately selected destination.

The owner controls each setting independently. The proposed future constitutional direction is that qualifying applications support the approved Dual-JSON capability while each user may choose whether active Dual-JSON redundancy is enabled for a workspace. External complete backup remains an independent user choice. This policy has not been integrated into or approved as a replacement for RC4.

<a id="topic2-configurations"></a>
#### 52.1.1. Four independent settings combinations

| Workspace Dual JSON | Complete On-Site Backup | Proposed workspace state |
|---|---|---|
| OFF | OFF | Original workspace data, plus any separate protections still required by the governing constitution and application contract. Do not imply that no protection is required. |
| ON | OFF | Original workspace data and its active individual and global JSON representations. No Complete On-Site Backup is being created by this feature. |
| OFF | ON | Original workspace data and independently versioned complete external backups. Do not generate new complete JSON representations merely because backup runs. |
| ON | ON | Original workspace data, active individual and global JSON representations, and complete external backups. |

Turning either setting OFF does not itself authorize deleting data already produced by that feature. The user must be told what is paused, retained, or unavailable. Deletion and retention follow [PRIV-1](#priv-1) and any future approved policy. Pausing, resuming, and separately deleting historical JSON representations remain open decisions.

<a id="topic2-conflict"></a>
#### 52.1.2. Explicit conflict with ratified RC4

RC4 [JSON-1](#json-1), [INFO-1](#info-1), and [SURVIVE-1](#survive-1) currently require accessible retained-workspace data and complete literal individual and global JSON recovery representations for applicable retained-user-data workspaces. Making active Dual JSON optional conflicts with those current requirements. The proposed option cannot silently take effect as current RC4 policy; a future formal amendment must state which clauses change, what protection remains when the option is OFF, and how affected requirements are reconciled.

The term “JSON recovery source” describes a data-recovery representation, not an alternate execution implementation. RC4 [NOFALL-2](#nofall-2) expressly treats its two JSON layers as complementary recovery representations and permits verified restoration. This proposal does not authorize a hidden secondary database or other substitute to satisfy JSON-1, nor a concealed execution path after failure. Operational databases may retain their separately defined responsibilities under existing workspace rules.

The proposed one- or two-version Complete On-Site Backup retention modes also need reconciliation with RC4 [REV-2](#rev-2)'s independent protected historical recovery points and [BACKUP-1](#backup-1)'s failure-domain and deletion-authority protections. A single retained copy, or two copies removable through the same ordinary credentials, cannot be presumed to satisfy those requirements. The future amendment must define whether another mechanism continues to meet RC4 when this feature is OFF or in Single Backup mode; the proposed retention count does not waive existing protection.

<a id="topic2-locations"></a>
### 52.2. Primary workspace, JSON locations, and external destination

The primary workspace remains the location of original user data. When Dual JSON is active, its individual and global recovery representations also remain in that workspace. They are not moved into the external backup destination. A complete external backup copies the declared workspace contents, including whichever JSON files exist at the captured recovery point.

An illustrative Menemora layout is:

    Menemora/
    ├── 00-START-HERE.md
    ├── 01-FOLDER-GUIDE.md
    ├── 02-DATA-DICTIONARY.md
    ├── catalog.json
    ├── master-data.json                 (when Dual JSON is active)
    ├── Recordings/
    │   └── 2026/October/Interview_A7F2/
    │       ├── recording.m4a
    │       ├── recording.json            (when Dual JSON is active)
    │       ├── transcript.md
    │       ├── Notes/notes.md
    │       └── History/changes.json
    └── Settings/
        ├── settings.json
        └── System/
            └── Recovery/
                ├── recovery-state.json
                ├── Transactions/
                └── Incidents/

    Selected external destination/
    └── Menemora/
        ├── Backup-Version-<identity>/
        └── Backup-Version-<previous-identity>/    (Two Backups mode)

The paths, filenames, and physical transaction layout are examples, not finalized storage protocol. Settings, retained histories, recovery evidence, credentials, and derived state each need the scope, access, retention, and recovery treatment required by their purpose. Do not expose credentials in ordinary readable JSON. Any backup exclusions—such as transient caches, incomplete staging, or the backup destination itself—must be explicit, justified, and safe from recursive inclusion.

<a id="topic2-first-run"></a>
### 52.3. First-run setup and ongoing controls

Before initial storage configuration, the application is to show the user the primary workspace location and proposed folder structure; where original data, settings, history, recovery information, and individual/global JSON would reside; any storage outside the selected workspace; whether existing data was detected and may be adopted; and relevant capacity and permission information. It should clearly identify which files are originals and which are recovery representations.

The user separately chooses **Workspace Dual JSON: ON or OFF** and **Complete On-Site Backup: ON or OFF**. Neither is silently selected on the user's behalf during first-time setup. If external backup is enabled, the user selects a supported destination, such as an external SSD, external HDD, NAS share, or another validated folder. The application checks the destination and explains whether it is physically independent from the primary workspace and the failure risks that remain. A different path, drive letter, mount, or NAS label alone does not establish independence.

After setup, both controls remain available through **Settings → Data Management**. Recovery approval and urgent integrity notices may appear in context while configuration remains discoverable there. The precise interface may differ by application; the settings and consequences must remain understandable.

If the application detects an existing workspace, it must distinguish adopting and validating that workspace from creating a new one. It must not silently reorganize files or overwrite an existing workspace during setup.

<a id="topic2-json-init"></a>
### 52.4. Enabling Dual JSON for an existing workspace

If the user enables Dual JSON after the workspace already contains data, the initial complete representation is **Workspace JSON Version 1**. Initialization is complete only after the application has:

1. Inventoried the retained data and declared recovery scope.
2. Validated relevant files, relationships, and the selected workspace identity.
3. Established a logically consistent baseline boundary.
4. Constructed all applicable complete individual JSON representations and the complete global `master-data.json`.
5. Verified the representation contents and their ability to reconstruct the declared retained data.
6. Published the verified baseline as Workspace JSON Version 1 and continued under the selected save policies.

Initialization must not assemble a mixed-time baseline while the application or external programs change files. The physical consistency method and the handling of edits during the build are not settled here. A process start, partial set of JSON files, or syntactically valid output is not a verified Version 1. An interrupted attempt must leave original data protected, report incomplete work, and preserve any safely recoverable evidence. Keep the application usable where doing so is safe.

<a id="topic2-json-scheduling"></a>
### 52.5. Edit protection, JSON schedules, and resource reporting

The agreed saving discussion has three layers, whose exact transaction protocol remains open:

1. **Durable edit protection.** Acknowledged edits need durable protection under the applicable data-safety policy without waiting for a potentially large full JSON rebuild. How this minimum durability works when optional Dual JSON is OFF has not been resolved. The future amendment must reconcile the user toggle with the applicable minimum durability and [OUT-1](#out-1); it must not imply that OFF makes acknowledged edits disposable.
2. **Individual JSON.** When Dual JSON is ON, the discussed user choices are immediate updates, updates every five minutes, or updates when the user becomes idle. These choices apply to individual JSON representations, not automatically to the full global JSON.
3. **Global JSON.** The complete `master-data.json` has its own schedule. Smart/Adaptive is the preferred mode discussed: an eligible update may start when pending changes exist and resource and execution conditions permit. Scheduled and manual updates were also discussed. Each published global JSON must represent a complete verified retained-workspace revision.

Individual JSON and global JSON may have separate resource profiles: **Memory Saver**, **Balanced**, and **Priority**. Values, triggers, fairness, capacity limits, and behavior when resources are unavailable are not selected by this record.

The interface is to distinguish the latest durably recorded edit, individual JSON revision, global JSON revision, pending changes, verification state, resource mode, failures, and recovery requirements. A generic “Saved” indicator must not imply that all layers are current when only an edit or one JSON layer is durable.

No resource-intensive saving or backup job silently continues after the application closes. Any post-close completion worker must be visible and explicitly authorized, then stop when its approved job finishes. No universal post-close execution guarantee is claimed for unsupported operating systems.

<a id="topic2-backup-init"></a>
### 52.6. Complete On-Site Backup and its first verified version

Complete On-Site Backup is separate from Dual JSON. It is user-controlled and has its own destination, schedule, resource policy, version identities, and retention choice. Each completed backup is a full, standalone physical copy of the entire declared retained-workspace scope, browsable as ordinary folders wherever the retained items are ordinary files. It is neither incremental nor a hybrid that requires an earlier backup to reconstruct the declared contents.

The complete scope may include original recordings and other files, transcripts, notes, folder structure, settings, retained histories, relevant manifests and documentation, recovery metadata, individual JSON files if present, the global JSON if present, and every other retained item included in the defined scope. Any exclusions must be documented as described in [section 22](#s22). A manifest or hash may support inventory and verification, but cannot replace missing payload.

Each backup has an identity in a namespace separate from Workspace JSON versions. If backup is enabled for a workspace that already contains years of data, the first successfully verified complete backup is **External Backup Version 1**. Initialization is not complete until both the copied contents and the published recovery point have been verified. A started, partial, inaccessible, or unverified copy is not a completed backup.

The backup process captures a consistent workspace state under a mechanism to be selected and tested for the target platform. It copies the JSON revisions that actually exist at that state and reports any lag or pending changes. A backup run does not silently trigger full regeneration of `master-data.json`. A disconnected drive, unavailable NAS, access denial, or uncertain copy result cannot be reported as success.

<a id="topic2-backup-schedule"></a>
### 52.7. Complete backup schedule

The five discussed frequency choices are **Daily**, **Weekly**, **Smart / Adaptive**, **Manual**, and **Custom**. Daily and weekly express an aim to create a complete backup each day or week; they do not promise execution when the destination, resources, permission, or authorized execution window is unavailable. Smart/Adaptive may start an eligible complete backup when changes, resources, destination availability, and authorized execution conditions permit. Manual runs only on an explicit request. Custom lets the user choose a supported schedule. All modes expose **Back Up Now**.

Backup frequency is independent of both JSON schedules and of retention mode. A missed run is shown as overdue and follows a transparent execution policy; a failed attempt is not a successful cycle. Execution and resource use remain bounded. The exact time zone, retry limits, catch-up behavior, and custom schedule syntax remain open.

<a id="topic2-backup-retention"></a>
### 52.8. Single Backup and Two Backups retention

The two proposed normal retention choices are:

| Mode | Completed versions retained after a successful safe rotation |
|---|---|
| **Single Backup** | The latest successfully verified complete backup. |
| **Two Backups** | The latest successfully verified complete backup and its immediately preceding successfully verified complete backup. |

For example, Two Backups advances from Current V1; then Current V2 / Previous V1; then Current V3 / Previous V2, with V1 retired after V3 is safely published. A failed attempt does not advance rotation.

The replacement must be fully copied, verified, and durably published before an older protected version is retired. Safe construction may temporarily require space for existing completed versions plus the staged candidate: Single Backup may need two physical copies during construction, and Two Backups may need three. The configured limit applies to completed retained versions after successful cleanup, not every staging instant. If capacity is insufficient, stop and report it; do not delete the only verified copy early to make room.

Pause automatic retirement of potentially valuable versions when corruption, unresolved missing files, or significant integrity conflicts have been detected. Show the hold and temporary extra storage clearly. Disclose that undetected corruption can be copied into a newer full backup. Turning backup OFF does not silently remove existing verified backups. Exact crash-safe publication and retirement mechanisms remain unresolved.

<a id="topic2-everyday-recovery"></a>
### 52.9. JSON-first everyday recovery and complete disaster recovery

For ordinary repair when Dual JSON is active, the proposed investigation order is: examine the relevant individual JSON; durable pending changes and revision relationships; the global `master-data.json` as needed; then other verified retained historical sources. Prepare the best-supported candidate. A newest timestamp alone does not establish the correct revision. An older individual JSON must not cause newer valid durable changes to be ignored. If only one file is damaged, repair only that file unless evidence justifies a wider operation.

Detection, investigation, and preparation may be automatic when safely supported. Replacing an existing original requires explicit user approval under [JSON-4](#json-4), [RECOVER-1](#recover-1), and the exact-target safeguards in [section 52.12](#topic2-restoration-safety).

Complete On-Site Backup primarily supports disasters such as loss of the primary drive, severe workspace destruction, large-scale unrecoverable loss, or reconstruction on replacement hardware. The proposed flow validates the selected backup and its versions; shows recovery-point information; lets the user choose a safe destination; avoids silently overwriting an existing workspace; restores the complete retained folder structure; verifies files and dependencies; reestablishes appropriate workspace identity and settings; reports unavailable, missing, or incompatible contents; and records the operation. A physically failed source drive whose original bytes cannot be accessed cannot have those bytes preserved by the software. The external destination protects against that failure only if it survives in a genuinely separate failure domain.

<a id="topic2-selective-compare"></a>
### 52.10. User-requested missing-file comparison

The proposed action is discoverable at **Settings → Data Management → Recovery & Restoration → I Think I'm Missing a File**. It is an explicit, read-only comparison and selective-recovery workflow:

1. Identify the active primary workspace and its stable identity.
2. Ask the user to select the external backup drive or folder, optionally suggesting a previously configured destination.
3. Validate the backup and identify available verified versions. In Two Backups mode, allow comparison with both current and previous versions.
4. Compare the current workspace with the selected version or versions and present a clear report.
5. Let the user inspect differences, choose files, and approve any proposed workspace changes.

Scanning and comparison do not change the workspace or external backup. A missing path can reflect intentional deletion, disconnected storage, revoked permission, or a different workspace; it is not automatically corruption, and an inaccessible workspace must not appear as an empty one.

At minimum, classify items as missing from current workspace, different, present only in current workspace, matching, or uncertain/inaccessible. Identify potential moves or renames only when trustworthy evidence supports that conclusion. Prefer a bounded inventory/manifest comparison using trusted relative paths, stable identities when available, sizes, revision metadata, recorded hashes, backup manifests, and current inventory. Investigate bytes more deeply where needed. Do not reread hundreds of gigabytes when a cheaper comparison can answer the question; manifest agreement alone is not a claim of fresh byte-by-byte verification.

Show missing, different, workspace-only, matching where useful, uncertain items, and the backup versions compared. Each item can be inspected by name, original relative path, current and backup locations, size, available hashes, backup version, relevant revision, available history, verification state, and conflicts. Permit individual selection and safe bulk selection. Treat ambiguous or conflicting items separately.

<a id="topic2-selective-restore"></a>
### 52.11. Selective restoration from a complete backup

The owner-approved design direction permits a user to restore one or more explicitly selected files from a complete backup without restoring the entire workspace. This is an intentional, user-requested path alongside ordinary JSON-first repair. For example, a transcript missing from the current workspace may be inspected in Backup V12 and restored from V12, or from V11 if V12 lacks it. The application never silently chooses an older copy or restores every absent file.

The proposed operation validates the selected version and target relative path; treats the external backup as read-only; stages and verifies the selected content; rechecks destination identity and current state; detects a file that appeared or changed since comparison; seeks renewed approval if the proposal's conditions changed; installs only the approved items; verifies the result; records provenance; and updates relevant recovery metadata and JSON status if Dual JSON is active. A genuinely absent target has no existing target bytes to preserve. If a target exists, treat it as a replacement conflict and apply the exact-byte safeguards below. Do not silently overwrite newer work or modify the backup during comparison or restore.

<a id="topic2-restoration-safety"></a>
### 52.12. Exact-byte preservation and explicit replacement approval

Before replacing an existing original, the proposed procedure identifies the trusted workspace and exact target; inspects current contents and revision information; validates the recovery source; reconstructs the candidate in isolated staging; verifies its bytes and required metadata; checks available capacity; and explains the recovery point, consequences, and conflicts. Approval is bound to the exact target, its observed current state, selected source revision, and proposed replacement bytes. Revalidate immediately before mutation. If the target changed after review or approval, stop and present a new proposal; do not silently overwrite it.

Preserve the original's exact existing bytes before replacement and verify that preservation. Then apply the authorized replacement through a recoverable transaction, verify the active result, record the outcome, and update revision/JSON states truthfully. Restoring an earlier point creates a new recovery revision with provenance; it does not rewrite history to imply the incident never occurred. After JSON-based repair, promptly synchronize the affected individual JSON when Dual JSON is ON using recovery-specific durability safeguards. The global JSON retains its separate schedule. Restoration never silently turns Dual JSON ON.

The proposal accounts for traversal, malicious filenames, symlinks, junctions/reparse points, escapes from the chosen workspace, collisions, destination changes, concurrent external edits, insufficient space, interrupted copy, crashes, partial completion, and failed readback. Do not assume one rename makes a multi-file operation atomic or durable. For multi-file repair, maintain durable per-file and batch transaction state. On partial failure, state exactly what was preserved, changed, verified, or left uncertain, and retain safely recoverable evidence.

For bulk restoration, present a closed list, validate each item, and use one understandable batch approval where appropriate. Exclude ambiguous, unsafe, or changed items; never add files after approval; report partial outcomes; and preserve exact damaged bytes before replacing any approved existing file. Incident archives may hold evidence, provenance, verified identities, hashes, decisions, and failure details. Archive naming must not blindly inherit an untrusted source filename. The illustrative Recovery/Incidents layout in [section 50](#s50) is not a finalized protocol.

<a id="topic2-states"></a>
### 52.13. Disabled, incomplete, and conflicting states

| State | Proposed truthful behavior |
|---|---|
| Dual JSON OFF | Do not assume complete JSON recovery exists. An available external backup may support user-initiated selective restore. Do not silently enable JSON. |
| External backup OFF | JSON recovery may be available if Dual JSON is ON. Do not imply that JSON on the failed primary drive survives physical loss of that drive. |
| Both OFF | Explain recovery limitations while retaining any other protections required by the applicable constitution and product contract. Do not invent a source. |
| JSON Version 1 incomplete | Do not call it verified. Individually verified artifacts may be considered only under a qualified recovery procedure. |
| Backup creation incomplete | Do not publish it as verified; protect the previous verified backups. |
| Requested historical revision unavailable | Say it is unavailable and offer evidenced alternatives without silently substituting another revision. |
| Evidence inadequate or conflicting | Do not automatically replace originals. Offer investigation, safe export, comparison, or restoration to a separate destination where appropriate. |
| Destination unavailable or inaccessible | Report the actual access/connectivity state; do not label the workspace empty or claim a completed backup. |

<a id="topic2-reporting"></a>
### 52.14. Status, integrity, and security limits

Status distinguishes original edit durability; individual and global JSON revision and verification; pending work; selected resource mode; backup schedule and overdue state; selected destination and access; current and previous backup identities; verification and publication state; retirement hold; recovery requirements; and errors or unknown outcomes. “Saved,” “protected,” “verified,” and “recoverable” must describe the specific evidence and boundary they actually establish.

Hashes support byte comparison and accidental-corruption detection when compared with an appropriate expected value. A hash stored beside a compromised file is not independent proof of authenticity, authorship, factual correctness, or clean history. Distinguish byte integrity, revision consistency, authenticity, physical independence, and disaster recovery. NAS or external storage is not independent merely because it has another path. Stronger defenses may need separately protected trust anchors, access control, or immutable protection; those designs are open.

<a id="topic2-open"></a>
### 52.15. Agreed direction versus unresolved decisions

This paragraph records the historical earlier option as originally discussed. The **later owner-locked requirements in section 53** supersede its optional Dual JSON toggle, four configuration descriptions and individual JSON scheduling decisions: Current JSON and lightweight verified Folder JSON are always-on, whereas only complete global Master JSON and external physical backup remain optional. The other safety practices are preserved as historical direction and are governed by their current, separately stated rules in sections 18, 21–22 and 53; this record creates no additional active requirement.

The following choices remain open; this section does not select mechanisms or defaults on the owner's behalf:

| Open decision | Still to be established |
|---|---|
| Durable transaction protocol | Original-before-secondary ordering, journal purpose, per-layer status and safe startup recovery are settled; the physical protocol, durable acknowledgement boundary and operation-evidence format remain open. |
| Consistent snapshots | A due backup during editing must use a supported consistent point-in-time snapshot or defer until editing finishes. Platform-appropriate snapshot and external-writer consistency mechanics remain open. |
| Locking and coordination | External editing is permitted; use brief justified locks and revalidate; preserve conflicting offline versions and merge only demonstrably independent compatible changes. Backend-specific stale-writer exclusion and multi-device coordination remain open. |
| Crash recovery and replay | Inspect pending journal work promptly, prioritize affected files, avoid full rescans, and auto-complete only established safe states. Durable transaction transitions, exact replay/idempotency and safe cleanup after interruption remain open. |
| Approval persistence and invalidation | Approval is bound to exact identities, revisions and hashes; a relevant change invalidates it and requires fresh comparison and approval. Persistence across restart and expiry rules remain open. |
| Incident retention and protected originals | Preserve damaged originals for at least 24 hours after verified recovery, and protect unresolved, pinned and sole-recoverable evidence as required. Exact storage, access separation, capacity and lawful-erasure mechanics remain open under privacy and deletion rules. |
| Verification and trust anchors | Which checks are freshly performed, independent evidence, tamper assumptions, key handling, and what “verified” means by operation. |
| Backup publication and retirement | Crash-safe promotion, catalog updates, cleanup, and proof the replacement is usable before retirement. |
| Insufficient space and interruption | Preflight, safe pause, truthful partial states, preserving recovery data and offering another destination are settled. App-specific margin calculation, staging/cancellation mechanics and recovery under each backend remain open. |
| Damaged storage | Conservatively limit writes, preserve readable evidence, avoid compounding damage and offer safe extraction or an alternate destination where supported. Exact platform-specific detection and behavior when reads fail remain open. |
| First-run validation | Respect the selected workspace root, validate existing workspace identity and avoid an empty substitute. Supported providers, permission/capacity checks and physical-independence validation remain app/platform-specific. |
| Earlier optional-Dual-JSON proposal | Superseded by section 53: mandatory Current JSON and Folder JSON, with only global Master JSON optional. The durable transaction algorithm remains open as stated in section 53.8. |
| Retention and RC4 protection | Single/Two Backup policies and workspace-selected history duration are settled in the candidate. Exact storage/access separation, pruning eligibility, erasure propagation, and interaction with REV-2's independent-protection and BACKUP-1 failure-domain controls still need implementation evidence under sections 18, 21, 22 and 47. |
| Constitutional amendment | Exact future wording, affected rule dispositions, transition behavior, and separate owner ratification process. |
| Adversarial validation | Test cases for hostile paths, races, crashes, power loss, tampering, partial batch operations, and supported platform/storage combinations. |

<a id="topic2-amendment"></a>
### 52.16. Future amendment implications

This subsection records the earlier proposed optional Dual-JSON change and its amendment questions. That proposal has been superseded and is not the current amendment agenda. Section 53 now proposes mandatory per-file Current JSON and Folder JSON, with optional complete Master JSON and separately optional Complete On-Site Backup; the applicable amendment and implementation gates appear in sections 53.8–53.12.

This historical section preserves the earlier post-RC4 design record. It does not edit, renumber, replace, or ratify any RC4 rule; change the existing count of ratified rules; authorize implementation against user data; or resolve any current implementation question. The newer, unratified candidate is in [section 53](#s53); ratification remains a separate owner decision under [GOV-3 through GOV-5](#gov-3).


<a id="s53"></a>
## 53. Owner-locked Current/Folder JSON and cross-application candidate — UNRATIFIED

**Authority boundary:** The owner has LOCKED the universal mandatory Current JSON, verified Folder JSON (Option B), and highlighted selective-diff reconciliation decisions. This section and its edits to earlier rules constitute an **unratified constitutional amendment candidate**, not separate formal ratification. Ratified RC4 continues to govern until separately approved through [GOV-3](#gov-3)–[GOV-5](#gov-5). The ratified source is commit `aac66fa5ea1de8579b860f8833725c531317fde2` and remains unchanged. [Section 52](#s52) is the owner's historical decision record. If this candidate's explicit controls conflict with preexisting language in this candidate, those clauses must be reconciled before ratification rather than treated as silently overridden. No current application, user-data migration, backup deletion, rollout, or source-code implementation is authorized by this document alone.

### 53.1. Owner-locked universal protection policy

Every qualifying application retaining user-owned original files MUST maintain **Current JSON** (one complete independent recoverable JSON per original file or appropriately justified durable logical data object) and a **Folder JSON** (a verified lightweight manifest of file membership, identity, path, revision and relationships for each applicable folder). **These two capabilities are mandatory, permanently ON and not user-disableable.** Current JSON contains literal original bytes; Folder JSON does not duplicate the file bytes. This applies universally to qualifying apps, with Menemora only an example.

Only a complete global **Master JSON** within the primary workspace and a separately located **Complete On-Site Backup** are user-optional, each controlled independently.

| Current JSON | Folder JSON | Optional Master JSON | Optional Complete On-Site Backup | Recovery representation |
|---|---|---|---|---|
| ON (mandatory) | ON (mandatory) | OFF | OFF | Original + complete per-file Current JSON on the primary workspace drive; verified Folder JSON is a manifest, not another copy. No separate drive-loss copy. |
| ON (mandatory) | ON (mandatory) | ON | OFF | Above plus independently reconstructible global Master JSON inside the primary workspace. |
| ON (mandatory) | ON (mandatory) | OFF | ON | Mandatory per-file recovery and manifests plus separately selected full standalone physical backups. |
| ON (mandatory) | ON (mandatory) | ON | ON | All four layers, with independently declared verification, freshness and failure domains. |

Mandatory Current/Folder JSONs cannot be turned OFF, paused as an optional feature or silently deleted by routine cleanup. Optional Master JSON and Complete Backup may each be switched OFF without silently deleting historical retained artifacts; any later deletion requires explicit, applicable authorization and privacy/retention handling. Original-file saving remains appropriately crash-safe and edit durability reporting honest in all four configurations.

### 53.2. First-run Settings and folder visibility

The setup flow MUST display the approved primary workspace path; original data folders; settings, history, catalogs, recovery files and relevant external locations; proposed directory tree; and how an existing user-owned workspace will be adopted, validated or left untouched. It MUST describe mandatory always-on Current JSON and Folder JSON as built-in architecture and explicitly collect ON/OFF choices only for optional Master JSON and Complete On-Site Backup, neither preselected silently. The workspace location and backup destination are different settings. When backup is ON, the user selects and approves a backup folder (for example, an external drive or NAS). The app checks reachability, permissions, space, identity and whether the destination is actually physically independent; another drive letter is not proof of another failure domain. App-internal and temporary storage outside the chosen workspace must be explained when applicable.

Central controls reside in **Settings → Data Management**, with discoverable overview, storage paths, protection switches, schedules, resource controls, backup versions, recovery and background activity. Contextual integrity notices and necessary restoration approvals may appear elsewhere; this does not move the underlying configuration out of Settings. Never silently create an empty substitute workspace because its configured location disappeared.

### 53.3. Mandatory immediate per-file synchronization and verified Folder JSON

The first-time setup or adoption of an existing workspace MUST inventory retained user files, stable identities and declared recovery scopes, validate source data and construct each file's complete Current JSON. Publish each initial verified per-file baseline only after exact-byte reconstruction checks. Create per-folder manifest baselines at an evidenced consistent revision boundary. Incomplete initialization is pending rather than proof of protection; do not disturb existing original bytes. A newly created original file gets its own mandatory Current JSON and properly verified folder membership.

**Immediate synchronization:** a recognized authorized file change MUST promptly initiate or safely queue an update **only for that changed file's Current JSON**. This is a trigger/eligibility requirement, not a guarantee that multi-gigabyte serialization completes instantly or every five seconds. Coalesce rapid edits safely using durable change evidence; do not indefinitely defer a pending current revision, and report verified source/current divergence. Current JSON remains a *complete literal payload* for its scope, never just a delta, pointer, hash or patch. Publish a verified staged successor without damaging the previous verified version or original; skipped, delayed, failed or interrupted writes remain visibly pending/failed.

**Folder verification:** after a relevant Current JSON change, the app queues resource-bounded, visible asynchronous verification for the relevant Folder JSON and any affected ancestor/old-new folder. The verifier examines the actual original, Current JSON, trusted identity/revision evidence and folder relationships at a consistent snapshot boundary. A newly detected edit during checking must not result in a mismatched mixed-time publication. Preserve the **last verified Folder JSON**, mark the new changes **Pending Verification** or **Conflict Detected**, and publish the new manifest only after its declared scope passes verification. Changed files/folders are prioritized; do not routinely scan or rewrite thousands of unrelated entries. Use bounded periodic/trust-boundary reconciliation to handle missed watcher notifications. Folder JSON never duplicates the original payload and alone cannot restore a lost file.

**Optional complete Master JSON** has a separate ON/OFF setting and independently verified **Global Master JSON Version 1** at first enabled successful initialization. It retains its complete standalone workspace-recovery scope, separate **Smart / Adaptive**, scheduled or manual update options, and verified version/freshness evidence. Master JSON is not regenerated wholesale merely to acknowledge a Current JSON update. External Complete On-Site Backup has its own frequency, verification and version namespace.

The UI MUST separately report original edit durability, per-file Current JSON verification/pending state, per-folder verified vs pending/conflict state, and optional global Master JSON freshness and external-backup completion. A generic green "Saved" indicator cannot equate original-save completion with successful verification of every recovery layer. **Automatic Resource Management** is the default. Optional **Memory Saver** and **Priority** modes MAY be offered under Advanced Settings; they can adjust resource use but cannot disable required protection or correctness. No undisclosed post-close verification or saving process; allow finish-before-close, expressly approved visible worker or safe resume later **only when pending data has appropriate durable protection and the user understands the risk**. Crash-safe original commits, journal protocol, staging, cancellation and cross-file atomicity remain target-platform implementation gates.

### 53.4. Complete On-Site Backup — full copies, schedules and versions

A Complete On-Site Backup is a **complete standalone physical workspace copy** in the user's separately selected destination, preserving ordinary files/folders for direct browsing and independent restoration. It is **not incremental, differential or hybrid**, and it never requires prior backup versions to reconstruct a published version. It covers all declared retained original files and associated settings, metadata, documentation, histories, recovery information, mandatory Current JSONs and Folder JSON manifests, and global Master JSON **when enabled or otherwise retained**. Excluded temporary artifacts and recursive backup containers must be specifically documented with complete retention/reconstruction consequences. Backup copies must have an independently verified consistent source boundary; copying a moving collection of files into an inconsistent mixed-time representation is not a valid complete recovery point. A new backup DOES NOT silently force regeneration of mandatory per-file Current JSON or optional global Master JSON, nor complete pending Folder JSON verifications; it records the actual snapshot's verified revisions and any lag.

The first successfully verified complete backup of existing data is **External Backup Version 1**, distinct from mandatory per-file Current JSON and per-folder manifest revisions and optional Global Master JSON Version 1. No started, staged, interrupted or partially verified candidate may masquerade as a completed backup. Backup frequency is user-configurable independently of JSON schedules and retention: **Daily**, **Weekly**, **Smart / Adaptive**, **Manual**, or **Custom**. All modes expose **Back Up Now**. Schedules are eligibility targets, not guarantees when the NAS, external drive, authorization or resources are unavailable. If a backup becomes due during editing, offer a consistent point-in-time snapshot where the supported storage contract can provide one, or defer the backup until editing is complete; never claim a mixed-time copy is consistent. Before copying, estimate capacity for the complete copy, verification, staging and a reasonable margin; recheck during work. Check source health and do not replace the last healthy completed backup with known-corrupted source data. Report due/overdue/failure/unknown accurately. Reconnection must verify destination identity before a resumed operation; interrupted work MAY resume only from safe confirmed verified-chunk checkpoints. Do not display a fabricated fixed percentage or imply unverified work completed. No hidden post-close worker is implied.

The user chooses one of exactly two ordinary completed-version retention policies:

* **Single Backup:** latest successfully verified complete version after safe replacement.
* **Two Backups:** latest and immediately preceding successfully verified complete versions; each is a full standalone copy.

A new version MUST be fully constructed, verified and durably published **before** the old protected version is retired. This may temporarily require two physical full copies for Single mode or three for Two mode (including new staging), while normal completed retention returns to one or two after cleanup. Do not delete a verified backup early to make storage space; stop, disclose capacity shortfall and offer authorized alternatives. Failed attempts do not advance rotation. Suspend automatic retirement when known corruption, unresolved missing files or major integrity disputes make an old version potentially uniquely useful, recording any temporary retention excess. Because unknown corruption may be copied into a new backup, never guarantee that rotating a verified *byte-copy* guarantees a semantically healthy historical source. Every retirement must respect authorized erasure and historical access/security constraints.

### 53.5. JSON-first everyday repair and external disaster recovery

Ordinary local-file repair investigates the corresponding mandatory Current JSON first, then relevant durable pending changes/lineage and Folder JSON evidence, then any verified enabled global `master-data.json` or other surviving independently verified historical source. This is a **source-investigation order**, not a rule that the newest timestamp or first matching JSON automatically wins. Prefer file-scoped restoration when only one original is affected. Unexplained file differences may be deliberate external edits; do not silently roll them back. The engine MAY detect, investigate and stage a verified candidate automatically within authorized resources, but MUST obtain approval before replacing an existing original.

The separate complete backup is primarily for catastrophes: failed or lost primary storage, destroyed workspace, or large-scale unrecoverable loss. An explicitly chosen verified full backup can reconstruct the declared workspace in a safely selected location without relying on an earlier backup. A physically inaccessible original device's bytes cannot be promised recoverable or preserved. Avoid automatic destructive restoration into an occupied location; report backup freshness, gaps and key/schema dependencies. For a complete restore, present the simple destination choice of the originally selected workspace location or another user-chosen folder. Construct and verify the complete replacement in staging before modifying that destination. If a healthy destination already exists, identify the exact destination and replacement scope and obtain explicit confirmation; preserve its prior contents until the verified replacement can be safely published. Preflight required temporary capacity, pause safely if space is insufficient, preserve recovery evidence and offer another destination where supported. The selected-file restore workflow is described in subsection 53.6.

If Complete On-Site Backup is ON, a user MAY initiate a scoped file restore directly from a verified external backup independently of the optional Master JSON setting. Mandatory Current JSON always remains present as an application capability; the external restoration route is neither a hidden fallback implementation nor automatic backup-triggered replacement.

### 53.6. “I Think I'm Missing a File” — read-only comparison and selective restoration

Settings → Data Management → Recovery & Restoration MUST expose **“I Think I'm Missing a File”** or an equally clear localized action. The user chooses the backup folder or drive, optionally aided by the last configured location. Before comparing, validate backup identity, applicable manifest and available verified versions; Two Backup mode allows inspection of both retained versions. Comparison MUST remain read-only for both backup and workspace.

The result MUST distinguish files **missing from workspace**, **different**, **workspace-only**, **matching**, and **uncertain/inaccessible**, plus suspected moves or renames only where supported by evidence. Do not interpret a disconnected workspace as empty or automatically resurrect intentionally deleted files. Use manifest/inventory metadata to narrow comparison efficiently; inspect actual bytes when required to substantiate the proposed repair. A matching manifest alone does not prove a fresh content read.

For each candidate show the trusted relative path, backup version, relevant identity/revision, size, available hashes, current/backup location, verification state and conflicts; offer explicit individual or bounded bulk selection. If the latest backup lacks the desired file but a previous verified backup contains it, let the user inspect and deliberately choose that older version. No automatic bulk restore or unapproved expansion of selected items.

For authorized missing-file recovery: copy only the selected backup bytes into isolated staging, verify them, revalidate the destination and its nonexistence immediately before installing, then place and reread the file at the approved path and record provenance. If a file appeared at the target or its identity changed after comparison, invalidate the earlier approval and treat it as an existing-file replacement instead.

### 53.7. Existing-file replacement — exact-byte preservation

Any operation that would overwrite existing original data MUST provide an intelligible proposal stating the target, observed original identity/hash, source/version, candidate bytes/hash, excluded newer edits, preserved-original destination, storage required and affected related state. Approval MUST bind to those exact file identities, versions, hashes and material inputs, not merely to a filename or general “fix” request. Immediately before modifying, revalidate target identity, content and authorization; a change to any relevant file after approval invalidates it, requires a fresh comparison and approval, and MUST NOT be overwritten under stale consent.

Candidate reconstruction MUST be isolated and verified. Before replacement, preserve **the original's exact existing bytes** in a protected incident location and verify the preservation. If that cannot be safely done, refuse in-place replacement or offer a separately approved non-destructive recovery destination. Guard against traversal, absolute paths, symlink/junction/reparse escapes, reserved names, case/Unicode collisions, device/special-file paths and unapproved destinations. Recovery metadata must never grant filesystem write authority by presenting a path.

Apply replacements through a documented crash-recoverable transaction with durable per-file and, where applicable, batch states. Do NOT claim an atomic several-file transaction merely because one rename is atomic. After installation, verify active bytes, IDs and relationships; record a new restoration revision linked to the historical source without pretending the prior damage never occurred. Durably protect the recovery event; promptly synchronize the affected mandatory Current JSON, queue affected Folder JSON reverification, and allow enabled Master JSON to follow its separate schedule, while truthfully reporting all outstanding synchronization. A bulk approval is a closed list; items that become unsafe can be skipped but new items may not be silently added. Partial results remain partial, not success.

If source integrity, keys, revision legitimacy, target control or sufficient storage cannot be established, safely refuse destructive repair and show supported comparison/export/investigation alternatives. Restoration respects legitimate deletion decisions and [PRIV-1](#priv-1).

### 53.8. State reporting and technical implementation gates

Status MUST independently show durable original revision, mandatory per-file Current JSON freshness and verification, affected Folder JSON's last verified vs pending/conflict revision, enabled Master JSON revision/pending state, configured backup connectivity/versions/schedule, retirement holds, staging, recovery incidents and genuine unknown results. An optional ON toggle means user intent, **not evidence of completed verification**. Current JSON and Folder JSON must never be represented as user-disableable. An optional OFF feature cannot be represented as providing backup/global recovery; an unresolved folder conflict may not appear as a verified healthy latest revision.

Before production implementation or declaring this candidate ready for constitutional adoption, the App Plan and appropriate owner-authorized review MUST still resolve and verify: crash-durable edit protocol and multi-file consistency; physical snapshots and external-writer locking; per-platform paths and supported providers; NAS disconnections and partial writes; approval binding/expiry; exact-byte incident preservation and lawful retention; backup staging/publishing/retirement durability; capacity preflight; failure during cleanup; independent authenticity trust anchors where claimed; malicious filenames/paths and TOCTOU races; key access; deletion/privacy propagation; unattended worker lifecycle; and adversarial tests including power loss and partial recovery. Do not substitute a default implementation or assume these mechanisms have already been technically proven.

### 53.9. Candidate reconciliation ledger

| Existing RC4 rule | Candidate disposition (requires separate ratification) |
|---|---|
| INFO-1, SURVIVE-1, WORKSPACE-1/2/4 | Keep independently accessible originals and discoverability; explicitly expose mandatory Current/Folder JSON paths and independently optional Master JSON/backup; absence of `master-data.json` is acceptable when optional Master JSON is OFF. |
| JSON-1 through JSON-4 | Always-active per-file Current JSON literal copies, lightweight verified Folder JSON manifests, immediate affected-file sync initiation, and separately optional full Master JSON; truthful independent per-layer status, preservation of competing versions when review is required, highlighted per-hunk user reconciliation and JSON-first controlled recovery. |
| REV-1/REV-2 | Retain revision evidence and competing old/new contents when needed for conflict review; independent full external backup retained only if selected, with disclosed risks and no silent deletion on OFF. |
| BACKUP-1/BACKUP-2 | When a complete backup is ON or claimed, the full standalone scoped copy, completeness, verification, isolation limits and restoration evidence remain binding; with OFF, no fictional backup. |
| RECOVER-1, PRIV-1, NOFALL-2 | Preserve original bytes before approved replacement, block unsafe repair, respect lawful deletion, and distinguish approved recovery sources from forbidden implementation fallbacks. |
| WORKSPACE-TEST-1 and applicable TEST/DEV/GOV rules | Apply edge-case validation, independent adversarial reviews, evidence and exact-revision owner ratification before adoption or production promises. |

### 53.10. Folder JSON (Option B): verified manifest and status safety

The owner has selected **Option B** universally: Folder JSON is a mandatory verified inventory and consistency witness, **not a third physical copy of the file payloads**. Each applicable folder manifest MUST identify its own stable folder identity, directly retained child files, expected safe relative paths, file identities, declared size/type/hash and current revisions, corresponding per-file Current JSONs and their verified revisions, relevant relationships/deletion/move state and its own verification state. Child folder manifests are related by stable references, not embedded in a recursive envelope; appropriate manifest scopes must avoid recursion and preserve independent discoverability.

Each record/file's original and its complete literal Current JSON are two byte-reconstructible representations **within the same primary workspace failure domain**. If both are lost, a Folder JSON does NOT recover their contents. Enabled Master JSON or independent external backup may provide other actual sources at their disclosed verified revisions.

The verifier MUST preserve its last **Verified at revision R** published manifest while any new **Pending Verification at R+1** candidate is checked. On failure or conflict, do not advance the verified pointer or mislabel current bytes as verified. Source inspection uses actual bytes and trusted revision evidence, not solely a hash supplied by the suspect state; mere hash agreement cannot independently authenticate an adversarial edit. Deletion, rename and move require stable identities and coordinated old/new folder membership so an intentionally removed file is not silently resurrected. Files appearing while verification is running need a consistent revision boundary and fair rescheduling; ordinary edits do not cause whole-workspace rescans.

### 53.11. User-highlighted selective difference review and reconciliation

If old and new versions require **user reconciliation**—for example competing changes, ambiguous external edits, failed verification, conflicting revisions, or user-requested comparison—the application MUST compare available relevant verified *content*, not merely whole-file timestamps or names. **Only the added/new and removed/missing or replaced portions** should be highlighted by default; unchanged context is collapsed with optional expansion. Present accessible red/removed and green/added markings with text/icon labels, per-hunk scope, the old and current source identities/revisions, and a final result preview. This rule does NOT impose conflict popups after every ordinary authorized keystroke or routine save.

Where format semantics permit meaningful merging, the user MAY choose for each independent change **Keep Previous**, **Keep Current**, or **Keep Both**. Mixing choices is permitted: retain an old paragraph while accepting a newly added section elsewhere. Present an accurate merged preview **before** applying. For plain text, Markdown, code and suitable structured documents use bounded line-, word-, field- or block-level diffs appropriate to the format. For PDFs, images or other visual formats use a genuinely supported page/visual/structural comparison where available. Binary or unsupported formats MUST use a truthful file-version/size/hash/metadata comparison or separate-copy review; never invent line-level content or silently combine incompatible binary bytes.

Folder JSON alone never contains prior full-file text. The comparison MUST retrieve its old/new bytes from actual surviving originals, verified Current JSON revisions, appropriately retained historical content or other legitimate verified sources. A manifest/hash without bytes is not a restore point. **When review is required and both contents are available, preserve the competing original and last verified recoverable Current JSON revision during the unresolved decision** rather than immediately replacing the only old recoverable copy with new bytes. If the old content has already legitimately expired or is unavailable, show the limitation and do not fabricate a diff or promise a “Keep Previous” option. Retention follows privacy and authorized erasure duties; no immutable forever copies are implied.

The system MUST distinguish an intentional deletion from accidental loss, and a legitimate new revision from unexpected corruption. It MUST NOT auto-select whichever version is newest or assume a changed original is bad. User choices/approval bind to exact original/current candidate hashes, revision IDs, specific selected changes and approved output. If the file changes during the review, invalidate stale approval and recompare. A chosen result that would replace an existing original MUST be safely staged and validated, preserve that original's exact present bytes beforehand, commit through a crash-recoverable transaction, record provenance/new revision, synchronize **only the affected Current JSON** promptly and queue affected Folder JSON reverification. No unapproved expansion of changes, no silent destructive merge, and no general overwrite of unrelated files. Report partially resolved or uncertain states honestly.

### 53.12. Implementation gates and resource safeguards

“Immediately update Current JSON” means **begin or safely queue the affected-file synchronization promptly**, not promise that a very large original can always be fully re-encoded and published within a fixed number of seconds. Do not rewrite unchanged Current JSONs, scan all other folders, or continuously re-encode a multi-gigabyte growing recording merely to meet an arbitrary timer. A published Current JSON remains a complete reconstructible payload even if construction uses memory-bounded streaming/staging and coalescing internally. Keep a durable honest original-file commit/recovery boundary that remains safe during Current JSON lag. The underlying storage medium can still fail and destroy the original and co-located JSON; optional physical independent backup addresses that separate failure class.

Use **Automatic Resource Management** by default to adapt CPU, memory, I/O and energy to the actual device, workload and available capacity. Optional **Memory Saver** and **Priority** modes belong under Advanced Settings. Under resource pressure, throttle lower-priority work first and communicate a material performance, energy or waiting impact in proportion to its user effect. The normal work order is safe original-file saves, required recovery obligations, mandatory Current JSON, affected Folder JSON and synchronization, then optional backup work, while honoring correctness dependencies between stages. Estimate realistic capacity and margin before large operations, recheck during work, and pause safely on actual exhaustion. Design for the lowest practical supported device specifications while permitting a justified temporary resource increase when needed for reliable behavior; do not invent one hardware threshold for every platform.

Before production implementation, the App Plan must resolve and actually test per-platform durable original writes, snapshot consistency while files grow, transaction journal semantics, last-verified-version preservation, collision/path/symlink security, long-running verification throttles, record/folder identity on move, external edits, legitimate deletion, privacy retention, missing revisions, binary diff limitations, insufficient staging capacity, interrupted build/replay, user approval staleness, trust anchors and safe background worker lifetime. Exact JSON names and logical object adaptations may vary per application **only** if all required outcomes and independently accessible file identities remain supported. This universal decision applies to all qualifying retained-data apps; Menemora is only an explanatory example. Neither this documentation change nor its publication itself migrates application data or implements runtime features.


**Historical integrity:** Changes in this candidate are proposed changes to RC4's normative text, not retroactive changes to the existing ratified RC4 commit or its independent reviews. The numeric rule-ID inventory remains stable for traceability; changed rule wording and applicability MUST receive fresh independent review. This candidate is explicitly **NOT RATIFIED**.

### 53.13. Owner-controlled review and completion boundary — non-normative

This mission integrates and publishes the current single-file candidate, freezes its exact published revision, performs the authorized read-only adversarial review, reports findings and then stops. It does not complete historical review-convergence requirements, ratify the candidate, apply findings, begin application development, or authorize multiple Markdown files. The owner-controlled later sequence is: review and discuss findings; separately authorize and apply fixes in a subsequent mission; supply any additional Markdown material; separately authorize any multi-file restructuring; run a fresh broad review of the restructured rulebook; resolve mandatory review gates; explicitly ratify one exact revision; and only then begin application development. No earlier historical reviews count as review evidence for this revision.
