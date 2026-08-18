# Evaluation Design

## Principles

1. **Fixed task set** — Once locked, changes require a new leaderboard version.
2. **Hybrid scoring** — Rule-based ground truth is primary. LLM judgment is secondary and structured.
3. **Comparable runs** — Same state schema, same tools interface, same logging across topologies.
4. **Full matrix** — Topology × Verifier × Failure intensity.

## Metrics (planned)

- Binary success (reached correct final state)
- Recovery success (succeeded *after* at least one injection)
- Extra steps / tokens caused by recovery
- Failure mode distribution
- Wall time under limits

## Anti-Patterns We Avoid

- Pure LLM-as-judge for the primary success metric
- Moving the task set every experiment
- Topology-specific evaluation logic
