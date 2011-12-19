from exponentiation import fast_exponentiation
import random
from euclidean_algo import extended_euclidean_algorithm
from utils import prime_factorization,large_random_prime, infinite_range
from ascii_to_int import int_to_ascii


def generate_keys():
    '''Alice builds a dicsrete-log public-key cipher system.

    '''

    cyclic_group = large_random_prime()
    generator = random_near_primitive_root(cyclic_group)
    private_key = random.randint(1, cyclic_group - 1)
    public_key = fast_exponentiation(generator, private_key, cyclic_group)

    return (generator, public_key, cyclic_group), private_key

def encrypt(message, b, c, p):
    r = large_random_prime()
    c_r = fast_exponentiation(c, r, p)
    encrypted_message = message * c_r % p
    header = fast_exponentiation(b, r, p)
    return encrypted_message, header


    
def decrypt(message, header, l, p):
    c_r = fast_exponentiation(header, l, p)
    inverse = extended_euclidean_algorithm(c_r, p)
    plaintext = (inverse * message) % p
    return plaintext
    
def _large_random_prime():
    return 291

def random_near_primitive_root(p):
    start = random.randint(2, p - 1)
    primes_to_test = prime_factorization(p - 1)
    for b in infinite_range(start, p):
        if primitive_root(b, primes_to_test, p):
            return b
            
def primitive_root(group, divisors, prime):
    for q in divisors:
        if fast_exponentiation(group, (prime - 1) / q, prime) == 1:
            return False
    return True

import unittest
class Tester(unittest.TestCase):
    def test_encrypt(self):
        self.assertEquals((421, 661), encrypt(559, 101, 482, 1009))
        
    def test_decryption(self):
        l = 237
        p = 1009
        message, header = 421, 661
        self.assertEqual(decrypt(message, header, l, p), 559)
        self.assertEqual(decrypt(5154192, ))
        
if __name__ == '__main__':
    #unittest.main()
    #print encrypt(1235, 2, 6329323223, 8209120459)
    #print generate_keys()
    #===========================================================================
    # p = 3079259
    # b = 448
    # private_key = 7
    # public_key = fast_exponentiation(b, private_key, p)
    # print decrypt(message=683482,
    #               header=2054398,
    #               l=7,
    #               p=p)
    # #print decrypt(20, 197, 72, 291)
    print encrypt(message=104105, 
                  b=60096, 
                  c=168710, 
                  p=191747)

    print int_to_ascii(decrypt(message=3415555458673405466, 
                               header=1580194612606838012, 
                               l=1245269559009664185, 
                               p=4462768852845629707))
