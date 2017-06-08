#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Given:
    A : [(1,3), (6,9)]
    B : [(2,4), (7,8)]
    C : [(10,15)]

Write a function to print what jobs are running
At the time steps
1,2: A
2,3: A,B
3,4: B
6,7: A
7,8: A,B
8,9: A
10,15: C
"""
from collections import namedtuple

Job = namedtuple('Job', ['time', 'job_name'])


def get_job_times(d):
    if d == {}:
        raise Exception("No jobs to schedule!")

    jobs = []
    # Flatten the dict
    for job, times in d.iteritems():
        for time in times:
            # create start and end time tuples
            jobs.append(Job(time[0], job))
            jobs.append(Job(time[1], job))

    # sort by start time
    jobs = sorted(jobs, key=lambda x: x.time)

    # Keeps track of running jobs
    running_jobs = {}
    # start time is ordered, so lets start at the first one
    start_time = jobs[0].time

    for job in jobs:
        # Check if any other jobs are running first
        if running_jobs.keys() != []:
            end_time = job.time
            print "%d,%d: %s" % (start_time, end_time, ','.join(running_jobs.keys()))
            start_time = end_time
            if job.job_name not in running_jobs:
                # add the job
                running_jobs[job.job_name] = job
            else:
                # end my job
                del running_jobs[job.job_name]
        else:
            # no jobs, so always a start
            start_time = job.time
            running_jobs[job.job_name] = job
         


if __name__ == '__main__':
    jobs = {
            'A': [(1,3), (6,9)],
            'B': [(2,4),(7,8)],
            'C': [(10,15)]
            }

    expected_output = """
                        1,2: A
                        2,3: A,B
                        3,4: B
                        6,7: A
                        7,8: A,B
                        8,9: A
                        10,15: C
                        """


    get_job_times(data)

    print "========"

    data = {
            'A': [(18,22), (25,28)],
            'B': [(20,26)],
            'C': [(27,30)]
            }
    expected_output = """
                        18,20: A
                        20,22: A,B
                        22,25: B
                        25,26: A,B
                        26,27: A
                        27,28: A,C
                        28,30: C
                        """
    get_job_times(data)

