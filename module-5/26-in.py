#/usr/bin/python3
""" A module that performs membership test on a dictionary"""
laptop = dict(
    brand = "HP",
    model = "probook",
    year = 2023,
    price =  250000,
    color = "silver",
    processor = "intel core i5",
    ram = 8,
    storage = 512,
    cpu =  "core",
    battery =  "double cell",
)
print("color" in laptop)
print("probook" in laptop)
print("age" in laptop)