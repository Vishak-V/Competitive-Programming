x=int(input())
l=[]
for i in range(x):
    l.append(int(input()))
m=max(l)
l.sort(reverse=True)
c=0
sl=0
sr=0
r=0
j=0
k=0;
#print(l)
while (j<len(l)):
    for k in range(j,len(l)):
        sr=sr+l[k]
        #print(sr)
        if(sr>=sl):
            sr=0
            j=k
            r=j
            if(k==len(l)-1):
                print(r+1)
                quit()
            break
        if(k==len(l)-1):
                print(r+1)
                quit()
        
    sl=sum(l[0:j+1])
    j=j+1      
        

        
        
