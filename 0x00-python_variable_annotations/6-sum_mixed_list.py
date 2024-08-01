#!/usr/bin/env python3
"""some module"""
from typing import List


def sum_mixed_list(mxd_lst: List[int | float]) -> float:
    sum: float = 0.0
    """
    Args:
        mxd_lst: a list of numbers
    Returns:
        the sum of the numbers as: float
    """
    for i in mxd_lst:
        sum += i
    return sum
