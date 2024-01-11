#!/usr/bin/env python3
"""This module contains a function make_multiplier."""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Return a function that mutiplies a float by multiplier."""
    def multiplier_func(n: float) -> float:
        """Return a float multiplied by multiplier."""
        return n * multiplier
    return multiplier_func
