# scripts/test_physics.py
from fracture.core.state import AgentState
from fracture.injectors.failures import PartialResultInjector, GoalDriftInjector
from fracture.injectors.dispatcher import InjectorDispatcher

# 1. Setup State
state = AgentState(original_goal="Find the root cause of the server spike.", current_goal="Find the root cause of the server spike.")

# 2. Configure Chaos (High probability for testing)
dispatcher = InjectorDispatcher(injectors=[
    GoalDriftInjector(probability=1.0, severity=1.0),
    PartialResultInjector(probability=1.0, severity=0.8) # 80% truncation
])

# 3. Define a Mock Tool
def mock_query_logs(timeframe: str):
    return f"Logs for {timeframe}: [Error at /api/v2/auth], [Timeout at /api/v1/users], [Error at /api/v2/auth]"

# 4. Execute
new_state = dispatcher.execute(state, "query_logs", mock_query_logs, timeframe="24h")

print("Mutated Goal:", new_state.current_goal)
print("Tool Result:", new_state.tool_history[0].result)