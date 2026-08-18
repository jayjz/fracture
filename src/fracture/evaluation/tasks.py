"""Fixed evaluation task set.

Once locked, this set should not change without versioning the leaderboard.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Task:
    id: str
    description: str
    # TODO: expected final state predicates, tool requirements, difficulty tags


# Seed tasks will be defined here in Phase 1.
TASKS: list[Task] = []
