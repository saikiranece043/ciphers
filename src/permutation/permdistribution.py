import itertools
import math
import prettytable as p
size = 7
totalcount =0
involutary = []

t = p.PrettyTable(['Structure', 'Count', 'Order'])

def countperms(perm):
    #print(perm)
    a = math.factorial(size) / math.factorial(size - sum(perm))
    b = 1
    uniq =[]
    c =1
    for i in perm:
        if i not in uniq:
            uniq.append(i)
        b = b*i
    for i in uniq:
        c = c * perm.count(i)
    return (a / b) / math.factorial(c)


def getlcm(a):
    '''returns the lcm for a given array of numbers'''
    lcm =a[0]
    for i in a[1:]:
        lcm = (lcm *i) // (math.gcd(lcm,i))
    return lcm


def findperms(size):
    perms =[]
    for x in itertools.product(list(range(0, size+1)), repeat=size+1):
        if sum(x) == size:
            y = list(x)
            y[:] = (value for value in y if value != 0)
            y.sort()
            if y not in perms:
                perms.append(y)
    return perms

perms = findperms(size)

for idx,perm in enumerate(perms):
    perm[:] = (value for value in perm if value !=1)

    if len(perm)!=0:
        lcm=getlcm(perm)
        if lcm == 2:
            involutary.append(perm)
        count=countperms(perm)
        totalcount = totalcount +count
        t.add_row([ perm, count , lcm])
        #print("Structure %s : Count %d : Order %d"%(perm,count,lcm))



totalperms = math.factorial(size)
print("Total count : %d total number of possible perms count %d" %(totalcount+1,totalperms))



print("Involutory perms group ",involutary)

print(t)