'''
Created on Dec 4, 2011

@author: andrewkittredge
'''

from exponentiation import fast_exponentiation
import logging

def miller_rabin(n, b):


    r = 0
    m = n - 1
    while m % 2 == 0:
        r += 1 
        m = m / 2
    if fast_exponentiation(b, m, n) in (n - 1, 1):
        return True
    power = 1
    while power < r - 1:
        b_m_squared_mod_n = fast_exponentiation(b, m * (2 ** power), n)
        if b_m_squared_mod_n == 1:
            return False
        elif b_m_squared_mod_n == n - 1:
            return True
        else:
            power = power * 2
    return False

import unittest
class Test(unittest.TestCase):
    def test_miller_rabin(self):
        for composite, base in ((1281, 41),
                                (1729, 10),
                                (3073, 1146),
                                (3201, 1163),
                                (3201, 1163),
                                (3585, 434),
                                (5377, 848)):
            self.assertTrue(miller_rabin(composite, base))
