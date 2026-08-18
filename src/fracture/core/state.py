"""Typed working state for a single Fracture run."""

from __future__ import annotations

from typing import Any

from pydantic import BaseModel, Field


class State(BaseModel):
    """
    Minimal shared state schema.

    All topologies must operate on the same state shape so experiments remain comparable.
    Extend carefully — changes here affect every experiment.
    """

    goal: str = Field(..., description="The original objective for this run")
    messages: list[dict[str, Any]] = Field(default_factory=list)
    data: dict[str, Any] = Field(default_factory=dict)
    metadata: dict[str, Any] = Field(default_factory=dict)
    step: int = 0
    status: str = "running"  # running | completed | failed | timed_out | budget_exceeded

    # TODO: add versioning and stricter schemas once task set is locked
