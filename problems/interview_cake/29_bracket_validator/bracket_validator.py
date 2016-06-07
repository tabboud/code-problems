#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Bracket Validator
"""
def bracket_validator(brackets):
    """ Validate a string of brackets

    Complexity:
        Time  -> O(n): Iterate the list once
        Space -> O(n): Use a stack
    """
    openers = ['(', '{', '[']
    closers = [')', '}', ']']
    bracket_map = {
        '(' : ')',
        '{' : '}',
        '[' : ']'
    }
    stk = []

    for bracket in brackets:
        if bracket in openers:
            stk.append(bracket)
        elif bracket in closers:
            latest_bracket = stk.pop()
            if bracket_map[latest_bracket] != bracket:
                return False

    return len(stk) == 0


if __name__ == "__main__":
    a = "{[]()}"  # True
    b = "{[(])}"  # False
    c = "{[}"     # False

    print bracket_validator(a)
    print bracket_validator(b)
    print bracket_validator(c)

