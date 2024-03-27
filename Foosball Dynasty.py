n=int(input())
l=list(map(str,input().split(' ')))

m=list(input())
#print(m)
w=[l[0],l[2]]
b=[l[1],l[3]]
l=l[4:]
#print(l)
target=[]
dl=1
teams=[]
index=[0]
q=0
for r in range(1,len(m)):
    if m[r-1]==m[r]:
        dl=dl+1
        #print("test")
    else:
        if dl>q:
            q=dl
            
            index=[]
            index=index+[r-dl]
        elif dl==q:
            index=index+[r-dl]
        
        #print(index)
        #print(r)
        #print(r-dl)
        dl=1

        
        
    
for i in range(len(m)):
    
    if m[i]=='W':
        teams.append(w)
        w=w[::-1]
        l.append(b[1])
        b[1]=b[0]
        b[0]=l.pop(0)
        
    else:
        teams.append(b)
        b=b[::-1]
        l.append(w[1])
        w[1]=w[0]
        w[0]=l.pop(0)
#print(teams)
for t in index:
        target.append(teams[t])
for j in target:
    for k in j:
        print(k,end=" ")
    print()
        

