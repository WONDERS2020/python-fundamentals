#/usr/bin/python3
""" Write a function that removes a key from a dictionary if it exists and returns the updated dictionary.
Parameters: dictionary and key to remove."""

def remove_key(dictionary, key_to_remove):
    
    if key_to_remove in dictionary:
        del dictionary[key_to_remove]
    return dictionary
my_dict = {'a': 1, 'b': 2, 'c': 3}
updated_dict = remove_key(my_dict, 'b')
print(updated_dict)  # Output: {'a': 1, 'c': 3}