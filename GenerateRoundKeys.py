'''
(1) K = K1 || K2 || K3 || K4 || K5 || K6 || K7 || K8
(2) for i = 1 to 7:
     K`i= FI(Ki, Ki+1)
(3) K`8 = FI(K8, K1)
(4) K` = K`1 || K`2 || K`3 || K`4 || K`5 || K`6 || K`7 || K`8
(5) KOi1 = Ki, KOi2 = Ki+2, KOi3 = Ki+7, KOi4 = Ki+4, KIi1 = K`i+5, KIi2 = K`i+1, KIi3 = K`i+3, (i = 1,..,8)
KLiL = K(i+1)/2 (odd i) or K`(i/2)+2 (even i), KLiR = K` (i+1)/2+6 (odd i) or K(i/2)+4 (even i) (i = 1,..,10)
'''
from functions import FI
def rotate_index(i):
    if i>8: 
        return (i - 8)
    else:
        return i

def GenerateRoundKeys(key: bytes) -> dict:
    assert len(key)==16

    K = [0]
    for i in range(0, 16, 2):
          part = key[i:i+2]  
          number = int.from_bytes(part, byteorder='big') 
          K.append(number)

    K_dash = [0]
    
    for i in range(1, 8):
        K_dash.append(FI(K[i], K[i+1]))
    K_dash.append(FI(K[8], K[1]))
 

   
    KO = []
    for i in range(1, 9):
        KO1 = K[rotate_index(i)]
        KO2 = K[rotate_index(i+2)]
        KO3 = K[rotate_index(i+7)] 
        KO4 = K[rotate_index(i+4)]
        KO.append((KO1, KO2, KO3, KO4))

    
    KI = []
    for i in range(1,9):
        KI1 = K_dash[rotate_index(i + 5)]
        KI2 = K_dash[rotate_index(i+1)]
        KI3 = K_dash[rotate_index(i + 3)]
        KI.append((KI1, KI2, KI3))

    KL = []
    for i in range(1, 11): 
        if i % 2 == 1: 
            # KL_L = K[((i + 1) // 2) % 8]
            # KL_R = K_dash[((i + 1) // 2 + 6 ) % 8]
            KL_L = K[rotate_index((i + 1) // 2)]
            KL_R = K_dash[rotate_index((i + 1) // 2 + 6 )]
        else:  
            KL_L = K_dash[rotate_index(i // 2 + 2)]
            KL_R = K[rotate_index(i // 2 + 4)]
        KL.append((KL_L, KL_R))
        
    return {
        "KO": KO,  # список з 8 кортежів (KO1, KO2, KO3, KO4)
        "KI": KI,  # список з 8 кортежів (KI1, KI2, KI3)
        "KL": KL,   # список з 10 кортежів (KL_L, KL_R)
        # "K_dash": K_dash
        }
    
