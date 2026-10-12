# Green Flag UI / product / Agent Skill research matrix

Date: 2026-10-12 (owner/client date). Candidate baseline: `bb0fac006cee6637cd3f4dff36a10bd0d4275ab4`.

This is non-normative evidence. Static source reads were performed before further edits under the newly supplied master prompt. An earlier authorized UI/skills draft was already uncommitted when that prompt arrived; it was preserved rather than reset. No downloaded installer, skill, script, binary, or package was executed. Git and raw GitHub files were retrieved; source code was treated as data.

## Source hierarchy and limits

Owner policy governs. Tier A is relevant standards/primary guidance; Tier B is first-party/maintained implementation evidence; Tier C is practitioner/community hypothesis. Popularity cannot override accessibility, authority, or security. A first-party repository does not make its language/framework/host-specific mechanisms universal.

Direct official web retrievals were blocked by the network proxy (`Tunnel connection failed: 403 Forbidden`). The mandatory live-source research is therefore not fully complete. Official repository alternatives provide useful partial evidence but cannot honestly be described as those inaccessible web pages. No claim of complete Green Flag research or source licensing/security certification is made.

## Pinned repository matrix

Every revision below is the exact HEAD retrieved in this pass; commit dates are source metadata, not evidence of maintenance quality or future support. File digests and scope are listed later. Recommendations concern process extraction/reference, not approval to install.

