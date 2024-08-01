#!/usr/bin/env python3
"""some module"""
from typing import Iterable, List, Tuple, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Args:
    Returns:
    """
    return [(i, len(i)) for i in lst]
