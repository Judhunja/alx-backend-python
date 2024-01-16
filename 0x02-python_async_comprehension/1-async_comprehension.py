#!/usr/bin/env python3
"""This module contains a coroutine async_comprehension."""
from typing import AsyncGenerator, List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> AsyncGenerator[List[float], None]:
    """Collect 10 random numbers using an async comprehension."""
    return [i async for i in (async_generator())]
