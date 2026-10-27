# Universal Rules for All Apps — MASTER PLAN

> Version: **1.1.1-locked-current-folder-json-candidate (unratified; built on RC4)**<br>
> Status: **OWNER-LOCKED NEW DESIGN — UNRATIFIED CONSTITUTIONAL AMENDMENT CANDIDATE; formal review and ratification remain separate**<br>
> RC4 integration started: 2026-10-17 UTC; resumed: 2026-10-18 UTC; historical rc3 consolidation: 2026-10-15 UTC<br>
> Document identifier: ECOSYSTEM-CONST-001<br>
> Source repository: https://github.com/mhyahya854/Universal-Rules<br>
> Policy and ratification authority: repository owner/user, unless explicitly delegated<br>
> RC4 baseline: `73b2e8adb0236af7d4e503e67f9d507148cc95b7`, MASTER_PLAN.md SHA-256 `07a0976686215cb68e4a0bf63d56aecfb9ec183e7946f84d4855f103fa110460`<br>
> Freeze identity and subsequent review results: revision-bound external receipt under section 42; never inferred from historical reviews

This single document contains the current candidate constitution, application planning/execution instructions, Green/Red/Fix procedure, historical preservation map, and technical research evidence. Its purpose is durable, user-owned, understandable, recoverable, portable, maintainable software with truthful evidence and bounded authority. It improves the probability of long-term usefulness without promising indefinite operation or flawless AI execution.

**Two different repository contracts:** the active **Universal Rules** tree contains exactly `MASTER_PLAN.md`. Future **application** repositories use the multi-folder planning and Codebase blueprint in [section 39](#s39). Application folders shown here are instructions for future products, not additional files in this constitutional repository. Git metadata is not a tracked constitutional file.

**NO FALLBACKS IN THE APP PLAN OR CODEBASE:** selected implementations fail honestly; [section 37](#s37) preserves explicit recovery, same-operation retries, independent local functionality, and deliberate platform/migration contracts without hidden substitution.

For the owner: start with [scope/authority](#s01), [ordered planning](#s34), [technology selection](#s35), [data survival](#s36), [visual direction](#s38), and [candidate status](#s30). For execution: use [future project entry points](#blueprint-1), [Project State and Continue](#exec-4), [numbered subphase contracts](#exec-2), and [completion gates](#exec-5). For constitutional review: use [GOV-5](#gov-5) and the complete [operating procedure](#s42). Rule anchors remain stable even when subsection numbers evolve.

<a id="contents"></a>
## 0. Navigation

1. [Scope and rule classification](#s01)
2. [Foundations and domain hazards](#s02)
3. [Definitions](#s03)
4. [Principals and delegation](#s04)
5. [Rust-first implementation](#s05)
6. [Feature-first architecture, shared core, and UI](#s06)
7. [Data lifecycle and application replacement](#s07)
8. [Authority, derivation, and reproducibility](#s08)
9. [Local and offline operation](#s09)
10. [Product platforms, portability, and visual assets](#s10)
11. [NAS support](#s11)
12. [Storage and crash consistency](#s12)
13. [Concurrency and conflict semantics](#s13)
14. [Operation outcomes and acknowledgements](#s14)
15. [Retries and deduplication](#s15)
16. [AI authority, tools, memory, and Hermes](#s16)
17. [Audit and provenance](#s17)
18. [Privacy, retention, and deletion](#s18)
19. [External editing and drift](#s19)
20. [Synchronization](#s20)
21. [Reversal and recovery](#s21)
22. [Backup and restoration](#s22)
23. [Import and export](#s23)
24. [Schema evolution and migrations](#s24)
25. [Security, secrets, and dependencies](#s25)
26. [Configuration, observability, and runtime lifecycle](#s26)
27. [Verification and evidence](#s27)
28. [Documentation, exceptions, and ratification](#s28)
29. [Anti-pattern index — non-normative](#s29)
30. [Candidate status and review continuation — non-normative](#s30)
31. [Application planning, continuity, and conformance](#s31)
32. [Universal Information Architecture Blueprint](#s32)
33. [Reusable Universal Agent Skills governance](#s33)
34. [Requirements-first planning and source reuse](#s34)
35. [Technology preferences after requirements](#s35)
36. [Data that survives the application](#s36)
37. [NO FALLBACKS in the App Plan or Codebase](#s37)
38. [Visual concepts, interaction modes, and named design guidance](#s38)
39. [Future application repository blueprint and feature organization](#s39)
40. [Beginner-readable implementation documentation and simplicity](#s40)
41. [Exact execution, limited repair, and evidence-bearing completion](#s41)
42. [Integrated constitutional operating procedure](#s42)
43. [Authorization provenance and historical preservation — non-normative](#s43)
44. [Technical factuality and source evidence — non-normative](#s44)
45. [User-owned data workspace and folder architecture](#s45)
46. [Mandatory per-file Current JSON, verified Folder JSON, optional global Master JSON](#s46)
47. [Revision integrity, external edits, and protected history](#s47)
48. [Trusted AI entry and bounded navigation](#s48)
49. [Workspace validation and lifetime feasibility](#s49)
50. [Menemora illustration and Open Engineering Decisions — non-normative](#s50)
51. [RC4 authority, reconciliation, and requirement coverage — non-normative](#s51)
52. [Topic 2: Optional Dual-JSON Recovery and Complete On-Site Backup — unratified design record](#s52)
53. [Universal Current JSON, Folder JSON and selective reconciliation — owner-locked unratified candidate](#s53)

