'''
Created on Dec 16, 2011

@author: andrewkittredge
'''

from euclidean_algo import euclidean_algo


    

def pollards_rho(n):
    f = lambda x : (x ** 2 + 1) % n
    x = 2
    y = 2
    g = 1
    while not 1 < g < n:
        print (x - y) % n
        if g == 1:
            x = f(x)
            y = f(f(y))
        elif g == n:
            raise Exception('failure, reinitialize.')
        g = euclidean_algo(abs(x - y), n)
    return g

import unittest
class FactoriztionTester(unittest.TestCase):
    def test_pollards_rho(self):
        self.assertEqual(pollards_rho(8051), 97)
