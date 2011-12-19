'''
Created on Dec 14, 2011

@author: andrewkittredge
'''

import math
from exponentiation import fast_exponentiation
from euclidean_algo import extended_euclidean_algorithm



def discrete_log(prime, public_key, primitive_root):
    m = int(math.floor((prime - 1) ** .5))
    base_exponents = {}
    for j in xrange(0, m):
        base_exponents[fast_exponentiation(primitive_root, j, prime)] = j
    
    inverse_b = extended_euclidean_algorithm(primitive_root, prime) % prime
    c = fast_exponentiation(inverse_b, m, prime)
    x = public_key
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
        self.assertEqual(237, discrete_log(1009, 482, 101))
        self.assertEqual(2397011, discrete_log(prime=6876731,
                                               public_key=3523346,
                                               primitive_root=3422))
        
if __name__ == '__main__':
    unittest.main()