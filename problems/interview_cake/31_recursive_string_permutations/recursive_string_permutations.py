#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Recursive String Permutations

"""
def swap(string, index1, index2):
    # Swap characters at index1 with index2 in the string
    string = list(string)
    tmp = string[index1]
    string[index1] = string[index2]
    string[index2] = tmp
    return ''.join(string)

def _permute(string, start, string_set=None):
    if string_set is None:
        string_set = set()

    # Base case
    if start >= len(string):
        return
    else:
        # Go through the string, swapping and recursing
        runner = start
        # iterate runner from this location to the end
        while runner < len(string):
            new_string = swap(string, start, runner)
            string_set.add(new_string)
            runner += 1
            # recurse
            _permute(new_string, start+1, string_set)

        return string_set

# Implementation 1
def permute(string):
    return _permute(string, 0)


# Implementation 2
def get_permutations(string):
    """ Generate all permutations by breaking it down into subproblems.
        The subproblem can be getting all permutations for all characters except
        the last one. Then we can insert the last character into every
        position of the previous permutations

        The base case will be when there is only 1 character, since the only
        permutation of 1 character is itself

    Complexity:
        Time  -> O():
        Space -> O():
    """

  # base case
    if len(string) <= 1:
        return set([string])

    all_chars_except_last = string[:-1]
    last_char = string[-1]

    # recursive call: get all possible permutations for all chars except last
    permutations_of_all_chars_except_last = get_permutations(all_chars_except_last)
    print permutations_of_all_chars_except_last

    # put the last char in all possible positions for each of the above permutations
    permutations = set()
    for permutation_of_all_chars_except_last in permutations_of_all_chars_except_last:
        for position in range(len(all_chars_except_last) + 1):
            permutation = permutation_of_all_chars_except_last[:position] + last_char + permutation_of_all_chars_except_last[position:]
            permutations.add(permutation)

    return permutations


if __name__ == "__main__":
    s = "abc"
    print permute(s)        # abc, acb, bac, bca, cab, cba
    print get_permutations(s)

