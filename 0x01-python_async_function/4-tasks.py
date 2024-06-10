#!/usr/bin/env python3
"""execute multiple coroutines at the same time with async"""


import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """execute multiple coroutines"""
    all_delays = []
    result = []

    for i in range(n):
        all_delays.append(task_wait_random(max_delay))

    for task in asyncio.as_completed(all_delays):
        result.append(await task)

    return result
