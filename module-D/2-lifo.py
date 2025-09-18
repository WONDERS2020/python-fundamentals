#!/usr/bin/python3
""" A module that opearte on the last in first in principle"""
from queue import LifoQueue
stack = LifoQueue()
stack.put("a")
stack.put("b")
stack.put("c")
print(stack)
print(stack.get())