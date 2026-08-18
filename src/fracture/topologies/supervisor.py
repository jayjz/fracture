"""Supervisor topology."""

from __future__ import annotations

from fracture.core.graph import Graph
from .base import BaseTopology


class SupervisorTopology(BaseTopology):
    """Central supervisor that routes work to workers and can replan."""

    name = "supervisor"

    def build(self) -> Graph:
        # TODO: implement supervisor + worker pattern
        raise NotImplementedError
