#!/usr/bin/python3

import re

text = "This is is a test test sentence."
# Regex to match repeated consecutive words
pattern = r'\b(\w+)\s+\1\b'
repeated_words = re.findall(pattern, text)
print("Repeated words:", repeated_words)
# Highlight repeated words
highlighted = re.sub(pattern, r'[\1 \1]', text)
print("Highlighted text:", highlighted)