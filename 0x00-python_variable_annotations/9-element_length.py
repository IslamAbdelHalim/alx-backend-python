#!/usr/bin/env python3
"""
takes a list mxd_1st of integers and floats
and returns their sum as a float.
"""

from typing import List, Sequence, Tuple, Iterable


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Return the sum of two floats"""
    return [(i, len(i)) for i in lst]
