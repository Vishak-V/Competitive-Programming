n=int(input())
v=[]
for i in range(n):
    x=int(input())
    l=list(map(int,input().split(' ')))
    v=[]
    for i in range(0,len(l)):
        if (v.count(l[i]%10)<3):
            v.append(l[i]%10)
    v.sort()
    #print(l)
    #print(v)
    br=0
    for q in range(len(v)):
        if br==1:
            break
        for j in range(1,len(v)):
            if br==1:
                break
            for k in range(2,len(v)):
                
                if(q!=j and q!=k and j!=k):
                    if((v[q]+v[j]+v[k])%10==3):
                        br=1
                        break
                        
                        
                            
    if (br==0):
        print("NO")
    else:
        print("YES")
    
