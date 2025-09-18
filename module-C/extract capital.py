#!/usr/bin/python3

import re

text = "Alice went to Wonderland with Bob and Charlie."
capitalized_words = re.findall(r'\b[A-Z][a-zA-Z]*\b', text)
print(capitalized_words)
