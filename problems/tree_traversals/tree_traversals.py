#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def preorder(root):
    """ Print the preorder traversal of a binary tree
        * root, left, right

    Complexity:
        Time  -> O(n): Go through all elements in binary tree
        Space -> O(n): Space for call stack since its recursive
    """
    if root is not None:
        print root.value
        preorder(root.left)
        preorder(root.right)

def preorder_no_recursion(root):
    """ Print the preorder traversal of a binary tree without recursion
        * root, left, right

    Complexity:
        Time  -> O(n): Go through all elements in binary tree
        Space -> O(n): Local stack
    """
    stack = []
    stack.append(root)
    visited = set()


    while len(stack) > 0:
        # get an element off the stack
        node = stack.pop()

        # push the right node, then the left node
        if node is not None:
            print node.value

            # add the right child
            if node.right is not None:
                stack.append(node.right)

            # add the left child
            if node.left is not None:
                stack.append(node.left)


def inorder(root):
    """ Print the inorder traversal of a binary tree
        * left, root, right

    Complexity:
        Time  -> O(n): Go through all elements in binary tree
        Space -> O(n): Space for call stack since its recursive
    """
    if root is not None:
        inorder(root.left)
        print root.value
        inorder(root.right)

def postorder(root):
    """ Print the postorder traversal of a binary tree
        * left, right, root

    Complexity:
        Time  -> O(n): Go through all elements in binary tree
        Space -> O(n): Space for call stack since its recursive
    """
    if root is not None:
        postorder(root.left)
        postorder(root.right)
        print root.value

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

    print "Preorder:"
    preorder(root)    # 1, 2, 4, 8, 9, 5, 3, 6, 7

    print "Preorder no recursion:"
    preorder_no_recursion(root)    # 1, 2, 4, 8, 9, 5, 3, 6, 7

    print "\nInorder:"
    inorder(root)     # 9, 8, 4, 2, 5, 1, 6, 3, 7

    print "\nPostorder:"
    postorder(root)   # 9, 8, 4, 5, 2, 6, 7, 3, 1
