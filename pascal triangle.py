l=int(input())
print(1)
print(1,1)
x=[0,1,1,0]
y=[]
n=0
for i in range(0,l-2):
    y=[]
    
    for j in range(0,len(x)-1):
        n=x[j]+x[j+1]
        y.append(n)
        
    print(y)
    y.append(0)
    y=[0]+y
    x=y

    
    
    
    
    
