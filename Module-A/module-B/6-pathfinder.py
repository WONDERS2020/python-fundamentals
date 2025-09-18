#!/usr/bin/python3

from functools import lru_cache

@lru_cache(maxsize=None)
def grid_paths(m: int, n: int) -> int:
    """
    Returns the number of unique paths in an m x n grid
    from top-left to bottom-right using memoization.
    """
    # Base case: if grid is 1x1, only 1 path (already there)
    if m == 1 and n == 1:
        return 1
    # If out of bounds, no path
    if m == 0 or n == 0:
        return 0
    
    # Move either down (m-1, n) or right (m, n-1)
    return grid_paths(m - 1, n) + grid_paths(m, n - 1)


# Example usage
print(grid_paths(3, 3))  # 6
print(grid_paths(3, 7))  # 28
print(grid_paths(1, 5))  # 1