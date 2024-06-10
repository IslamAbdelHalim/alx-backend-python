#!/usr/bin/env python3
"""The basic async"""


import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """This is a coroutine function"""
    delay = random.random() * max_delay
    await asyncio.sleep(delay)
    return delay
