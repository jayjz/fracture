"""Diamond topology."""

from __future__ import annotations

from fracture.core.graph import Graph
from .base import BaseTopology


class DiamondTopology(BaseTopology):
    """
    Parallel fan-out followed by a join/aggregation node.
    Useful for testing partial failure and consensus under corruption.
    """

    name = "diamond"

    def build(self) -> Graph:
        # TODO: implement diamond (fan-out / fan-in)
        raise NotImplementedError
