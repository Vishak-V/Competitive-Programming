n=int(input())
for i in range(n):
    n=0
    w=0
    e=0
    s=0
    cord=[0,0]
    prev=[[0,0]]
    time=0
    l=list(input())
    for i in range(len(l)):
        if(l[i]=='N'):
            n=n+1
            cord[0]+=1
            time+=5
        if(l[i]=='S'):
            s=s+1
            cord[0]
            time+=5
        if(l[i]=='E'):
            e=e+1
            time+=5
        if(l[i]=='W'):
            w=w+1
            time+=5
        if((n==s and e==w) or (e==w and (n!=0 and s!=0)) or (n==s and (e!=0 and w!=0))):
            total=n+w+e+s
            n=0
            w=0
            e=0
            s=0
            j=i-total
            k=i
            while(l[j]==l[k]):
                time=time-4
                j=j+1
                k=k+1
                
                
            
            
            
            
        
