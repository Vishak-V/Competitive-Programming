n=int(input())
l=input()
l=l.split(" ")
print(l)
for i in range(0,len(l)):
    l[i]=int(l[i])
print(l)    
def rec(x):
        if len(x)==1:
            return x[0]
        else:
            
            y=x[0]
            p=x.pop(0)
            j=y+1/rec(x)
        
            return j

print(rec(l))        
        
    
    
