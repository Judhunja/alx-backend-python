#!/usr/bin/env python3
"""This module contains a coroutine async_generator."""
import random
import asyncio
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """Yield random numbers between 0 and 10 in a loop."""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
