<a id="plan-2"></a>
### 34.2. PLAN-2 — Pinned source ZIP reuse and assessment

**Type:** ECOSYSTEM POLICY | **Origin:** USER POLICY | **Applies:** application planning that considers existing projects and adoption of third-party source foundations

Promising projects MUST be assessed for suitability, source history, maintenance, code quality, security, licensing, platforms, portability, and adaptation cost. The preferred reuse mechanism is a **pinned source ZIP**, rather than creating a GitHub fork. Use a different acquisition mechanism only with a recorded concrete reason and applicable authority; source reuse does not require creating a fork.

An adopted source snapshot MUST record repository URL, exact revision/commit, ZIP origin, checksum or equivalent integrity evidence, license and obligations, imported scope, attribution retained, security-review disposition, and local modifications. Record available authentic source/signature evidence separately: a checksum alone does not authenticate an author. A public repository without an applicable license MUST NOT be assumed to grant modification or redistribution rights. Acquisition, dependencies, continuity, and redistribution remain subject to [SEC-3](#sec-3)–[SEC-5](#sec-5), [IO-1](#io-1), and [SKILL-3](#skill-3) where relevant.

Untrusted downloaded scripts/installers MUST NOT be executed before review. Inspect the actual adopted implementation and apply [DEV-14](#dev-14): preserve correct work, assess gaps, and repair deficiencies without indiscriminate rewriting. The App Plan MUST distinguish imported, modified, replaced, and newly implemented responsibilities.

