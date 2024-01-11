#!/usr/bin/env python3
"""This module contains a function element_length."""
from typing import List, Iterable, Tuple, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Return a list of tuples with iterables and their length."""
    return [(i, len(i)) for i in lst]
