#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Permutation Palindrome

Thoughts:
    BruteForce O(n!):
        Generate all permutations of the input string and check if they are
        palindromes
    Optimize:
        - key word here is "any permutation" so if the first permutation is
          palindrome then we can return, otherwise we need to keep checking,
          so how can we check that right away
        - The frequency of the words can tell us that it is a palindrome. i.e.
          All even character frequencies, or all even and exactly 1 odd will be
          a palindrome
"""
from collections import Counter


def permuation_palindrome(s):
    """ Check if any permutation of s is a palindrome

    Complexity:
        Time  -> O(n): Iterate the list once
        Space -> O(n): Use a hashmap to store the frequencies of the characters
    """
    s_map = Counter(s)

    # Check for all even character frequencies and exactly 1 odd frequency
    found_odd = False
    for key, value in s_map.items():
        if value % 2 != 0:
            # found an odd number
            if found_odd is True:
                # Found a second odd frequency character, so not a palindrome
                return False
            found_odd = True

    # Only even character frequencies exist or 1 odd frequency character, so definately a palindrome
    return True


def permuation_palindrome_set(s):
    """ Check if any permutation of s is a palindrome using a set

    Complexity:
        Time  -> O(n): Iterate the list once
        Space -> O(k): where k is the number of odd frequency chars
    """
    s_set = set()

    # Check for all even character frequencies and exactly 1 odd frequency
    for ch in s:
        if ch not in s_set:
            # add it to the set
            s_set.add(ch)
        else:
            # Must be in the set, so remove it
            s_set.remove(ch)

    # return the whether there are more than 1 element in the set, which
    # signifies the number of odd freq. chars.
    return len(s_set) <= 1


if __name__ == "__main__":
    #           True     True     False    False    True
    strings = ["civic", "ivicc", "civil", "livci", "raccar"]
    for string in strings:
        print permuation_palindrome(string)
