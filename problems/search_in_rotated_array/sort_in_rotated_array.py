#!/usr/bin/env python
# -*- coding: utf-8 -*-

def search_in_sorted_array(arr, n):
    """ Modified binary search

    Complexity:
        Time  -> O(logn): Basic binary search
        Space -> O(1): No extra space needed
    """
    start = 0
    end = len(arr) - 1

    while start <= end:
        middle = (start + end) / 2
        middle_value = arr[middle]

        if n == middle_value:
            return middle
        elif n > middle_value and n <= arr[end]:
            # go right
            start = middle + 1
        else:
            # go left
            end = middle - 1


if __name__ == "__main__":
    arr = [15, 16, 17, 20, 25, 1, 3, 4, 5, 7, 10, 14]
    print search_in_sorted_array(arr, 5)    # 8 (index of 5 in the array)

    for x in arr:
        print search_in_sorted_array(arr, x)    # 0-11 (all index's)

