"""Node abstraction."""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any

from .state import State


class Node(ABC):
    """Unit of work in a Fracture graph."""

    name: str

    def __init__(self, name: str) -> None:
        self.name = name

    @abstractmethod
    async def run(self, state: State, **kwargs: Any) -> State:
        """Execute the node and return updated state."""
        ...
