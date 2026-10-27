<a id="dev-15"></a>
### 31.15. DEV-15 — Repository memory and the longevity test

**Type:** ECOSYSTEM POLICY | **Origin:** USER POLICY | **Applies:** application planning, documentation, and long-term continuation

Planning MUST ask: **Could another human or AI understand, maintain, repair, migrate, and continue this application years later using only the repository and documented external dependencies?** If not, planning/documentation is insufficient and the identified gaps MUST be addressed before claiming the relevant plan or phase ready.

The repository MUST carry durable development memory sufficient to establish what the app is, why major decisions were made, what is implemented, what remains, what was rejected, known risks, how to validate, and how to continue. Conversation history may assist planning but MUST NOT be required for continuation. Avoid unnecessary dependence on one developer's memory, one AI conversation, one model provider, one computer, undocumented file locations/decisions, or unsupported proprietary assumptions. Document necessary external dependencies and recovery/access requirements without committing secrets or retaining unnecessary sensitive conversation payloads; [PRIV-1](#priv-1) and [SEC-2](#sec-2) still apply.

