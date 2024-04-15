def bucketsort(arr, k):
    """
    Perform bucket sort on the given array.

    Parameters:
    arr (list): The input list to be sorted.
    k (int): The number of buckets.

    Returns:
    list: The sorted list.

    Examples:
    >>> bucketsort([3, 2, 1, 5, 4], 6)
    [1, 2, 3, 4, 5]
    >>> bucketsort([], 5)
    []
    >>> bucketsort([5], 10)
    [5]
    >>> bucketsort([3, 5, 2, 3, 2, 5, 4, 4], 6)
    [2, 2, 3, 3, 4, 4, 5, 5]
    """
    counts = [0] * k
    for x in arr:
        counts[x] += 1

    sorted_arr = []
    for i in range(k):
        sorted_arr.extend([i] * counts[i])

    return sorted_arr

import doctest

if __name__ == "__main__":
    doctest.testmod()