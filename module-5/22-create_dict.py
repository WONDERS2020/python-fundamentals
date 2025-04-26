#/usr/bin/python3
""" A file that create a dictionary of items"""
wonders = {
    "names": ['Henry', 'Rashnotech', 'Ayomide', 'Micheal', 'Moses'],
    "cars": ['Ferari', 'Venza', 'Toyota', 'Tesla', 'Benz']
}
print(wonders)
print(wonders.get('names'))
print(wonders.get('cars')[1])