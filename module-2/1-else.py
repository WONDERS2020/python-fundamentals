#/usr/bin/python3
""" A program that takes the age of the person and displays double of that age if its greater than 18 otherwise display the age"""
age = int(input("Enter your age"))
if age >= 18:
    print(age * 2)
else:
    print(age)
    