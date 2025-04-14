

from des_file_io import read_file, write_file
from des_encrypt import des_encrypt_block


def str_to_bin(s):
    return ''.join(f"{ord(c):08b}" for c in s)


def pad_binary(bin_data):
    while len(bin_data) % 64 != 0:
        bin_data += "0"
    return bin_data


def main():
    plaintext = read_file("des/input.txt")
    key = read_file("des/key.txt")

    bin_text = pad_binary(str_to_bin(plaintext))
    bin_key = str_to_bin(key)[:64].ljust(64, "0")  
    result = ""
    for i in range(0, len(bin_text), 64):
        block = bin_text[i:i + 64]
        cipher_block = des_encrypt_block(block, bin_key)
        result += cipher_block

    write_file("des/output.txt", result)


if __name__ == "__main__":
    main()
