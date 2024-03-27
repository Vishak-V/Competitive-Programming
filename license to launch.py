n=int(input())
x=input()
x=x.split(" ")
t=int(x[0])
for i in range(0,n):
    if t>int(x[i]):
        t=int(x[i])
        c=i
    
    
print(c)
    
