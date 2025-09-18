#!/usr/bin/python3
""" A module on how to create a queue"""
import queue


task = queue.Queue()
task.put("task1")
task.put("task2")
print(task.get())
