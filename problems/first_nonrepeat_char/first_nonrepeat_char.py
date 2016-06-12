#!/usr/bin/env python
# -*- coding: utf-8 -*-
from collections import Counter  # Use this instead of my own hashmap

def first_nonrepeat(string):
    """ Find the first non-repeating character in the string

    Complexity:
        Time  -> O(n): iterate over the string twice
        Space -> O(n): hashmap of n elements
    """
    string_count = Counter(string)
    for ch in string:
        if string_count[ch] < 2:
            return ch



if __name__ == "__main__":
    string = "teeter"
    print first_nonrepeat(string)    # r

    string = "total"
    print first_nonrepeat(string)    # o

