#!/usr/bin/env python
# -*- coding: utf-8 -*-

def kth_largest(arr, k):
    """
    Find the kth largest number in the integer array, where k=1 is the first largest

    Runtime:
        Time  -> O(nlog(n)): Perform the sort on the array
        Space -> O(1): In place sorting

    """
    return sorted(arr, reverse=True)[k-1]



if __name__ == "__main__":
    arr = [3, 4, 1, 2, 5]
    k = 1
    print kth_largest(arr, k)   # 5
    k = 2
    print kth_largest(arr, k)   # 4
    k = 3
    print kth_largest(arr, k)   # 3

