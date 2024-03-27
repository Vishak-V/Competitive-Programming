import math
def dist(x1,y1,x2,y2):
    return math.sqrt((x1-x2)**2+(y1-y2)**2)

s=input().split(" ")+input().split(" ")+input().split(" ")
#print(s)
for i in range(9):
    
    s[i]=int(s[i])
l=[]
for i in range(9):
    l.append((s[i],i%3,int(i/3)))

l.sort()
#print(l)
d=0
for i in range(len(l)-1):
    d+=dist(l[i][1],l[i][2],l[i+1][1],l[i+1][2])
print(d)
