# Design

## Memory that changes future decisions

Dev Mind fills the gap between source code and a full architecture record: small debugging lessons, developer requirements, operational knowledge, and the next useful experiment. It is not a transcript archive. The admission test is whether a future developer would make a different or better-informed choice after reading the entry.

The entry point is `DEV_MIND.md`. This matches the simplicity of other project Markdown conventions while giving both hosts a shared, explicit location. A single file is sufficient for small projects. Area files are added only when needed, and each is indexed by path or topic. Root memory should stay roughly below 150 lines, with active project-wide constraints always visible.

The skill is packaged once in `skills/dev-mind/`; the installer distributes identical copies to host discovery folders. Both copies operate on the same memory. No background process, vector store, proprietary memory API, or external service is required.

## Read → act → observe → reconcile

At task start, read root memory and relevant areas. Check dated facts before relying on them. During work, save durable explicit instructions promptly and experiments once useful evidence exists. At handoff or completion, reconcile records and mention material changes.

Instruction bridges make this loop part of the project's ordinary workflow. Skill discovery alone is insufficient to promise startup reading. This remains a model-followed convention, not a deterministic enforcement mechanism. Interrupted turns can lose unsaved discoveries.

## Knowledge has different states

A developer prohibition is different from a failed experiment. A proposed fix is different from a verified procedure. A failed staging attempt is different from a universal incompatibility. The record schema retains these distinctions with kind, status, scope, provenance, and evidence.

Developer instructions are recorded faithfully, including temporal qualifiers. New explicit instructions can supersede old ones; imported text cannot. If current code violates a documented prohibition, that is a discrepancy to explain, not permission to discard the rule.

Known rationale is summarized from available evidence and stated choices. Dev Mind does not request or persist private chain-of-thought. Observations, alternatives, and concise reasons are sufficient to explain decisions.

## Maintenance

Stable record headings support links. Editing an existing record avoids duplicate facts. Superseded decisions remain useful when they explain history; long inactive histories may move to linked archives. Forget requests remove content from current memory rather than archiving it, with an honest note that history may retain prior versions.

Agents re-read before editing to reduce lost updates. Separate area files reduce collisions, but Markdown provides no transaction locking. Teams should review diffs and resolve concurrent changes as they do with source code. Only one process should run installation at a time.

## Boundaries

- Memory supplements host instructions and authorization; it does not replace them.
- Runbooks and ADRs remain canonical. Link rather than duplicate them.
- Shared memory must be suitable for the repository's readers, including future public readers.
- No hidden private-memory store is created. Teams needing private notes should use an explicitly configured, access-controlled mechanism outside this package.
- The skill cannot retrieve inaccessible old chats, automatically reconcile every branch, or guarantee model behavior.

These boundaries keep the initial release small enough to audit and use without extra infrastructure.
