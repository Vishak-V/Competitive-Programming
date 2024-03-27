
d=1
x=int(input())
while(x!=0):
    d=1
    for j in range(x+1):
        print(d)
        if(j==0):
            d=1
        else:
            d=d*j
            while(d%10000000==0):
                d=int(d/10000000)
            d=d%10000000
    while(d%10==0):
        d=int(d/10)
    print(d%10)
    print("----")
    x=int(input())
            
