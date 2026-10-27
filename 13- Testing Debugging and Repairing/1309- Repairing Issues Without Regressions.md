<a id="exec-3"></a>
### 41.3. EXEC-3 — Evidence-based bounded repair

**Type:** ECOSYSTEM POLICY | **Origin:** USER POLICY | **Applies:** compiler failures, test failures, and similar execution defects during a subphase

An executor MAY attempt correction within the current subphase's expressly authorized repair scope. Before execution, that scope MUST establish finite attempt and/or time limits appropriate to the task, with an unambiguous stop condition; a repair loop MUST NOT reset its budget by relabeling the same failure. Use actual compiler/test/runtime evidence to identify or narrow the cause, make a bounded correction, and rerun the affected validation and required regression checks. Record attempts, evidence, changes, results, and remaining uncertainty.

Repair MUST NOT rewrite unrelated components, disable or weaken required tests/acceptance, add dummy code or prohibited fallbacks, alter requirements, or change architecture without applicable authority. Escalate when the limit is reached, cause cannot be safely resolved, or repair exceeds scope. Record the precise blocker and needed planning decision in Project State. Endless error-repair loops are not progress; a failed repair leaves the subphase unfinished.

