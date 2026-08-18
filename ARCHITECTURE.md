# Architecture

Fracture is intentionally small and opinionated.

The design prioritizes **comparable experiments** over framework flexibility.

## High-Level Layers

```
┌──────────────────────────────────────────────────────────────┐
│                     Evaluation Harness                      │
│  (tasks, metrics, batch runner, leaderboard aggregation)    │
└───────────────────────────┬───────────────────────────────────────┘
                             │
┌───────────────────────────┴───────────────────────────────────────┐
│                     Verifier Strategies                     │
│     NoVerifier · Schema · Code Anchors · LLM Critic         │
└───────────────────────────┬───────────────────────────────────────┘
                             │
┌───────────────────────────┴───────────────────────────────────────┐
│                        Topologies                           │
│              Pipeline · Supervisor · Diamond                │
└───────────────────────────┬───────────────────────────────────────┘
                             │
┌───────────────────────────┴───────────────────────────────────────┐
│                      Core Runtime                           │
│              State · Node · Edge · Graph                    │
└───────────────────────────┬───────────────────────────────────────┘
                             │
┌───────────────────────────┴───────────────────────────────────────┐
│                    Failure Injectors                        │
│  Tool · Partial · State Corruption · Goal Drift · Limits    │
└───────────────────────────────────────────────────────────────┘
```

The injectors sit *between* the runtime and the actual tools / state mutations.  
This is deliberate: failure is a first-class, controllable concern rather than an accidental side effect.

## Core Concepts

### State
Typed, versioned, serializable working memory for a single run.  
All topologies share the same state schema so comparisons remain fair.

### Node
Unit of work. Receives state, optionally calls tools, returns updated state (or a decision).

### Edge
Conditional transition. Pure function of state (or verifier result).

### Graph
Collection of nodes + edges + entry/exit points + policy.

### Topology
A concrete graph construction pattern (Pipeline, Supervisor, Diamond).  
Topologies are thin. The interesting behavior comes from how they interact with injectors and verifiers.

### Injector
A pure-ish component that can:
- Intercept tool calls
- Mutate or replace tool results
- Corrupt or rewrite state
- Alter the goal
- Enforce hard limits

Each injector has controllable **intensity** (probability + severity).

### Verifier
Runs after nodes (or at defined checkpoints).  
Can accept, reject, or request repair.  
Must be swappable without changing topology code.

## Evaluation Philosophy

- **Fixed task set** once locked.
- **Hybrid metrics**: rule-based ground truth + limited structured LLM judgment.
- Never rely solely on LLM-as-judge for recovery success.
- Every experiment records:
  - Which failures were injected and when
  - Final state correctness
  - Extra tokens / steps caused by recovery
  - Whether the original goal was preserved

## Design Non-Negotiables

1. Injectors must be independent of any particular topology.
2. Topologies must be runnable with zero verifiers (baseline).
3. Adding a new verifier must not require changes to topology implementations.
4. The evaluation harness must be able to run the full combinatorial matrix.
5. Everything that affects results must be configurable and logged.

## Future Extensions (Post-MVP)

Only after the core matrix produces clear signal:

- Additional topologies (hybrid, swarm-style, etc.)
- Dynamic graph rewriting under failure
- Memory-as-graph-nodes experiments
- Public submission of recovery strategies (much later)
