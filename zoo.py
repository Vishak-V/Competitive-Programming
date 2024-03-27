x=int(input())
l=[]
for i in range(x):
    l.append(int(input()))
m=max(l)
l.sort(reverse=True)
j=1
s=0
#print(l)
while (s<m and j<len(l)):
    s=s+l[j]
    j=j+1
j=j-1    
if(j==len(l)-1):
    print(1)
else:    
    print(j+1)    

    
