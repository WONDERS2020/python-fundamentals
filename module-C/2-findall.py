#!/usr/bin/python3
""" A module that extract all the digits from a string"""
import re

pattern = r"\d+"
text = "my number is 12345 and my zip is 67890"
matches = re.findall(pattern, text)
if matches:
    print("Found digits:", matches)