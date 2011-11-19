def write_public_info(public_key, encryption_key, out_file):
    with open(out_file, 'wb') as out:
        out.write(str(encryption_key) + '\n')
        out.write(str(public_key) + '\n')

def read_public_info(file):
    with open(file, 'rb') as input:
        encryption_key = int(input.readline().strip())
        public_key = int(input.readline().strip())

    return encryption_key, public_key

def write_private_info(p, q, file):
    with open(file, 'wb') as out:
        out.write_line(p)
        out.write_line(q)

def read_private_info(file):
    with open(file, 'rb') as input:
        p = input.read_line()
        q = input.read_line()
