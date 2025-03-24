#/usr/bin/python3
sum_of_evens = 0
for number in range(1, 101):
    if number % 2 == 0:
        sum_of_evens += number 
print("The sum of even numbers between 1 and 100 is:", sum_of_evens)
