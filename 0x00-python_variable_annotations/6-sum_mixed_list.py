#!/usr/bin/env python3
"""This module contains a function sum_mixed_list."""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Return sum in float of a list with mixed ints and floats."""
    sum: float = 0.0
    for i in mxd_lst:
        sum += i
    return sum
