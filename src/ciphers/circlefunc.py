

a =[3,5,1,2,4]
b =[4,1,5,3,2]

def ifidentity(x):
    """This function is to check if a given permutation is identity permuatation or may be not"""
    for idx,val in enumerate(x):
        if idx+ 1 != val:
            return False
    return True



def circlfunc(a,b):
    """This function is to create a new permutation from two given permutations also circle of two permutations"""
    c = []
    for i in range(0,len(a)):
        c.append(a[b[i]-1])

    return c


def order(a):
    """This function is to find the order of a given permutation i.e no of times a permutation is multiplied to form identity permuatation"""
    order = 2
    circ = circlfunc(a,a)
    while True:
        if ifidentity(circ):
            return order
        else:
            circ= circlfunc(a,circ)
            order = order+1


x=[3,1,2]
print(order(x))


def circnot(a):
    """This function is to denote a given permutation as circular notation"""
    sample =[]
    


