# Universal Rules for All Apps

> Version: 1.0.0-rc2.1<br>
> Status: Owner-Authorized Repaired Frozen Candidate — Fresh Red Review Required — Not Yet Ratified<br>
> Date: 2026-10-13<br>
> Prior frozen review target: `e15191c1509facc3859b46c25cc8a1d1b7eaa12f`<br>
> Document identifier: ECOSYSTEM-CONST-001<br>
> Source repository: https://github.com/mhyahya854/Universal-Rules<br>
> Governance authority: repository owner/user, unless explicitly delegated<br>
> Integration baseline: reviewed `1.0.0-rc1`, `d9fc392ceddad5f760e0d4a71070bbc723609f77`

This constitution governs ecosystem software through engineering invariants, deliberate ecosystem policies, and capability-specific requirements. Candidate `1.0.0-rc2.1` is the owner-authorized repaired frozen successor to `1.0.0-rc2` at `e15191c1509facc3859b46c25cc8a1d1b7eaa12f`. The owner authorized GREEN FIX for RF-01 and RF-02 only on 2026-10-13: DEV-5 clarifies bounded pre-freeze research experiments; GOV-5 conditions clean-result reporting and preserves universal residual-risk disclosure. No other normative rule changed. The [repair record](governance/2026-10-green-fix-rf01-rf02.md) identifies authorization, prior findings, dispositions, validation, and the new frozen revision. The [original freeze record](governance/2026-10-plan-freeze.md) remains historical evidence. The previous Red result does not count toward post-repair convergence; two consecutive independent clean Red rounds are required. This candidate is unratified and has not received a post-repair Red attack. Earlier integration gates remain historical prerequisites satisfied by the recorded owner freeze and scoped repair authorization, not waivers of substantive rules.

