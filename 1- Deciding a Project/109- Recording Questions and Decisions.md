<a id="dev-8"></a>
### 31.8. DEV-8 — Comparative research and explicit decisions

**Type:** ECOSYSTEM POLICY | **Origin:** USER POLICY | **Applies:** significant researched alternatives and architectural decisions

Research records MUST identify what was examined, why it was relevant, strengths, weaknesses, what was adopted or rejected, and why. Preserve important source/version references and comparative evidence sufficiently for future humans or AI to understand the decision without repeating major research. Such records do not require copying entire third-party repositories or restricted source material.

Research claims MUST distinguish verified evidence, inference/conditional evidence, and unresolved unknowns under [EVID-1](../0-%20Start%20Here%20and%20Universal%20Rules/009-%20Evidence%20and%20Truthful%20Completion.md#evid-1). Supporting evidence belongs in or is referenced through the Evidence responsibility under [DEV-6](108-%20Selecting%20a%20Preliminary%20Project%20Blueprint.md#dev-6). Repetition MUST NOT turn an assumption into a frozen architectural fact. Material unverified assumptions and conflicts MUST be resolved or explicitly accepted with their status intact at the [Plan Freeze Gate](../7-%20Attacking%20and%20Freezing%20the%20Master%20Plan/710-%20Freezing%20the%20Approved%20Master%20Plan.md#dev-5).

Important architectural decisions MUST be explicit and individually discoverable, including applicable Rust-core, storage-engine, sync-model, NAS-topology, UI, identity, AI/Hermes-boundary, and backup choices. A weaker model must not need to infer them from hundreds of pages of historical text. Decision records MUST identify current versus superseded decisions and link to the Master Plan where needed.

