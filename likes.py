n=int(input())
for i in range(n):
    x=int(input())
    m=list(map(int,input().split(" ")))
    l=m
    m.sort(reverse=True)
    c=0
    n=0
    p=0
    for i in m:
        if(i>0):
            c=c+1
            p=p+1
            print(c,end=" ")
        if(i<0):
            c=c-1
            print(c,end=" ")
            n=n+1
    q=n
    print()
    for i in range(q):
        if(p>0 and n>0):
            print("1 0",end=" ")
            p=p-1
            n=n-1
    r=0
    for i in range(p):
        r=r+1
        print(r,end=" ")
        
    print()
        
            
    #print(l)

    
