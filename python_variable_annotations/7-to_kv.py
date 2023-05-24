#!/usr/bin/env python3
"""
write a function to_kv
"""


from typing import List, Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    to_kv is passed as
    args and have to be
    annotated, while v is
    squared
    """
    return (k, v * v)
