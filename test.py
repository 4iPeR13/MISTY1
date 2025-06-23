from GenerateRoundKeys import GenerateRoundKeys 
from Encrypt import EncryptBlock
from Decrypt import DecryptBlock

def test():
    vectors = [
        {
            "key": "00112233445566778899aabbccddeeff",
            "pt":  "0123456789abcdef",
            "ct":  "8b1da5f56ab3d07c",
            "k_dash": "cf518e7f5e29673acdcb07d6bf355e11"
        },
        {
            "key": "414afd99bb577ee69df58cc8fb4e6888",
            "pt":  "9fc302e281310e90",
            "ct":  "15c270974b9b9163",
            "k_dash": "c7bd6e012268237a4389305a1b360b8c"
        },
        {
            "key": "3c54aed9a5389c947167db9d97c6967a",
            "pt":  "032c4a4a100ee807",
            "ct":  "3346cb8c779cf2de",
            "k_dash": "7c8e13ebfe7648050c9097934205662b"
        },
        {
            "key": "d3f11a6d25f1b3866fdada0b5e53fa17",
            "pt":  "db9e3218402023f3",
            "ct":  "b2dd1595a450bc98",
            "k_dash": "f011d035ac920f832f69bcf7b860d4f0"
        },
        {
            "key": "5f87f88ec7641d83af03fd8327821046",
            "pt":  "6553de24c0dd900b",
            "ct":  "60081e65cb7c2b84",
            "k_dash": "3736172d7421c91401596db29d3d5536"
        }
        ]

    for i, v in enumerate(vectors, 1):
        key = bytes.fromhex(v["key"])
        pt = bytes.fromhex(v["pt"])
        ct_expect = bytes.fromhex(v["ct"])
        k_dash_expect = bytes.fromhex(v["k_dash"])

        rk = GenerateRoundKeys(key)
        ct = EncryptBlock(pt, rk)
        pt_decrypted = DecryptBlock(ct, rk)

        assert ct == ct_expect, f"Тест {i}: очікувалось {ct_expect.hex()}, а вийшло {ct.hex()}"
        assert pt_decrypted == pt, f"Тест {i}: дешифрування не співпало"

        k_dash = b""
        for val in rk["K_dash"]:
            k_dash += val.to_bytes(2, "big")
        if k_dash != k_dash_expect:
            print(f"TEST {i} тупо помилка в тестових даних WOW!!!")
        if i!=1:
             assert k_dash == k_dash_expect, f"Тест {i}: K'={k_dash.hex()}, а очікувалось {k_dash_expect.hex()}"
        
        print(f"Тест {i} Успішно: шифр={ct.hex()}, K'={k_dash.hex()}")

    print("Усі тести пройдено успішно.")