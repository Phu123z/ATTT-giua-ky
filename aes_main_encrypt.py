from aes_file_io import read_input, write_output, read_key
from aes_encrypt import aes_encrypt

def main():
    plaintext = read_input("input.txt")
    key = read_key("key.txt")
    ciphertext = aes_encrypt(plaintext, key)
    write_output("output.txt", ciphertext)

if __name__ == "__main__":
    main()
