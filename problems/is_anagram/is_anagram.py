#!/usr/bin/env python

def hash_string(str):
    """
  Map characters to prime numbers and return a multiplicative unique hash

  Only works on a-z, A-Z
    """
    charMap = {
      'a': 2,
      'b': 3,
      'c': 5,
      'd': 7,
      'e': 11,
      'f': 13,
      'g': 17,
      'h': 19,
      'i': 23,
      'j': 29,
      'k': 31,
      'l': 37,
      'm': 41,
      'n': 43,
      'o': 47,
      'p': 53,
      'q': 59,
      'r': 61,
      's': 67,
      't': 71,
      'u': 73,
      'v': 79,
      'w': 83,
      'x': 89,
      'y': 97,
      'z': 101,
      'A': 103,
      'B': 107,
      'C': 109,
      'D': 113,
      'E': 127,
      'F': 131,
      'G': 137,
      'H': 139,
      'I': 149,
      'J': 151,
      'K': 163,
      'L': 167,
      'M': 173,
      'N': 179,
      'O': 181,
      'P': 191,
      'Q': 193,
      'R': 197,
      'S': 199,
      'T': 211,
      'U': 223,
      'V': 227,
      'W': 229,
      'X': 233,
      'Y': 239,
      'Z': 241
    }

    return reduce(lambda memo, char: memo * charMap[char], list(str), 1);


def is_anagram(str1, str2):
    """
   Check if str1 is an anagram of str2

   Runtime:
       O(n): Go through each string once, and the hashmap once
    """
    # anagrams if they have the same number of characters
    # initial check for string length
    if len(str1) != len(str2):
        return False

    map1 = {}
    map2 = {}

    for ch in str1:
        if ch in map1:
            map1[ch] += 1
        else:
            map1[ch] = 0

    for ch in str2:
        if ch in map2:
            map2[ch] += 1
        else:
            map2[ch] = 0

    if map1 != map2:
        return False
    else:
        return True


def is_anagram_prime(s1, s2):
    """
    Use prime numbers since they are multiplicatively unique, that the hash of each string will equal the same
    Runtime:
        O(n): Just need to go through each string once and calculate the hash
    """
    # check the lengths
    if len(s1) != len(s2):
        return False

    s1_hash = hash_string(s1)
    s2_hash = hash_string(s2)

    if s1_hash == s2_hash:
        return True
    else:
        return False


if __name__ == "__main__":
    print is_anagram('abcde', 'edcba') # YES
    print is_anagram('abcde', 'ea')    # NO

    print is_anagram_prime('abcde', 'edcba') # YES
    print is_anagram_prime('abcde', 'ea')    # NO
