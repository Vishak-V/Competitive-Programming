n=int(input())
l=list(map(int,input().split(" ")))
i=1
s=0
ans=0
def sumn(l,i,j):
    s=0
    x=l[i]
    
    while i-1>=j:
        s=s+x-l[i-1]
        i=i-1
    return s
j=0
while i < len(l):
    if s<20:
        s=s+sumn(l,i,j)
        
    if s>=20:
        ans=ans+1
        s=0
        j=i
    i=i+1
print(ans+1)
        
        
    
