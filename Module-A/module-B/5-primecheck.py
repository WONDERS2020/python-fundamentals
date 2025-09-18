#!/usr/bin/python3

from functools import lru_cache
import math

@lru_cache(maxsize=None)  # memoization decorator
def is_prime(n: int) -> bool:
    """Check if a number is prime with memoization."""
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    # Only check up to sqrt(n)
    limit = int(math.isqrt(n)) + 1
    for i in range(3, limit, 2):
        if n % i == 0:
            return False
    return True


# Example usage:
print(is_prime(2))   # True
print(is_prime(19))  # True
print(is_prime(20))  # False
print(is_prime(19))  # Cached result, very fast