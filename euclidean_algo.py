#An implementation of the Euclidean Algorithm.

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

class Euclidean_Expression(object):
    def __init__(self, dividend, coefficient, modulus):
        self.dividend = dividend
        self.coefficient = coefficient
        self.modulus = modulus
    
    def __str__(self):
        return '(%s, %s, %s)' % (self.dividend, 
                               self.coefficient, 
                               self.modulus)
    
    def __repr__(self):
        return self.__str__()   

def remembering_euclidian_algorithm(x, y):
    expressions = []
    modulus, dividend = sorted((x, y))
    remainder = -1
    while remainder not in (0, 1):
        coefficient = -(dividend / modulus)
        expressions.append(Euclidean_Expression(dividend, 
                                                coefficient, 
                                                modulus))

        remainder = dividend % modulus
        dividend = modulus
        modulus = remainder
    ret_val = 1 if remainder == 1 else dividend
    return ret_val, expressions

def find_coefficients(x, y):
    _, expressions = remembering_euclidian_algorithm(x, y)
    expressions = list(reversed(expressions))
    
    first_coefficient = 1
    second_coefficient = expressions[0].coefficient
    for i in range(len(expressions) - 1):
        prev_first_coefficient = first_coefficient
        first_coefficient = second_coefficient
        next_line = expressions[i + 1]
        second_coefficient = prev_first_coefficient + second_coefficient * next_line.coefficient
        
    return first_coefficient, second_coefficient


if __name__ == '__main__':
    print find_coefficients(614, 513)