#/usr/bin/python3
def unique_sorted_list(numbers):
    
        # Convert the list to a set to remove duplicates
    unique_numbers = set(numbers)
    
    # Convert the set back to a list and sort it in ascending order
    sorted_list = sorted(list(unique_numbers))
    
    return sorted_list

numbers = [5, 2, 3, 5, 2, 1]
result = unique_sorted_list(numbers)
print(result)  # Output: [1, 2, 3, 5]