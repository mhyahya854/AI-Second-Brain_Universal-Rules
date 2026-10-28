<a id="dev-3"></a>
### 31.3. DEV-3 — Research before architecture freeze

**Type:** ECOSYSTEM POLICY | **Origin:** USER POLICY | **Applies:** new or substantially revised application architecture

After the idea is sufficiently defined and before architecture is frozen, planning MUST research relevant existing solutions: GitHub repositories, mature open-source applications, standards, libraries/frameworks, technical papers or documentation where useful, known architectural failures, and competing approaches. Scope research to the actual problem and authorized sources. Ask whether an existing solution solves a relevant problem better than the proposed design; copying another project is not the goal.

If no better solution is found, refine and retain the design. If a superior pattern is found, understand its advantage, determine applicable parts, and deliberately update the plan. Important comparisons and resulting decisions MUST be preserved under [DEV-8](../1-%20Deciding%20a%20Project/109-%20Recording%20Questions%20and%20Decisions.md#dev-8); lack of evidence MUST NOT be reported as completed research.

Before rebuilding a difficult subsystem from scratch, research whether mature existing software solves the relevant problem substantially better. Deliberately evaluate use as a dependency, wrapping, adaptation, vendoring, forking, or rejection, considering architecture fit, security, maintenance, licensing, portability, long-term control, and integration cost. Existence alone does not require adoption. Significant source foundations need provenance under [SEC-4](209-%20Choosing%20What%20to%20Reuse%20or%20Build.md#sec-4); Rust-first artifact/exception scope remains governed by [LANG-1](../3-%20Deciding%20the%20Stack/303-%20Choosing%20Programming%20Languages.md#lang-1).

[PLAN-1](../1-%20Deciding%20a%20Project/102-%20Identifying%20the%20Actual%20Problem.md#plan-1) orders initial review, mandatory existing-project discovery, and final design/technology selection. Pinned ZIP reuse and actual source assessment follow [PLAN-2](205-%20Evaluating%20Reusable%20Source%20Code.md#plan-2).

