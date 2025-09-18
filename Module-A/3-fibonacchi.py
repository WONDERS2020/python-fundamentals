#!/usr/bin/python3


def memoize(func):
    cache = {}

    def wrapper(n):
        if n in cache:
            return cache[n]
        result = func(n)
        cache[n] = result
        return result
    return wrapper


@memoize
def fibonacci(n):
    
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        else:
            return fibonacci(n-1) + fibonacci(n-2)

for i in range(10):
    print(f"Fibonacci({i}) = {fibonacci(i)}")