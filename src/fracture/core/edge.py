"""Edge / transition logic."""

from __future__ import annotations

from typing import Callable

from .state import State

# Simple condition type for now
EdgeCondition = Callable[[State], bool]


class Edge:
    """Conditional transition between nodes."""

    def __init__(
        self,
        source: str,
        target: str,
        condition: EdgeCondition | None = None,
        name: str | None = None,
    ) -> None:
        self.source = source
        self.target = target
        self.condition = condition or (lambda s: True)
        self.name = name or f"{source}->{target}"

    def should_traverse(self, state: State) -> bool:
        return self.condition(state)
