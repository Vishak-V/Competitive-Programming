n=list(map(int,input().split(' ')))
l=list(map(int,input().split(' ')))
for i in range(n[2]):
    s=set()
    c=0
    x=list(map(int,input().split(' ')))
    temp=l[x[0]-1:x[1]]
    temp_s=set(temp)
    temp_s=list(temp_s)
    #print(temp_s)
    j=0
    while j<len(temp_s):
        if(temp.count(temp_s[j])%2==0):
           pass
        else:
            s.add(temp_s[j])
            c=c+1
            if(c>1):
                break

            
        j=j+1    
            
    p=list(s)
    if(c==1):
        print(p[0])
    else:
        print(0)
