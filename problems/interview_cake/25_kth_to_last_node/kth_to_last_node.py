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


def kth_to_last_node(k, root):
    """ Return the kth to last node in a linked list

    Complexity:
        Time  -> O(n): Iterate the list once
        Space -> O(1): No extra space
    """
    if root is None:
        return

    # Use two pointers to traverse the list
    first = second = root

    # Move second pointer k positions
    for _ in xrange(k):
        if second.next is None:
            raise Exception("k is out of range!")
        second = second.next

    # Now move first and second one at a time until second reaches the end
    while second != None:
        second = second.next
        first = first.next

    # Return the value under first
    return first.value



if __name__ == "__main__":
    a = LinkedListNode("Angel Food")
    b = LinkedListNode("Bundt")
    c = LinkedListNode("Cheese")
    d = LinkedListNode("Devil's Food")
    e = LinkedListNode("Eccles")

    a.next = b
    b.next = c
    c.next = d
    d.next = e

    # returns the node with value "Devil's Food" (the 2nd to last node)
    print kth_to_last_node(2, a)

