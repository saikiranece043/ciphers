import math
import prettytable as p

r = p.PrettyTable(['Permutation size','Number of involutory keys','Total Number of keys'])
def count(size,num):
    a=  1/ math.factorial(num)
    b = 1/ math.pow(2,num)
    c = math.factorial(size)/ math.factorial(size - 2*num)
    return a*b*c

def countinvkeys(size):
    sum =0
    for i in range(1,math.floor(size/2)+1):
        sum = sum + count(size,i)
    return sum



for i in [2,3,4,5,6]:
    totalkeys = math.factorial(i)
    invkeys = countinvkeys(i)
    r.add_row([i,invkeys, totalkeys])



print(r)
