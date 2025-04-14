def read_input_file(path='input.txt'):
    with open(path, 'rb') as f:
        return f.read()

def write_output_file(data, path='output.txt'):
    with open(path, 'wb') as f:
        f.write(data)

def pad(plaintext):
    padding_len = 16 - (len(plaintext) % 16)
    return plaintext + bytes([padding_len] * padding_len)

def unpad(plaintext):
    padding_len = plaintext[-1]
    return plaintext[:-padding_len]
