<a id="port-3"></a>
### 10.3. PORT-3 — Declared Product Platform Scope

**Type:** ECOSYSTEM POLICY | **Origin:** USER POLICY | **Applies:** application product scope and supported clients

Each application MUST declare its actual Product Platform Scope or scopes and concrete support matrix under [PORT-1](#port-1), following requirements rather than assuming every product needs every platform. Desktop-only, mobile-only, desktop/mobile/tablet, web, and a justified narrower subset are valid product definitions. Scopes do not require every CLI, library, or service to acquire a graphical or mobile interface. Record technical reasons, intended users, supported configurations and limits; formal departures from an applicable ecosystem policy remain governed by [GOV-3](#gov-3).

| Scope | Product targets and evidence |
|---|---|
| DESKTOP | Consider Windows, macOS, and Linux as the normal desktop/laptop scope; justify a narrower actual product scope. Where Linux is supported, assess Linux Mint's current stable Ubuntu-based release, Ubuntu LTS, Arch Linux, and CachyOS explicitly. |
| MOBILE | Consider Android, iPhone/iOS, iPadOS/iPad, and applicable Android tablets; declare the actual phone/tablet subset and adaptive behavior under [UI-2](#ui-2). |
| UNIVERSAL DEVICE APPLICATION | This claimed scope targets Windows, macOS, Linux, Android, iPhone/iOS, iPadOS, and applicable Android tablets. Name any incomplete targets accurately. Web MAY additionally be included. |
| WEB | Declare supported browsers, versions/capabilities and evidence. Web support is distinct from native application support. |

Linux Mint, Ubuntu LTS, Arch Linux, and CachyOS MUST NOT be casually omitted from desktop-Linux assessment or assumed interchangeable. For each, record first-class supported/tested, planned/unverified, compatibility/best-effort, or unsupported status, the concrete reason, versions or rolling snapshots, material environment assumptions, and the testing commitment. Arch Linux and CachyOS remain important targets; Ubuntu LTS and Linux Mint remain explicit stable-distribution assessment targets. An intentionally narrower support contract is a recorded product decision, not a claim that omitted systems passed.

Every declared first-class supported target MUST receive applicable installation/packaging, launch, updates, filesystem, permissions, core-feature, and native/system-integration validation. State automated/manual coverage and limits under [TEST-1](#test-1). A declared target awaiting implementation/testing MUST remain labeled accordingly. Passing Ubuntu or Mint tests does not validate Arch, CachyOS, or all Linux distributions. Framework support or a successful build is not verified runtime support. Within the declared desktop-Linux scope, other mainstream Linux distributions remain compatibility/best-effort targets where dependencies permit unless explicitly promoted to first-class support or excluded by the justified narrower support contract. Best-effort status is not verified support. [TECH-3](#tech-3) governs platform/frontend investigation.

