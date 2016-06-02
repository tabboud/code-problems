#!/usr/bin/env python
# -*- coding: utf-8 -*-

def get_all_products_brute(arr):
    """
    Brute Force
        Go through all values and skip the current index
    Runtime:
        Time -> O(n^2)
    """
    products = []
    arr_len = len(arr)

    for i in range(0,arr_len):
        product = 1
        for j in range(0,arr_len):
            if j == i:
                continue
            product *= arr[j]
        products.append(product)

    return products


def get_all_products(arr):
    """
    Get all products of numbers prior to index
    Then compute the products of all numbers after index

    Ex.
        input_int_array       -> [1, 7, 3, 4]
        products_before_index -> [ 1,  1, 7, 21]
        products_after_index  -> [84, 12, 4,  1]
        products              -> [84, 12, 28, 21]

    Runtime:
        Time  -> O(n): Iterate through the list twice
        Space -> O(n): Construct 1 extra list
    """
    arr_len = len(arr)
    products_before_index = [1] * arr_len
    products_after_index = [1] * arr_len

    # Generate all products before index
    for i in range(1, arr_len):
        products_before_index[i] = products_before_index[i-1] * arr[i-1]

    #NOTE: We can save some space by performing the multiplication with products_before_index here
    # Generate all products after index
    #for i in range(arr_len-2, -1, -1):
        #products_after_index[i] = products_after_index[i+1] * arr[i+1]

    # Multiply the two elements in the list
    #return [x*y for x, y in zip(products_before_index, products_after_index)]
    #ENDNOTE

    # Alternative without using an extra list
    prev_product = 1
    for i in range(arr_len-2, -1, -1):
        next_product = prev_product * arr[i+1]
        prev_product = next_product
        products_before_index[i] *= next_product
    return products_before_index


if __name__ == "__main__":
    ints = [1, 7, 3, 4]
    print get_all_products(ints)
    print get_all_products_brute(ints)
