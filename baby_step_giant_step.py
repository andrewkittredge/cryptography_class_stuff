'''
Created on Dec 14, 2011

@author: andrewkittredge
'''

import math
from exponentiation import fast_exponentiation
from euclidean_algo import extended_euclidean_algorithm

def discrete_log(prime, base, b):
    m = int(math.floor((prime - 1) ** .5))
    base_exponents = {}
    for j in xrange(0, m):
        base_exponents[fast_exponentiation(base, j, prime)] = j
    
    _, inverse_b = extended_euclidean_algorithm(b, prime)
    c = fast_exponentiation(b, -m, prime)
    x = base
    for i in xrange(0, m):
        if x in base_exponents:
            return (m * i) + base_exponents[i] 
        else:
            x = x * c

import unittest
class BabyStepGiantStepTester(unittest.TestCase):
    def test_dicrete_log(self):
        self.assertEqual(5, discrete_log(29, 2, 3))
        self.assertEqual(69, discrete_log(101, 2, 3))
        
if __name__ == '__main__':
    unittest.main()