"""Graph container."""

from __future__ import annotations

from .edge import Edge
from .node import Node


class Graph:
    """Collection of nodes and edges that form a topology instance."""

    def __init__(self, name: str) -> None:
        self.name = name
        self.nodes: dict[str, Node] = {}
        self.edges: list[Edge] = []
        self.entry: str | None = None
        self.exit: str | None = None

    def add_node(self, node: Node) -> None:
        self.nodes[node.name] = node

    def add_edge(self, edge: Edge) -> None:
        self.edges.append(edge)

    def set_entry(self, node_name: str) -> None:
        self.entry = node_name

    def set_exit(self, node_name: str) -> None:
        self.exit = node_name
