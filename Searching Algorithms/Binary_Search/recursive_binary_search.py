def recursive_binary_search(start_index, end_index, int_list, target):
    """
    This function is used to search the given element using binary search algorithm
    Args:
        start_index (int): index of the starting element
        end_index (int): index of the last element
        int_list (list): list of integers which is sorted
        target (int): element to be found
    Returns:
        int: position of the searching element
    """
    if start_index <= end_index:
        mid = (start_index + end_index) // 2
        if target == int_list[mid]:
            return mid
        elif target < int_list[mid]:
            return recursive_binary_search(start_index, mid-1, int_list, target)
        elif target > int_list[mid]:
            return recursive_binary_search(mid+1, end_index, int_list, target)
    else:
        return -1


sample_list = [2, 6, 99, 200, 5000, 10089]
start, end = 0, len(sample_list)-1
key = 200
output = recursive_binary_search(start, end, sample_list, key)
print("The target element is found in index {}".format(output))

