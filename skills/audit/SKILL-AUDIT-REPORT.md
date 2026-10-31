# Skill security audit report

Generated 2026-10-31T23:16:32.920769Z. The audit used the pinned Instagram-Dump snapshot and scanned imported packages while they remained under the inactive intake tree.

## Scope and provenance

- Instagram-Dump `8397dacc7d927552ff8f48891c4fa2d103bed90d`: all **187 tracked files** accounted for, **1130 unique URLs**, and **501 repository records**. The source checkout remained clean and unchanged.
- **2634 resolved package identities** have pinned upstream `SKILL.md` entrypoints and source hashes. **22 ambiguous skill leads** remain unresolved and are listed in `source-mapping.json`.
- The crosswalk records 229 repositories with skill candidates, 264 non-skill/tool/framework or embedded records, 7 unresolved upstream repositories, and 1 catalog-pointer record. It separately tracks 333 Podo pointers, 6 unresolved.
- Redistribution permission was verified for **2364 identities**. **270** remain registry-only because permission was not verified. The eligible identities map to **2305 physical folders**, with 59 exact-content alias identities.
- Rehash verification matched **18,930 imported files**, **2,305 package tree hashes**, and **189 license copies**, with zero mismatches.

## Scanner and coverage

- NVIDIA SkillSpector **v2.13.1**, pinned at `f3b25697d76256998ca9d42c198d256258d4c035`, was installed in an isolated Python 3.12 virtual environment outside this library. The release commit signature was verified through GitHub. Lockfile SHA-256: `65682A369310657AA3FDE7E3C647E31D3D901E45BC34C80FF8AEEFEB260DAB33`.
- Each unique folder received `skillspector scan <individual-skill-folder> --no-llm --format json`. **2305 final JSON reports** were saved and hash-verified. Exit codes: `0` 2040, `1` 265. Coverage: `complete` 752, `partial` 1553. Recommendations: `CAUTION` 1345, `DO_NOT_INSTALL` 265, `SAFE` 695.
- One long-path package was retried using a Windows extended-length path. Its retry emitted valid JSON but remains partial with `DO_NOT_INSTALL` because SkillSpector hit its output limit; both attempts are preserved.
- Official scanner fixtures behaved as expected: safe fixture `SAFE`, exit 0, complete; malicious fixture `DO_NOT_INSTALL`, exit 1, CRITICAL, complete. See `scan-reports/_scanner-selftests/`.
- Semantic model analysis was not run; no approved backend was selected, and no skill contents were sent to an external model. The static SC4 analyzer used OSV.dev lookups where package coordinates were detectable; only dependency coordinates were sent.

## Assessment

Counts below are by **unique physical folder**, taking the most restrictive status when identical content shares a folder.

| Status | Folders |
|---|---:|
| `CAUTION` | 134 |
| `INCOMPLETE` | 1373 |
| `PASS` | 532 |
| `QUARANTINED` | 266 |

Candidate identity counts, including registry-only and deduplicated identities:

| Status | Candidate identities |
|---|---:|
| `CAUTION` | 138 |
| `INCOMPLETE` | 1679 |
| `PASS` | 538 |
| `QUARANTINED` | 279 |

`PASS` requires complete static analysis, a SAFE recommendation, no scanner findings, verified source/tree hashes, verified redistribution permission, and no unresolved packaging finding. A CAUTION recommendation or any finding never becomes PASS. Incomplete coverage and unresolved packaging/rights remain INCOMPLETE. No confirmed behavior was classified FAIL; scanner `DO_NOT_INSTALL` results and pinned vulnerable dependencies were quarantined.

## Significant security findings

- SkillSpector recommended `DO_NOT_INSTALL` for **265 folders**. All remain quarantined. That recommendation is a block, not proof every package is malicious; reports include incomplete-reference, executable-coverage, obfuscation, and other static-pattern findings.
- SC4 recorded **20 occurrences of version-pinned vulnerable dependencies across 8 physical folders**. All are quarantined, including the one folder whose top-level recommendation was CAUTION. Dependency paths and advisory IDs are in `dependency-findings.json` and the linked raw reports.

