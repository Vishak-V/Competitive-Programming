import math

P = [2,3]

def np():
    n = P[-1]
    while 1:
        n += 2
        br = True
        sq = int(n**0.5)+1
        for pm in P:
            if pm >= sq:
                break
            if not (n/pm)%1:
                br = False
                break
        if br:
            return(n)

def pf(x):
    n = x
    PL = []
    ind = 0
    while 1:
        if ind == len(P):
            P.append(np())
        p = P[ind]
        c = 0
        while not (n/p)%1:
            n //= p 
            c += 1
        if c:
            PL.append((p,c))
        if n == 1:
            return(PL)
        ind += 1

def facs(L):
    v = L[0][0]
    if len(L) == 1:
        return([v**i for i in range(L[0][1]+1)])
    else:
        NL = []
        for i in range(L[0][1]+1):
            NL = NL+[(v**i)*x for x in facs(L[1:])]
        return(sorted(NL))

def factors(x):
    return(facs(pf(x)))

n=int(input())
l=[]
for i in range(n):
    l.append(int(input()))
m=min(l)
for i in range(len(l)):
    l[i]=l[i]-m
g=math.gcd(l[0],l[1])    
for i in range(len(l)):
    g=math.gcd(g,l[i])

'''for i in range(2,g+1):
    if(g%i==0):
        print(i,end=" ")'''
f=factors(g)

for i in range(1,len(f)):
    print(f[i],end=" ")

