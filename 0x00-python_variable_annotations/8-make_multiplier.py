#!/usr/bin/env python3
"""some module"""
from typing import Callable


def call(multi: float) -> float:
    return multi * multi


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Args:
    Returns:
    """
    return call
