#/usr/bin/python3
""" A program that prompts the user to enter their age and 
checks if they are eligible to vote (age >= 18)."""

age_input = input("Please enter your age: ")

try:
    age = int(age_input)
   
    if age >= 18:
        print("You can vote!")
    elif age >= 0:
        print("Sorry, you're not eligible to vote yet.")
    else:
        print("Age can't be negative.")
except ValueError:
    print("Invalid input. Please enter a valid number.")