#/usr/bin/pyhon3
""" Write a function that checks if two sets have any common items and returns True or False.
"""
def have_common_items(set1, set2):
  
    return not set1.isdisjoint(set2)
a = {1, 2, 3}
b = {3, 4, 5}
print(have_common_items(a, b))  # Output: True

c = {6, 7}
print(have_common_items(a, c))  # Output: False
