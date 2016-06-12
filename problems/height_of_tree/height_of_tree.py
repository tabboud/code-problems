#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def height_of_tree(root):
    """ Return the maximum height of a binary tree

    Complexity:
        Time  -> O(n): Go through all elements in binary tree
        Space -> O(n): Space for call stack since its recursive
    """
    if root is None:
        return 0
    else:
        left = height_of_tree(root.left)
        right = height_of_tree(root.right)

        return 1 + max(left, right)


if __name__ == "__main__":
 #        1
 #    2       3
 #   4 5     6  7
 #  8
 # 9

    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)

    root.left.left = Node(4)
    root.left.left.left = Node(8)
    root.left.left.left.left = Node(9)

    root.left.right = Node(5)

    root.right.left = Node(6)
    root.right.right = Node(7)

    print "height = ", height_of_tree(root)
