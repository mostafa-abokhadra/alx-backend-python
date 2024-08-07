#!/usr/bin/env python3
"""second task module
"""
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Args:
        n: numebr of tasks
        max_delay: maxSeconds
    Return:
        seconds of tasks: List
    """
    listy = []
    for i in range(n):
        task = asyncio.create_task(wait_random(max_delay))
        sec = await task
        listy.append(sec)
    return sorted(listy)
