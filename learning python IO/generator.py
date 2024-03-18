#!/usr/bin/python3

import itertools
import asyncio


squares = (x for x in itertools.count(1))
print(type(squares))
for n in squares:
    if n > 10:
        print()
        break
    print(n, end=', ')


async def async_squares(par):
    for n in itertools.count(1, par):
        print (f'async_squares: {n}')
        await asyncio.sleep(1)
        print (f'async_squares: {n} after sleep')
        if n > 20:
            break

async def main():
    batch = asyncio.gather(async_squares(2), async_squares(3))
    await batch

asyncio.run(main())
