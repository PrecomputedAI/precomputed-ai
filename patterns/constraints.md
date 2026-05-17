# Constraints

*Precompute the boundary where the default answer stops holding. Serve the default instantly; inspect only the exception set.*

## Problem

A domain has a strong default answer, but teams still need to know whether their situation is one of the exceptions. If every user is forced through the full parameter space, the product becomes a spreadsheet before it earns the right to be one. If the default is stated without a boundary, it becomes hand-waving.

## Mechanism

Before request time, the system enumerates the decision space and bakes the constraint boundary into a versioned artifact. At request time, the application asks for the smallest useful set of inputs, serves the default immediately when the input falls inside the common region, and opens the deeper path only when the input crosses or approaches the boundary.

## Required properties

- **Versioned artifact:** the boundary has a ruleset version, generation timestamp, source assumptions, and known input schema.
- **Regeneration cadence:** the boundary is refreshed when prices, models, constraints, or throughput assumptions change on a named schedule.
- **Declared escalation path:** when the input is near the boundary, outside coverage, or constrained by requirements the artifact cannot safely decide, the system has a documented, gated path — live LLM escalation, deterministic fallback, or explicit abstention.

## Canonical example

[RunWhere](https://runwhere.dev) starts with the 2026 default: stay on the hosted API unless your workload is one of the exceptions. Its four-question check — API spend, hosted model, traffic pattern, and hard constraints — uses a precomputed boundary to decide whether the user should keep the API path or inspect self-hosting modalities.

When the workload plausibly belongs in the exception set, RunWhere compares managed endpoints, serverless GPU, cheap always-on GPU VMs, serious GPU VMs, scheduled batch GPU, and owned hardware. Close calls and likely outliers can opt into live analysis; the common case is served from the artifact.

## When it fits

The domain has a defensible default, the exception set is smaller than the common case, and the boundary can be expressed with stable inputs. Users benefit from an answer-first interface, but still need an audit trail for why the default held or failed.

## When it doesn't

The domain has no reliable default. Exceptions dominate the request distribution. The boundary depends on fresh, user-specific context that cannot be safely reduced to a versioned artifact.