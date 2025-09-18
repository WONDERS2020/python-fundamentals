#/usr/bin/python3
""" A module that adds a method to a class"""

class Person:
    name = ""
    age = 0

    def greet(self):
        print("Good Morning {}".format(self.name))

if __name__ == "__main__":
    person = Person()
    person.name = "Joshua"

    person.greet()