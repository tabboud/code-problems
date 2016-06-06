#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Write a function to see if a binary tree is superbalanced (if the difference
between the depths of any leaf nodes is no greater than one)
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


def is_balanced_bfs(root):
    """
    Traverse the tree level-order and mark the min_depth and
    max_depth as we traverse the tree

    Runtime:
        Time  -> O(n): Iterate all the tree nodes
        Space -> O(n): Place all elements into a queue
    """
    from Queue import Queue
    q = Queue()
    visited = set()

    # place initial node into queue
    q.put((root, 0))  # (node, depth)

    # set defaults for the min/max depths
    min_depth = 100
    max_depth = 0

    while not q.empty():
        node, cur_depth = q.get()
        visited.add(node)

        # Check if its a leaf node
        if node.left is None and node.right is None:
            # update min or max depth
            min_depth = min(min_depth, cur_depth)
            max_depth = max(max_depth, cur_depth)
        else:
            # add children to the queue
            if node.left is not None and node.left not in visited:
                q.put((node.left, cur_depth+1))
            if node.right is not None and node.right not in visited:
                q.put((node.right, cur_depth+1))


    # print "max: %d, min: %d" % (max_depth, min_depth)
    if max_depth - min_depth <= 1:
        return True
    else:
        return False


def is_balanced_dfs(root):
    """
    Iterative depth-first search to prevent a stack-overflow
    """
    # Hold all depths, we can stop traversing if there are more than 2 depths (i.e. they must be different)
    depths = []

    # Use a list as a stack
    stack = []

    cur_node = root
    # add first element to stack
    stack.append((cur_node, 0))    # (node, depth)

    while len(stack) > 0:
        print repr(stack)
        # get a node from the stack
        cur_node, cur_depth = stack.pop()

        # Case 1: Leaf node
        if cur_node.left is None and cur_node.right is None:
            if cur_depth not in depths:
                depths.append(cur_depth)
                # check the depths now
                depths_len = len(depths)
                if depths_len > 2 or (depths_len == 2 and abs(depths[0] - depths[1]) > 1):
                    # break out early if we found the wrong depth
                    return False
        else:
            # Case 2: keep stepping down the tree
            if cur_node.left is not None:
                stack.append((cur_node.left, cur_depth+1))

            if cur_node.right is not None:
                stack.append((cur_node.right, cur_depth+1))



    return True



if __name__ == "__main__":
    root = BinaryTreeNode(1)
    root.insert_left(2)
    root.insert_right(3)

    root.left.insert_left(4)
    root.left.insert_right(5)

    root.right.insert_left(6)
    root.right.insert_right(7)

    root.left.left.insert_left(8)
    # root.left.left.left.insert_left(9)

    # preorder_print(root)
    print "bfs: ", is_balanced_bfs(root)
    print "dfs: ", is_balanced_dfs(root)

#             1
#         2       3
#     4     5    6   7
# 8

