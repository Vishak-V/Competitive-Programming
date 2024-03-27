def decrypt(x):
    if x<26:
        return chr(ord('A')+x)
    elif x<=35:
        return chr(35-x)
    else:
        return ' '
    
def multiply(m,l2):
    l=0
    s=0
    for i in range(len(m)):
        s=s+m[i]*l2[i]
        l=s%37
    return l  
            
n=int(input())
m=[[] for i in range(n)]
for i in range(n):
    m[i]=list(map(int,input().split()))
l=list(input())
print(l)
c=0
v=[36]*n
j=0
k=0
while j<len(l):
    while k<n:
        if(l[j].isalpha()):
            c=ord(l[j])-ord('A')
        elif(l[j].isdigit()):
            c=int(l[j])+26
        v[k]=c
        j=j+1
    print(v)
    k=k+1
    if k==3:
        k=0
    
    
    for i in v:
        v1=multiply(m[k],v)
        print(decrypt(v1))
    v=[36]*n    





            
        
        
    
