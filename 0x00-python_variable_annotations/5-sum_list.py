#!/usr/bin/env python3
"""some another module"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    sum: float = 0.0
    for i in input_list:
        sum += i
    return sum
