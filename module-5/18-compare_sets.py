#/usr/bin/python3
def set_operations(set_a, set_b):
    
    result = {
        'union': set_a | set_b,
        'intersection': set_a & set_b,
        'difference_A_B': set_a - set_b,
        'difference_B_A': set_b - set_a
    }
    return result

a = {1, 2, 3}
b = {3, 4, 5}

print(set_operations(a, b))