#!/usr/bin/env python3
"""Concurrent coroutines in Python"""


def measure_time(n: int, max_delay: int) -> float:
    """Measures the total execution time for wait_n"""
    wait_n = __import__('1-concurrent_coroutines').wait_n
    import time
    import asyncio
    start = time.time()
    (asyncio.run(wait_n(n, max_delay)))
    return time.time() - start


if __name__ == "__main__":
    print(measure_time(5, 2))
    print(measure_time(4, 3))
    print(measure_time(3, 1))
    print(measure_time(2, 5))
    print(measure_time(1, 4))
