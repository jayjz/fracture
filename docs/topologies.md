# Topologies Under Test

## Pipeline
Linear sequence of nodes.  
Minimal recovery options. Useful as a baseline for how fragile pure sequential control is under injection.

## Supervisor
Central controller that can route, replan, and re-assign work.  
Expected to show stronger recovery under goal drift and tool failure when paired with good verifiers.

## Diamond
Fan-out to parallel workers followed by a join/aggregation node.  
Particularly useful for testing partial result failures and state corruption under concurrent paths.

---

All three share the same state schema and tool interface so differences in recovery can be attributed to control structure + verification rather than implementation details.
