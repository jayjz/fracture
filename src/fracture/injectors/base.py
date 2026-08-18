"""Base class for all failure injectors."""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any

from fracture.core.state import State


class BaseInjector(ABC):
    """
    First-class failure injection component.

    Intensity controls both probability and severity of the injected failure.
    """

    name: str

    def __init__(self, intensity: float = 0.3) -> None:
        if not 0.0 <= intensity <= 1.0:
            raise ValueError("intensity must be between 0.0 and 1.0")
        self.intensity = intensity

    @abstractmethod
    async def maybe_inject(self, state: State, context: dict[str, Any]) -> State:
        """
        Possibly mutate state or context according to the failure model.

        Must be side-effect free except for the returned state / logged events.
        """
        ...
