#!/usr/bin/python3
""" A module that implememt heap data structure"""

import heapq

heap = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
heapq.heapify(heap)
print(heap)

print(type(heap))