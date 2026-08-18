# src/fracture/topologies/diamond.py
from langgraph.graph import StateGraph, START, END
from fracture.core.state import AgentState
from fracture.injectors.dispatcher import InjectorDispatcher

class DiamondTopology:
    def __init__(self, dispatcher: InjectorDispatcher, tools: dict):
        self.dispatcher = dispatcher
        self.tools = tools

    def planner_node(self, state: AgentState) -> dict:
        return {}

    def worker_a(self, state: AgentState) -> dict:
        # Returns a dict e.g., {"tool_history": [...], "total_cost": 0.05}
        return self.dispatcher.execute(state, "tool_a", self.tools.get("tool_a"))

    def worker_b(self, state: AgentState) -> dict:
        return self.dispatcher.execute(state, "tool_b", self.tools.get("tool_b"))

    def synthesis_node(self, state: AgentState) -> dict:
        return {}

    def build(self):
        builder = StateGraph(AgentState)
        
        builder.add_node("planner", self.planner_node)
        builder.add_node("worker_a", self.worker_a)
        builder.add_node("worker_b", self.worker_b)
        builder.add_node("synthesis", self.synthesis_node)
        
        builder.add_edge(START, "planner")
        builder.add_edge("planner", "worker_a")
        builder.add_edge("planner", "worker_b")
        builder.add_edge("worker_a", "synthesis")
        builder.add_edge("worker_b", "synthesis")
        builder.add_edge("synthesis", END)
        
        return builder.compile()