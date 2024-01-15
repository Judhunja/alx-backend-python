#!/usr/bin/env python3
"""This module contains an async routine wait_n."""
import asyncio
from typing import List

wait_random = __import__("0-basic_async_syntax").wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Spawns wait_random n times with the specified max_delay."""
    delay_list = []
    tasks = [asyncio.gather(wait_random(max_delay)) for _ in range(n)]

    for task in asyncio.as_completed(tasks):
        result = await task
        delay_list.append(result)
    return delay_list
