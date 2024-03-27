x=1
y=1
l=[]

while x<1000000:
    while y<1000000:
        s=2*(x**2)+y**2
        l.append(s)
        y=y+1
    x=x+1    

if len(l) == len(set(l)):
        print("yes")
    
    
