#!/usr/bin/python3
""" A module that delete an element in a queue"""
from collections import deque
my_queue = deque([1, 2, 3, 4, 5])
remove_elemet = my_queue.popleft()
print(remove_elemet)