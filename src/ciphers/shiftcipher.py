
'''This is a library to encrypt and decrypt messages from  '''


def encrypt(plaintext,key =3):
    """encrypt a string using standard shift cipher definition"""
    ciphertext = ""
    for x in plaintext:
        ciphertext = ciphertext + chr(((ord(x) - 97 + key) % 26) + 65)

    return ciphertext


def decrypt(ciphertext,key = 3):
    """decrypt a string using standard shift cipher definition"""
    plaintext = ""

    for x in ciphertext:
        plaintext = plaintext + chr((ord(x) - 65 - key) % 26 + 97)

    return plaintext





for i in range(0,26):
    print()
    print("Decrypted text : %s and the key %d "%(decrypt(ciphertext,key = i),i))






