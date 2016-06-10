#!/usr/bin/env python
"""
 Rough Algorithm:
    Iterate through all words in dictionary
    get the difference for each word in dictionary, then return the min

Complexity:
    Time  -> O(M*N): Where M is the size of the dictionary and N is the length
                        of the given word (for each word in the dictionary, we
                        may need to iterate over the given word)
    Space -> O(1): No extra space needed
 """
def get_deletions(string, key):
    deletions = 1000
    string_len = len(string)
    key_len = len(key)
    #print string_len, key_len, s, key

    if string_len >= key_len:
        # iterate through both strings
        S = L = 0
        while L < string_len:
            if S == key_len:
                deletions = string_len - key_len
                break
            if string[L] == key[S]:
                S += 1
                L += 1
            else:
                L += 1

    return deletions
    
def minimum_deletions(s, dictionary):
    result = 100
    for key in dictionary.keys():
        x = get_deletions(s, key)
        print x
        result = min(result, x)

    return result



s = "catnot"
dictionary = {
        "cat" : 1,
        "dog" : 1,
        "animal" : 1,
        "something" : 1,
        "okay" : 1,
        "work" : 1,
        "fireplace" : 1,
        }

print minimum_deletions(s, dictionary)

