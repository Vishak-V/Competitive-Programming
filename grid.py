import math
def dist(x1,y1,x2,y2):
    return math.sqrt((x1-x2)**2+(y1-y2)**2)

l=[]
for i in range(9):
    l.append([i%3,int(i/3)])
#print(l)
s=input().split(" ")+input().split(" ")+input().split(" ")
#print(s)
for i in range(9):
    
    s[i]=int(s[i])
    
#print(s)
su=0
for i in range(1,9):
    su+=dist(l[s[i]-1][0],l[s[i]-1][1],l[s[i-1]-1][0],l[s[i-1]-1][1])
    
print(su)
