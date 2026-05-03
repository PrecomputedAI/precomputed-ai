# Explanation Caching

*An LLM writes the reasoning layer ahead of time. The application serves precomputed explanations at request time; the decision logic itself is deterministic.*

## Problem

A bounded decision surface — model selection, content classification, eligibility, routing — is handled by deterministic logic that already works. But users need to understand *why* they got the answer they got. Generating that explanation with a live LLM call on every request burns tokens and adds latency for reasoning that rarely changes between inputs of the same class.

## Mechanism

Before request time, an LLM is prompted to generate explanations for each region of the decision space. The resulting explanation cache — a JSON or YAML artifact mapping decision outcomes to human-readable reasoning — is versioned and served alongside the deterministic result. The decision logic runs without the LLM. The explanation layer is the precomputed artifact.

## Required properties

- **Versioned artifact:** the explanation cache has a version ID, generation timestamp, and known mapping to the decision outputs it covers.
- **Regeneration cadence:** the explanation cache is regenerated on a named schedule, or when the underlying decision surface changes (new models, changed pricing, shifted capabilities).
- **Declared coverage path:** when an input doesn't have a precomputed explanation, or the explanation has expired, the system has a documented, gated path — live LLM escalation, deterministic fallback, or explicit abstention. No silent guesses.

## Canonical example

[RightModel](https://rightmodel.dev) maps coding task signals to model tiers using deterministic decision logic. The PAI artifact is the explanation cache: precomputed, LLM-authored reasoning for each recommendation, versioned and served alongside the result. Requests served from the cache cost zero tokens. When the cached explanation can't cover a case — novel input, edge case, user wants deeper reasoning — the user can opt into "deep analysis," a disclosed-cost live LLM call. The numbers question this answers: what does it cost to keep the explanation layer fresh, and what does that buy us?

## When it fits

The decision logic is already deterministic. The value the LLM adds is the reasoning layer — the "why," not the "what." Explanations change more slowly than request frequency. Coverage gaps in the explanation space are detectable.

## When it doesn't

The decision itself requires live LLM reasoning. Explanations are highly personalized or context-dependent. The explanation space is too large to precompute meaningfully.
