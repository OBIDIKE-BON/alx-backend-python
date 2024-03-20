#!/usr/bin/env python3
""" Module to demonstrate Async Generator"""
import asyncio
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """ Coroutine to generate random float numbers """
    import random
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)


if __name__ == "__main__":
    async def print_yielded_values():
        result = [i async for i in async_generator()]
        print(result)

    asyncio.run(print_yielded_values())
