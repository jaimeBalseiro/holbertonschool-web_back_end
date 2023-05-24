#!/usr/bin/env python3
"""
write a function sum_mixed_list
"""


from typing import List, Union


def sum_mixed_list(mxd_list: List[Union[int, float]]) -> float:
    """
    function sum_mixed_list
    sums the mixed list and
    returns it as a float
    """
    return sum(mxd_list)
