#!/usr/bin/python3

def logger(func):
    """Decorator to log function calls with arguments and results."""
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f"Calling {func.__name__} with args={args}, kwargs={kwargs} → result={result}")
        return result
    return wrapper

 
@logger
def coin_change(coins, amount):
    """
    Returns the minimum number of coins needed to make up the given amount.
    If it's not possible, return -1.
    """
    # DP array, initialize with infinity
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0  # 0 coins needed for amount 0
    
    for coin in coins:
        for x in range(coin, amount + 1):
            dp[x] = min(dp[x], dp[x - coin] + 1)
    
    return dp[amount] if dp[amount] != float('inf') else -1


# Example usage
print(coin_change([1, 2, 5], 11))  # 3 (5+5+1)
print(coin_change([2], 3))         # -1
print(coin_change([1], 0))         # 0