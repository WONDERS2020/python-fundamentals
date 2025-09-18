#!/usr/bin/python3
""" A module that uses python collection as the stack """
from collections import deque
mystack = deque()

mystack.append("a")
mystack.append("b")
mystack.append("c")
print(mystack)