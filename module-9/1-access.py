#/usr/bin/python3
""" A module that access the attribute of a class"""

class Person:
    """ A class that has a public attribute
    name
    age
    """
    name = "Wonders"
    age = 29

if __name__ == '__main__':
    person = Person()
    print(person.name)
    print(person.age)