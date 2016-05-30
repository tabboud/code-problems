#!/usr/bin/env python
# -*- coding: utf-8 -*-

def largest_continous_sum(arr):
    """
    Find the largest continous sum in the array

    Runtime:
        Time  -> O():
        Space -> O():

    """
    max_so_far = 0
    max_ending_here = 0

    for num in arr:
        max_ending_here += num

        # Don't handle negative numbers yet
        if max_ending_here < 0:
            max_ending_here = 0

        max_so_far = max(max_ending_here, max_so_far)

    return max_so_far


if __name__ == "__main__":
    arr = [-2, -3, 4, -1, -2, 1, 5, -3]
    print largest_continous_sum(arr)    # 7
