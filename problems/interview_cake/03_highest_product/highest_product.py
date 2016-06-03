#!/usr/bin/env python
# -*- coding: utf-8 -*-

def highest_product_of_3_brute(list_of_ints):
    """ Find the highest product of 3 integers in an array
    Args:
    Returns:

    Runtime:
        Time  -> O(n^3)
        Space -> O()
    """
    highest_product = 1
    for i, elem1 in enumerate(list_of_ints[0:-2]):
        for j, elem2 in enumerate(list_of_ints[i+1:-1]):
            for k, elem3 in enumerate(list_of_ints[j+1:]):
                    highest_product = max(highest_product, elem1*elem2*elem3)

    return highest_product


def highest_product_greedy(arr):
    """ Return the highest product by using a greedy algorithm

    Runtime:
        Time  -> O(n): Traverse the list in 1 pass
        Space -> O(1):
    """
    highest = max(arr[0], arr[1])
    lowest = min(arr[0], arr[1])
    highest_product_of_two = arr[0] * arr[1]
    lowest_product_of_two = arr[0] * arr[1]
    highest_product_of_three = arr[0] * arr[1] * arr[2]

    for num in arr[2:]:
        # update highest product of three
        highest_product_of_three = max(highest_product_of_three, highest_product_of_two*num, lowest_product_of_two*num)

        # update highest and lowest product of two
        highest_product_of_two = max(highest_product_of_two, highest*num, lowest*num)
        lowest_product_of_two = min(lowest_product_of_two, highest*num, lowest*num)

        # update the highest and lowest value
        highest = max(highest, num)
        lowest = min(lowest, num)

    return highest_product_of_three


if __name__ == "__main__":
    arr = [4,1,2,3]   # 24
    arr2 = [-10, -10, 1, 12, 10]   # 1200
    arr3 = [1, 10, -5, 1, -100]    # 5000
    list_of_ints = [-10,-10,1,3,2] # 300

    print(highest_product_greedy(arr))
    print "---"
    print(highest_product_greedy(arr2))
    print "---"
    print(highest_product_greedy(arr3))
    print "---"
    print(highest_product_greedy(list_of_ints))

