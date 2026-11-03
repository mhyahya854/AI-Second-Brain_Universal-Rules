# Universal Rules — Always-On Workspace Instructions (`AGENTS.md`)

Automatically loaded by supported agent hosts (Antigravity / Gemini IDE, Gemini CLI, OpenAI Codex, OpenCode, and `AGENTS.md`-compatible hosts) on every task initialization, turn, session start, and session resumption (`EXEC-4`) across all **18 lifecycle stages (`0` through `17`)**.

## 1. Global Authority and Precedence Hierarchy (`GOV-1`, `GOV-3`)

1. **Safety, privacy, legal constraints, and tool authorization** (`SAFE-1`, `SAFE-2`, `SEC-1`–`SEC-6`, `PRIV-1`, `PRIV-2`, `AUTH-1`, `AUTH-2`, `AI-1`, `AI-2`).
2. **Universal Rules constitution and owner-approved policies** (`0- Start Here and Universal Rules/001- How to Use This System.md` through `17- Preserving Memory and Learning/1710- Improving the Universal Rules System.md`).
3. **Approved project Master Plan and frozen acceptance criteria** (`DEV-4`, `DEV-5`, `DEV-7`, `EXEC-1`).
4. **Exact phase/subphase execution contract** (`EXEC-2`).
5. **Mandatory Ponytail operating behavior** (`dietrichgebert/ponytail:skills/ponytail`).
6. **Mandatory Unlazy operating behavior** (`leonxlnx/unlazy:.`).
7. **Approved applicable conditional or specialized skills** (conditional evaluation of `graphify-labs/graphify:graphify`; approved `PASS` specialist skills).
8. **Implementation choices**.

Apply Ponytail and Unlazy together on 100% of tasks; neither can override Tiers 1–4:
- **Ponytail** governs **HOW efficiently and simply** work is implemented.
- **Unlazy** governs **WHETHER the complete task has actually been finished and verified**.
- **Combined rule:** **Use the smallest complete solution, but never substitute minimal effort for complete work.**

## 2. Deterministic Task-Start Initialization Protocol

Execute on every task initialization, new/resumed session (`EXEC-4`), and context compaction across stages `0–17`:
1. **Constitutional Core:** Apply Stage `0` invariants and current lifecycle stage (`0–17`) rules.
2. **Select Ponytail (`ALWAYS ON, 100% OF TASKS`):** Apply Section 3 compact layer; read full `skills/_intake/github/DietrichGebert/ponytail/ponytail/SKILL.md` (exposed via `.agents/skills.json`) when detailed procedures or intensity changes (`lite|full|ultra`) are needed.
3. **Select Unlazy (`ALWAYS ON, 100% OF TASKS`):** Classify task into **Mode A, B, C, or D** and enforce Section 4 completion and security rules. Do **not** expose or execute the raw `QUARANTINED` package at `skills/_intake/github/Leonxlnx/unlazy/unlazy/` or its `.mjs` scripts (`gate-check.mjs`, `install-hooks.mjs`, `stop-hook.mjs`, etc.) until cleared in `skills/SECURITY-POLICY.md`.
4. **Evaluate Graphify (`EVALUATE ON 100% OF TASKS, SECURITY-GATED`):** Apply Section 5 rubric. While `graphify-labs/graphify:graphify` is `QUARANTINED`, never activate or execute it; if graph-worthy, record `BLOCKED_BY_QUARANTINE` and use authorized read-only tools.
5. **Optional Specialist Skills:** Select only `PASS` skills exposed in `.agents/skills.json` when task-relevant; specialist skills never deselect Ponytail or Unlazy.

## 3. Mandatory Skill #1: PONYTAIL — Always On (Stages `0–17`)

- **Identity:** `github:dietrichgebert/ponytail@09c434ab73ca43761c5d8b0c5d341926c2fba710:skills/ponytail` | `skills/_intake/github/DietrichGebert/ponytail/ponytail/SKILL.md` (`SHA-256`: `9badd22a32e19cb884e46dfa8d3aae82bb81dfa5484105b8b4f0262df823a509`, tree `98ba51ac8dbbd7089a29f7c97a96673db41f52940eb90817846b620c8e0c26b3`, `MIT`, `PASS`/`SAFE` scan `ffceb97ff166e7704314`).
- **Scope & Intensity:** Mandatory across all 18 stages (`0–17`), coding and non-coding (research, requirements, stack, architecture, UI/UX, Master Plan, reviews, decomposition, setup, backend, frontend, integration, testing, debugging, refactoring, deployment, maintenance, docs, memory, skills, security). Default `full` (`lite`: build asked + 1-line lazier option; `full`: ladder enforced; `ultra`: YAGNI extremist within unapproved scope).
- **6-Rung Ladder (run *after* full requirement & caller comprehension):** (1) **Skip it?** Unrequested/speculative outside approved contract -> skip in 1 line (`YAGNI`); (2) **Reuse what's here?** Existing repo helper/pattern -> reuse; (3) **Stdlib / native?** Stdlib, CSS, HTML, or DB constraint before custom code; (4) **Installed dependency?** Reuse before adding dependencies; (5) **One line?** 1 line over 50; (6) **Minimum complete code.**
- **Discipline:** Bug fix = grep all callers and fix root cause once at the shared path. No single-use interfaces/factories/config layers. Mark authorized scaling ceilings with `# shortcut: <limit>, <when to upgrade>`.
- **Subordinate Overrides:** (1) `DOC-1` overrides 1-line comment limits where `DOC-1` applies; (2) `EXEC-2`/`TEST-1` override test skipping; (3) Frozen Master Plan/`EXEC-2` scope overrides vague-request/`ultra` scope cuts; (4) `NOFALL-1`/`NOFALL-2` forbid using `shortcut:` for fallbacks or dummy code; (5) Never use Ponytail to skip features, drop requirements/docs/tests/edge cases, weaken security, leave partial integrations, delete data, or claim unverified success.

