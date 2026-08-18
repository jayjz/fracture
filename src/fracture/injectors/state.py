"""State corruption injector."""

from __future__ import annotations

from typing import Any

from fracture.core.state import State
from .base import BaseInjector


class StateCorruptionInjector(BaseInjector):
    """Mid-execution mutation or deletion of state fields."""

    name = "state_corruption"

    async def maybe_inject(self, state: State, context: dict[str, Any]) -> State:
        # TODO: implement controlled state corruption
        return state
