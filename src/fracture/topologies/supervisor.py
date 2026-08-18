# src/fracture/topologies/supervisor.py
from langgraph.graph import StateGraph, START, END
from fracture.core.state import AgentState
from fracture.injectors.dispatcher import InjectorDispatcher

class SupervisorTopology:
    """Hub-and-spoke graph: Supervisor routes to tools and evaluates results."""
    
    def __init__(self, dispatcher: InjectorDispatcher, tools: dict):
        self.dispatcher = dispatcher
        self.tools = tools

    def supervisor_node(self, state: AgentState) -> AgentState:
        # In a real run, an LLM or verifier sits here to decide the next step.
        # For the scaffold, we just update iteration count.
        new_state = state.model_copy(deep=True)
        new_state.iteration_count += 1
        return new_state

    def tool_node(self, state: AgentState) -> AgentState:
        # Executes the currently required tool based on supervisor logic
        # (Mocked to execute 'tool_1' for the scaffold)
        return self.dispatcher.execute(state, "tool_1", self.tools.get("tool_1"))

    def routing_logic(self, state: AgentState) -> str:
        # If goal drift or cost limits hit, the supervisor might exit early
        if state.iteration_count > 3 or state.total_cost > 1.0:
            return END
        
        # Check if the last tool call had an error (injected failure)
        if state.tool_history and state.tool_history[-1].error:
            return "tool_node" # Retry
            
        return "tool_node"

    def build(self):
        builder = StateGraph(AgentState)
        
        builder.add_node("supervisor", self.supervisor_node)
        builder.add_node("tool_node", self.tool_node)
        
        builder.add_edge(START, "supervisor")
        builder.add_conditional_edges("supervisor", self.routing_logic)
        builder.add_edge("tool_node", "supervisor") # Always loop back to supervisor
        
        return builder.compile()