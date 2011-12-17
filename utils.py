def prime_factorization(n):
    prime_factors = set()
    for i in range(2, n):
        while n % i == 0:
            prime_factors.add(i)
            n = n / i
    return list(prime_factors)


def gcd(x, y):
    '''x and y are integers.'''
    smaller, larger = sorted((x, y))
    dividend = larger
    modulus = smaller
    remainder = True
    while remainder:
        remainder = dividend % modulus 
        dividend = modulus
        modulus = remainder
    return dividend