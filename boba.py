n=int(input())
x=list(map(int,input().split()))
#print(x)
m=int(input())
y=list(map(int,input().split()))
l=[]
for i in range(n):
    l.append(list(map(int,input().split())))

a=int(input())
z=1000000000000
for i in range(n):
    for j in range(m):
        for k in l[i][1:]:
            if(x[i]+y[k-1]<z):
                z=x[i]+y[k-1]
            


print(z)
c=-1
while(a>=z):
    a=a-z
    c=c+1
print(c)
