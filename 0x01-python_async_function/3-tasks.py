#!/usr/bin/env python3
""" task 4 module
"""
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int):
    """
    Args:
        max_delay: max second
    Returns:
        asyncio.Task
    """
    return asyncio.create_task(wait_random(max_delay))
