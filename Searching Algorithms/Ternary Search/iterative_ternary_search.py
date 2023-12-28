def iterative_ternary_search(int_list, target):
    """
    This function is used to search the given element using binary search algorithm
    Args:
        int_list (list): list of integers which is sorted
        target (int): element to be found
    Returns:
        int: position/index of the searching element
    """
    start_index = 0
    end_index = len(int_list) - 1
    while start_index <= end_index:
        mid1 = start_index + ((end_index - start_index)//3)
        mid2 = end_index - ((end_index - start_index)//3)
        if target == int_list[mid1]:
            return mid1
        if target == int_list[mid2]:
            return mid2
        if target < int_list[mid1]:
            end_index = mid1 - 1
        elif target > int_list[mid2]:
            start_index = mid2 + 1
        else:
            start_index = mid1 + 1
            end_index = mid2 - 1
    return -1


sample_list, key = [2, 6, 99, 200, 5000, 10089], 1
output = iterative_ternary_search(sample_list, key)
if output == -1:
    print("The desired element was not found in the given list")
else:
    print("The target element is found in index {}".format(output))
