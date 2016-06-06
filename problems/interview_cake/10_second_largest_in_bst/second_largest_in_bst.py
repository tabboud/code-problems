#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Binary Search Tree
1. All values to the left are less than this value
2. All values to the right are greater than this value
"""

class BinaryTreeNode(object):
  def __init__(self, value):
      self.value = value
      self.left  = None
      self.right = None

  def insert_left(self, value):
      self.left = BinaryTreeNode(value)
      return self.left

  def insert_right(self, value):
      self.right = BinaryTreeNode(value)
      return self.right

  def __repr__(self):
      return "%d" % self.value

def preorder_print(root):
    if root is not None:
        print "Node: ", root.value
        inorder_print(root.left)
        inorder_print(root.right)



def get_min_max_element(root, function):
    # Return the min/max of a tree (must pass in min or max)
    if root is None:
        return None
    else:
        left = get_min_max_element(root.left, function)
        right = get_min_max_element(root.right, function)
        values = [root.value] + [x for x in [left, right] if x is not None]

        return function(values)

def create_bst():
    #             5
    #         2       7
    #     1     3    6   8

    root = BinaryTreeNode(5)
    root.insert_left(2)
    root.insert_right(7)

    root.left.insert_left(1)
    root.left.insert_right(3)

    root.right.insert_left(6)
    root.right.insert_right(8)
    return root


def largest(root):
    # Find the largest value in a BST
    # keep going right while there are right nodes
    cur = root
    while cur is not None:
        if cur.right is None:
            # found the largest
            return cur.value
        cur = cur.right


def second_max_in_bst_recursive(root):
    """
    Go right all the way then return the second to last node

    Runtime:
        Time  -> O(h): where h is the height of the tree
        Space -> O(h): from the call stack
    """
    # base case: Empty tree
    if root is None:
        return None

    # Case 2: Largest element has a left subtree (i.e. 2nd largest is largest of this subtree)
    if root.right is None and root.left is not None:
        print "case 2"
        return largest(root.left)

    # Case 3: Check if we are at the second largest and the largest does not have a left subtree
    if root.right is not None and root.right.right is None and root.right.left is None:
        print "case 3"
        return root.value

    # Otherwise continue going right
    return second_max_in_bst(root.right)


def second_max_in_bst(root):
    """
    Go right all the way then return the second to last node

    Runtime:
        Time  -> O(h): where h is the height of the tree
        Space -> O(1):
    """
    # base case: Empty tree
    if root is None:
        return None
    elif root.left is None and root.right is None:
        return None

    cur = root

    while cur is not None:
        # Case 1: Largest element has a left subtree (i.e. 2nd largest is largest of this subtree)
        if cur.right is None and cur.left is not None:
            return largest(cur.left)

        # Case 2: Check if we are at the second largest and the largest does not have a left subtree
        if cur.right is not None and cur.right.right is None and cur.right.left is None:
            return cur.value

        # Otherwise continue going right
        cur = cur.right


if __name__ == "__main__":
    root = create_bst()

    # preorder_print(root)
    print second_max_in_bst(root)


