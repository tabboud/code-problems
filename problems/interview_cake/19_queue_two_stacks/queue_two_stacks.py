#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Implement a queue with 2 stacks and maintain FIFO
"""

class Queue(object):
    """
    Queue that achieves a total runtime of O(m^2) for m function calls
    """
    def __init__(self):
        self.stk1 = []
        self.stk2 = []

    def enqueue(self, value):
        """
        Move n items from stk1 to stk2, then n-1 items back
        Complexity:
            Time  -> O(n)
        """
        # steps:
        # 1. push everything from stk1 onto stk2
        while len(self.stk1) > 0:
            self.stk2.append(self.stk1.pop())

        # 2. Insert the value into the bottom of stk1
        self.stk1.append(value)

        # 3. push everything from stk2 back onto stk1
        while len(self.stk2) > 0:
            self.stk1.append(self.stk2.pop())


    def dequeue(self):
        """
        Pop directly from stk1
        Complexity:
            Time  -> O(1)
        """
        # always dequeue from stk1
        if len(self.stk1) == 0:
            raise Exception("No elements to dequeue!")
        
        return self.stk1.pop()


class SmartQueue(object):
    """
    Alternate Queue that achieves a total runtime of O(m) for m function calls
    """
    def __init__(self):
        self.in_stack = []
        self.out_stack = []

    def enqueue(self, value):
        """
        Complexity:
            Time  -> O(1): Always insert into in_stack
        """
        # steps:
        # 1. push everything to in_stack
        self.in_stack.append(value)

    def dequeue(self):
        """
        Check the out_stack first for any elements, and dequeue from there, then
        move all elements from in_stack to out_stack if the out_stack is empty

        Complexity:
            Time  -> O(n)
        """
        if len(self.out_stack) > 0:
            # pop directly from the out_stack
            return self.out_stack.pop()

        # otherwise, move items from in_stack to out_stack
        while len(self.in_stack) > 1:
            self.out_stack.append(self.in_stack.pop())

        return self.in_stack.pop()


if __name__ == "__main__":
    q = SmartQueue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)

    print repr(q.in_stack)
    print repr(q.out_stack)

    print q.dequeue()
    print q.dequeue()

    q.enqueue(5)

    print repr(q.in_stack)
    print repr(q.out_stack)

    print q.dequeue()
    print q.dequeue()


