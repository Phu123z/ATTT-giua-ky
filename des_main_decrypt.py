from des_file_io import read_file, write_file
from des_decrypt import des_decrypt_block


def bin_to_str(b):
    chars = [b[i:i + 8] for i in range(0, len(b), 8)]
    return ''.join(chr(int(c, 2)) for c in chars)


def main():
    cipher = read_file("des/output.txt")
    key = read_file("des/key.txt")

    bin_key = ''.join(f"{ord(c):08b}" for c in key)[:64].ljust(64, "0")

    result = ""
    for i in range(0, len(cipher), 64):
        block = cipher[i:i + 64]
        plain_block = des_decrypt_block(block, bin_key)
        result += plain_block

    plain_text = bin_to_str(result).rstrip("\x00")
    write_file("des/decrypted.txt", plain_text)


if __name__ == "__main__":
    main()
