"""Tool failure and partial/incorrect result injectors."""

from __future__ import annotations

from typing import Any

from fracture.core.state import State
from .base import BaseInjector


class ToolFailureInjector(BaseInjector):
    """Simulate complete tool call failures / exceptions."""

    name = "tool_failure"

    async def maybe_inject(self, state: State, context: dict[str, Any]) -> State:
        # TODO: implement probabilistic tool failure
        return state


class PartialResultInjector(BaseInjector):
    """Simulate tools returning incomplete or subtly incorrect data."""

    name = "partial_result"

    async def maybe_inject(self, state: State, context: dict[str, Any]) -> State:
        # TODO: implement partial / incorrect tool results
        return state
