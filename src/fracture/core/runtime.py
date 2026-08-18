"""Minimal runtime that executes a graph with optional injectors and verifiers."""

from __future__ import annotations

from typing import Any

from .graph import Graph
from .state import State


class Runtime:
    """
    Executes a graph.

    Injectors and verifiers are attached here so topologies stay clean.
    """

    def __init__(
        self,
        graph: Graph,
        injectors: list[Any] | None = None,
        verifiers: list[Any] | None = None,
    ) -> None:
        self.graph = graph
        self.injectors = injectors or []
        self.verifiers = verifiers or []

    async def run(self, initial_state: State) -> State:
        """
        Execute the graph starting from entry node.

        TODO: implement proper traversal, injection points, verifier checkpoints,
        timeout/cost tracking, and structured logging.
        """
        raise NotImplementedError("Runtime execution will be implemented in Phase 1–2")
