n=int(input())
l=[]
for i in range(n):
    x=int(input())
    l.append(x)
c=0
br=0
for i in range(1,201):
    if(i<l[c]):
        print(i)
        br=1
    else:
        c=c+1
        if (c>=n):
            break
        
if (br==0):
    print("good job")
