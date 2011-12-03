
padding = 7

char_to_binary = lambda char : '{:07b}'.format(ord(char))

string_to_int = lambda string : int(''.join(map(char_to_binary, string)), 2)

int_to_binary_string = lambda i : '{:b}'.format(i)

chunkify = lambda binary_repr : [binary_repr[i * padding : padding * (i + 1)] for i in range(len(binary_repr) / padding)]

make_string_from_chunks = lambda chunks : ''.join(map(lambda b : chr(int(b, 2)), chunks))

def int_to_string(int):
    binary_repr = int_to_binary_string(int)
    chunks = chunkify(binary_repr)
    return make_string_from_chunks(chunks)
