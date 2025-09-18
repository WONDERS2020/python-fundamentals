#/usr/bin/python3
""" A module that can erite information in the public attribute"""

class Person:
    name = ""
    age = 30

if __name__ == '__main__':
    person = Person()
    person.name = "Joseph"
    person.age = 29

    print(person.name, person.age)