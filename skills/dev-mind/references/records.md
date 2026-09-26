# Memory record format

Use ordinary Markdown. No database, timestamps on every sentence, or full conversation dumps are needed. Each record should answer the fields below; omit conditional fields when irrelevant.

```markdown
### auth-cookie-scope — Keep sessions host-only
- Kind: decision
- Status: accepted
- Scope: `services/auth/`, browser session cookies
- Source: developer instruction, 2026-09-26; `docs/adr/007-sessions.md`
- Updated: 2026-09-26
- Statement: Use host-only cookies for the customer portal.
- Why: Sibling applications have independent trust boundaries.
- Evidence: ADR 007; session integration tests passed on commit <actual SHA>.
- Alternatives: Shared parent-domain cookie rejected because it widens access.
- Revisit when: The application trust model changes.
```

Use an actual observed date and actual evidence in live records. Example values and placeholders are not facts. A chat-only source can be “developer instruction, YYYY-MM-DD, brief faithful paraphrase”; it does not require a fabricated message ID or transcript URL.

## Required meaning

| Field | Purpose |
| --- | --- |
| ID and title | A descriptive, stable heading unique within its file. |
| Kind | `instruction`, `decision`, `attempt`, `procedure`, or `open-thread`. |
| Status | State the type-specific status below. |
| Scope | Project-wide, affected paths/topic/environment, or task/release-limited. |
| Source | Who requested it or where it was observed, with a date or durable reference. |
| Updated | Date the content was last materially changed. |
| Statement | The rule, decision, observation, procedure link, or proposed action. |
| Why | Known rationale; say “not stated” when absent. |
| Evidence | Observations and verification limits; “not tested” when appropriate. |

Add alternatives, retry conditions, consequences, expiry, replacement links, or next steps where useful. Avoid repetitive empty headings.

For relative limits such as “this week,” retain the original wording and source date. Normalize to an exact expiry only when the calendar boundary and timezone are known. If the ambiguity affects an action in a later session, clarify applicability before that action; do not silently extend the exception.

## Status vocabulary

- Instructions: `active`, `superseded`, `expired`.
- Decisions: `proposed`, `accepted`, `superseded`.
- Attempts: `failed`, `succeeded`, `inconclusive`.
- Procedures: `documented` (not verified), `verified`, `stale`.
- Open threads: `untested`, `blocked`, `resolved`, `abandoned`.
- Any kind may be `disputed` or `stale` when applicable; explain the uncertainty.

Success is scoped to its evidence. A unit test passing is not proof of a successful production deployment. A command failing due to a sandbox restriction is not evidence that credentials are invalid. An interruption is not a failed hypothesis.

## Debugging records

Record the symptom, relevant environment/version, attempted change, observable outcome, safe evidence reference, and retry condition. Write “request still timed out after increasing pool size” rather than “the database is broken.” Keep causal explanations labeled as hypotheses until tested. Mention temporary edits that remain; do not imply they were reverted unless observed.

## Deployment records

Prefer a link to the authoritative runbook. Otherwise retain the environment, approved method, non-secret prerequisites, working directory, verified commands, health check, and rollback reference if known. Record which steps have actually run. Missing rollback knowledge remains an open question, not an invented command. Past permission to deploy does not authorize an unrelated future deployment.
