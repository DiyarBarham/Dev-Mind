# Dev Mind — project memory

## Project context

Dev Mind is a public, MIT-licensed skill for Codex and Claude Code. The canonical
package is `skills/dev-mind/`. It preserves developer instructions, decisions,
useful attempts, procedures, and open threads in shared project Markdown.

## Active project-wide instructions

### cross-host-memory — Support Codex and Claude Code
- Kind: instruction
- Status: active
- Scope: whole project
- Source: repository creator's project request, 2026-09-26
- Updated: 2026-09-26
- Statement: Provide a well-written, documented public skill named Dev Mind for both hosts, with project-wide and area-specific memory.
- Why: Preserve context that otherwise disappears between AI coding conversations.
- Evidence: Explicit project brief; implementation is in `skills/dev-mind/`.

### github-proxy — Use the supplied local proxy for this maintainer's GitHub operations
- Kind: instruction
- Status: active
- Scope: current maintainer's local environment; not a requirement for skill consumers
- Source: repository creator's project request, 2026-09-26
- Updated: 2026-09-26
- Statement: Set `HTTPS_PROXY`, `HTTP_PROXY`, and `ALL_PROXY` to `http://127.0.0.1:7897` for GitHub operations in this environment.
- Why: Required networking route supplied by the maintainer.
- Evidence: Network-enabled `gh auth status --hostname github.com` and repository inspection succeeded through this proxy.

## Decisions and useful attempts

### shared-markdown — One canonical skill and shared project memory
- Kind: decision
- Status: accepted
- Scope: package architecture and installation
- Source: initial implementation, 2026-09-26; [design](docs/design.md)
- Updated: 2026-09-26
- Statement: Distribute one Markdown skill to both hosts, with a root `DEV_MIND.md` and optional linked area notes. Add host instruction bridges for fresh sessions.
- Why: Keep memory portable, readable, reviewable, and independent of hosted memory services.
- Evidence: Host documentation confirms skill discovery and separate startup instructions; installer preservation tests pass. Real host startup behavior still needs end-to-end verification.
- Alternatives: Background hooks and a database omitted from the initial release because they add host-specific behavior and operational dependencies.

### auth-sandbox — Restricted auth failure was misleading
- Kind: attempt
- Status: succeeded
- Scope: this environment's GitHub connectivity
- Source: local tool observations, 2026-09-26
- Updated: 2026-09-26
- Statement: Restricted `gh auth status` reported an invalid token; repeating with authorized network access succeeded without changing credentials.
- Why: Distinguish execution restrictions from actual authentication problems.
- Evidence: Successful keyring authentication and public repository inspection through the supplied proxy.
- Revisit when: A network-enabled check also fails; do not reset credentials based solely on the restricted result.

## Scope index

- [Design](docs/design.md): memory lifecycle, scoping, reconciliation, and limits.
- [Installation](docs/installation.md): host paths, conservative file handling, updates, and removal.
- [Evaluation](docs/evaluation.md): test evidence and remaining validation gaps.

## Open threads

### host-smoke-tests — Verify fresh sessions in both products
- Kind: open-thread
- Status: untested
- Scope: Codex and Claude Code discovery and startup behavior
- Source: initial validation scope, 2026-09-26
- Updated: 2026-09-26
- Statement: Run the documented two-session scenario in separate real Codex and Claude Code sessions.
- Why: File tests and one model simulation do not establish host-specific loading or consistent compliance.
- Evidence: Not yet tested end to end in both products.
