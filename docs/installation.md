# Installation and lifecycle

## Project installation (recommended)

Run `scripts/install.py --project <existing-directory> --agent both` from a clone of this repository. Choose `codex` or `claude` for a single host. Preview with `--dry-run`. Python 3.9+ is required; no pip installation is needed.

The project path may contain spaces when quoted. The script preflights all planned destinations before writing, rejects symlinks inside the selected project, preserves existing bytes in instruction files, and leaves existing memory untouched. It resolves the project path itself, so a project path alias targets its resolved directory.

Run it while no other process is editing the installation destinations. It detects common concurrent changes but is not a filesystem transaction: an I/O failure or concurrent write can leave a partial installation. Inspect the diff, resolve the cause, and rerun. It never commits, pushes, changes global configuration, or executes project commands.

## Manual installation

Copy the entire `skills/dev-mind/` directory, including its references and assets, to one or both destinations:

| Host | Project | Personal, all projects |
| --- | --- | --- |
| Codex | `.agents/skills/dev-mind/` | `~/.agents/skills/dev-mind/` |
| Claude Code | `.claude/skills/dev-mind/` | `~/.claude/skills/dev-mind/` |

Codex also supports its configured skills directory, commonly `~/.codex/skills/`. Claude custom configuration roots can relocate its personal directory. Prefer a single active copy per host to avoid ambiguity.

Create root `DEV_MIND.md` from the [template](../skills/dev-mind/assets/DEV_MIND.md), without overwriting existing memory. Append the [bridge](../skills/dev-mind/references/bootstrap.md) to `AGENTS.md` for Codex and `CLAUDE.md` for Claude. Preserve all existing instructions. For a personal installation, initialize each project separately; personal skill availability alone does not enable project startup instructions.

Start a new session, invoke `$dev-mind` or `/dev-mind`, and ask the agent to identify the memory it loaded. If it cannot find the skill, check the destination folder and host configuration. The public package targets Codex and **Claude Code**, not automatic installation in the Claude web app.

## Updates

Review upstream changes, then compare your installed skill directory against `skills/dev-mind/`. Merge local customizations deliberately. The installer refuses to overwrite differing skill files; it is not an upgrade manager. Do not replace `DEV_MIND.md` or `.dev-mind/` when upgrading skill instructions. They belong to the consuming project.

For a clean unmodified installation, you may remove only the installed `dev-mind` skill directories and rerun the installer after reviewing the new version. Preserve or reconcile any customized bridge before rerunning.

## Removal

Remove only the selected hosts' `skills/dev-mind/` folders and the block between `<!-- dev-mind:start -->` and `<!-- dev-mind:end -->` in their project instructions. Preserve surrounding instructions. Memory can remain as ordinary documentation; remove it separately only if desired. Removal does not erase Git history.

## GitHub behind a local proxy

If your environment requires a proxy, prefix the GitHub command with your own proxy settings. For example:

```sh
HTTPS_PROXY=http://127.0.0.1:7897 \
HTTP_PROXY=http://127.0.0.1:7897 \
ALL_PROXY=http://127.0.0.1:7897 \
gh auth status --hostname github.com
```

This is an optional local networking example, not a requirement for Dev Mind. Do not put proxy credentials into shared memory.
