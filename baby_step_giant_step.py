'''
Created on Dec 14, 2011

@author: andrewkittredge
'''

import math
from exponentiation import fast_exponentiation
from euclidean_algo import extended_euclidean_algorithm

def discrete_log(prime, a, b):
    m = int(math.floor((prime - 1) ** .5))
    base_exponents = {}
    for j in xrange(0, m):
        base_exponents[fast_exponentiation(b, j, prime)] = j
    
    inverse_b = extended_euclidean_algorithm(b, prime) % prime
    c = fast_exponentiation(inverse_b, m, prime)
    x = a
    for i in xrange(0, m):
        if x in base_exponents:
            return (m * i) + base_exponents[x] 
        else:
            x = (x * c) % prime

import unittest
class BabyStepGiantStepTester(unittest.TestCase):
    def test_dicrete_log(self):
        self.assertEqual(5, discrete_log(29, 3, 2))
        self.assertEqual(69, discrete_log(101, 3, 2))
        
if __name__ == '__main__':
    unittest.main()