"""Timeout and cost limit injectors / enforcers."""

from __future__ import annotations

from typing import Any

from fracture.core.state import State
from .base import BaseInjector


class TimeoutCostInjector(BaseInjector):
    """Hard wall-clock and token/cost budget enforcement."""

    name = "timeout_cost"

    def __init__(
        self,
        intensity: float = 0.3,
        max_seconds: float | None = None,
        max_tokens: int | None = None,
    ) -> None:
        super().__init__(intensity=intensity)
        self.max_seconds = max_seconds
        self.max_tokens = max_tokens

    async def maybe_inject(self, state: State, context: dict[str, Any]) -> State:
        # TODO: implement hard limits and early termination
        return state
