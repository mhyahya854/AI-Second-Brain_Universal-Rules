<a id="plan-2"></a>
### 34.2. PLAN-2 — Pinned source ZIP reuse and assessment

**Type:** ECOSYSTEM POLICY | **Origin:** USER POLICY | **Applies:** application planning that considers existing projects and adoption of third-party source foundations

Promising projects MUST be assessed for suitability, source history, maintenance, code quality, security, licensing, platforms, portability, and adaptation cost. The preferred reuse mechanism is a **pinned source ZIP**, rather than creating a GitHub fork. Use a different acquisition mechanism only with a recorded concrete reason and applicable authority; source reuse does not require creating a fork.

An adopted source snapshot MUST record repository URL, exact revision/commit, ZIP origin, checksum or equivalent integrity evidence, license and obligations, imported scope, attribution retained, security-review disposition, and local modifications. Record available authentic source/signature evidence separately: a checksum alone does not authenticate an author. A public repository without an applicable license MUST NOT be assumed to grant modification or redistribution rights. Acquisition, dependencies, continuity, and redistribution remain subject to [SEC-3](../3-%20Deciding%20the%20Stack/307-%20Choosing%20Libraries%20and%20Dependencies.md#sec-3)–[SEC-5](../15-%20Packaging%20Deploying%20and%20Releasing/1502-%20Preparing%20Reproducible%20Production%20Builds.md#sec-5), [IO-1](../10-%20Building%20the%20Core%20and%20Backend/1008-%20Implementing%20Required%20Core%20Capabilities.md#io-1), and [SKILL-3](../7-%20Attacking%20and%20Freezing%20the%20Master%20Plan/706-%20Checking%20Skills%20Dependencies%20and%20Conflicts.md#skill-3) where relevant.

Untrusted downloaded scripts/installers MUST NOT be executed before review. Inspect the actual adopted implementation and apply [DEV-14](../9-%20Preparing%20the%20Development%20Environment/901-%20Verifying%20the%20Repository%20Starting%20State.md#dev-14): preserve correct work, assess gaps, and repair deficiencies without indiscriminate rewriting. The App Plan MUST distinguish imported, modified, replaced, and newly implemented responsibilities.

