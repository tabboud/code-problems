#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Dropbox hackerrank question
"""
def pattern_search(hmap, pattern, string):
    """ Determine if string follows the pattern 
    
    Complexity:
        Time  -> O()
        Space -> O()
    """
    if hmap is None:
        hmap = dict()

    match_length = len(string)

    while(match_length > 0):
        # Get whats left of the string
        match = string[0:match_length]
        p = pattern[0]
        left = string[match_length:]
        hmap_copy = dict(hmap)
        #print("match: %s\tleft: %s     \tpattern: %s"%(match, left, pattern))
        if p not in hmap_copy:
            hmap_copy[p] = match

        if hmap_copy[p] == match:
            # either a new entry or it matches an existing pattern value
            if len(pattern) > 1:
                # recurse while there are still pattern values left
                if len(left) > 0 and pattern_search(hmap_copy, pattern[1:], left):
                    return True
            else:
                # no more pattern elements left, then we already know its a match
                if len(left) == 0:
                    return True

        match_length -= 1
    return False

if __name__ == "__main__":
    print pattern_search ({}, ['a', 'b', 'a'], "xyZxy")  # True
    print pattern_search ({}, ['a', 'b', 'a', 'b'], "redblueredblue")  # True
    print pattern_search ({}, ['a', 'a', 'b'], "redblueredblue")  # False

