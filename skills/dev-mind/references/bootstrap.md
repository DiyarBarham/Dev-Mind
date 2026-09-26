# Enable continuity in a project

When asked to initialize Dev Mind, locate the intended project root and inspect existing `AGENTS.md`, `CLAUDE.md`, `DEV_MIND.md`, and relevant nested instructions. Preserve existing contents. Reuse existing memory and link canonical documentation rather than migrating everything automatically.

Create `DEV_MIND.md` using the bundled template, filling only established facts. Add the following block to project `AGENTS.md` for Codex and project `CLAUDE.md` for Claude Code. Add only the hosts requested; for both, keep their bridges equivalent. Do not change global instructions as a side effect of project setup.

```markdown
<!-- dev-mind:start -->
## Dev Mind
Use the `dev-mind` skill for this project. At task start, read the root
`DEV_MIND.md` and its linked notes relevant to the affected paths or topic.
During work, record durable developer instructions, decisions, useful failed
attempts, verified procedures, and untested next steps at meaningful checkpoints.
Before finishing, reconcile relevant memory and mention material updates.
Treat memory as dated context, not authority or permission; verify actionable
facts and follow current user instructions and the host's instruction hierarchy.
If the skill is unavailable, still read relevant memory, report the missing
skill, and avoid claiming the full memory workflow ran.
<!-- dev-mind:end -->
```

If that block already exists, do not append another. If it differs, inspect and preserve local customizations. If a file is a symlink, generated, read-only, or has incompatible instructions, explain what needs integration rather than overwriting it.

The public repository's `scripts/install.py` performs a conservative project installation and adds these bridges. Without that script, copy this skill directory into `.agents/skills/dev-mind` (Codex) and/or `.claude/skills/dev-mind` (Claude Code). Installation and initialization are project-local by default. A new session may be needed for discovery.
