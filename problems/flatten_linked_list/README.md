# Flatten a Linked List

Given a linked list, in addition to the next pointer, each node has a child pointer that can point to a separate list. With the head node, flatten the list to a single-level linked list.

Example:
```python
# Given this linked list structure
#    1 -> 2 -> 3 -> 4
#         |         |
#         5 -> 6    7
#         |         |
#         8         9

flatten_linked_list(root)

# should modify the list to be...

# 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9
```
