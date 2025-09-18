#!/usr/bin/python3

import re

text = "<div><p>Hello</p><a href='#'>Link</a></div>"
# Regex to find all HTML tags
tags = re.findall(r'<[^>]+>', text)
print(tags)
