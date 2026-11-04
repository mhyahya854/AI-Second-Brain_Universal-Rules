<a id="s26"></a>
## 26. Configuration, observability, and runtime lifecycle

*Section 26 rules across lifecycle files: [RUN-1](#run-1), [RUN-2](../16-%20Maintaining%20Updating%20and%20Recovering/1601-%20Monitoring%20Application%20Health.md#run-2), [RUN-3](#run-3).*

<a id="run-1"></a>
### 26.1. RUN-1 — Explicit configuration and defaults

**Type:** DEFAULT | **Origin:** ARCHITECTURAL DECISION | **Applies:** configurable applications

Applications SHOULD separate environment-specific settings from portable logic and define deterministic resolution/validation. Built-in defaults are legitimate. CLI, environment, deployment file, user preferences, defaults is an illustrative order; managed policy may be non-overridable. Surface relevant effective non-secret settings and use supported host discovery or explicit configuration. Changing configuration does not imply environments have equivalent capabilities.

<a id="run-3"></a>
### 26.3. RUN-3 — Declared deployment and bounded lifecycle

**Type:** CONDITIONAL | **Origin:** DERIVED ENGINEERING RULE | **Applies:** supported deployment modes and persistent services

Applications MUST document supported runtime modes. Native binaries, desktops, mobile/browser runtimes, services, and OCI images are options, not universal simultaneous requirements. Container identities, mounts, permissions, and isolation must fit their role; packaging does not establish NAS semantics.

Startup MUST verify prerequisites for safe operation, including relevant schema compatibility/exclusivity. Read-only software need not demand writable canonical storage. Preflight success does not replace runtime handling. Shutdown SHOULD stop new work, complete or safely interrupt work, and flush/close according to contract within appropriate bounds. Crash safety cannot depend solely on graceful shutdown. Exit status and diagnostics MUST reflect material failures; process exit alone does not prove effects completed.

<a id="web-dev-1"></a>
### WEB-DEV-1 — Vibe-coded website/app release expectations

**Type:** CONDITIONAL | **Origin:** USER POLICY | **Applies:** launch or release of AI-assisted ("vibe-coded") websites/apps, with each item scoped to the product and deployment mode

This is the **vibe-coded app development** category of the owner's living three-category ruleset. AI-generated source or a good-looking demo is not proof of a shippable application. Before claiming launch readiness, verify the actual implemented functionality, supported routes and devices, ownership of dependencies/assets, permission boundaries, production build and deployment, and relevant security controls. The existing [DEV-13](../14-%20Reviewing%20the%20Entire%20Application/1408-%20Checking%20Rule%20and%20Requirement%20Compliance.md#dev-13), [UI-7](../5-%20Designing%20the%20UI%20and%20UX/510-%20Reviewing%20and%20Approving%20the%20Design.md#ui-7), [SEC-1](../7-%20Attacking%20and%20Freezing%20the%20Master%20Plan/703-%20Finding%20Security%20and%20Privacy%20Risks.md#sec-1), and [OUT-1](../0-%20Start%20Here%20and%20Universal%20Rules/009-%20Evidence%20and%20Truthful%20Completion.md#out-1) rules still govern verified completion.

**Avoid by default unless explicitly requested:** shipping an AI-generated visual prototype as a complete product, leaving a generic "made with AI" badge when removal is permitted and requested by this default, and omitting genuinely applicable public-site launch essentials merely because the coding environment offered a preview URL. Do not misrepresent removal that contractual/platform terms prohibit.

**Try to employ / verify before launch (as applicable):**

1. **Custom domain:** require or verify a custom domain for a public-facing website intended to launch as its real product. This does not mandate a public domain for offline, local-only, internal, CLI, or private self-hosted software unless explicitly specified by its App Plan.
2. **Favicon:** supply and verify a working favicon for an applicable website or web app, including real deployed pages.
3. **Branding:** remove a "made with AI" badge where permitted by the platform, attribution terms, license, or contract. If not permitted, do not circumvent conditions; record the limitation.
4. **Legal pages:** verify a privacy policy and terms and conditions for public-facing deployments where the owner's declared launch requirement or applicable processing/business/legal circumstances call for them. Content must truthfully reflect actual data handling and applicable terms; a generated template is not legal compliance proof. Non-public apps do not automatically require public website legal pages.
5. **Security review:** examine CORS, access control and authorization (not only login), exposed secrets/keys, publicly reachable endpoints, sensitive logging/data, dependencies, and other relevant vulnerabilities. Fix material findings before launch or record an owner-authorized scoped exception where the underlying rule permits one; never claim risks were eliminated without evidence.

These are conditional launch gates, **not** instructions to publish a private application, accept an incompatible platform, create fictional legal claims, or introduce internet dependencies into offline-first products. A launch check should record applicable / not applicable / passed / failed / not verified, the evidence, and any blockers. Do not confuse the marketing launch checklist with backend correctness.

<a id="web-deploy-1"></a>
### WEB-DEPLOY-1 — Explicit production-environment failure checks

**Type:** CONDITIONAL | **Origin:** USER POLICY | **Applies:** web/application deployments or production builds with environment-specific configuration, browser/API boundaries, or a database

Production readiness MUST explicitly check the following **when relevant**; passing development mode alone is insufficient:

1. **Missing environment variables or deployment secrets:** enumerate required configuration; verify values at build versus runtime as appropriate, and test missing/incorrect values. Fail clearly for missing required values rather than silently falling back to an unsafe environment. Do not print secret values in diagnostics.
2. **Hardcoded localhost/local URLs:** inspect production browser/client and server configuration, redirects, API bases, callbacks, asset paths, webhooks, and generated bundles for unintended localhost, 127.0.0.1, development domains, or machine-specific addresses. Keep genuine localhost dependencies for intentionally local/offline deployments; distinguish those from accidental publicly deployed settings.
3. **Database connectivity:** verify production connection settings, authentication, network/TLS policy, schema compatibility/migrations, pool sizing, startup/readiness handling, and appropriate failure diagnostics. Do not assume that build success proves database access or durability.
4. **Production-build-only failures:** run the actual production build and deploy/serve a representative artifact in the target-like environment; exercise applicable critical flows, SSR/SSG or client navigation, environment injection, route handling, static assets, permissions, migrations, and caching. Treat minification, tree-shaking, platform differences, and build-time substitutions as potential sources of defects.
5. **Incorrect CORS configuration:** for cross-origin browser access, verify actual allowed origins, methods, headers, preflights, redirects and credential behavior in the deployed topology; do not use indiscriminate origin reflection or wildcard credentials. CORS is a browser access policy, **not** replacement authentication, authorization, CSRF defenses, or server-side request validation. No CORS policy is required merely because a native/local process uses HTTP.

Record actual results and environment, including **passed, failed, not applicable, and not tested**. Any required failed or unrun release check blocks a verified "production ready" claim until remedied or accurately scoped under existing governance. Exercise failure and recovery paths, not only the happy path. Apply [RUN-1](#run-1), [RUN-3](#run-3), [RUN-2](../16-%20Maintaining%20Updating%20and%20Recovering/1601-%20Monitoring%20Application%20Health.md#run-2), [TEST-1](../13-%20Testing%20Debugging%20and%20Repairing/1301-%20Preparing%20the%20Complete%20Test%20Environment.md#test-1), and [WEB-SYS-1](../4-%20Planning%20the%20Architecture%20and%20Data/401-%20Designing%20the%20Application%20Architecture.md#web-sys-1); do not invent an SLO, mandatory CDN/orchestrator, or cloud dependency.
