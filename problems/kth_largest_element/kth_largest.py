#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Queue import PriorityQueue

def kth_largest(arr, k):
    """
    Find the kth largest number in the integer array, where k=1 is the first largest

    Runtime:
        Time  -> O(nlog(n)): Perform the sort on the array
        Space -> O(1): In place sorting

    """
    return sorted(arr, reverse=True)[k-1]


def kth_largest_pq(arr, k):
    """
    Find the kth largest number in the integer array, where k=1 is the first
    largest using a Priority Queue

    Runtime:
        Time  -> O(logn): Priority queue uses a heap under the hood
        Space -> O(n): Using a queue

    """
    q = PriorityQueue(len(arr))

    # add all items to the queue, using their value as the priority
    # we have to add the negative of the value, since the python priority queue
    # returns the lowest value first
    for val in arr:
        q.put(-val)

    # pop off k number of values to get the kth largest
    for i in xrange(k-1):
        q.get()

    # Finally return the value (negating it again to get back the original value)
    return -q.get()


if __name__ == "__main__":
    arr = [3, 4, 1, 2, 5]
    k = 1
    print kth_largest(arr, k)       # 5
    print kth_largest_pq(arr, k)    # 5
    k = 2
    print kth_largest(arr, k)       # 4
    print kth_largest_pq(arr, k)    # 4
    k = 3
    print kth_largest(arr, k)       # 3
    print kth_largest_pq(arr, k)    # 3

