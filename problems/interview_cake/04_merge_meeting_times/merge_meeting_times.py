#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Algorithm:
1. Sort the meeting times in increasing order
2. if the next start time <= current end time, then we need to condense, otherwise
    they can remain separate
3. Check the next end time to see if it ends before or after the current end time
"""

def condense_meeting_times_sorted(meetings):
    """ Return a list of condensed meeting times
    Args:
        meetings: List of meeting time ranges (list of tuples)
    Returns:
        List of condensed meeting times

    Runtime:
        Time  -> O(nlogn): Sort the meetings by start time
        Space -> O(n): Use extra space for the new list
    """
    if len(meetings) < 2:
        raise Exception("Need atleast 2 meetings")

    # sort the meetings by start time in O(nlogn) time
    meetings = sorted(meetings)
    condensed_meetings = []

    start = meetings[0][0]
    end = meetings[0][1]

    # merge meetings as we go
    for next_start, next_end in meetings[1:]:
        # implement the same algorithm used to merge two meetings

        if next_start <= end:
            # next meeting starts before the end of the first, but ends after
            # so merge and use the next_end time
            if next_end > end:
                end = next_end
        else:
            # push the current start, end combo
            condensed_meetings.append((start, end))
            # update start and end
            start = next_start
            end = next_end

    # push last element
    condensed_meetings.append((start, end))
    return condensed_meetings




if __name__ == "__main__":
    meetings = [(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)]    # [(0, 1), (3, 8), (9, 12)]
    print condense_meeting_times_sorted(meetings)

    meetings = [(1, 2), (2, 3)]    # [(1, 3)]
    print condense_meeting_times_sorted(meetings)

    meetings = [(1, 5), (2, 3)]    # [(1, 5)]
    print condense_meeting_times_sorted(meetings)

    meetings = [(1, 10), (2, 6), (3, 5), (7, 9)]    # [(1, 10)]
    print condense_meeting_times_sorted(meetings)
