n=int(input())
for i in range(n):
    q=int(input())
    l=list(map(int,input().split(" ")))
    s=0
    for i in range(1,len(l)):
        if(l[i]==0):
            s=s+max(l[:i])
            l[l.index(max(l[:i]))]=0
    print(s)
            
