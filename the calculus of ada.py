l=list(map(int,input().split(' ')))
s=l[1:]
d=[]
degree=0
q=[]
while True:
    d=[]
    degree=degree+1
    for i in range(1,len(s)):
        d=d+[s[i]-s[i-1]]
    q=q+[d[-1]]
    if len(set(d))==1:
        break
    s=d
#print(q)
#print(sum(q))
print(degree, end=" ")
print(l[-1]+sum(q))
