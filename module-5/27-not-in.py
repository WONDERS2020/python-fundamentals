#/usr/bin/python3
""" A module that check for membership test on a dictionry"""

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
print("color" not in laptop)
print("probook" not in laptop)
print("age" not in laptop)