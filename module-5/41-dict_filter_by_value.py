#/usr/bin/python3
""" Write a function that returns a new dictionary only containing items where the value is greater than a given number.
"""
def filter_dict_by_value(data, threshold):
    
    return {key: value for key, value in data.items() if value > threshold}
scores = {'Alice': 88, 'Bob': 72, 'Charlie': 95, 'David': 65}
filtered = filter_dict_by_value(scores, 80)
print(filtered)  # Output: {'Alice': 88, 'Charlie': 95}