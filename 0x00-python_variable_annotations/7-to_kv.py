#!/usr/bin/env python3
"""some module"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Args:
        k: a string
        v: a number
    Returns:
        a tuple
    """
    return (k, v ** 2)
