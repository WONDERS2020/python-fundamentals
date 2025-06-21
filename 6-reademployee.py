#!/usr/bin/python3
""" import csv
with open("Employee.csv", "r") as csvfile:
    reader = csv.reader(csvfile, delimiter=",")
    for row in reader:
        if "Bachelors" in row:
            print(" ".join(row))
            
            """

"""
import csv
with open("Employee.csv", "r") as csvfile:
    reader = csv.reader(csvfile, delimiter=",")
    for row in reader:
        if "Masters" in row:
            print(" ".join(row))
            
            """

import csv
with open("Employee.csv", "r") as csvfile:
    reader = csv.reader(csvfile, delimiter=",")
    for row in reader:
        if "PHD" in row:
            print(" ".join(row))