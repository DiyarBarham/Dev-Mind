# Research and design inputs

Reviewed for the initial implementation on 2026-09-26. Vendor conventions can change; follow the linked primary documentation when updating integrations.

- [Agent Skills specification](https://agentskills.io/specification): portable skill folders with YAML frontmatter and Markdown instructions. Dev Mind keeps one shared entry point and supporting resources.
- [Codex skills](https://developers.openai.com/codex/skills/) and [project instructions](https://developers.openai.com/codex/guides/agents-md/): skills and project startup instructions have different roles. Dev Mind supplies both a discoverable skill and a small project bridge. Context7's `/openai/codex` source confirmed project `.agents/skills` discovery and supported user skill roots.
- [Claude Code skills](https://code.claude.com/docs/en/skills) and [memory](https://code.claude.com/docs/en/memory): skill bodies load when used; project instructions provide continuity. Context7's `/websites/code_claude` documentation confirmed skill invocation and `.claude/skills` conventions.
- [Michael Nygard, Documenting Architecture Decisions](https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions): retain the context, choice, and consequences behind meaningful architecture decisions. Dev Mind extends that practical idea to experiments, scoped instructions, and operational knowledge without replacing ADRs.
- [GDS, Documenting architecture decisions](https://gds-way.digital.cabinet-office.gov.uk/standards/architecture-decisions.html): keep meaningful decision context alongside project work.

The repository creator supplied an unattributed article about “decision debt” as inspiration. Its framing informed the problem statement; this project does not claim authorship of that article, reproduce it, or assert ownership of the term.
