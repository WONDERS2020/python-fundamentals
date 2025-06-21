#/usr/bin/python3
""" A program that can read a file"""
with open("newfile.txt", "r") as f:
    a = f.read()
    print(a)