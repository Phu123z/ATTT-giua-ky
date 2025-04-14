from des.constants import IP, FP, E, P, PC1, PC2, SHIFTS
from des.sboxes import S_BOXES
from des.utils import permute, xor, left_shift, split_in_half


def sbox_substitution(bits48):
    result = ""
    for i in range(8):
        block = bits48[i * 6:(i + 1) * 6]
        row = int(block[0] + block[5], 2)
        col = int(block[1:5], 2)
        val = S_BOXES[i][row][col]
        result += f"{val:04b}"
    return result


def feistel(right, subkey):
    expanded = permute(right, E)
    xored = xor(expanded, subkey)
    substituted = sbox_substitution(xored)
    return permute(substituted, P)


def generate_subkeys(key_64):
    key_56 = permute(key_64, PC1)
    left, right = split_in_half(key_56)
    subkeys = []

    for shift in SHIFTS:
        left = left_shift(left, shift)
        right = left_shift(right, shift)
        combined = left + right
        subkeys.append(permute(combined, PC2))

    return subkeys
