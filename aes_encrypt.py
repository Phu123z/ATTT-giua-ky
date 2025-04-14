from aes_core import sub_bytes, shift_rows, mix_columns, add_round_key
from aes_constants import R_CON, S_BOX

def key_expansion(key):
    # Simplified for 128-bit key
    # Placeholder: Normally should return list of 11 round keys
    return [key] * 11

def bytes_to_matrix(b):
    return [list(b[i:i+4]) for i in range(0, 16, 4)]

def matrix_to_bytes(matrix):
    return bytes(sum(matrix, []))

def encrypt_block(plaintext, key):
    state = bytes_to_matrix(plaintext)
    round_keys = key_expansion(key)
    
    state = add_round_key(state, bytes_to_matrix(round_keys[0]))
    
    for i in range(1, 10):
        state = sub_bytes(state)
        state = shift_rows(state)
        state = mix_columns(state)
        state = add_round_key(state, bytes_to_matrix(round_keys[i]))

    state = sub_bytes(state)
    state = shift_rows(state)
    state = add_round_key(state, bytes_to_matrix(round_keys[10]))

    return matrix_to_bytes(state)
