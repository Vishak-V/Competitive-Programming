n=int(input())
for i in range(n+1):
    x=int(input())
    c=0
    while(x>0):
        if('4' not in str(x)):
            x=x-1
            c=c+1
        else:
            l=str(x)
            
            c=c+1+10**(len(l)-l.index('4')-1)
            x=x-10**(len(l)-l.index('4')-1)
    print(c)
        
