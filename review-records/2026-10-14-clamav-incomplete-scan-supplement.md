# Targeted RED supplement — ClamAV incomplete/limit-skipped scans

## Scope and status

This is a read-only, narrowly scoped adjudication supplement for IO-2/IO-3 at the exact candidate commit `a9c597c8f14536a4404a64494cf56e9015e1288a`, whose normative document SHA-256 is `1c6471ab3ec5291b9cd4ec884912ccec10431d2e35e9e514ad29574b778b082d). It is not a full Red round and does not count toward convergence.

Review instance: `/root/clamav_incomplete_scan_adjudication`. The coordinator configured GPT-6 Luna with maximum reasoning effort. The reviewer did not provide an independently inspectable deployed model identifier. No files were edited; no implementation was tested; no commit or push was made.

**Disposition: NOT AN ISSUE** (high confidence on normative fit; medium-high confidence on source-limited operational details). No normative repair is proposed.

## Primary-source evidence

Retrieved on 2026-10-14 UTC: official upstream ClamAV source pinned to commit `72cd48c9faed4fa4afc22bc4ed0b9b19f8d3f8f7`, [clamscan/clamscan.c](https://github.com/Cisco-Talos/clamav/blob/72cd48c9faed4fa4afc22bc4ed0b9b19f8d3f8f7/clamscan/clamscan.c). The matching raw source had SHA-256 `96744d214198d7c67598df661bf1036b6d9578e7febbaee0d43e89b70d22cada). At source lines 349–350, help says `--max-scantime`: scan time beyond the threshold “will be skipped and assumed clean”; `--max-filesize`: larger files “will be skipped and assumed clean.” This confirms the premise.

The cited help text does not establish a particular CLI exit code/output format or a specific adapter’s behavior. The reviewer did not run ClamAV or test an implementation.

## Candidate wording and adjudication

IO-3 at candidate line 915 says: “Failure to scan MUST NOT equal clean” and defines CLEAN as “no threat detected under the recorded scanner/engine/signature/policy state”; it lists `SCAN_FAILED` and `UNSUPPORTED` among flexible, equivalent states. An object or portion skipped for a configured size/time cap has not been scanned (or fully scanned), even if ClamAV’s own policy calls the result “assumed clean.” Passing that engine-level assumption through as application CLEAN is therefore contrary to IO-3. It can be represented as SCAN_FAILED, UNSUPPORTED, or another explicit non-clean/incomplete status; no exact status label is required.

IO-2 line 900 says the required configured intake policy must succeed and pending, failed, stale, or unavailable verification cannot silently satisfy its gate. Thus required promotion remains blocked for an object whose required scan is incomplete. IO-3 line 923 requires truthful status for blocked/unverified content.

Cross-rules are consistent: IO-1 line 881 covers attachments, archives, media, plugin packages, and other external files as untrusted and permits size/resource limits as controls; IO-2/IO-3 govern scan and promotion outcomes. SEC-6 line 1013 requires a generic capability adapter to preserve core outcomes/promotion, and line 1017 routes scan failure to IO-3. SEC-1 governs risk-based parser isolation. SKILL-3 independently keeps unreviewed Agent Skills untrusted and requires review of instructions/scripts/dependencies/permissions; a ClamAV CLEAN result cannot stand in for that workflow. SYNC-1 says peer data must pass applicable controls; IO-3 line 925 disallows universal trust from remote CLEAN. OFFLINE-3 and IO-3 line 917 preserve unrelated local capabilities during scanner outage while keeping gates for affected content enforced. No cross-rule escape was established.

## Concrete scenario, competing interpretation, and risk

Adversarial case: a file-intake plan requires scanning before promotion; its ClamAV adapter sets `--max-filesize` or `--max-scantime`, accepts ClamAV’s “assumed clean” result for a skipped/partial object, records the policy version and a CLEAN verdict, and lets the configured gate pass. The official source exposes this possible implementation trap.

The strongest contrary interpretation is that a deliberately capped successful CLI operation is a successful scan under the recorded policy, and that “failure to scan” means only a crash, unavailable scanner, or explicit error. The reviewer rejected it: the actual object/portion was skipped, which is failure to scan that object/portion; CLEAN is not merely “the command returned without an error.” A policy may decide that malware verification is not required for a particular low-risk input (IO-1/IO-2 say not every input needs every step), but then it cannot pass that as a CLEAN scan verdict or claim a required scan gate succeeded.

An explicit clause naming limit-skipped scans would be redundant. A broader rule that every configured cap blocks intake could conflict with IO-1’s risk-based resource controls and could overblock benign/unsupported inputs or unrelated offline work. Existing scope blocks only promotion whose required malware gate is unverified, not the whole application. No implementation test or empirical adapter behavior was established.
