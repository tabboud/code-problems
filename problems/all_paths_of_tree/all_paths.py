#!/usr/bin/env python
# -*- coding: utf-8 -*-
class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __repr__(self):
        return str(self.value)


def print_all_paths(root, path=None):
    """ Print all paths of a binary tree

    Complexity:
        Time  -> O(n): Go through all elements in the tree
        Space -> O(n): Call stack space
    """
    if path is None:
        path = []

    if root is not None:
        path.append(root.value)
        print_all_paths(root.left, path)
        print_all_paths(root.right, path)

        # hit a leaf node, so print the path
        if root.left is None and root.right is None:
            print ", ".join(str(x) for x in path)

        # remove the last element from the list and continue
        path.pop()


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

    print_all_paths(root)
    # 1, 2, 4, 8, 9
    # 1, 2, 5
    # 1, 3, 6
    # 1, 3, 7
