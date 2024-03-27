import math
n=int(input())
for i in range(n):
    m=int(input())
    x=0
    y=0
    for j in range(m):
        l=list(map(float,input().split()))
        
        theta=l[0]*(math.pi/180)
        d=l[1]
        x=x+math.cos(theta)*d
        #print(x)
        y=y+math.sin(theta)*d

    print(x,y)
        
