#!/usr/bin/env python3
"""This module contains a function to_kv."""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Return k(string) and the square of v(int or float) as float."""
    square: float = v ** 2
    return (k, square)
