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


def is_bst(root, lower_bound, upper_bound):
    # base case
    if root is None:
        return True
    else:
        if root.value < lower_bound or root.value > upper_bound:
            return False
        left = is_bst(root.left, lower_bound, root.value)
        right = is_bst(root.right, root.value, upper_bound)

        if left is True and right is True:
            return True
        else:
            return False

def bst_checker(root):
    """ Check if a binary tree is a valid BST

    Runtime:
        Time  -> O(n):
        Space -> O(n):
    """
    # maybe find lowest and max value in tree first
    min_number = get_min_max_element(root, min)
    max_number = get_min_max_element(root, max)
    return is_bst(root, min_number, max_number)


def create_not_bst():
    #             1
    #         2       3
    #     4     5    6   7
    # 8

    root = BinaryTreeNode(1)
    root.insert_left(2)
    root.insert_right(3)

    root.left.insert_left(4)
    root.left.insert_right(5)

    root.right.insert_left(6)
    root.right.insert_right(7)

    root.left.left.insert_left(8)
    return root

def create_not_bst_web():
    #             50
    #         30       80
    #     20   60    70  90

    root = BinaryTreeNode(50)
    root.insert_left(30)
    root.insert_right(80)

    root.left.insert_left(20)
    root.left.insert_right(60)

    root.right.insert_left(70)
    root.right.insert_right(90)

    return root

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


if __name__ == "__main__":
    not_bst = create_not_bst()
    not_bst_web = create_not_bst_web()
    root = create_bst()

    # preorder_print(root)
    print bst_checker(root)
    print bst_checker(not_bst)
    print bst_checker(not_bst_web)


