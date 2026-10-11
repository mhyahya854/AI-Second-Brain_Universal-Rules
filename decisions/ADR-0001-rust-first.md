# ADR-0001 — Rust-first implementation

- Date: 2026-10-11
- Decision authority: repository owner/user, unless explicitly delegated
- Decision status: user-directed ecosystem policy; its constitutional wording is CANDIDATE
- Originally integrated in: 1.0.0-rc1 — not yet ratified
- Current wording aligned with: 1.0.0-working.1 — Pre-Ratification Working Candidate
- Governing clause: [LANG-1](../UNIVERSL%20RULES%20FOR%20ALL%20APPS.md#lang-1)
- Origin: the owner's Rust-first policy and subsequent integration instructions in this conversation

## Context

The initial constitution left implementation language entirely open. The owner has now selected Rust as the presumptive language for new ecosystem software. This is a deliberate ecosystem policy, not a claim that one language is technically optimal for every component. The adversarial review supports this distinction and the need for component-scoped exceptions.

## Decision

Use Rust by default for new applications, services, daemons, CLI tools, core libraries, storage and synchronization components, AI tool servers, and other software. A different language needs a documented technical justification and approval under the constitution's [exception process](../UNIVERSL%20RULES%20FOR%20ALL%20APPS.md#gov-3).

The decision question is: **What concrete technical requirement makes another language materially more appropriate for this component?** The burden of justification belongs to the deviation. This decision does not authorize rewriting existing applications or inspecting their implementations.

## Rationale

Rust offers useful language-level memory-safety and ownership tools, strong types, explicit error handling, native deployment options, and a shared implementation baseline. These can reduce particular classes of defects and ecosystem maintenance fragmentation when used well. The policy especially favors Rust around authoritative data, filesystem operations, concurrency, synchronization, long-running services, security boundaries, durable infrastructure, performance-sensitive processing, AI capability enforcement, and domain operations.

Those benefits depend on design and implementation. Rust is not evidence of domain correctness, durable writes, distributed consistency, safe FFI, secure capability boundaries, or correct concurrency semantics. Unsafe code, dependencies, storage assumptions, and operational behavior remain reviewable responsibilities.

## Exception criteria

A decision record identifies the component, alternative language, concrete reason Rust was rejected, why the alternative better meets requirements, scope, risks and mitigations, duration or review trigger where relevant, and actual approving authority. A component exception does not exempt the remainder of the application.

The policy concerns authored implementation components. Imported libraries and FFI dependencies do not automatically constitute a new authored non-Rust component. Generated bindings/code, SQL, configuration, shaders, schemas, platform resources, and frontend assets are classified by role, not merely extension. Authored executable implementation logic still needs applicable justification. Component-level or standing exceptions can cover related artifacts within their approved scope; separate paperwork for every generated file is unnecessary.

Exceptions are reconsidered on expiry or material changes to assumptions, rationale, or scope. They may be renewed, replaced, superseded, or withdrawn under [GOV-3](../UNIVERSL%20RULES%20FOR%20ALL%20APPS.md#gov-3); there is no arbitrary periodic review requirement for unchanged enduring exceptions.

Legitimate reasons include platform-required SDKs, host/plugin constraints, essential libraries impractical in Rust, specialized scientific or ML capabilities, interoperability or runtime constraints, deployment requirements, materially safer lifecycle or maintenance outcomes, and scripting/configuration/generated glue where Rust adds disproportionate complexity without meaningful benefit.

Staffing, certification, qualification, available expertise, and support continuity may be valid reasons when tied to material lifecycle or safety risk. An evidence-based support constraint is different from personal familiarity alone.

## Examples

Non-normative legitimate examples:

- A platform UI component uses its native SDK language while Rust implements suitable shared domain logic.
- A scientific component needs a validated Python numerical ecosystem with no practical equivalent meeting its qualification requirements.
- A plugin host mandates JavaScript; the exception is bounded to that interface and its necessary behavior.
- A deployment helper is a small shell script, with controlled inputs and effects, whose conversion would add tooling complexity without useful safety gain.
- A safety-critical subsystem has a qualified toolchain and support obligation that an available Rust toolchain cannot meet for its deployment lifecycle.

Insufficient on their own: familiarity, habit, trendiness, tutorials, framework preference, avoiding Rust's learning curve, copying an unrelated stack, or claiming faster prototyping without a concrete lifecycle advantage.

## Consequences and polyglot boundaries

Rust-first does not require every line to be Rust. Language boundaries should have deliberate ownership, interfaces, failure handling, build dependencies, and security responsibilities. Minimize accidental polyglot sprawl, while retaining boundaries that improve the system. Do not force FFI or complex bridges merely to make Rust usage appear larger.

The subsequent shared-product-core policy in [CORE-1](../UNIVERSL%20RULES%20FOR%20ALL%20APPS.md#core-1) requires one shared Rust implementation of product domain and durable behavior across clients where technically practical. Both platform-appropriate UIs and a shared cross-platform UI are valid under [UI-1](../UNIVERSL%20RULES%20FOR%20ALL%20APPS.md#ui-1). A UI language exception does not authorize separate rewrites of business logic. Technical core exceptions remain scoped and documented.

The policy adds learning and toolchain costs and may constrain hiring or dependency choices. Such costs should be evaluated concretely. They neither automatically invalidate the policy nor automatically defeat a justified exception. Future revisions require an owner decision; an AI reviewer cannot independently ratify or repeal this policy.

The constitution is the primary normative source. This ADR records rationale and examples; it does not create stronger obligations than its governing clause.
