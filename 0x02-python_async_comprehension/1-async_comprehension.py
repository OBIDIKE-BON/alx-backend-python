#!/usr/bin/env python3
""" Module to demonstrate Async Comprehension"""
import asyncio
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """ Coroutine to generate random float numbers """
    return [x async for x in async_generator()]


if __name__ == "__main__":
    async def main():
        print(await async_comprehension())

    asyncio.run(main())
