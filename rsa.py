from euclidean_algo import extended_euclidean_algorithm
from exponentiation import fast_exponentiation

theta = lambda p, q : (p - 1) * (q - 1)

def p_and_q():
    return 107, 113

def multiplicative_inverse(theta_n, key):
    _, inverse_n = extended_euclidean_algorithm(theta_n, key)
    inverse_n = inverse_n % theta_n
    return inverse_n

def decryption_key(p, q, key, n):
    t = theta(p, q)
    return multiplicative_inverse(t, key)

def public_knowledge():
    return 12091, 3

def decrypt(encrypted_message, decrypt_key, n):
    return fast_exponentiation(encrypted_message, decrypt_key, n)

def encrypt(n, encrypt_key, message):
    return fast_exponentiation(message, encrypt_key, n)
