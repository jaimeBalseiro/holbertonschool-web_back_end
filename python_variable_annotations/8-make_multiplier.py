#!/usr/bin/env python3
"""
write a function make_multiplier
"""


from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    takes multiplier and
    passes it as an
    argument
    """
    def multiplied(number: float) -> float:
        """
        'number' becomes a variable
        that returns a float
        """
        return (number * multiplier)

    return multiplied
