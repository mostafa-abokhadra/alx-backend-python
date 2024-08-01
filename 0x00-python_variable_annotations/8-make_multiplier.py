#!/usr/bin/env python3
"""some module"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Args:
    Returns:
    """
    return lambda x: x * multiplier
