l=list(map(int,input().split()))
s=0
prod=1

k=[2,3,5,7,11,13,17,19]
for i in range(0,len(l)):
    if l[i]<k[i]-1:
        s=s+(k[i]-l[i]-1)*(prod)
    prod=prod*k[i]
print(s)
