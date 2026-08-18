"""Structured LLM critic verifier."""

from __future__ import annotations

from typing import Any

from fracture.core.state import State
from .base import BaseVerifier


class LLMCriticVerifier(BaseVerifier):
    """
    LLM-based critic with structured output and optional retry policy.
    Use sparingly and always in combination with rule-based checks.
    """

    name = "llm_critic"

    async def verify(self, state: State, context: dict[str, Any]) -> tuple[bool, State]:
        # TODO: implement structured critic + repair loop
        return True, state
