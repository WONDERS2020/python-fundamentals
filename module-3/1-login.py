#/usr/bin/python3
""" A program that ask the user for username and password"""

username = input("Enter Username: ")
password = input("Enter Password: ")
if username == "admin" and password == "12345":
    print("login successful")
else:
    print("Invalid Credentials")