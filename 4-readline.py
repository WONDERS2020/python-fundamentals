#!/usr/bin/python3
""" A program that can read line"""
with open("newfile.txt", "r") as f:
    for line in f.readlines():
        print(line)