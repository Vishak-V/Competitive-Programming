l=eval(input())
k=int(input())
i=0
n=len(l)-1
l.sort()
x=0
while i<n:
    if l[i]+l[n]==k:
        x=x+1
        i=i+1
    elif l[i]+l[n]>k:
        n=n-1
    elif l[i]+l[n]<k:
        i=i+1
        
print(x)
