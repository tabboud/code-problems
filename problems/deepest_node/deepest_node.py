#!/usr/bin/env python
"""
 Rough Algorithm:
    Use BFS to go through all nodes in the tree. The deepest node will be the
    element that is last in the queue.

Complexity:
    Time  -> O(M*N): Where M is the size of the dictionary and N is the length
                        of the given word (for each word in the dictionary, we
                        may need to iterate over the given word)
    Space -> O(1): No extra space needed
 """
from Queue import Queue

class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def find_deepest_node(root):
    q = Queue()
    q.put(root)
    visited = set()

    while not q.empty():
        node = q.get()
        
        # add all the children
        if node.left is not None and node.left not in visited:
            q.put(node.left)

        if node.right is not None and node.right not in visited:
            q.put(node.right)

        if q.empty():
            print "Deepest Node is: ", node.value
            return


def find_deepest_node_recursive(root, level):
    if root is None:
        return (None, level)
    elif root.left is None and root.right is None:
        return (root.value, level)
    else:
        # find left deepest node
        left = find_deepest_node_recursive(root.left, level+1)

        # find right deepest node
        right = find_deepest_node_recursive(root.right, level+1)

        if left[1] > right[1] and left[0] is not None:
            return left
        elif right[0] is not None:
            return right
        else:
            return (None, 0)


if __name__ == "__main__":
    root = Node(5)
    root.left = Node(3)
    root.right = Node(7)
    root.left.left = Node(2)
    root.left.right = Node(4)

    root.right.left = Node(6)
    root.right.right = Node(8)
    root.right.right.right = Node(7)
    root.right.right.right.right = Node(1)

    find_deepest_node(root)    # Deepest node is 1
    print find_deepest_node_recursive(root, 0)    # Deepest node is 1, level 4

