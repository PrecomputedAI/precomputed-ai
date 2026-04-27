# Patterns

Named patterns under the [Precomputed AI](https://precomputedai.com) frame. Each pattern applies the three required properties — versioned artifact, regeneration cadence, declared escalation — to a specific class of problem.

| Pattern | Canonical example |
|---|---|
| [Ruleset Compilation](./ruleset-compilation.md) | [RightModel](https://rightmodel.dev) |
| [Scheduled Generation](./scheduled-generation.md) | [CloudEstimate](https://cloudestimate.dev) |
| [Heuristic-First, LLM-Escalated](./heuristic-first-llm-escalated.md) | [RightModel](https://rightmodel.dev) |

## Contributing

A pattern earns a name when it has a shipped worked example and meets all three required properties. Pattern PRs without a worked example will be redirected to an issue tagged `pattern-candidate` until a demo exists.

Open a PR against this directory with a new pattern file following the structure of the existing three: problem, mechanism, required properties, canonical example, when-it-fits, when-it-doesn't.