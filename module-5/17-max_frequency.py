
from collections import Counter

def most_frequent_string(strings):
    
    if not strings:
        return None, 0

    count = Counter(strings)
    most_common = count.most_common(1)[0]  # Returns a list of (item, count)
    return most_common
input_list = ["apple", "banana", "apple", "orange", "banana", "apple"]
print(most_frequent_string(input_list))