n=int(input())
l=input()
l=l.split(" ")
for i in range(0,len(l)):
    l[i]=int(l[i])

br=max(l)-min(l)
#print(br)
i=0
x=l[0]
m=0
k=0
while(i<=br/2):
    x=l[0]
    c=1
    for j in range(1,len(l)):
        #print(x)
        if(l[j]>l[j-1]):
            x=x+i
        elif(l[j]<l[j-1]):
            x=x-i
        if(l[j]==x):
            c=c+1
    if(c>=m):
        m=c
        k=i
    if(c>len(l)/2):
        break
    
    i=i+1    
print(m)
print(k)
