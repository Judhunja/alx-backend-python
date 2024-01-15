#!/usr/bin/env python3
"""This module contains a function task_wait_n."""
import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Calls task_wait_random instead of wait_random."""
    delay_list = []
    tasks = [task_wait_random(max_delay) for _ in range(n)]

    for task in asyncio.as_completed(tasks):
        result = await task
        delay_list.append(result)
    return delay_list
