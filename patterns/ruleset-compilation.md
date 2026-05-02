# Ruleset Compilation

*An LLM writes a decision table ahead of time. The application reads the table at request time.*

## Problem

A bounded decision surface — model selection, content classification, eligibility, routing — is being decided by a live LLM call on every request. The reasoning is stable; only the input varies. Token cost and latency compound across every request.

## Mechanism

Before request time, an LLM is prompted to enumerate the decision space and emit a structured ruleset: a JSON or YAML artifact mapping input conditions to outputs. The application loads this ruleset and serves directly from it. The LLM is not in the request path.

## Required properties

- **Versioned artifact:** the ruleset has a version ID, generation timestamp, and known input schema.
- **Regeneration cadence:** the ruleset is regenerated on a named schedule, or when underlying inputs (model pricing, available models, vendor changes) shift.
- **Declared coverage path:** when an input doesn't match a rule, or matches with low confidence, the system has a documented, gated path — live LLM escalation, deterministic fallback, or explicit abstention. No silent guesses.

## Canonical example

[RightModel](https://rightmodel.dev) compiles its model recommendation logic into "ruleset v2," a JSON artifact mapping coding task signals to model tiers. Requests served by the ruleset cost zero tokens. When the ruleset can't decide, the user can opt into "deep analysis" — a disclosed-cost live LLM call.

## When it fits

The decision surface is enumerable. The reasoning changes more slowly than request frequency. Coverage gaps are detectable. Escalation cost is acceptable for the residual cases.

## When it doesn't

The decision space is open-ended or highly personalized. Rules cannot capture the distinguishing reasoning. Coverage cannot be defined.