
import sys
import src.ciphers.preprocess as pre
import os
# find inverse of a
def modInverse(a, m) :

	a = a % m;
	for x in range(1, m) :
		if ((a * x) % m == 1) :
			return x
	return 1

# Driver Program
# a = 28
# m = 29
#
# for i in range(1,m):
#     if modInverse(i,m)!= 1:
#         print("multiplicative inverse of %d is %d"%(i,modInverse(i,m)))
#   #print(",",modInverse(i, m),end="")


# Affine cipher
# Encryption e(x) = ( a x + b ) mod m
# Decryption d(x) = a-1 * (x - b ) mod m


def encrypt(plaintext,a, b ):
    """Encrytping using the standard affine cipher definition"""
    if a != 1 and modInverse(a,26) == 1:
        print("affine cipher mandates the key to have an inverse and the provided key inverse doesn't exist")
        sys.exit()

    ciphertext =''
    for c in plaintext:
        x = ord(c) - 97
        ec  = chr( ( (a * x + b ) % 26) + 65)
        ciphertext  = ciphertext + ec
    return ciphertext


def decrypt(ciphertext,a,b):
    """Decrypting using the standard affine cipher definition"""
    if a != 1 and modInverse(a,26) == 1:
        print("affine cipher mandates the key to have an inverse and the provided key inverse doesn't exist")
        sys.exit()
    plaintext =''
    inv = modInverse(a, 26)
    for c in ciphertext:
        y = ord(c) - 65
        dc = chr(( (inv * ( y - b) ) % 26 ) +97)
        plaintext = plaintext + dc
    return plaintext


plaint= pre.preprocess(os.getcwd()+'/sample')
a = 15
b=5
print("plain text ", plaint)
ciphert = encrypt(plaint,a,b)
print(ciphert)
print(decrypt(ciphert,a,b))