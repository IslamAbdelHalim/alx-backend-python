#!/usr/bin/env python3
"""
sum_mixed list
"""


from typing import List, Union


def sum_mixed_list(mxd_1st: List[Union[int, float]]) -> float:
    """
    takes a list mxd_1st of integers and floats
    and returns their sum as a float.
    """
    return sum(mxd_1st)
