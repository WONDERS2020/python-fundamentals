#/usr/bin/python3
""" A module that handle exception"""
try:
    with open("file.txt", "r") as f:
        print(f.read())
except Exception as e:
        print("File Not Found!")