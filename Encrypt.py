'''
(2) for i = 1, 3, ..., 7 (increment in steps of 2 because the loop body consists of two rounds):
Ri= FL(Li-1, KLi)
Li= FL(Ri-1, KLi+1)⊕ FO(Ri, KOi, KIi)
Li+1 = Ri⊕ FO(Li, KOi+1, KIi+1)
Ri+1 = Li

for i = 9:
Ri= FL(Li-1, KLi)
Li= FL(Ri-1, KLi+1)

(3) C = L9 || R9
'''

from functions import FL, FO

def EncryptBlock(block_bytes: bytes, key_data: dict) -> bytes:
    assert len(block_bytes) == 8
    L= [int.from_bytes(block_bytes[0:4], 'big')]
    R= [int.from_bytes(block_bytes[4:8], 'big')]
    for i in range(0, 8, 2):
        Ri = FL(L[-1], i, key_data)
        Li = FL(R[-1], i + 1, key_data) ^ FO(Ri, i, key_data)
        Li1 = Ri ^ FO(Li, i + 1, key_data)
        Ri1 = Li

        L.append(Li1)
        R.append(Ri1)

    R9 = FL(L[-1], 8, key_data)
    L9 = FL(R[-1], 9, key_data)

    return L9.to_bytes(4, 'big') + R9.to_bytes(4, 'big')




   
