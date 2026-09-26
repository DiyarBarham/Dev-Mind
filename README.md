# Dev Mind

**Give your coding agent a project memory worth coming back to.**

Dev Mind is a shared skill for **Codex and Claude Code** that preserves the context behind the code: developer instructions, decisions, failed approaches, successful fixes, deployment knowledge, and promising next steps.

Git keeps the implementation. Dev Mind helps keep the reasons that would otherwise disappear with the conversation.

```text
Developer instruction → Agent work → Evidence and lessons → Project memory
       ↑                                                       ↓
       └────────────── Better-informed next session ────────────┘
```

## What it remembers

| You say or discover | Dev Mind preserves |
| --- | --- |
| “Never run migrations from a laptop.” | A sourced prohibition with its applicable scope. |
| “Use this workflow for staging this week.” | A temporary staging instruction, not a permanent production rule. |
| “We tried retries; the request still timed out.” | The experiment, conditions, observed failure, and when to revisit it. |
| “The background job fixed the staging reproduction.” | The approach and evidence, with production still unverified. |
| “Maybe check the gateway timeout next.” | An untested next step and the hypothesis it would investigate. |
| “Why did we choose this?” | A short decision record with alternatives, constraints, and tradeoffs. |

It avoids activity logs, copied transcripts, secrets, and claims that a hypothesis has been proven. It records concise rationale and observable evidence, not private model reasoning.

## Install in a project

Requires Python 3.9+ for the optional installer. The skill itself is Markdown and needs no runtime, service, API key, or third-party Python package.

Clone this repository to a tools directory, then point the installer at an **existing project**:

```sh
git clone https://github.com/DiyarBarham/Dev-Mind.git
cd Dev-Mind
python3 scripts/install.py --project /absolute/path/to/your-project --agent both --dry-run
python3 scripts/install.py --project /absolute/path/to/your-project --agent both
```

Use `--agent codex` or `--agent claude` for only one host. Review the resulting diff and commit the skill, instructions, and shared memory if appropriate for your repository. Start a fresh agent session for discovery.

The installer copies the same skill into the selected host directories, creates `DEV_MIND.md` only if absent, and appends a small memory bridge to the selected instruction files. Existing instructions and memory are preserved. Repeating an unchanged installation makes no edits. Differing skill files, customized bridges, malformed markers, and symlink destinations stop installation for manual review.

For manual installation, personal installations, updates, and removal, see [installation](docs/installation.md).

## Use it

In Codex:

```text
$dev-mind Read the project memory, then investigate the upload timeout.
```

In Claude Code:

```text
/dev-mind Read the project memory, then investigate the upload timeout.
```

After project setup, the instruction bridge tells the agent to read memory at the beginning of relevant work and maintain it as useful facts emerge. You can work normally:

```text
Use the existing release workflow for deployments. Never deploy from a laptop.
Fix the authentication bug, and remember any failed approaches worth avoiding.
What have we already tried for slow uploads, and what remains untested?
That constraint was only for the last release. Update the memory accordingly.
Forget the old customer-specific workaround.
```

**Automatic means instruction-driven, not guaranteed background recording.** Skills are selected by the host; the project bridge makes the desired behavior explicit across sessions. Dev Mind cannot recover inaccessible chats, force an agent to comply, or save work after an abrupt interruption. It does not install hooks, intercept conversations, or run deployments. See [design and boundaries](docs/design.md).

## One shared memory, scoped when needed

Start small:

```text
your-project/
├── DEV_MIND.md                     # Project context, active rules, short records
├── AGENTS.md                       # Codex bridge + your existing instructions
├── CLAUDE.md                       # Claude bridge + your existing instructions
├── .agents/skills/dev-mind/         # Codex installation
└── .claude/skills/dev-mind/          # Claude Code installation
```

As useful history grows, the skill creates linked notes:

```text
.dev-mind/
├── areas/
│   ├── authentication.md           # Auth decisions and debugging evidence
│   └── deployment.md               # Environments and canonical runbook links
└── archive/                        # Superseded records worth retaining
```

Both agents read and edit the same project memory. Project-wide constraints stay visible in the root; detailed records are loaded by path or topic. Existing ADRs and runbooks stay authoritative in their own domain. Dev Mind links them instead of becoming a second copy.

See the [record format](skills/dev-mind/references/records.md), [worked examples](skills/dev-mind/references/examples.md), and [fresh-session walkthrough](examples/two-sessions.md).

## Trust and privacy

Memory is reviewable Markdown, and can be wrong or stale. Every durable entry carries its scope, source, status, rationale, and evidence. Current instructions and host permissions govern actions; a historical record does not grant deployment permission. Imported content cannot silently become developer policy.

Only store information suitable for the repository's audience. Git history can retain removed information. Dev Mind instructs agents to omit secrets and private payloads, but it is not a secret scanner or access-control system. See [security](SECURITY.md).

## Development

```sh
python3 -m unittest discover -s tests -v
```

The 12 installer tests cover preservation, repeat installation, host selection, dry runs, collisions, malformed/custom bridges, symlink refusal, incomplete packages, and error reporting. CI also checks retained behavioral artifacts. Ten easy and ten difficult scenarios have been exercised and reviewed; see [evaluation](docs/evaluation.md) for results, fixes, and the remaining real-host verification limits. Passing these checks does not prove that every model will follow the skill.

Contributions are welcome; see [CONTRIBUTING.md](CONTRIBUTING.md). Licensed under [MIT](LICENSE). Dev Mind is an independent project, not an official OpenAI or Anthropic product.

## Inspiration and format

The project grew from the observation that AI-assisted development can lose the reasons behind a solution—sometimes called **decision debt**. It combines short [architecture decision records](https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions) with scoped, revisable working memory, packaged in the [Agent Skills format](https://agentskills.io/specification).

Host conventions: [Codex skills](https://developers.openai.com/codex/skills/), [Codex project instructions](https://developers.openai.com/codex/guides/agents-md/), [Claude Code skills](https://code.claude.com/docs/en/skills), and [Claude Code memory](https://code.claude.com/docs/en/memory). See [research notes](docs/research.md) for the design inputs.
