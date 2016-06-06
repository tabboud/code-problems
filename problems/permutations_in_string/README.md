# Permutations In String

Given two strings, s1 and s2, where the length of s1 > s2. Write a function to
determine how many permutations of s2 exist in s1.

** This was one of Gayle Laakmann McDowell's favorite interview questions (Found
on HackerRank Live: AMA)

```python
s1 = "abcdecabxabc" 
s2 = "abc"          #Permutations: abc, acb, bac, bca, cab, cba

print count_permutations(s1, s2)    # 2 -> abc, cab
```

