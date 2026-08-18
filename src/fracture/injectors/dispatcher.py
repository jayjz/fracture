# src/fracture/injectors/dispatcher.py
import time
import uuid
from typing import Callable, List, Any, Dict
from fracture.core.state import AgentState, ToolCall
from fracture.injectors.base import BaseInjector
from fracture.injectors.failures import (
    StateCorruptionInjector,
    GoalDriftInjector,
    ToolFailureInjector,
    PartialResultInjector,
    TimeoutCostInjector
)

class InjectorDispatcher:
    def __init__(self, injectors: List[BaseInjector]):
        self.injectors = injectors

    def execute(self, state: AgentState, tool_name: str, tool_func: Callable, **kwargs) -> dict:
        """Executes the tool, applies failures, and returns a LangGraph-compatible state diff."""
        new_state = state.model_copy(deep=True)
        
        # 1. Pre-Execution (Cognitive Failures)
        for injector in self.injectors:
            if isinstance(injector, (StateCorruptionInjector, GoalDriftInjector)):
                new_state = injector.inject(new_state)

        pending_call = ToolCall(id=uuid.uuid4().hex[:8], name=tool_name, arguments=kwargs)

        # 2. Hard Failure (Circuit Breaker)
        hard_failed = False
        for injector in self.injectors:
            if isinstance(injector, ToolFailureInjector):
                new_state = injector.inject(new_state, pending_call)
                if pending_call.error is not None:
                    hard_failed = True
                    break

        # 3. Normal Execution & 4. Post-Execution Mutations
        if not hard_failed:
            start_time = time.time()
            try:
                result = tool_func(**kwargs)
                pending_call.result = str(result)
            except Exception as e:
                pending_call.error = str(e)
            
            pending_call.duration_ms = (time.time() - start_time) * 1000.0
            pending_call.cost = 0.05
            
            for injector in self.injectors:
                if isinstance(injector, (PartialResultInjector, TimeoutCostInjector)):
                    new_state = injector.inject(new_state, pending_call)

            if pending_call not in new_state.tool_history:
                new_state.tool_history.append(pending_call)

        new_state.iteration_count += 1

        # --- THE MAGIC: COMPUTE THE STATE DIFF FOR LANGGRAPH ---
        diff = {}
        
        # Only grab the NEW tool calls to append
        new_calls = new_state.tool_history[len(state.tool_history):]
        if new_calls:
            diff["tool_history"] = new_calls
            
        # Add the cost delta
        cost_delta = new_state.total_cost - state.total_cost
        if cost_delta > 0:
            diff["total_cost"] = cost_delta
            
        diff["iteration_count"] = new_state.iteration_count - state.iteration_count
        
        if new_state.current_goal != state.current_goal:
            diff["current_goal"] = new_state.current_goal
            
        if new_state.memory != state.memory:
            diff["memory"] = new_state.memory
            
        return diff