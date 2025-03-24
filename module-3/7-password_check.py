#/usr/bin/python3
""" A program that ask a user for password at least 8 characters etc"""
import re

def is_valid_password(password):
    if len(password) < 8:
        return False
    if not re.search(r'\d', password):
        return False
    if not re.search(r'[A-Z]', password):
        return False
    if not re.search(r'[a-z]', password):
        return False
    return True

while True:
    user_password = input("Please enter a password: ")
    if is_valid_password(user_password):
        print("Correct Password!")
        break
    else:
        print("Password is invalid. It must meet the following criteria:")
        print("- At least 8 characters long")
        print("- Contain at least one digit")
        print("- Contain at least one uppercase letter")
        print("- Contain at least one lowercase letter")
        print("- Contain at least one special character")
    pass