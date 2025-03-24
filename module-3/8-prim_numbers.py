#/usr/bin/python3
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def find_factors(n):
    factors = []
    for i in range(1, n + 1):
        if n % i == 0:
            factors.append(i)
    return factors

for num in range(1, 51):
    if is_prime(num):
        print(f"{num} is prime and has no factors other than 1 and itself.")
    else:
        factors = find_factors(num)
        print(f"{num} is not prime and its factors are: {factors}")