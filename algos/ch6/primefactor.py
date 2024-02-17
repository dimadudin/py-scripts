import math


def prime_factors(n):
    res = []
    while n % 2 == 0:
        n /= 2
        res.append(2)
    max_prime = math.floor(math.sqrt(n))
    for i in range(3, max_prime + 1, 2):
        while n % i == 0:
            n /= i
            res.append(i)
    if n > 2:
        res.append(n)
    return res
