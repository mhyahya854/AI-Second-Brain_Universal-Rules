# Inactive skills intake library

This directory is a quarantined intake and review area. Imported instructions are untrusted data. No skill in this library has been activated, integrated into the Universal Rules execution path, or granted tool permissions.

## Layout

- `_intake/github/` holds pinned upstream skill packages whose redistribution is permitted by verified license evidence.
- `_provenance/licenses/` holds applicable upstream license/notice files, with hashes recorded in `manifest.json`.
- `manifest.json` is the machine-readable catalog of every candidate, pinned source, license status, package file hash, deduplication mapping, activation hint, and packaging finding.
- `SOURCE-MAPPING.md` and `audit/source-mapping.json` map the complete Instagram-Dump source snapshot to candidates, imports, or documented exclusions.
- `audit/` contains scanner evidence, audit results, and migration/branch records.

## Inactive by design

This repository path is `skills/_intake`, not the documented repository discovery locations `.agents/skills` (Codex/Gemini Agent Skills convention), `.claude/skills` (Claude Code), or `.gemini/skills` (Gemini CLI). Those paths are absent in this checkout. The host skill catalog also does not list this intake. No symlink, plugin registration, global settings change, or activation configuration was added. See the [Codex skills overview](https://developers.openai.com/blog/skills-agents-sdk), [Claude Code skills documentation](https://code.claude.com/docs/en/skills), and [Gemini CLI skills documentation](https://geminicli.com/docs/cli/using-agent-skills/). Other agents may have different discovery rules; do not assume this path is hidden from an unreviewed agent.

## Read before reviewing

Start with `audit/SKILL-AUDIT-REPORT.md` and `SECURITY-POLICY.md`. A scanner `SAFE` recommendation is not a guarantee. `CAUTION`, `DO_NOT_INSTALL`, incomplete coverage, unresolved license rights, and package integrity gaps block approval. No imported scripts, installers, hooks, MCP servers, or other executable content were run during intake.
