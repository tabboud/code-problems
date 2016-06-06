#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Find the rotation point of a list of strings
"""

def find_rotation_point(arr):
    """
    Binary search until the previous value is greater then current lexicographically
    """
    start = 0
    end = len(arr) - 1

    while start < end:
        middle = (start+end)//2

        # check that the middle is < the end. if not then the reflection is to the left
        if arr[middle] < arr[end]:
            # correctly sorted, so go left
            end = middle - 1
        elif arr[middle] > arr[end]:
            # reflection must be right
            start = middle + 1

    return end

if __name__ == "__main__":
    arr = [
        "xyz",
        "zzz",
        "abc",   # Inflection
        "bcd",
        "cde",
        "def",
        "efg",
    ]

    print find_rotation_point(arr)
