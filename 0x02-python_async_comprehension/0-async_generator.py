#!/usr/bin/env python3
"""Async Generator """


import asyncio
from typing import AsyncGenerator
import random


async def async_generator() -> AsyncGenerator[float, None]:
    for i in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10
