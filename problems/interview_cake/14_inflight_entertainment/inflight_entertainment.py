#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Since we know the flight length, we can subtract each movie_length from the
flight_length to get the length of the required movie to fit, then check if that
exists (we can store everything in a hashmap)
"""

def two_movies_in_flight_length(flight_length, movie_lengths):
    """ Return True or False if there are two numbers in movie_lengths whose sum
    equals flight_length

    Args:
        flight_length (int): length of the flight in minutes
        movie_lengths (list of ints): list of movie lengths
    Returns:
        True if two movie_lengths in flight_length, False otherwise

    Runtime:
        Time  -> O(n): Iterate the list twice
        Space -> O(n): Store all lengths in a hashmap
    """
    # Store all n values Space-> O(n)
    # iterate the list once
    movie_length_map = {}
    for movie_length in movie_lengths:
        movie_length_map[movie_length] = 0

    for movie_length in movie_lengths:
        next_movie_length = flight_length - movie_length
        if next_movie_length in movie_length_map:
            # debug
            print movie_length, next_movie_length
            return True

    return False


if __name__ == "__main__":
    flight_length = 60    # flight length in minutes
    movie_lengths = [10, 20, 30, 40, 50, 60, 5, 15, 25, 35, 45, 55] # in minutes
    print two_movies_in_flight_length(flight_length, movie_lengths)

