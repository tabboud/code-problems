#!/usr/bin/env python
# -*- coding: utf-8 -*-
class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __repr__(self):
        return str(self.value)


def find_path(root, value, path=None):
    """ Return the path to a node in a binary tree"""
    if path is None:
        path = []

    # Base Case
    if root is None:
        return None

    path.append(root)

    if root.value == value:
        return path

    # check left and right
    left = find_path(root.left, value, path)
    right = find_path(root.right, value, path)

    if left is not None:
        return left
    elif right is not None:
        return right

    # if we get here then we need to remove the root from the path
    # since its not the value and we have checked left and right
    path.pop()
    return None


def find_path_iterative(root, value):
    """ Iteratively find the path to a node"""
    stack = [root]
    visited = set()

    while len(stack) > 0:
        # last node in stack
        node = stack[-1]
        visited.add(node)

        if node is not None and node.value == value:
            return stack

        # add left and right nodes if not visited
        if node.left is not None and node.left not in visited:
            stack.append(node.left)
        elif node.right is not None and node.right not in visited:
            stack.append(node.right)
        else:
            stack.pop()


def lowest_common_ancestor(root, node1, node2):
    """ Find the lowest common ancestor between two
        nodes in a binary tree
        *Assume the nodes exist in the tree

    Complexity:
        Time  -> O(n): Go through all elements in the tree
        Space -> O(n): Possibly create a n element paths
    """
    # find the path to node1
    # path_to_node1 = find_path_iterative(root, node1.value)
    path_to_node1 = find_path(root, node1.value)
    # find the path to node2
    # path_to_node2 = find_path_iterative(root, node2.value)
    path_to_node2 = find_path(root, node2.value)


    # compare the two paths to find where they deviate
    length = min(len(path_to_node1), len(path_to_node2))
    for index in range(0, length):
        if path_to_node1[index] != path_to_node2[index]:
            return path_to_node1[index - 1]


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

    node1 = root.left.left.left   # 8
    node2 = root.left.right       # 5
    print lowest_common_ancestor(root, node1, node2)  # 2

    node1 = root.left.left.left   # 8
    node2 = root.right.right      # 7
    print lowest_common_ancestor(root, node1, node2)  # 1
