#/usr/bin/python3
""" Main for calculator"""
add = __import__("cal").add
sub = __import__("cal").sub
mul = __import__("cal").mul
div = __import__("cal").div

operators = {
    "+" : add,
    "-" : sub,
    "*" : mul,
    "/" : div,
}
num1 = float(input("enter any number of your choice"))
num2 = float(input("Enter any number of your choice"))


op = input("Enter the operator of your choice")
if op not in operators:
    print ("Invalid Operation, Try Again")
    exit(1)

for key, value in operators.items():
    if op == key:
        result = operators.get(op)(num1, num2)
        print(result)
        break