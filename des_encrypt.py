from des_core import feistel, generate_subkeys
from des_utils import permute, xor, split_in_half
from des_constants import IP, FP


def des_encrypt_block(block_64, key_64):
    subkeys = generate_subkeys(key_64)
    block = permute(block_64, IP)
    left, right = split_in_half(block)

    for subkey in subkeys:
        temp = right
        right = xor(left, feistel(right, subkey))
        left = temp

    final_block = permute(right + left, FP)
    return final_block
