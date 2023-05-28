#!/usr/bin/env python3
"""Take imported from task 1"""


import time
from typing import List
import random
import asyncio
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int = 10) -> float:
    """_summary_
    Args:
        n (int): _description_
        max_delay (int): _description_
    Returns:
        float: _description_
    """
    start = time.time()
    asyncio.run(wait_n(n, max_delay))
    end = time.time()
    total_time = end - start
    return (total_time / 2)
