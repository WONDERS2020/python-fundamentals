#/usr/bin/python3
""" Write a function that takes two sets and returns a tuple with their union and intersection.
"""
def union_and_intersection(set1, set2):
    union = set1 | set2
    intersection = set1 & set2
    return (union, intersection)
a = {1, 2, 3}
b = {3, 4, 5}
result = union_and_intersection(a, b)
print(result)  # Output: ({1, 2, 3, 4, 5}, {3})