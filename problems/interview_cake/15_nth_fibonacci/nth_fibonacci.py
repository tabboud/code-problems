#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
"""

def memoize(f):
    cache  = {}
    def function(n):
        if n in cache:
            return cache[n]
        else:
            cache[n] = f(n)
            return cache[n]
    return function

@memoize
def fib_memo(n):
    """ Find nth fibonacci number using memoization

    Complexity:
        Time  -> O(n): Caching the results
        Space -> O(n): Keeping a dictionary of n possible results
    """
    if n < 2:
        return n
    else:
        return fib_memo(n-1) + fib_memo(n-2)

def fib_bottomup(n):
    """ Find nth fibonacci number starting from fib(0) up to fib(n)

    Complexity:
        Time  -> O(n): Iterate from 0 to n
        Space -> O(1): No extra space needed
    """
    if n < 0:
        raise Exception("No negative numbers")

    if n <= 1:
        return n

    # start at 0 and go up to n
    result = 0
    prev_1 = 1      # fib(n-1)
    prev_2 = 0      # fib(n-2)

    for _ in xrange(n-1):
        # compute the fib (prev + 2nd_prev)
        result = prev_1 + prev_2
        prev_2 = prev_1
        prev_1 = result

    return result


if __name__ == "__main__":
    print fib_memo(9)
    print fib_bottomup(9)

