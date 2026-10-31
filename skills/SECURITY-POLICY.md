# Security policy for imported skills

## Scope and quarantine

Every package under `_intake/` is untrusted source material. It is not loaded by an agent, cannot trigger automatically, and receives no filesystem, shell, network, credential, or MCP permission from this library. Never execute an imported script, installer, hook, server, or binary during review.

## Provenance and integrity

Each candidate is pinned to an upstream commit and exact source subdirectory. SHA-256 hashes cover each imported source file and content tree. License evidence is copied and hashed when redistribution is allowed. A package without verified redistribution permission is registry-only. Do not remove or alter an upstream security finding to obtain a cleaner scan. Record all packaging repairs with original and revised hashes.

## Required scanner

The required baseline is NVIDIA SkillSpector static analysis, run individually for each unique imported package folder using the pinned CLI and `--no-llm --format json`. Capture stdout, stderr, exit code, scanner version, source commit, package identity, and time. Inspect JSON recommendation, issue severity, and coverage/completeness fields; exit code zero alone is never a pass. Re-scan after any package repair.

Semantic LLM review is optional only when a reviewed backend is available and source handling is authorized. No package text, user secrets, or protected information may be sent to an external provider without authorization. Unavailable semantic coverage must be disclosed.

## Statuses

- `PASS`: verified provenance and package integrity; complete required static review; no blocking finding; permitted capabilities and declared dependencies reviewed.
- `CAUTION`: nonblocking finding or unresolved activation concern; human review required before any future adoption.
- `FAIL`: confirmed unacceptable behavior or critical security defect.
- `QUARANTINED`: dangerous or suspicious package isolated from use.
- `INCOMPLETE`: missing required resources, incomplete scanner coverage, unresolved integrity/licensing, or unavailable required evidence.
- `NOT_APPLICABLE`: repository mention is not an importable agent skill.

A scanner `SAFE` recommendation supports, but does not establish, `PASS`. `CAUTION` never maps to `PASS`. `DO_NOT_INSTALL` is never enabled. High-risk evidence remains quarantined.

## Approval gate

No skill is activated by this intake. Future adoption requires review of individual source, license, package hashes, scanner JSON, dependency findings, capability fit, and outstanding flags. The owner must separately authorize any activation, rule integration, permissions, or source-repository cleanup.
