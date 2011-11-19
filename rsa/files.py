def write_public_info(pubic_key, encryption_key, out_file):
    with open(out_file, 'wb') as out:
        out.write_line(encyption_key)
        out.write_line(public_key)

def read_public_info(file):
    with open(file, 'rb') as input:
        encryption_key = input.readline()
        decryption_key = input.readline()

def write_private_info(p, q, file):
    with open(file, 'wb') as out:
        out.write_line(p)
        out.write_line(q)

def read_private_info(file):
    with open(file, 'rb') as input:
        p = input.read_line()
        q = input.read_line()
