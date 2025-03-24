#/usr/bin/python3
""" A program that takes a person's age as input"""

age = int(input("Enter your age: "))
if age < 13:    
    print("you are a child")
elif age >= 13 <=19:
    print("You are a teenager")
else:
    print("You are an adult")