#/usr/bin/python3
""" Write a function that returns the symmetric difference of two sets.
Explain what symmetric difference means in your docstring or comment."""

def symmetric_difference_sets(set1, set2):
 
    return set1.symmetric_difference(set2)
a = {1, 2, 3}
b = {3, 4, 5}
result = symmetric_difference_sets(a, b)
print(result)  # Output: {1, 2, 4, 5}