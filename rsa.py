from euclidean_algo import extended_euclidean_algorithm
from exponentiation import fast_exponentiation
from utils import prime_factorization
import random

phi = lambda p, q : (p - 1) * (q - 1)

def p_and_q():
    return 107, 113

def multiplicative_inverse(phi_n, key):
    inverse_n = extended_euclidean_algorithm(phi_n, key)
    inverse_n = inverse_n % phi_n
    return inverse_n

def decryption_key(phi, public_key):
    return multiplicative_inverse(phi, public_key)

def generate_public_knowledge(p, q):
    #assert p % 3 == 4 and q % 3 == 4
    n = p * q
    phi_n = phi(p, q)
    public_key = random.randint(1, 2 ** 128)
    phi_factors = prime_factorization(phi_n)
    while public_key in phi_factors:
        public_key = random.randint(1, 2 ** 128)
    return public_key, n

def decrypt(encrypted_message, decrypt_key, n):
    return fast_exponentiation(encrypted_message, decrypt_key, n)

def encrypt(n, encrypt_key, message):
    return fast_exponentiation(message, encrypt_key, n)

import unittest
class Test(unittest.TestCase):
    def test_rsa(self):
        
        public_key = 3
        p, q = 107, 113
        message = 3981
        n = p * q
        phi_p_q = phi(p, q) 
        self.assertEqual(decryption_key(11872, 3), 7915)
        
        encrypted_message = encrypt(n, public_key, message)
        self.assertEqual(encrypted_message, 12039)
        d_key = decryption_key(phi_p_q, public_key) 
        decrypted_message = decrypt(encrypted_message, d_key, n)
        self.assertEqual(decrypted_message, message)

if __name__ == '__main__':
    #unittest.main()
    p, q = 3167, 2591
    n = p * q
    public_key = 17
    phi_p_q = phi(p, q)
    assert public_key not in prime_factorization(phi_p_q)
    print generate_public_knowledge(p, q)
    d_key = decryption_key(phi_p_q, public_key)
    print decrypt(4270848, d_key, n)