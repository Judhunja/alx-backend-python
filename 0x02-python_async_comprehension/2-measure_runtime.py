#!/usr/bin/env python3
"""This module contains a coroutine measure_runtime."""
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Measure runtime for running four async operations in parallel."""
    s = time.perf_counter()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    elapsed = time.perf_counter() - s
    return elapsed
