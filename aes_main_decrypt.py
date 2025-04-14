from aes_file_io import read_output, write_decrypted, read_key
from aes_decrypt import aes_decrypt

def main():
    ciphertext = read_output("output.txt")
    key = read_key("key.txt")
    decrypted = aes_decrypt(ciphertext, key)
    write_decrypted("decrypted.txt", decrypted)

if __name__ == "__main__":
    main()
