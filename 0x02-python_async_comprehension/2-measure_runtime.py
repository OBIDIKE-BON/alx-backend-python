#!/usr/bin/env python3
""" Module to demonstrate Async Comprehension"""
import asyncio
from typing import List
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """ Coroutine to measure runtime """
    start = asyncio.get_event_loop().time()
    batch = [async_comprehension() for _ in range(4)]
    await asyncio.gather(*batch)
    end = asyncio.get_event_loop().time()
    return end - start


if __name__ == "__main__":
    print(asyncio.run(measure_runtime()))
