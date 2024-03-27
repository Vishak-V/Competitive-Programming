l=input()
a=input()
b=input()
l=l.split()
a=a.split()
b=b.split()
for i in range(0,len(a)):
    a[i]=int(a[i])
for i in range(0,len(b)):
    b[i]=int(b[i])               

n=l[0]
q=l[1]
MOD=l[2]
n=int(n)
q=int(q)
MOD=int(MOD)
def fib(a):
    if a==1 or a==2:
        return 1
    else:
        p=fib(a-1)+fib(a-2)
        return p
    

def fib_add(x,y):
    c=1
    for i in range(x[0],x[1]+1):
        y[i-1]=y[i-1]+fib(c)
        c=c+1
    return y
def mod(n,mod):
    while n>=mod:
        n=n-mod
    return n    
def mod_l(l,x):
    for i in range(0,len(l)):
        l[i]=mod(l[i],x)
    return l    
           
while True:
     z=input()
     z=z.split()
     if z==[]:
         break
     if z[0]=="A":
         fib_add([int(z[1]),int(z[2])],a)
         a=mod_l(a,MOD)
     else:
         fib_add([int(z[1]),int(z[2])],b)
         b=mod_l(b,MOD)
     if a==b:
         print("YES")
     else:
         print("NO")
        
    
    
    

