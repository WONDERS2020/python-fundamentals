#!/usr/bin/python3
""" A module that fine alphabet"""
import re

pattern = r"[a-zA-Z]+"
text = "Hello World 123"
match = re.search(pattern, text)

if match:
    print("Found an alphabet:", match.group())
