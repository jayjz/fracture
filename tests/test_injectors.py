"""Tests for failure injectors."""

import pytest

from fracture.injectors.base import BaseInjector


def test_intensity_bounds() -> None:
    with pytest.raises(ValueError):
        BaseInjector(intensity=1.5)  # type: ignore[abstract]
