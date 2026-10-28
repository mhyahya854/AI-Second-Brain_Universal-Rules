<a id="s05"></a>
## 5. Rust-first implementation

<a id="lang-1"></a>
### 5.1. LANG-1 — Rust as the mandatory ecosystem default

**Type:** ECOSYSTEM POLICY | **Origin:** USER POLICY | **Applies:** new software and components developed in this ecosystem

Rust is the presumptive language for applications, services, background processes, CLI tools, core libraries, storage engines, synchronization components, AI tool servers, and other software. A non-Rust selection MUST document why another language materially better meets the component's requirements and obtain applicable approval under [GOV-3](../0-%20Start%20Here%20and%20Universal%20Rules/003-%20Rule%20Priority%20and%20Authority.md#gov-3). The burden of justification belongs to the deviation.

The question is: **What concrete technical requirement makes another language materially more appropriate for this component?**

Valid reasons include platform-required SDKs/languages; critical capabilities unavailable or impractical in Rust; host/plugin constraints; specialized scientific/ML ecosystems; interoperability/runtime constraints; deployment requirements; materially safer lifecycle or maintenance outcomes; and scripting, configuration, or generated glue where Rust adds disproportionate complexity without meaningful benefit.

Familiarity, habit, popularity, trendiness, tutorials, framework preference, avoiding Rust's learning curve, or faster personal prototyping are insufficient by themselves. Staffing, qualification, certification, expertise, long-term maintenance, and operational support can justify a deviation when tied to material lifecycle or safety risk.

The decision MUST identify the component, selected language, concrete reason Rust was rejected, why the alternative better meets requirements, and whether scope is one component or the whole application. Polyglot systems are permitted with deliberate, maintainable boundaries. Rust is especially preferred for canonical state, filesystem operations, synchronization, concurrency, long-running services, security boundaries, durable infrastructure, performance-sensitive work, AI capability enforcement, and domain operations.

This language-selection requirement governs authored implementation components. Importing a library or an FFI dependency written in another language does not by itself constitute authoring a new non-Rust application component; dependency and boundary responsibilities still apply. Generated bindings/code, SQL, configuration, shaders, schemas, platform resources, and frontend assets MUST be classified by their role rather than their file extension. They are not automatically separate application components requiring individual exceptions. Authored executable frontend or other implementation logic remains subject to this policy. A documented component-level or standing exception MAY cover related implementation artifacts within its approved scope; generated glue does not exempt independently authored domain logic. The shared product core follows [CORE-1](../4-%20Planning%20the%20Architecture%20and%20Data/403-%20Designing%20the%20Shared%20Core.md#core-1).

Rust does not establish domain correctness, storage durability, distributed consistency, safe FFI, secure architecture, or correct concurrency semantics. Those remain architectural responsibilities. This policy does not itself mandate rewriting existing applications. Rationale and examples: [ADR-0001](https://github.com/mhyahya854/Universal-Rules/blob/a9c597c8f14536a4404a64494cf56e9015e1288a/decisions/ADR-0001-rust-first.md).

