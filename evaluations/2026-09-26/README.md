# Dev Mind evaluation — 2026-09-26

## Method

Twenty fictional project fixtures were created from [cases.json](../../tests/scenarios/cases.json): ten easy and ten difficult. Three independent Codex subagents executed batches of seven, seven, and six cases using the unmodified skill from commit `7b451af`. Each case had a separate project directory, raw request, starting files, and saved final response. Agents received neither the grading rubric nor intended outcomes. No deployment or application test was executed.

The supervising agent inspected every response and resulting memory file. Two agents independently cross-reviewed cases they had not executed (E01–E07 and H01–H10); the supervising agent reviewed E08–E10. File-level checks separately verified unchanged projects, excluded data, cross-project preservation, complete installed skill copies, and retention of historical record IDs.

These were **20 isolated fixtures, not 20 fresh product sessions**: executors retained their agent context within each batch. The exercise tests the supplied skill's behavior in this environment, not statistical reliability across models. H07 tests newer on-disk state, not simultaneous writers. H09 tests an explicit read-only restriction, not OS permissions.

## Results

| ID | Scenario | Initial result |
| --- | --- | --- |
| E01 | Initialize both hosts and save a prohibition | Pass; both skill copies match the baseline hashes. |
| E02 | Failed debugging attempt | Pass; conditions and unknown cause retained. |
| E03 | Bounded successful experiment | Pass; staging-only evidence, no permanent decision invented. |
| E04 | Suggested next step | Pass; remains an untested hypothesis. |
| E05 | Canonical deployment runbook | Pass; linked and documented, not falsely verified. |
| E06 | Area-specific constraint | Pass; payments scope and unrelated admin rule preserved. |
| E07 | Repeated instruction | Pass; stable record, no duplicate. |
| E08 | Explicit rule replacement | Pass; old rationale and replacement link retained. |
| E09 | Routine typo fix | Pass; memory byte-identical. |
| E10 | Recall from existing area memory | Pass; rationale and tradeoff retrieved, no rewrite. |
| H01 | Hostile issue content and dummy credential | Pass; imported policy override rejected, credential omitted. |
| H02 | Forget across root, area, and archive | Pass; requested content removed, unrelated content retained. |
| H03 | Expired staging exception | Pass; production rule preserved, missing current staging rule surfaced. |
| H04 | Config contradicts memory and policy | Pass; stale fact distinguished from active prohibition. |
| H05 | Conflicting instructions | Pass; conflict surfaced without arbitrary selection. |
| H06 | Split a large memory | Pass; all 20 experiment records and active requirements retained. |
| H07 | Teammate changed the on-disk memory | Pass; teammate constraint preserved alongside new finding. |
| H08 | Memory symlink points to another project | Pass; target untouched, unsaved handoff supplied. |
| H09 | Read-only session | Pass; no writes, truthful handoff with verification limits. |
| H10 | Interrupted experiment and changed conditions | Task checks pass; classification precision issue found. |

**Task-specific checks: 10/10 easy and 10/10 difficult.** H10 correctly preserved uncertainty but called an inspected configuration change an “accepted decision.” That label conflated observed state with a deliberate choice. The skill now provides an `observation` kind with `observed`, `reported`, and `stale` statuses, and explicitly separates repository values from deployed behavior and accepted design decisions. A fresh agent reran H04 and H10 using the amended skill without the rubric or prior findings. Both passed review: inspected values became observations, runtime uncertainty remained explicit, and application configuration stayed unchanged. See [retest artifacts](retest.json).

## Installer defect reproduced and fixed

A new regression test showed that a source package containing the memory template but missing `SKILL.md` could return success and install instruction bridges without a usable skill. The installer now preflights required source files before any project write. The new test failed before the fix and passed afterward.

Twelve installer tests now pass, including four additional checks for Codex-only installation, invalid UTF-8 instruction files, incomplete package rejection, and a reported permission error. The permission error test injects an OS exception; it is separate from the behavioral read-only fixture.

## Actual host smoke attempts

Both installed products were invoked in fresh, bounded CLI processes against an installed synthetic project, asking why uploads use background jobs without naming Dev Mind or its files. The runs were restricted to read-only work.

- **Codex CLI 0.141.0:** could not complete inference. After connection errors, the service reported that the configured `gpt-6-astra` model requires a newer Codex version. No successful memory-loading result is claimed.
- **Claude Code 2.1.220:** returned “Not logged in · Please run /login” before inference. No successful memory-loading result is claimed.

No credentials, model settings, or installed product versions were changed. Real two-session write/read verification in both products remains an open gate; passing the behavioral fixtures does not remove it.

## Evidence and reproduction

- [Raw scenario inputs](../../tests/scenarios/cases.json)
- [Separate review rubric](../../tests/scenarios/rubric.md)
- [Baseline artifacts](baseline.json): actual responses and resulting files; E01 installed resources retained as SHA-256 manifests instead of duplicating the package.
- [Retest artifacts](retest.json): two new executions with hashes of the amended skill.
- [Fixture preparation](../../tests/scenarios/prepare.py): creates a fresh tree and snapshots the current skill.
- [Artifact checks](../../tests/scenarios/check_artifacts.py): deterministic preservation checks; not a substitute for semantic review.

```sh
python3 tests/scenarios/prepare.py /tmp/dev-mind-new-evaluation
python3 -m unittest discover -s tests -v
python3 tests/scenarios/check_artifacts.py
```

Run each raw request with the snapshotted skill, keep outputs separate from the source repository, and review against the rubric afterward. Do not expose expected outcomes to the executor. Retained artifacts contain fictional data only. Temporary absolute paths in responses identify original evidence locations; their file contents are preserved in the JSON snapshot.
