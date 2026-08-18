# Failure Taxonomy

Precise definitions of the five failure classes Fracture injects.

## 1. Tool Failure
Complete failure of a tool call (exception, timeout, or explicit error return).  
The agent must detect the failure and decide whether to retry, replan, or abort.

## 2. Partial / Incorrect Results
Tool returns data that is incomplete, outdated, or subtly wrong.  
Harder than total failure because the agent may continue with corrupted intermediate state.

## 3. State Corruption
Direct mutation or deletion of fields in the working state mid-execution.  
Tests whether the topology + verifiers can detect inconsistency and recover.

## 4. Goal Drift
Subtle rewriting of the original objective.  
Tests whether the system can notice that it is no longer optimizing for the original goal.

## 5. Timeout & Cost Limits
Hard wall-clock and token/cost budgets.  
Forces early termination and tests graceful degradation under resource pressure.

---

Each injector exposes an **intensity** parameter (0.0–1.0) that controls both probability and severity.
