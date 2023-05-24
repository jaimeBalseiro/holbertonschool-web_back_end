#!/usr/bin/env python3
"""
Annotate the functions given
"""


from typing import List, Tuple, Sequence, Iterable


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Annotate the func
    given
    """
    return [(i, len(i)) for i in lst]
