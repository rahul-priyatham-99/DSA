def ternary_search(start_index, end_index, int_list, target):
    """
    This function is used to search the given element using ternary search algorithm
    Args:
        start_index (int): index of the starting element
        end_index (int): index of the last element
        int_list (list): list of integers which is sorted
        target (int): element to be found
    Returns:
        int: position/index of the searching element
    """
    if end_index >= start_index:
        mid1 = start_index + ((end_index - start_index) // 3)
        mid2 = end_index - ((end_index - start_index) // 3)
        if target == int_list[mid1]:
            return mid1
        if target == int_list[mid2]:
            return mid2
        elif target < int_list[mid1]:
            return ternary_search(start_index, mid1 - 1, int_list, target)
        elif target > int_list[mid2]:
            return ternary_search(mid2 + 1, end_index, int_list, target)
        else:
            return ternary_search(mid1+1, mid2-1, int_list, target)
    return -1


sample_list = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
start = 0
end = len(sample_list) - 1
key = 10

output = ternary_search(start, end, sample_list, key)
print("The target element is found in index {}".format(output))

