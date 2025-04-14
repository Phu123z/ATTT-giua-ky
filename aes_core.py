from aes_constants import S_BOX, INV_S_BOX

def sub_bytes(state):
    return [[S_BOX[byte] for byte in row] for row in state]

def inv_sub_bytes(state):
    return [[INV_S_BOX[byte] for byte in row] for row in state]

def shift_rows(state):
    return [
        state[0],
        state[1][1:] + state[1][:1],
        state[2][2:] + state[2][:2],
        state[3][3:] + state[3][:3],
    ]

def inv_shift_rows(state):
    return [
        state[0],
        state[1][-1:] + state[1][:-1],
        state[2][-2:] + state[2][:-2],
        state[3][-3:] + state[3][:-3],
    ]

def mix_single_column(column):
    # GF(2^8) multiply (simplified)
    def xtime(a): return ((a << 1) ^ 0x1b) & 0xff if (a & 0x80) else a << 1
    t = column[0] ^ column[1] ^ column[2] ^ column[3]
    return [
        column[0] ^ t ^ xtime(column[0] ^ column[1]),
        column[1] ^ t ^ xtime(column[1] ^ column[2]),
        column[2] ^ t ^ xtime(column[2] ^ column[3]),
        column[3] ^ t ^ xtime(column[3] ^ column[0]),
    ]

def mix_columns(state):
    return [mix_single_column(col) for col in zip(*state)]

def inv_mix_columns(state):
    # inverse mix_columns using precalculated constants
    def mul(a, b):
        p = 0
        for i in range(8):
            if b & 1: p ^= a
            hi_bit_set = a & 0x80
            a = (a << 1) & 0xFF
            if hi_bit_set: a ^= 0x1b
            b >>= 1
        return p

    result = []
    for col in zip(*state):
        result.append([
            mul(col[0], 0x0e) ^ mul(col[1], 0x0b) ^ mul(col[2], 0x0d) ^ mul(col[3], 0x09),
            mul(col[0], 0x09) ^ mul(col[1], 0x0e) ^ mul(col[2], 0x0b) ^ mul(col[3], 0x0d),
            mul(col[0], 0x0d) ^ mul(col[1], 0x09) ^ mul(col[2], 0x0e) ^ mul(col[3], 0x0b),
            mul(col[0], 0x0b) ^ mul(col[1], 0x0d) ^ mul(col[2], 0x09) ^ mul(col[3], 0x0e),
        ])
    return [list(row) for row in zip(*result)]

def add_round_key(state, round_key):
    return [[s ^ k for s, k in zip(row_s, row_k)] for row_s, row_k in zip(state, round_key)]
