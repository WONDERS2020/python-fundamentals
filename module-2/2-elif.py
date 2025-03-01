#/usr/bin/python3
""" A program in python that can differenciate between even and odd values"""
num = int(input("Enter any number: "))
if num % 2 == 1:
    print("this is odd my guy")
elif num % 2 == 0:
    print("this is even my guy")
else:
    print("undefined")