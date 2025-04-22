#/usr/bin/python3
def set_difference(set1, set2):
    
    # Calculate the difference between set1 and set2
    difference = set1 - set2
    
    return difference

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5}
result = set_difference(set1, set2)
print(result)  # Output: {1, 2}
