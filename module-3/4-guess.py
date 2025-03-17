#/usr/bin/python3
import random 

guess = random.randint(1, 20)

while True:
    num = int(input("Enter num:" ))
    if num == guess:
        print("Congratulations, You Guess It!")
        exit(0)
    elif num > guess:
        print("Too High, Try Again")
    else:
        print("Too Low, Try Again!")