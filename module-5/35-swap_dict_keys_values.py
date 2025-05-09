#/usr/bin/python3
""" Write a function that swaps keys and values in a dictionary.
Example: {"a": 1, "b": 2} → {1: "a", 2: "b"}"""

def swap_keys_values(d):
    return {value: key for key, value in d.items()}
original = {"a": 1, "b": 2}
swapped = swap_keys_values(original)
print(swapped)  # Output: {1: 'a', 2: 'b'}