#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Find index of matching parens
"""
def find_matching_parens(sentence, start):
    """ Find the index of the matching parenthesis

    Complexity:
        Time  -> O(n): Iterate the list once
        Space -> O(1): No extra space needed
    """
    open_cnt = 1

    for index, ch in enumerate(sentence[start+1:]):
        if ch == "(":
            open_cnt += 1
        elif ch == ")":
            if open_cnt == 1:
                return index + start + 1
            else:
                open_cnt -= 1

    return start


def find_matching_parens_stack(sentence, start):
    """ Find the index of the matching parenthesis

    Complexity:
        Time  -> O(n): Iterate the list once
        Space -> O(n): Store n values in a stack
    """
    stack = []

    # push on the first parenthesis
    stack.append(sentence[start])
    for index, ch in enumerate(sentence[start+1:]):
        if ch == "(":
            stack.append(ch)
        elif ch == ")":
            stack.pop()
            if len(stack) == 0:
                # the index is offset by the start position
                return index + start + 1
                
    return start


if __name__ == "__main__":
    s = "Sometimes (when I nest them (my parentheticals) too much (like this (and this))) they get confusing."
    print find_matching_parens_stack(s, 10)
    print find_matching_parens(s, 10)
