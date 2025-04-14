def permute(block, table):
    return "".join(block[i - 1] for i in table)


def xor(bits1, bits2):
    return "".join("1" if b1 != b2 else "0" for b1, b2 in zip(bits1, bits2))


def left_shift(bits, shift):
    return bits[shift:] + bits[:shift]


def split_in_half(bits):
    half = len(bits) // 2
    return bits[:half], bits[half:]
