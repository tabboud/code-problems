#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Single Riffle Check
"""

def single_riffle(shuffled_cards, half1, half2):
    """ Check if shuffled cards is a single riffle of half1 and half2

    Complexity:
        Time  -> O(n): iterate through the cards once
        Space -> O(1): no extra space is used
    """
    # look at the first card in shuffled_cards, it must be one of half1 or half2
    # then increment the cooresponding pointer
    half1_index = 0
    half2_index = 0
    for card in shuffled_cards:
        if half1_index < len(half1) and card == half1[half1_index]:
            half1_index += 1
        elif half2_index < len(half2) and card == half2[half2_index]:
            half2_index += 1
        else:
            return False

    return True


if __name__ == "__main__":
    # valid single riffle since they alternate
    shuffled_cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    half1 = [1, 3, 5, 7, 9]
    half2 = [2, 4, 6, 8, 10]
    print single_riffle(shuffled_cards, half1, half2)

    # valid single riffle since they alternate
    shuffled_cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    half1 = [1, 2, 3, 4, 5]
    half2 = [6, 7, 8, 9, 10]
    print single_riffle(shuffled_cards, half1, half2)

    # INVALID single riffle since the cards don't follow the pattern
    shuffled_cards = [1, 10, 9, 8, 7, 2, 3, 4, 5, 6]
    half1 = [1, 2, 3, 4, 5]
    half2 = [6, 7, 8, 9, 10]
    print single_riffle(shuffled_cards, half1, half2)
