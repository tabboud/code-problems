#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Reverse a linked list in-place
"""

class LinkedListNode(object):
    def __init__(self, value):
        self.value = value
        self.next = None


def print_list(root):
    while root is not None:
        print "Data: ", root.value
        root = root.next


def reverse_list(root):
    """ Reverse a linked list in-place

    Complexity:
        Time  -> O(n): Iterate the list once
        Space -> O(1): In-place reversal
    """
    if root is None:
        return

    cur = root
    tail = None

    while cur is not None:
        tmp = cur.next
        cur.next = tail
        tail = cur
        cur = tmp


if __name__ == "__main__":
    a = LinkedListNode(1)
    b = LinkedListNode(2)
    c = LinkedListNode(3)
    d = LinkedListNode(4)
    e = LinkedListNode(5)
    
    a.next = b
    b.next = c
    c.next = d
    d.next = e

    print_list(a)
    reverse_list(a)
    print "Reversed:"
    print_list(e)

