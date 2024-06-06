#!/usr/bin/env python3
"""
takes a list mxd_1st of integers and floats
and returns their sum as a float.
"""


from typing import Any, Sequence, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """First element"""
    if lst:
        return lst[0]
    else:
        return None
