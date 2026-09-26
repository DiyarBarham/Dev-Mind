# Contributing

Open an issue describing a concrete memory failure or send a focused pull request. Include the scenario, current behavior, desired behavior, and a redacted example. Do not post private conversations, credentials, or customer data.

The canonical skill lives in `skills/dev-mind/`. Keep the entry point concise and use references for conditional detail. Prefer changes that improve a demonstrated decision over adding universal rules for hypothetical situations. Preserve compatibility with Codex and Claude Code, and keep project memory separate from skill instructions.

For installer changes, run:

```sh
python3 -m unittest discover -s tests -v
```

Add behavioral coverage for changed file-handling behavior. For skill changes, use the scenarios in [evaluation](docs/evaluation.md), inspect the resulting memory artifacts, and document what was actually evaluated. Do not present a model's self-assessment as proof of correctness.

Keep documentation, bootstrap bridge, and installer behavior consistent. Changes should preserve existing instructions, memory, and local customizations. Contributions are provided under the repository's MIT license.
