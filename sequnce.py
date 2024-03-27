n=int(input())
for i in range(n):
    x=int(input())
    
    y=0
    c=0
    while(x>0):
        y=y+10**(c)*y%9
        x=int(x/9)
        c=c+1
        print(y)
