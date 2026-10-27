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