| Source | Exact revision / commit date | Tier | License observed | Adopted principles | Rejected / security and scope notes |
|---|---|---|---|---|---|
| [anthropics/claude-code](https://github.com/anthropics/claude-code/tree/3deb873687379f0c199a69fdaccc65f0865f7a29) | `3deb873687379f0c199a69fdaccc65f0865f7a29` / 2026-10-11T19:07:16Z | A/B | Commercial terms / all rights reserved | Intentional brief and composition, codebase exploration before architecture, confidence-filtered review. | Reject fixed vendor models, GH-comment authority, blanket aesthetic bans, SDK auto-install/cloud review without actual authorization. Security hooks include SDK bootstrap and external Claude review; not executed. |
| [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official/tree/f359d43b406057f1a8cdbc4ea93b827642c162e6) | `f359d43b406057f1a8cdbc4ea93b827642c162e6` / 2026-10-10T19:41:21-07:00 | A/B | Apache-2.0 | First-party frontend/feature/review/security workflows corroborate modular process and scoped tools. | Apache license read for official repository and frontend skill; individual distributions still need applicable notices/review. No plugin installed. |
| [openai/codex](https://github.com/openai/codex/tree/0c329ad2c9d5a2592128a1d536c66e16f9397e46) | `0c329ad2c9d5a2592128a1d536c66e16f9397e46` / 2026-10-12T19:02:36Z | A/B | Apache-2.0 | Official inspectable skill/prompt references; audit instructions, bound execution, and preserve tool security. | docs/skills.md is only a pointer to an inaccessible live page, not a substitute for that page. Local prompting fallback is evidence, not independent inspection of the named live blog. |
| [openai/openai-cookbook](https://github.com/openai/openai-cookbook/tree/5bd6cb40b6b84b69b2032d810610aa85064102df) | `5bd6cb40b6b84b69b2032d810610aa85064102df` / 2026-10-09T12:41:21-07:00 | A | MIT | Skills package instructions/scripts/assets; hosted or local shell, repeatable procedures and version-aware use. | Reject universal cloud-shell/API/provider dependence or treating example commands as authorization to execute. |
| [w3c/wcag](https://github.com/w3c/wcag/tree/23bad5904949904275a08f1c6e395b78a02aa6f3) | `23bad5904949904275a08f1c6e395b78a02aa6f3` / 2026-10-04T20:02:22+01:00 | A | W3C document/software terms | Keyboard, non-color-only meaning, contrast, focus, dragging alternatives, target size and disabling interaction motion support accessible outcomes. | Read official source criteria, not the blocked published snapshot. Distinguish applicable WCAG levels/web scope; do not impose every numeric criterion on every native/headless app. |
| [w3c/aria-practices](https://github.com/w3c/aria-practices/tree/0f765e4dc33e966026114ac12a8380db1de3b787) | `0f765e4dc33e966026114ac12a8380db1de3b787` / 2026-09-29T22:17:08-07:00 | A | W3C document/software terms | Accessible names/descriptions and explicit keyboard/focus handling; ARIA attributes do not implement keyboard behavior. | APG informs web-widget implementation; do not require ARIA in native UI or confuse guidance/examples with universal conformance. |
| [microsoft/fluentui](https://github.com/microsoft/fluentui/tree/389e06cc77c7f3621bf2af7dea251fc12fe68a2f) | `389e06cc77c7f3621bf2af7dea251fc12fe68a2f` / 2026-10-12T19:06:02+02:00 | A/B | MIT | Semantic tokens protect themes/high contrast; component accessibility review and purposeful motion. | Fluent repository evidence is not independent inspection of blocked Fluent 2 website. Reject package/token names and archived motion values as universal requirements. |
| [material-components/material-web](https://github.com/material-components/material-web/tree/47adb655bd7a88c4d62e8faac2873084eed555dc) | `47adb655bd7a88c4d62e8faac2873084eed555dc` / 2026-10-07T14:17:40-07:00 | A/B | Apache-2.0 | Semantic light/dark color roles, typeface and shape tokens enable coherent themes. | Material component docs are additional comparative evidence; reject one Material visual style, token naming, or web stack universally. |
| [pbakaus/impeccable](https://github.com/pbakaus/impeccable/tree/245ad82def45831dc56a21b683c7a1ff530b06cc) | `245ad82def45831dc56a21b683c7a1ff530b06cc` / 2026-10-12T10:12:50-07:00 | B/C | Apache-2.0 | Hierarchy, audit/distill/polish, context-aware design systems and iterative rendered review. | Launcher can download an executable into a user cache; browser tooling and hooks expand surface. No binary or installer executed. Reject its authority-sounding claims and categorical tint/font/style prescriptions. |
| [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill/tree/7246805992a42b7bba37d4cac83b01416f0c6c44) | `7246805992a42b7bba37d4cac83b01416f0c6c44` / 2026-10-12T18:08:03+07:00 | B/C | MIT | Searchable guidance database, product/stack classification, reusable design records and deliberate optional dials. | Python search/persistence and Node GitHub-release download/ZIP installation inspected. Reject installer execution, global stack assumptions, numeric dial defaults, and bulk context loading. |
| [better-auth/better-icons](https://github.com/better-auth/better-icons/tree/033316ecb8f4982235af4111a2257e80231f5ab1) | `033316ecb8f4982235af4111a2257e80231f5ab1` / 2026-04-02T08:54:17-07:00 | B/C | MIT | Scoped icon search/retrieval can maintain coherent SVG families and smaller result context. | CLI fetches Iconify content and may write downloaded assets; MIT tool license does not license every icon collection. Check SVG trust and individual asset provenance before use. |
| [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill/tree/d237dd399d57524945c0c81327da5da19f7a468d) | `d237dd399d57524945c0c81327da5da19f7a468d` / 2026-10-11T23:56:48+02:00 | C | MIT | Optional variance/motion/density vocabulary and critique of formulaic UI. | Large current skill (~13k words) and v1 fixed 8/6/4 dials; framework/package assumptions and blanket prohibitions conflict with owner policy. Reference only; do not adopt a universal Taste style or automatic npx commands. |
| [jakubkrehel/make-interfaces-feel-better](https://github.com/jakubkrehel/make-interfaces-feel-better/tree/35545ea1512ad59fa463e6b1f95ca9c052981fe6) | `35545ea1512ad59fa463e6b1f95ca9c052981fe6` / 2026-08-29T18:59:35+02:00 | C | MIT | Polish within the existing styling system, optical alignment, state review, interruptible/limited motion. | Selected package is text guidance with referenced resources, no implementation script in tree. Reject fixed timing/geometry/optical offsets as universal laws. |
| [carmahhawwari/ui-design-brain](https://github.com/carmahhawwari/ui-design-brain/tree/38f04c5a1dee55d99c686a16643cef4e2ce0f7a2) | `38f04c5a1dee55d99c686a16643cef4e2ce0f7a2` / 2026-02-27T23:25:15-08:00 | C | MIT | Component-pattern knowledge can reduce invented controls and improve semantics/hierarchy. | Small text catalog assumes modern/minimal SaaS/web style and categorical visual rules. Reference components; reject global SaaS identity and mandatory display/body pairing. |
| [ibelick/ui-skills](https://github.com/ibelick/ui-skills/tree/f2264c30213a8a55bd0a6a7668d0438e4564e090) | `f2264c30213a8a55bd0a6a7668d0438e4564e090` / 2026-10-12T18:28:03+02:00 | B/C | MIT | Focused accessibility and baseline review; improve-ui emphasizes product evidence and rendered proof. | CLI/package/publisher tooling exists; selected baseline mandates motion/react, specific primitives and timing; improve-ui narrows some accessibility findings unless requested. Adapt process, never narrow constitutional obligations or impose React/Tailwind everywhere. |
| [petergyang/no-ai-slop](https://github.com/petergyang/no-ai-slop/tree/000650b156983f5159695b441477f4e63b25dc85) | `000650b156983f5159695b441477f4e63b25dc85` / 2026-09-01T21:19:00-07:00 | C | MIT | Concrete copy, author voice, named evidence rather than claiming AI detection. | Markdown guidance with Python archive builder; no builder executed. Reference writing process beneath product voice; reject universal word bans and automatic rewriting. |
| [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills/tree/063bee94c3f4df8453406c830b0a7df0f2860278) | `063bee94c3f4df8453406c830b0a7df0f2860278` / 2026-08-28T15:36:07+02:00 | A/B | Not established in inspected root; verify before copying | Focused web interface review and short metadata-based discovery. | web-design-guidelines/SKILL.md explicitly fetches mutable remote main/command.md as rules/output instructions. Pin/record fetched content and constrain network; license not established by a root LICENSE in the inspected tree, verify before copying. |
| [vercel-labs/web-interface-guidelines](https://github.com/vercel-labs/web-interface-guidelines/tree/434b7f91364665f2f733b310ec54809bf8f37937) | `434b7f91364665f2f733b310ec54809bf8f37937` / 2026-10-05T13:49:16-07:00 | A/B | MIT | Relevant keyboard/focus, forms, motion, typography, layout, dark mode and web review. | MIT guidance inspected at pinned revision. Framework syntax, punctuation and numeric conventions remain scoped; avoid automatic mutable-main trust. |

## Third-party candidate assessment

All ten candidates below are **reference only** for this pass. None is installed, added as a runtime dependency, or entered into a trusted execution registry. Adapt portable process ideas only after any later project-specific security/licensing review. Selected-file static inspection is not an exhaustive dependency or executable audit.

| Candidate | Runtime/network/write surface and overlap | Context / platform assumptions | Recommendation |
|---|---|---|---|
| pbakaus/impeccable | Launcher can download an executable into a user cache; browser tooling and hooks expand surface. No binary or installer executed. Reject its authority-sounding claims and categorical tint/font/style prescriptions. Overlaps frontend/audit/polish or writing concerns; select one primary workflow. | .agents/skills/impeccable/SKILL.md: 1656 words; host/platform assumptions must remain scoped. | Reference only; retain useful process, reject universal style/authority defaults. |
| nextlevelbuilder/ui-ux-pro-max-skill | Python search/persistence and Node GitHub-release download/ZIP installation inspected. Reject installer execution, global stack assumptions, numeric dial defaults, and bulk context loading. Overlaps frontend/audit/polish or writing concerns; select one primary workflow. | .claude/skills/ui-ux-pro-max/SKILL.md: 2118 words; host/platform assumptions must remain scoped. | Reference only; retain useful process, reject universal style/authority defaults. |
| better-auth/better-icons | CLI fetches Iconify content and may write downloaded assets; MIT tool license does not license every icon collection. Check SVG trust and individual asset provenance before use. Overlaps frontend/audit/polish or writing concerns; select one primary workflow. | skills/SKILL.md: 515 words; host/platform assumptions must remain scoped. | Reference only; retain useful process, reject universal style/authority defaults. |
| Leonxlnx/taste-skill | Large current skill (~13k words) and v1 fixed 8/6/4 dials; framework/package assumptions and blanket prohibitions conflict with owner policy. Reference only; do not adopt a universal Taste style or automatic npx commands. Overlaps frontend/audit/polish or writing concerns; select one primary workflow. | skills/taste-skill/SKILL.md: 13127 words, skills/taste-skill-v1/SKILL.md: 2937 words, skills/redesign-skill/SKILL.md: 2390 words; host/platform assumptions must remain scoped. | Reference only; retain useful process, reject universal style/authority defaults. |
| jakubkrehel/make-interfaces-feel-better | Selected package is text guidance with referenced resources, no implementation script in tree. Reject fixed timing/geometry/optical offsets as universal laws. Overlaps frontend/audit/polish or writing concerns; select one primary workflow. | skills/make-interfaces-feel-better/SKILL.md: 1842 words; host/platform assumptions must remain scoped. | Reference only; retain useful process, reject universal style/authority defaults. |
| carmahhawwari/ui-design-brain | Small text catalog assumes modern/minimal SaaS/web style and categorical visual rules. Reference components; reject global SaaS identity and mandatory display/body pairing. Overlaps frontend/audit/polish or writing concerns; select one primary workflow. | SKILL.md: 1237 words; host/platform assumptions must remain scoped. | Reference only; retain useful process, reject universal style/authority defaults. |
| ibelick/ui-skills | CLI/package/publisher tooling exists; selected baseline mandates motion/react, specific primitives and timing; improve-ui narrows some accessibility findings unless requested. Adapt process, never narrow constitutional obligations or impose React/Tailwind everywhere. Overlaps frontend/audit/polish or writing concerns; select one primary workflow. | skills/baseline-ui/SKILL.md: 508 words, skills/fixing-accessibility/SKILL.md: 734 words, skills/improve-ui/SKILL.md: 1114 words; host/platform assumptions must remain scoped. | Reference only; retain useful process, reject universal style/authority defaults. |
| petergyang/no-ai-slop | Markdown guidance with Python archive builder; no builder executed. Reference writing process beneath product voice; reject universal word bans and automatic rewriting. Overlaps frontend/audit/polish or writing concerns; select one primary workflow. | skills/no-ai-slop/SKILL.md: 1715 words; host/platform assumptions must remain scoped. | Reference only; retain useful process, reject universal style/authority defaults. |
| vercel-labs/agent-skills | web-design-guidelines/SKILL.md explicitly fetches mutable remote main/command.md as rules/output instructions. Pin/record fetched content and constrain network; license not established by a root LICENSE in the inspected tree, verify before copying. Overlaps frontend/audit/polish or writing concerns; select one primary workflow. | skills/web-design-guidelines/SKILL.md: 176 words; host/platform assumptions must remain scoped. | Reference only; retain useful process, reject universal style/authority defaults. |
| vercel-labs/web-interface-guidelines | MIT guidance inspected at pinned revision. Framework syntax, punctuation and numeric conventions remain scoped; avoid automatic mutable-main trust. Overlaps frontend/audit/polish or writing concerns; select one primary workflow. | Pinned command guidance, not SKILL.md; host/platform assumptions must remain scoped. | Reference only; retain useful process, reject universal style/authority defaults. |

## Direct web attempts / research still outstanding

| Required source or locator | Attempted URL | Result / limitation |
|---|---|---|
| OpenAI Skills | https://developers.openai.com/codex/skills/ | <urlopen error Tunnel connection failed: 403 Forbidden> |
| OpenAI API Skills | https://developers.openai.com/api/docs/guides/tools-skills | <urlopen error Tunnel connection failed: 403 Forbidden> |
| OpenAI prompting primary pointer | https://developers.openai.com/api/docs/guides/latest-model/gpt-6-astra.md | <urlopen error Tunnel connection failed: 403 Forbidden> |
| OpenAI named skills article candidate URL, identity unverified | https://developers.openai.com/blog/rethinking-skills-and-prompts-for-gpt-6-astra/ | <urlopen error Tunnel connection failed: 403 Forbidden> |
| OpenAI prompt-injection article candidate URL, identity unverified | https://openai.com/index/designing-ai-agents-to-resist-prompt-injection/ | <urlopen error Tunnel connection failed: 403 Forbidden> |
| Anthropic skill reference | https://code.claude.com/docs/en/skills | <urlopen error Tunnel connection failed: 403 Forbidden> |
| WCAG 2.2 published standard | https://www.w3.org/TR/WCAG22/ | <urlopen error Tunnel connection failed: 403 Forbidden> |
| WAI-ARIA APG | https://www.w3.org/WAI/ARIA/apg/ | <urlopen error Tunnel connection failed: 403 Forbidden> |
| Apple HIG | https://developer.apple.com/design/human-interface-guidelines/ | <urlopen error Tunnel connection failed: 403 Forbidden> |
| Fluent 2 primary site | https://fluent2.microsoft.design/ | <urlopen error Tunnel connection failed: 403 Forbidden> |
| Material 3 primary site | https://m3.material.io/ | <urlopen error Tunnel connection failed: 403 Forbidden> |
| NNG ten heuristics | https://www.nngroup.com/articles/ten-usability-heuristics/ | <urlopen error Tunnel connection failed: 403 Forbidden> |
| NNG progressive disclosure | https://www.nngroup.com/articles/progressive-disclosure/ | <urlopen error Tunnel connection failed: 403 Forbidden> |
| NNG error-message guidance | https://www.nngroup.com/articles/error-message-guidelines/ | <urlopen error Tunnel connection failed: 403 Forbidden> |
| NNG heuristic evaluation | https://www.nngroup.com/articles/how-to-conduct-a-heuristic-evaluation/ | <urlopen error Tunnel connection failed: 403 Forbidden> |
| UX by Example title candidate URL, identity unverified | https://uxbyexample.com/the-60-30-10-rule/ | <urlopen error Tunnel connection failed: 403 Forbidden> |

The candidate URLs for the named OpenAI blog articles and UX by Example title are unverified locators, not established canonical identities. No search capability or accessible primary site resolved them. The owner-supplied Maya Brennan article title/date (September 29, 2026) and de-slopification/community observations were inspected as supplied text; authorship/publication/current page was not independently verified. Adopt deliberation, subtraction, references, workflow-first design, complementary skills, and product value as owner policy; do not cite the supplied observations as an independently retrieved standard.

Outstanding required source coverage: live OpenAI Skills/prompt/security guidance; Anthropic live skill reference; current Apple HIG; Fluent 2 primary-site guidance beyond repository evidence; NNG usability/progressive-disclosure/error/heuristic material; UX by Example 60/30/10 title/canonical source. W3C, APG and Material have pinned official-repository evidence, with published/live pages unverified. These access limits must be resolved or explicitly dispositioned by the owner before claiming the master research gate complete.

## Conflicts and adopted boundary decisions

- Standards/applicable accessibility and security outrank community aesthetic preferences. No universal font/color/card/gradient/sidebar bans, dial numbers, animation milliseconds, or vendor design systems.
- 60/30/10 remains an owner-preferred heuristic, without independent current article verification; semantic colors and accessibility take priority.
- First-party hooks can install dependencies and disclose source material. First-party provenance does not supply execution or disclosure authority.
- Vercel mutable-main retrieval is a concrete reproducibility/supply-chain case: pin or identify and validate exact content before trusted adoption; project/owner contracts remain higher authority.
- Complementary layering requires one primary workflow per concern, conflict precedence and a context budget. Skill count is not maturity.
- Native/shared/web implementations remain product-appropriate; WCAG/APG web mechanisms and framework-specific packages are not universal requirements.

## Exact inspected-file inventory

Each entry records retrieved bytes, not runtime verification. Large scripts were inspected through targeted static excerpts; no claim of exhaustive whole-program security certification is made. File selection focused on instructions, license declarations, installers/network/write surfaces, and relevant standards.

| Repository | Path at pinned revision | Bytes / SHA-256 |
|---|---|---|
| anthropics/claude-code | `plugins/frontend-design/skills/frontend-design/SKILL.md` | 9390 / `d91970639e9f5c37682ac7ab60094d35f1c7c1f38d731bd56396563aee10c1d3` |
| anthropics/claude-code | `plugins/feature-dev/commands/feature-dev.md` | 5097 / `652e5d6264fd253fcb70c2f84de986a88d77109a02410aacd90230a6ab4bf557` |
| anthropics/claude-code | `plugins/code-review/commands/code-review.md` | 7297 / `2b0837c5ec0b2e75f8ba4565bdafd76fa916b0dc146608c5733af7ba5802012c` |
| anthropics/claude-code | `plugins/security-guidance/README.md` | 7219 / `8e9f9ed1f43a2b877de1040a0a5181a80deed95417a919eee55efc58bd5f48eb` |
| anthropics/claude-code | `plugins/security-guidance/hooks/hooks.json` | 2783 / `37181aea2a1ccd4efa88c427d4cd194fac48ab1ca67779c14edf8de375809181` |
| anthropics/claude-code | `plugins/security-guidance/hooks/llm.py` | 112010 / `bf2f1e71ac04eea6364b545b69aa876168b928fc767146ba5d86988cfb213b34` |
| anthropics/claude-code | `plugins/security-guidance/hooks/review_api.py` | 24763 / `b5e5ee59787e174998adb70a53e0b06252449c6e96f2d52e735f8ad5cbe4e319` |
| anthropics/claude-code | `plugins/security-guidance/hooks/ensure_agent_sdk.py` | 9856 / `e682d82026521106ec00267078fb4e2190b3a0a501362fc9f4a0753f2d7a1b56` |
| anthropics/claude-code | `plugins/pr-review-toolkit/README.md` | 7528 / `364cb1d46aa64a01016e4ef5f41dfea5bd5e3cf530459409a376feba93dd2b49` |
| anthropics/claude-code | `LICENSE.md` | 150 / `728158fd1037143fad6907e8fa34804177e598b7326519503fe83cafdef849e6` |
| anthropics/claude-code | `README.md` | 2873 / `aa0d8b80ac083e1591be0789273f447058cc9187b4331634a5614155da27778d` |
| anthropics/claude-plugins-official | `plugins/frontend-design/skills/frontend-design/SKILL.md` | 9390 / `d91970639e9f5c37682ac7ab60094d35f1c7c1f38d731bd56396563aee10c1d3` |
| anthropics/claude-plugins-official | `plugins/frontend-design/skills/frontend-design/LICENSE.txt` | 10174 / `0d542e0c8804e39aa7f37eb00da5a762149dc682d7829451287e11b938e94594` |
| anthropics/claude-plugins-official | `plugins/feature-dev/commands/feature-dev.md` | 5097 / `652e5d6264fd253fcb70c2f84de986a88d77109a02410aacd90230a6ab4bf557` |
| anthropics/claude-plugins-official | `plugins/code-review/commands/code-review.md` | 7422 / `7d5a0bc9a41babad32a387152f9680316997bc4ad376928827d670b1760cc890` |
| anthropics/claude-plugins-official | `plugins/security-guidance/README.md` | 7858 / `0ef73ff5a40f37a09baabd3a7bc22781cc512c2f3ae84d2494c6e5133cce2194` |
| anthropics/claude-plugins-official | `plugins/security-guidance/hooks/hooks.json` | 5483 / `7fcc90a45db5ad74146865e850566776fa72852b47888f4d9ec708196abb4dc5` |
| anthropics/claude-plugins-official | `plugins/security-guidance/hooks/llm.py` | 123647 / `6d93937f8e2cae0b6acf062004d77986289a0db4a832acbf19e0eeab82815352` |
| anthropics/claude-plugins-official | `plugins/security-guidance/hooks/review_api.py` | 24763 / `b5e5ee59787e174998adb70a53e0b06252449c6e96f2d52e735f8ad5cbe4e319` |
| anthropics/claude-plugins-official | `plugins/security-guidance/hooks/ensure_agent_sdk.py` | 41917 / `ca293fb53fe6d5f9745392b27f527cee0e9d12ba607ce67f50d82def19a52b6b` |
| anthropics/claude-plugins-official | `plugins/pr-review-toolkit/README.md` | 7528 / `364cb1d46aa64a01016e4ef5f41dfea5bd5e3cf530459409a376feba93dd2b49` |
| anthropics/claude-plugins-official | `LICENSE` | 11358 / `cfc7749b96f63bd31c3c42b5c471bf756814053e847c10f3eb003417bc523d30` |
| anthropics/claude-plugins-official | `README.md` | 3859 / `f34b8730d2b61617045c61ea2d9bf3ab08561305bfac77ea061e755bf46aeac2` |
| openai/codex | `docs/skills.md` | 115 / `e59789d09692310bbf94e2ef8db0aaf00d97f2226982c8c5330d2d260583a97d` |
| openai/codex | `SECURITY.md` | 923 / `a71f3645c5438400bf803a210cae829a07b5319ac1babe289badad7d1091af3a` |
| openai/codex | `codex-rs/skills/src/assets/samples/openai-docs/references/prompting-guide.md` | 10128 / `5c791edd5bfc9363cb4251ac3ccd3b1dbac3bb2a6654f78606a9d2357c97c172` |
| openai/codex | `codex-rs/skills/src/assets/samples/openai-docs/references/upgrading-to-gpt-6-astra.md` | 19676 / `cacacdfe0b516f7420af51df10dfa0829bf67c4a670544d58992f6ce4ac22583` |
| openai/codex | `LICENSE` | 10926 / `d17f227e4df5da1600391338865ce0f3055211760a36688f816941d58232d8dc` |
| openai/codex | `README.md` | 3334 / `ba4e1f69ff48386e72a9c5e1edaf76aad64a475c2d51af79ccba6d1128261ba7` |
| openai/openai-cookbook | `examples/skills_in_api.ipynb` | 29585 / `b5162ce54fe14d576f4d6a55f5fcd3b7cb6d2337a160f7b91dcdd0e6284113d5` |
| openai/openai-cookbook | `.codex/skills/docs-editor/SKILL.md` | 4290 / `a10903669374933624fcfb16cb1580dc5282c7c5ba2b7e113b422a1316030c32` |
| openai/openai-cookbook | `LICENSE` | 1063 / `13df7812ca53ecaae1cb4a868844bb598373047ae1d580e4debfbef1dd5b6915` |
| openai/openai-cookbook | `README.md` | 1211 / `ed596b962642ea131470fef9aa699606881f218621bae563f4b12c418ef33476` |
| w3c/wcag | `guidelines/sc/20/keyboard.html` | 872 / `8724a66650968536ac46ec2cb486c4cedeade25531d2840f75aedf6826e7aed1` |
| w3c/wcag | `guidelines/sc/20/use-of-color.html` | 545 / `81b0f49c1c18ed014de5eb93836c1f6d5b218b55663fcb2a43b78b78efada9b9` |
| w3c/wcag | `guidelines/sc/20/contrast-minimum.html` | 1071 / `f1d819b44cc5ba64e962ce64889de2ab214af6911b27a119f7d24c43197b2e64` |
| w3c/wcag | `guidelines/sc/22/focus-appearance.html` | 1591 / `24cc3b410b57253765513d7ce12b1d9bb8f311fae88028a5301e90fe3161e763` |
| w3c/wcag | `guidelines/sc/22/target-size-minimum.html` | 1737 / `b5cd439141c3771e69cd20596f6fbda5fadfe28967f8783559066a435a62b123` |
| w3c/wcag | `guidelines/sc/22/dragging-movements.html` | 656 / `e70cd9ec2cdd31203174a8f241b907bd6884a841cb5e1ad4705ec940997a57dc` |
| w3c/wcag | `guidelines/sc/21/animation-from-interactions.html` | 352 / `ebf2dad0e24deb24b7963b7309ab7872d93a4b22859524edfd74021a41c66b10` |
| w3c/wcag | `LICENSE.md` | 155 / `7a3ad7d36b8855bc301276279769da4aff648ea5d7b92f3f023c0823ee948764` |
| w3c/wcag | `README.md` | 21432 / `fa2a43e2fa8e43fade0313289807eb11882d59c7c82e5cd76e8eaa8f640397ae` |
| w3c/aria-practices | `content/practices/names-and-descriptions/names-and-descriptions-practice.html` | 109512 / `c3ac8f452b8f48cab51fb827b7b96ec76546ad5f25943ae2336d540b52b70b69` |
| w3c/aria-practices | `content/practices/keyboard-interface/keyboard-interface-practice.html` | 49393 / `8c922b69503be478307c1a2d5598f70badc76dccb14c0f787154f6dba1bf8e86` |
| w3c/aria-practices | `content/patterns/button/button-pattern.html` | 7588 / `d4cf3c946ccef12dabc131bb119653bb93cc73bbbae5525d9bc541d36e233207` |
| w3c/aria-practices | `LICENSE.md` | 165 / `7519b8221b1bf98b4105477c2fec93323e97a1c9699b3856ec65f492e9076727` |
| w3c/aria-practices | `README.md` | 5991 / `60e9518c4dba41cdf4ea211b70ef707fdcd6423780f8732a923bf6383fb81efb` |
| microsoft/fluentui | `docs/architecture/design-tokens.md` | 2342 / `43b569405e69d1478252233298d5111e431e27fcb19e5b193af85c06fbf2bd06` |
| microsoft/fluentui | `docs/react-v9/contributing/accessibility-review-checklist.md` | 22264 / `eb4b42d4d9fc8bc7b0bc95caa9e5fbb0786163c83fac132d0dca2bf9fde366e1` |
| microsoft/fluentui | `apps/public-docsite/src/pages/Styles/MotionPage/docs/web/MotionOverview.md` | 516 / `b0691ad3c93d2785b9a5a0a055e7da6c81c8d4001fa3c419fc5bf692b1d2f249` |
| microsoft/fluentui | `LICENSE` | 1212 / `1434c6b2a8417d41e4db20ff3b772888e66a0069e20d928f83fa1390f44758c7` |
| microsoft/fluentui | `README.md` | 10623 / `763a28150cd2873c0ea776d71d92ccef2967f0ddac2d7f8ec36d4d9e15c4b10a` |
| material-components/material-web | `docs/theming/color.md` | 3540 / `f24aaeb7a63af5b226cde99779d07f293ab5740db2d64f805547983295e4e6c2` |
| material-components/material-web | `docs/theming/typography.md` | 5734 / `a04998310ce654ab51daf884f08ec24a25250c2dab316380abeb65eb18577710` |
| material-components/material-web | `docs/theming/shape.md` | 1527 / `406302e4164c10f7fbc54a8af3d66ea93345e30920f71444884e0bfb95138d05` |
| material-components/material-web | `LICENSE` | 11348 / `295cdb4364b782931c914f5ca8c47fac87c732fa7e448b788a47aa5b25728212` |
| material-components/material-web | `README.md` | 3146 / `2e09574705d14f6447603c1795014d9a3f0043a06577e3830a4a591d62a36a85` |
| pbakaus/impeccable | `.agents/skills/impeccable/SKILL.md` | 12263 / `58c0252bca04521de87007aeb495f7ec99dc4c7341bc890fe82b6d577573af91` |
| pbakaus/impeccable | `.agents/skills/impeccable/scripts/impeccable` | 8514 / `39d9600489073e227e4f4d55c451ce4252a6632ed7ae37923efbbcbc91f16d07` |
| pbakaus/impeccable | `.agents/skills/impeccable/scripts/live-browser.js` | 548448 / `d7f1ee3fdfc423e90268e9c666dce61b2180b62431dbb6ecfc48bca65398a1f8` |
| pbakaus/impeccable | `package.json` | 3877 / `cc4e283b6a62786d7989305c1d649189abfee36f6500a56466d0e8205525c074` |
| pbakaus/impeccable | `LICENSE` | 10766 / `02bb8c3b4e70190e3986c0404ad2fd8d639b4f534252d82379cc1b502b6d1812` |
| pbakaus/impeccable | `README.md` | 29582 / `256b85659e13ffd7f5aba978f83bc91677d7439967283744d71cb0b082bb81a3` |
| pbakaus/impeccable | `README.npm.md` | 3941 / `f7b63241e9018af70fc9d2f366412b155788d2d698a29c5c4884a9a823b5521a` |
| nextlevelbuilder/ui-ux-pro-max-skill | `.claude/skills/ui-ux-pro-max/SKILL.md` | 15969 / `ea087c341bfb5b23195c7302027268ede86da802554c18a5c4896a6017b439f9` |
| nextlevelbuilder/ui-ux-pro-max-skill | `cli/package.json` | 2433 / `1b816c9238043df596f6b8c31fa9669a4c551ae1cb9b9df2092b19904d9f38e5` |
| nextlevelbuilder/ui-ux-pro-max-skill | `cli/src/commands/init.ts` | 7781 / `49f2f095e9e3a5bc870b6ca8188d3ed33c86a52bab6a1f5c7a6c06a265e29aac` |
| nextlevelbuilder/ui-ux-pro-max-skill | `cli/src/utils/github.ts` | 4000 / `78ed9417edf0c912b60e421cc0bfc776df917d3d97c8eeabbac085ecfa87dc41` |
| nextlevelbuilder/ui-ux-pro-max-skill | `cli/src/utils/extract.ts` | 4144 / `b4f8fc7a166dabdb4c9563e350c56ac8dffd60b00b083733b9265c5867affa67` |
| nextlevelbuilder/ui-ux-pro-max-skill | `src/ui-ux-pro-max/scripts/search.py` | 9373 / `d54e648fe0ec2932cac66684220cc17be4bd4b4eba1d23d3195d509d398db374` |
| nextlevelbuilder/ui-ux-pro-max-skill | `LICENSE` | 1075 / `738f69dfa83db5c347c678fb9d90e560877059f0de93a327c39001bff92dc014` |
| nextlevelbuilder/ui-ux-pro-max-skill | `README.id.md` | 35313 / `9652c578ed92a607c95eaf8297ac17a9a9d1d2e58c1bc92baed9f810fd7c2848` |
| nextlevelbuilder/ui-ux-pro-max-skill | `README.ko.md` | 33248 / `58ef85ce00943d0f4ad0e5ed94cecb59340440b487e26ad466decc9fbb00edbd` |
| nextlevelbuilder/ui-ux-pro-max-skill | `README.md` | 37924 / `bb8f3ec05c8654d568485c1e1ad0e938241828f7702d109c0b1ae6dd24cdd6d3` |
| nextlevelbuilder/ui-ux-pro-max-skill | `README.vi.md` | 40937 / `cefd29bfeb350f61110f293302096ffcf7709748d87b88465c732ae81ae1adcf` |
| nextlevelbuilder/ui-ux-pro-max-skill | `README.zh.md` | 34114 / `47da3425b824800ea23b00a7c5fbbba3b929bbfe52972d657bbff9b0f086eb25` |
| better-auth/better-icons | `skills/SKILL.md` | 3584 / `3d12532000bae46a54ac5ea47a8cc5ce24cb7008b366abe6ccf4f7e86c489110` |
| better-auth/better-icons | `package.json` | 1133 / `61fe2e014ba8c8a9d8d911ba6dde674470a0cc45ffac101a214cfaacbce16703` |
| better-auth/better-icons | `src/index.ts` | 1956 / `03c89156ba8165f1209238dd32bc31075a2f53b55dab3549052dbf7127a26e5b` |
| better-auth/better-icons | `LICENSE` | 1074 / `f1a436b9a396ebf3b09735931e0027c9f1f28aa282fc3c701dc22da5a15d1e2c` |
| better-auth/better-icons | `README.md` | 8510 / `dcd17a52ded5773b4d9fac34add9e72be8204a936b6ee5642d030645208d7621` |
| Leonxlnx/taste-skill | `skills/taste-skill/SKILL.md` | 89478 / `2136ed83016bfada39f7b8013b2aafd9f78fcbd9799110ed222a79c6419ba5fb` |
| Leonxlnx/taste-skill | `skills/taste-skill-v1/SKILL.md` | 21195 / `033d45af1ed23832730642f95f40ab49db7fb5222848489a6c5656144bfc6dae` |
| Leonxlnx/taste-skill | `skills/redesign-skill/SKILL.md` | 16267 / `a75d547d04595fe97a5d377dddf145d029d51487a4f2a0a5a9d3b532ca3b84cd` |
| Leonxlnx/taste-skill | `LICENSE` | 1065 / `4575a543ab88dad12ccea7d97e563d0bce5b448b06072e65d3264497dad326df` |
| Leonxlnx/taste-skill | `README.md` | 18905 / `f3a3903a31e1386fd7ac581e3e0f85356d0159d1baf40d517c6f12c37fbff387` |
| jakubkrehel/make-interfaces-feel-better | `skills/make-interfaces-feel-better/SKILL.md` | 11818 / `c1d508fa7bef8e47ee682b4f214c7a4ed1416b91d05a97285e555bad1c41a23e` |
| jakubkrehel/make-interfaces-feel-better | `LICENSE` | 1069 / `ed1dfe988fc40511b4845ccd9050a143a2002fee3bedc8064c47fa342b5d8d4f` |
| jakubkrehel/make-interfaces-feel-better | `README.md` | 661 / `d1357d0aa07aa105bab5775c23124c197ab0b921891cf6876a05e5afb24255bd` |
| carmahhawwari/ui-design-brain | `SKILL.md` | 8302 / `89e6ee68cef797d2b5c822043c478972db0dfda1ccef534f87c1687f4c3f6ec0` |
| carmahhawwari/ui-design-brain | `LICENSE.txt` | 1227 / `c1b676bc87c2dfd9182264830f47168db1afc15d0ad61993eec1e4958bbdd8bd` |
| carmahhawwari/ui-design-brain | `README.md` | 4803 / `a313a4467545f93e39b38cfc62a51033453006f4fe4a0d73753c551f17649bfc` |
| ibelick/ui-skills | `skills/baseline-ui/SKILL.md` | 3419 / `fea3322f36d58fdafafce2aef56e4556dd2ac7b20876b7dff7d8be7f25fa597f` |
| ibelick/ui-skills | `skills/fixing-accessibility/SKILL.md` | 4718 / `549261e8a53b53a1a20c0ddbf736821e5fc0876ad82eee76e0efab8e9ee9dadf` |
| ibelick/ui-skills | `skills/improve-ui/SKILL.md` | 7830 / `fa2ac808f6d9dab7bb3620880b014d2c18e227e5b006102856038096e573e69a` |
| ibelick/ui-skills | `package.json` | 2018 / `0dfae33637aa283cf9a6a6f0f50a8250ed2a5933501d2ef2794d32119bf8a40b` |
| ibelick/ui-skills | `scripts/check-agent-skills-digests.mjs` | 1231 / `1fe96cc65eae1c6d7708042ee8799dd9a51742daa9db4aae50e5e00c25714afb` |
| ibelick/ui-skills | `LICENSE` | 1072 / `c615621c4cc1676ccde194e7a01b6469ba477780251bd71e007fc473a49c2c2b` |
| ibelick/ui-skills | `README.md` | 691 / `4dc3e9f0216a750d980f55db8412f5c8d656066bc9aadd26deeb8fd4798f991d` |
| petergyang/no-ai-slop | `skills/no-ai-slop/SKILL.md` | 10853 / `992b365f51a2f62cf4c1c5ed22049a9ee551dfea677550c1a72b371c0ceadd62` |
| petergyang/no-ai-slop | `scripts/build_plugin.py` | 4581 / `ac836f53d02a232945327b64d39d33d9b8205ab8846666670eb3cef3422b89e6` |
| petergyang/no-ai-slop | `LICENSE` | 1067 / `b7a7fe370cc4c9e974528c7cea7841cf8ac886bc9ed947edb11b289441fba4a8` |
| petergyang/no-ai-slop | `README.md` | 3248 / `a2e24837d6531c2e827876123d05ea482a21bcfc25358dbdacbf581fb1e51d81` |
| vercel-labs/agent-skills | `skills/web-design-guidelines/SKILL.md` | 1231 / `f4647ca866a3accf763777f83e7682954f0187cd6bea7eea0399796652414e8f` |
| vercel-labs/agent-skills | `package.json` | 126 / `4346dba39e76172e83a7f836077b2832a950cec9aeb1caf47d2713151a4391b9` |
| vercel-labs/agent-skills | `README.md` | 7838 / `7c02f64b08fc6c4eef03c01d64f3e2ed478193ccfcbd14edba379abe23304651` |
| vercel-labs/web-interface-guidelines | `command.md` | 8055 / `d246b026f4f29b5823a9cc857f9edf3d2507002e055e32040cadeaf3b38e0234` |
| vercel-labs/web-interface-guidelines | `LICENSE` | 1068 / `6cd1609c9c12233507cdd2ce0d32e9a721e3c27494951be06b90090deeeb7af2` |
| vercel-labs/web-interface-guidelines | `README.md` | 19239 / `eda7dfa9998215267c7f920475d1773ea4129cb08ed088276ca598dd45d20aa5` |

This record can be resumed without hidden chat: retrieve the blocked primary resources, verify canonical titles/URLs, record dates/source identity, compare principles with the pinned matrix, and disposition any changes before updating the Green verdict. Do not repeat completed static repository reads unless source changes or a concrete unresolved question requires it.
