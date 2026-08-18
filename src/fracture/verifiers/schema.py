"""Schema / type verifier."""

from __future__ import annotations

from typing import Any

from fracture.core.state import State
from .base import BaseVerifier


class SchemaVerifier(BaseVerifier):
    """Basic structural and type checks on state."""

    name = "schema"

    async def verify(self, state: State, context: dict[str, Any]) -> tuple[bool, State]:
        # TODO: implement schema validation
        return True, state
