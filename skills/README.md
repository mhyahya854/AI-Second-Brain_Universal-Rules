# Skills Intake Library and Controlled Integration Boundary

This directory is the repository's skill intake, provenance, and security review area. Imported packages under `_intake/` remain untrusted archive material by default: only packages that have passed the individual adoption gate in `SECURITY-POLICY.md` and been explicitly registered in `.agents/skills.json` may be exposed for active host discovery.

## Layout

- `_intake/github/` holds pinned upstream skill packages whose redistribution is permitted by verified license evidence (`2,305` imported package folders). No file in `_intake/` is modified during integration.
- `_provenance/licenses/` holds applicable upstream license/notice files (`189` files), with SHA-256 hashes recorded in `manifest.json`.
- `manifest.json` is the machine-readable catalog of every candidate (`2,634` candidate identities), pinned source commit, license status, package file hash, deduplication mapping, activation hint, and packaging finding.
- `SOURCE-MAPPING.md` and `audit/source-mapping.json` map the complete Instagram-Dump source snapshot (`8397dacc7d927552ff8f48891c4fa2d103bed90d`) to candidates, imports, or documented exclusions.
- `audit/` contains historical scanner evidence (`audit/scan-reports/`), `audit/SKILL-AUDIT-REPORT.md`, `audit/skill-results.json`, `audit/dependency-findings.json`, and migration/branch records. Historical audit receipts in `audit/` are immutable evidence records and are never rewritten to reflect later policy decisions.

## Controlled Repository-Local Integration (Phase 5 Policy)

The bulk library at `skills/_intake` is **not** a bulk automatic-discovery directory. Instead, repository-local enforcement uses two controlled host mechanisms at the repository root:

1. **`AGENTS.md` (Always-On Workspace Rule):** Loaded automatically by Antigravity / Gemini IDE, Gemini CLI, OpenAI Codex, OpenCode, and `AGENTS.md`-compatible hosts on every turn, task initialization, and session resumption across all **18 lifecycle stages (`0` through `17`)**.
2. **`.agents/skills.json` (Selective Skill Registration):** Exposes **only** individually security-approved (`PASS`) skill packages via explicit `include_only` filtering (`skills/_intake/github/DietrichGebert/ponytail` with `"include_only": ["ponytail"]`), keeping all `2,304` other intake folders (including sibling `INCOMPLETE` packages and all `QUARANTINED` packages) unexposed.

### Current Status of Owner-Designated Skills

| Skill | Canonical / Stable Identifier | Intake Path | Security Status | Phase 5 Integration Disposition |
|---|---|---|---|---|
| **Ponytail** (Always On, 100% of tasks) | `dietrichgebert/ponytail:skills/ponytail` (`github:dietrichgebert/ponytail@09c434ab73ca43761c5d8b0c5d341926c2fba710:skills/ponytail`) | `skills/_intake/github/DietrichGebert/ponytail/ponytail` | **`PASS`** (`SAFE`, risk `0`, `100.0%` coverage, `0` issues, `MIT`) | **ACTIVATED.** Compact operating layer enforced in `AGENTS.md`, `SKILL-1`, and `SKILL-2`; full `SKILL.md` (`9badd22a...`) exposed via `.agents/skills.json`. |
| **Unlazy** (Always On, 100% of tasks, Modes A–D) | `leonxlnx/unlazy:.` (`github:leonxlnx/unlazy@16671491f6679ad9378f52604d3bc2415b4120c7:.`) | `skills/_intake/github/Leonxlnx/unlazy/unlazy` | **`QUARANTINED`** (`DO_NOT_INSTALL`, risk `100`, `92.3%` partial coverage, `12` findings, `10` `.mjs` scripts, `MIT`) | **PREPARED / PACKAGE GATED BY SECURITY.** Proportional Modes A–D completion discipline and 10 Security Boundaries enforced in `AGENTS.md`, `SKILL-1`, `SKILL-2`, and `SKILL-3`; raw `_intake` package and `.mjs` scripts remain unexposed and unexecuted pending quarantine remediation/waiver in `SECURITY-POLICY.md`. |
| **Graphify** (Conditional evaluation on 100% of tasks) | `graphify-labs/graphify:graphify` (`github:graphify-labs/graphify@0a8cd4e1e342235fe53e881fb5d591bf0460071f:graphify`) | `skills/_intake/github/Graphify-Labs/graphify/graphify` | **`QUARANTINED`** (`DO_NOT_INSTALL`, risk `100`, `7.3%` partial coverage, `112` findings, `Apache-2.0`) | **CONDITIONAL POLICY CONFIGURED / PACKAGE BLOCKED BY QUARANTINE.** Evaluated on every task initialization; execution, hooks, and config installers remain strictly prohibited while `QUARANTINED`. |

### Updated Operational Recommendations vs. Historical Phase 4 Triage

Without altering historical audit receipts, current operational policy updates the prior Phase 4 triage recommendations as follows:

- **Lifecycle Stage Numbering:** The Universal Rules lifecycle consists of **18 stages numbered `0` through `17`** (`0- Start Here and Universal Rules` through `17- Preserving Memory and Learning`), never `1–18`.
- **Ponytail:** Elevated from a candidate global simplicity option to **mandatory always-on (`100%` of tasks across stages `0–17`)**.
- **Unlazy:** Added as the second **mandatory always-on discipline (`100%` of tasks, Modes A–D)**, with its raw executable package held at the `SECURITY-POLICY.md` quarantine gate until remediated or explicitly waived.
- **Graphify:** Reclassified from permanent exclusion to **mandatory conditional evaluation on every task**, gated by its `QUARANTINED` security blocker until a verified read-only, hook-free, non-config-mutating subset passes static review.
- **Caveman (`juliusbrussee/caveman`):** Not a mandatory global skill; `caveman` terse-voice remains excluded (`INCOMPLETE`), while its individually verified `PASS` software-engineering skills (`caveman-evidence-review`, `caveman-manage`, `caveman-optimize`, `investigate-first`, `lean-build`, `migration`, `safe-refactor`, `surgical-patch`, `verify-and-stop`) remain eligible for future task-specific approval.
- **Andrej Karpathy Skill (`duolahypercho/andrej-karpathy-skills:skills/andrej-karpathy-skill`, `PASS`):** Not a global substitute for Ponytail; eligible only as an optional task-specific specialist when compatible and independently useful (`multica-ai/andrej-karpathy-skills:skills/karpathy-guidelines` remains `INCOMPLETE` / unimported due to missing upstream license).

## Read before reviewing

Start with `audit/SKILL-AUDIT-REPORT.md` and `SECURITY-POLICY.md`. A scanner `SAFE` recommendation is not a guarantee. `CAUTION`, `DO_NOT_INSTALL`, incomplete coverage, unresolved license rights, and package integrity gaps block package exposure. No imported scripts, installers, hooks, MCP servers, or other executable content were run during intake or Phase 5 integration.