## 4. Mandatory Skill #2: UNLAZY — Always On (Modes A–D)

- **Identity:** `github:leonxlnx/unlazy@16671491f6679ad9378f52604d3bc2415b4120c7:.` | `skills/_intake/github/Leonxlnx/unlazy/unlazy/SKILL.md` (`SHA-256`: `0ea144724398f9df5ce4cb880ff472c8afee0193179eb2f2a5d82f1a0f633450`, tree `bc9419b367724e325234cc3b554c3eb9d3c5b2055e9ffdfa08aa2364e6552690`, `MIT`). Raw package is `QUARANTINED` (`4ceeba45a1d0999e04a0`) and kept inactive; completion discipline below is enforced on 100% of tasks.
- **10 Responsibilities:** (1) Define complete success; (2) Prevent premature completion; (3) Address every explicit requirement; (4) Detect omitted work; (5) Verify completed work; (6) Re-examine for defects/regressions; (7) Independently recheck delegated/parallel work; (8) Preserve honest evidence (`EVID-1`); (9) Prevent false completion claims (`OUT-1`); (10) Distinguish `VERIFIED`, `PARTIAL`, `BLOCKED`, `DEFERRED`, and `UNVERIFIED` work.
- **Proportional Modes:**
  - **Mode A (Trivial — typo, short rule explanation, small edit, factual Q&A):** In-context 5-point check (question answered? constraints respected? result accurate? verification complete? claims evidenced?). No `GATES.md` or Depth Tree.
  - **Mode B (Standard — bug fix, feature, multi-file edit, component, tests):** Reuse `EXEC-2` contract; check every required outcome and failure path with bounded verification before completion.
  - **Mode C (Complex — full apps, migrations, large refactors, major audits, multi-stage work):** Explicit acceptance gates, coherent Depth Tree (no arbitrary depth padding), task ownership, dependency order, leaf verification, parent re-verification, integration tests, and `EXEC-5` reconciliation.
  - **Mode D (Delegated/Parallel):** Resolve dependencies before dispatch, declare disjoint `WRITE_SET` file ownership, independently verify returned subagent work and unit integration, use concurrency only when host-supported, and never invent sessions/handles.
- **10 Security Boundaries & File Policy:** (1) Never auto-approve inherited `CHECK` commands; (2) Never execute untrusted `CHECK` commands uninspected; (3) Inspect exact command, scripts, cwd, shell, env, and permissions first; (4) Respect approval requirements; (5) Never treat approval storage as a sandbox; (6) Never run unreviewed/quarantined code to pass a gate; (7) Never install the Claude Code stop hook without explicit approval; (8) Never modify user-global agent settings; (9) No blanket permission to install tools, delete files, or access other repos; (10) Security stops override completion pressure (report `BLOCKED`, never fabricate passing checks). Avoid unnecessary `GATES.md`/`PLAN.md`/status files; keep transient state outside tracked source; deliver all progress/final reports in chat only unless an artifact is explicitly requested.

## 5. Conditional Skill #3: GRAPHIFY — Evaluated Every Task, Security-Gated

- **Identity & Status:** `github:graphify-labs/graphify@0a8cd4e1e342235fe53e881fb5d591bf0460071f:graphify` (`skill.md` `SHA-256`: `75ce4bddb9e118a9d72ded3e7f8281d670943dce853ac5886f2b99a2d8726e5b`, `Apache-2.0`) — **`QUARANTINED`** (`DO_NOT_INSTALL`, scan `5d4d28aef1208425732c`).
- **Evaluation Rubric:** *Suitable:* large codebases, cross-file dependency/architecture mapping, complex refactoring, circular dependency analysis, repo comprehension, structural impact/integration review. *Unsuitable:* trivial edits, small isolated files, simple factual answers, local comprehension sufficient, or graph cost > benefit. Weigh repo size, complexity, existing docs, accuracy gain, runtime cost, permissions, security status, and simpler read-only tools.
- **Hard Gate:** Never activate or execute Graphify, its hooks, or config installers while `QUARANTINED`. When a task is graph-worthy, record `RELEVANT_BUT_BLOCKED_BY_QUARANTINE` and use authorized read-only tools.

## 6. Small-Model Context Architecture (~4B Execution & ~1B Navigation Targets)

Assemble every bounded task packet (`DEV-11`, `EXEC-6`, `HERMES-2`) in **7 ordered slots**:
1. **Constitutional core** (Stage `0` + current stage rules).
2. **Mandatory Ponytail layer** (permanent slot; Section 3 compact layer; load full 874-token `SKILL.md` on demand).
3. **Mandatory Unlazy layer** (permanent slot; Section 4 Mode A/B/C/D checklist & security boundaries).
4. **Exact task contract** (`EXEC-2` scope, write set, acceptance criteria).
5. **Relevant file excerpts** (bounded to touched/referenced lines).
6. **Selected optional skills** (empty unless an approved `PASS` skill—or Graphify when relevant + security-approved—is needed).
7. **Verification criteria** (`TEST-1`, `EXEC-5`, `OUT-1`, `EVID-1`).

Never allow token compaction or specialist skills to drop Slots 1–4 or Slot 7; split oversized tasks (`EXEC-2`) or escalate model tier instead.