Its purpose is to maximize the probability that applications remain maintainable, understandable, recoverable, portable, evolvable, AI-continuable, user-controlled, structurally coherent, and usable for as many years as reasonably possible. It is a blueprint and development system for discovering, challenging, documenting, building, verifying, and maintaining app-specific designs, not a requirement for identical features or content hierarchies. The development lifecycle is specified in [section 31](#s31).

## Contents

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
30. [Freeze status and review continuation — non-normative](#s30)
31. [Application planning, continuity, and conformance](#s31)
32. [Universal Information Architecture Blueprint](#s32)
33. [Reusable Universal Agent Skills governance](#s33)

<a id="s01"></a>
## 1. Scope and rule classification

<a id="gov-1"></a>
### GOV-1 — Interpretation and applicability

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

<a id="s02"></a>
## 2. Foundations and domain hazards

<a id="safe-1"></a>
### SAFE-1 — Integrity and truthful guarantees

**Type:** UNIVERSAL INVARIANT | **Origin:** DERIVED ENGINEERING RULE | **Applies:** operations and retained information governed by an application contract

Applications MUST protect retained user data according to declared integrity and lifecycle contracts and MUST NOT silently corrupt it or misrepresent known loss. Intentional loss, transformation, or deletion requires applicable authority and accurate semantics. Important operation outcomes MUST be truthful under [OUT-1](#out-1). Guarantees require appropriate evidence under [TEST-1](#test-1), with limits and uncertainty disclosed.

<a id="safe-2"></a>
### SAFE-2 — Domain-aware hazard decisions

**Type:** UNIVERSAL INVARIANT | **Origin:** DERIVED ENGINEERING RULE | **Applies:** conflicts among safety, security, privacy, integrity, and operational obligations

Applications MUST identify material domain hazards and applicable obligations and resolve conflicts on that basis. A global ranking MUST NOT force data preservation when it creates greater human, physical, security, or privacy harm or defeats applicable erasure duties. Emergency shutdown, credential revocation, and containment can require intentional interruption or loss. Record consequential tradeoffs and residual risks proportionately.

Example: a hardware controller may stop an actuator before persisting telemetry; an archive may prioritize retention under a legitimate preservation duty. Neither priority becomes a universal ordering for other domains.

<a id="safe-3"></a>
### SAFE-3 — Explicit, testable core behavior

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

<a id="s04"></a>
## 4. Principals and delegation

<a id="auth-1"></a>
### AUTH-1 — Effective authorization and integrity enforcement

**Type:** UNIVERSAL INVARIANT | **Origin:** DERIVED ENGINEERING RULE | **Applies:** effects subject to authorization or integrity constraints

Permissions, domain constraints, and effect limits MUST be enforced at a boundary callers cannot silently bypass within the declared threat model. Hidden UI controls and prompts alone are insufficient. Interfaces may differ in authentication, privileges, quotas, rate limits, confirmation, and scope; they MUST NOT introduce an unacknowledged bypass of applicable integrity constraints. Administrative operations need explicitly authorized semantics.

Enforcement can reside in functions, databases, services, sandboxes, operating-system boundaries, or combinations. An in-process convention does not establish protection against a malicious same-account process or host administrator.

<a id="auth-2"></a>
### AUTH-2 — Ownership, delegation, and attribution

**Type:** UNIVERSAL INVARIANT | **Origin:** DERIVED ENGINEERING RULE | **Applies:** operations requiring authority or accountability

Applications MUST distinguish the relevant principal, actor, mechanism, and delegation. Machine ownership MUST NOT imply ownership of all data or unrestricted authority. Shared ownership, data-subject rights, administration, and tenant boundaries require explicit authority and conflict semantics.

Delegations MUST define relevant resources, allowed effects, duration or lifecycle, conditions, and revocation behavior. Accountability-required operations MUST be attributable to the extent supported by evidence; unknown or externally asserted identity MUST NOT be reported as verified. Queued and long-running actions MUST handle authority changes according to their delegation contract.

<a id="s05"></a>
## 5. Rust-first implementation

<a id="lang-1"></a>
### LANG-1 — Rust as the mandatory ecosystem default

**Type:** ECOSYSTEM POLICY | **Origin:** USER POLICY | **Applies:** new software and components developed in this ecosystem

Rust is the presumptive language for applications, services, background processes, CLI tools, core libraries, storage engines, synchronization components, AI tool servers, and other software. A non-Rust selection MUST document why another language materially better meets the component's requirements and obtain applicable approval under [GOV-3](#gov-3). The burden of justification belongs to the deviation.

The question is: **What concrete technical requirement makes another language materially more appropriate for this component?**

Valid reasons include platform-required SDKs/languages; critical capabilities unavailable or impractical in Rust; host/plugin constraints; specialized scientific/ML ecosystems; interoperability/runtime constraints; deployment requirements; materially safer lifecycle or maintenance outcomes; and scripting, configuration, or generated glue where Rust adds disproportionate complexity without meaningful benefit.

Familiarity, habit, popularity, trendiness, tutorials, framework preference, avoiding Rust's learning curve, or faster personal prototyping are insufficient by themselves. Staffing, qualification, certification, expertise, long-term maintenance, and operational support can justify a deviation when tied to material lifecycle or safety risk.

The decision MUST identify the component, selected language, concrete reason Rust was rejected, why the alternative better meets requirements, and whether scope is one component or the whole application. Polyglot systems are permitted with deliberate, maintainable boundaries. Rust is especially preferred for canonical state, filesystem operations, synchronization, concurrency, long-running services, security boundaries, durable infrastructure, performance-sensitive work, AI capability enforcement, and domain operations.

This language-selection requirement governs authored implementation components. Importing a library or an FFI dependency written in another language does not by itself constitute authoring a new non-Rust application component; dependency and boundary responsibilities still apply. Generated bindings/code, SQL, configuration, shaders, schemas, platform resources, and frontend assets MUST be classified by their role rather than their file extension. They are not automatically separate application components requiring individual exceptions. Authored executable frontend or other implementation logic remains subject to this policy. A documented component-level or standing exception MAY cover related implementation artifacts within its approved scope; generated glue does not exempt independently authored domain logic. The shared product core follows [CORE-1](#core-1).

Rust does not establish domain correctness, storage durability, distributed consistency, safe FFI, secure architecture, or correct concurrency semantics. Those remain architectural responsibilities. This policy does not itself mandate rewriting existing applications. Rationale and examples: [ADR-0001](decisions/ADR-0001-rust-first.md).

<a id="s06"></a>
## 6. Feature-first architecture, shared core, and UI

<a id="arch-1"></a>
### ARCH-1 — Feature-first organization

**Type:** ECOSYSTEM POLICY | **Origin:** USER POLICY | **Applies:** applications with multiple meaningful user or domain capabilities

Feature-first organization is presumptive. Responsibility ownership, domain/capability boundaries, authoritative-state ownership, shared concepts, dependencies, and cross-boundary effects MUST be understandable and deliberate. A feature MUST NOT silently bypass another feature's applicable invariants. Policy departures require a scoped rationale and approval under [GOV-3](#gov-3).

No fixed folders or files are prescribed. A tiny cohesive utility is outside the multi-capability trigger. Compiler passes, signal-processing pipelines, rendering engines, mathematical kernels, framework layers, hardware-oriented structures, and justified process boundaries are valid where appropriate. Different folder names or fewer layers are not policy exceptions.

<a id="arch-2"></a>
### ARCH-2 — Modular monolith by default

**Type:** DEFAULT | **Origin:** USER POLICY | **Applies:** ordinary feature-rich application deployment

A modular monolith SHOULD be preferred when it is the simplest design satisfying isolation, reliability, privilege boundaries, scaling, deployment, lifecycle, maintainability, and performance. Multiple processes/services may be justified by fault containment, plugin isolation, runtime incompatibility, independent lifecycle, hardware placement, operational economics, reliability, or scaling. Record the rationale; literal single-process impossibility is not required. Distribution adds network, transaction, deployment, and recovery responsibilities.

<a id="arch-3"></a>
### ARCH-3 — Contracts and shared code

**Type:** DEFAULT | **Origin:** ARCHITECTURAL DECISION | **Applies:** modular codebases

Modules SHOULD communicate through explicit interfaces and avoid unnecessary dependency cycles. Build-time cycles and runtime conversations differ. Shared code SHOULD have cohesive responsibility and ownership; substantial shared domain kernels may be appropriate. Choose duplication or reuse by consistency needs and change coupling, not line counts or folder names.

Examples: typed application functions, query ports, commands, events, actor messages, callbacks, streams, and plugin protocols. A feature may contain domain logic, adapters, presentation, tests, and documentation without needing every category. An event bus can conceal coupling and does not by itself prove modularity.

<a id="core-1"></a>
### CORE-1 — One shared Rust product core

**Type:** ECOSYSTEM POLICY | **Origin:** USER POLICY | **Applies:** products with multiple clients sharing domain or durable application behavior

Where technically practical, all clients of the same product MUST share the same Rust core for domain logic, canonical-state rules, data models, validation, synchronization, conflict semantics, migrations where applicable, authorization rules, AI capability enforcement, and durable application behavior. The goal is **one product truth, multiple clients**. Platform code may call into the core through suitable interfaces. Business logic MUST NOT be independently rewritten in Kotlin, Swift, TypeScript, or desktop frontend code merely because clients use different UI technologies.

This spans applicable Windows, macOS, Linux, Android, iOS, iPadOS, tablet, and web-associated native clients within the declared product scope. Neither UI strategy may independently alter canonical behavior; product behavior remains governed by the shared core and its documented technical exceptions.

Supported AI, native UI, web, CLI, and headless interfaces MUST operate on the same logical application state through shared core/domain contracts. They MUST NOT unknowingly maintain separate incompatible truths merely because the interface differs. Declared replicas and interface-specific presentation/preferences are allowed; canonical state and synchronization remain explicit under [DATA-1](#data-1) and [SYNC-1](#sync-1). Planning MUST ask whether a supported interface could disappear for years and return without conversion from a separate hidden interface-only truth. Legitimate version/schema migration may still be required.

Technical departures MUST document the affected component, concrete constraint, scope, and consistency implications under [LANG-1](#lang-1) and [GOV-3](#gov-3). A shared core may consist of cohesive feature modules and target-specific builds; it does not require one giant module, identical binaries, or one process. [ARCH-3](#arch-3)'s general duplication discretion does not override this product-core policy. Shared code does not establish trusted execution: enforce authority at the effective boundary under [AUTH-1](#auth-1), including service-side enforcement where clients are untrusted.

<a id="ui-1"></a>
### UI-1 — Platform-appropriate or shared UI

**Type:** ECOSYSTEM POLICY | **Origin:** USER POLICY | **Applies:** products with user interfaces across platform scopes

When resources allow, products SHOULD prefer separate platform-appropriate UIs while preserving product identity, visual consistency, and applicable capabilities. Android-native UI technologies, Swift/SwiftUI on Apple platforms, and suitable desktop technologies are valid choices. Non-Rust platform UI components may meet [LANG-1](#lang-1)'s technical exception criteria; record the component or standing exception without treating it as permission to duplicate core behavior.

When maintaining several UIs imposes excessive time or development cost, a shared cross-platform UI MAY be selected as a first-class compliant architecture. This is not an inferior compliance state and needs no exception to this UI strategy. Its implementation language still follows [LANG-1](#lang-1). Both strategies preserve the shared Rust core under [CORE-1](#core-1).

<a id="ui-2"></a>
### UI-2 — Reuse priorities and adaptive presentation

**Type:** ECOSYSTEM POLICY | **Origin:** USER POLICY | **Applies:** products spanning device sizes or platform interaction models

Products MUST share core logic under [CORE-1](#core-1), SHOULD share UI when beneficial, and MUST NOT sacrifice a materially better platform experience merely to maximize UI code reuse. Cross-platform does not mean identical presentation. Navigation, layouts, windowing, gestures, keyboard behavior, menus, share interfaces, and platform integrations may differ while representing the same underlying product and data. Phone and tablet interfaces MUST adapt to their interaction and layout needs rather than simply stretching a phone interface onto a tablet.

<a id="ui-3"></a>
### UI-3 — Accessible interaction as product correctness

**Type:** ECOSYSTEM POLICY | **Origin:** USER POLICY | **Applies:** user-facing capabilities, including administration and tooling interfaces where exposed

Important supported workflows MUST provide reasonable accessible interaction appropriate to the target platform and interaction model. The App Plan MUST identify applicable accessibility acceptance criteria and relevant platform/industry standards, considering keyboard or other non-pointer operation, semantic controls, assistive technology, text scaling, visible/readable focus, contrast, reduced motion, and alternative interaction where relevant. Accessibility is part of product correctness, not merely optional visual polish; validate applicable workflows under [TEST-1](#test-1).

Native, shared cross-platform, and web UIs retain this outcome while adapting mechanisms and presentation under [UI-1](#ui-1) and [UI-2](#ui-2). No single accessibility standard or identical UI is universally required. Headless libraries, background daemons, and machine-facing APIs need no graphical accessibility controls; any user-facing administration or tooling is assessed on its own applicable interactions.

Accessibility MUST be considered from relevant wireframe, component, interaction/state, and design-system decisions, not deferred entirely to final polish. Applicable criteria SHOULD address accessible names, focus order/visibility, screen-reader structure, target size, dragging alternatives, and non-color-only meaning. Use current platform/industry guidance and WCAG/APG where applicable without imposing web mechanisms on native/headless software.

<a id="ui-4"></a>
### UI-4 — Deliberate design brief, identity, and generic-aesthetic review

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

References from software/screenshots/platforms, design systems, print, architecture, photography, physical products, typography, moodboards, or historical UI MAY inform composition, rhythm, hierarchy, interaction, and density. References do not authorize copying proprietary work. Prefer owner-created, properly licensed/open resources, public standards, and original design, preserving relevant provenance. Art-direction dials such as variance, motion intensity, or density MAY clarify the brief; no third-party numerical default becomes universal policy.

<a id="ui-5"></a>
### UI-5 — Coherent design system and purposeful presentation

**Type:** ECOSYSTEM POLICY | **Origin:** USER POLICY | **Applies:** substantial user-facing applications and supported themes/platform presentations

Applications MUST define a reusable design system or equivalent coherent design contract for relevant typography, sizes/weights/line heights, spacing/grid/rhythm, colors/surfaces, borders/radii, elevation/shadows, icons, motion, focus, interaction states, and responsive behavior. Do not improvise these independently per screen. Semantic design tokens SHOULD represent reusable visual constants where practical; names such as `surface.primary`, `text.muted`, `action.primary`, `status.error`, `space.1`, or `motion.quick` are examples, not universal naming. Equivalent controls SHOULD share semantic behavior for primary/destructive actions, modal dismissal, validation, search, selection, navigation, and notifications instead of arbitrary conventions for novelty.

The approximate **60 / 30 / 10** color balance SHOULD be a starting heuristic where appropriate: dominant/base canvas and large low-emphasis surfaces; secondary/supporting navigation, panels, and structural surfaces; scarce accent for primary actions, focus, and selected/active emphasis. No literal pixel counting or mathematical ratio enforcement is required. Semantic error/danger/warning/success/information/focus/selection communication and accessibility MUST take precedence over this decorative balance. Primary accent SHOULD retain meaning rather than indiscriminately color every icon, heading, card, border, and control.

Supported dark mode MUST be deliberately designed rather than blindly invert light mode: define relevant surfaces, hierarchy, contrast, text tones, borders, shadows/elevation, focus/semantic states, and image treatment. Themes retain product identity without requiring identical visual treatment. Typography SHOULD be deliberately selected for readability, hierarchy, platform, supported languages, weights, performance, licensing, and longevity; Inter, Roboto, or framework defaults are valid when reasoned. Iconography SHOULD use a coherent family/style with deliberate reasons for mixed strokes, filled/outline styles, or generated imagery; vector artwork remains subject to [ASSET-1](#asset-1).

Density SHOULD reflect task frequency, information complexity, expertise, device size, and accessibility, rather than universally impose huge cards, spacing, or typography on finance, developer, media, medical, settings, and other products. Motion SHOULD communicate transition, relationship, hierarchy, continuity, progress, or feedback; respect reduced-motion needs under [UI-3](#ui-3). Visual decoration MUST NOT obscure hierarchy, navigation, actions, application state, errors/warnings, permissions, security/sync state, or progress. Product identity MUST respect applicable navigation, keyboard/windowing/gesture/back/menu/input/selection/system-control conventions; cross-platform consistency means shared identity and semantics, not identical pixels. [UI-2](#ui-2) and [CORE-1](#core-1) still govern adaptation and common product truth.

Establish the core design system before proliferating independently designed screens. Avoid artificial sparsity and chaotic density through grouping/hierarchy. Icon aggregators do not license every underlying asset; verify collection/asset licensing and provenance under [ASSET-2](#asset-2) and [SEC-3](#sec-3). Motion MUST NOT be the only channel of important meaning. Refine hover/pressed/focus/loading/transition/scroll/selection/drag/success/error micro-interactions after the interaction structure is sound; polish does not rescue missing information architecture.

<a id="ui-6"></a>
### UI-6 — Complete workflow states and actionable copy

**Type:** ECOSYSTEM POLICY | **Origin:** USER POLICY | **Applies:** user-facing workflows and their materially relevant states

Design MUST cover relevant states beyond the ideal happy path: initial/empty, loading/progressive loading, success/error/partial failure, unavailable service, offline/reconnecting, sync conflict, stale information, permission denied/authentication required, migration/recovery/unsupported version, security scan running/detection/quarantine/scanner unavailable, backup/recovery state, destructive confirmation, and irreversible-action warnings. A state with no applicable capability need not be invented. State presentation MUST accurately reflect outcomes and uncertainty under [OUT-1](#out-1), [RUN-2](#run-2), and [IO-3](#io-3), without changing established authorization or confirmation policy.

User-facing copy MUST be specific, understandable, context-aware, and concise where possible, explaining actual value, state, or action rather than generic AI marketing. Empty states SHOULD explain what belongs there, why it is empty, a useful next action, and whether content is expected automatically where relevant; generic “Nothing here yet!” filler and meaningless illustrations are insufficient when guidance is needed. Errors SHOULD explain what happened/was affected, whether anything changed, whether retry is safe, and the next action to the extent known. Raw implementation failures or “Something went wrong” MUST NOT be the sole explanation when they conceal known material information or uncertainty. Apply [PRIV-1](#priv-1) and [SEC-2](#sec-2) to disclosures.

<a id="ui-7"></a>
### UI-7 — Rendered UI evidence and completion gate

**Type:** ECOSYSTEM POLICY | **Origin:** USER POLICY | **Applies:** substantial interface completion and validation of supported sizes/workflows

UI evaluation MUST NOT rely solely on immaculate placeholders or lorem ipsum. Test relevant long/short names, absent optional information, large/small numbers, long/empty lists, unusual Unicode, supported languages, long dates/times/filenames, errors, and realistic content density. Where multiple sizes/form factors are supported, validate actual rendered UI at representative sizes for hierarchy, controls, density, text readability, overflow, navigation, focus, touch targets, and orientation where relevant. A responsive framework alone does not establish good adaptive behavior.

Substantial interface work MUST receive visual review from actual rendered output, using real rendering, screenshots, device previews, human/AI visual review, or equivalent evidence as appropriate; source correctness alone is insufficient. Mature interfaces SHOULD consider visual-regression automation where stability matters; trivial UIs need no screenshot infrastructure. Before declaring substantial UI implementation complete, explicitly review product identity, component/design-system consistency, platform conventions, accessibility, responsive/adaptive behavior, state coverage, realistic content, generic-aesthetic signals, and visual hierarchy. Evidence may be concise but MUST compare rendered behavior with the design brief/contracts and applicable [UI-3](#ui-3) criteria. This review feeds [DEV-13](#dev-13)'s existing Three-Layer Conformance Gate rather than replacing it or creating a second completion authority.

Use a proportionate draft → render → inspect → identify specific issue → modify → render/re-review loop, preferably in coherent flows/screens/components/states rather than giant one-shot whole-product generation. Include representative zoom/text scaling, platform context, and supported localizations/RTL where relevant. Passing code tests MUST NOT alone overrule a coherent owner/designer rejection against intended product direction; preserve actionable evidence and resolve it under project authority/contracts.

Substantial UI SHOULD receive applicable usability heuristic review: system status, real-world match, user control, consistency, error prevention, recognition over memory, flexibility, minimalist focus, error recovery, and useful help. Progressive disclosure SHOULD reduce complexity without hiding necessary primary/frequent functions merely for visual sparsity. Where scale/stakes justify it, validate representative tasks with users, owner walkthroughs for personal products, or equivalent evidence. Tiny personal utilities need no formal research bureaucracy. Subjectivity does not excuse required brief, rendered evidence, accessibility, or workflow review.

For substantial or high-stakes interfaces where resources justify formal heuristic evaluation, multiple independent reviewers SHOULD be preferred over a single self-review, with findings aggregated because different perspectives can uncover different usability failures. No fixed reviewer count or expert panel is required for every interface; this preference neither replaces evidence-based completion nor authorizes a constitutional Red review.

<a id="s07"></a>
## 7. Data lifecycle and application replacement

<a id="life-1"></a>
### LIFE-1 — Preservation across supported replacement

**Type:** UNIVERSAL INVARIANT | **Origin:** DERIVED ENGINEERING RULE | **Applies:** installation, update, replacement, or removal with retained state

Lifecycle operations MUST honor declared preservation and deletion semantics. Retained data, user configuration, required keys, and required evidence MUST NOT be accidentally destroyed by an operation represented as preserving them. Reattachment claims MUST account for schemas, keys, permissions, formats, and required software.

<a id="life-2"></a>
### LIFE-2 — Long-term accessibility

**Type:** ECOSYSTEM POLICY | **Origin:** USER POLICY | **Applies:** information designated for long-term user retention

Applications MUST provide a practicable preservation and exit path beyond a particular runtime or vendor's lifetime, using documented formats, exports, readers, and recovery dependencies as appropriate. This does not require indefinite retention of expiring tokens or deleted content. Host bindings and secrets need an explicit portability/recovery strategy.

Where durable user information is retained, its lifecycle MUST be distinguished from replaceable application binaries, UI, AI/model providers, indexes, runtime state, and machines. Loss or replacement of one of those components MUST NOT automatically destroy or unnecessarily trap the retained information within disposable implementation state. Planning MUST ask: **Could the application implementation be replaced without unnecessarily destroying or trapping the user's retained information?** Recovery remains bounded by declared retention, portability, and dependency contracts, including [BACKUP-1](#backup-1); this does not promise that every binary artifact is readable without software or that every failure is recoverable.

The goal is **maintenance-minimal**, not maintenance-zero: documented schemas, portable data, replaceable components, the shared Rust core, stable identities, migration discipline, explicit dependencies, tests, reproducible builds where applicable, rebuildable derived state, and durable planning context reduce future work. Applications MUST NOT promise that they work forever without maintenance without supportable evidence.

<a id="life-3"></a>
### LIFE-3 — Logical storage separation

**Type:** RECOMMENDATION | **Origin:** ARCHITECTURAL DECISION | **Applies:** applications with multiple data lifecycles

Applications SHOULD distinguish replaceable code, retained data, configuration, generated artifacts, audit evidence, operational logs, backups, and exports. Directories, tables, object namespaces, or platform-managed stores may implement the distinction. Executables and data may be colocated if lifecycle operations preserve their contracts.

Roles such as `app/`, `data/`, `config/`, `derived/`, `audit/`, `cache/`, `logs/`, `backups/`, and `exports/` are illustrative. An export is not automatically disposable staging. Git may intentionally store canonical documents; it is not automatically a suitable database or independent backup. Prevent unintended inclusion in unrelated source repositories using suitable ignore rules, controls, and review; `.gitignore` is not an enforcement boundary.

<a id="s08"></a>
## 8. Authority, derivation, and reproducibility

<a id="data-1"></a>
### DATA-1 — Independent state dimensions

**Type:** UNIVERSAL INVARIANT | **Origin:** DERIVED ENGINEERING RULE | **Applies:** state whose authority or lifecycle matters

Applications MUST identify authoritative state and when other representations may be relied on or discarded. Authority, factual verification, provenance, ownership, reproducibility, retention value, recovery cost, sensitivity, and lifecycle MUST NOT be automatically treated as equivalent or inferred from one another without an explicit justified rule. Valid policy relationships between these dimensions are permitted; for example, sensitivity can inform retention and access policy. A generated document may be authoritative and valuable; canonical temporary state may expire. Distributed authority is permitted with defined semantics.

Storage technology does not determine authority: a vector database can hold authoritative originals and embeddings. An expendable cache must not hold the only copy of information promised preservation. Human edits or confirmation do not establish factual correctness of a whole record. Verification claims MUST identify the actual reviewed scope.

<a id="data-2"></a>
### DATA-2 — Honest regeneration claims

**Type:** CONDITIONAL | **Origin:** DERIVED ENGINEERING RULE | **Applies:** artifacts claimed to be rebuildable through generation

Recovery MUST specify its target: identical bytes, semantic equivalence, equivalent functionality or quality, or an acceptable replacement. Exact reproduction claims require preserved dependencies and evidence. If exact artifact identity matters, preserve the artifact for its required lifecycle rather than relying on unproven regeneration.

Account for models, versions, seeds, external inputs, licenses, hardware behavior, cost, and availability where relevant. Non-reproducible outputs and expensive embeddings are not automatically disposable. Derived-state backup is permitted. Synchronous indexes/materialized views are permitted; derivation does not grant authority to mutate canonical records outside [AUTH-1](#auth-1).

Indexes, search/vector databases, embeddings, caches, previews, thumbnails, OCR indexes, materialized views, and generated reports/workbooks are often derived; their actual authority and retention follow [DATA-1](#data-1), not their names. Deleting a store declared rebuildable MUST NOT destroy the canonical information or retained dependencies needed for its declared rebuild contract. A derived artifact MUST NOT silently become the sole copy of irreplaceable information.

Editing a derived report, spreadsheet, index, dashboard, projection, cache, or generated view MUST NOT silently mutate canonical state. Supported bidirectional editing requires deliberately designed, validated adoption/import semantics under [EDIT-1](#edit-1), [IO-1](#io-1), and [AUTH-1](#auth-1); a projection is not automatically a write authority.

<a id="data-3"></a>
### DATA-3 — Originals, derivative lineage, and annotations

**Type:** ECOSYSTEM POLICY | **Origin:** USER POLICY | **Applies:** applications ingesting or preserving source artifacts and meaningful derivatives

Applications MUST distinguish preserved originals from extraction, normalization, transformation, interpretation, annotation, AI-generated derivatives, and canonical decisions where those roles exist. A searchable derivative MUST NOT silently replace a preserved original merely for convenience. Preservation follows the declared retention/privacy contract, not indefinite storage of every source.

Meaningful derivatives SHOULD retain proportionate lineage sufficient to identify their parent/source and relevant source version/hash, tool/version, model/version where applicable, creation time, method, and review/verification status. Not every field is needed for trivial artifacts, and uncertain model identity must remain uncertain. Material source changes MUST support invalidation, stale marking, regeneration, or review as appropriate rather than silently representing outdated derivatives as current. Lineage and its retention follow [EVID-1](#evid-1) and [PRIV-1](#priv-1).

Where originals are to be preserved, notes, highlights, comments, tags, review decisions, and AI annotations SHOULD normally be related overlays anchored to the original, rather than destructive alteration. Ordinary editable documents remain valid. Anchors and their source-context validity follow [INFO-4](#info-4).

<a id="data-4"></a>
### DATA-4 — Locale-independent durable meaning

**Type:** ECOSYSTEM POLICY | **Origin:** USER POLICY | **Applies:** durable or interchange values whose interpretation or identity can materially depend on locale or text conventions

Persistent/interchange meaning MUST NOT silently depend on the reading device's current display locale. Use typed or otherwise unambiguous representations where needed, separating semantic values from locale-aware presentation. The App Plan MUST declare relevant number, date, currency, percentage, unit, sorting/collation, encoding, Unicode normalization, case, and identifier semantics where these affect durable meaning or identity across supported platforms. [PORT-2](#port-2) governs filesystem differences; no universal normalization algorithm is prescribed.

Human-formatted imports/exports MUST declare parsing/interpretation assumptions, detect ambiguity where practical, and preserve source representation/provenance where meaningful under [IO-1](#io-1), [EVID-1](#evid-1), and [PRIV-1](#priv-1). An ambiguous value such as `1,234` MUST NOT silently be reinterpreted using the current device locale when durable meaning matters. No translation mandate, support for every locale, or locale metadata on every stored string is required.

<a id="data-5"></a>
### DATA-5 — Universal timezone policy and explicit temporal meaning

**Type:** ECOSYSTEM POLICY | **Origin:** USER POLICY | **Applies:** every application's timezone planning, with temporal representations and controls determined by actual semantics

Every App Plan MUST explicitly state its timezone policy, regardless of domain or presence of scheduling features. Define how timezone-sensitive values are represented, converted, persisted, compared, displayed, imported, exported, synchronized, and migrated wherever those operations occur. Consider logs, audit events, backups, sync, filesystem observations, migrations, certificates/security events, scheduled jobs, reports, APIs, receipts, provenance, and diagnostics as well as user-visible domain values. A small application may use a concise statement identifying its actual temporal inputs/outputs and absent operations; lack of scheduling MUST NOT be used to omit timezone planning.

Distinguish relevant event/effective time, source observation, ingestion, creation/modification, due time, absolute instants, local civil date/time, timezone-relative schedules, recurring local times, date-only values, elapsed durations, and monotonic runtime intervals. Only relevant concepts need representation. Date-only birthdays, elapsed durations, and monotonic timers MUST NOT acquire arbitrary timezone meaning or conversions. UTC instants are appropriate for many events, not a universal representation for every temporal concept.

Changes to OS timezone, travel location, device, NAS, or locale MUST NOT silently reinterpret persisted historical meaning. Conversions MUST retain enough source context to reconstruct or explain the relevant original meaning where required by the domain/retention contract, distinguishing source timezone, canonical instant, and display timezone where significant. For example, a deadline defined as 23:59 Asia/Bahrain does not become 23:59 Europe/London because a laptop travels; a converted display may differ while preserving declared meaning. Retention remains subject to [PRIV-1](#priv-1).

An observed offset such as UTC+03:00 and a timezone-rule identity such as Asia/Riyadh are not interchangeable concepts. Where future rule changes affect meaning, the App Plan SHOULD use durable timezone semantics rather than relying solely on today's numeric offset, and MUST define how relevant rule changes are handled. No single storage representation or timezone database is prescribed. Where wall-clock correctness matters, account proportionately for skew, unsynchronized devices, source-provided timestamps, device clock changes, uncertain zones, and daylight-saving/rule changes; an OS timestamp is not automatically verified truth under [EVID-1](#evid-1).

Leases, retries, deadlines, expirations, synchronization, idempotency, and ordering MUST use time semantics appropriate to their correctness contracts. Distinguish wall-clock readings from monotonic elapsed-time measurement where conflation could break correctness; document relevant clock, restart, and cross-device assumptions. No one clock mechanism provides distributed ordering or stale-writer exclusion by itself; [CON-1](#con-1), [CON-2](#con-2), and [RETRY-1](#retry-1) continue to apply.

<a id="s09"></a>
## 9. Local and offline operation

<a id="offline-1"></a>
### OFFLINE-1 — Useful local operation by policy

**Type:** ECOSYSTEM POLICY | **Origin:** USER POLICY | **Applies:** capability design and network dependencies

Applications SHOULD maximize useful local operation where the domain permits it. They MUST define offline behavior per capability and avoid unrelated cloud dependencies disabling otherwise independent local access. Intentional departures need technical justification under [GOV-3](#gov-3).

Search services, email delivery, streaming, live collaboration, market access, and other remote-native capabilities may need connectivity. Intrinsic documented dependence is not a policy exception. Preserve useful drafts, cached content, or inspection where appropriate; do not imply uncached or remotely authoritative information is current or available.

<a id="offline-2"></a>
### OFFLINE-2 — Safe delayed execution

**Type:** CONDITIONAL | **Origin:** DERIVED ENGINEERING RULE | **Applies:** queued or offline operations

Queueing MUST have domain-safe freshness, expiry, cancellation, authorization, replay, and conflict semantics. Time-sensitive orders, physical commands, or door-unlock actions MUST NOT replay automatically merely because connectivity returns. A domain may reject offline writes, allocate rights in advance, or restrict operations to preserve shared invariants. Distinguish queued intent from completed remote action under [OUT-1](#out-1).

<a id="offline-3"></a>
### OFFLINE-3 — Device-local personal operation

**Type:** ECOSYSTEM POLICY | **Origin:** USER POLICY | **Applies:** personal applications with ordinary local capabilities

Each applicable personal application MUST remain usable locally on its supported devices. A permanent NAS, cloud service, or Internet connection MUST NOT be required for ordinary local capabilities unless the capability itself is inherently remote. Devices MAY maintain appropriate local working copies; loss of connectivity MUST NOT unnecessarily remove ordinary local functionality or access to locally held user data. Products MUST describe what is retained locally, what is available offline, and which operations require remote coordination. An appropriate working copy need not contain an entire huge media collection. Offline changes and reconnection remain subject to [OFFLINE-2](#offline-2) and [SYNC-1](#sync-1).

<a id="s10"></a>
## 10. Product platforms, portability, and visual assets

<a id="port-1"></a>
### PORT-1 — Avoid unnecessary platform lock-in

**Type:** ECOSYSTEM POLICY | **Origin:** USER POLICY | **Applies:** platform and deployment choices

Applications SHOULD preserve portable architecture where practical and MUST document architectural portability, source portability, buildability, tested support, and official support separately. Product targets follow the declared scopes in [PORT-3](#port-3); platform-specific departures use documented exceptions under [GOV-3](#gov-3). A build is not runtime evidence. CPU architectures, OS versions, browser versions, BSD, and NAS platforms are not automatically one support matrix for every product. Declare concrete supported configurations and evidence. NAS obligations follow [NAS-1](#nas-1).

<a id="port-2"></a>
### PORT-2 — Portable references and faithful content

**Type:** CONDITIONAL | **Origin:** DERIVED ENGINEERING RULE | **Applies:** filesystem references and portable/interchange data

Hardcoded developer-specific paths in portable logic MUST NOT become runtime assumptions. Absolute paths may legitimately be host bindings, user configuration, filesystem-tool inputs, or audit evidence. Where relocation is promised, references MUST have documented identity/resolution semantics and explicit rebinding for host resources.

Use runtime path APIs where appropriate. Claimed targets require consideration of case behavior, Unicode normalization, reserved names, permissions, links, and collisions. Case-sensitive comparison or a universal sanitizer does not solve these differences. Preserve original names, bytes, and line endings when identity, signatures, fidelity, or user intent requires it; transformations need defined semantics and collision handling.

Example: `attachments/doc1.pdf` can be relative when its base and escaping are specified. `file://attachments/doc1.pdf` places `attachments` in the URI authority; it is not an ordinary relative reference. Reversible mappings can avoid lossy sanitation.

<a id="port-3"></a>
### PORT-3 — Declared Product Platform Scope

**Type:** ECOSYSTEM POLICY | **Origin:** USER POLICY | **Applies:** application product scope and supported clients

Each application MUST declare its Product Platform Scope or scopes and its concrete support matrix under [PORT-1](#port-1). Scopes describe the product being offered; they do not require every CLI, library, or service to acquire a mobile or graphical interface. Platform-specific applications may receive documented exceptions under [GOV-3](#gov-3).

| Scope | Product targets |
|---|---|
| DESKTOP | Normal desktop/laptop products SHOULD support Windows, macOS, and Linux. Arch Linux, CachyOS, Ubuntu LTS, and Linux Mint — current stable Ubuntu-based release — are first-class tested Linux baselines for this scope. |
| MOBILE | Mobile products SHOULD normally support Android, iOS/iPhone, iPadOS/iPad, and Android tablets where applicable, with adaptive phone/tablet layouts under [UI-2](#ui-2). |
| UNIVERSAL DEVICE APPLICATION | The declared universal scope targets Windows, macOS, Linux, Android, iPhone/iOS, iPadOS, and applicable Android tablets. Its Linux targets include the desktop baselines. Web MAY additionally be included. |
| WEB | Supported modern browsers, with explicit versions/capabilities and evidence. Web support is distinct from native application support. |

Arch Linux and CachyOS are particularly important first-class Linux targets; Ubuntu LTS provides the mainstream stable baseline. Linux Mint's current stable Ubuntu-based release has the same first-class support expectations as every other named Linux baseline. Each named baseline MUST receive applicable installation/packaging, launch, updates where applicable, filesystem behavior, permissions, core-feature, and native/system-integration support, with relevant automated/manual validation. Products MUST identify tested versions or rolling-release snapshots and material environment assumptions; a declared target awaiting implementation/testing MUST be labeled accordingly rather than reported as verified support. Evidence remains proportional under [TEST-1](#test-1).

Passing Ubuntu or Linux Mint tests MUST NOT be represented as proof of compatibility with every other Linux distribution or as a substitute for validating the other named baselines. Other mainstream Linux distributions remain compatibility/best-effort targets where dependencies permit unless explicitly promoted to first-class support.

<a id="asset-1"></a>
### ASSET-1 — Genuine vector source artwork

**Type:** ECOSYSTEM POLICY | **Origin:** USER POLICY | **Applies:** application-owned visual assets, including web UI assets

Naturally vector-representable assets SHOULD use genuine SVG as their source format, including icons, logos, interface symbols, badges, simple illustrations, diagrams, and decorative vector artwork. When recreating a raster reference as a UI icon or another vector-representable asset, authors MUST reconstruct genuine vector geometry rather than embed PNG/JPEG content in an SVG wrapper and claim compliance. Appropriate structures include paths, shapes, gradients, masks, and vector text converted appropriately when needed.

Photographs, screenshots, scans, textures, camera images, complex photographic artwork, and other intrinsically raster content MAY remain raster in formats appropriate to the use case. They MUST NOT be converted into meaningless SVG merely to satisfy this policy. Required generated raster icon sizes and platform/store-specific containers are permitted; naturally vector artwork SHOULD retain vector source-of-truth artwork. Generated platform derivatives do not violate this policy.

<a id="asset-2"></a>
### ASSET-2 — Third-party brand fidelity

**Type:** ECOSYSTEM POLICY | **Origin:** USER POLICY | **Applies:** third-party trademarks and brand assets

Products MUST NOT inaccurately redraw third-party trademarks from screenshots. Where permitted, use official brand assets and follow applicable brand requirements. The application-owned SVG preference does not authorize inaccurate conversion or disregard of asset licensing or brand constraints.

<a id="asset-3"></a>
### ASSET-3 — SVG trust boundaries

**Type:** CONDITIONAL | **Origin:** USER POLICY | **Applies:** SVG acceptance, rendering, and application-owned SVG assets

Untrusted SVG MUST NOT automatically be treated as harmless image data. Applications accepting external SVG MUST handle script execution, remote resource access, and unsafe embedded content according to the actual renderer and trust boundary, using appropriate restrictions, sanitization, isolation, or rejection. Application-owned SVG SHOULD avoid unnecessary executable or external content. File extensions and SVG wrappers do not establish safety.

<a id="s11"></a>
## 11. NAS support

<a id="nas-1"></a>
### NAS-1 — Mandatory ecosystem support policy

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
### NAS-2 — Configuration-specific evidence

**Type:** CONDITIONAL | **Origin:** DERIVED ENGINEERING RULE | **Applies:** claimed NAS modes and network storage

Claims MUST identify engine, protocol, client/server, filesystem, and configuration assumptions with proportionate empirical evidence. Mode 4 MUST be supported only where the engine explicitly supports that configuration and the application's assumptions have been verified. Unsupported configurations MUST be rejected or clearly reported as unsupported, rather than silently accepted as safe.

SMB/NFS locking is configuration- and failure-dependent. Ordinary multi-process SQLite WAL coordination commonly relies on shared coordination mechanisms; shared-memory coordination does not describe every possible WAL configuration. This does not establish safe multi-host SQLite database access over SMB/NFS. Specialized configurations, including custom VFS behavior, require their own supported contract and evidence under Mode 4. A NAS-local database service is a different mode.

`fsync` and `FlushFileBuffers` offer the guarantees implemented by the complete storage stack; server acknowledgements, caches, hardware, and error propagation matter. Oplocks do not alone define stable-storage durability. Permissions depend on identities/ACLs; `0755` and `0644` are not universal privacy settings. Latency assumptions MUST be measured or bounded for the claimed workload, not copied from fixed illustrative numbers.

Access, quota, and free-space preflights improve diagnostics but cannot prove a future operation succeeds. Disconnects may leave outcomes unknown under [OUT-1](#out-1). Timestamp leases and heartbeats without stale-writer exclusion cannot establish safe overlapping access; coordination follows [CON-1](#con-1).

Possible patterns include NAS-local database services, supported transactional engines, ordinary files with bounded semantics, or immutable chunks with a publication protocol. Chunking is not mandatory and does not itself create a transaction.

<a id="s12"></a>
## 12. Storage and crash consistency

<a id="store-1"></a>
### STORE-1 — Explicit storage contracts

**Type:** CONDITIONAL | **Origin:** DERIVED ENGINEERING RULE | **Applies:** persistence backends

Each backend MUST document crash-consistency, acknowledgement, concurrency, and recovery contracts and supporting failure assumptions. Protect retained state against the interruptions the application claims to tolerate, and disclose limits instead of promising immunity to arbitrary hardware, software, or adversarial failures.

Visibility, atomicity, durability, replication, and external completion differ. Define consistency units and observers of intermediate state. Larger workflows may expose recoverable intermediate states rather than use one global transaction. Logical rollback need not restore every physical byte to an earlier layout.

Storage MUST fit workload, transaction, concurrency, and recovery needs; a product name is not evidence. Open text and documented binary formats are valid. Parquet is an open binary columnar format, not human-readable text.

<a id="store-2"></a>
### STORE-2 — Mechanisms follow the contract

**Type:** RECOMMENDATION | **Origin:** DERIVED ENGINEERING RULE | **Applies:** storage implementation choices

Implementations SHOULD use proven engine protocols where suitable. ACID transactions, copy-on-write, append logs, journals, transactional object stores, engine-native updates, and atomic replacement are possible mechanisms. No file algorithm is required for every write.

For a replaceable file on a backend with suitable semantics, an illustrative sequence is: create a unique temporary file on the required filesystem; serialize and check writes; synchronize as required; publish through a supported replace/rename operation; synchronize directory metadata where required; recover interrupted work. It also needs safe temporary-file creation, race protection, metadata/permission handling, and failure classification. Same-filesystem placement is not proof of full crash durability. Windows APIs, sharing modes, and filesystems need qualification; a replacement flag is not a universal guarantee.

Append stores and databases may use different protocols, including protected in-place page updates. An intent journal alone does not provide atomic multi-file behavior: durable ordering, commit markers, reader visibility, partial application, and recovery need a complete protocol.

<a id="s13"></a>
## 13. Concurrency and conflict semantics

<a id="con-1"></a>
### CON-1 — Prevent invalid interleavings

**Type:** CONDITIONAL | **Origin:** DERIVED ENGINEERING RULE | **Applies:** state reachable by concurrent actors/processes

Applications MUST prevent invalid interleavings according to declared consistency semantics. Enforced single-writer access is permitted. Exclusive-access assumptions MUST be enforced or explicitly bounded; a convention alone is not exclusion.

MVCC, serialized services, transactions, optimistic concurrency, CRDTs, append protocols, and storage-enforced fencing are possible mechanisms. Version/hash checks MUST be coupled to transitions when used to prevent races; check-then-write is insufficient. Lease designs MUST prevent stale holders violating promised semantics through storage-enforced fencing or an equivalent protocol, not just heartbeats.

Lock scope/deadlines depend on engine and workload; relational writes do not universally need exclusive database locks. Define cancellation, timeout, and starvation behavior where material to correctness or availability.

<a id="con-2"></a>
### CON-2 — Domain-appropriate conflict resolution

**Type:** CONDITIONAL | **Origin:** DERIVED ENGINEERING RULE | **Applies:** conflicting state changes

Resolution MUST preserve declared semantics and MUST NOT silently discard independently meaningful work contrary to them. Reject/retry, semantic merge, preserved alternatives, domain-approved last-writer-wins, or user decisions are options. A deterministic merge can still violate an invariant.

Lamport clocks order events consistently with causality but do not alone identify concurrency. Vector clocks track causal relationships under protocol assumptions. Hashes indicate content equality/difference, not independent causality. CRDTs provide specific convergence semantics, not arbitrary business-invariant preservation. These mechanisms are not interchangeable.

<a id="s14"></a>
## 14. Operation outcomes and acknowledgements

<a id="out-1"></a>
### OUT-1 — Report what is actually known

**Type:** UNIVERSAL INVARIANT | **Origin:** DERIVED ENGINEERING RULE | **Applies:** important local and external operation results

Results MUST distinguish relevant states: rejection, acceptance, queued intent, local application, local durable commit, remote acknowledgement, external completion, failure before execution, partial execution, or unknown outcome. Exact labels are optional. Acceptance MUST NOT imply completion; remote acknowledgement MUST NOT imply stronger durability/finality than its contract provides.

A timeout, crash, or NAS disconnect can leave success indeterminate. Applications MUST report uncertainty, retain suitable recovery correlation, and reconcile or use a demonstrably safe retry policy. Missing acknowledgement alone MUST NOT be reported as proof of failure. Relevant callers, including AI, need the actual durability/completion boundary.

Example result fields: operation ID, known phase, affected resources, durability scope, external correlation, uncertainty, and allowed next actions. A small utility may convey these semantics through exit status and a concise message.

<a id="ops-1"></a>
### OPS-1 — Operation identity and recovery receipts

**Type:** ECOSYSTEM POLICY | **Origin:** USER POLICY | **Applies:** consequential operations whose retry, boundary crossing, crash survival, or uncertainty requires effect correlation

Such operations SHOULD use a stable operation identity or equivalent correlation mechanism to distinguish retrying the same intended operation from a genuinely new operation. Pure local reads with no meaningful side effects do not require idempotency keys. Where identity is used for idempotency, the complete protocol in [RETRY-1](#retry-1) applies; an ID alone does not prevent all duplicates.

When recovery requires knowing what happened, the application MUST maintain durable evidence appropriate to the operation. A receipt may contain operation ID, normalized request identity/hash, result, affected object IDs, commit/reconciliation state, verification evidence, timestamps, and relevant actor/principal. No one format or permanent payload-retention rule is required. Receipts MAY reuse existing audit or execution records rather than duplicate them; required mutation/evidence coupling follows [AUDIT-2](#audit-2) and privacy follows [PRIV-1](#priv-1).

Receipts MUST distinguish observed results from unestablished external completion under [OUT-1](#out-1). Recording intent or a local commit cannot prove that a remote or physical effect occurred. Unknown outcomes require reconciliation or a demonstrably safe retry policy, not blind replay after a lost acknowledgement.

<a id="s15"></a>
## 15. Retries and deduplication

<a id="retry-1"></a>
### RETRY-1 — Replay safety is a protocol

**Type:** CONDITIONAL | **Origin:** DERIVED ENGINEERING RULE | **Applies:** retried, replayed, or redelivered operations

Contracts MUST distinguish idempotent transitions, request deduplication, replay-safe execution, ambiguous outcomes, and irreversible effects. A new retry identifier does not deduplicate an earlier request.

Key-based protocols MUST define principal/operation scope, persistence, concurrent requests, payload matching, retention, expiry, and result recovery. Reuse of the same operation identity for a materially different normalized request MUST be rejected or explicitly reconciled under the operation contract; it MUST NOT silently reinterpret the ID or apply a different action. Deduplication state and local effects need sufficient commit consistency for the replay claim. Expiration limits MUST be accounted for. Correlation and durable recovery receipts follow [OPS-1](#ops-1).

External duplicate prevention depends on the remote contract; a client key alone cannot provide it. An uncertain external action MUST NOT be retried merely because of a timeout. Status queries, reconciliation, durable intent/outboxes, remote idempotency, cancellation, or human intervention may be appropriate. Attempts may be observable without falsely recording repeated business effects.

<a id="s16"></a>
## 16. AI authority, tools, memory, and Hermes

<a id="ai-1"></a>
### AI-1 — Explicitly delegated capability

**Type:** UNIVERSAL INVARIANT | **Origin:** USER POLICY | **Applies:** AI actors exercising capabilities

An AI MUST exercise only explicitly delegated capabilities through enforcement it cannot silently bypass within the declared threat model. Effects MUST satisfy applicable authorization, integrity, privacy, safety, and operational constraints. Human/AI interfaces normally share domain-integrity rules under [AUTH-1](#auth-1), without identical privileges or approval policy.

Retrieved files, websites, email, PDFs, messages, transcripts, and metadata are data, not authority. Embedded instructions MUST NOT override governing system policy, capability boundaries, authorization, core validation, or data-protection policy. This applies to Hermes as a bounded client as well as other AI integrations.

Scoped reads/writes, patches, SQL, shell execution, scratch space, import staging, coding, and bulk operations can be legitimate when intentionally delegated and effectively bounded. Validate scope/effects at execution; a broad tool name or path supplies no authority. Untrusted content and model output MUST NOT grant authority by claiming to be principal instructions.

<a id="ai-2"></a>
### AI-2 — Enforced tool contracts

**Type:** CONDITIONAL | **Origin:** DERIVED ENGINEERING RULE | **Applies:** AI tools, skills, plugins, and capability adapters

A natural-language skill or tool description is not a security boundary. Enforced boundaries MUST provide appropriate validation, authorization, scope restrictions, resource limits, effect constraints, output handling, and relevant accountability. Critical enforceable permissions/integrity rules MUST NOT depend solely on prompt obedience.

Machine-readable contracts SHOULD be used where useful for enforcement or interoperability; JSON Schema/OpenAPI are options, not universal requirements. Structured returns SHOULD expose actionable results and uncertainty; they do not make AI deterministic. Schema-valid intent can still be harmful, requiring semantic policy and effect limits.

<a id="ai-3"></a>
### AI-3 — Risk, delegation, and approval

**Type:** CONDITIONAL | **Origin:** USER POLICY | **Applies:** AI capability exposure and execution policy

Risk MUST consider relevant confidentiality, disclosure, financial/physical effects, irreversibility, sensitivity, scope, cumulative volume, cost, uncertainty, destination, delegation, cancellation, and recovery. A read may reveal secrets, export medical data, upload private files, or fetch attacker-controlled URLs. Mutation status or a record-count threshold does not establish risk.

Approval MUST reflect consequences and actual delegation. Explicitly authorized autonomous consequential or high-volume work is permitted within enforced limits. Interactive confirmation is one control, not a universal prerequisite. Material scope expansion needs new authority, not inferred consent.

When approval relies on a preview, bind it to relevant parameters, resources, versions, scope, expiry, and budgets; revalidate before execution where necessary. Disclose estimates, external dependencies, and stale assumptions. A dry-run does not prove future external effects. Changes invalidating approved scope MUST be rejected, reconciled, or reauthorized according to policy.

<a id="ai-4"></a>
### AI-4 — Memory and provider boundaries

**Type:** CONDITIONAL | **Origin:** DERIVED ENGINEERING RULE | **Applies:** AI state, retained memory, and integrations

Domain consistency MUST NOT depend solely on hidden model memory or ephemeral context. Explicit state follows [DATA-1](#data-1); scratch work need not become permanent history. Retained AI memory MUST have defined inspection, correction, export, access, deletion, and derived-copy lifecycle controls consistent with principals' rights. It MUST NOT silently override authoritative records or policy.

Provider integrations SHOULD isolate replaceable dependencies where useful and declare capabilities. Abstraction reduces coupling, not differences in model quality, interfaces, cost, licensing, or availability. Provider-specific tools may intentionally use unique capabilities. Optional AI failure SHOULD preserve independent functions; AI-native functions may become unavailable with truthful results. Protect retained data and contain failure within stated assumptions rather than promising immunity to all crashes or resource exhaustion.

<a id="hermes-1"></a>
### HERMES-1 — Optional, bounded intelligence

**Type:** ECOSYSTEM POLICY | **Origin:** USER POLICY | **Applies:** applications integrating Hermes

Hermes MUST remain an optional intelligence layer rather than the sole means of using the application. Core application behavior MUST work without Hermes. Hermes MUST NOT receive unrestricted raw authority over canonical state; canonical writes MUST pass through validated, authorized application operations under [AUTH-1](#auth-1) and [AI-1](#ai-1). Hermes SHOULD be able to operate locally where the relevant data and model are available. Optional Hermes capabilities do not redefine unrelated AI-native functions in [AI-4](#ai-4) as ordinary core functionality.

Approved application/core operations MUST enforce applicable deterministic validation and bounded authority; model-generated intent supplies neither approval nor validation. Retrieval MUST respect access scope and privacy; provenance and audit follow [AUDIT-1](#audit-1), [AUDIT-2](#audit-2), and [PRIV-1](#priv-1).

Hermes import/processing of untrusted file content MUST use the same deterministic intake/security gates as native UI operations under [IO-2](#io-2) and [IO-3](#io-3). Model size or provider grants no bypass of required malware checks, quarantine, or core validation.

Canonical data MUST NOT exist solely inside an opaque AI memory/vector database with no independent application access and preservation path. This concerns opacity and sole dependence on the intelligence layer, not a blanket ban on vector storage technology: authoritative originals may use such a backend under [DATA-1](#data-1), [LIFE-2](#life-2), and applicable storage/export contracts.

Hermes embeddings, vector stores, semantic indexes, generated summaries, and retrieval caches are normally navigation aids. They SHOULD be reconstructable from retained sources and appropriate deterministic metadata under the actual [DATA-2](#data-2) reproduction contract, without assuming bit-for-bit regeneration of nondeterministic summaries. They MUST NOT silently become the sole repository of irreplaceable information. An explicit, justified authoritative classification is permitted under [DATA-1](#data-1), with independent access, retention, and recovery obligations; it does not excuse opaque model-only preservation.

<a id="hermes-2"></a>
### HERMES-2 — Structured, bounded small-model retrieval

**Type:** ECOSYSTEM POLICY | **Origin:** USER POLICY | **Applies:** information architecture and retrieval interfaces for Hermes or other AI clients

Information architecture and AI retrieval interfaces MUST provide structured, scoped discovery and bounded context rather than uncontrolled workspace wandering or reliance on loading entire huge workspaces into a model. The logical flow is **user intent → capability discovery → structured query → catalog/index/core → stable ID → exact object → precise anchor where meaningful → bounded context**. Equivalent mechanisms are allowed. The application/core SHOULD perform as much deterministic narrowing as practical through IDs, aliases, catalogs, typed filters, relationships, bounded search, anchors, candidate lists, and structured errors.

Normal retrieval MUST NOT require the language model to recursively scan the entire user-data tree to answer ordinary queries. Authorized deterministic maintenance or index construction may traverse the corpus; that is distinct from the bounded result consumed by the model. Enforce relevant scope, authorization, and privacy during retrieval and context assembly. Rebuild claims follow [DATA-2](#data-2).

Where Hermes/local AI is part of the product, interfaces MUST be designed and tested assuming a suitably capable constrained local model before relying on a powerful cloud model. Approximately 1B-class models are an engineering target where realistic, not a guarantee of flawless behavior or a universal parameter-count threshold. Record tested capabilities and limits under [TEST-1](#test-1). Cloud clients may provide better reasoning but MUST use the same authority model without hidden architectural privileges.

The **Hermes / User-Adaptable File Structure Blueprint is integrated as CANDIDATE policy**, together with [section 32](#s32). It standardizes discoverability and integrity while leaving user-facing organization domain-appropriate and adaptable. This product-use goal is distinct from the full-app development continuity goal in [DEV-11](#dev-11).

<a id="hermes-3"></a>
### HERMES-3 — Core resolution, ambiguity, and actionable failures

**Type:** ECOSYSTEM POLICY | **Origin:** USER POLICY | **Applies:** AI-facing lookup and application-operation interfaces

AI MAY express intent using names, aliases, search terms, friendly references, or previously resolved identifiers. The deterministic application/core MUST resolve or validate authoritative identity, exact location/path, and mutation semantics. Model-generated text MUST NOT by itself create authoritative IDs, canonical paths, or hidden persistence structures. Authorized create/import operations may assign or validate identities according to the product contract; this rule does not forbid delegated coding or scratch work under [AI-1](#ai-1).

When a friendly reference has multiple plausible matches and the contract does not uniquely resolve it, tools MUST return scoped candidates and relevant distinguishing information, indicating that clarification is required. They MUST NOT silently choose the first match or require the AI to invent an ID. Candidate disclosure remains subject to access/privacy controls; excessive result sets may be bounded and narrowed.

Failures SHOULD expose deterministic, actionable information where practical: what failed and why, whether anything changed or remains unknown, relevant object/operation IDs, candidates, a safe next action, and whether user input is required. A raw stack trace alone SHOULD NOT be the ordinary continuation contract. Outcomes remain truthful under [OUT-1](#out-1); structured errors do not grant additional authority or guarantee AI obedience.

<a id="s17"></a>
## 17. Audit and provenance

<a id="audit-1"></a>
### AUDIT-1 — Proportionate accountable evidence

**Type:** CONDITIONAL | **Origin:** DERIVED ENGINEERING RULE | **Applies:** operations requiring accountability under domain, policy, or applicable obligations

Applications MUST define required events and an audit contract covering granularity, principal/actor/mechanism, outcome, resources, necessary before/after information, retention, access, redaction, archival, deletion, integrity, and recovery. Evidence MUST support the claim without indiscriminate payload capture. Relevant failures/unknown outcomes MUST be distinguishable from successful effects.

Bulk events may reference an affected set; micro-events may be aggregated if accountability is retained. Model identities may be unknown/provider-reported. Human review records its actual scope. Prompts and free-text reasons need privacy treatment and are not mandatory permanent payloads. Rollback identifiers SHOULD be references rather than enduring bearer authority.

Diagnostics and audit evidence have distinct purposes/lifecycles, without mandatory separate directories. Ordinary correction/reversal should retain its relation to earlier events. Authorized expiry/redaction follows [PRIV-1](#priv-1); append-only semantics do not forbid it.

<a id="audit-2"></a>
### AUDIT-2 — Mutation and evidence commit consistency

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
### AUDIT-3 — Integrity claims and trust anchors

**Type:** CONDITIONAL | **Origin:** DERIVED ENGINEERING RULE | **Applies:** claims of tamper evidence

Claims MUST identify adversaries, protected references, verification, and recovery limits. Hashes detect changes relative to trusted references; attackers able to replace data and manifests can defeat comparison. Hash chains need protected anchors or independent evidence against wholesale rewriting. Encryption does not itself establish authorization or audit completeness. Authorized redaction/expiry MUST be distinguishable from unexplained alteration within the stated integrity model.

<a id="evid-1"></a>
### EVID-1 — Provenance, evidence status, and uncertainty

**Type:** ECOSYSTEM POLICY | **Origin:** USER POLICY | **Applies:** imported/observed information and research whose provenance or evidence strength materially affects decisions or meaning

Relevant provenance MUST be retained proportionately: source/identifier/version, acquisition or import method, observation time, importer/tool, human modification, and verification scope where meaningful. Successful import, a credible source, or canonical designation MUST NOT silently upgrade an observation into verified factual truth; [DATA-1](#data-1) keeps those dimensions distinct.

Applications and planning records MUST represent evidence strength equivalent to **VERIFIED**, **INFERRED / CONDITIONAL**, and **UNKNOWN** where it affects decisions. Verification identifies its actual scope and supporting evidence. Research, compatibility, external integrations, migrations, planning assumptions, and source observations MUST NOT become architectural facts through repetition alone. Meaningful uncertainty MUST remain representable, including known, unknown, unavailable, ambiguous, unverified, stale, conflicting, and pending-review states as applicable; one universal enumeration is not required. This complements operation uncertainty under [OUT-1](#out-1).

When credible sources conflict, preserve sufficient competing evidence, provenance, uncertainty, and review state rather than silently choosing a winner. Automatic resolution requires an explicit deterministic, justified rule; otherwise retain an unresolved interpretation or obtain authorized review. Evidence retention is purpose-limited under [PRIV-1](#priv-1), not a mandate to keep all original sensitive payloads forever.

An upstream source changing or deleting its copy MUST NOT automatically destroy locally retained evidence or user data. Represent removed-upstream, unavailable, superseded/new-version, stale, or tombstone status as appropriate. Actual deletion follows the applicable retention, privacy, authority, and synchronization contract; legitimate erasure and agreed deletion propagation remain enforceable.

<a id="s18"></a>
## 18. Privacy, retention, and deletion

<a id="priv-1"></a>
### PRIV-1 — Purpose-limited processing and retention

**Type:** UNIVERSAL INVARIANT | **Origin:** DERIVED ENGINEERING RULE | **Applies:** sensitive/personal information collection, processing, disclosure, retention

Processing and retention MUST be limited to authorized purposes and applicable obligations. Audit, provenance, prompts, diagnostics, before/after state, model metadata, backups, and derived copies are included. Full prompts, secrets, personal information, and deleted payloads MUST NOT be retained merely because available.

Deletion/retention policies MUST define scope, timing, protected obligations, replicas, indexes, backups, and known limitations. Logical append-only history may coexist with authorized redaction, expiry, archival, key destruction, and cryptographic erasure. Preserve necessary evidence of lifecycle actions without recreating erased payloads. Restore MUST account for applicable deletion decisions rather than silently reinstating information contrary to policy.

Cryptographic erasure depends on effective key destruction and copies; it cannot recall disclosed plaintext. Soft deletion is not a universal substitute for erasure. Resolve conflicting rights and retention obligations through [SAFE-2](#safe-2) with a documented legitimate basis.

<a id="priv-2"></a>
### PRIV-2 — Local data and deliberate disclosure

**Type:** ECOSYSTEM POLICY | **Origin:** USER POLICY | **Applies:** user-data storage and external transmission

Local machine/private NAS storage is the default. External disclosure MUST have informed authorization appropriate to purpose, destination, data scope, and principal. Standing delegation is permitted without per-request prompts. Remote-native functions follow [OFFLINE-1](#offline-1). Cloud AI requests SHOULD include only necessary relevant context. Local inference MAY help but does not prove other components transmit nothing. Diagnostic exports need sanitization and user control without mandatory manual inspection of every byte.

<a id="s19"></a>
## 19. External editing and drift

<a id="edit-1"></a>
### EDIT-1 — User control and safe adoption

**Type:** CONDITIONAL | **Origin:** USER POLICY | **Applies:** managed files/records accessible outside the ordinary runtime

Users may edit their own Markdown, source, configuration, documents, and open formats subject to legitimate shared rights. Applications MUST define supported edits, validation, adoption, conflicts, and rejection. They MUST NOT silently adopt unsafe state merely because it is in an expected directory. Unsupported edits may be rejected/quarantined without claiming ownership over user files. Reconciliation MUST avoid overwriting newer valid work or destroying the only recoverable copy without authority.

<a id="edit-2"></a>
### EDIT-2 — Proportionate drift detection

**Type:** CONDITIONAL | **Origin:** DERIVED ENGINEERING RULE | **Applies:** storage models where external change affects claimed integrity

Detection MUST fit threats, dataset size, architecture, and acceptable latency. Hashes, versions, watcher hints, database versioning, service boundaries, snapshots, or reconciliation protocols are options; constant all-file hashing is not required. Watchers can miss changes and need validation/rescan strategies where the contract requires it.

Drift does not prove maliciousness or authorship. Snapshots can roll back data and a local manifest together; detection of that rollback needs evidence outside the boundary. Adoption, restoration, merge, preserved alternatives, and user decisions are possible resolutions subject to current-state coordination under [CON-1](#con-1).

<a id="s20"></a>
## 20. Synchronization

<a id="sync-1"></a>
### SYNC-1 — Explicit distributed authority

**Type:** CONDITIONAL | **Origin:** DERIVED ENGINEERING RULE | **Applies:** synchronization or replicas of a logical dataset

Protocols MUST define authority, identity, causal/conflict semantics, disconnected changes, duplicate handling, deletion propagation, and recovery. Peer data MUST pass applicable authority/integrity controls; sync is not a bypass. Preserve origin and propagation identity where needed for accountability.

Offline availability is constrained by invariants: scarce resources may need online coordination or preallocated rights. Convergence is not proof of correctness. Tombstone retention, long-offline replicas, and reintroduction of erased information need explicit lifecycle semantics. Conflicts follow [CON-2](#con-2); delay follows [OFFLINE-2](#offline-2).

Applications synchronizing large retained datasets MUST define a risk-based policy for destructive or anomalous bulk-change propagation; a locally observed change is not automatically legitimate user intent. Consider mass rewrites, renames/deletions, unexpected encrypted/high-entropy replacements, unexplained bursts, and broad schema-invalidating changes where relevant. These signals are not proof of malware. Proportionate responses may pause propagation, stage/quarantine, reconcile, preserve permitted prior versions, or alert; no universal numeric threshold or fresh prompt for every bulk operation is required.

Where suspected compromise could propagate damage, the system MUST provide an appropriate containment route, such as sync pause, device revocation, replica isolation, read-only operation, connector disablement, or staged-import quarantine. Resume automatic propagation only after applicable validation/reconciliation under [RECOVER-1](#recover-1). Authorized bulk work and legitimate deletion/erasure remain supported under [AUTH-2](#auth-2) and [PRIV-1](#priv-1); containment is not indefinite retention authority.

<a id="sync-2"></a>
### SYNC-2 — Device continuity without a NAS

**Type:** ECOSYSTEM POLICY | **Origin:** USER POLICY | **Applies:** personal products requiring cross-device continuity

Without a NAS, supported laptops, desktops, phones, and tablets MUST retain applicable local operation under [OFFLINE-3](#offline-3). Such products MUST support direct device synchronization or another explicitly selected local-first synchronization mechanism, for example Phone ↔ Laptop or Phone ↔ Laptop ↔ Tablet. A permanent central cloud server MUST NOT be required merely to synchronize the user's own devices. Optional selected intermediaries remain subject to declared dependencies, privacy, and authorization. Conflicts, offline changes, unknown outcomes, integrity, retries, and recovery follow [SYNC-1](#sync-1), [OUT-1](#out-1), and [RETRY-1](#retry-1).

<a id="sync-3"></a>
### SYNC-3 — Opt-in NAS synchronization hub

**Type:** ECOSYSTEM POLICY | **Origin:** USER POLICY | **Applies:** applicable personal products with a suitable NAS enabled by the user for shared synchronization

When a suitable NAS is available and the user enables this role, it MUST become the primary shared synchronization hub for application data. All applicable retained/shared data SHOULD synchronize to it according to the declared data scope, permissions, retention, and synchronization contract. Desktop, mobile, and tablet instances act as clients of that shared system while retaining appropriate local working copies. This policy does not silently upload data excluded by user scope, authority, or privacy rules.

The NAS MUST NOT become a hard requirement for ordinary offline work. Temporary disconnection MUST preserve applicable local operation; reconnection MUST synchronize and reconcile according to the declared consistency model and current authority. Primary hub placement does not by itself transfer ownership or make every local write a globally final commit. Distinguish local persistence, hub acknowledgement, and reconciliation under [OUT-1](#out-1). NAS storage/service, backup, and hosting roles remain distinct under [NAS-1](#nas-1).

<a id="sync-4"></a>
### SYNC-4 — Safe topology transitions

**Type:** ECOSYSTEM POLICY | **Origin:** USER POLICY | **Applies:** applicable products transitioning between device-local/peer operation and a NAS synchronization hub

Products SHOULD support safe transitions between no-NAS local or peer operation and an enabled NAS hub. Adding a NAS MUST NOT require destructive migration or recreation of all user data. Removing or temporarily losing the NAS MUST NOT make the user's locally held data inaccessible. Appropriate working copies and documented availability still apply; a client cannot promise offline access to content it has never retained.

Authority transitions MUST define identity continuity, reconciliation of concurrent/offline changes, deletion handling, pending or unknown operations, and which participants may accept changes during and after the transition. Removing a hub deliberately MUST provide a preservation/transfer path for retained data needed by the chosen replacement topology; failures MUST report remaining unavailable data truthfully. Existing synchronization, migration, recovery, and authorization contracts apply. These are outcome requirements, not a mandated peer protocol, conflict algorithm, or central-cloud dependency.

<a id="s21"></a>
## 21. Reversal and recovery

<a id="recover-1"></a>
### RECOVER-1 — Honest recovery semantics

**Type:** UNIVERSAL INVARIANT | **Origin:** DERIVED ENGINEERING RULE | **Applies:** undo, restoration, reversal, or compensation claims and recovery of important retained user state

Applications MUST describe actual recovery/compensation honestly and provide recovery where technically and operationally appropriate. Distinguish inverse mutation, transaction rollback, restoration, compensation, cancellation, reconciliation, and irreversible actions. Reversal MUST use current authority and constraints, not historical permission alone.

Communications cannot be recalled from recipients' knowledge. Refunds are separate effects; physical actions may be irreversible; APIs may need reconciliation. Restoring old global state MUST NOT be presented as safe undo without accounting for newer valid work. Expired/erased information may not be recoverable. Required reversal audit links to the original under [AUDIT-1](#audit-1).

For applications owning important retained user state, successful normal application startup MUST NOT be the only route to inspect, verify, extract, or recover otherwise recoverable information. Define an appropriate recovery route and its dependencies/limits in the App Plan, supported by proportionate evidence under [BACKUP-2](#backup-2) and [TEST-1](#test-1). A read-only recovery mode, independent reader, doctor tool, recovery executable, or documented portable inspection/export procedure may suffice. Neither a CLI nor a separate rescue application is required where the durable format already provides an adequate route. Recovery MUST preserve applicable authorization, privacy, and key-access constraints under [AUTH-1](#auth-1), [PRIV-1](#priv-1), and [BACKUP-1](#backup-1).

Recovery MUST distinguish corruption detection/diagnosis, derived-state rebuilding, verified canonical restoration, and canonical repair. It MUST NOT fabricate missing facts to claim a healthy state. When facts cannot be established, preserve uncertainty under [EVID-1](#evid-1), surface the problem, quarantine where appropriate, and stop destructive repair; [SAFE-1](#safe-1), [DATA-2](#data-2), and [EDIT-1](#edit-1) remain governing constraints.

Malware/ransomware recovery SHOULD, where applicable, contain affected clients/services, stop unsafe propagation, identify the best evidenced known-good canonical state/recovery points, validate backup integrity, restore or reconstruct canonical information, rebuild disposable derived state, reconcile legitimate newer information where safe, and rotate/revoke compromised credentials before validated sync resumption. Recovery MUST NOT overwrite the best surviving clean evidence merely for convenience. Recovery copies may themselves be corrupted, malicious, or already compromised; age or immutability does not establish cleanliness. Evidence and uncertainty follow [BACKUP-2](#backup-2) and [EVID-1](#evid-1), with privacy/deletion duties intact.

<a id="recover-2"></a>
### RECOVER-2 — Prefer bounded reversibility

**Type:** DEFAULT | **Origin:** ARCHITECTURAL DECISION | **Applies:** mutations and consequential automation

Operations SHOULD offer scoped undo, reversible preparation, cancellation, or compensation where benefit justifies cost. Soft deletion may help; retention/privacy may require erasure. Communicate irreversible boundaries where relevant. Delegation can authorize automatic execution under [AUTH-2](#auth-2) and [AI-3](#ai-3) without repeated confirmation.

For retained user-owned data, destructive deletion SHOULD normally include a reversible stage where practical before permanent purge. Trash or pending-deletion state is one pattern, not a required directory. Explicit secure deletion, privacy/legal erasure, ephemeral/cache/temp data, safety/security needs, and other justified cases may require a different lifecycle. No indefinite retention is implied; [PRIV-1](#priv-1) and [SAFE-2](#safe-2) govern conflicting obligations.

<a id="s22"></a>
## 22. Backup and restoration

<a id="backup-1"></a>
### BACKUP-1 — Complete recovery dependency set

**Type:** CONDITIONAL | **Origin:** DERIVED ENGINEERING RULE | **Applies:** retained state with provided/claimed backup or recovery

Strategies MUST identify a consistent recovery point and complete dependency set for the promised result: potentially data, configuration, keys/key-recovery paths, audit evidence, schemas, readers, migration metadata, expensive derived artifacts, and external dependencies. Secrets need protection and recoverability, not indiscriminate packaging with public exports.

No directory inclusion list or derived-data exclusion applies universally. NAS/filesystem snapshots, OS backup, database-native, or application-native backup may be used. Understand snapshot scope and cross-store consistency. A copy in the same failure domain does not establish independent recovery.

For important retained data, the backup strategy MUST distinguish active copies, synchronized replicas, NAS hubs, snapshot/version history, and backups, and consider a recovery copy not simultaneously destroyable through the same ordinary client credentials or failure mechanism. Document the chosen protection and residual risk proportionately. Immutable/write-protected history, offline/disconnected media, separately credentialed storage, append/versioned backup, or another justified isolation mechanism may fit; no topology is universally required. Ordinary client credentials SHOULD NOT automatically have unrestricted deletion authority over all independent backup generations unless genuinely required; separate retention/deletion authority where meaningful. Isolation does not override authorized erasure under [PRIV-1](#priv-1).

<a id="backup-2"></a>
### BACKUP-2 — Recovery evidence

**Type:** CONDITIONAL | **Origin:** DERIVED ENGINEERING RULE | **Applies:** backup-readiness and recoverability claims

Claims MUST have documented, testable restoration and supporting evidence. Verify intended results, keys/dependencies, compatibility, and meaningful failure cases. Untested backups are unverified, not necessarily empty or legally nonexistent. State recovery-point/time expectations and untested limits.

Manifests/checksums can detect accidental corruption; adversaries may require protected evidence under [AUDIT-3](#audit-3). Verification SHOULD avoid active-data changes and restore tests SHOULD use safe destinations. Actual restore requires authority and accounting for later work/deletion policy.

For important retained data, restoration or equivalent recoverability MUST be validated at a proportionate cadence defined in the App Plan. A successful backup write alone is insufficient. Test/sample restores, isolated rehearsals, integrity/dependency verification, or another justified method must support the actual recovery claim; checksums alone do not establish that an application can use the restored state. Assess possible corruption, malicious content, and already-compromised backup state, using evidence to select the best available known-good recovery point and preserving uncertainty when cleanliness cannot be established. Older or immutable does not automatically mean clean; [RECOVER-1](#recover-1) governs safe recovery.

<a id="s23"></a>
## 23. Import and export

<a id="io-1"></a>
### IO-1 — Controlled ingestion and faithful export

**Type:** CONDITIONAL | **Origin:** DERIVED ENGINEERING RULE | **Applies:** import/export capabilities

Imports MUST validate format/domain constraints, define identity/conflicts, and prevent blind overwrite contrary to intent. Staging, skip, audited replacement, merge, or alternatives may be used. Track needed provenance without unrelated sensitive content.

Externally supplied data MUST be treated as untrusted until processed according to the application's risk model. This includes applicable downloads, email attachments, documents/media, archives, office files, plugin packages, NAS content, sync peers, APIs, and removable media. Controls may include format/type/magic validation, safe-path/traversal checks, archive-depth/expansion and decompression-bomb limits, size/resource limits, active-content restrictions, staging/quarantine, scanning, and restricted parsing under [SEC-1](#sec-1). Harmless bounded values need no expensive scanning without meaningful benefit. Parsing success or location in a data tree does not grant execution trust. Locale/time interpretation follows [DATA-4](#data-4) and [DATA-5](#data-5).

Controlled intake SHOULD provide risk-appropriate inspection/staging, validation using the relevant controls above, duplicate/identity/provenance resolution, commit, and operation receipts where needed. These are applicable safeguards, not mandatory heavyweight quarantine or a fixed physical pipeline for every tiny input.

For externally supplied files, [IO-2](#io-2) defines the preferred logical Raw/Intake boundary; [IO-3](#io-3) governs applicable malware-verification state and [SEC-6](#sec-6) the replaceable local scanning capability.

Exports presented as copies MUST NOT silently mutate/delete sources. An intentional move or export-and-delete needs separate effect semantics and authority. Exports MUST document scope, omissions, transformations, consistency point, and format, distinguishing archival fidelity from presentation. Apply [PRIV-1](#priv-1).

A portable-exit claim MUST preserve the declared meaning, not merely copy bytes: applicable stable IDs, relationships, metadata, provenance, originals, annotations, history, and schema definitions may be needed. Disclose what the target format cannot represent; silently dropping meaning MUST NOT be called lossless export. An ordinary export is an output snapshot, not a new write authority. Editing it does not mutate canonical state without an explicit validated re-import/adoption operation under [EDIT-1](#edit-1).

Canonical snapshots, human-readable reports, interchange formats, and diagnostics are useful categories, not four required features. JSON, Markdown, CSV, documented databases, and open binary formats serve different purposes. Scheduled export is optional unless the selected preservation contract relies on it.

<a id="io-2"></a>
### IO-2 — Untrusted Raw intake, promotion, and quarantine

**Type:** ECOSYSTEM POLICY | **Origin:** USER POLICY | **Applies:** applications ingesting, receiving, downloading, synchronizing, or otherwise accepting externally supplied file-like content

Such applications SHOULD expose a dedicated logical Raw/Intake/Staging area; `Raw/` is the preferred human-readable name where it fits the design. The boundary may be a directory, managed store, or equivalent logical state; no universal physical name or hierarchy is required. Content entering it MUST initially be untrusted regardless of location inside application-owned data. File-ingesting applications SHOULD prefer this boundary together with the local malware-intake pipeline in [IO-3](#io-3) and [SEC-6](#sec-6), proportionate to actual protection benefit. Applications without relevant file intake need no empty Raw directory, scanner, quarantine UI, or signature infrastructure.

Before promotion to ordinary managed/canonical content or risky normal processing, the required configured intake policy MUST succeed. Define relevant gates explicitly: malware verification, format/security validation, identity/provenance resolution, core validation, and authorized adoption under [IO-1](#io-1) and [AUTH-1](#auth-1). Not every input needs every step; isolated intake analysis is distinct from ordinary trusted processing. Pending, failed, stale, or unavailable verification MUST NOT silently satisfy a required gate. Bind promotion to the actual verified content/version and current applicable policy; intervening changes invalidate unsupported verdict reuse under [CON-1](#con-1).

A scanner detection alone MUST NOT automatically destroy retained source content. Quarantine/isolation SHOULD be the default response. Quarantined objects MUST NOT execute, receive ordinary trusted parsing, be automatically promoted, or be represented as clean canonical content. Authorized inspection/recovery may remain available through appropriate restricted mechanisms. Permanent deletion requires explicit policy/user authority or applicable security/privacy obligations under [PRIV-1](#priv-1) and [SAFE-2](#safe-2). A folder named `Quarantine/` is not sufficient isolation: the App Plan MUST choose risk-appropriate controls such as restricted access, non-executable storage, exclusion from normal import paths, renamed/encapsulated representation, or isolated storage.

Promotion need not delete the Raw original. Retained originals may support evidence, provenance, reproduction, or recovery under [DATA-3](#data-3), but remain subject to untrusted-content handling and retention/privacy policy. A derived canonical record does not authorize executing or reinterpreting its original, and canonical authority does not mean malware safety under [DATA-1](#data-1).

<a id="io-3"></a>
### IO-3 — Incremental malware verification and visible scan state

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
### MIGRATE-1 — Versioned, recoverable evolution

**Type:** CONDITIONAL | **Origin:** DERIVED ENGINEERING RULE | **Applies:** persistent format/schema evolution

Migrations MUST be explicit, versioned, and testable with defined dependencies/order, preconditions, interruption, and recovery. Define exclusive versus online execution, compatibility windows, concurrent writers, rollback/roll-forward, snapshot role, restoration boundary, and failure classification. Resource preflights cannot prove future allocation succeeds.

Consistent snapshots/backups are useful safeguards; a local full copy is not required for every migration. Failure MUST NOT cause unconditional snapshot restoration. Determine whether rollback succeeded, work remains partial, newer writes exist, or forward recovery is needed. Restoration requires authority over the real loss boundary. Restricted/read-only operation may be appropriate during recovery.

Retry safety may come from idempotent steps or a correctly recorded execution protocol. Safe downgrade may be unavailable; do not invent a non-destructive `down()` when information has been lost.

<a id="migrate-2"></a>
### MIGRATE-2 — Semantic compatibility

**Type:** CONDITIONAL | **Origin:** DERIVED ENGINEERING RULE | **Applies:** evolving persistent formats and protocols

Compatibility MUST be explicit. Unknown fields/new semantics MUST NOT be silently accepted then destroyed or misinterpreted. Define readable, preservable, transformable, and writable versions; reject unsafe writes or require supported migration. Liberal acceptance is not a blanket persistence rule. Tolerant reading may work when content is preserved safely and constraints remain understood.

An older application MUST NOT silently write or downgrade a newer data/workspace format it does not understand. If safe compatibility cannot be established, use a supported read-only, export-only, migration-required, or refusal mode as appropriate; do not offer even read/export behavior as faithful unless its contract can be met. Unknown newer fields MUST NOT be silently discarded.

<a id="s25"></a>
## 25. Security, secrets, and dependencies

<a id="sec-1"></a>
### SEC-1 — Threat-based boundaries and exposure

**Type:** CONDITIONAL | **Origin:** DERIVED ENGINEERING RULE | **Applies:** resources exposed to actors or networks

Controls MUST reflect principals, reachable surfaces, protocols, deployment, and threats, including relevant local processes, supply-chain inputs, network devices, and prompt injection. Localhost, LAN, or VPN membership alone does not establish application identity/authority. Least privilege means minimum effective authority for the role; backup/credential workers can need broad controlled access.

Local apps SHOULD bind local services to loopback by default. Network services may use intended interfaces, including containers, with explicit secure deployment. Authentication, authorization, transport protection, browser-origin defenses, and rate limits MUST match exposed operations/data. Deliberately public data may have public access semantics; private LAN location does not justify sensitive unauthenticated access. CORS/WAFs are not universal protocol controls; CORS is not general authorization.

Where relevant, the threat model MUST address malware/ransomware, malicious imports/archives/external content, compromised parsers/plugins/updates/dependencies, and unauthorized local processes through defense in depth. Antivirus/endpoint protection may contribute but is not the whole contract. High-risk parsing, previewing, extraction, conversion, transcoding, and rendering SHOULD run with the minimum authority reasonably required, using process isolation, sandboxing, restricted filesystem views, reduced privileges, bounded network access, resource limits, or disposable working space where technically practical. Processing one object SHOULD NOT automatically expose the entire archive, backups, secrets/credentials, NAS administration, arbitrary network services, or unrelated data.

Substantial retained-data applications MUST assess and limit unnecessary compromise propagation from a client, parser, optional subsystem, plugin, or AI tool to all data, replicas, NAS history, backups, and secrets. Use the existing capability model under [AUTH-1](#auth-1): an indexer needs no unrelated remote-write authority, a media parser needs no backup-deletion rights, and ordinary UI/sync need no automatic destructive backup-management or NAS-admin privilege. Presence inside a retained-data tree MUST NOT make content trusted executable code. Distinguish data from executable extensions; scripts/macros/binaries discovered as ordinary data MUST NOT execute merely because of location. Executable extensions require an explicitly trusted installation/activation process or equivalent authority boundary.

Document trust assumptions and residual risk: controls reduce likelihood and blast radius; they do not guarantee virus-proof software, malware-free snapshots, or containment against a fully compromised OS/root/admin. Hashes and sandboxes alone do not establish malware immunity. Encryption at rest primarily addresses access to protected storage without an authorized unlocked session, including lost/stolen media or offline theft; malware with equivalent authority in an unlocked session may still read data. Encryption does not replace least privilege, isolation, safe parsing, integrity verification, independent recovery, or backup protection. Malware controls likewise do not replace appropriate privacy encryption; they address different threats.

<a id="sec-2"></a>
### SEC-2 — No accidental secret disclosure

**Type:** PROHIBITION | **Origin:** DERIVED ENGINEERING RULE | **Applies:** secrets and security credentials

Applications MUST NOT disclose usable secrets through unintended source control, logs, prompts, exports, or interfaces. Storage/delivery MUST match threats and permit appropriate revocation/rotation. Credential stores, managed services, protected configuration, and environment injection are options. Restricted plaintext local files may suit a bounded threat model; they do not isolate all same-account processes. Environment variables also have exposure paths.

Ignore rules and permissions are not complete access or history-erasure controls. Disclosures need appropriate containment, including revocation where needed. Removing a file from a current tree does not remove every historical copy.

<a id="sec-3"></a>
### SEC-3 — Dependency and build discipline

**Type:** ECOSYSTEM POLICY | **Origin:** ARCHITECTURAL DECISION | **Applies:** released application builds and third-party dependencies

Released builds MUST record a reproducible dependency-resolution strategy appropriate to their toolchains, preserving integrity/trust checks. Library version ranges may coexist with reproducible test/release environments. Assess dependencies by function, provenance, maintenance, vulnerabilities, license, transitive cost, and replacement feasibility. Short handwritten security/parsing code is not inherently preferable.

Use supported lock/resolution mechanisms and review updates. `go.sum` records checksums; it alone is not an exact Go dependency lock model, which also involves `go.mod` and resolution semantics. Rust ownership checks and `Cargo.lock` do not establish trust. Vulnerability review SHOULD be proportionate and recurring; CVE scans cannot prove absence of defects.

Protect software delivery proportionately through dependency provenance, controlled resolution, source/release integrity verification, appropriately verifiable packages/updates, restricted build/release authority, vulnerability response, and review of critical third-party changes. No one signing system, SBOM format, package manager, or scanner is mandated. Automated updates MUST verify authorization and integrity before execution using an appropriate platform mechanism; arriving through the update path is not trust evidence by itself. Update failure MUST NOT silently authorize destructive data migration; [MIGRATE-1](#migrate-1) and [MIGRATE-2](#migrate-2) still apply. Reconstruction and material dependency-disappearance dispositions follow [SEC-5](#sec-5).

<a id="sec-4"></a>
### SEC-4 — Vendored or forked foundation provenance

**Type:** ECOSYSTEM POLICY | **Origin:** USER POLICY | **Applies:** third-party source snapshots vendored or forked as meaningful application foundations

Projects MUST preserve durable provenance appropriate to the foundation: upstream project/repository, version/tag where applicable, exact commit/revision, source digest where appropriate, license/notices, import date, acquisition method, local modification boundary, and maintenance/update strategy. When source identifiers differ, record an equivalent exact snapshot identity rather than inventing a commit.

Explicitly decide whether the project tracks upstream, selectively merges changes, or owns a fixed independent fork/snapshot. Do not leave that maintenance responsibility ambiguous. This does not require vendoring dependencies; foundation evaluation follows [DEV-3](#dev-3) and dependency safety follows [SEC-3](#sec-3).

<a id="sec-5"></a>
### SEC-5 — Release reconstruction and critical-dependency continuity

**Type:** ECOSYSTEM POLICY | **Origin:** USER POLICY | **Applies:** software built/distributed as executables, and dependencies whose disappearance materially threatens building, operation, migration, recovery, or maintenance

Projects producing executable software MUST preserve durable instructions and inputs sufficient to reconstruct a supported release or equivalent functioning build where reasonably practicable. Record applicable source revision, toolchain/compiler/runtime requirements, build commands, dependency resolution/locks, required build-time assets and generated-code steps, platform prerequisites, packaging/signing procedures, release provenance, and known limits. A future maintainer MUST NOT need undocumented tribal knowledge to determine how a supported release is produced. A tiny utility may satisfy this with concise prerequisites, its source revision, and one deterministic build command; larger distributions need proportionate detail and evidence under [TEST-1](#test-1).

For critical frameworks, runtimes, SDKs, toolchains, package ecosystems, libraries, required local services, model runtimes/providers, APIs, or platform components, the App Plan MUST record a proportionate disappearance-risk disposition where material. Options include replacement paths, interface boundaries, preserved source/vendor snapshots, migration/archive strategies, supported alternatives, or deliberately accepted dependency risk with applicable authority. Match treatment to criticality, replaceability, maintenance burden, license, security, and intended lifetime. Existing selection and foundation provenance follow [SEC-3](#sec-3) and [SEC-4](#sec-4).

State material reconstruction limits honestly, including proprietary SDKs, unavailable signing systems, hardware, closed platforms, discontinued services, and legal restrictions where relevant. No perpetual rebuild guarantee, bit-for-bit reproducibility, mandatory SBOM format, universal vendoring, permanent toolchain-binary retention, or archive of every historical release is required. Preservation does not require continued use of vulnerable obsolete components; distinguish preserved reference material from safe supported execution. No mandatory cloud build infrastructure is introduced. Protect signing secrets and respect access/retention constraints under [SEC-2](#sec-2) and [PRIV-1](#priv-1).

<a id="sec-6"></a>
### SEC-6 — Replaceable native malware-scanning capability

**Type:** ECOSYSTEM POLICY | **Origin:** USER POLICY | **Applies:** applications/security components benefiting from file malware detection

Projects SHOULD evaluate and prefer ClamAV as the default open-source malware engine where platform support, licensing, distribution, performance, and threat-model benefit are suitable. ClamAV is replaceable, not canonical architectural authority. Product code MUST depend on a generic malware-scanning capability boundary; engine-specific details belong in the adapter, not core product semantics. A suitable alternative or supplementary engine MAY be selected with documented rationale without requiring an exception merely for replacing this preferred implementation. Typed operations such as `scan_object`, `scan_stream`, `query_scan_status`, and `quarantine`, or equivalent contracts, preserve core-controlled authorization, outcomes, and promotion.

Scanning SHOULD execute locally on the user's device or authorized local infrastructure. Ordinary scanning MUST NOT require uploading private files to a cloud scanner; cloud scanning may only be an explicitly authorized optional capability under [PRIV-2](#priv-2). Where practical, prefer a constrained scanner process/service behind protected local IPC for crash isolation, resource limits, bounded filesystem/network access, privilege separation, replaceability, and security updates. Direct library integration remains permissible with technical and licensing justification; neither integration mechanism is universal. [SEC-1](#sec-1) and [AUTH-1](#auth-1) still govern effective boundaries.

For `clamd` or equivalent daemons, the scanner interface MUST remain local/protected unless an explicitly secured architecture justifies another deployment. Unauthenticated TCP listeners MUST NOT be exposed to the public Internet or untrusted networks. Prefer protected local sockets/IPC, constrained loopback, or equivalent platform transport; locality alone does not supply authorization. Preserve declared Windows, macOS, Linux, and other product targets under [PORT-3](#port-3); Linux-only ClamAV on-access functionality MUST NOT become a universal dependency. Platform-specific adapters may differ behind the capability contract. Scanning/signature failure follows [IO-3](#io-3) without giving the scanner canonical mutation authority.

When a ClamAV source archive is incorporated into an application or shared security component, record its version, upstream source/repository, exact revision if available, archive/source digest, license/notices, acquisition/import date, local modifications, build configuration, and update strategy under [SEC-4](#sec-4) and [SEC-5](#sec-5). Preserve modification history; do not silently alter vendored security source. Before distribution, verify the actual integration and redistribution model against applicable GPLv2 obligations and relevant bundled-component licenses. This policy does not establish that a particular archive, linking/process arrangement, or distribution is compliant. Importing a foreign-language engine remains governed by [LANG-1](#lang-1)'s dependency/artifact scope; it does not justify independently rewriting the shared Rust product core.

<a id="s26"></a>
## 26. Configuration, observability, and runtime lifecycle

<a id="run-1"></a>
### RUN-1 — Explicit configuration and defaults

**Type:** DEFAULT | **Origin:** ARCHITECTURAL DECISION | **Applies:** configurable applications

Applications SHOULD separate environment-specific settings from portable logic and define deterministic resolution/validation. Built-in defaults are legitimate. CLI, environment, deployment file, user preferences, defaults is an illustrative order; managed policy may be non-overridable. Surface relevant effective non-secret settings and use supported host discovery or explicit configuration. Changing configuration does not imply environments have equivalent capabilities.

<a id="run-2"></a>
### RUN-2 — Proportionate diagnostics

**Type:** CONDITIONAL | **Origin:** DERIVED ENGINEERING RULE | **Applies:** failure reporting and operations

Applications MUST provide sufficient outcome/failure information without unnecessary sensitive exposure. Expected conditions differ from faults; a best-effort cleanup failure may need no stack trace, but material loss or a failed commit MUST NOT be hidden. Logs need bounded resources and appropriate retention.

Structured logging, correlation IDs, metrics, and health endpoints SHOULD be used where helpful; short-lived tools may need only exit status and diagnostics. Separate liveness, readiness, and deeper checks. Ordinary probes SHOULD be lightweight/non-destructive. Read-only probes cannot guarantee future writes; deliberate synthetic writes need explicit scope and cleanup.

<a id="run-3"></a>
### RUN-3 — Declared deployment and bounded lifecycle

**Type:** CONDITIONAL | **Origin:** DERIVED ENGINEERING RULE | **Applies:** supported deployment modes and persistent services

Applications MUST document supported runtime modes. Native binaries, desktops, mobile/browser runtimes, services, and OCI images are options, not universal simultaneous requirements. Container identities, mounts, permissions, and isolation must fit their role; packaging does not establish NAS semantics.

Startup MUST verify prerequisites for safe operation, including relevant schema compatibility/exclusivity. Read-only software need not demand writable canonical storage. Preflight success does not replace runtime handling. Shutdown SHOULD stop new work, complete or safely interrupt work, and flush/close according to contract within appropriate bounds. Crash safety cannot depend solely on graceful shutdown. Exit status and diagnostics MUST reflect material failures; process exit alone does not prove effects completed.

<a id="s27"></a>
## 27. Verification and evidence

<a id="test-1"></a>
### TEST-1 — Evidence appropriate to the claim

**Type:** UNIVERSAL INVARIANT | **Origin:** DERIVED ENGINEERING RULE | **Applies:** claimed application guarantees

Applications MUST verify claims with evidence appropriate to scope, risk, and failure model. Important claims require relevant failure, recovery, concurrency, migration, portability, security-boundary, AI-capability, and NAS-mode checks where those capabilities exist. Record tested configurations and distinguish passed, failed, skipped, unrun, and unsupported outcomes. A syntactic checklist does not prove semantics.

Non-AI apps need no AI tests; stateless formatters need no backup tests; NAS backup does not imply raw network-database support. Reuse engine/platform evidence only within its assumptions and verify integration. Tests reduce uncertainty rather than establish absence of all defects.

<a id="test-2"></a>
### TEST-2 — Practical verification patterns

**Type:** RECOMMENDATION | **Origin:** DERIVED ENGINEERING RULE | **Applies:** development/release verification choices

Automation SHOULD cover critical transitions, interfaces, interruption points, authority boundaries, and representative workflows. Examples: concurrent edits, stale lease holders, disconnect after commit before acknowledgement, audit/outbox recovery, deletion then restore, incompatible schemas, and revoked queued authority. Use actual targets where needed; an emulator cannot certify every NAS appliance.

A shared conformance harness MAY help inspect declared applicability, links, schemas, and selected guarantees. It SHOULD measure behavior rather than prescribed filenames. Destructive tests need isolated fixtures and scope; a documentation rule does not authorize inspection or mutation of unrelated applications.

<a id="s28"></a>
## 28. Documentation, exceptions, and ratification

<a id="gov-2"></a>
### GOV-2 — Proportional living contracts

**Type:** ECOSYSTEM POLICY | **Origin:** USER POLICY | **Applies:** ecosystem repositories

Documentation MUST describe actual behavior, guarantees, assumptions, support, and limits. A concise README can cover a tiny tool; larger systems need relevant ownership maps, storage/authority contracts, AI capabilities, NAS configurations, recovery/migration, deployment, and evidence. Unimplemented aspirations MUST NOT be presented as existing behavior.

Machine-readable contracts SHOULD be maintained where they improve interoperability/enforcement. Schema generation reduces drift but does not prove runtime semantic or authorization agreement. Record significant tradeoffs and governing clauses. This constitution is primary; ADRs, reviews, and examples cannot silently strengthen it.

The specific development-governance obligations in [section 31](#s31) apply alongside this proportionality rule. Concise or combined records may satisfy them; proportionality does not waive idea refinement, the Plan Freeze Gate, current Project State, or phase conformance. The required machine-readable and human-readable Project State is governed by [DEV-9](#dev-9), not left optional by the general recommendation above.

<a id="gov-3"></a>
### GOV-3 — Policy authority and exceptions

**Type:** ECOSYSTEM POLICY | **Origin:** USER POLICY | **Applies:** policy decisions, deviations, and ratification

The repository owner/user is ultimate policy and ratification authority unless explicitly delegated. AI reviewers may recommend, challenge, draft, and verify, but cannot independently ratify. No governance board is presumed.

Formal exceptions to ecosystem policies, prohibitions, explicitly mandatory defaults, or genuine exceptional conflicts involving invariants MUST record rule ID, component/scope, technical reason, risk, mitigation, relevant duration/permanence or review trigger, and actual approving authority with approval evidence. Proposed exceptions are not approved. Scoped prior delegation can authorize decisions without repeated prompts.

Exceptions MUST be reconsidered when they expire, their assumptions materially change, their technical rationale disappears, or the requested scope changes. They may be renewed, replaced, superseded, or withdrawn by the applicable authority, with the disposition and affected scope recorded. Expiry does not silently renew approval, and changed scope is not automatically covered. When coverage lapses, record the resulting deviation and a proportionate resolution or transition; do not claim conformance or force unsafe immediate changes to deployed systems. Standing or enduring exceptions need no arbitrary periodic review when no expiry or material trigger applies.

Ordinary DEFAULT alternatives need a proportionate rationale, not impossibility proof or formal exception unless their clause expressly requires one. RECOMMENDATION alternatives need no exception. Material CONDITIONAL non-applicability should be documented without requiring approval. Rust-first and applicable NAS/feature-first departures follow formal policy governance; folder-name variation within feature-first does not.

An exception MUST NOT present an unmet engineering guarantee as satisfied. A real domain conflict needs revised scope, affected claims, residual risk, and authority under [SAFE-2](#safe-2). Approval cannot waive physical constraints or applicable legal obligations by declaration.

<a id="gov-4"></a>
### GOV-4 — Reviewable evolution

**Type:** ECOSYSTEM POLICY | **Origin:** USER POLICY | **Applies:** constitutional changes and adoption

Changes MUST preserve reviewability through recorded versions, rationale, affected rule IDs, and evidence. Candidate status MUST remain explicit until owner ratification. Adoption should identify exact revision and applicability date. Preserve historical reviews rather than rewriting findings to fit the result. Substantive changes need appropriate adversarial review and disposition. Changes here do not authorize automatic migration or assessment of governed repositories.

For this integration phase, a new adversarial attack and final release-candidate freeze MUST wait until the owner explicitly confirms **“There is nothing else left to add.”** Integration may resolve direct contradictions and validate documentation without conducting a hostile ratification review. The owner-supplied four-app blueprint is integrated as candidate policy; no final rc2 designation, ratification, merge, push, or release tag is authorized by this pass. Prior rc1 verification applies only to its reviewed revision, not automatically to this expanded working candidate.

The application Plan Freeze Gate in [DEV-5](#dev-5) does not trigger a constitutional attack or permit bypassing this gate. With the four-app blueprint integrated and subsequent UI/product/skill owner decisions supplied, finish authorized Green research/integration and completeness review, obtain explicit confirmation and candidate freeze, and only then conduct Red under [GOV-5](#gov-5). Earlier completeness recommendations apply only to their reviewed revision, not the expanded candidate. Adoption and authority to inspect another application's implementation remain separate decisions.

Supporting records: [Rust ADR](decisions/ADR-0001-rust-first.md), [historical review](reviews/2026-10-astra-adversarial-review.md), [integration disposition](reviews/2026-10-rc1-integration-disposition.md), [changelog](CHANGELOG.md), [historical attestation](provenance/initial-generation-boundary.md). Historical section numbers refer to their baseline, not this candidate.

<a id="gov-5"></a>
### GOV-5 — Green Flag, Red Flag, and review convergence

**Type:** ECOSYSTEM POLICY | **Origin:** USER POLICY | **Applies:** constitutional candidate integration, frozen-candidate attack, repair, and ratification recommendations

**GREEN FLAG** researches, integrates, reconciles, validates, and may repair confirmed findings within authorized scope. **RED FLAG** independently attacks the written owner-frozen candidate and is read-only: no normative edits, repairs, repair commits, or favorable reinterpretation of ambiguity. **GREEN FIX**, when invoked by the owner after Red findings, verifies the exact report/revision, repairs only validated findings, preserves owner policy, records every disposition, validates regressions, commits locally, and reports the new candidate HEAD. It does not introduce unrelated policy or ratify. Operational instructions are persisted in the [Green/Red protocol](governance/green-red-protocol.md); this rule remains normative authority.

Before RED FLAG, verify branch/HEAD/status, actual normative text, and explicit owner freeze evidence identifying the candidate. Without that evidence, STOP with **RED FLAG REQUIRES OWNER-AUTHORIZED PLAN FREEZE**. Prior completeness recommendations, integration reports, rule counts, historical favorable verdicts, or skill invocation do not authorize freeze/attack. After normative Green Fix, identify the exact repaired revision and verify that the owner freeze/repair authorization covers its review; do not transfer a prior verdict or infer authority for unrelated new policy. Scoped prior delegation may cover repair/review without a fresh prompt under [GOV-3](#gov-3). [GOV-4](#gov-4)'s completion-confirmation gate and separate ratification authority remain.

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

Every normative Green Fix invalidates an earlier Red pass and requires another attack. Recommend ratification only when zero BLOCKER/MATERIAL findings remain, prior findings have explicit dispositions, no old material defect regressed, current structural/factuality/proportionality checks pass, and **two consecutive independent Red rounds after the last normative repair** find no BLOCKER/MATERIAL defect. Disclose unavailable independence; a same-author replay is not independent. A recommendation is not ratification. No mode grants push, merge, remote-main/tag/release, or ratification authority without separate authorization.

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
## 30. Freeze status and review continuation — non-normative

Rust-first, feature-first, modular-monolith default, applicable NAS support, local/offline-first, owner governance, scoped product platforms, the shared Rust core, UI strategies, device/NAS synchronization direction, and vector-asset policy are owner decisions integrated into this frozen candidate. Universal event sourcing, one database, per-action confirmation, and identical presentation across all devices are not pending requirements.

**Hermes / User-Adaptable File Structure Blueprint — INTEGRATED AS CANDIDATE POLICY; NO LONGER PENDING DESIGN.** The owner reports completion of the comparative design analysis of Mosaic, LMS / Studies, Accounting & Money, and Read & Watch and has supplied the approved generalized direction. [Section 32](#s32), [HERMES-1](#hermes-1), [HERMES-2](#hermes-2), [HERMES-3](#hermes-3), and the reconciled data, evidence, operation, and development rules integrate that blueprint. It standardizes discoverability and integrity rather than one user-facing content hierarchy. The development-artifact blueprint in [DEV-6](#dev-6) remains a separate responsibility.

Those applications informed the owner's analysis; their repositories, plans, and domain-specific behavior are not normative sources or dependencies of this constitution. No application repositories were inspected during this integration. The [four-app integration record](reviews/2026-10-four-app-blueprint-integration.md) preserves self-contained design provenance and policy coverage. Earlier records accurately showing pending design remain historical and unchanged.

**Current checkpoint: RF-01 and RF-02 repaired under explicit owner GREEN FIX authority; candidate `1.0.0-rc2.1` is frozen for fresh review and unratified.** The [repair record](governance/2026-10-green-fix-rf01-rf02.md) binds the two findings, scope, validation, and resulting revision. The original freeze, revision receipt, research, and historical reports remain preserved.

Ordinary policy brainstorming remains closed. Only DEV-5 and GOV-5 were normatively repaired. The previous Red review of `e15191c1509facc3859b46c25cc8a1d1b7eaa12f` found zero BLOCKER, zero MATERIAL, and two NON-BLOCKING findings; that historical result does not validate the repaired candidate or satisfy post-repair convergence.

Remaining sequence:

1. Conduct a fresh independently reviewed Red Flag round against the exact repaired frozen revision under [GOV-5](#gov-5) and the [persisted protocol](governance/green-red-protocol.md). No new Red attack occurred during this Green Fix.
2. Preserve findings, evidence, and explicit dispositions; supporting history cannot excuse defective normative wording.
3. Any further normative repair needs applicable authority and invalidates prior clean rounds again.
4. Require two consecutive independent clean Red rounds after the last normative repair, with zero BLOCKER/MATERIAL findings and the remaining convergence checks. Ratification remains a separate owner decision; no push, merge, tag or release is authorized here.

The prior rc1 verdict was **RATIFY WITH NON-BLOCKING ISSUES**, with no blockers and four clarifications; its historical outcome is recorded [separately](reviews/2026-10-rc1-verification-outcome.md). Subsequent owner decisions required this integration before ratification. The rc1 verdict is not a review of this revision. Policy coverage is recorded in the [initial integration report](reviews/2026-10-pre-attack-integration.md) and subsequent [development-governance integration](reviews/2026-10-development-governance-integration.md).

<a id="s31"></a>
## 31. Application planning, continuity, and conformance

These are intentional owner development-governance policies, not claims that a particular directory structure is a universal engineering invariant. They inherit CANDIDATE status. Their application to another repository requires the applicable adoption and task authority; this integration does not authorize inspecting or changing other apps.

<a id="dev-1"></a>
### DEV-1 — App-specific design and long-lived purpose

**Type:** ECOSYSTEM POLICY | **Origin:** USER POLICY | **Applies:** application design and development lifecycle

The development process MUST pursue maintainability, understandability, recoverability, portability, evolvability, AI continuity, user control, structural coherence, and useful longevity. The constitution governs how designs are discovered, challenged, documented, built, verified, and maintained. It MUST NOT be interpreted as requiring identical application features or identical user-data structures. The design MUST reflect the idea, users, domain, risk, data, target platforms, and intended lifecycle. These goals improve the probability of long-term success; they do not guarantee indefinite usability.

<a id="dev-2"></a>
### DEV-2 — Refine the idea before implementation

**Type:** ECOSYSTEM POLICY | **Origin:** USER POLICY | **Applies:** new applications before implementation begins

Implementation MUST NOT begin merely because an initial idea exists. Before implementation code is changed, the idea MUST be interrogated and refined into a coherent product definition addressing the problem, users, long-term role, owned/preserved information, offline capabilities, multi-device needs, NAS behavior, desktop/mobile/web scope, Hermes/AI role, privacy/security expectations, user configuration, expected lifetime, migration/portability needs, and major failure scenarios where applicable. Record non-applicability rather than inventing unnecessary features. Brainstorming MUST NOT silently become implementation. Planning then proceeds through research, specification, and the [Plan Freeze Gate](#dev-5).

Substantial product refinement MUST include actual value/differentiation under [DEV-18](#dev-18) before architecture freeze; private/internal fit does not require a commercial moat.

<a id="dev-3"></a>
### DEV-3 — Research before architecture freeze

**Type:** ECOSYSTEM POLICY | **Origin:** USER POLICY | **Applies:** new or substantially revised application architecture

After the idea is sufficiently defined and before architecture is frozen, planning MUST research relevant existing solutions: GitHub repositories, mature open-source applications, standards, libraries/frameworks, technical papers or documentation where useful, known architectural failures, and competing approaches. Scope research to the actual problem and authorized sources. Ask whether an existing solution solves a relevant problem better than the proposed design; copying another project is not the goal.

If no better solution is found, refine and retain the design. If a superior pattern is found, understand its advantage, determine applicable parts, and deliberately update the plan. Important comparisons and resulting decisions MUST be preserved under [DEV-8](#dev-8); lack of evidence MUST NOT be reported as completed research.

Before rebuilding a difficult subsystem from scratch, research whether mature existing software solves the relevant problem substantially better. Deliberately evaluate use as a dependency, wrapping, adaptation, vendoring, forking, or rejection, considering architecture fit, security, maintenance, licensing, portability, long-term control, and integration cost. Existence alone does not require adoption. Significant source foundations need provenance under [SEC-4](#sec-4); Rust-first artifact/exception scope remains governed by [LANG-1](#lang-1).

<a id="dev-4"></a>
### DEV-4 — Strongest reasonably available planning capability

**Type:** ECOSYSTEM POLICY | **Origin:** USER POLICY | **Applies:** creation or substantial redesign of an application Master Plan

Planning MUST use the highest-capability model reasonably available for research synthesis, architectural resolution, edge cases, interfaces, storage and synchronization semantics, platform strategy, AI/Hermes design, risks, phases, and acceptance criteria. Record the planning capability selected and material availability constraints proportionately. This requires neither a named provider nor permanent cloud access; relevant data-access and privacy constraints remain in force.

Reasoning, decisions, contracts, and requirements needed for implementation MUST be captured in durable project artifacts. The implementation process MUST NOT depend on continued access to the strongest model or on its hidden conversation history. Model selection does not itself establish correctness or authority.

<a id="dev-5"></a>
### DEV-5 — Candidate-plan review and Plan Freeze Gate

**Type:** ECOSYSTEM POLICY | **Origin:** USER POLICY | **Applies:** application plans before implementation and material architectural replanning

Once the full application plan appears complete, freeze an identifiable candidate plan for hostile review before implementing it. Review MUST use the strongest reasonably available AI capability and relevant human/domain expertise and targeted technical research as appropriate to the plan and risk. Attack correctness, architecture, maintainability, longevity, data loss, storage/NAS failures, partitions, sync conflicts, migrations, offline behavior, platform differences, AI failures, security, privacy, performance, recovery, technology/dependency changes, small-model usability, developer replacement, and incomplete requirements where applicable.

Use **Attack → Fix → Attack → Fix**, preserving findings and dispositions, until no known material issue remains unresolved. The **Plan Freeze Gate** is: implementation may begin only when all known material architectural questions, contradictions, blocking risks, and unresolved design decisions have been resolved or explicitly accepted and documented by the applicable authority. Record the gated plan revision, evidence, accepted constraints, and any approved exceptions. Acceptance MUST NOT disguise a missing decision as an implementation task or waive a constitutional obligation without [GOV-3](#gov-3) authority. The gate is an evidence-based decision, not mathematical “100% perfection.”

Authorized, bounded research experiments MAY precede Plan Freeze when needed to resolve a material planning question, including architecture, API/platform compatibility, performance, storage, migration, or crash/recovery behavior. For this gate and [DEV-2](#dev-2), these are evidence-gathering activities, not adopted product implementation. Each experiment MUST define its research question or hypothesis, bound its scope to the evidence needed, and record results and relevant limitations through [DEV-6](#dev-6) and [DEV-8](#dev-8). Experimental code/data MUST be clearly identified as experimental/disposable or otherwise non-authoritative unless deliberately adopted later; the label does not authorize destruction of retained source data or required evidence. Small research scripts need no full production phase merely to gather evidence, but actual authorization, security/privacy controls, safe execution, and truthful evidence remain required.

Incorporation of experimental code or behavior into the product MUST pass the normal Plan Freeze, phase, conformance, security, testing, and evidence requirements. “Prototype” or “research” MUST NOT become a loophole for implementing substantial production scope before planning. Exploratory work MUST NOT silently become canonical architecture merely because it exists. Unresolved questions remain planning questions; this research route does not waive [DEV-11](#dev-11)'s stop-rather-than-guess rule or [DEV-13](#dev-13)'s completion gate.

Material new architectural uncertainty during implementation returns the affected work to planning and this gate; do not silently improvise a different architecture. This application-plan review requirement does not authorize the constitution's final attack, which remains blocked under [GOV-4](#gov-4).

Necessary emergency maintenance may temporarily precede complete planning only under [DEV-17](#dev-17), with bounded authority, evidence, and reconciliation before ordinary feature work resumes. This does not waive the gate for normal implementation.

<a id="dev-6"></a>
### DEV-6 — Discoverable planning and implementation responsibilities

**Type:** ECOSYSTEM POLICY | **Origin:** USER POLICY | **Applies:** substantial application repositories, with proportionate representations for smaller applications

Substantial applications SHOULD conceptually separate `App/APP Plan/` from `App/Codebase/`. The implementation belongs to Codebase; APP Plan holds durable specification, intelligence, state, decisions, and the roadmap. These logical responsibilities MUST remain clear and discoverable. Exact directory names and physical layout MAY be adapted; smaller projects may combine concise records without dropping applicable lifecycle gates.

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
### DEV-7 — Authoritative current Master Plan

**Type:** ECOSYSTEM POLICY | **Origin:** USER POLICY | **Applies:** application planning and changes to intended architecture or behavior

The Master Plan MUST state the current authoritative specification of the intended completed product, directly or through clear references. It MUST cover applicable product purpose, users, features, architecture, shared Rust core, platform scope, UI strategy, storage architecture, canonical data model, synchronization, NAS and local-only behavior, AI/Hermes, security, privacy, backup/recovery, migrations, testing, deployment, packaging, interfaces, extension points, constraints, and accepted exceptions.

Keep historical brainstorming and superseded rationale in Research, Decisions, Reviews, or provenance; do not make a reader infer current intent from chronology. Changes to intended behavior MUST update the plan deliberately with relevant decision and phase links. The Master Plan specifies intended product truth; it does not claim unbuilt features exist or supersede the constitution without an approved exception.

Every App Plan MUST state the timezone policy under [DATA-5](#data-5). It MUST also specify, where applicable, release reconstruction and dependency-disappearance dispositions ([SEC-5](#sec-5)), recovery without normal startup ([RECOVER-1](#recover-1)), lifetime growth/validation assumptions ([DEV-16](#dev-16)), emergency repair/reconciliation ([DEV-17](#dev-17)), accessibility acceptance criteria ([UI-3](#ui-3)), and locale parsing/identity semantics ([DATA-4](#data-4)). Make procedures, limits, and criteria discoverable without inferring them from code; no separate empty documents are required.

For substantial retained-data applications, security planning MUST address relevant hostile inputs and exposed processors, their access and compromise consequences, destructive sync propagation, NAS-history protection, actual backup copies/deletion authority, restore validation, update integrity, suspected-compromise containment, and evidence for known-good recovery points. Reference the contracts in [SEC-1](#sec-1), [SEC-3](#sec-3), [IO-1](#io-1), [SYNC-1](#sync-1), [NAS-1](#nas-1), [BACKUP-1](#backup-1), [BACKUP-2](#backup-2), and [RECOVER-1](#recover-1) rather than duplicating a parallel security plan. Scope effort to retained-data value, attack surface, and architecture.

Applicable file-intake plans MUST make the [IO-2](#io-2), [IO-3](#io-3), and [SEC-6](#sec-6) contracts discoverable: logical boundary, required promotion gates, scanner selection/transport/authority, verdict reuse and rescan policy, signature maintenance, quarantine controls, status reporting, cross-device trust, lifetime performance, source provenance, and distribution-license verification. Concise references may satisfy this without a separate scanner governance system.

For relevant user-facing work, the plan MUST include or reference the design responsibilities under [UI-4](#ui-4)–[UI-7](#ui-7) and product value under [DEV-18](#dev-18). Development metadata SHOULD identify applicable skill families, trusted versions, local changes/provenance and permissions under [section 33](#s33), without duplicating unchanged central guidance.

<a id="dev-8"></a>
### DEV-8 — Comparative research and explicit decisions

**Type:** ECOSYSTEM POLICY | **Origin:** USER POLICY | **Applies:** significant researched alternatives and architectural decisions

Research records MUST identify what was examined, why it was relevant, strengths, weaknesses, what was adopted or rejected, and why. Preserve important source/version references and comparative evidence sufficiently for future humans or AI to understand the decision without repeating major research. Such records do not require copying entire third-party repositories or restricted source material.

Research claims MUST distinguish verified evidence, inference/conditional evidence, and unresolved unknowns under [EVID-1](#evid-1). Supporting evidence belongs in or is referenced through the Evidence responsibility under [DEV-6](#dev-6). Repetition MUST NOT turn an assumption into a frozen architectural fact. Material unverified assumptions and conflicts MUST be resolved or explicitly accepted with their status intact at the [Plan Freeze Gate](#dev-5).

Important architectural decisions MUST be explicit and individually discoverable, including applicable Rust-core, storage-engine, sync-model, NAS-topology, UI, identity, AI/Hermes-boundary, and backup choices. A weaker model must not need to infer them from hundreds of pages of historical text. Decision records MUST identify current versus superseded decisions and link to the Master Plan where needed.

<a id="dev-9"></a>
### DEV-9 — Project State as the current execution entry point

**Type:** ECOSYSTEM POLICY | **Origin:** USER POLICY | **Applies:** every active application

Each active application MUST maintain a concise machine-readable and human-readable Project State record, discoverable from the repository entry point. One record or consistently generated views MAY satisfy both forms; no exact format is mandated. Its sole governing responsibility is current execution status and navigation, not duplication of the full Master Plan or completed history.

Without prior conversation, it MUST reveal the current phase, last completed phase, completed capabilities, work in progress, work not started, known blockers, current branch/revision where applicable, next authoritative action, and the active phase specification's location. Identify the revision actually observed rather than inventing a self-referential commit identifier. Update status when work, blockers, phase completion, or next action changes; distinguish verified completion from claims awaiting verification. State/implementation contradictions MUST be reconciled before relying on that state to proceed.

<a id="dev-10"></a>
### DEV-10 — Phases as executable implementation specifications

**Type:** ECOSYSTEM POLICY | **Origin:** USER POLICY | **Applies:** planned implementation and conformance phases

Each phase MUST be sufficiently specified for bounded execution rather than a loose task list. Define as appropriate its objective, rationale, prerequisites, current and expected end states, files/components, interfaces/contracts, data structures, dependencies, tasks and ordering, invariants, files/systems that must not change, error behavior, edge cases, migration impact, security/privacy, tests, validation commands, expected results, completion evidence, stopping conditions, follow-up state, and next phase.

If major architecture must still be invented during execution, the phase is insufficiently specified and affected implementation MUST stop for planning resolution. A phase MUST distinguish delegated implementation choices from unresolved architectural decisions. Acceptance criteria and validation MUST describe outcomes that can actually be checked under [TEST-1](#test-1), not merely the presence of code.

Large phases MAY be decomposed into bounded tasks. As applicable, a task SHOULD state its ID, objective, prerequisites, scope, permitted and forbidden changes, expected result, validation, and stop conditions. The phase remains the governing specification and conformance boundary. Tiny phases need no artificial task hierarchy.

The temporary emergency path in [DEV-17](#dev-17) may defer only necessary normal planning steps; its durable emergency record and subsequent repair contract do not grant permission to invent unknown architecture.

Phase specifications MAY name relevant process skills for bounded loading, but MUST retain their actual project-specific specification under [SKILL-2](#skill-2). Substantial UI phase acceptance MUST include applicable rendered review under [UI-7](#ui-7); “use frontend-design skill” alone is not a phase contract.

<a id="dev-11"></a>
### DEV-11 — Full-build small-model continuity and safe resumption

**Type:** ECOSYSTEM POLICY | **Origin:** USER POLICY | **Applies:** application plans, phase execution, and AI-assisted continuation

Plans and repositories MUST be designed so that a sufficiently capable small local model can build the entire application phase by phase using APP Plan and Codebase, without hidden conversation history or continuous rescue by a stronger model. Shift complexity into specifications, contracts, examples, indexes, tests, acceptance criteria, deterministic tooling, and explicit Project State. Strong planning captures architectural reasoning ahead of time; weaker execution remains bounded. This is a full-build design target, not merely the ability to continue one task and not a claim that any model or parameter count can complete every application.

Every phase MUST support zero-conversation resumption: locate Project State; establish completion and active phase; read the specification; locate implementation; understand the required outcome; make authorized safe changes; run validation; record results; determine completion; and proceed only where permitted by the phase gate. Local execution is the baseline design target; a suitable cloud model may follow the same artifacts, but provider/location alone does not establish capability and continued cloud access is not required.

**A weaker model is allowed to do less, but not to invent more.** If required information is missing, contradictory, or cannot be safely established, the executor MUST stop affected work and record the precise blocker and needed resolution. It MUST NOT invent architecture, silently reinterpret the Master Plan, claim unperformed validation, expand authority, or bypass [AI-1](#ai-1), [AI-3](#ai-3), or [AUTH-1](#auth-1). Full-build continuity does not grant unrestricted autonomous execution; it supplies the information needed to execute authorized work safely.

This **product-development** goal concerns building/continuing software from APP Plan, phases, Project State, tests, and Codebase. The separate **product-use** goal under [HERMES-2](#hermes-2) concerns navigating and using supported application tools through structured, bounded retrieval. Both apply where relevant; satisfying either one does not prove the other.

<a id="dev-12"></a>
### DEV-12 — Evidence-bearing Done Phases

**Type:** ECOSYSTEM POLICY | **Origin:** USER POLICY | **Applies:** phases that have passed the completion gate

A completed phase MUST be moved or recorded in discoverable Done Phases history, preserving the original specification or its immutable reference, actual implementation, deviations, relevant decisions, tests executed, outcomes, completion evidence, relevant commit/revision references, and remaining follow-ups. Update Project State with the result and next permitted action. A failed or unverified phase MUST NOT be represented as done.

Done Phases complements Git and other version history with understandable evidence; it neither replaces version control nor requires reconstructing completed work solely from commits. References may avoid duplicating large artifacts, provided the promised evidence remains accessible under its retention contract. Follow-ups MUST NOT conceal unresolved required acceptance criteria; approved exceptions are explicit.

For substantial tasks/phases, preserve execution evidence during work as well as at completion: what was attempted, what actually changed, validation performed, passed/failed outcomes, remaining uncertainty, and the containing revision/commit where relevant. Interrupted or failed work needs an accurate continuation record rather than a false Done entry. Project State points to this evidence; completion incorporates or references it in Done Phases without unnecessary duplication or a mandatory `Operations/` directory.

Evidence MAY include tests, builds, static checks, runtime validation, relevant screenshots, schemas, hashes, migration comparisons, commit IDs, and operation receipts as appropriate. Evidence supports the actual claim and the [Three-Layer Conformance Gate](#dev-13); its mere existence or a screenshot cannot establish unrelated guarantees.

<a id="dev-13"></a>
### DEV-13 — Three-Layer Conformance Gate after every phase

**Type:** ECOSYSTEM POLICY | **Origin:** USER POLICY | **Applies:** completion of every implementation or conformance phase

Code being written is not completion. Before a phase is marked complete or the next implementation phase proceeds, all applicable layers MUST pass:

1. **Universal Rules:** conformance to the applicable constitutional revision and approved exceptions.
2. **App Master Plan:** conformance to the application's current specified architecture and behavior.
3. **Phase Contract:** satisfaction of that phase's acceptance criteria and required evidence.

Verification MAY be performed by AI, humans, automated validation, or a combination. The verifier MUST compare the actual implementation/artifacts with specifications rather than merely trusting the implementing agent's completion claim. Use deterministic evidence where practical: tests, builds, schemas, static analysis, fixtures, integration validation, and artifact inspection. Record applicable criteria, outcomes, evidence, and exceptions; skipped or unrun required checks are not passes. Separate verifier identity is not universally required, but evidence-based comparison is.

The continuing cycle is **Implement → Verify → Universal Rules → Master Plan → Phase Contract → Pass: continue / Fail: repair**. Do not accumulate known architectural debt for later without an explicit approved exception under [GOV-3](#gov-3). Phase checks cover implemented scope and effects, including regressions in previously conformant work; a planned future capability is not automatically a present violation. Required-but-missing behavior for the current scope remains a failure. Repair phases may address documented failures; ordinary feature progression cannot bypass them.

Emergency containment/repair follows [DEV-17](#dev-17)'s temporary procedure and post-emergency reconciliation gate; it does not count as verified phase completion merely because it was urgent.

<a id="dev-14"></a>
### DEV-14 — Brownfield assessment and conformance before features

**Type:** ECOSYSTEM POLICY | **Origin:** USER POLICY | **Applies:** existing or partially built applications when these rules are applied with appropriate authority

Normal feature development MUST pause before extending inherited implementation. First inspect the authorized application, create/update its Master Plan, compare implementation with the applicable Universal Rules, Master Plan, and intended architecture, classify existing work, create Conformance Phases, repair, verify conformance, and only then resume ordinary planned development. Applying this workflow requires actual authority for that repository; this constitutional rule alone grants none.

An Existing App Assessment or equivalent MUST classify inherited implementation as applicable: already compliant, correct and reusable, usable with modification, obsolete, unsafe, architecturally inconsistent, or missing. **Preserve compliant work, repair non-compliant work, replace only where necessary.** Age or predating the current plan does not justify rewriting working compliant code. Record evidence, gaps, retained work, required repairs, and any approved exceptions.

Conformance Phases MUST precede new feature phases and use [DEV-10](#dev-10) and [DEV-13](#dev-13). They bring the inherited implemented scope into alignment with the constitution and current Master Plan; they do not require all future roadmap features to exist before development can resume. A failed gate permits scoped repair, not ordinary feature expansion. Following aggregate conformance verification, every subsequent phase remains subject to the same three-layer gate. Applicable safety/containment actions under [SAFE-2](#safe-2) remain possible; they are not a feature-development bypass.

<a id="dev-15"></a>
### DEV-15 — Repository memory and the longevity test

**Type:** ECOSYSTEM POLICY | **Origin:** USER POLICY | **Applies:** application planning, documentation, and long-term continuation

Planning MUST ask: **Could another human or AI understand, maintain, repair, migrate, and continue this application years later using only the repository and documented external dependencies?** If not, planning/documentation is insufficient and the identified gaps MUST be addressed before claiming the relevant plan or phase ready.

The repository MUST carry durable development memory sufficient to establish what the app is, why major decisions were made, what is implemented, what remains, what was rejected, known risks, how to validate, and how to continue. Conversation history may assist planning but MUST NOT be required for continuation. Avoid unnecessary dependence on one developer's memory, one AI conversation, one model provider, one computer, undocumented file locations/decisions, or unsupported proprietary assumptions. Document necessary external dependencies and recovery/access requirements without committing secrets or retaining unnecessary sensitive conversation payloads; [PRIV-1](#priv-1) and [SEC-2](#sec-2) still apply.

<a id="dev-16"></a>
### DEV-16 — Lifetime growth envelope and maintenance validation

**Type:** ECOSYSTEM POLICY | **Origin:** USER POLICY | **Applies:** planning and verification where retained data, history, media, logs, indexes, or relationships may materially grow

The App Plan MUST define a reasonable expected lifetime growth envelope and its validation assumptions where scale affects architecture. Relevant dimensions may include records/files, storage/media volume, relationships, history/audit growth, devices, archive age, and users/accounts/tenants. State assumptions and limits so future humans or AI need not infer the intended workload. This is a planning envelope, not an indefinite capacity guarantee or universal numerical threshold.

Validation under [TEST-1](#test-1) MUST consider applicable ordinary and lifecycle operations at expected scale: startup, query/search, index rebuilding, backup, restore, migration, sync, recovery, export, integrity scans, and compaction/retention. The App Plan defines suitable resource/time budgets and supporting evidence, including limitations of estimates or representative samples. Tiny or inherently bounded applications may state that bound and its rationale without special scaling architecture or meaningless benchmarks.

<a id="dev-17"></a>
### DEV-17 — Emergency maintenance and reconciliation

**Type:** ECOSYSTEM POLICY | **Origin:** USER POLICY | **Applies:** urgent maintenance where delay materially increases security, data-loss, privacy, safety, or unrecoverable operational risk

Emergency maintenance MAY precede complete normal planning when necessary under [SAFE-2](#safe-2). Bound work to the minimum necessary containment, mitigation, repair, urgency-appropriate validation, and preservation of change evidence. Defer only planning or routine approval steps that cannot practicably precede containment, using actual applicable emergency authority or prior delegation under [AUTH-2](#auth-2) and [GOV-3](#gov-3). Emergency status does not manufacture permission, waive integrity/privacy boundaries, or authorize ordinary feature development. Routine bugfixes do not automatically invoke this procedure.

Maintain a proportionate durable record of trigger, scope, authorization, affected components, actual change, validation, residual risks, and temporarily deferred requirements. Link it from Project State under [DEV-9](#dev-9) so an interrupted session can resume safely. A small urgent patch needs concise evidence, not a parallel paperwork system. [DEV-11](#dev-11) still prohibits guessing missing facts or inventing architecture; choose only safely established, authorized actions and record blockers for the rest.

Before ordinary feature development resumes after a material emergency change, reconcile the applicable Master Plan, Project State, Decisions, phase/execution history, tests, architecture, compatibility expectations, migration implications, and documentation. Establish or update the repair's phase contract and run the applicable [Three-Layer Conformance Gate](#dev-13); deferred required checks are not passes. Outstanding failures require repair or an actually approved scoped exception under [GOV-3](#gov-3), not silent permanent drift. Emergency repair may temporarily precede complete planning; it MUST NOT permanently bypass project truth or mark an unverified phase complete.

<a id="dev-18"></a>
### DEV-18 — Product value and differentiation before architecture freeze

**Type:** ECOSYSTEM POLICY | **Origin:** USER POLICY | **Applies:** idea refinement and planning of substantial applications

Before architecture freeze, the product MUST answer: **If someone else can create software performing the same general function, why should someone use this application?** Record actual value such as workflow/usability, privacy/local operation/user ownership, reliability/portability/accessibility, performance/interoperability, specialist fit, low friction, execution quality, longevity/recovery/trust, or precise fit to an individual owner's needs. No fake commercial moat, novelty for its own sake, or market claim is required for private/internal products.

The answer MUST influence relevant workflows, feature priorities, UX/UI, architecture, privacy, platform support, integrations, performance and offline/local behavior; an interchangeable implementation with only a slogan is insufficient. Record what should not be built alongside purpose and alternatives under [DEV-2](#dev-2), [DEV-3](#dev-3), and [DEV-7](#dev-7). Verify the connection in applicable phase/UI review under [DEV-13](#dev-13) and [UI-7](#ui-7).

<a id="s32"></a>
## 32. Universal Information Architecture Blueprint

This candidate blueprint standardizes discoverability and integrity contracts across applicable products, not domain features or one universal folder tree. The owner-supplied four-app analysis provides design provenance, not external normative dependencies. These rules complement existing data, storage, recovery, privacy, synchronization, and AI authority contracts.

<a id="info-1"></a>
### INFO-1 — Logical information architecture independent of storage layout

**Type:** ECOSYSTEM POLICY | **Origin:** USER POLICY | **Applies:** applications managing durable user information

The logical information model MUST support deterministic discovery/resolution, identity, provenance where meaningful, relationships, documented access, recovery, continuation, rebuildability where claimed, and portability where required. Human-facing hierarchy MUST remain application/domain-appropriate and MAY be user-configurable. **Standardize the discoverability and integrity contract, not every user's folder names.**

Files, SQLite, PostgreSQL, embedded object stores, services, and other justified architectures may satisfy this contract through manifests, catalogs, schemas, APIs, export contracts, deterministic indexes, or equivalent mechanisms. Filesystem-backed canonical storage, Markdown, any particular database, and universal filenames are not required. “Deterministic” here concerns lookup and explicit contracts, not proof that facts, AI outputs, or all application behavior are deterministic.

Where practical, retained information SHOULD support both human comprehension through meaningful names, metadata, documentation, relationships, readers or exports, and machine reliability through structured IDs, schemas, manifests, catalogs, or typed records. Do not sacrifice deterministic interfaces for attractive folders or long-term comprehensibility merely for AI indexing convenience. Documented binary stores are compatible with these outcomes under [LIFE-2](#life-2) and [STORE-1](#store-1).

<a id="info-2"></a>
### INFO-2 — Discoverable workspace entry contract

**Type:** ECOSYSTEM POLICY | **Origin:** USER POLICY | **Applies:** substantial durable workspaces, including equivalent database/service-managed datasets

A workspace MUST expose a predictable logical entry point through which authorized deterministic software and suitably constrained AI can discover applicable workspace identity, schema/format version, major domains/collections, registered data roots, important catalogs/indexes, supported operations, migration/version state, relevant policy/configuration, and lineage where required.

A root manifest, workspace catalog, typed API, database schema plus discovery endpoint, or equivalent deterministic mechanism may implement this capability. No physical root filename or public disclosure of private metadata/secrets is required. Discovery is subject to authorization; version handling follows [MIGRATE-2](#migrate-2). Supported offline discovery and synchronization follow the existing local-first and sync contracts.

<a id="info-3"></a>
### INFO-3 — Durable identity, organization, and relationships

**Type:** ECOSYSTEM POLICY | **Origin:** USER POLICY | **Applies:** important durable logical objects whose identity must survive organization changes

Such objects MUST have durable product-owned logical identity or an equivalent documented identity contract independent of mutable filenames, display names, paths, categories, statuses, or UI locations. The product SHOULD resolve **stable identity → current location** where location applies. Ordinary renaming or movement between folders, collections, statuses, categories, and views MUST NOT unnecessarily create a new identity or destroy relationships, provenance, or retained history. Explicit copy/new-object and migration operations may have distinct documented identity semantics.

When an object participates in multiple views or relationships, prefer explicit references/relationships over uncontrolled canonical duplication. Canonical information SHOULD NOT be duplicated merely to appear in multiple organizational views when references preserve the same meaning safely. Deliberate replicas, snapshots, backups, and derivatives remain valid with declared authority and lifecycle. Where byte identity or deduplication matters, content hashes or equivalents may assist integrity, provenance, and tracking; content-addressing is not universally required, and byte equality is not automatically logical identity or authenticated origin.

<a id="info-4"></a>
### INFO-4 — Precise sub-object addressing and source context

**Type:** ECOSYSTEM POLICY | **Origin:** USER POLICY | **Applies:** large or heterogeneous content where sub-object addressing materially improves retrieval, citation, annotation, or verification

Applications MUST support appropriate deterministic stable/bounded addressing where technically meaningful so a consumer can resolve **object → precise relevant region** without loading or reasoning over an entire huge object. Pages, sections, paragraphs, records, spreadsheet ranges, timestamps, transcript segments, media frames, image regions, and code symbols are examples, not required features or one universal anchor format.

Anchors to mutable content MUST retain enough source context to determine validity, such as source version/hash, surrounding-text hash, record revision, time/version relationship, or an equivalent mechanism. An old annotation/extraction MUST NOT silently attach to unrelated changed content. Stale, ambiguous, or unresolvable anchors require explicit status, revalidation, or a justified remapping operation. Source and derivative lineage follows [DATA-3](#data-3), while uncertainty follows [EVID-1](#evid-1).

<a id="s33"></a>
## 33. Reusable Universal Agent Skills governance

These owner policies define a reusable workflow library and its trust/authority contracts. This constitutional catalog is not a claim that operational skill packages have already been authored, installed, reviewed, or tested. An Agent Skill means inspectable workflow guidance and any supporting resources/scripts; calling it a prompt does not remove supply-chain or execution risk.

<a id="skill-1"></a>
### SKILL-1 — Modular, discoverable, portable process expertise

**Type:** ECOSYSTEM POLICY | **Origin:** USER POLICY | **Applies:** design and maintenance of ecosystem/project Agent Skill libraries

The ecosystem Agent Skill Library MUST organize reusable engineering process expertise rather than encode each application's product truth. Universal skills and project-specific/domain skills MUST remain distinguishable; project-specific workflows remain under that project's Master Plan and authority. A catalog/manifest or equivalent discovery contract MUST expose skill name/purpose, applicability, needed permissions, source/provenance and current trusted revision/review state where relevant, plus availability and deprecated/superseded status. No universal directory tree, filename, or copy of each unchanged global skill inside every project is required; reliable versioned references may suffice.

Skills SHOULD be cohesive modules loaded progressively for the current task rather than one universal super-prompt containing frontend, security, deployment, databases, planning, UX, tests, and legal disciplines at once. Identify relevant guidance, load only what is needed, execute within the phase, and leave irrelevant material out of active context where tooling permits. Trivial work needs no dozens of skills. Supporting templates, checklists, scripts, examples, schemas, and references MAY be included, while governing instructions and permissions remain understandable.

Complex skills SHOULD use compact root instructions that route to relevant supporting documents or scripts when needed, instead of loading every workflow or repository document for every task. Reusable guidance SHOULD avoid rigid itineraries that add context or constraints without improving correctness, safety, evidence, or reproducibility. This does not weaken the executable Phase Contract under [DEV-10](#dev-10), required validation, or stop conditions; reusable process guidance and project-specific execution specifications have different responsibilities.

Critical workflow instructions MUST remain reviewable text or equivalent inspectable durable process documentation; an opaque proprietary prompt/service MUST NOT be their only representation. Core expertise SHOULD be portable across current/future cloud models, local models, and human developers, with provider-specific wrappers where useful. Skills SHOULD supply explicit procedure, expected inputs/outputs, stop conditions, validation, and evidence for bounded small-model execution under [DEV-11](#dev-11); limited capability does not justify broader authority.

Initial discovery SHOULD expose concise metadata, loading detailed instructions only for relevant tasks. Prefer one primary skill per concern with complementary specialized/project/review layers, rather than competing frontend/color/architecture/testing/writing foundations. Where skills overlap, record priority, why both are needed, and conflict behavior; governing product/design contracts and constitution prevail. Manage context budget for small models; skill/prompt/plugin count is not a quality metric. Centrally maintained references MUST remain revision-resolvable and support future continuation without silent disappearance; dependency continuity follows [SEC-5](#sec-5).

<a id="skill-2"></a>
### SKILL-2 — Subordinate guidance and bounded skill execution

**Type:** ECOSYSTEM POLICY | **Origin:** USER POLICY | **Applies:** selection, invocation, and output of Agent Skills during development or application operations

The execution hierarchy is **Universal Rules → owner policy → App Master Plan → Phase/Task Contract → project-specific design/system rules → relevant Agent Skills → implementation**, subject to actual owner authority/approved exceptions under [GOV-3](#gov-3). A skill MUST NOT override governing rules, owner policy, Master Plan, Phase Contract, project design/system contracts, security boundaries, or authorization. External installed skills MUST NOT silently become universal policy. A skill may guide use of existing authorized capabilities; it MUST NOT independently grant filesystem, deployment, credential, canonical-mutation, or production access, nor inherit every capability available to its host AI. Enforce only the permissions required by the workflow through [AUTH-1](#auth-1) and [AI-2](#ai-2). Frontend review normally needs no production DB writes, secrets, or backup deletion; documentation guidance normally needs no deployment authority.

Skill output, including reviews, recommendations, plans, and classifications, MUST remain subject to evidence, relevant core validation/tests, project contracts, and applicable owner approval. Labels or successful skill execution do not establish factual truth or completion under [EVID-1](#evid-1), [TEST-1](#test-1), and [DEV-13](#dev-13). A skill reference MUST NOT replace project-specific phase objectives, files, constraints, target state, tests, evidence, or stopping conditions under [DEV-10](#dev-10). Materially guiding skill choices SHOULD be discoverable in phase/development metadata to support resumption; source/version/local modifications/permissions follow [SKILL-3](#skill-3). Neither a named adversarial skill nor this catalog authorizes the constitution's final attack under [GOV-4](#gov-4).

<a id="skill-3"></a>
### SKILL-3 — Skill supply-chain review, revisions, and lifecycle

**Type:** ECOSYSTEM POLICY | **Origin:** USER POLICY | **Applies:** third-party skill consideration/trusted use and maintenance of consequential reusable skills

Third-party Agent Skills MUST be treated as supply-chain inputs. Before trusted use, perform the **Skill Security Review** workflow in [SKILL-4](#skill-4): assess provenance/source/repository/author/version, inspect instructions and supporting resources, scripts/dependencies, requested tools, network/filesystem/shell access, credential exposure, prompt-injection behavior, hidden downloads, and update strategy. This may be performed by an authorized human or trusted tooling; it does not require first executing an unreviewed security-review package. Do not install and execute an Internet skill with full shell/credentials merely because it appears helpful or is described as “only a prompt.” Unreviewed resources remain untrusted under [IO-1](#io-1) and [AI-1](#ai-1).

Trusted reusable skills MUST preserve proportionate provenance and review state where consequential: name/purpose, source, version/revision or equivalent identity/digest, license, author/maintainer, local modifications, reviewed scope, and approving authority where required. Projects MUST be able to identify the revision that materially guided work when review/reproducibility matters. A materially changed remote revision MUST NOT silently replace a trusted skill during an active phase; reassess content, permissions, and affected contracts before trusted adoption. Record actual trust/version identity in the discoverable catalog under [SKILL-1](#skill-1); do not claim unperformed review or infer verified provenance.

Important reusable skills SHOULD have workflow-appropriate validation, such as fixtures, expected output structures, policy-compliance cases, permission tests, or adversarial cases; parsing a prose file alone establishes no trust. Review/modification history SHOULD preserve enough evidence to understand significant past work where needed. Obsolete, insecure, superseded, or incompatible skills MUST be marked and have their trusted invocation state reconsidered; old references do not justify continued automatic use. Preserve useful lineage without retaining unnecessary private payloads under [PRIV-1](#priv-1). General dependency/build safety and privilege boundaries in [SEC-1](#sec-1), [SEC-3](#sec-3), and [SEC-4](#sec-4) remain controlling.

Dynamically fetched remote instructions MUST remain untrusted until validated. Pin/verify content where practical, constrain network access, and record the exact retrieved revision or digest before trusted adoption; mutable `main` or `latest` MUST NOT silently change governing instructions mid-phase. Skill Security Review MUST include installer behavior, symlinks/path traversal, license, dynamic remote resources, and overlap/conflicts as well as scripts, dependencies, permissions, and credentials. Trust registration follows source → revision/license → static/content review → scripts/dependencies → permission/network/conflict review → version/digest → approved discoverable registry. Presence in a registry is a recorded trust disposition, not proof of immunity.

<a id="skill-4"></a>
### SKILL-4 — Universal workflow capability catalog

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
