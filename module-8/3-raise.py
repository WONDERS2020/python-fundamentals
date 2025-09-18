#/usr/bin/python3
""" A module that divide two numbers"""
try:
    number1 = int(input("Enter a number : "))
    number2 = int(input("Enter a number : "))
    if number2 == 0:
        raise ZeroDivisionError("Number cannot be divided by zero")
    a = number1/number2
    print(a)
except Exception as e:
    print(e)