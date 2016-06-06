#!/usr/bin/env python
# -*- coding: utf-8 -*-
from collections import Counter

def is_permutation(str1, str2):
    """ Check if str1 is an permutation of str2

    Complexity:
        Time  -> O(n): Go through each string once, and the hashmap once
        Space -> O(n): Create two hashmaps
    """
    map1 = Counter(str1)
    map2 = Counter(str2)

    return map1 == map2



def count_permutations(s1, s2):
    """ Count the number of permutations of s2 that exist in s1

    Complexity:
        Time  -> O(n): Go through the string once
        Space -> O(n): Create the permutations list
    """ 
    window_size = len(s2)
    permutations = set()

    for i in xrange(len(s1)-window_size+1):
        substring = s1[i:i+window_size]
        if is_permutation(substring, s2) is True and substring not in permutations:
            permutations.add(substring)
    
    return len(permutations)


if __name__ == "__main__":
    s1 = "abcdecabxabc"
    s2 = "abc"          # Permutations: abc, acb, bac, bca, cab, cba
    print count_permutations(s1, s2) # 2 -> abc, cab

