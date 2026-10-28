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

MUST describes candidate conformance, not proof of adoption. Examples, implementation notes, ADR rationale, and historical reviews add no normative obligations. Sections 3, 29, and 30 are interpretive or informative and defer to governing rules. Deviations and conflicts follow [GOV-3](003-%20Rule%20Priority%20and%20Authority.md#gov-3); approval cannot make an unsupported technical guarantee true.

This file is the single current constitutional source. Sections 34–41 integrate later owner decisions; they refine the named earlier clauses rather than leaving superseded wording active. [Section 42](../17-%20Preserving%20Memory%20and%20Learning/1710-%20Improving%20the%20Universal%20Rules%20System.md#s42) operationalizes GOV-3–GOV-5 without independent override authority. Sections 45–49 integrate the later RC4 workspace decisions within their stated applicability; sections 50–51 contain non-normative examples, open decisions and coverage. Sections 43–44 contain historical non-normative preservation/research evidence; external references are provenance, not missing operating instructions. When an actual contradiction remains, stop affected decisions and record it for authorized repair under GOV-3; do not silently select convenient wording. The constitution governs conformance; actual owner authority may amend policy or approve recorded scoped exceptions, while approval cannot make an unsupported engineering claim true.

