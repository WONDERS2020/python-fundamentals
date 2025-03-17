#/usr/bin/python3
for num in range (1, 51): 
    if num % 3 == 0 and num % 5 ==0:
        print("FizzBuzz", end=" ")
    elif num % 5 == 0:
        print("Buzz", end=" ")
    elif num % 3 == 0: 
        print("Fizz", end=" ")
    else:
        print(num, end=" ")