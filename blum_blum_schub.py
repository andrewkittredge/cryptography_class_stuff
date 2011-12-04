'''
Created on Dec 3, 2011

@author: andrewkittredge
'''
from utils import prime_factorization
import random

p, q = 103, 107

def blum_blum_shub(p, q):
    assert p % 4 == 3 and q % 4 == 3
    n = p * q
    possible_seeds = prime_factorization(n)
    seed = random.choice(possible_seeds)
    seeds = seed_generator(seed, n)
    for s in seeds:
        yield s % 2
    
def seed_generator(s, n):
    while True:
        ss = s ** 2 % n
        yield ss
        s = ss

from itertools import islice
import unittest
class Tester(unittest.TestCase):
    def test_blum_blum_shub(self):
        print '\n'.join(map(str, islice(blum_blum_shub(p, q), 100)))

if __name__ == '__main__':
    unittest.main()