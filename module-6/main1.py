#/usr/bin/python3
""" Main Entry of the calculator"""
import sys
from cal import add
from cal import sub
from cal import mul
from cal import div




operators = {
    "+" : add,
    "-" : sub,
    "x" : mul,
    "//" : div,
}

if len (sys.argv) !=4:
    print("Incomplete Argument")
    exit(1)

num1 = float (sys.argv[1])
num2 = float (sys.argv[3])

op = (sys.argv[2])
if op not in operators:
    print("Invalid Operators")
    exit(1)

for key, value in operators.items():
    if op == key:
            result = operators.get(op)(num1, num2)
            print(result)
            break