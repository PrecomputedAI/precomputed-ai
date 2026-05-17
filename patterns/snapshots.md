# Snapshots

*The artifact refreshes on a named cadence. Like a newspaper, not a livestream.*

## Problem

The reasoning is stable enough to precompute, but the underlying world state changes — prices shift, models are released, vendor architectures evolve. A precomputed artifact that never regenerates becomes silently wrong. A live LLM call on every request is the wrong solution to staleness.

## Mechanism

A scheduled job — daily, weekly, or triggered by an external event — regenerates the artifact. Between runs, the application serves from the static snapshot. The freshness window is surfaced to the user, typically as a "last refreshed" timestamp.

## Required properties

- **Versioned artifact:** each regeneration produces a new versioned snapshot.
- **Regeneration cadence:** the schedule is named and enforced. The staleness window is a property of the system, not an accident.
- **Declared escalation path:** when freshness has expired or the artifact does not cover an input, the next step is documented — live LLM escalation, deterministic fallback, or explicit abstention.

## Canonical example

[CloudEstimate](https://cloudestimate.dev) prices self-managed workloads across AWS, GCP, and Azure against scheduled regional pricing snapshots and serves LLM-generated sizing explanations from a versioned artifact cache. Both the pricing and explanation artifacts refresh daily via GitHub Actions. The "Pricing data last refreshed" footer surfaces the staleness window directly to the user.

## When it fits

The world state changes on a knowable cadence. Users tolerate a known staleness window. Regeneration cost is bounded and predictable.

## When it doesn't

The world state changes faster than any reasonable refresh interval. Users require strict real-time accuracy. Regeneration cost approaches the saved inference cost.