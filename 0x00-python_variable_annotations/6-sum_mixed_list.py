#!/usr/bin/env python3
"""some module"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Args:
        mxd_lst: a list of numbers
    Returns:
        the sum of the numbers as: float
    """
    sum: float = 0.0
    for i in mxd_lst:
        sum += i
    return sum
