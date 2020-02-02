# Affine and shift cipher is a special case of substitution cipher
# Subsituition cipher key is one of the possible permutations of n! possible cases (n=26 in case of english alphabets)

def inverse(a=[]):
    """return the inverse of a given perumatation"""
    i=[]
    for idx in range(len(a)):
        i.append(a.index(idx+1)+1)

    return i

print(inverse([3,4,2,1,5]))

str = 'TGEEMNELNNTDROEOAAHDOETCSHAEIRLM'
m =8
p =[4,1,6,2,7,3,8,5]

def encryption(plaint, m=8, p=[]):
    chunks = [ plaint[i:i+m] for i in range(0,len(plaint),m)]
    ctext=[]
    for chars in chunks:
        for index,c in enumerate(chars):
            ctext.append(chars[p[index]-1].capitalize())

    return ''.join(ctext)


def decryption(ciphert,m=6,p=[]):
    p = inverse(p)
    chunks = [ciphert[i:i + m] for i in range(0, len(ciphert), m)]
    ctext = []
    for chars in chunks:
        for index, c in enumerate(chars):
            ctext.append(chars[p[index] - 1].lower())

    return ''.join(ctext)


print(decryption(str,m,p))