| Skill package | Pinned dependency versions flagged | Disposition |
|---|---|---|
| `fal-ai-community/skills:skills/fal-redesign` | `basic-ftp==5.3.0`, `extract-zip==2.0.1`, `ip-address==10.1.0`, `js-yaml==4.1.1`, `sharp==0.34.5`, `ws==8.20.0`, `zod==3.25.76` | `QUARANTINED` |
| `google/skills:skills/cloud/agent-platform-tuning` | `datasets==2.18.0` | `QUARANTINED` |
| `google/skills:skills/cloud/cloud-trace-querying` | `urllib3==2.2.1` | `QUARANTINED` |
| `latent-spaces/brag:skills/brag` | `msgpack==1.2.1` | `QUARANTINED` |
| `muthuishere/hand-drawn-diagrams:.` | `pygments==2.19.2`, `pytest==9.0.2` | `QUARANTINED` |
| `ryktara/design-engineering-skill:design-engineering` | `next-intl==4.0.2`, `next==15.3.0` | `QUARANTINED` |
| `trailofbits/skills:plugins/culture-index/skills/interpreting-culture-index` | `pillow==12.3.0` | `QUARANTINED` |
| `tw93/kami:skills/kami` | `brace-expansion==5.0.9`, `glob==13.0.6`, `minimatch==10.2.6` | `QUARANTINED` |

- An additional **26 SC4 occurrences across 13 folders** match dependencies with advisories but no exact version; affected-version status is unknown. Those candidates remain CAUTION, INCOMPLETE, or QUARANTINED according to their scan and package state.
- No package dependency or executable file was edited. An upgrade was not applied without verifying a compatible patched version and preserving upstream behavior. See `dependency-findings.json` for all SC4 observations.

## Packaging and coverage limits

- The manifest retains **1552 packaging-finding occurrences** across candidate records (overlapping findings): `link_escapes_package` 5, `link_targets_directory_without_file` 46, `linked_file_outside_package_root` 740, `missing_internal_link_target` 488, `missing_or_invalid_frontmatter` 3, `redistribution_permission_not_verified` 270.
- Some cross-scope references resolve to sibling packages in the intake; others point outside the copied skill subdirectory. The path heuristic also records code tokens and examples as missing path-like targets. The three packages with absent/invalid SKILL.md frontmatter remain unchanged; metadata was not invented. No source instruction or link was rewritten without a verified behavior-preserving correction.
- **1553 scans are partial**, commonly due to scanner runtime/parser/output limits, excluded executable content, and unresolved path-like references. A partial result is never counted as PASS.
- No imported script, installer, hook, MCP server, or binary was executed. Semantic intent review remains a disclosed gap.

## Inactive state and readiness

Packages remain under `skills/_intake/`. The documented Codex, Claude Code, and Gemini CLI automatic discovery directories are absent in this checkout; no global registration, symlink, permission grant, or execution-rule change was made. No skill was activated, integrated into Universal-Rules, or removed from Instagram-Dump.

**This audit is not ready for the separate skills integration or activation stage.** Review incomplete, caution, quarantined, and rights-unverified entries first. That later stage remains deferred.

## Evidence

- Per-candidate source, status, scan, and report pointer: `skill-results.json`
- All supply-chain analyzer results and advisories: `dependency-findings.json`
- Source-file and repository crosswalk: `../SOURCE-MAPPING.md` and `source-mapping.json`
- Raw individual JSON reports and exit ledgers: `scan-reports/`
- Scanner install and self-test: `scanner-installation.json` and `scan-reports/_scanner-selftests/`
- Branch preservation and merge evidence: `BRANCH-CONSOLIDATION.md`
