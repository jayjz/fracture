"""Batch evaluation harness."""

from __future__ import annotations


class EvaluationHarness:
    """
    Runs the combinatorial matrix of topology × verifier × failure intensity
    over a fixed task set and aggregates results.
    """

    def __init__(self) -> None:
        # TODO: accept task registry, topology registry, verifier registry
        pass

    async def run_matrix(self, trials: int = 10) -> None:
        """Execute the full experimental matrix."""
        raise NotImplementedError("Will be implemented in Phase 3")
