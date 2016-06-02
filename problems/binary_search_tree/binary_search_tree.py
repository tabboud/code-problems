#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree(object):
    """
    <= go left
    >  go right
    """
    def __init__(self):
        self.root = None
        self.count = 0


    def search(self, value):
        # search for value in the tree
        if self.root is None:
            return

        cur = self.root
        while cur != None:
            if cur.value == value:
                print "Found %s" % value
                return
            elif value < cur.value:
                cur = cur.left
            else:
                cur = cur.right

        print "could not find (%s)" % value


    def insert(self, node):
        if self.root is None:
            # insert at the root
            self.root = node
        else:
            # find the spot for insertions
            cur = self.root
            prev = self.root
            while cur != None:
                if node.value <= cur.value:
                    # go left
                    if cur.left is None:
                        # insert it now
                        cur.left = node
                        break
                    cur = cur.left
                elif node.value > cur.value:
                    # go right
                    if cur.right is None:
                        # insert it now
                        cur.right = node
                        break
                    cur = cur.right

        self.count += 1


    def remove(self, value):
        # remove an element with value from the tree
        if self.root is None:
            return

        if self.root.value == value:
            self.root = None

        cur = self.root
        prev = self.root
        while cur != None:
            if cur.value == value:
                print "Found %s" % value
                return
            elif value < cur.value:
                cur = cur.left
            else:
                cur = cur.right

        print "could not find (%s)" % value
        self.count -= 1

    def inorder_print(self, root=None):
        # inorder traversal of tree
        if root != None:
            self.inorder_print(root.left)
            print "Node: %s" % root.value
            self.inorder_print(root.right)


if __name__ == "__main__":
    bst = BinarySearchTree()
    bst.insert(Node(5))
    bst.insert(Node(2))
    bst.insert(Node(4))
    bst.insert(Node(1))
    bst.insert(Node(0))

    bst.inorder_print(bst.root)

    bst.search(0)
    bst.search(2)
    bst.search(20)
