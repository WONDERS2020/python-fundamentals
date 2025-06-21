#!/usr/bin/python3
""" A program to Append add ainformation to a file """
with open("newfile.txt", "a+") as f:
    f.write("\n The informtion inside this documents is" \
    " classified, you can only see this when you are" \
    " taking a python course")