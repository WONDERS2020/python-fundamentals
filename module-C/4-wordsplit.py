#!/usr/bin/python3
""" A moodule that splits a sentence nti words"""
import re

pattern = r"\b\w+\b"
text = "hello, word! How are you?"

words = re.findall(pattern, text)
print(words)
