import math
n=int(input())
def solve(k,m,r):
    if k==1:
        return int(m*(m+1)/2)
    if m==r:
        return m
    
    q=math.ceil(((m-r)/k)*(k-1))+r
    return q+solve(k,m,q)

for i in range(n):
    l=list(map(int,input().split(" ")))
    print(l[0],l[1])
    print(solve(l[0],l[1],0))
    
    
