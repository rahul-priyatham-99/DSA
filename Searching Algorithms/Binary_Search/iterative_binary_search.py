def iterative_binary_search(int_list, target):
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
        mid = (start_index + end_index) // 2
        if target == int_list[mid]:
            return mid
        elif target < int_list[mid]:
            end_index = mid - 1
        elif target > int_list[mid]:
            start_index = mid + 1
    return -1


sample_list, key = [2, 6, 99, 200, 5000, 10089], 200
output = iterative_binary_search(sample_list, key)
print("The target element is found in index {}".format(output))










