#!/usr/bin/env python3
"""some another module"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Args:
        input_list: list of float nums
    Returns:
        the sum of list as: float
    """
    sum: float = 0.0
    for i in input_list:
        sum += i
    return sum
