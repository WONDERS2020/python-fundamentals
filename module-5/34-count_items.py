#/usr/bin/python3
""" Write a function that takes a list of items and returns a dictionary with the count of each item.
Example: ["apple", "banana", "apple"] → {"apple": 2, "banana": 1}
"""
def count_items(items):
    item_counts = {}
    for item in items:
        if item in item_counts:
            item_counts[item] += 1
        else:
            item_counts[item] = 1
    return item_counts
fruits = ["apple", "banana", "apple"]
result = count_items(fruits)
print(result)  # Output: {'apple': 2, 'banana': 1}
