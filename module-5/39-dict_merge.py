#/usr/bin/python3
""" Write a function that merges two dictionaries. If a key exists in both, keep the value from the second dictionary.
"""

def merge_dictionaries(dict1, dict2):
    merged = dict1.copy()  # Make a copy to avoid modifying the original dict1
    merged.update(dict2)   # Update with items from dict2
    return merged
d1 = {'a': 1, 'b': 2}
d2 = {'b': 3, 'c': 4}
result = merge_dictionaries(d1, d2)
print(result)  # Output: {'a': 1, 'b': 3, 'c': 4}