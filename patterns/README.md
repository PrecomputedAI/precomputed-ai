# Patterns

Things you can precompute under [Precomputed AI](https://precomputedai.com):

- **[Reasoning](./reasoning.md)** — LLM-authored prose alongside deterministic decisions. Canonical example: [RightModel](https://rightmodel.dev).
- **[Constraints](./constraints.md)** — boundaries where the default answer stops holding. Canonical example: [RunWhere](https://runwhere.dev).
- **[Snapshots](./snapshots.md)** — point-in-time captures of state, regenerated on a named cadence. Canonical example: [CloudEstimate](https://cloudestimate.dev).

Each artifact type meets the three required properties — versioned artifact, regeneration cadence, declared escalation path — when wired into a real system. The catalog grows as new artifact types ship with worked examples.

## Contributing

A pattern earns a name when it has a shipped worked example and meets all three required properties. PRs without a worked example will be redirected to an issue tagged `pattern-candidate` until a demo exists.

Open a PR against this directory with a new pattern file following the structure of the existing patterns: problem, mechanism, required properties, canonical example, when it fits, when it doesn't.