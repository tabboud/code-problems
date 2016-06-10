#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Group Anagrams
"""

def group_anagrams(arr):
    """ Group all anagrams in a list of strings
    
    Algorithim:
        1. Sort the strings
        2. Insert the string into a hashmap
        3. 

    Complexity:
        Time  -> O(nlogn): Sorting the list and iterating it 
        Space -> O(n): Need extra space for the list and dictionary
    """
    a_map = {}
    for word in arr:
        sorted_word = ''.join(sorted(word))
        if sorted_word not in a_map:
            a_map[sorted_word] = [word]
        else:
            a_map[sorted_word].append(word)

    groups = []
    for key, values in a_map.items():
        groups.append(values)

    return groups


if __name__ == "__main__":
    strings = ["cat", "dog", "act", "door", "odor"]
    print group_anagrams(strings)

