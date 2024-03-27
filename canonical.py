n=int(input())
l=list(map(int,input().split(" ")))
br=0;
for i in range(1,len(l)):
    if(l[i]%l[1]==0):
        continue
    else:
        br=1
        break
        
if (br==1):
    print("non-cannonical")
else:
    print("canonical")
