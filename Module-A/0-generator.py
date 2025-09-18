#!/usr/bin/python3
""" A module that gnerates a numer between 1 and 5"""

def generate_number(start, end):
    """ a fuction that generate a numer between start and end"""
    while start <= end:
        yield start
        start +=1
    return start
    

if __name__ == "__main__":
    """ main function to test the number generator"""
    print(list(generate_number(1, 5)))
    # for number in generate_number(1, 5):
     #   print(number)