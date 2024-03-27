n=int(input())
x=int(input())
y=int(input())
l=input().split(" ")
for i in range(len(l)):
    l[i]=int(l[i])
l.sort()
#print(l)
i=0
s=0
while(s<=(i+1)*y and i<len(l)):
    s=s+l[i]*x
    if s>(i+1)*y:
        break
    i=i+1
    
#    print(s)
print(i)
