# Heuristic-First, LLM-Escalated

*A simple rule handles the easy cases. The LLM only gets pulled in when the rule abstains.*

## Problem

Most requests in a domain are repeatable — the same handful of cases hit again and again. A small number are novel, ambiguous, or outside coverage. Treating every request as if it needs full LLM reasoning overpays for the easy majority.

## Mechanism

A precomputed artifact — usually a ruleset, lookup table, or classifier — handles the requests it can answer with high confidence. When the artifact's coverage or confidence threshold is not met, the system escalates to a live LLM. The escalation is declared: documented, gated, and surfaced.

## Required properties

- **Versioned artifact:** the heuristic layer is itself a versioned, testable artifact.
- **Regeneration cadence:** the heuristic is refreshed when its coverage erodes.
- **Declared escalation:** the gating condition — low confidence, missing coverage, expired freshness, ambiguous input — is explicit. In user-facing tools, escalation is opt-in with disclosed cost. In enterprise systems, it is policy-, budget-, or admin-gated.

## Canonical example

[RightModel](https://rightmodel.dev) uses its compiled ruleset as the first layer. When the ruleset can't decide — novel task signals, conflicting evidence — the user is offered "deep analysis," a live LLM escalation with the cost disclosed before the user commits.

## When it fits

The request distribution is long-tailed: a small number of cases dominate volume. The cost gap between heuristic serving and live inference is large. Users accept a two-tier experience.

## When it doesn't

The request distribution is uniform. Every case requires open-ended reasoning. The escalation cost is unacceptable to users or operators.