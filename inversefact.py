import math
st=input()
#print(st)
l=list(st)
s=len(l)
c=0
n=0
if(st=='1'):
    print(1)
    quit()
elif(st=='6'):
    print(3)
    quit()
elif(st=="2"):
    print(2)
    quit()
elif(st=="24"):
    print(4)
    quit()    
else:    
    while (s>math.ceil(c)):
        n=n+1
        c=c+math.log(n,10)
        
    print(n)    
