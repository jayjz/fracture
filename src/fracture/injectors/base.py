# src/fracture/injectors/base.py
import random
from abc import ABC, abstractmethod
from copy import deepcopy
from fracture.core.state import AgentState, ToolCall

class BaseInjector(ABC):
    def __init__(self, probability: float = 0.3, severity: float = 0.5):
        """
        probability: 0.0 to 1.0 chance the injection triggers on a given turn.
        severity: 0.0 to 1.0 multiplier for how destructive the injection is.
        """
        self.probability = probability
        self.severity = severity

    def should_trigger(self) -> bool:
        return random.random() < self.probability

    @abstractmethod
    def inject(self, state: AgentState, pending_call: Optional[ToolCall] = None) -> AgentState:
        """Returns a mutated copy of the state/call."""
        pass