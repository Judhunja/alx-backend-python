#!/usr/bin/env python3
"""This module contains an asynchronous coroutine wait_random."""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Take in max_delay and waits for a random delay between 0
    and max_delay and eventually returns it.
    """
    float_delay = float(max_delay)
    delay = random.uniform(0, float_delay)
    await asyncio.sleep(delay)
    return delay
