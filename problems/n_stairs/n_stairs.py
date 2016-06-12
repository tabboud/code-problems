#!/usr/bin/env python
# -*- coding: utf-8 -*-
def memoize(fn):
    cache = {}
    def f(n):
        if n in cache:
            return cache[n]
        else:
            cache[n] = fn(n)
            return cache[n]
    return f

@memoize
def n_stairs(n):
    """ Count the number of ways to get to n stairs

    Complexity:
        Time  -> O(n): memoized
        Space -> O(n): memoized cache
    """
    if n <= 1:
        return n

    return n_stairs(n-1) + n_stairs(n-2)


if __name__ == "__main__":
    N = 20
    print n_stairs(N+1) #

    N = 4
    print n_stairs(N+1) # 5
