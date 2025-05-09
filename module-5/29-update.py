#/usr/bin/python3
""" A module that update the value of a dictionary"""

laptop = {
    "brand": "HP",
    "model": "probooh",
    "year": 2023,
    "price":  250000,
    "color": "silver",
    "processor": "intel core i5",
    "ram": 8,
    "storage": 512,
    "cpu": "core",
    "battery": "double cell",
    
}

laptop.update({"price": 1500000.00})
laptop.update({"size": "14 inches"})
print(laptop)
