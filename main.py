from test import test
from Encrypt import EncryptBlock
from Decrypt import DecryptBlock


if __name__ == "__main__":
    
    test()

   
    print("\n=== MISTY1 Шифрування ===")
    while True:
        print("\nОберіть дію:")
        print("1. Зашифрувати файл")
        print("2. Розшифрувати файл")
        print("0. Вихід")
        choice = input("Ваш вибір: ").strip()
        if choice == '0':
            print("Вихід.")
            break
        elif choice == '1':
            infile = input("Введіть ім'я вхідного файлу: ").strip()
            outfile = input("Введіть ім'я вихідного файлу: ").strip()
            keyfile = input("Введіть ім'я файлу з ключем (hex-рядок, 32 шістнадц. символи): ").strip()
            try:
                with open(keyfile, 'r', encoding='utf-8') as f:
                    keyhex = f.read().strip()
                key_bytes = bytes.fromhex(keyhex)
            except Exception as e:
                print("Помилка читання ключа:", e)
                continue
            try:
                with open(infile, 'rb') as f:
                    data = f.read()
            except Exception as e:
                print("Помилка читання вхідного файлу:", e)
                continue
            try:
                enc = EncryptBlock(data, key_bytes)
                with open(outfile, 'wb') as f:
                    f.write(enc)
                print(f"Файл зашифровано, результат записано в '{outfile}'.")
            except Exception as e:
                print("Помилка при шифруванні:", e)
        elif choice == '2':
            infile = input("Введіть ім'я вхідного файлу: ").strip()
            outfile = input("Введіть ім'я вихідного файлу: ").strip()
            keyfile = input("Введіть ім'я файлу з ключем (hex-рядок, 32 шістнадц. символи): ").strip()
            try:
                with open(keyfile, 'r', encoding='utf-8') as f:
                    keyhex = f.read().strip()
                key_bytes = bytes.fromhex(keyhex)
            except Exception as e:
                print("Помилка читання ключа:", e)
                continue
            try:
                with open(infile, 'rb') as f:
                    data = f.read()
            except Exception as e:
                print("Помилка читання вхідного файлу:", e)
                continue
            try:
                dec = DecryptBlock(data, key_bytes)
                with open(outfile, 'wb') as f:
                    f.write(dec)
                print(f"Файл розшифровано, результат записано в '{outfile}'.")
            except Exception as e:
                print("Помилка при дешифруванні:", e)
        else:
            print("Невірний вибір, спробуйте ще раз.")
