s=input()
n=0
x=[]
for i in range(len(s)):
    x=set()
    for j in range(i+1,len(s)):
        if((s[j] not in x) and s[j]!=s[i]):
            n=n+1
        if(s[j]!=s[i]):
            x.add(s[j])
        else:
            break
        
        
        
            
print(n)            
