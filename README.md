# Fracture

**Chaos engineering for graph agents.**

Deliberately break agent graphs with tool failures, partial results, state corruption, goal drift, and hard limits — then measure which topologies and verifier strategies actually recover.

> Most agent demos live on the happy path.  
> Fracture forces the failure modes that matter.

## Why This Exists

Single-agent loops go goal-blind.  
Static graphs without verifiers and reality anchors still fail silently.  

The interesting question is no longer “can I wire a graph?”  
It is: **under controlled, realistic failure injection, which control structures and verification strategies recover — and which ones just look good in a diagram?**

Fracture is a focused research harness for that question.

## Core Capabilities (Target)

| Failure Type              | Description                                      |
|---------------------------|--------------------------------------------------|
| Tool Failure              | Complete tool call failures / exceptions         |
| Partial / Incorrect Results | Tools return incomplete or subtly wrong data   |
| State Corruption          | Mid-execution mutation or deletion of state      |
| Goal Drift                | Subtle rewriting of the original objective       |
| Timeout & Cost Limits     | Hard wall-clock and token/cost budgets           |

**Topologies under test:** Pipeline · Supervisor · Diamond  

**Verifier strategies:** None · Schema/Type · Code-level Reality Anchors · Structured LLM Critic

## Project Status

**Scaffold + Roadmap** — Implementation begins now.

See [ROADMAP.md](ROADMAP.md) for the full phased plan.

## Design Principles

1. **Failure models first** — The injectors are first-class, not an afterthought.
2. **Comparable experiments** — Same tasks, same state schema, same metrics across topologies.
3. **Hybrid evaluation** — Rule-based ground truth + limited LLM judgment. Never pure LLM-as-judge.
4. **Reproducibility** — Fixed task set, controllable intensity, deterministic seeds where possible.
5. **No scope creep** — Three topologies. Five failure classes. A locked evaluation set.

## Quick Start (once implemented)

```bash
# Install
pip install -e .

# Run a single injection experiment
python -m fracture.examples.basic_injection

# Run the full matrix
python scripts/run_benchmark.py --trials 20
```

## Repository Structure

```
src/fracture/
├── core/           # State, Node, Edge, Graph, Runtime
├── injectors/      # The five failure injectors
├── topologies/     # Pipeline, Supervisor, Diamond
├── verifiers/      # Schema, Code anchors, LLM critic
├── evaluation/     # Metrics, harness, tasks, leaderboard
└── utils/
```

## License

MIT

---

**Break the graph. Measure the recovery.**
