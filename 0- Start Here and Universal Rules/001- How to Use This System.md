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

**Two different repository contracts:** the active **Universal Rules** tree contains exactly `MASTER_PLAN.md`. Future **application** repositories use the multi-folder planning and Codebase blueprint in [section 39](../6-%20Writing%20the%20Complete%20Master%20Plan/608-%20Finalizing%20the%20Project%20Folder%20Structure.md#s39). Application folders shown here are instructions for future products, not additional files in this constitutional repository. Git metadata is not a tracked constitutional file.

**NO FALLBACKS IN THE APP PLAN OR CODEBASE:** selected implementations fail honestly; [section 37](002-%20The%20Universal%20Constitution.md#s37) preserves explicit recovery, same-operation retries, independent local functionality, and deliberate platform/migration contracts without hidden substitution.

For the owner: start with [scope/authority](004-%20Rule%20Types%20and%20Applicability.md#s01), [ordered planning](../1-%20Deciding%20a%20Project/102-%20Identifying%20the%20Actual%20Problem.md#s34), [technology selection](../3-%20Deciding%20the%20Stack/301-%20Applying%20Existing%20Technology%20Defaults.md#s35), [data survival](../4-%20Planning%20the%20Architecture%20and%20Data/405-%20Designing%20Data%20Models%20and%20Storage.md#s36), [visual direction](../5-%20Designing%20the%20UI%20and%20UX/504-%20Creating%20Three%20Design%20Directions.md#s38), and [candidate status](../17-%20Preserving%20Memory%20and%20Learning/1710-%20Improving%20the%20Universal%20Rules%20System.md#s30). For execution: use [future project entry points](../6-%20Writing%20the%20Complete%20Master%20Plan/608-%20Finalizing%20the%20Project%20Folder%20Structure.md#blueprint-1), [Project State and Continue](008-%20Continuing%20Previous%20Work.md#exec-4), [numbered subphase contracts](../8-%20Dividing%20the%20Project%20Into%20Executable%20Steps/803-%20Dividing%20Subphases%20Into%20Atomic%20Tasks.md#exec-2), and [completion gates](../14-%20Reviewing%20the%20Entire%20Application/1409-%20Performing%20Independent%20Final%20Reviews.md#exec-5). For constitutional review: use [GOV-5](../7-%20Attacking%20and%20Freezing%20the%20Master%20Plan/708-%20Performing%20Independent%20Adversarial%20Reviews.md#gov-5) and the complete [operating procedure](../17-%20Preserving%20Memory%20and%20Learning/1710-%20Improving%20the%20Universal%20Rules%20System.md#s42). Rule anchors remain stable even when subsection numbers evolve.

<a id="contents"></a>
## 0. Navigation

1. [Scope and rule classification](004-%20Rule%20Types%20and%20Applicability.md#s01)
2. [Foundations and domain hazards](002-%20The%20Universal%20Constitution.md#s02)
3. [Definitions](002-%20The%20Universal%20Constitution.md#s03)
4. [Principals and delegation](../10-%20Building%20the%20Core%20and%20Backend/1007-%20Implementing%20Security%20and%20Authorization.md#s04)
5. [Rust-first implementation](../3-%20Deciding%20the%20Stack/303-%20Choosing%20Programming%20Languages.md#s05)
6. [Feature-first architecture, shared core, and UI](../4-%20Planning%20the%20Architecture%20and%20Data/402-%20Dividing%20the%20Application%20Into%20Features.md#s06)
7. [Data lifecycle and application replacement](../4-%20Planning%20the%20Architecture%20and%20Data/408-%20Planning%20Backup%20Migration%20and%20Recovery.md#s07)
8. [Authority, derivation, and reproducibility](../10-%20Building%20the%20Core%20and%20Backend/1001-%20Implementing%20Shared%20Data%20Types.md#s08)
9. [Local and offline operation](../4-%20Planning%20the%20Architecture%20and%20Data/407-%20Planning%20Offline%20and%20Sync%20Behavior.md#s09)
10. [Product platforms, portability, and visual assets](../3-%20Deciding%20the%20Stack/308-%20Checking%20Compatibility%20and%20Portability.md#s10)
11. [NAS support](../4-%20Planning%20the%20Architecture%20and%20Data/407-%20Planning%20Offline%20and%20Sync%20Behavior.md#s11)
12. [Storage and crash consistency](../10-%20Building%20the%20Core%20and%20Backend/1004-%20Implementing%20Storage%20and%20Persistence.md#s12)
13. [Concurrency and conflict semantics](../10-%20Building%20the%20Core%20and%20Backend/1005-%20Implementing%20Transactions%20and%20Migrations.md#s13)
14. [Operation outcomes and acknowledgements](009-%20Evidence%20and%20Truthful%20Completion.md#s14)
15. [Retries and deduplication](../10-%20Building%20the%20Core%20and%20Backend/1006-%20Implementing%20APIs%20and%20Services.md#s15)
16. [AI authority, tools, memory, and Hermes](../4-%20Planning%20the%20Architecture%20and%20Data/406-%20Planning%20Security%20and%20Permissions.md#s16)
17. [Audit and provenance](../10-%20Building%20the%20Core%20and%20Backend/1005-%20Implementing%20Transactions%20and%20Migrations.md#s17)
18. [Privacy, retention, and deletion](../6-%20Writing%20the%20Complete%20Master%20Plan/606-%20Documenting%20Data%20Security%20and%20Recovery.md#s18)
19. [External editing and drift](../12-%20Connecting%20and%20Completing%20the%20Application/1205-%20Connecting%20Complete%20Data%20Workflows.md#s19)
20. [Synchronization](../12-%20Connecting%20and%20Completing%20the%20Application/1206-%20Integrating%20Offline%20and%20Sync%20Capabilities.md#s20)
21. [Reversal and recovery](../12-%20Connecting%20and%20Completing%20the%20Application/1207-%20Integrating%20Error%20and%20Recovery%20Behavior.md#s21)
22. [Backup and restoration](../16-%20Maintaining%20Updating%20and%20Recovering/1606-%20Testing%20Backup%20and%20Restoration.md#s22)
23. [Import and export](../10-%20Building%20the%20Core%20and%20Backend/1008-%20Implementing%20Required%20Core%20Capabilities.md#s23)
24. [Schema evolution and migrations](../16-%20Maintaining%20Updating%20and%20Recovering/1605-%20Managing%20Data%20and%20Schema%20Migrations.md#s24)
25. [Security, secrets, and dependencies](../7-%20Attacking%20and%20Freezing%20the%20Master%20Plan/703-%20Finding%20Security%20and%20Privacy%20Risks.md#s25)
26. [Configuration, observability, and runtime lifecycle](../15-%20Packaging%20Deploying%20and%20Releasing/1506-%20Preparing%20Deployment%20Configuration.md#s26)
27. [Verification and evidence](../13-%20Testing%20Debugging%20and%20Repairing/1301-%20Preparing%20the%20Complete%20Test%20Environment.md#s27)
28. [Documentation, exceptions, and ratification](005-%20Selecting%20Applicable%20Rules.md#s28)
29. [Anti-pattern index — non-normative](010-%20Universal%20Readiness%20Checklist.md#s29)
30. [Candidate status and review continuation — non-normative](../17-%20Preserving%20Memory%20and%20Learning/1710-%20Improving%20the%20Universal%20Rules%20System.md#s30)
31. [Application planning, continuity, and conformance](../1-%20Deciding%20a%20Project/103-%20Defining%20the%20Project%27s%20Purpose.md#s31)
32. [Universal Information Architecture Blueprint](../5-%20Designing%20the%20UI%20and%20UX/503-%20Designing%20Information%20Architecture%20and%20Flows.md#s32)
33. [Reusable Universal Agent Skills governance](006-%20Global%20Skills%20and%20Always-On%20Rules.md#s33)
34. [Requirements-first planning and source reuse](../1-%20Deciding%20a%20Project/102-%20Identifying%20the%20Actual%20Problem.md#s34)
35. [Technology preferences after requirements](../3-%20Deciding%20the%20Stack/301-%20Applying%20Existing%20Technology%20Defaults.md#s35)
36. [Data that survives the application](../4-%20Planning%20the%20Architecture%20and%20Data/405-%20Designing%20Data%20Models%20and%20Storage.md#s36)
37. [NO FALLBACKS in the App Plan or Codebase](002-%20The%20Universal%20Constitution.md#s37)
38. [Visual concepts, interaction modes, and named design guidance](../5-%20Designing%20the%20UI%20and%20UX/504-%20Creating%20Three%20Design%20Directions.md#s38)
39. [Future application repository blueprint and feature organization](../6-%20Writing%20the%20Complete%20Master%20Plan/608-%20Finalizing%20the%20Project%20Folder%20Structure.md#s39)
40. [Beginner-readable implementation documentation and simplicity](../12-%20Connecting%20and%20Completing%20the%20Application/1203-%20Integrating%20Complete%20Features.md#s40)
41. [Exact execution, limited repair, and evidence-bearing completion](../8-%20Dividing%20the%20Project%20Into%20Executable%20Steps/802-%20Dividing%20Phases%20Into%20Subphases.md#s41)
42. [Integrated constitutional operating procedure](../17-%20Preserving%20Memory%20and%20Learning/1710-%20Improving%20the%20Universal%20Rules%20System.md#s42)
43. [Authorization provenance and historical preservation — non-normative](../17-%20Preserving%20Memory%20and%20Learning/1710-%20Improving%20the%20Universal%20Rules%20System.md#s43)
44. [Technical factuality and source evidence — non-normative](../3-%20Deciding%20the%20Stack/310-%20Finalizing%20Technology%20Decisions.md#s44)
45. [User-owned data workspace and folder architecture](../4-%20Planning%20the%20Architecture%20and%20Data/405-%20Designing%20Data%20Models%20and%20Storage.md#s45)
46. [Mandatory per-file Current JSON, verified Folder JSON, optional global Master JSON](../4-%20Planning%20the%20Architecture%20and%20Data/408-%20Planning%20Backup%20Migration%20and%20Recovery.md#s46)
47. [Revision integrity, external edits, and protected history](../4-%20Planning%20the%20Architecture%20and%20Data/408-%20Planning%20Backup%20Migration%20and%20Recovery.md#s47)
48. [Trusted AI entry and bounded navigation](../4-%20Planning%20the%20Architecture%20and%20Data/404-%20Defining%20APIs%20and%20Interfaces.md#s48)
49. [Workspace validation and lifetime feasibility](../13-%20Testing%20Debugging%20and%20Repairing/1304-%20Running%20End-to-End%20Tests.md#s49)
50. [Menemora illustration and Open Engineering Decisions — non-normative](../4-%20Planning%20the%20Architecture%20and%20Data/410-%20Reviewing%20Architecture%20Decisions.md#s50)
51. [RC4 authority, reconciliation, and requirement coverage — non-normative](../17-%20Preserving%20Memory%20and%20Learning/1710-%20Improving%20the%20Universal%20Rules%20System.md#s51)
52. [Topic 2: Optional Dual-JSON Recovery and Complete On-Site Backup — unratified design record](../4-%20Planning%20the%20Architecture%20and%20Data/408-%20Planning%20Backup%20Migration%20and%20Recovery.md#s52)
53. [Universal Current JSON, Folder JSON and selective reconciliation — owner-locked unratified candidate](../4-%20Planning%20the%20Architecture%20and%20Data/408-%20Planning%20Backup%20Migration%20and%20Recovery.md#s53)

