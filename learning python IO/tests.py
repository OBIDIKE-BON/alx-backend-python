#!/usr/bin/env python3
import random

def random_numbers():
    while True:
        yield random.uniform(1, 100)

def main():
    numbers = random_numbers()
    for _ in range(110):
        print(next(numbers))

if __name__ == '__main__':
    main()
    main()
    main()
    main()
    main()
    main()
    main()
    main()