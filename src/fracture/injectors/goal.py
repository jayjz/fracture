"""Goal drift injector."""

from __future__ import annotations

from typing import Any

from fracture.core.state import State
from .base import BaseInjector


class GoalDriftInjector(BaseInjector):
    """Subtle rewriting of the original objective during execution."""

    name = "goal_drift"

    async def maybe_inject(self, state: State, context: dict[str, Any]) -> State:
        # TODO: implement goal drift (subtle rewrites of state.goal)
        return state
