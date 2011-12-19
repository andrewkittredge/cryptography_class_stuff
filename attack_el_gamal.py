'''
Created on Dec 17, 2011

@author: andrewkittredge
'''
from ascii_to_int import int_to_ascii
from baby_step_giant_step import discrete_log
from elgamal import decrypt
from exponentiation import fast_exponentiation


def attack_elgamal(_primitive_root, _public_key, _prime, header, message):
    l = discrete_log(prime=_prime,
                     primitive_root=_primitive_root,
                     public_key=_public_key)
    decrypted_message = decrypt(message, header, l, _prime)
    return decrypted_message
    pass

def ascii_attack_elgamal(b, c, p, message):
    return int_to_ascii(attack_elgamal(b, c, p, message))

import unittest
class ElGamalAttackTester(unittest.TestCase):
    def test_attack_elgamal(self):
        #Alice

        p = 1009
        b = 101
        c = 482
        l = discrete_log(prime=p,
                         primitive_root=b,
                         public_key=c)
        
        #Bob
        x = 559
        r = 291
        c_to_the_r = fast_exponentiation(c, r, p)
        encrypted_message = x * c_to_the_r % p
        header = fast_exponentiation(b, r, p)        
        
        decrypted_message = decrypt(encrypted_message, header, l, p)
        
        print attack_elgamal(_primitive_root=b,
                             _public_key=c,
                             _prime=p,
                             message=encrypted_message,
                             header=header)