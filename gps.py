import math
l=list(map(int,input().split(" ")))
n=l[0]
t=l[1]
l=list(range(n))
for i in range(n):
    x=list(map(int,input().split(" ")))
    l[i]=x
dist=0
for i in range(1,len(l)):
    dist=dist+(((l[i][0]-l[i-1][0])**2)+((l[i][1]-l[i-1][1])**2)**(1/2))
    #print(dist)
               
               
