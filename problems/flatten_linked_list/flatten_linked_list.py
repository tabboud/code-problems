#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Queue import Queue
class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None
        self.child = None


def print_list(root):
    cur = root
    while cur is not None:
        print cur.value
        cur = cur.next


def create_linked_list():
    """ Here is the linked list structure
    '->' == next pointers
    '|'  == child pointers

    1 -> 2 -> 3 -> 4
         |         |
         5 -> 6    7
         |         |
         8         9

    """
    one = Node(1)
    two = Node(2)
    three = Node(3)
    four = Node(4)
    five = Node(5)
    six = Node(6)
    seven = Node(7)
    eight = Node(8)
    nine = Node(9)

    # add the next/child pointers
    one.next = two
    two.next = three
    two.child = five
    three.next = four
    four.child = seven
    five.next = six
    five.child = eight
    seven.child = nine

    return one


def flatten_linked_list(root):
    """ Flatten a linked list and keep the sorted order

    Algorithm:
        1. Traverse the linked list like normal
        2. When a node has a child, add the child to the queue
        3. When the list next pointer hits the end,
           pop an element from the queue, fix the next pointer, and continue

    Complexity:
        Time  -> O(n): Iterate the list once
        Space -> O(n): n element queue
    """
    q = Queue()
    visited = set()

    cur = root

    while cur is not None:
        visited.add(cur)

        if cur.child is not None and cur.child not in visited:
            # add child to queue
            q.put(cur.child)

        # next is done, so continue with the child, but fix the next pointer
        if cur.next is None and not q.empty():
            next_node = q.get()
            cur.next = next_node

        cur = cur.next


if __name__ == "__main__":
    root = create_linked_list()
    print "List Before:"
    print_list(root)

    flatten_linked_list(root)

    print "List After:"
    print_list(root)

