# Security policy for imported skills

## Scope and quarantine

Every package under `_intake/` is untrusted source material. It is not loaded by an agent, cannot trigger automatically, and receives no filesystem, shell, network, credential, or MCP permission from this library. Never execute an imported script, installer, hook, server, or binary during review.

## Provenance and integrity

Each candidate is pinned to an upstream commit and exact source subdirectory. SHA-256 hashes cover each imported source file and content tree. License evidence is copied and hashed when redistribution is allowed. A package without verified redistribution permission is registry-only. Do not remove or alter an upstream security finding to obtain a cleaner scan. Record all packaging repairs with original and revised hashes.

## Required scanner

The required baseline is NVIDIA SkillSpector static analysis, run individually for each unique imported package folder using the pinned CLI and `--no-llm --format json`. Capture stdout, stderr, exit code, scanner version, source commit, package identity, and time. Inspect JSON recommendation, issue severity, and coverage/completeness fields; exit code zero alone is never a pass. Re-scan after any package repair.

Semantic LLM review is optional only when a reviewed backend is available and source handling is authorized. No package text, user secrets, or protected information may be sent to an external provider without authorization. Unavailable semantic coverage must be disclosed.

## Statuses

- `PASS`: verified provenance and package integrity; complete required static review; no blocking finding; permitted capabilities and declared dependencies reviewed.
- `CAUTION`: nonblocking finding or unresolved activation concern; human review required before any future adoption.
- `FAIL`: confirmed unacceptable behavior or critical security defect.
- `QUARANTINED`: dangerous or suspicious package isolated from use.
- `INCOMPLETE`: missing required resources, incomplete scanner coverage, unresolved integrity/licensing, or unavailable required evidence.
- `NOT_APPLICABLE`: repository mention is not an importable agent skill.

A scanner `SAFE` recommendation supports, but does not establish, `PASS`. `CAUTION` never maps to `PASS`. `DO_NOT_INSTALL` is never enabled. High-risk evidence remains quarantined.

## Approval gate

No skill is activated merely by existing in `_intake/`. Adoption requires verification of individual source commit, license copy, package file hashes, SkillSpector JSON report, dependency findings, constitutional compatibility, and permission boundaries. Only packages that satisfy `PASS` (or receive an explicit, revision-bound owner security exception after complete static remediation) may be exposed in `.agents/skills.json`.

## Phase 5 Individual Package Security Dispositions

### 1. `dietrichgebert/ponytail:skills/ponytail` — `PASS` (Approved & Exposed)

- **Pinned Source:** `https://github.com/DietrichGebert/ponytail` at `09c434ab73ca43761c5d8b0c5d341926c2fba710` (`SKILL.md` SHA-256: `9badd22a32e19cb884e46dfa8d3aae82bb81dfa5484105b8b4f0262df823a509`; tree SHA-256: `98ba51ac8dbbd7089a29f7c97a96673db41f52940eb90817846b620c8e0c26b3`; MIT license SHA-256: `fb1bc6909ac3ef82d5c22106e32ef682b0cff66788fa915fb9b53b15c9d2f3ab`).
- **Scan Evidence:** `audit/scan-reports/ffceb97ff166e7704314.json` — CLI exit `0`, recommendation `SAFE`, risk score `0` (`LOW`), coverage `100.0%` (`complete`), `0` issues, `0` scripts, `0` dependencies.
- **Disposition:** Approved for repository-local exposure via `.agents/skills.json` (`"include_only": ["ponytail"]`, excluding sibling `INCOMPLETE` folders `ponytail-audit`, `ponytail-debt`, `ponytail-gain`, `ponytail-review`) and enforced on 100% of tasks via `AGENTS.md`, `SKILL-1`, and `SKILL-2` with subordinate constitutional overrides (`DOC-1`, `EXEC-2`, `TEST-1`, `NOFALL-1`, `NOFALL-2`).

### 2. `leonxlnx/unlazy:.` — `QUARANTINED` (Prepared in Policy; Raw Package & Scripts Gated)

