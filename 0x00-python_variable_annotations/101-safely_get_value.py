#!/usr/bin/env python3
"""Duck Typing"""
from typing import Any, Sequence, Union, Optional, Mapping, TypeVar
T = TypeVar('T')


def safely_get_value(dct: Mapping,
                     key: Any,
                     default:
                     Optional[Union[T, None]] = None) -> Union[Any, T]:
    """First element"""
    if key in dct:
        return dct[key]
    else:
        return default
