#!/usr/bin/python3
""" A module that validate a simple email address"""
import re

pattern = r"^\w+@\w+\.\w{2,}$"
text = "user@example.com"

if re.match(pattern, text):
    print("Valid email format")
else:
    print("Invalid email format")