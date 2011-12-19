import random
from miller_rabin import check_primality_miller_rabin
from itertools import islice, count

def prime_factorization(n):
    prime_factors = set()
    for i in infinite_range(2, n):
        while n % i == 0:
            prime_factors.add(i)
            n = n / i
    return list(prime_factors)

def infinite_range(start, end):
    val = start
    while val <= start:
        yield val
        val += 1

def gcd(x, y):
    '''x and y are integers.'''
    smaller, larger = sorted((x, y))
    dividend = larger
    modulus = smaller
    remainder = True
    while remainder:
        remainder = dividend % modulus 
        dividend = modulus
        modulus = remainder
    return dividend


def large_random_prime(lower_bound = 1e15, upper_bound=1e20):
    candidate = max(random.randint(lower_bound, upper_bound), 2)
    while not check_primality_miller_rabin(candidate):
        candidate = max(random.randint(lower_bound, upper_bound), 2)
    return candidate

import unittest
class TestLargeRandomPrime(unittest.TestCase):
    def test_large_random_prime(self):
        print large_random_prime(1, 100)