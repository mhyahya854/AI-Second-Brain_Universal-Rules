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

