#!/usr/bin/python3
""" A module that extract sate DD-MM-YY format"""
import re

pattern = r"\b\d{2}-\d{2}-\d{4}\b"
text = "Today's date is 23-08-2025 and tomorow is 24-08-2025"

dates = re.findall(pattern, text)
print(dates)