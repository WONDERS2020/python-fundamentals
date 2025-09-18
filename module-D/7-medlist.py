#!/usr/bin/python3
""" A module that prints the topm3 finisher in women 100metres olypic race"""

import heapq
result = ["Christiana williams 11.0", "Mark Wonders 10.86", "Henry Wonders 10.71", "Alice Wonders 10.60",
"Shelly Ann 10.50", "English 10.94", "michelle 10.92", "Define 10.90"]
top3 = heapq.nsmallest(3, result, key = lambda x: float(x.split()[-1]))
print(top3)