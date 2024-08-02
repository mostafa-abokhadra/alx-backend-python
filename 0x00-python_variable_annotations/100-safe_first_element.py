#!/usr/bin/env python3
"""duck typed"""
from typing import Any, Sequence, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Args:
    Returns:
    """
    if lst:
        return lst[0]
    else:
        return None
