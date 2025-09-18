#!/usr/bin/python3

""" A module that explains decorators with arguments"""

def decorator(func):

    def wrapper(*args, **kwargs):
        print("Before the function call")
        func(*args, **kwargs)
        print("After the function call")

    return wrapper

@decorator
def greet(name):
    print(f"Hello, {name}!")

if __name__ == '__main__':
    greet("Alice, Wonders")