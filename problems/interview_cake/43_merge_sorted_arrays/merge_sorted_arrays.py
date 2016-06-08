#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Merge Sorted Arrays
"""

def merge_lists(l1, l2):
    """ Merge two sorted lists

    Complexity:
        Time  -> O(n): Iterate both lists once
        Space -> O(n): Create a new list with n values
    """
    # check empty lists
    if len(l1) == 0 and len(l2) == 0:
        raise Exception("Both lists are empty")

    merged_lists = []
    start1 = 0
    start2 = 0

    while start1 < len(l1) or start2 < len(l2):
        # compare both
        if start1 < len(l1) and start2 < len(l2):
            if l1[start1] < l2[start2]:
                merged_lists.append(l1[start1])
                start1 += 1
            else:
                merged_lists.append(l2[start2])
                start2 += 1
        elif start1 < len(l1):
            # append the rest of l1
            merged_lists += l1[start1:]
            break
        elif start2 < len(l2):
            # append the rest of l2
            merged_lists += l2[start2:]
            break

    return merged_lists


if __name__ == "__main__":
    my_list     = [3, 4, 6, 10, 11, 15]
    alices_list = [1, 5, 8, 12, 14, 19]

    print merge_lists(my_list, alices_list) # [1, 3, 4, 5, 6, 8, 10, 11, 12, 14, 15, 19]

