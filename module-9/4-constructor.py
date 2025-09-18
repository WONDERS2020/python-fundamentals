#/usr/bin/python3
""" A module tha make use of a constructor to assign values"""

class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age
    def greet(self):
        print("Good Morning {}".format(self.name))

if __name__ == '__main__':
    person = Person("Joshua", 29)
    person.name = "Abidal"
    person.greet()