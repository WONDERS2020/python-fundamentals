#/usr/bin/python3
""" Write a function that retrievs an element from a list"""

def element_at(my_list, idx):
    if idx < 0:
        return None
    if idx > len(my_list):
        return my_list[idx]
    
    cars = ["Venza", "Tesla", "Cyber truck", "Ferrari", "Lamghogini"]
    result = element_at(cars, 3)
    print(result)