n=int(input())
l=list(map(int,input().split(" ")))
l.sort()
#print(l)
i=0
if len(l)==1:
    print("N")
    quit()
c=0
br=0
m=max(l)
x=[0]*(m+1)
for j in l:
    x[j]=x[j]+1
    
#print(x)        

for i in range(len(x)-1):
    if(x[i]>1):
        r=int(x[i]/2)
        x[i]=x[i]%2
        x[i+1]=x[i+1]+r
print(x)
x=[x for x in x if x!=0]
print(x)
if(len(x)<3):
    print("Y")
else:
    print("N")
