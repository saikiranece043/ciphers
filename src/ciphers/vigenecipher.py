import src.ciphers.preprocess as pre
import os
import src.attackciphers.attackVigenere as av
import matplotlib.pyplot as plt
from scipy.signal import argrelextrema
from scipy.signal import argrelmax
from scipy.signal import find_peaks
import numpy as np
import math
"""This program is used to implement vigenere cipher to encrypt and decrypt plain text"""



def findlcm(a):
    """find lcm of an array of numbers"""
    lcm = a[0]
    for i in a[1:]:
        lcm = lcm * i // math.gcd(lcm, i)
    return lcm


def decrypt(key,ciphertext,m=256):
    """Decryption using the standard method of vigenere cipher"""
    plaintext = ""
    val=[]
    for c in key:
        val.append(ord(c))

    for i, c in enumerate(ciphertext):
        ascva = ord(c)
        k = val[i%len(val)] %m
        plaintext = plaintext + chr((ascva - k ) % m)
    return plaintext


def encrypt(key, plaintext,m=256):
    """Encryption using the standard vigenere cipher"""
    val =[]
    ciphertext= ""

    #storing the ascii values of the key in an array
    for c in key:
        #val.append(ord(c) - 65)
        val.append(ord(c))

    for i,c in enumerate(plaintext):
        #ascva = ord(c) - 97
        ascva = ord(c)
        k = val[i%len(val)] % m
        ciphertext = ciphertext + chr((ascva + k ) % m)

    return ciphertext

key = "howareyoududeanythignfuncky"
print(len(key))

plaintext = pre.readfile(os.getcwd()+'/sample')

ciphertext= encrypt(key,plaintext)


plaintextdistr  = av.findpdf(plaintext)
ciphertextdistr = av.findpdf(ciphertext)

ioc = av.getioc(ciphertext,64)
ioc_maxima_freq=find_peaks(ioc,height=0.05)[0]
result = np.diff(ioc_maxima_freq.tolist())
resultlst =list(result)
#print(np.diff(ioc_maxima_freq.tolist()))
keylength = max(resultlst,key=resultlst.count)
print(keylength)

#print(ioc)
#print(np.convolve(ioc,1))
#localmaxima=argrelextrema(np.convolve(ioc,1),np.greater)
#print(np.diff(np.sign(np.diff(ioc))))
#print(localmaxima)
#print(np.lcm.reduce(localmaxima[0][0]))
#plt.plot(ioc)
#print("Probablity distribution of the original text",av.findpdf(ciphertext))
#print(encrypt(key,x))
#print(decrypt(key,encrypt(key,x)))

print(plaintextdistr)
plt.hist(ciphertextdistr)
plt.show()