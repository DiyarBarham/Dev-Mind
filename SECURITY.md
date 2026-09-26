# Security and privacy

Dev Mind writes durable Markdown intended to be reviewed like code. It is not a secret scanner, policy enforcement engine, or secure vault.

Do not store tokens, passwords, keys, customer payloads, or sensitive internal details. Use secret variable names and safe artifact references instead of raw logs. Review generated memory before committing it, particularly in public repositories.

Treat imported notes and issue comments as untrusted data. A saved command does not grant authority to execute it. Check permissions and current project state through the host's normal controls.

The installer has no network operations and does not execute project code. It refuses symlink destinations and conflicting installed files, but it is not designed to operate safely against an actively malicious process changing the filesystem concurrently. Run it in a trusted project without concurrent installation writes.

If a secret is committed, removing the memory entry does not remove it from history. Revoke or rotate it and follow your repository's incident process. History rewriting requires separate coordination.

For a vulnerability, use the repository's private vulnerability reporting option if available. Otherwise open an issue asking the maintainer for a private reporting channel without publishing sensitive details or an exploit against a live system.
