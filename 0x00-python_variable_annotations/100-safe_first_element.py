#!/usr/bin/env python3
"""This module contains a function safe_first_element."""
from typing import Sequence, Any, Union


# The types of the elements of the input are not know
def safe_first_element(lst: Sequence[Any]) -> Union[Any, type(None)]:
    """Duck typed annotations for this function."""
    if lst:
        return lst[0]
    else:
        return None
