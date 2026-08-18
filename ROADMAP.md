# Fracture Roadmap

**Goal:** A focused, high-signal failure injection harness for graph agents that produces reproducible evidence about which topologies + verifier strategies recover under realistic failure conditions.

This is a solo-dev research artifact, not a general-purpose framework. Scope is deliberately constrained.

---

## Guiding Constraints

- Solo developer
- Part-time capacity (~15–20 hrs/week)
- Prefer depth over breadth
- Evaluation quality > visual polish
- Fixed task set once locked (no moving goalposts)

---

## Phase 0 — Scaffold & Contracts (Complete)

- [x] Repository created
- [x] Project structure + packaging
- [x] Core markdown (README, ROADMAP, ARCHITECTURE)
- [x] Empty modules with clear interfaces

**Exit criteria:** Anyone can clone and understand the intended architecture and evaluation philosophy.

---

## Phase 1 — Core Primitives (Week 1–2)

**Focus:** Typed state + failure injection layer that sits *between* the runtime and tools/state.

### Deliverables
- [ ] `State` schema (Pydantic or equivalent) with versioning
- [ ] `Node` / `Edge` / `Graph` minimal interfaces
- [ ] Base `Injector` ABC + intensity control (probability + severity)
- [ ] Five concrete injectors:
  - ToolFailureInjector
  - PartialResultInjector
  - StateCorruptionInjector
  - GoalDriftInjector
  - TimeoutCostInjector
- [ ] Structured logging of every injection event
- [ ] 4–5 seed tasks that require multi-step tool use

**Exit criteria:**  
You can run a single agent, inject any of the five failures at configurable rates, and get clean traces + logs. No topology logic yet.

**Risk:** Over-engineering the state schema. Keep it minimal but typed.

---

## Phase 2 — Topologies (Week 3)

**Focus:** Three comparable control structures on top of the same runtime and state schema.

### Deliverables
- [ ] `PipelineTopology`
- [ ] `SupervisorTopology`
- [ ] `DiamondTopology`
- [ ] Shared tool interface + cost/latency tracking
- [ ] Hard timeout + cost limit enforcement

**Exit criteria:**  
Same task + same failure profile can be executed across all three topologies with comparable logs and metrics.

**Risk:** Making topologies “clever” instead of clean and different. Keep implementations honest and minimal.

---

## Phase 3 — Evaluation Harness (Week 4)

**Focus:** Measurement that is actually useful.

### Deliverables
- [ ] Recovery success criteria (binary + graded)
- [ ] Hybrid scoring:
  - Rule-based checks (final state correctness, tool sequence after failure, etc.)
  - Limited structured LLM judge for qualitative recovery quality
- [ ] Automatic aggregation (success rate, extra tokens, recovery steps, failure mode distribution)
- [ ] Batch runner (`N` trials × topology × verifier × failure intensity)
- [ ] Seed control + reproducibility notes

**Exit criteria:**  
One command produces a results table from a fixed set of tasks.

**Critical decision:** Lock the task set here. Do not expand it later without versioning the leaderboard.

---

## Phase 4 — Verifier Strategies (Week 5)

**Focus:** Make verification first-class and swappable.

### Deliverables
- [ ] `NoVerifier` (baseline)
- [ ] `SchemaVerifier` (type + structure checks)
- [ ] `CodeAnchorVerifier` (pure Python / rule-based reality checks)
- [ ] `LLMCriticVerifier` (structured output + retry policy)
- [ ] Clean swap interface so topology code does not change

**Exit criteria:**  
Any topology can be run with any verifier combination without code changes.

---

## Phase 5 — Results & Public Surface (Week 6–7)

**Focus:** Ship evidence, not just code.

### Deliverables
- [ ] Full matrix run on locked task set
- [ ] Analysis write-up: which combinations recover from which failures
- [ ] Clean README with results tables
- [ ] Static leaderboard (markdown + optional simple HTML)
- [ ] Exact reproduction instructions
- [ ] Failure taxonomy documentation

**Exit criteria:**  
A stranger can read the README, understand the failure model, see the numbers, and reproduce the runs.

---

## Phase 6 — Hardening & Polish (Week 8)

- [ ] Config-driven intensity and experiment definitions
- [ ] Additional 1–2 tasks only if the current set is too narrow
- [ ] Light interactive demo (Streamlit or CLI) — optional
- [ ] Documentation pass
- [ ] Basic CI (lint + unit tests for injectors)

---

## Explicit Non-Goals (First 8 Weeks)

- Dynamic graph construction
- Arbitrary third-party tool ecosystems
- Multi-user submission system for the leaderboard
- Fancy real-time graph visualizer
- Supporting every Anthropic workflow pattern
- “Production-grade” claims beyond the research harness

---

## Success Definition

A public repository where:

1. The failure taxonomy is precise and documented.
2. Numbers exist showing differential recovery across topology + verifier combinations.
3. Experiments are reproducible.
4. It is obviously *not* another happy-path LangGraph demo.

That is rare. That is the point.

---

## Tracking

Update this file as phases complete.  
Keep a short `CHANGELOG.md` for user-visible changes.
