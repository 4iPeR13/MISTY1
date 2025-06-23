from functions import FL_INV, FO

def DecryptBlock(block_bytes: bytes, key_data: dict) -> bytes:
    assert len(block_bytes) == 8

    L = [FL_INV(int.from_bytes(block_bytes[0:4], 'big'), 9, key_data)]
    R = [FL_INV(int.from_bytes(block_bytes[4:8], 'big'), 8, key_data)]

    
    for i in reversed(range(0, 8, 2)):
        Li = R[-1] ^ FO(L[-1], i + 1, key_data)
        Ri = FL_INV(L[-1], i + 1, key_data) ^ FO(Li, i, key_data)

        L_prev = FL_INV(Ri, i, key_data)
        R_prev = Li

        L.insert(0, L_prev) 
        R.insert(0,R_prev)

    return L[-1].to_bytes(4, 'big') + R[-1].to_bytes(4, 'big')