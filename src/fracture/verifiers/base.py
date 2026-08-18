"""Base verifier interface."""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any

from fracture.core.state import State


class BaseVerifier(ABC):
    """
    Post-node or checkpoint verification.

    Can accept, reject, or request repair. Must be swappable.
    """

    name: str

    @abstractmethod
    async def verify(self, state: State, context: dict[str, Any]) -> tuple[bool, State]:
        """
        Returns (accepted, possibly_repaired_state).
        """
        ...
