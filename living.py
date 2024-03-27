n=int(input())
for i in range(n+1):
    x=int(input())
    c=x
    i=0
    
    while(i<x):
        if('4' in str(x)):
            s=str(x)
            c=c+10**(len(s)-l.index('4')-1)
            i=i+10**(len(s)-l.index('4')-1)
        else:
            c=c+1
            i=i+1
    print(c)
