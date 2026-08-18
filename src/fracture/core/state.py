# src/fracture/core/state.py
import operator
from typing import List, Dict, Any, Optional, Annotated
from pydantic import BaseModel, Field

class ToolCall(BaseModel):
    id: str
    name: str
    arguments: Dict[str, Any]
    result: Optional[str] = None
    error: Optional[str] = None
    duration_ms: float = 0.0
    cost: float = 0.0

class AgentState(BaseModel):
    original_goal: str
    current_goal: str
    
    # Overwrite entirely (allows Amnesia injectors to delete items)
    memory: List[Dict[str, str]] = Field(default_factory=list) 
    
    # Reducers: LangGraph will safely concatenate/add these from parallel workers
    tool_history: Annotated[List[ToolCall], operator.add] = Field(default_factory=list)
    iteration_count: Annotated[int, operator.add] = 0
    total_cost: Annotated[float, operator.add] = 0.0
    status: str = "running"