from des_file_io import read_output, write_decrypted, read_key
from des_decrypt import des_decrypt

def main():
    ciphertext = read_output("output.txt")
    key = read_key("key.txt")
    decrypted = des_decrypt(ciphertext, key)
    write_decrypted("decrypted.txt", decrypted)

if __name__ == "__main__":
    main()
