n=input().split(" ")
x=int(n[0])
y=int(n[1])
for i in range(x):
    for j in range(x*4+2):
        if(j==x-i-1 or j==2*x+2+x-i-1):
            print("/",end="")
        elif (j==x+i or j==2*x+2+x+i):
            print("\\",end="")
        else:
            if(i==x-1 and ((j>x-i-1 and j<x+i) or ( j>2*x+2+x-i-1 and j<2*x+2+x+i))):
                print("_",end="")
            else:
                print(" ",end="")
    print()
for i in range(x*4+2)"
    print(" ",end="")
i=0
j=0

while j<x*4+2:
    if(j<x*2-y+1 or j>x*2+y-1):
        print(" ",end="")
    else:
        print("\\/",end="")
        j=j+1
    j=j+1    
print()
j=0
while j<x*4+2:
    if(j<x*2-y+1 or j>x*2+y-1):
        print(" ",end="")
    else:
        print("/\\",end="")
        j=j+1
    j=j+1    
#print()
    
