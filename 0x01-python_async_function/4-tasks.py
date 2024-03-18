#!/usr/bin/env python3
"""Concurrent coroutines in Python"""
import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Wait for a random delay between 0 and max_delay seconds"""
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    return [await task for task in asyncio.as_completed(tasks)]


if __name__ == '__main__':
    n = 5
    max_delay = 6
    print(asyncio.run(task_wait_n(n, max_delay)))
