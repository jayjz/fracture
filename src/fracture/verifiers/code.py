"""Code-level reality anchors."""

from __future__ import annotations

from typing import Any

from fracture.core.state import State
from .base import BaseVerifier


class CodeAnchorVerifier(BaseVerifier):
    """
    Pure Python / rule-based checks that do not rely on an LLM.
    Highest signal for determinism experiments.
    """

    name = "code_anchor"

    async def verify(self, state: State, context: dict[str, Any]) -> tuple[bool, State]:
        # TODO: implement domain-specific reality anchors
        return True, state
