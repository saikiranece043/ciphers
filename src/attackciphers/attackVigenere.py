import prettytable as p
import matplotlib.pyplot as plt

r=p.PrettyTable(['character','ascii value','probability'])

def findpdf(text,m=256):

    count =[0] * (m)
    x =[]
    y =[]

    for c in text:
        if  ord(c) < 257:
            count[ord(c)]= count[ord(c)]+1

    return count


def plot(x,y):
    plt.bar(x,y)
    plt.show(block=False)



def compareshift(x1,x2):
    if x1==x2:
        return 1
    return 0

def getioc(ciphertext,shifts,m=256):
    n =len(ciphertext)
    n=10000
    ioc =[0]
    # we are going to calculate for number of shifts the summation
    for s in range(1,shifts+1):
        sum =0
        # we are going to sum (n-i) times
        for loc in range(1,n-s+1):
            sum = sum + compareshift(ciphertext[loc],(ciphertext[loc+s]))

        sum = sum/ (n - s)
        ioc.append(sum)
    return ioc





