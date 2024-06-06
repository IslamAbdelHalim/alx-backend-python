#!/usr/bin/env python3
"""
takes a list mxd_1st of integers and floats
and returns their sum as a float.
"""


from typing import List, Union


def safe_first_element(lst: List[Union[int, float]]) -> Union[int, float, None]:
    """
    takes a list mxd_1st of integers and floats
    and returns their sum as a float.
    """
    if lst:
        return lst[0]
    else:
        return None
