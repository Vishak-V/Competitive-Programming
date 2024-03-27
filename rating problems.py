l=list(map(int,input().split(" ")))
n=l[0]
k=l[1]
M=[-3]*n
m=[3]*n
for i in range(k):
    x=int(input())
    M[i]=x
    m[i]=x
print(sum(M)/n,sum(m)/n,sep=" ")
