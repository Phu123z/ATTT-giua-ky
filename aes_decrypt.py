from aes.core import inv_sub_bytes, inv_shift_rows, inv_mix_columns, add_round_key
from aes.encrypt import key_expansion, bytes_to_matrix, matrix_to_bytes

def decrypt_block(ciphertext, key):
    state = bytes_to_matrix(ciphertext)
    round_keys = key_expansion(key)
    
    state = add_round_key(state, bytes_to_matrix(round_keys[10]))
    state = inv_shift_rows(state)
    state = inv_sub_bytes(state)

    for i in range(9, 0, -1):
        state = add_round_key(state, bytes_to_matrix(round_keys[i]))
        state = inv_mix_columns(state)
        state = inv_shift_rows(state)
        state = inv_sub_bytes(state)

    state = add_round_key(state, bytes_to_matrix(round_keys[0]))

    return matrix_to_bytes(state)
