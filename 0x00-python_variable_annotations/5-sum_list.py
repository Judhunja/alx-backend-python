#!/usr/bin/env python3
"""This module contains a function sum_list."""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """Return sum of all floats in input list."""
    sum: float = 0.0
    for i in input_list:
        sum += i
    return sum
