#!/usr/bin/env python3
import asyncio
from time import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Measure the runtime of wait_n"""
    start_time = time()
    asyncio.run(wait_n(n, max_delay))
    end_time = time()
    return end_time - start_time
