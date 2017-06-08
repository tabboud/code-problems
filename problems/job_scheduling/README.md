# Job Scheduling

Given a list of jobs and associated time intervals in which they run:

```python
    jobs = {
            'A': [(1,3), (6,9)],
            'B': [(2,4),(7,8)],
            'C': [(10,15)]
            }
```

Write a function to print what jobs are running at the same time:

```python
1,2: A
2,3: A,B
3,4: B
6,7: A
7,8: A,B
8,9: A
10,15: C
```
