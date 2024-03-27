n=int(input())
for i in range(n):
    l=list(map(int,input().split(" ")))
    l[0]=0
    for z in range(1,len(l)-1):
        if(l[z]<l[z-1]):
            print(z)
            break
        if(l[z]>l[z+1] and l[z-1]<l[z+1]):
            
            print(z)
            break
        
            
        
        
