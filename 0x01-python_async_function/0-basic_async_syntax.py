#!/usr/bin/env python3
""" basic syntax of async await
"""
import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """
    Args:
        max_delay: max delay
    Returns:
        random num
    """
    seconds: float = random.uniform(0, max_delay)
    await asyncio.sleep(seconds)
    return seconds
