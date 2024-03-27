def fparent(a,b,c):
    if a==b and a==1:
        return []
    if a>b:
        return fparent(a-b,b,c+1)+['L']
        c=c+1
    if a<b:
        return fparent(a,b-a,c+1)+['R']

n=int(input())
for i in range(n):
    l=input().split(" ")
    x=int(l[0])
    y=l[1].split("/")
    a=int(y[0])
    b=int(y[1])
    q=fparent(a,b,0)
    if q==[]:
        print(x,1,sep=" ")
        
    else:
        q=q[::-1]
        t=2**(len(q)+1)-1
        for i in range(len(q)):
            if q[i]=='R':
                t=t-2**(i)
                
                
                
        print(x,t,sep=" ")
          
