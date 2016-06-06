#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
An example of the unbounded knapsack problem
"""

def max_duffel_bag_value_sorting(cake_tuples, capacity):
    """
    Find the maximum monetary value that the duffel bag can hold
    """
    if capacity <= 0:
        return 0

    # Get a value/weight ratio for each cake (ratio, list_index)
    cake_tuple_ratios = [(value/weight, i) for i, (weight, value) in
            enumerate(cake_tuples) if weight > 0]

    # sort the ratios in reverse (highest to lowest ratio)
    # O(nlogn) to sort
    cake_tuple_ratios = sorted(cake_tuple_ratios, reverse=True)

    # put in as many cakes with the highest value/weight ratio until we hit our
    # weight limit, then move to the next
    cur_weight = 0
    total_value = 0
    ratio_index = 0

    while cur_weight <= capacity and ratio_index < len(cake_tuple_ratios):
        # try adding this cake
        index = cake_tuple_ratios[ratio_index][1]
        if cur_weight + cake_tuples[index][0] > capacity:
            # don't add this one, increment ratio_index
            ratio_index += 1
        else:
            # its okay to add this cake
            cur_weight += cake_tuples[index][0]
            total_value += cake_tuples[index][1]

    return total_value


def max_duffel_bag_value(cake_tuples, weight_capacity):
    """
    Dynamic Programming solution

    Complexity:
        Time  -> O(n*k): where n is the number of types of cake
                               k is the capacity of the bag
                        We loop through each cake (n cakes) for every capacity
                        (k capacities)
        Space -> O(k): List of k capacities
    """
# we make a list to hold the maximum possible value at every
# duffel bag weight capacity from 0 to weight_capacity
# starting each index with value 0
    max_values_at_capacities = [0] * (weight_capacity + 1)

    for current_capacity in xrange(weight_capacity + 1):

      # set a variable to hold the max monetary value so far for current_capacity
      current_max_value = 0

      for cake_weight, cake_value in cake_tuples:

          # if a cake weighs 0 and has a positive value the value of our duffel bag is infinite!
          if (cake_weight == 0 and cake_value != 0):
              return float('inf')

          # if the current cake weighs as much or less than the current weight capacity
          # it's possible taking the cake would give get a better value
          if (cake_weight <= current_capacity):

              # so we check: should we use the cake or not?
              # if we use the cake, the most kilograms we can include in addition to the cake
              # we're adding is the current capacity minus the cake's weight. we find the max
              # value at that integer capacity in our list max_values_at_capacities
              max_value_using_cake = cake_value + max_values_at_capacities[current_capacity - cake_weight]

              # now we see if it's worth taking the cake. how does the
              # value with the cake compare to the current_max_value?
              current_max_value = max(max_value_using_cake, current_max_value)

      # add each capacity's max value to our list so we can use them
      # when calculating all the remaining capacities
      max_values_at_capacities[current_capacity] = current_max_value

    return max_values_at_capacities[weight_capacity]

if __name__ == "__main__":
    cake_tuples = [(7, 160), (3, 90), (2, 15)]
    capacity = 20
    print max_duffel_bag_value(cake_tuples, capacity)  # 555 (6 of the middle type and 1 of the last type)

    cake_tuples = [(0,30), (50, 200)]
    capacity = 100
    print max_duffel_bag_value(cake_tuples, capacity)    # 3000

    cake_tuples = [(3,40), (5, 70)]
    capacity = 9
    print max_duffel_bag_value(cake_tuples, capacity)    # 3000

