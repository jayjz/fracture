"""Pipeline topology."""

from __future__ import annotations

from fracture.core.graph import Graph
from .base import BaseTopology


class PipelineTopology(BaseTopology):
    """Linear sequence of nodes. Simple, predictable, limited recovery options."""

    name = "pipeline"

    def build(self) -> Graph:
        # TODO: implement clean pipeline construction
        raise NotImplementedError
