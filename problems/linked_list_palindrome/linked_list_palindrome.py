#!/usr/bin/env python
# -*- coding: utf-8 -*-
class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None

def create_linked_list(values):
    root = Node(values[0])
    prev_node = root

    for value in values[1:]:
        tmp = Node(value)
        prev_node.next = tmp
        prev_node = tmp

    return root


def is_permutation_stack(root):
    """ Check if the linked list is a permutation by using a stack

    Complexity:
        Time  -> O(n): Iterate the list twice
        Space -> O(n): Create an n element stack
    """
    # use a stack to compare the last elements to the first elements
    # This is the same way recursion would work
    stk = []

    cur = root
    while cur is not None:
        stk.append(cur.value)
        cur = cur.next

    cur = root
    while cur is not None:
        if stk.pop() != cur.value:
            return False
        cur = cur.next
    return True


def is_permutation_list(root):
    """ Check if the linked list is a permutation by storing the 
        values in a list and comparing the list to its reverse

    Complexity:
        Time  -> O(n): Iterate the list twice
        Space -> O(n): Create an n element list
    """
    elements = []

    cur = root
    while cur is not None:
        elements.append(cur.value)
        cur = cur.next

    return elements == elements[::-1]



if __name__ == "__main__":
    root = create_linked_list('racecar')
    print is_permutation_stack(root)
    print is_permutation_list(root)

