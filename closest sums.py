n=int(input())

l=[]
for i in range(n):
    x=int(input())
    l.append(x)

m=int(input())
#print(m)
s=[]
c=0
for i in l:
    s.append(i)
    c=i
    for j in l:
        if(i!=j):
            c=i+j
            s.append(c)

case=0
p=[]
d=0
q=[0]
g=[]
while(True):
    
    if(p==q):
        for i in range(m):
            b=int(input())
        
        
    else:
        
        q=[]
        for i in range(m):
            try:
                y=int(input())
            except:
                quit()
            q.append(y)
        if(g!=q):
            case=case+1
            print("Case ",case,":",sep="")
            for i in q:
                m=10000000
                for j in s:
                    if(abs(j-i)<m):
                        m=abs(j-i)
                        d=j
                print("Closest sum to ",i," is ",d,".",sep="")
            g=q
        
    m=int(input())
    
            
     
    
