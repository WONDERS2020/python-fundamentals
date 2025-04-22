
def swap_min_max(lst):
    if not lst or len(lst) < 2:
        return lst  # No swap needed

    min_index = lst.index(min(lst))
    max_index = lst.index(max(lst))

    # Swap the elements
    lst[min_index], lst[max_index] = lst[max_index], lst[min_index]

    return lst

numbers = [4, 9, 2, 7, 5]
print(swap_min_max(numbers))