- **Pinned Source:** `https://github.com/Leonxlnx/unlazy` at `16671491f6679ad9378f52604d3bc2415b4120c7` (`SKILL.md` SHA-256: `0ea144724398f9df5ce4cb880ff472c8afee0193179eb2f2a5d82f1a0f633450`; tree SHA-256: `bc9419b367724e325234cc3b554c3eb9d3c5b2055e9ffdfa08aa2364e6552690`; `26/26` files verified; MIT license SHA-256: `4575a543ab88dad12ccea7d97e563d0bce5b448b06072e65d3264497dad326df`; zero npm dependencies).
- **Scan Evidence:** `audit/scan-reports/4ceeba45a1d0999e04a0.json` — CLI exit `1`, recommendation `DO_NOT_INSTALL`, risk score `100` (`CRITICAL`), coverage `92.3%` (`partial`: `24/26` complete, `2/26` partial), `12` findings (`5 HIGH`, `7 MEDIUM`).
- **Complete Static Inspection of All 26 Files:**
  - **Causes of `partial` (`92.3%`) coverage:** (1) `SKILL.md` lines 12, 38, 98 reference runtime files (`GATES.md`, `.claude/settings.local.json`, `.unlazy-hook-state.json`) flagged as `reference_missing`; (2) `scripts/gate-check.mjs` and `scripts/lib/gates.mjs` define a terminal-output sanitizer regex `/[\u0000-\u001f\u007f-\u009f\u061c\u200e\u200f\u2028-\u202e\u2066-\u2069]/` (`stripUnsafeTerminalText`) that strips C0/C1 control and Unicode bidi characters from untrusted command output, which SkillSpector flagged as `obfuscated_instruction_text`; (3) `scripts/lib/gates.mjs` (`953` lines) hit `static_parse_limit` on `static_patterns_tool_misuse`.
  - **Causes of `12` findings:** `MP3` (`HIGH`, 2x: prose `"never invent a handle or delete state"` in `README.md:142` and `delete state.sessions[sessionKey]` in `scripts/stop-hook.mjs:95`); `AS1` (`HIGH`, 2x: `.claude/settings*.json` references in `SECURITY.md:58` and `scripts/install-hooks.mjs:19`); `E4` (`HIGH`, 1x: directory tree example containing `status.log` and `session` in `references/parallel.md:15`); `RA2` (`MEDIUM`, 4x: `GATES.md` / `ABANDON:` / `--reverify` persistence docs); `RP1` (`MEDIUM`, 1x: unpinned `npx skills add Leonxlnx/unlazy` in `README.md:22`); `LP3` (`MEDIUM`, 1x: missing `allowed-tools` in `SKILL.md:1`); `TR2` (`MEDIUM`, 1x: `"do not stop until it is done"` in `SKILL.md:1`).
  - **Bundled `.mjs` Scripts & Permissions:** `gate-lint.mjs` and `dispatch-check.mjs` are pure static parsers; `gate-check.mjs` executes `CHECK:` commands via `check-supervisor.mjs` only when an exact SHA-256 approval record exists in `UNLAZY_APPROVAL_DIR` / `~/.unlazy/approved` or `--approve` is passed (`--status` is read-only and never invokes a shell); `install-hooks.mjs` and `stop-hook.mjs` modify `.claude/settings*.json` and `.unlazy-hook-state.json`.
- **Disposition & Remediation Gate:** Because `DO_NOT_INSTALL` (`QUARANTINED`) packages are never enabled in `.agents/skills.json`, the raw `skills/_intake/github/Leonxlnx/unlazy/unlazy` package and its 10 `.mjs` scripts remain unexposed and unexecuted. Unlazy's proportional completion methodology (Modes A–D) and 10 Security Boundaries are enforced through `AGENTS.md`, `SKILL-1`, `SKILL-2`, and `SKILL-3`. Full package exposure requires either: (a) a carved-out documentation-only derivative (excluding `install-hooks.mjs` and `stop-hook.mjs`, with ASCII-escaped bidi regexes if scripts are retained) that achieves a `SAFE` / `PASS` SkillSpector re-scan, or (b) an explicit revision-bound owner waiver for `16671491f6679ad9378f52604d3bc2415b4120c7` after independent static review.

### 3. `graphify-labs/graphify:graphify` — `QUARANTINED` (Conditional Policy Configured; Package Blocked)

- **Pinned Source:** `https://github.com/Graphify-Labs/graphify` at `0a8cd4e1e342235fe53e881fb5d591bf0460071f` (`skill.md` SHA-256: `75ce4bddb9e118a9d72ded3e7f8281d670943dce853ac5886f2b99a2d8726e5b`; tree SHA-256: `252373d5ab09123474aabfba2cc845d09fec8daca0481a16a5b6fc16c17c1bd9`; `234/234` files verified; Apache-2.0 license SHA-256: `3448ea175bba09f6fed8a743000139fb4c7112de83f164355b5540b158576621`).
- **Scan Evidence:** `audit/scan-reports/5d4d28aef1208425732c.json` — CLI exit `1`, recommendation `DO_NOT_INSTALL`, risk score `100` (`CRITICAL`), coverage `7.3%` (`partial`: `17/234` complete, `217/234` partial), `112` findings (`37 HIGH`, `73 MEDIUM`, `2 LOW`), including `AST5` (`os.execvpe` in `__main__.py:795`), `RA1` (self-modifying skill refresh in `__main__.py:1068-1080`), Git hook installers (`hooks.py`), global/workspace agent config writers (`install.py` and `always_on/*.md`), and external command/network runners (`google_workspace.py`, `ingest.py`, `llm.py`, `serve.py`).
- **Disposition & Future Read-Only Feasibility:** Strictly inactive and blocked from execution while `QUARANTINED`. Every task evaluates Graphify's suitability (`AGENTS.md` Section 5, `SKILL-1`, `SKILL-2`), but any graph-worthy task must record `BLOCKED_BY_QUARANTINE` and use authorized read-only tools. A future safe read-only mode is technically feasible only if the deterministic tree-sitter AST extraction and local NetworkX query modules (`extract.py`, `extractors/`, `cluster.py`, `analyze.py`, `build.py`) are isolated from `install.py`, `hooks.py`, `watch.py`, `ingest.py`, `google_workspace.py`, `llm.py`, `serve.py`, and `always_on/`, and that isolated subset independently passes a 100%-coverage SkillSpector scan and owner approval. No such mode is approved today.
