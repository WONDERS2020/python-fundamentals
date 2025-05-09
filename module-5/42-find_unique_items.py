#/usr/bin/python3
""" Write a function that takes two lists and returns a set of items that appear in only one list.
"""
def symmetric_difference(list1, list2):
 
    return set(list1).symmetric_difference(set(list2))
a = [1, 2, 3, 4]
b = [3, 4, 5, 6]
result = symmetric_difference(a, b)
print(result)  # Output: {1, 2, 5, 6}