# A fresh-session walkthrough

This is an illustrative scenario, not a report of a deployment or integration test.

## Session one

Developer: “Production deploys go through `release.yml`. Don't run migrations from a laptop. Investigate why large uploads time out.”

The agent reads project memory, records the deployment constraint with developer provenance, and investigates. Increasing retry count still returns 504 for large staging uploads. Background processing passes the staging reproduction.

It records two attempts with their conditions and evidence, plus the decision to use background processing and its tradeoff: callers must poll for completion. It does not claim production is verified. The root links an uploads area, while the project-wide migration prohibition stays visible in root memory.

## Session two

Developer: “Could we simplify this back into a synchronous request?”

The new agent reads `DEV_MIND.md` and the uploads area. It explains the previous failure and checks whether timeout limits or workload requirements have changed. It can propose a new experiment if the conditions changed; it does not blindly repeat the old test or claim synchronous processing can never work.

Developer: “For the new staging environment, use `preview.yml` this week.”

The agent records that temporary staging instruction without replacing the production deployment rule. If the expiry date is unclear, it preserves the wording and source date rather than inventing a precise deadline.

## What a human should review

The useful artifact is the memory diff: scoped requirements, accurate observations, the bounded success claim, and links that let a future session find the relevant record. The conversation itself need not be copied into the repository.
