from functions import FL_INV, FO

def DecryptBlock(block_bytes: bytes, key_data: dict) -> bytes:
    assert len(block_bytes) == 8
    L= [int.from_bytes(block_bytes[0:4], 'big')]
    R= [int.from_bytes(block_bytes[4:8], 'big')]
    for i in range(0, 8, 2):
        Ri = FL_INV(L[-1], 9-i, key_data)
        Li = FL_INV(R[-1], 8-i , key_data) ^ FO(Ri, 7 - i, key_data)
        Li1 = Ri ^ FO(Li, 6 - i , key_data)
        Ri1 = Li

        L.append(Li1)
        R.append(Ri1)

    R9 = FL_INV(L[-1], 1, key_data)
    L9 = FL_INV(R[-1], 0, key_data)

    return L9.to_bytes(4, 'big') + R9.to_bytes(4, 'big')
