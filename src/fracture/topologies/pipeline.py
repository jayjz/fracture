# src/fracture/topologies/pipeline.py
from langgraph.graph import StateGraph, START, END
from fracture.core.state import AgentState
from fracture.injectors.dispatcher import InjectorDispatcher

class PipelineTopology:
    """A rigid, sequential graph: Step 1 -> Step 2 -> Step 3"""
    
    def __init__(self, dispatcher: InjectorDispatcher, tools: dict):
        self.dispatcher = dispatcher
        self.tools = tools

    def step_1(self, state: AgentState) -> AgentState:
        # Example: Call the first tool in the sequence
        return self.dispatcher.execute(state, "tool_1", self.tools.get("tool_1"))

    def step_2(self, state: AgentState) -> AgentState:
        # Blindly calls the next tool, assuming step_1 succeeded
        return self.dispatcher.execute(state, "tool_2", self.tools.get("tool_2"))

    def build(self):
        builder = StateGraph(AgentState)
        
        builder.add_node("step_1", self.step_1)
        builder.add_node("step_2", self.step_2)
        
        builder.add_edge(START, "step_1")
        builder.add_edge("step_1", "step_2")
        builder.add_edge("step_2", END)
        
        return builder.compile()