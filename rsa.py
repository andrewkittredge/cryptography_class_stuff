from euclidean_algo import extended_euclidean_algorithm
from exponentiation import fast_exponentiation
from utils import prime_factorization
import random
from ascii_to_int import ascii_to_int, int_to_ascii

phi = lambda p, q : (p - 1) * (q - 1)

def p_and_q():
    return 107, 113

def multiplicative_inverse(phi_n, key):
    inverse_n = extended_euclidean_algorithm(phi_n, key)
    inverse_n = inverse_n % phi_n
    return inverse_n

def decryption_key(phi, public_key):
    return multiplicative_inverse(phi, public_key)

def encryption_key(p, q):
    #assert p % 3 == 4 and q % 3 == 4
    phi_n = phi(p, q)
    public_key = random.randint(1, 2 ** 128)
    phi_factors = prime_factorization(phi_n)
    while public_key in phi_factors:
        public_key = random.randint(1, 2 ** 128)
    return public_key

def decrypt(encrypted_message, decrypt_key, n):
    return fast_exponentiation(encrypted_message, decrypt_key, n)

def encrypt(n, encrypt_key, message):
    return fast_exponentiation(message, encrypt_key, n)

class RSA_Reciever(object):
    '''Bob from the example.
    
    '''
    def __init__(self, generate_primes, encryption_key):
        p, q = generate_primes()
        self.n = p * q
        e = encryption_key(p, q)
        d = multiplicative_inverse(phi(p, q), e)
        self.e, self.d = e, d
        
    def decrypt(self, message):
        m = decrypt(message, self.d, self.n)
        return m
    
    def ascii_decrypt(self, message):
        return int_to_ascii(self.decrypt(message))
    
class RSA_Sender(object):
    '''Alice from the example.
    
    '''
    def __init__(self, n, encryption_key):
        self.n = n
        self.encryption_key = encryption_key
        
    def encrypt(self, message):
        assert message < self.n
        return encrypt(self.n, self.encryption_key, message)
    
    def ascii_encrypt(self, message):
        message = ascii_to_int(message)
        return self.encrypt(message)

def generate_test_p_q():
    yield 107
    yield 113

import unittest
class Test_Sender_Reciever(unittest.TestCase):
    def setUp(self):
        bob = RSA_Reciever(generate_test_p_q, lambda p, q  : 3)
        alice = RSA_Sender(bob.n, bob.e)
        self.bob, self.alice = bob, alice
        
    def test_alice_bob(self):
        bob, alice = self.bob, self.alice
        self.assertEqual(bob.n, 12091)
        self.assertEqual(alice.encrypt(3981), 12039)
        
    def test_int_round_trip(self):
        bob, alice = self.bob, self.alice
        m = 10000
        encrypted_message = alice.encrypt(m)
        decrypted_message = bob.decrypt(encrypted_message)
        self.assertEqual(m, decrypted_message)
    
    def test_ascii_rount_trip(self):
        bob, alice = self.bob, self.alice
        m = 'h'
        encrypted_message = alice.ascii_encrypt(m)
        decrypted_message = bob.ascii_decrypt(encrypted_message)
        self.assertEqual(m, decrypted_message)
        
        
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
    #receiver = RSA_Reciever(generate_test_p_q, lambda p, q : 3)
    #print 'n, e = %s, %s' % (receiver.n, receiver.e)
    sender = RSA_Sender(n=4993627030669, encryption_key=202829)
    print sender.ascii_encrypt('hi')
    