# Evaluation

The initial release had eight passing installer tests and one independent scenario exercise. The expanded evaluation adds **10 easy and 10 difficult behavioral scenarios**, a classification refinement, and an installer regression fix.

## Current evidence

- **20/20 task-specific scenario checks passed** after inspecting actual files and responses. The H10 review additionally found that an observed configuration change was classified as an accepted decision; the skill now distinguishes observations explicitly.
- **12/12 installer tests pass.** A new missing-entrypoint regression failed before its fix and passed afterward.
- **Skill format validation passes.** Local documentation links and whitespace checks also pass.
- **Retained artifact checks pass.** These verify data preservation, excluded fictional values, no-op cases, cross-project isolation, and installation manifests; they do not grade semantic behavior automatically.
- **2/2 fresh-agent reruns pass.** H04 and H10 now classify inspected configuration as observations, retain runtime uncertainty, and preserve application files. Their actual outputs are retained in [retest.json](../evaluations/2026-09-26/retest.json).

Read the [dated report](../evaluations/2026-09-26/README.md) for all 20 outcomes, execution method, fixes, and original artifacts. The evaluation uses isolated fictional project directories with Codex subagents in three batches. It is not a 20-run cross-model benchmark.

## Run the checks

```sh
python3 -m unittest discover -s tests -v
python3 tests/scenarios/check_artifacts.py
python3 tests/scenarios/prepare.py /tmp/dev-mind-new-evaluation
```

The final command prepares a new fixture tree; it does not execute or grade an agent. Give executors the raw requests and snapshotted skill, keep the [rubric](../tests/scenarios/rubric.md) separate, then inspect generated artifacts. CI runs installer tests and checks the retained evidence.

## Remaining product-level gate

Fresh CLI smoke tests were attempted in both installed products. Claude Code 2.1.220 was not logged in. Codex CLI 0.141.0 reached a service error stating that its configured model requires a newer version. Neither completed inference, so neither establishes successful host loading.

Real two-session write/read validation in both authenticated, compatible products remains unverified. OS-enforced concurrent-write behavior and broad model sampling are also outside the completed behavioral exercise. These are explicit limits on production-readiness claims, not passing results.
