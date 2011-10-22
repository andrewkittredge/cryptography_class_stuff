def exponentiation(X, E, m):
    Y = 1
    while E != 0:
        if E % 2 == 0:
            X = (X * X) % m
            E = E / 2
        else:
            Y = (X * Y) % m
            E = E - 1
        print X, E, Y
    return Y

if __name__ == '__main__':
    exponentiation(2, 56, 1001)