#/usr/bin/python3
num1 = float(input ("enter the first number: "))
num2 = float(input ("enter the second number: "))
op = input("Enter your operator: ")

if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "*":
    print(num1 * num2)
elif op == "/":
    print(num1 / num2)
else:
    print("undefined operator")