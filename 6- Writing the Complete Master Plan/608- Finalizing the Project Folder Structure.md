<a id="s39"></a>
## 39. Future application repository blueprint and feature organization

The one-file Universal Rules repository and a future application's repository have different purposes. This section's folders belong to **future applications**, not the active constitutional repository, whose sole tracked file is `MASTER_PLAN.md`.

<a id="blueprint-1"></a>
### 39.1. BLUEPRINT-1 — Complete substantial-application blueprint

**Type:** DEFAULT | **Origin:** USER POLICY | **Applies:** substantial future application repositories, with proportionate physical simplification for tiny applications

The following is the detailed default conceptual blueprint implementing [DEV-6](../1-%20Deciding%20a%20Project/108-%20Selecting%20a%20Preliminary%20Project%20Blueprint.md#dev-6). Preserve its discoverable responsibilities. Physical names/layout MAY change when sound engineering or framework compatibility requires it, with an explicit mapping in repository entry instructions. Do not create meaningless empty folders, duplicate implementation areas that have no responsibility, or treat folder presence as evidence of implemented behavior. Tiny apps MAY simplify the hierarchy while preserving applicable safety, continuity, specification, and verification obligations.

```text
Application/
│
├── AGENTS.md
├── README.md
│
├── Master Plan/
│   │
│   ├── Languages and Data/
│   │   ├── 1- stack and languages used.md
│   │   └── 2- How the data is stored.md
│   │
│   ├── Master Plan/
│   │   └── master plan.md
│   │
│   ├── Research and Decisions/
│   │   ├── GitHub Research/
│   │   ├── Technical Comparisons/
│   │   ├── Architecture Decisions/
│   │   ├── Rejected Alternatives/
│   │   └── Evidence/
│   │
│   ├── Design/
│   │   ├── Visual Concepts/
│   │   ├── Approved Design/
│   │   ├── Design System/
│   │   ├── Motion/
│   │   └── Accessibility/
│   │
│   ├── Reviews/
│   │   ├── Frontend Reviews/
│   │   ├── Backend Reviews/
│   │   ├── Database Reviews/
│   │   ├── Architecture Reviews/
│   │   ├── Security Reviews/
│   │   ├── Performance Reviews/
│   │   ├── Integration Reviews/
│   │   └── Final Reviews/
│   │
│   ├── Phases/
│   │   ├── To Be Executed Phases/
│   │   │   ├── Phase-001/
│   │   │   │   ├── phase-001.md
│   │   │   │   ├── subphase-001-001.md
│   │   │   │   ├── subphase-001-002.md
│   │   │   │   └── subphase-001-003.md
│   │   │   └── Phase-002/
│   │   │
│   │   └── Done Phases/
│   │
│   └── project-state.md
│
└── Codebase/
    ├── Frontend/
    │   ├── Features/
    │   └── Shared/
    │
    ├── Backend/
    │   ├── Features/
    │   └── Shared/
    │
    ├── Database/
    │   ├── Schemas/
    │   ├── Migrations/
    │   └── Storage/
    │
    └── Documentation/
        ├── code-map.md
        ├── feature-map.md
        └── dependency-map.md
```

`AGENTS.md` MUST route an executor to applicable authority, the current App Master Plan, Project State, and the next authorized phase. `README.md` MUST provide a beginner-readable project entry point. Existing-app assessment under [DEV-14](../9-%20Preparing%20the%20Development%20Environment/901-%20Verifying%20the%20Repository%20Starting%20State.md#dev-14), relevant Skill metadata under [SKILL-1](../0-%20Start%20Here%20and%20Universal%20Rules/006-%20Global%20Skills%20and%20Always-On%20Rules.md#skill-1)–[SKILL-3](../7-%20Attacking%20and%20Freezing%20the%20Master%20Plan/706-%20Checking%20Skills%20Dependencies%20and%20Conflicts.md#skill-3), and additional review disciplines MUST remain discoverable even where the illustrated tree has no dedicated folder. Links or meaningful records may satisfy these responsibilities without empty scaffolding.

