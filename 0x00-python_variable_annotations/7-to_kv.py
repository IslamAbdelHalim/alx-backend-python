#!/usr/bin/env python3
"""
takes a list mxd_1st of integers and floats
and returns their sum as a float.
"""


from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    takes a string k and an int OR float v as arguments
    and returns a tuple.
    The first element of the tuple is the string k.
    The second element is the square of the int/float v
    and should be annotated as a float.
    """
    return (k, v * v)
