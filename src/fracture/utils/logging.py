"""Structured logging helpers for experiments."""

from __future__ import annotations

import structlog


def get_logger(name: str = "fracture"):
    """Return a configured structlog logger."""
    return structlog.get_logger(name)
