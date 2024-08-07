#!/usr/bin/env python3
""" task 5 module
"""
import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Args:
        n: numebr of tasks
        max_delay: maxSeconds
    Return:
        seconds of tasks: List
    """
    listy = []
    for i in range(n):
        task = task_wait_random(max_delay)
        sec = await task
        listy.append(sec)
    return sorted(listy)
