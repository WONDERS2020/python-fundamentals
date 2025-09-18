#!/usr/bin/python3

def logger(func):
    """Decorator to log function calls with input string and result."""
    def wrapper(s, word_dict, *args, **kwargs):
        result = func(s, word_dict, *args, **kwargs)
        print(f"Calling {func.__name__} with s='{s}' → result={result}")
        return result
    return wrapper


@logger
def word_break(s, word_dict):
    """
    Returns True if string s can be segmented into words from word_dict.
    Uses recursion + memoization.
    """
    word_set = set(word_dict)
    memo = {}

    def can_break(start):
        if start == len(s):
            return True
        if start in memo:
            return memo[start]

        for end in range(start + 1, len(s) + 1):
            if s[start:end] in word_set and can_break(end):
                memo[start] = True
                return True
        memo[start] = False
        return False

    return can_break(0)


# Example usage
print(word_break("leetcode", ["leet", "code"]))       # True
print(word_break("applepenapple", ["apple", "pen"]))  # True
print(word_break("catsandog", ["cats","dog","sand","and","cat"]))  # False