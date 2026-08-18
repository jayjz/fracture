"""Recovery metrics and scoring."""

from __future__ import annotations

from pydantic import BaseModel, Field


class RunMetrics(BaseModel):
    """Metrics collected from a single experimental run."""

    topology: str
    verifier: str
    failure_profile: str
    success: bool
    recovered: bool
    steps: int = 0
    extra_tokens: int = 0
    wall_time_s: float = 0.0
    failure_events: list[str] = Field(default_factory=list)
    notes: str = ""


# TODO: aggregation helpers, graded recovery scores, hybrid judge interface
