#/usr/bin/python3
""" A program that ask a user for a number"""

num = int(input("Enter number: "))
if num % 2 == 0 and num % 5 == 0:    
    print("the number is even and divisible by 5")
elif num % 2 == 1 and num % 3 == 0:
    print("the number is odd and divisible by 3")
else:
    print("the number does not meet any condition")