import src.ciphers.preprocess as pre
import os

"""This program is used to implement vigenere cipher to encrypt and decrypt plain text"""

def decrypt(key,ciphertext):
    """Decryption using the standard method of vigenere cipher"""
    plaintext = ""
    val=[]
    for c in key:
        val.append(ord(c) - 65)

    for i, c in enumerate(ciphertext):
        ascva = ord(c) - 65
        plaintext = plaintext + chr(((ascva - val[i % len(val)]) % 26) + 97)
    return plaintext


def encrypt(key, plaintext):
    """Encryption using the standard vigenere cipher"""
    val =[]
    ciphertext= ""
    for c in key:
        val.append(ord(c) - 65)

    for i,c in enumerate(plaintext):
        ascva = ord(c) - 97
        ciphertext = ciphertext + chr( ((ascva + val[i%len(val)]) % 26 ) + 65)

    return ciphertext

key = "saikiran"
x = pre.preprocess(os.getcwd()+'/sample')
print(x)
ciphert = encrypt(key,x)
print(ciphert)
plaint = decrypt(key,ciphert)
print(plaint)