"""Base topology interface."""

from __future__ import annotations

from abc import ABC, abstractmethod

from fracture.core.graph import Graph


class BaseTopology(ABC):
    """Constructs a concrete Graph for a given pattern."""

    name: str

    @abstractmethod
    def build(self) -> Graph:
        """Return a fully configured Graph instance."""
        ...
