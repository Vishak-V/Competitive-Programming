l=list(map(int,input().split(" ")))
p=l[0]
d=l[1]
l=[]
for i in range(p):
    x=list(map(int,input().split(" ")))
    l.append(x)

l.sort()
#print(l)
a=[]
b=[]
q=0
for i in range(1,d+1):
    sa=0
    sb=0
    wa=0
    wb=0
    v=0
    for j in l:
        if i==j[0]:
            sa=sa+j[1]
            sb=sb+j[2]
            v=v+j[1]+j[2]
            q=q+j[1]+j[2]
    if sa>sb:
        print("A",end=" ")
        print(sa-int(v/2)-1, end=" ")
        a.append(sa-int(v/2)-1)
        print(sb)
        b.append(sb)
        
    else:
        print("B",end=" ")
        print(sa,end=" ")
        a.append(sa)
        print(sb-int(v/2)-1)
        b.append(sb-int(v/2)-1)
        
print(abs(sum(a)-sum(b))/q)      
        
            
    
