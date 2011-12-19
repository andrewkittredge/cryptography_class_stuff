'''
Created on Dec 16, 2011

@author: andrewkittredge
'''

from euclidean_algo import euclidean_algo
from rsa import multiplicative_inverse, decrypt
from ascii_to_int import int_to_ascii
    

def pollards_rho(n):
    f = lambda x : (x ** 2 + 1) % n
    x = 2
    y = 2
    g = 1
    while not 1 < g < n:
        if g == 1:
            x = f(x)
            y = f(f(y))
        elif g == n:
            raise Exception('failure, reinitialize.')
        g = euclidean_algo(abs(x - y), n)
    return g

def attack_rsa(n, e, message):
    p = pollards_rho(n)
    q = n / p
    phi_n = (p - 1) * (q - 1)
    d = multiplicative_inverse(phi_n, e)
    return decrypt(message, d, n)

import unittest
class FactoriztionTester(unittest.TestCase):
    def test_pollards_rho(self):
        self.assertEqual(pollards_rho(8051), 97)

class AttackTester(unittest.TestCase):
    def test_attack_rsa(self):
        n=4993627030669
        e=202829
        message=874814388105
        decrypted_message = int_to_ascii(attack_rsa(n, e, message))
        self.assertEqual(decrypted_message, 'hi')
        
if __name__ == '__main__':
    #print pollards_rho(4993627030669)
    print attack_rsa(n=22779161373223907036709223293229496777,
                     e=133325100753502750892526923899399,
                     message=20395050182554241083161336405745338859)