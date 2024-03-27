k=int(input())
l1=list(input())
l2=list(input())
s=0
for i in range(len(l1)):
    if l1[i]==l2[i]:
        s=s+1
d=len(l1)-s
ans=0
if k>=s:
    ans=ans+s


if len(l1)-k>=d:
    ans=ans+d
else:
    ans=len(l1)-k

print(ans)
    
