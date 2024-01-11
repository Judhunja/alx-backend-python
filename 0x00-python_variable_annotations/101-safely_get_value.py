#!/usr/bin/env python3
"""This module contains a function safely_get_value."""
from typing import Mapping, Any, TypeVar, Union


T = TypeVar('T')  # generic type variable


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[T, type(None)] = None) -> Union[Any, T]:
    """Use TypeVar to create a variable that can represent any type."""
    if key in dct:
        return dct[key]
    else:
        return default
