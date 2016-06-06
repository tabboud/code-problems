#!/usr/bin/env python
# -*- coding: utf-8 -*-

class TempTracker(object):
    def __init__(self):
        self.temps = {}
        self.max_temp = None
        self.min_temp = None
        self.sum_of_temps = 0.0
        self.num_of_temps = 0

    def insert(self, new_temp):
        """ Record a new temperature """
        # check if temperature exists
        if new_temp not in self.temps:
            self.temps[new_temp] = 1
        else:
            self.temps[new_temp] += 1

        self.sum_of_temps += new_temp
        self.num_of_temps += 1
        self.max_temp = max(self.max_temp, new_temp)
        if self.min_temp is None:
            self.min_temp = new_temp
        else:
            self.min_temp = min(self.min_temp, new_temp)


    def get_max(self):
        """ Return the highest temp we've seen so far """
        return self.max_temp

    def get_min(self):
        """ return the lowest temp we've seen so far """
        return self.min_temp

    def get_mean(self):
        """ return the mean of all temps seen so far """
        # returns a float
        return self.sum_of_temps / self.num_of_temps

    def get_mode(self):
        """ Return the mode of all temps seen so far """
        modes = max(zip(self.temps.values(), self.temps.keys()))
        return modes[1]


if __name__ == "__main__":
    tracker = TempTracker()
    tracker.insert(1)
    tracker.insert(10)
    tracker.insert(5)
    tracker.insert(31)
    tracker.insert(10)

    print tracker.get_max()
    print tracker.get_min()
    print tracker.get_mean()
    print tracker.get_mode()

